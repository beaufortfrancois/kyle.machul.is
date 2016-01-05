title: Keepon Control via Kinect
date: 2011-11-16 00:12:09

And the hits just keep on comin'.

http://www.youtube.com/watch?v=6XhbYWLnsq0

I threw this together this evening, in about 4 hours from top to
bottom (code + video). Yay open source. 

<!--more-->

Project uses:

* Arduino + Keepoff [http://www.github.com/qdot/keepoff](http://www.github.com/qdot/keepoff) - Control of Keepon Robot
* Processing [http://www.processing.org](http://www.processing.org) - tying the whole thing together
* OSCP5 [http://www.sojamo.de/oscP5](http://www.sojamo.de/oscP5) - talk to python script that's controlling arduino, already had that written so didn't write serial controls in Processing
* GSVideo [http://gsvideo.sourceforge.net](http://gsvideo.sourceforge.net) - for webcam (filming keepon)
* SimpleOpenNI [http://code.google.com/p/simple-openni](http://code.google.com/p/simple-openni) - kinect recording and skeleton tracking in processing
* libfreenect [http://www.openkinect.org](http://www.openkinect.org) - Cross platform kinect access

Processing running on Linux, X Forwarded to OS X because apparently
it's impossible to get good screencast software on linux.

It's missing the side to side bend sensor because I'm still not quite
sure how that motor message works yet, but this is good enough for a
first demo.

Code is, as usual, available at

[http://www.github.com/qdot/keepoff](http://www.github.com/qdot/keepoff)

So, why goth dance? This is a running joke we had at
[the Art and Code conference at CMU last month](http://www.artandcode.com/3d).
For those not familiar with the youtube meme:

http://www.youtube.com/watch?v=PvNrjcg3WjA

I figured that I might as well turn it into a way to demo new
hardware. Other A&&C people, consider the (velvet, tear stained)
gauntlet thrown down.
