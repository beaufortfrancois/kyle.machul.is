--- 
title: libnifalcon v0.2 and np_nifalcon Max/Pd patches finished
date: 2008-04-05 23:03:40 -07:00
mt_id: 1175
layout: post
---
Well, <A HREF='http://libnifalcon.sf.net'>v0.2 of libnifalcon is all done</A>. Yay. That took a lot more work than I thought it would. 

Of course, I've also now run into the nasty fact that libftdi is around 4x slower than ftd2xx, meaning that what's a 1000hz update rate on windows ends up being 300hz max on Linux and OS X. Not happy about this at /all/, but there's really not much I can do outside of porting to a kernel driver probably. Which, yeah, I've thought about doing, because I hate myself.

Anyways, I've also finished Max and Pd patches for the falcon for all platforms, thus my first real released "application" for this. Only took me 9 months. Go me.

Now then, see if you can figure out which program is the free one, and which one is the expensive one:

Max/MSP:

<a href="http://www.flickr.com/photos/qdot76367/2389032528/" title="np_nifalcon Max External Tutorial by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2289/2389032528_fcc6668dea.jpg" width="500" height="365" alt="np_nifalcon Max External Tutorial" /></a>

PureData:

<a href="http://www.flickr.com/photos/qdot76367/2391872168/" title="np_nifalcon PureData External Tutorial by qdot76367, on Flickr"><img src="http://farm3.static.flickr.com/2336/2391872168_f84a82107a_o.jpg" width="406" height="313" alt="np_nifalcon PureData External Tutorial" /></a>

Is there such a thing as a pretty PD patch? I have yet to see one. 
