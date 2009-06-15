--- 
title: NP Labs Projects Update
date: 2008-11-02 21:21:20 -08:00
mt_id: 1203
layout: post
---
Wow. Almost 5 months between posts. I've been so busy on my projects that I have no time to write about them anymore. :)

First off, <A HREF='http://libnifalcon.sourceforge.net'>libnifalcon</A>, the open source driver for the <A HREF='http://home.novint.com'>Novint Falcon</A>, is currently in alpha stage for the v1 release, soon to move to beta after a few more bugs are fixed. It's already seeing some usage, too!

<CENTER><object width="400" height="300">	<param name="allowfullscreen" value="true" />	<param name="allowscriptaccess" value="always" />	<param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=2138448&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=01AAEA&amp;fullscreen=1" />	<embed src="http://vimeo.com/moogaloop.swf?clip_id=2138448&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=01AAEA&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="300"></embed></object><br /><a href="http://vimeo.com/2138448?pg=embed&amp;sec=2138448">Haptic Interfaces for Virtual Instruments using libnifalcon</a> from <a href="http://vimeo.com/user154518?pg=embed&amp;sec=2138448">qDot</a> on <a href="http://vimeo.com?pg=embed&amp;sec=2138448">Vimeo</a>.</CENTER>

The video above is a demo of a couple of patches for <A HREF='http://www.puredata.info'>PureData</A> written by <A HREF=''>Edgar Berdahl</A> for use in <A HREF='http://ccrma.stanford.edu/courses/250a/labs/lab6-Falcon/'>Physical Interaction Design for Music</A> class at the <A HREF='http://ccrma.stanford.edu'>Center for Computer Research in Music and Acoustics at Stanford University</A>. The video shows a haptic simulation of a bowed instrument, as well as a training patch for drum rolls. Moving toward the line in the middle of the window causes the falcon to kick back slightly, and the user must hold the end effector steady to keep the sound steady and constant. All of this is running on a beta version of the np_nifalcon external for max and pd, which is available on the libnifalcon site.

Next up is another project that I decided to throw together today to check out the <A HREF='http://opensoundcontrol.org/'>OpenSoundControl protocol</A>.

<CENTER><object width="400" height="300">	<param name="allowfullscreen" value="true" />	<param name="allowscriptaccess" value="always" />	<param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=2138821&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=01AAEA&amp;fullscreen=1" />	<embed src="http://vimeo.com/moogaloop.swf?clip_id=2138821&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=01AAEA&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="300"></embed></object><br /><a href="http://vimeo.com/2138821?pg=embed&amp;sec=2138821">Kitelight w/ iPhone Controls</a> from <a href="http://vimeo.com/user154518?pg=embed&amp;sec=2138821">qDot</a> on <a href="http://vimeo.com?pg=embed&amp;sec=2138821">Vimeo</a>.</CENTER>

This is the <A HREF='http://vimeo.com/1392439'>Kitelight system</A> controlled using the <A HREF='http://poly.share.dj/projects/#mrmr'>mrmr OSC interface builder for the iPhone</A>. It's connecting to laptop running python using <A HREF='liblo.sourceforge.net'>liblo</A> and <A HREF='das.nasophon.de/pyliblo/'>pyliblo</A> for OSC controls. This goes through a <A HREF='http://digi.com/products/wireless/point-multipoint/xbee-series1-module.jsp'> xbee dev kit board</A> to <A HREF='http://arduino.cc'>an arduino</A> with <A HREF='nkcelectronics.com/freeduino-arduino-xbee-shield-kit.html'>xbee shield</A> which is controlling a panel of RGB LEDs attached to the kite.

Usable range on the zigbee is ~100m, more than enough room for flyer to kite communications. Now that this works, I can also run lighting commands from PureData to do music synchonization or whatever else I might think of. 

For all the URLs listed above, this project came together rather quick, about 90 minutes from start to finish, though obviously all the boards were already built, so it was just a matter of coding it all and learning OSC and mrmr. 

Now, back to working on getting libnifalcon released... 
