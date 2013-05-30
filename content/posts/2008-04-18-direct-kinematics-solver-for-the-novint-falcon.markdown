title: Direct Kinematics Solver for the Novint Falcon
date: 2008-04-18 00:07:59 

[![OpenGL Falcon Direct Kinematics Solver][1]][2]

I swear this makes more sense if you actually see it moving, but nonetheless, I now have a neat little DK simulator for the Novint Falcon, actually _controlled_ by the Falcon itself. The buttons on the falcon can rotate/zoom the camera on the model. The triangle in back in the fixed frame (which I have NO idea on the size on, since the falcon is weirdly setup. That's partially why I created this simulation, so I could just change numbers until things seem right.), the three big white spheres are the knee positions, and the one out in front is the end effector origin. 

Outside of the fact that the simulator can't reliably pick which solution it wants to use (meaning sometimes it thinks the end effector ends up behind the fixed frame, oops), and that it's not mirroring the exact wonky angles the Falcon axes come out at, it works! And all in under a day's work. Not bad for being a little rusty on my OGL. 

   [1]: http://farm4.static.flickr.com/3200/2422071335_9eb017d3f7.jpg
   [2]: http://www.flickr.com/photos/qdot76367/2422071335/ (OpenGL Falcon Direct Kinematics Solver by qdot76367, on Flickr)

