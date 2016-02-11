title: libusb, libftdi, latency, and my own stupidity
date: 2008-04-29 22:01:51 

When last we left off, I had an OpenGL kinematics simulator for my current OCD fulfillment object, the Novint Falcon. I'll get to the math behind all that in the next post, but for right now, suffice to say, it just works. The kinematics loops can easily hit 40000 iterations per second, which is more than enough for my first few basic projects, including mouse control. However, that really only mattered on windows, because when I finished the simulator, windows still had a 1000hz update rate, while linux and os x were still running at 70-150hz update rate on a good day with the wind going in the right direction. I spent last week trying to get linux and mac up to the same speed as windows. What follows is the story of that week.

But first off, let's rewind to August of last year. Before Novint put out their own SDK, I was bound and determined to get my own out, just because it seemed like a fun challenge. I managed to document out the firmware download process, but not completely replicate it. My first program worked by starting up one of their test programs to load firmware, then using my own code after that to communicate with the falcon. The hack ended up being successful, if ridiculously unsafe to look at in a normal workplace. The video of the results are NSFW:

http://www.youtube.com/watch?v=EfrMalBiXuY 

Anyways, while doing this, I took some notes on the startup sequence for firmware loading. Here's a picture of those notes:

[![Comm Trace notes for the Novint Falcon][1]][2]

Now, fast forward back to last week. Time to make everything equally fast.

To start, how the falcon communicates. Using the test firmware that came with the disc in the falcon box (currently the only thing I have mapped, and I honestly don't even know if there's other firmware out there), it receives 16 bytes input, and upon receiving that, gives back 16 bytes as output (it's actually 18 bytes, due to ftdi modem status being tacked on the front, but those are negliable). That's it.

Let's look at the stats that test programs were putting out for each platform (thanks to people on the libnifalcon-devel list for helping out on this):

Linux:

Time between I/O Iterations: 0.015991s

Average Frequency: 62.534351 per second

Windows:

Time between I/O Iterations: 0.000942s

Average Frequency: 980.382853 per second

Yeah. Bit of a difference, eh? So something was causing I/O iterations on linux to take around 16ms each, while on windows, we were getting 1 iteration per millisecond, and achieving near the 1khz that's mentioned by Novint all the time. This is running on the EXACT same code, up to the point of the FTDI library being used. The Windows version was using the ftd2xx drivers, while linux was using libftdi. ftd2xx on linux seemed to run decently fast, though I don't have the number handy at the moment.

Now, I'd read a few things around the net about libftdi being ridiculously slow, mostly in terms of bitbanging though. Either way, I figured it was something in either libftdi or libusb that was causing the slowdown. Rebuilt everything with -gp and let gprof at it for a while, just to see that, nope, it was just sitting there waiting during the I/O loop, for 16ms at a time.

At this point, I start wondering if it's not the synchronousity of libusb-0.1 that's slowing me down. Luckily, [libusb-1.0 is in development right now, which enable asynchronous transfers for usb][3]. Pulled the dev branch of that, tried it out. Asynchronous sends, writes are superfast, reads... 16ms.

Damnit.

So, something in the read is taking 16ms. It's time to start playing with our read transfer and see what else we can change. First off, changing the read request size to 64 bytes, the maximum packet size for the endpoint.

Time between I/O Iterations: 0.000919s

Well, that made something happy. The problem there is, we're now sending 1000 input packets, and only getting back ~250 output packets. This means that there was something I was missing about sub-maximal packet sizes. 

Much googling insues. No information found. Finally out of frustration, I just google "ftdi 64 bytes".

[And I find the FTDI Addendum on Data Throughput, Latency, and Handshaking for the FT232 Series Chips][4] (PDF)

There it is, clear as day. There's a latency timer on the chip that will send bytes to the host assuming one of three conditions:

  * A serial status line (DTR, RTS, etc...) is flipped
  * The buffer reaches maximum capacity (Thus our results with the 64 bytes
  * The latency timer overflows

We're obviously not playing with the first one. The second one we've seen the effects of, but we don't want to have to wait for 62 user bytes at a time. 

What's the default starting value of the latency timer?

16ms.

If you scroll back up and look at my notes again, you'll see there's a line there that says "0x9 (latency timer?) 0x1". This was a control message sent over by the Falcon test program. 0x9 is the control message index, and 0x1 is the value. They set the latency timer to 1ms during the initialization stage. I totally skipped over that when transcribing the code for the initialization sequence, and it meant I was sitting on slow code for many, many months.

I added that single line of code to the libusb-0.1.12/libftdi based libnifalcon libraries.

Time between I/O Iterations: 0.002019s

Yyyaaaaaayyyyyyyy!!waitaminute. 2 ms?

And thus, the synchronous call issue comes back to bite me in the ass, except this time, it's actually a correct diagnosis. 

You see, when you send a USB message, it's packed into a USB frame. Each USB frame can carry multiple messages, but at a rate of 1 frame per millisecond (we're at USB 2.0 fullspeed here). libusb-0.1.12 only packs one request per frame, so we have 1ms input, 1ms output. 2ms overall, locking our I/O loop to 500hz. DAMNIT.

So, the solution to this is to either figure out a way to get both input and output in the same frame, which may be possible with libusb-1.0. That remains to be seen, and that code is still very, very alpha. I'll keep working with it, though.

Anyways, this still leaves a couple of questions. First off, when I was checking the ftd2xx drivers for linux, I decided to check their symbol table for the dynamic library...

...
    
    
    
    
             U time
    
    
    
    
             U tolower
    
    
    
    
             U toupper
    
    
    
    
    00013673 T usb_bulk_read
    
    
    
    
    0001357d T usb_bulk_write
    
    
    
    
    00017d30 B usb_busses
    
    
    
    
    000132ff T usb_claim_interface
    
    
    
    
    00014309 T usb_clear_halt
    
    
    
    
    000120e6 T usb_close
    
    
    

...

HEY! Those are libusb calls! So ftd2xx is at least partially based on libusb. How they're managing the superfast I/O, I'm not sure. Could be threading, could be they've got their own asynch thing going on.

Secondly, I obviously didn't have the latency timer set on the ftd2xx version of the drivers, either. Why did my drivers run so fast on windows without that? I'm guessing there could be a config file I was missing somewhere, or maybe their drivers just do it themselves on connection or something.

Anyways, the moral of the story: Read the god damn spec sheet. And all the addendums. And pay attention to your own notes. 

   [1]: https://farm3.static.flickr.com/2030/2446569720_27520421f3.jpg
   [2]: https://www.flickr.com/photos/qdot76367/2446569720/ (Comm Trace notes for the Novint Falcon by qdot76367, on Flickr)
   [3]: http://libusb.wiki.sourceforge.net/Libusb1.0
   [4]: http://www.ftdichip.com/Documents/AppNotes/AN232B-04_DataLatencyFlow.pdf

