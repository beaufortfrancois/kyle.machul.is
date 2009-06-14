--- 
title: Everything I Know About the Novint Falcon as of March 2008
date: 2008-03-25 22:53:59 -07:00
mt_id: 1174
layout: post
---
After <A HREF='http://www.nonpolynomial.com/archives/2008/03/that-thingy-that-feels.php'>my article on the Novint Falcon box</A> got linked by <A HREF='http://www.gamesetwatch.com/2008/03/gamesetlinks_from_falcon_to.php'>GameSetWatch</A> and <A HREF='http://arstechnica.com/journals/thumbs.ars/2008/03/25/novint-falcon-at-retail-problems-in-selling-haptic-controllers'>Ars Technica</A>, it seems like it might be time to do a nice, technical throwdown about what's going on, inside and out of the novint falcon, since everyone else seems hung up on games usage (I guess it's a game controller, but that's not the fun part!). I've been working with the Falcon since early August, and am actually getting fairly far with it.

If you didn't understand my box article, read on anyways. I'm gonna try to make this as understandable to everyone as possible, so you'll all learn C and inverse kinematics and algebraic geometry and come romp with me down the happy streets of writing a driver for a badly marketed piece of hardware no one is buying. 

Come on, what other relaxing hobbies do you have that involve Jacobian Matrices, hmmmmm?

Please note: I have not used Novint's SDK. I do not plan on using Novint's SDK (That would be cheating). I don't know what their developer support is like (though Tom seems nice enough on the forums. Hi Tom!). What you see here is what I've gained from lots of web searching, talking to people that know what they're doing (I'm not a haptics engineer, in fact, this is my project to learn haptics engineering and programming), and randomly trying things while hoping I don't break the falcon. I'll wikify all of this information in time, but it's honestly much faster for me to brain dump in conversational blog mode than it is into a wiki. 

<B>So what the God Damn Hell is the Falcon anyways?!?!</B>

It's everyone's favorite time of class, video time! <i>*wheels in the TV with bad color and hissing, blinking 12:00 VCR*</i>

Seriously. I can't figure out how to explain it. Novint can't figure out how to explain it. So, watch this video, which tries to explain it.

<object width="425" height="355"><param name="movie" value="http://www.youtube.com/v/f3r3od7nah4&hl=en"></param><param name="wmode" value="transparent"></param><embed src="http://www.youtube.com/v/f3r3od7nah4&hl=en" type="application/x-shockwave-flash" wmode="transparent" width="425" height="355"></embed></object>

If you don't understand what it is yet, well, I can't help you anymore. But enjoy this randomly technical description that follows anyways. I worked hard on it, and I did it <B>JUST FOR YOU</B>. Yes, <i>you</i>.

<B>A Little Background on Parallel Robots and Haptic Controllers</B>

Before we dig into the guts, let's start with what you can find out before you take the case off the thing. For reference, here's a picture of the Falcon:

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/falcon.jpg'></CENTER>

A bit of background (this will contain much glossing as I'd like to focus on the falcon, but it's good to have a knowledge of what's out there otherwise). In the world of haptics, there are two major types of controllers. Serial (pen type controllers), and parallel. <A HREF='http://www.bracina.com/haptichardware.html'>An overview of a bunch of the different hardware types is available in an article on bracina.com</A>. 

The NovInt Falcon is a <A HREF='http://www.parallemics.org'>parallel robot</A>. <A HREF='http://en.wikipedia.org/wiki/Parallel_manipulator'>Parallel robots</A> are called such because they have multiple chains of joints working together to create the final position of the controller (or end effector, if you want to be technical about it). Not to mention, the math uses parallelograms to line up the positions.  

If you watch a lot of How It Works (which, if you have cable with the Discovery Channel, you invariably end up doing no matter what. That show is video heroin.), you've seen these before. 

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/parallel1.jpg'></CENTER>

They're real popular in pick and place operations. That's exactly what it sounds like. Pick something up, put it somewhere else. Repeat ad inifinitum. Puttin' things in or on other things. They're good at that. 

Here's one in action.

<CENTER><object width="425" height="355"><param name="movie" value="http://www.youtube.com/v/wzvYsklwKqk&hl=en"></param><param name="wmode" value="transparent"></param><embed src="http://www.youtube.com/v/wzvYsklwKqk&hl=en" type="application/x-shockwave-flash" wmode="transparent" width="425" height="355"></embed></object></CENTER>

So, you're probably like "But it's all pointing down"

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/parallel2.jpg'></CENTER>

Ok, look more familiar now? The NovInt Falcon is a parallel robot <i>turned on its side</i>. It's actually a Delta variant of the parallel manipulator (<A HREF='http://www.eurohaptics.vision.ee.ethz.ch/2001/grange.pdf'>Here's a nice overview of the Delta Haptic Device, which is quite similar to the Falcon/Omega setup</A>). If you want all sorts of interesting history about where it came from, <A HREF='http://www.parallemic.org/Reviews/Review002.html'>check out this article on parallemics.org</A>. But for now, we'll just say: France. It came from France.

There's lots of reasons why using parallel robots in haptics is important. However, I don't quite understand the math behind it all yet, so I'll just repeat what all the webpages say. "Good stiffness and accuracy in a small workspace". Having used some serial controllers before, I can see what they mean. Hard definitely feels... hard. I'm sure I'll be talking more about this in later articles on the development of <A HREF='http://libnifalcon.sourceforge.net'>libnifalcon</A>.

To show a bit of what else is out there, here's the <A HREF='http://www.forcedimension.com/'>ForceDimension and their Omega series of controllers</A>.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/falcon/omega3_2.jpg'></CENTER>

Once again, looks familiar, no?

Well, one major difference.

The Falcon is $249US.

The Omega starts at around $20,000US (the more degrees of freedom, the more expensive. The Omega 7 is around $50k.)

Ok, and the Omega comes with a PCI interface and all sorts of APIs and what not and FD is actually an offshoot of the subset of France that we mentioned above that created this whole thing in the first place, but still. That's some significant 0's worth of difference there.

There's rumors that ForceDimension helped out on the Falcon design. There's also rumors that it came from Sandia with Tom. Only Art Bell truly knows.

So why all this about parallel robots? Well, many future posts will be talking about research in this field, so I figured I'd at least introduce the term. There's also lots of reference and searchable material in here if you're interested in going your own direction with this information. Anyways, back to hackyness.

<B>Internal Circuitry</B>

Now that we've got that out of the way, what's inside it?

Click the image below to go to an annotated flickr picture of the insides. 

<a href="http://www.flickr.com/photos/qdot76367/2275967695/" title="The Inside of the Falcon by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2093/2275967695_20b971efce.jpg" width="500" height="334" alt="The Inside of the Falcon" /></a>

Connectors:
<UL><LI>USB B Connector</LI><LI>Power Connector - goes to 30V 1A wall wart of DOOM</LI></UL>

Yes, the falcon is quite possibly cranking 30W through the motors when you max the torque on all the axes.

Chips (Links to Datasheets or Product Websites):
<UL><LI><A HREF='http://www.ftdichip.com/'>FTDI FT232R</A> USB to Serial Chip</LI><LI><A HREF='http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1335&dDocName=en010215'>PIC 16F688 Microcontroller</A></LI><LI><A HREF='http://focus.ti.com/docs/prod/folders/print/tms320r2811.html'>TI TMS320 R2811</A> DSP Processor</LI></UL>

I don't have specific parts on the 3 motor blocks in the circuit (they're all exactly the same), but what you've basically got going on there is three really large old style mouse encoders. Each of the 3 large wheels attached to the motors have a disc attached to them, alternating little clear slots with opaque slots. There's a photoresistor that shines light through those slots. Whenever the light goes through (clear), you get a 1. Whenever the light is blocked (opaque), you get a zero. And that's how we know how far the motor has gone. 

Whether direction is measured using some sort of quadrature encoding or Back-EMF polarity is something I forgot to check (but will do so at the point where I can figure out how to write my own firmware for this thing).

<B>Communications and Initialization/Bootloading Sequence</B>

Now, for the part I kinda sorta know more about than the other parts. 

The Falcon uses the FTDI chip as it's main communications link to the computer. Everything is filtered back and forth through the FTDI chip, converting from USB on the computer side to RS232 on the circuit side. This is because it's orders of magnitude easier to program your microcontrollers to talk RS232 than it is to talk USB. 

Novint distributes and uses the stock FTDI driver with their software. The only change they've made is to the VID and PID. They've chosen to use <A HREF='http://www.ftdichip.com/FTDrivers.htm'>FTDI's free "have a PID" program</A>, which has them listed under FTDI (0x0403) as a vendor, but with their own special product ID (0xcb48, as opposed to the default PID for FTDI chips, 0x6001).

<i>NOTE: I have not actually proven this next paragraph, it's more what I think is going on than anything.</i> You might've noticed in the Internal Circuitry section that there are two microcontrollers on the board: the PIC and the TI. This is where the bootloader sequence comes in. The TI DSP uC is actually reconfigurable on connection to a PC. The PIC acts as a bootloader, maintaining the logic needed to run the FTDI communications to pick up firmware and program the TI with it. This allows a developer (currently just Novint, since I've had no luck analyzing the pins. Stupid tiny LQFP pins and my shaky hand.) to possibly speed up the control loop on the internal processor depending on application specific needs. Damn fine idea, even if it did crank the price of the hardware quite a bit, I'm sure.

When a program wants to connect to the falcon, the following sequence occurs (if you want to follow along, check out <A HREF='http://libnifalcon.svn.sourceforge.net/viewvc/libnifalcon/trunk/libnifalcon/src/nifalcon_libftdi.c?view=lo'>nifalcon_libftdi.c</A>). Note that the bauds get funky, because baud rate actually turns into a clock subdivision on the board, so I just converted the rate to the lowest clock subdivision possible that would still make them work. See the How I Mapped The Test Firmware Protocol section for more info.

<UL><LI>Open connection to FTDI chip</LI><LI>The "Are we at least connected" Step:</LI><UL><LI>Set to 9600 8N1, No Flow Control, DTR High</LI><LI>Write a 3 byte check message, {0x0a, 0x43, 0x0d}</LI><LI>Read, expect 5 bytes back</LI></UL><LI>The "Send the firmware over" Step:</LI><UL><LI>Set 140000 baud, DTR Low</LI><LI>Write a single byte (Usually 0x41 "A")</LI><LI>Read, expect same byte back</LI><LI>Send firmware file in 128 byte chunks</LI><LI>Read, expect exact chunk we sent back from the falcon as error check</LI></UL><LI>The "Ready To Go" Step:</LI><UL><LI>Set baud to 1456213 (Maximum for the chip?)</LI></UL></UL>

After we've gotten this far, we're ready to run an I/O loop to the falcon.

<B>The Test Firmware</B>

So far, the only firmware that's usable with code I've written is what I call the "test" firmware. This is the NOVINT.BIN file included with the drivers, that the utilities in "c:\Program Files\Novint\Falcon\TestUtilities\" in a normal windows nVent (I HATE NVENT but that's an article for another day) install will use.

Rather than repeat the info here, if you're interested in the packet layout of the test firmware, <A HREF='http://wiki.nonpolynomial.com/NovintFalcon'>check out my wiki page on it</A>. 

Note, however, that there are a few things you might not be aware of. First off, when you set a motor torque, it's only for a very short period of time (Haven't scoped out the exact value). Basically, you're expected to be polling the falcon <i>constantly</i> and setting the torques as needed. The controlling program is closing the control loop to the falcon, as just keeping torques on until next update can cause lots of badness (motor wear, crunched fingers, etc...)

<B>Goals of the libnifalcon Project</B>

So, that's pretty much all I know about this thing right now. I'm working on learning the math behind the haptics and placement algorithms, and while I learn, you'll get to learn along with me, in the form of reading my ridiculously long blog posts!

All of this is going into code form in the <A HREF='http://libnifalcon.sourceforge.net'>libnifalcon</A> project on Sourceforge. As of this writing, v0.2 is sitting in the repository waiting for me to finish a few cleanup things.

Here's a few applications I have planned for <A HREF='http://libnifalcon.sourceforge.net'>libnifalcon</A>:

<UL><LI>Max/MSP and PureData Patch (already done, just needs to be cleaned, threaded, and released. It's in the repository if you absolutely can't wait)</LI><LI>Mouse movement/simulation</LI><LI>Basic open source haptics library integration</LI><LI>Mapping the TMS320 pins and possibly starting on my own firmware</LI></UL>

As you can see, right now I'm more interested in getting a code platform built and teaching myself haptics programming from the ground up than I am in implementing any specific application. However, I do spend a lot of time in Pd playing with the falcon at the moment, and will most likely be posting interesting projects out of that in between code geekouts.

<B>Aside 1: How I Mapped the Test Firmware Protocol</B>

Mapping the test firmware protocol was fairly easy. I used <A HREF='http://www.pcausa.com/Utilities/UsbSnoop/default.htm'>SniffUSB</A> to record the packets going to/from the Falcon in the test programs, then compared the data in those with the protocol mapping for the FTDI available in the <A HREF='http://www.intra2net.com/de/produkte/opensource/ftdi/'>libftdi</A> source code. The bootloader code is basically a handwritten replay of this sequence, except translated back into FTDI driver calls instead of pure USB comms, hence some of the weirdness in the explanation (the "send 3 get back 5" seqeuence, the odd baud rates, etc...). 

This was, quite literally, all it took. No amazingness or code breaking or whatever. Figuring out the packet setup was just a matter of mapping the numbers from the test GUI to the changing bytes of the packets. 

<B>Aside 2: FTD2XX versus <A HREF='http://www.intra2net.com/de/produkte/opensource/ftdi/'>libftdi</A>, Operating Systems, and You</B>

<A HREF='http://libnifalcon.sourceforge.net'>libnifalcon</A> comes in two flavors right now.

<UL><LI><A HREF='http://www.ftdichip.com'>FTD2XX</A></LI><UL><LI>This is the driver that FTDI distributes, and the one that the default Windows Falcon drivers use. It seems fine on windows, outside of the fact that I personally have issues connecting the Falcon through a hub. This may or may not be due to my machine. However, this drivers seem wildly unstable on Mac and Linux. Also, they have no versions available for 64-bit Linux</LI></UL><LI><A HREF='http://www.intra2net.com/de/produkte/opensource/ftdi/'>libftdi</A></LI><UL><LI>This is the free, reverse engineered version of FTDI's drivers, that use libusb. They seem to be stable across all platforms, though I only recommend using them for anything non-windows (or non-publically distributed on windows. Don't make people switch drivers if you don't have to.). It's GPL'd, too, so if you want to use libnifalcon under <A HREF='http://www.intra2net.com/de/produkte/opensource/ftdi/'>libftdi</A>, you're stuck with the GPL too. Meh.</LI></UL></UL>
 
