title: XIO - Novint's Gaming Exoskeleton
date: 2011-04-24 22:12:21


I'm not really used to writing about hardware that's hardly to
prototype stage yet, but damn, I cannot wait 'til this comes out so I
can start reverse engineering it.

[Novint][1], the company that manufacturers the [Falcon][2] haptic
device (that I wrote/maintain the cross-platform [libnifalcon][3] for
- if you aren't familiar with the falcon,
[check out this rather exhaustive article I wrote on it a couple of years ago][8]),
recently announced a merger with another company.

The other company in the deal, Forcetek Enterprises, doesn't even seem
to exist outside of the PR about this merger (*UPDATE:*
[Ok, I actually found their old website finally.][9] Apparently this
was shown at E3?). Successful stealth mode.

What came out of the merger...

<CENTER><A HREF='http://novint.com/index.php?option=com_content&view=article&id=76&Itemid=178'><IMG
SRC='http://images.nonpolynomial.com/nonpolynomial.com/blog/xioarm.jpg' /></A></CENTER>

is a partial exoskeleton for gaming.

The XIO is a sleeve exoskeleton that allows you to feel forces
throughout the arm, versus just through the hand like the Novint
Falcon. There is actuation along the arm and elbow, meaning much
larger force distribution and a much more immersive feel. In applied
terms, this means that you'll be able to feel things like gun kickback
all the way through your shoulder, versus just your hand. You can also
do interesting things like simulating weight and fatigue in the arms
by restricting certain movements.

This combined with depth cameras like the kinect could be HUGE.
Players would have both full body tracking AND at least partial body
actuation, which is better than the "flail without feedback" option
we've had for years with the Power Glove/P5/Wiimote/Kinect/Move.

The demo video below shows a full VR rig built from consumer
hardware, using

* Vuzix HMD
* XIO
* [TNGames Third Space Vest][5] ([Which I also write drivers for!][4])
* Some new gun controller

<CENTER><object width="480" height="390"><param name="movie" value="http://www.youtube.com/v/lV3j2Yxv7jY?fs=1&amp;hl=en_US"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/lV3j2Yxv7jY?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="390"></embed></object></CENTER>

The XIO is supposed to integrate with Novint's _F-Gen_ drivers. F-Gen
is an abstract programmer layer (similar to [GlovePIE][7]) made to
implement haptics on top of arbitrary games, instead of doing direct
game integration (which Novint has with things like Source Engine
games and the Penumbra series). This allows users to possibly script
haptics to whatever game they want. How well this works, I have no
idea, but it means that any game the falcon supports should also be
supported by the XIO on release.

Novint's yet again done a horrible job of the PR with this one, as it
looks like no one has really picked up the news yet even though the
press release happened over a week ago, and now all of the images on
the front page of their site are broken. [Novint's CEO even changed his
twitter account on the launch][6] for reasons I'm not real sure
of. 

That said, I've been incredibly happy with Novint's quality of
engineering on the Falcon. Novint knows how to make extensible
hardware, as they've shown with the grip and firmware system on the
falcon. It was a joy to reverse engineer, and I'm hoping that follows
onto this as well. I can't wait to get my hands on (and in) the XIO.

[1]: http://www.novint.com
[2]: http://novint.com/index.php?option=com_content&view=article&id=39&Itemid=175
[3]: http://www.github.com/qdot/libnifalcon
[4]: http://www.github.com/qdot/libthirdspacevest
[5]: http://www.tngames.com
[6]: http://www.twitter.com/tomlucient
[7]: http://sites.google.com/site/carlkenner/glovepie
[8]: http://www.nonpolynomial.com/2008/03/25/everything-i-know-about-the-novint-falcon-as-of-march-2008/
[9]: http://www.forcetekusa.com/
