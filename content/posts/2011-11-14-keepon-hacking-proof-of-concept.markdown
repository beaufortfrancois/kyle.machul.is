title: Keepon Hacking Proof of Concept
date: 2011-11-14 00:12:09

We have Keepon control!

http://www.youtube.com/watch?v=P0u2lakH5nc

Yay! Thanks to [mAngO on the comment thread for my last keepon post](/2011/11/09/mykeepon-hacking/#comment-359766077), we now know that grounding out the bus during keepon's powerup allows you to act as the master to the bus! This means we can now control the motors and sound, as can be seen in the video above. I'm just controlling motors there, using the [Control Program for Android](http://charlie-roberts.com/Control/) to send OSC messages to a python script I wrote. The python talks to the USB serial port, and the arduino turns the commands coming over serial into I2C to go to keepon.

All the source code for this is available in completely raw, uncommented form at

[http://www.github.com/qdot/keepoff](http://www.github.com/qdot/keepoff)

So, that's the first part finished. Now it's on to polishing things out and figuring out the rest of the parts of the hardware we don't have access to yet. I'm keeping [the github issues list](http://www.github.com/qdot/keepoff/issues) updated with things we have left to do.
