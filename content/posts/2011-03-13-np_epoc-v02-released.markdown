title: np_epoc v0.2 released
date: 2011-03-13 23:12:09


Did some work this weekend on making np_epoc a little more usable,
since v0.1 had VID/PID and encryption keys hardcoded to the headset I
have.

<a href="http://www.flickr.com/photos/qdot76367/5080605788/" title="np_epoc by qdot76367, on Flickr"><img src="http://farm5.static.flickr.com/4013/5080605788_eb455a1daa.jpg" width="410" height="500" alt="np_epoc" /></a>

VID/PID and key are now selectable by users. You can also get a device
count to make sure you have the VID/PID pair set up correctly.

Hopefully key and ID detection will be done by [emokit][1] soon, but
that's going to take a little more work since we're not yet sure how
the key is deduced on connection.

[Binaries are available on the sourceforge NP Labs release site.][2]
Currently I've only got OS X 10.6 Max 5 binaries up. Pd has been
tested on linux, works fine, but the source package is... not the best
at the moment, so I'll hopefully have OS X and Linux Pd binaries up
soon. I'm still trying to figure out how I'm going to build the
binaries for windows at all, since VS10 is giving me some problems
against flext.

[1]: http://www.github.com/qdot/emokit
[2]: https://sourceforge.net/projects/nplabs/files/np_epoc/0.2/
