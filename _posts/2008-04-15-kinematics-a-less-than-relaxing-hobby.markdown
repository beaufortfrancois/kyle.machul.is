--- 
title: "Kinematics: A Less than Relaxing Hobby"
date: 2008-04-15 00:31:01 -07:00
mt_id: 1180
layout: post
---
So, in my eternal quest to [understand every single god damn thing about the Novint Falcon][1] before ever using it for anything interesting, I've now dug up a bunch of information on Direct/Inverse Kinematic analysis of DELTA style parallel robots. Of course, at the end of all that digging, I found one paper that explains it pretty thoroughly.

[Descriptive Geometric Kinematic Analysis of Clavel's Delta Robot][2], P.J. Zsombor-Murray, McGill University

I'll be doing a "unwind the [retroencabulatoresque][3] wording" post later, but for those of you used to reading engineering/math papers, check out the "Rationale" section. It contains a really awesome abstract algebraic version of "go fuck yourself".

Anyways, this paper has one problem. The pictures at the end are... engineery. Very, very engineery. Unreadably so. So, I decided to spend a little time working in that whole Second Life thing that I spend all of my day job time on, except actually doing something creative in it.

[![Diagram of IK/DK Derivations for a Clavel DELTA Robot][4]][5]

And thus, my reworking of the IK/DK derivation, which is a hell of a lot easier to understand visually (basically: Expand everything out to constraint spheres, find the meeting points of 2 of those spheres, logic out which is the correct point of the meeting of the 3 to save yourself the unnecessary processing). This can be seen at http://slurl.com/secondlife/Hyperborea/160/45/23/

Oh yeah. And actually, two problems with the paper, now that I think about it. Bricks of BASIC are not helpful as code. Ever. And this is literal brick, too. Whitespace is for bitches.

For anyone else wondering about the Falcon; the paper above expresses the direct kinematics in terms of hip angles. However, the falcon's a little different. It gives you back encoder values from the motors, so you're stuck with a single integer value that relates to the extension distance of the thigh. This is due to one of the nice features of the Falcon, though. The bent extension thigh (versus usual static rotation-only bar thingy, or at least, that's my made up mechanical engineering term for it) gives you a smaller footprint for the workspace than usual haptics deltas would give you, which is important since this was made to go on a gamer's desk. It's probably a bit more rugged too, since those nice rotational sensors in $30,000 equipment probably weren't made to take cheeto dust either. So, good for you on that one, Novint.

Anyways, what that means is the encoder values refer to some point on a 4" arc that the knee traces on the hip constraint sphere, instead of an angle. You can either translate between those to get your angle back and plug into his code, or wait for me to just post my finished code here. The encoder value is probably a faster way to do this, too, since I'm betting you can avoid floating point math at some point with it.

This, of course, will all happen as soon as I decide to stop spending time making pretty pictures and posting about how proud I am of said pretty pictures. 

   [1]: http://www.nonpolynomial.com/archives/2008/03/everything-i-know-about-the-novint-falcon.php
   [2]: http://www.nonpolynomial.com/pdf/claveldelta.pdf
   [3]: http://www.youtube.com/watch?v=TD1LHejil6M
   [4]: http://farm4.static.flickr.com/3067/2415446632_2a7f2f9061.jpg
   [5]: http://www.flickr.com/photos/qdot76367/2415446632/ (Diagram of IK/DK Derivations for a Clavel DELTA Robot by qdot76367, on Flickr)

