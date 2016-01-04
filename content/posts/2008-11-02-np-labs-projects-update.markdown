title: NP Labs Projects Update
date: 2008-11-02 21:21:20

Wow. Almost 5 months between posts. I've been so busy on my projects that I have no time to write about them anymore. :)

First off, [libnifalcon][1], the open source driver for the [Novint Falcon][2], is currently in alpha stage for the v1 release, soon to move to beta after a few more bugs are fixed. It's already seeing some usage, too!

http://vimeo.com/2138448

The video above is a demo of a couple of patches for [PureData][6] written by Edgar Berdahl for use in [Physical Interaction Design for Music][8] class at the [Center for Computer Research in Music and Acoustics at Stanford University][9]. The video shows a haptic simulation of a bowed instrument, as well as a training patch for drum rolls. Moving toward the line in the middle of the window causes the falcon to kick back slightly, and the user must hold the end effector steady to keep the sound steady and constant. All of this is running on a beta version of the np_nifalcon external for max and pd, which is available on the libnifalcon site.

Next up is another project that I decided to throw together today to check out the [OpenSoundControl protocol][10].

http://vimeo.com/2138821

This is the [Kitelight system][14] controlled using the [mrmr OSC interface builder for the iPhone][15]. It's connecting to laptop running python using [liblo][16] and [pyliblo][17] for OSC controls. This goes through a [ xbee dev kit board][18] to [an arduino][19] with [xbee shield][20] which is controlling a panel of RGB LEDs attached to the kite.

Usable range on the zigbee is ~100m, more than enough room for flyer to kite communications. Now that this works, I can also run lighting commands from PureData to do music synchonization or whatever else I might think of. 

For all the URLs listed above, this project came together rather quick, about 90 minutes from start to finish, though obviously all the boards were already built, so it was just a matter of coding it all and learning OSC and mrmr. 

Now, back to working on getting libnifalcon released... 

   [1]: http://libnifalcon.sourceforge.net
   [2]: http://home.novint.com
   [3]: http://vimeo.com/2138448?pg=embed&sec=2138448
   [4]: http://vimeo.com/user154518?pg=embed&sec=2138448
   [5]: http://vimeo.com?pg=embed&sec=2138448
   [6]: http://www.puredata.info
   [8]: http://ccrma.stanford.edu/courses/250a/labs/lab6-Falcon/
   [9]: http://ccrma.stanford.edu
   [10]: http://opensoundcontrol.org/
   [11]: http://vimeo.com/2138821?pg=embed&sec=2138821
   [12]: http://vimeo.com/user154518?pg=embed&sec=2138821
   [13]: http://vimeo.com?pg=embed&sec=2138821
   [14]: http://vimeo.com/1392439
   [15]: http://poly.share.dj/projects/#mrmr
   [16]: liblo.sourceforge.net
   [17]: das.nasophon.de/pyliblo/
   [18]: http://digi.com/products/wireless/point-multipoint/xbee-series1-module.jsp
   [19]: http://arduino.cc
   [20]: nkcelectronics.com/freeduino-arduino-xbee-shield-kit.html

