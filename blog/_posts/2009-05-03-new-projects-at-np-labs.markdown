--- 
title: New Projects at NP Labs
date: 2009-05-03 13:44:51 -07:00
mt_id: 1208
layout: post
---
<CENTER><a href="http://www.flickr.com/photos/qdot76367/3497299795/" title="Workin on new toys by qdot76367, on Flickr"><img src="http://farm4.static.flickr.com/3316/3497299795_6293533843_m.jpg" width="240" height="180" alt="Workin on new toys" /></a></CENTER>

Well, another 6 months have come and gone, and I've got a few new projects on the radar here.

<A HREF='http://www.github.com/qdot/libomron'>libomron</A> 

This is a framework for accessing the USB capabilities of Omron medical equipment, specifically the <A HREF='http://www.amazon.com/Omron-HEM-790IT-Automatic-Pressure-Management/dp/B000O58QM0'>Omron 790IT Blood Pressure Monitor</A> at the moment. There has been some talk online about accessing their pedometers in a cross platform manner (reference: <A HREF='http://www.dullest.com/blog/my-favorite-pedometer-omron-hj-720itc/'>dullest.com</A>), and I'm hoping the protocol for that and their other blood pressure monitors are basically the same, so I can extend the protocol parsing to the whole family of products.

<A HREF='http://www.github.com/qdot/libambx'>libambx</A> 

libambx is an open source, cross platform library for the <A HREF='http://www.ambx.com'>Ambx ambient environment feedback system</A> that I'm working on in conjunction with the people at <A HREF='http://electrosthetics.blogspot.com/'>Electrosthetics</A>. I'm currently working on reversing the ambx communications protocol (<A HREF='http://qdot.github.com/libambx'>document available here</A>). It's nice to work with someone else on this stuff for once.

<A HREF='http://www.github.com/qdot/libnifalcon'>libnifalcon updates</A>

libnifalcon is still coming along nicely, if a bit slow at the moment since I'm stuck on some rather difficult problems with firmware loading and kinematics. It's been used in a couple of papers (<A HREF='http://insectbot.rsise.anu.edu.au/pub/doc/papers/virtual_force_feedback_teleoperation_of_the_insectbot_using_optic_flow-acra08.pdf'>including this one on teleoperation of an insectbot</A>), and there's also been some work on <A HREF='http://www.chai3d.org'>porting it to Chai3d</A> for use in the <A HREF='http://idmil.org/software/dimple'>Dimple environment for physical interaction with sound</A>. 
