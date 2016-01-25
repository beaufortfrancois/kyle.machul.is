title: Keepon Hacking and Kinect Control
slug: keepon-kinect-control
template: project

Reverse engineered a MyKeepon robot toy. Tapped the i2c bus to map
commands, then wrote an Arduino based firmware [KeepOff](http://www.github.com/qdot/keepoff) to control
the bot via USB.

Kinect control was a rapid prototyping project to make an interesting
demo for the [KeepOff MyKeepon Reverse Engineering project](http://www.github.com/qdot/keepoff).

Uses:

- [Arduino + Keepoff](http://www.github.com/qdot/keepoff) - Control of Keepon Robot
- [Processing](http://www.processing.org) - tying the whole thing together
- [OSCP5](http://www.sojamo.de/oscP5) - talk to python script that’s
  controlling arduino, already had that written so didn’t write serial
  controls in Processing
- [GSVideo](http://gsvideo.sourceforge.net) - for webcam (filming keepon)
- [SimpleOpenNI](http://code.google.com/p/simple-openni) - kinect
  recording and skeleton tracking in processing
- [libfreenect](http://www.openkinect.org) - Cross platform kinect access
- Processing running on Linux

The goth dance is a running joke from the Art and Code conference at
CMU, held October 2011. For those not familiar with the youtube meme,
see http://www.youtube.com/watch?v=PvNrjcg3WjA.

[BeatBots](http://www.beatbots.net), the company behind the MyKeepon,
took the KeepOff code and improved upon it to create the
[MyKeepon Library](http://github.com/beatbots/MyKeepon), which is now
the standard library for Keepon control.

