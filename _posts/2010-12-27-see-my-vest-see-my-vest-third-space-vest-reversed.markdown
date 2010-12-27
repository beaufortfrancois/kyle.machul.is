--- 
title: See my vest! See my Vest! Third Space Vest Reverse Engineered
date: 2010-12-27 00:30:20 -08:00
layout: post
---

Presenting [libthirdspacevest][6], the open source, cross platform
driver for the [The TN Games Third Space Vest][1] by Kyle
Machulis/Nonpolynomial Labs. 

Because apparently it wasn't enough to just work on the [kinect][5].

<CENTER markdown='1'>[![Third Space Vest][4]][1]</CENTER>

This is a USB controlled vest with 8 air cells in it, which can be
used to cause quick haptic force via pneumatics. In other words, it's
a vest that can simulate being shot, by way of making the user feel
like a roll of bubble wrap. I've also heard it described as "being
poked by gnomes. And not with their fingers." While I cannot vouch for
the physical accuracy of that statement (yet), it does fit well with
the mental images of the feeling.

As usual, I decided to reverse engineer it to write my own drivers,
which will eventually turn into Max/Pd externals, and also another
project that I'll be annoucing later this week.

This normally wouldn't be a problem, but this time around, much like
the issues emokit had, the manufacturer encrypted the protocol, but
distributed a free (pre-compiled, closed source) SDK. I ended up
[writing up the procedure for reversing out the protocol and building the library][2],
since it's one of the more complicated procedures I've had to do to
get new hardware working. I was thinking about posting the doc here,
but it's rather long.

Anyways, it's now done and there's proof of concept python using
[pyusb][3] in the repo. I'll be extending this to a C API as soon as
possible, just to get it over with since there's not a ton of
functionality to the vest.

To close, here's a video of my cat versus the vest (running my code!):

<CENTER markdown='1'><object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/q76cphm7hFI?fs=1&amp;hl=en_US"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/q76cphm7hFI?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object></CENTER>

[1]: http://www.tngames.com
[2]: https://github.com/qdot/libthirdspacevest/blob/master/doc/third_space_vest_reverse_engineering.asciidoc
[3]: http://pyusb.berlios.de/
[4]: http://images.nonpolynomial.com/nonpolynomial.com/blog/thirdspacevest.jpg
[5]: http://www.openkinect.org
[6]: http://github.com/qdot/libthirdspacevest/
