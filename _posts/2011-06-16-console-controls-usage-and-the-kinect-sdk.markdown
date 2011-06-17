--- 
title: Console Controls Usage and the Kinect SDK
date: 2011-06-16 14:15:09 -08:00
layout: post
---

Oh frabjous fucking day. The [Microsoft Kinect SDK is out][1]. Along
with a license that takes a [very, very nasty FAQ to explain][2].

On this big day in UI development, let's take a look over the current
console controls landscape, and what it means to non-game
developers.

Why focus on game consoles controls? They've driven down sensor prices
like crazy, due to mass manufacturing and required price points for
game sales. They've established more than a few careers of
non-game-developers now. Uses of the kinect and the wiimote for
projects not pertaining to their original console have been all over
the media lately. Keeping a forecast of where development for these
technologies is going means we have a better idea of how to ride the
wave when it comes.

## Disclaimers ##

* In terms of licensing issues, I am not a lawyer. I do not play one
  on TV. However, I do have a lawyer fursona.
* While I am part of the OpenKinect project, I do not speak for others
  involved in the project. All opinions expressed here are my own, and
  all cursing is far fucking better than anyone else on the project
  could turn out, so while I may share my source code, I'm not giving
  them rights to that.
* I strive to keep all the information as correct as possible, but,
  well, I've been drinking.
* I am not a game developer. I am a reverse engineer that specializes
  in controls and interface devices. My view of this hardware is
  purely from the driver and capabilities side.
* I have not directly used the Move SDK or Kinect SDK. But I have read
  some articles and created very strong opinions, which means they are
  valid for internet consumption.
* This article is only about reversing/using alternative console
  controllers, not about reversing consoles themselves. There's a
  completely different history to that which would take much more than
  a blog post to cover, though I will admit that it does have some
  influence on the information here..

## Nintendo Wiimote ##

The WiiMote was first out of the gate, so let's start with it. 

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-wiimote.jpg' /></CENTER>

You get:

* 100hz update for 4 IR points with 4 bits of depth @ 1024x768
* 3-axis Accelerometer
* Bluetooth Communication
* 3-axis Gyro with WiiMotion Plus
* Extensible Control Port

### What Nintendo provide in terms of software ###

Nothing.

### What the community provides in terms of software ###

The [Wiimote protocols have been reversed and known for years][3], and
there's availability in pretty much every language you can think of.

### What Nintendo thinks of non-game developers ###

Are you Zelda? Are you Mario? No. No you are not. Therefore, go fuck
yourself.

Nintendo hasn't put out anything in terms of press releases about the
DIY community during the lifetime of the Wiimote. They're happy to let
them live seperately, and that's a fine strategy. Nintendo has to put
zero into support, they aren't actively stopping people from using the
wiimote, and developers can survive on their own.

### Where Nintendo is going with it ###

Honestly? Not real sure here. With the upcoming release of the WiiU
controller, there wasn't a lot of talk about Nintendo's flaily
controls strategy.

### Where the community is going with it ###

Where haven't they? There's [Johnny Lee's demos][4], there's
[sex toys][5], there's more "generative art" than you could shake a
wiimote at. The Wiimote is as ubiquitous as alternative controls get
these days.

With the WiiMotion Plus, it even turns into a nice IMU. The WiiMote
still has some life to it as a cheap, extensible sensor platform,
especially with the amount of prior usage it has seen already. Outside
of a somewhat flakey bluetooth interface, the "just works"ness of it
will keep it alive for a while to come.

## Nintendo WiiU Controller ##

I don't even know if this'll exist in a year, but it's been
announced, so might as well talk about it.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-wiiu.jpg' /></CENTER>

You Get:

* A 6.2inch screen
* No idea on communications method, but enough bandwidth to pipe over video in real time
* Joystick
* 3-axis Accel/Gyro
* Front Facing Camera
* Probably other stuff that I'm missing or they'll add.

### What Nintendo provide in terms of software ###

Well, it's not gonna come out for another 18 months, so I have no
idea. It may not even look the same by then.

### Where Nintendo's going with it ###

I... don't know, and I don't think that's good. It's almost _too_
integrated, when we're already seeing new controllers that provide
both physical controls and a detachable screen.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-livid.jpg' /></CENTER>

<CENTER><small markdown='1'>Above: [Livid Instruments Controller][9] integrated with iPad</small></CENTER>

These are using tablets that, by the release time of the WiiU, should
be under $100. Between the Android OpenAccessories SDK and whatever
Apple decides to do, this will be far beyond replicated by
release. Not only that, the rumors are flying about the WiiU only
working with one controller per console.

In the end, it's really too far out to make accurate predictions for
this, though that's obviously not stopping me from trying. I thought
the GBA interface to Gamecube games was great, but, well, it could
still be a GBA after that too. This... Who knows. It doesn't seems as
mind breaking at the Wiimote did, but then again, you only get to
one-up the joystick once.

### What Nintendo think of non-game developers ###

You still won't be Mario or Zelda, so you can still go fuck yourself. 

More important this time though, why would it be easier for you to
work with Nintendo's hardware than with a tablet and another
accessory? Nintendo has already proven time and time again they don't
care to support developers outside of console games.  Doesn't seem
like this will gain community traction in its current state.

## Playstation Move ##

Sony's entry into the gaming market: a wand with a light on it.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-move.jpg' /></CENTER>

You get:

* A wand with a light on it
* Bluetooth connection
* Accelerometer
* Gyro
* EyeToy Camera to watch wand with light on it

### What Sony provides in terms of software ###

The [MoveMe SDK][6], announced at GDC, not yet released. This allows
you to get full real-time 3d positioning from Move controllers.

It requires you to get this information via a network connection to
your PS3. The tracking algorithms are locked onto the PS3, and you
have to have the console running special server software to use the
SDK.

To develop for the Move, you have a minimum investment of around $600,
for the controller plus the console. A fanboy would tell you that you
also get a Blu-Ray player out of that. I am not a fanboy.

### What the community provides in terms of software ###

There's the [MoveOnPC project][7], which is an effort to create open
source drivers for using the Move as a control mechanism. They're not
real far along yet, but the project is at least active.

### What Sony think of non-game developers ###

"Absolutely adorable" is about the best thing I can think of. They
think the homebrew and DIY community is cute, and they seem to view
homebrew devs, much like their customers, as lesser beings. Weirder
still, they seem to harbor both fear and disdain at the same time. For
instance, as seen through the way they released the SDK. They're
making SURE you have to have a console, and that you only get what
they want, and getting to their algos will require both hardware and
software reversing.

### Where Sony's going with it ###

Same idea as the Wiimote, except more accurate positioning. Build
plastic toys around it, use those as controls. Oh boy.

### Where the community is going with it ###

This turns the Nintendo view around... Does the community really care?
I haven't seen bounties out for the Move. I haven't seen message
boards filled with people working on it. This time, it seems like the
company would be insulting the community with the way they released
their SDK, but the community doesn't even care in the first place.

## Microsoft Kinect ##

For the Kinect, we've got so many different solutions out there now
that I'm actually splitting them into their own sections.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-teardown.jpg' /></CENTER>

You get:

* 640x480 RGB @ 30hz
* 320x240 Depth @ 30hz, .5-4m depth range
* USB 2.0 High Speed Connection
* Microphone Array
* LED, Accelerometer

## Microsoft Kinect - OpenKinect ##

[OpenKinect][11] was the project that sprung up around the
[OpenKinect Bounty hosted by Adafruit Industries][12] in November
2010. If you've like a more in-depth history, check out
[my presentation on it at Maker Faire 2011][8].

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-openkinect.png' /></CENTER>

As I said in the intro, while I am part of the OpenKinect project,
what I am stating about the project here is my own opinion, and does
not speak for other members of the project.

### What OpenKinect provides ###

An open-source, cross-platform method for accessing raw data coming
off of the kinect. Nothing more, nothing less. It was the first to
publically provide access to images, leds, and accelerometers on all
major platforms. Audio support is in the works, and has been taken to
the proof of concept stage.

There's been talk of including processing algorithms created by the
open source community, in a seperate library. This part of the project
has not yet taken shape, though, and most concentration lies in
finishing the driver.

### What OpenKinect think of non-game developers ###

Not to sound harsh, but they just don't. They don't really think about
any kind of specific developer. The driver exists to be just the
driver, and this is the simplest way to serve that goal. You take it
and do whatever you want with it. Have fun.

What this means is that, unlike OpenNI and Microsoft's SDK, OpenKinect
is the easiest way to get the raw data from the camera. If you are
interested in doing something other than skeleton tracking, this makes
it the lowest barrier to entry.

### Where OpenKinect is going with it ###

At this point, it's all about finishing providing the features of the
camera. This mostly has to do with the audio core, as the camera
features are fairly well covered.

In terms of what will happen with OpenKinect now that the Microsoft
SDK is out, I think the answer is "not much". There's a fork of
OpenNI's sensor library that uses OpenKinect to talk to the kinect and
provide the rest of the OpenNI capabilities for that camera. MS has no
interest in supporting non-windows 7 platforms, so there will
certainly still be a place for OpenKinect in the Kinect ecosystem.

Not only that, Windows has been by far the hardest platform to deal
with for development and support for OpenKinect. I actually hope that
we can build an API wrapper around the MS SDK, to make it fit with
OpenKinect without having to switch out drivers. However, having not
read much of the MS SDK documentation as of yet, this remains to be
seen. 

Also, with the licensing terms as they currently are, OpenKinect
remains commercially viable on all platforms, while Microsoft's SDK
specifically prohibits that kind of usage.

## Microsoft Kinect - PrimeSense/OpenNI ##

A few weeks after the OpenKinect project put out the source for their
library, depth camera chip manufacturer [PrimeSense][13] followed suit
with their own SDK, known as [OpenNI][14].

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-openni.png' /></CENTER>

OpenNI is both a library and an initiative. The library is the
implementation of a standard that PrimeSense is pushing to be a
standard SDK for future depth sensors. The initiative part includes
multiple companies on board with this standard.

### What PrimeSense provides ###

PrimeSense provides 3 different libraries, all cross-platform, with
varying open/closed source policies:

* Sensor - Hardware access library. Their version only supports their
  PrimeSense SDK camera, but there's a version that's build on top of
  OpenKinect for kinect access. Open Source.
* OpenNI - This is supposed to be an "abstraction library for depth
  cameras". Which I guess translates into "huge C++ beast". It's a
  way to abstract depth camera information so you can use anything
  providing depth data with any program that will take depth
  data. Seeing the only consumer depth cameras are PrimeSense's, this
  works out well for them. Open Source.
* NITE - This is PrimeSense's body/skeleton tracking library. Unlike
  Microsoft's algorithms, NITE requires a calibration pose to find
  skeletons, meaning you have to stand in front of the camera and hold
  your arms in a certain way for it to find you in the scene. This can
  be flakey sometimes. Unlike Microsoft's libraries, NITE is available
  for commercial use. It is closed source, but the binaries are free.

### What they think of non-game developers ###

Developers, via OpenNI, are marketing for PrimeSense.

Funny enough, PrimeSense doesn't actually care about game
developers. It's not really even their domain. Primesense wants to own
the home theatre remote control market, hence their focus on things
like the Asus Wavi Xtion. The battle for being able to control your
media consumption is far larger than the battle to control how you
flail in front of your TV and call it control. More people watch TV
and movies than play video games, and the amount of hours logged on
watching activities is exponentially higher. TV Remotes are getting
unwieldy now, so the next step that is apparently logical to someone
with money is that we now wave our hands around to start and stop our
movies, or change our channels.

On top of this, PrimeSense is not a camera company, they are a chip
company. They need to be able to sell their chip in large quantities
to people who will manufacture cameras with it. Therefore, if
developers make applications with OpenNI/NITE, and OpenNI/NITE will
"just work" with any PrimeSense camera, then PrimeSense gets to claim
they are "open", and anyone that manufactures a camera with a
PrimeSense chip will have access to all the applications that've
already been written by other developers.

### Where they're going with it ###

OpenNI/NITE is another weapon in the battle for the home theatre as
home information hub. That's why PrimeSense wants the chip and
software everywhere, not just in kinects. So, they're betting both for
and against Microsoft at the same time, which is a very interesting
position to be in.

If NITE doesn't support non-calibration poses very soon, it's going to
lose out to SDKs that do. MS has proven you can track bodies without
calibration, even if it does take thousands of hours of video to
analyze through advanced algorithms. Now that MS's SDK is out and does
not require calibration poses, people's expectations are quickly going
to change. NITE still has a foothold on the commercial licensing side,
but that doesn't help much for consumer expectations of product.

## Microsoft Kinect - Microsoft's SDK ##

On June 16th 2011,
[Microsoft released their own SDK for the kinect][17], much to the
surprise of just about everyone, since there had been no communication
since March about it.

<CENTER><IMG SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/kinect-mssdk.png' /></CENTER>

As of this writing, the SDK is still considered "beta", and is only
available for non-commercial use.

### What Microsoft provides ###

Seamless skeleton tracking, which is a huge deal. While the algorithms
have been released and replicated in open source, the advantage that
MS has here is big data. Thousands of hours of training sets to send
through the algorithm so that it can find any body type, meaning that
people can walk in and out of the scene and instantly be recognized
and tracked. Seriously fucking _BIG_ deal.

There is also access to the audio system, which no project has gotten
a complete hold on yet. OpenKinect has some access to the raw audio
stream, but Microsoft provides a voice SDK that allows developers to
identify and position users based on sound.

### What they think of non-game developers ###

With the beta licensing terms, developers are somewhere between
fanboys and marketing. Open Source developers are back on the bad
side, too.

The [Beta SDK FAQ][2] is chock full of interesting issues, including:

* Not being able to distribute applications standalone, users must
  also download SDK to get the runtimes
* No commercial use, and on top of that, due to the fact that MS
  cannot predict the usage of the kinect SDK, all SDK derived
  applications should not be considered "allowed under the SDK".
* Microsoft owns the right to say what software you can use the
  hardware with, and using the kinect with anything outside of the SDK
  is not allowed. Even with this wording in place, the MSDN Channel 9
  launch video lauded all of the open source applications currently
  available for the kinect.
* The SDK will not run on Virtual Machines
* Refusal for any SDK derived application code to be released
  under copyleft licenses (GPL, etc...)

In other words, you can write kinect apps for yourself, then you can
upload videos of those apps to show off how awesome the SDK is, but
redistribution is not allowed, and neither is selling. There's no word
on when a commercial SDK will be available or how much it will cost.

Of course, MS can't really track most of what they claim in the FAQ,
but it seems to be worded in a very predatory way. It's still better
than Sony's "lock down the algorithms on the console" idea, and it's
not really enforcable for a lot of projects. Whether anyone but nerds
like me will give a shit about that is a completely different question
that we're not going to answer because it's my blog and I'm the center
of the universe here.

### Where they're going with it ###

Everywhere, and into everything, as fast as possible. Which, for a
company the size of Microsoft, will not be all that quick. There's
already talk of Windows 8 shipping with kinect drivers.

With the algorithms and samples Microsoft has put out in their SDK,
they've jumped way ahead of the other solutions in the NUI
game. Without the calibration pose requirement, MS SDK programs should
"just work" for people coming in to/out of the scene. It adds access
to the audio core that no other solution can get anywhere near at the
moment. For the time being, MS is now winning the NUI game in terms of
capabilities available to developers. 

At least, for developers want to make non-distributable demos. Since
the license is still non-commercial only, that's all they're going to
win. This could end up pissing off the industry enough that they find
some way to replicate it without Microsoft's terms. At that point, we
have a very fun war on our hands.

### Where the community is going with it ###

There's not much of a community to speak of since it's been out all of
10 hours as I write this. While I know [CodePlex][10] is huge, I've
never really dealt with the MS Open Source Community, or, well, any MS
community period in the past decade or so. I guess we'll see what
happens. I'm certainly interested to see how the cultural philosophies
of OpenKinect versus MS SDK influence the projects that come out of
them. 

For a better perspective on this, I defer to [Josh Blake][18], who I
am signing up to write an article on it before even asking him. Hi
Josh!

## Conclusion ## 

So, that's how I see things going for creative outside development on
console controls for the time being. Take it with a variable sized
grain of salt.

For the wiimote, it's gonna keep dropping from an already fairly
cheap price, and the fact that you don't have to solder things to it
makes it very handy for prototyping. It'll live for a while longer.

I wouldn't be surprised if the move never sees the light of day in the
maker community. It's just not getting any sort of traction from
either side, and it seems easy enough to just replicate at some point.

For the Kinect, MS has a good grip on the NUI market now. However,
there are many other uses for depth cameras that don't require a body
to be in front of it. 3d modeling, robotics, art, etc... Yes, the
kinect was made to track bodies, and that's what the camera range and
other properties of the camera reflect. While the MS SDK will make
access the raw data easier on windows, it won't completely overtake
the Kinect development world.

It'll also be interesting to see if the open source community can
figure out a way to source enough data to train their own algorithms,
and provide MS with some competition. We've thrown this idea around at
the [SF 3D Vision Meetup][15] and in the [OpenKinect IRC channel][16],
but that's a huge undertaking. It signals the next big move for the
open source community though. We've proven out big code, and see huge
projects released as open source. Now it's time to start playing more
with open big data.

[1]: http://research.microsoft.com/en-us/um/redmond/projects/kinectsdk/default.aspx
[2]: http://research.microsoft.com/en-us/um/redmond/projects/kinectsdk/faq.aspx
[3]: http://wiibrew.org/wiki/Wiimote
[4]: http://johnnylee.net/projects/wii/
[5]: http://www.colorsaregood.de/index.php?cont=4&inhalt=oioo
[6]: http://us.playstation.com/ps3/playstation-move/move-me/
[7]: http://code.google.com/p/moveonpc/
[8]: http://fora.tv/2011/05/21/Kyle_Machulis_OpenKinect
[9]: http://lividinstruments.com/
[10]: http://www.codeplex.com
[11]: http://www.openkinect.org
[12]: http://www.adafruit.com/blog/2010/11/10/we-have-a-winner-open-kinect-drivers-released-winner-will-use-3k-for-more-hacking-plus-an-additional-2k-goes-to-the-eff/
[13]: http://www.primesense.com
[14]: http://www.openni.org
[15]: http://www.meetup.com/3DVision/
[16]: http://openkinect.org/wiki/IRC
[17]: http://research.microsoft.com/en-us/um/redmond/projects/kinectsdk/
[18]: http://nui.joshland.org/
