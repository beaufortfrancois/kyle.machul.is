--- 
title: "WiiYo: IR LED + Yoyo + WiiMote"
date: 2008-01-13 22:42:38 -08:00
mt_id: 1164
layout: post
---
Taking some inspiration from <A HREF='http://www.cs.cmu.edu/~johnny/projects/wii/'>Johnny Chung Lee's WiiMote Projects</A>, I decided I'd like to figure out something neat to do with the WiiMote's IR Camera. I didn't realize that it's 1024x768 @ 100hz for up to 4 IR points (with 4 bits of depth, even), which gives you enough resolution to do some interesting stuff.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2192046336/" title="yoyoproject by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2380/2192046336_40962cb9bc.jpg" width="500" height="375" alt="yoyoproject" /></a></CENTER>

For those of you that haven't known me a while, you might not be aware that I used to yoyo quite a bit. I still play every so often, but not nearly as much as I used to. I ended up building up quite the collection, though. Something I always wanted to be able to do was yoyo tracking. I played a little bit with blob tracking and LEDs, but didn't have the hardware or experience back then (2000-2001ish) to really do what I wanted.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2191251499/" title="yoyoproject 005 by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2239/2191251499_bd418c6510.jpg" width="500" height="375" alt="yoyoproject 005" /></a></CENTER>

After seeing the head tracking and finger tracking videos, the first thing I thought of was trying the yoyo project again. Without taking the time to actually look at my collection, I decided to drill up an old freehand pog and electric tape it to my Pyro with a CR2032 pack attached to the back of the pog for power.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2192039408/" title="yoyoproject 006 by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2415/2192039408_30013b1db0.jpg" width="500" height="375" alt="yoyoproject 006" /></a></CENTER>

This ended up being such a colossally bad idea that I'm not gonna spend much time talking about it. The yoyo was unusably unbalanced. So, digging through my yoyo box somemore, I realized I still had some Torch LED pogs.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2192039620/" title="yoyoproject 009 by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2277/2192039620_3792f6a831.jpg" width="500" height="375" alt="yoyoproject 009" /></a></CENTER> 

I removed the Red LED off of these and replaced it with an IR LED and a smaller resistor. Since I didn't really have any Spintastics yoyos I wanted to throw the pog in, I ended up dismantling my already sort of broken Night Moves 2 (the plastic on the axle end had cracked on it a while ago for some reason), and hot gluing the pog in to hold it. Sure enough, the yoyo was slightly unbalanced, but completely usable for most any trick. After ninja starring the pog due to not having hot glued it well enough the first time, I made sure to do a better job, and now I have an IR yoyo!

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2192039668/" title="yoyoproject 010 by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2025/2192039668_8ddc30c628.jpg" width="500" height="375" alt="yoyoproject 010" /></a></CENTER>

So, with yoyo+wiimote setup finished, I fired up Max/MSP and used the <A HREF='http://www.iamas.ac.jp/~aka/max/'>aka.objects wiiremote and appleremote</A> externals along with the LCD object to make a little drawing program. The Apple Remote works as a pen start/stop and clearing device, so I can clear the screen and start/stop drawing while standing far back from the computer. The Wiimote external is wired to draw lines depending on the first IR readout from the camera.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2187280106/" title="gerbil by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2028/2187280106_abb8570bf4.jpg" width="500" height="375" alt="gerbil" /></a></CENTER>

The above picture is a drawing from that program, of an almost-but-not-really version of the <A HREF='http://sector_y.yoyoing.com/Tricks/String_Tricks/Skin_the_Gerbil/Skin_the_Gerbil.htm'>"skin the gerbil" trick</A> by <A HREF='http://www.doctorpopular.com'>Doctor Popular</A>. 

The picture also shows a couple of the current problems with the system. First off, I've completely trashed my office getting this done, so I can't back up very far and don't have a good idea of what the Wiimote is seeing. This could be fixed by calibration, which is something I plan on figuring out. Secondly, there's some sampling issue with large swings. Either my swings are causing tilt, the LED doesn't have a wide enough angle, or some combination of the two. I've ordered 5 more kinds of LEDs to test this.

<CENTER><a href="http://www.flickr.com/photos/qdot76367/2190430077/" title="patchpic by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2228/2190430077_16ae778335.jpg" width="500" height="314" alt="patchpic" /></a></CENTER>

Finally, I hooked up a little sample looper in Max/MSP to the setup so that it would spit out some noise, too.

<CENTER><object width="425" height="355"><param name="movie" value="http://www.youtube.com/v/9RqBJgGNiE8&rel=1"></param><param name="wmode" value="transparent"></param><embed src="http://www.youtube.com/v/9RqBJgGNiE8&rel=1" type="application/x-shockwave-flash" wmode="transparent" width="425" height="355"></embed></object></CENTER>
 
This video is a combination of the drawing and the video, processed through Jitter. Warning, the sound is VERY desynchronized from the video. 100% of my experience with Jitter has happened in the last 24 hours, and apparently I missed something about getting the video to synchronize (realtime setting, maybe?), which is why the sound doesn't match the video.

So, that was my weekend. The project still has a long way to go. I've got 2 more Torch boards to mod once the LEDs come in, and it'll be interesting to see which LEDs work best. I should have those later this week. I also plan on modding a spintastics top I have that has a torch board in it, so I can do Augmented Reality Battle Tops. 

Have any interesting ideas for this project? Please leave comments! Seems like there's a million places this could go.  
