--- 
title: Everything I Know About the Novint Falcon as of March 2008
date: 2008-03-25 22:53:59 -07:00
mt_id: 1174
layout: post
---

**Update**: libnifalcon is still alive and kicking. The new url for it is [http://libnifalcon.nonpolynomial.com][26]. All of the up to date information can be found there.

---

After [my article on the Novint Falcon box][1] got linked by [GameSetWatch][2] and [Ars Technica][3], it seems like it might be time to do a nice, technical throwdown about what's going on, inside and out of the novint falcon, since everyone else seems hung up on games usage (I guess it's a game controller, but that's not the fun part!). I've been working with the Falcon since early August, and am actually getting fairly far with it.

If you didn't understand my box article, read on anyways. I'm gonna try to make this as understandable to everyone as possible, so you'll all learn C and inverse kinematics and algebraic geometry and come romp with me down the happy streets of writing a driver for a badly marketed piece of hardware no one is buying. 

Come on, what other relaxing hobbies do you have that involve Jacobian Matrices, hmmmmm?

Please note: I have not used Novint's SDK. I do not plan on using Novint's SDK (That would be cheating). I don't know what their developer support is like (though Tom seems nice enough on the forums. Hi Tom!). What you see here is what I've gained from lots of web searching, talking to people that know what they're doing (I'm not a haptics engineer, in fact, this is my project to learn haptics engineering and programming), and randomly trying things while hoping I don't break the falcon. I'll wikify all of this information in time, but it's honestly much faster for me to brain dump in conversational blog mode than it is into a wiki. 

**So what the God Damn Hell is the Falcon anyways?!?!**

It's everyone's favorite time of class, video time! _*wheels in the TV with bad color and hissing, blinking 12:00 VCR*_

Seriously. I can't figure out how to explain it. Novint can't figure out how to explain it. So, watch this video, which tries to explain it.

If you don't understand what it is yet, well, I can't help you anymore. But enjoy this randomly technical description that follows anyways. I worked hard on it, and I did it **JUST FOR YOU**. Yes, _you_.

**A Little Background on Parallel Robots and Haptic Controllers**

Before we dig into the guts, let's start with what you can find out before you take the case off the thing. For reference, here's a picture of the Falcon:

![][4]

A bit of background (this will contain much glossing as I'd like to focus on the falcon, but it's good to have a knowledge of what's out there otherwise). In the world of haptics, there are two major types of controllers. Serial (pen type controllers), and parallel. [An overview of a bunch of the different hardware types is available in an article on bracina.com][5]. 

The NovInt Falcon is a [parallel robot][6]. [Parallel robots][7] are called such because they have multiple chains of joints working together to create the final position of the controller (or end effector, if you want to be technical about it). Not to mention, the math uses parallelograms to line up the positions. 

If you watch a lot of How It Works (which, if you have cable with the Discovery Channel, you invariably end up doing no matter what. That show is video heroin.), you've seen these before. 

![][8]

They're real popular in pick and place operations. That's exactly what it sounds like. Pick something up, put it somewhere else. Repeat ad inifinitum. Puttin' things in or on other things. They're good at that. 

Here's one in action.

So, you're probably like "But it's all pointing down"

![][9]

Ok, look more familiar now? The NovInt Falcon is a parallel robot _turned on its side_. It's actually a Delta variant of the parallel manipulator ([Here's a nice overview of the Delta Haptic Device, which is quite similar to the Falcon/Omega setup][10]). If you want all sorts of interesting history about where it came from, [check out this article on parallemics.org][11]. But for now, we'll just say: France. It came from France.

There's lots of reasons why using parallel robots in haptics is important. However, I don't quite understand the math behind it all yet, so I'll just repeat what all the webpages say. "Good stiffness and accuracy in a small workspace". Having used some serial controllers before, I can see what they mean. Hard definitely feels... hard. I'm sure I'll be talking more about this in later articles on the development of [libnifalcon][12].

To show a bit of what else is out there, here's the [ForceDimension and their Omega series of controllers][13].

![][14]

Once again, looks familiar, no?

Well, one major difference.

The Falcon is $249US.

The Omega starts at around $20,000US (the more degrees of freedom, the more expensive. The Omega 7 is around $50k.)

Ok, and the Omega comes with a PCI interface and all sorts of APIs and what not and FD is actually an offshoot of the subset of France that we mentioned above that created this whole thing in the first place, but still. That's some significant 0's worth of difference there.

There's rumors that ForceDimension helped out on the Falcon design. There's also rumors that it came from Sandia with Tom. Only Art Bell truly knows.

So why all this about parallel robots? Well, many future posts will be talking about research in this field, so I figured I'd at least introduce the term. There's also lots of reference and searchable material in here if you're interested in going your own direction with this information. Anyways, back to hackyness.

**Internal Circuitry**

Now that we've got that out of the way, what's inside it?

Click the image below to go to an annotated flickr picture of the insides. 

[![The Inside of the Falcon][15]][16]

Connectors:

* USB B Connector
* Power Connector - goes to 30V 1A wall wart of DOOM

Yes, the falcon is quite possibly cranking 30W through the motors when you max the torque on all the axes.

Chips (Links to Datasheets or Product Websites):

* [FTDI FT232R][17] USB to Serial Chip
* [PIC 16F688 Microcontroller][18]
* [TI TMS320 R2811][19] DSP Processor

I don't have specific parts on the 3 motor blocks in the circuit (they're all exactly the same), but what you've basically got going on there is three really large old style mouse encoders. Each of the 3 large wheels attached to the motors have a disc attached to them, alternating little clear slots with opaque slots. There's a photoresistor that shines light through those slots. Whenever the light goes through (clear), you get a 1. Whenever the light is blocked (opaque), you get a zero. And that's how we know how far the motor has gone. 

Whether direction is measured using some sort of quadrature encoding or Back-EMF polarity is something I forgot to check (but will do so at the point where I can figure out how to write my own firmware for this thing).

**Communications and Initialization/Bootloading Sequence**

Now, for the part I kinda sorta know more about than the other parts. 

The Falcon uses the FTDI chip as it's main communications link to the computer. Everything is filtered back and forth through the FTDI chip, converting from USB on the computer side to RS232 on the circuit side. This is because it's orders of magnitude easier to program your microcontrollers to talk RS232 than it is to talk USB. 

Novint distributes and uses the stock FTDI driver with their software. The only change they've made is to the VID and PID. They've chosen to use [FTDI's free "have a PID" program][20], which has them listed under FTDI (0x0403) as a vendor, but with their own special product ID (0xcb48, as opposed to the default PID for FTDI chips, 0x6001).

_NOTE: I have not actually proven this next paragraph, it's more what I think is going on than anything._ You might've noticed in the Internal Circuitry section that there are two microcontrollers on the board: the PIC and the TI. This is where the bootloader sequence comes in. The TI DSP uC is actually reconfigurable on connection to a PC. The PIC acts as a bootloader, maintaining the logic needed to run the FTDI communications to pick up firmware and program the TI with it. This allows a developer (currently just Novint, since I've had no luck analyzing the pins. Stupid tiny LQFP pins and my shaky hand.) to possibly speed up the control loop on the internal processor depending on application specific needs. Damn fine idea, even if it did crank the price of the hardware quite a bit, I'm sure.

When a program wants to connect to the falcon, the following sequence occurs (if you want to follow along, check out [nifalcon_libftdi.c][21]). Note that the bauds get funky, because baud rate actually turns into a clock subdivision on the board, so I just converted the rate to the lowest clock subdivision possible that would still make them work. See the How I Mapped The Test Firmware Protocol section for more info.

* Open connection to FTDI chip
* The "Are we at least connected" Step:
  * Set to 9600 8N1, No Flow Control, DTR High
  * Write a 3 byte check message, {0x0a, 0x43, 0x0d}
  * Read, expect 5 bytes back
* The "Send the firmware over" Step:
  * Set 140000 baud, DTR Low
  * Write a single byte (Usually 0x41 "A")
  * Read, expect same byte back
  * Send firmware file in 128 byte chunks
  * Read, expect exact chunk we sent back from the falcon as error check
* The "Ready To Go" Step:
  * Set baud to 1456213 (Maximum for the chip?)

After we've gotten this far, we're ready to run an I/O loop to the falcon.

**The Test Firmware**

So far, the only firmware that's usable with code I've written is what I call the "test" firmware. This is the NOVINT.BIN file included with the drivers, that the utilities in "c:\Program Files\Novint\Falcon\TestUtilities\" in a normal windows nVent (I HATE NVENT but that's an article for another day) install will use.

Rather than repeat the info here, if you're interested in the packet layout of the test firmware, [check out my wiki page on it][22]. 

Note, however, that there are a few things you might not be aware of. First off, when you set a motor torque, it's only for a very short period of time (Haven't scoped out the exact value). Basically, you're expected to be polling the falcon _constantly_ and setting the torques as needed. The controlling program is closing the control loop to the falcon, as just keeping torques on until next update can cause lots of badness (motor wear, crunched fingers, etc...)

**Goals of the libnifalcon Project**

So, that's pretty much all I know about this thing right now. I'm working on learning the math behind the haptics and placement algorithms, and while I learn, you'll get to learn along with me, in the form of reading my ridiculously long blog posts!

All of this is going into code form in the [libnifalcon][12] project on Sourceforge. As of this writing, v0.2 is sitting in the repository waiting for me to finish a few cleanup things.

Here's a few applications I have planned for [libnifalcon][12]:

* Max/MSP and PureData Patch (already done, just needs to be cleaned, threaded, and released. It's in the repository if you absolutely can't wait)
* Mouse movement/simulation
* Basic open source haptics library integration
* Mapping the TMS320 pins and possibly starting on my own firmware

As you can see, right now I'm more interested in getting a code platform built and teaching myself haptics programming from the ground up than I am in implementing any specific application. However, I do spend a lot of time in Pd playing with the falcon at the moment, and will most likely be posting interesting projects out of that in between code geekouts.

**Aside 1: How I Mapped the Test Firmware Protocol**

Mapping the test firmware protocol was fairly easy. I used [SniffUSB][23] to record the packets going to/from the Falcon in the test programs, then compared the data in those with the protocol mapping for the FTDI available in the [libftdi][24] source code. The bootloader code is basically a handwritten replay of this sequence, except translated back into FTDI driver calls instead of pure USB comms, hence some of the weirdness in the explanation (the "send 3 get back 5" seqeuence, the odd baud rates, etc...). 

This was, quite literally, all it took. No amazingness or code breaking or whatever. Figuring out the packet setup was just a matter of mapping the numbers from the test GUI to the changing bytes of the packets. 

**Aside 2: FTD2XX versus [libftdi][24], Operating Systems, and You**

[libnifalcon][12] comes in two flavors right now.

* [FTD2XX][25]

  * This is the driver that FTDI distributes, and the one that the default Windows Falcon drivers use. It seems fine on windows, outside of the fact that I personally have issues connecting the Falcon through a hub. This may or may not be due to my machine. However, this drivers seem wildly unstable on Mac and Linux. Also, they have no versions available for 64-bit Linux

* [libftdi][24]

  * This is the free, reverse engineered version of FTDI's drivers, that use libusb. They seem to be stable across all platforms, though I only recommend using them for anything non-windows (or non-publically distributed on windows. Don't make people switch drivers if you don't have to.). It's GPL'd, too, so if you want to use libnifalcon under [libftdi][24], you're stuck with the GPL too. Meh.

   [1]: http://www.nonpolynomial.com/archives/2008/03/that-thingy-that-feels.php
   [2]: http://www.gamesetwatch.com/2008/03/gamesetlinks_from_falcon_to.php
   [3]: http://arstechnica.com/journals/thumbs.ars/2008/03/25/novint-falcon-at-retail-problems-in-selling-haptic-controllers
   [4]: http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/falcon.jpg
   [5]: http://www.bracina.com/haptichardware.html
   [6]: http://www.parallemics.org
   [7]: http://en.wikipedia.org/wiki/Parallel_manipulator
   [8]: http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/parallel1.jpg
   [9]: http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/parallel2.jpg
   [10]: http://www.eurohaptics.vision.ee.ethz.ch/2001/grange.pdf
   [11]: http://www.parallemic.org/Reviews/Review002.html
   [12]: http://libnifalcon.sourceforge.net
   [13]: http://www.forcedimension.com/
   [14]: http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/omega3_2.jpg
   [15]: http://farm3.static.flickr.com/2093/2275967695_20b971efce.jpg
   [16]: http://www.flickr.com/photos/qdot76367/2275967695/ (The Inside of the Falcon by qdot76367, on Flickr)
   [17]: http://www.ftdichip.com/
   [18]: http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1335&dDocName=en010215
   [19]: http://focus.ti.com/docs/prod/folders/print/tms320r2811.html
   [20]: http://www.ftdichip.com/FTDrivers.htm
   [21]: http://libnifalcon.svn.sourceforge.net/viewvc/libnifalcon/trunk/libnifalcon/src/nifalcon_libftdi.c?view=lo
   [22]: http://wiki.nonpolynomial.com/NovintFalcon
   [23]: http://www.pcausa.com/Utilities/UsbSnoop/default.htm
   [24]: http://www.intra2net.com/de/produkte/opensource/ftdi/
   [25]: http://www.ftdichip.com
   [26]: http://libnifalcon.nonpolynomial.com
