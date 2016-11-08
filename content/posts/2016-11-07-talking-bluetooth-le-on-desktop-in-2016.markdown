title: Talking Bluetooth LE on Desktop in 2016
date: 2016-11-07 17:50:27
slug: talking-bluetooth-le-on-desktop-in-2016

![Bluetooth LE](/images/2016-11-07-talking-bluetooth-le-on-desktop-in-2016/btle.jpg)

I am sorry. I am so, so sorry.

Every so often, I decide "Gosh, I'd really like to write code for some
Bluetooth LE devices, but I don't really do much on mobile. Maybe
things have gotten better on desktop!" So far, I have been
disappointed every time. Now is no exception, but I've decided to
actually write down that disappointment as a form of therapy. 

This post will go over how different desktop OSes, libraries, and
hardware deal with Bluetooth LE. I'm sticking to desktop here because
product manufacturers assume BTLE devices will usually be used with
phones. Mobile certainly isn't a solved problem either, but it's
better than desktop right now.

This article isn't an introduction to BTLE itself. I'm going to assume
readers know the basic terms and differences between, say, pairing and
connection. If you're not familiar, I recommend checking
out
[Adafruit's BTLE Intro.](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/introduction) Apple's
[CoreBluetooth Overview](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothOverview/CoreBluetoothOverview.html#//apple_ref/doc/uid/TP40013257-CH2-SW1) has
some nice explanation also, though the examples are obviously platform
specific.

## Operating System Support

### OS X

Starting off easy. OS X has had support as a BTLE Central Node since
10.6, and as a peripheral node since 10.9. Done!

### Linux

tl;dr: Bluez < 5.38 or so, use gattlib. Bluez >= 5.38 or so, use dbus.

And then right on up the difficulty curve to Linux, where we
have [bluez](http://www.bluez.org/). I've yet to ever hear anyone say
"yay bluez!"

Bluez got BTLE support in 4.93 or so. As of this writing (November
2016), we're at 5.43. That's a full major version and a ton of minor
versions difference.

Between bluez 4 and 5, APIs moved from direct access to dbus. Then,
within DBUS 5, the methods have changed multiple times. I spent part
of last weekend trying to write some dbus code for accessing BTLE
devices with no luck, as I couldn't seem to identify services on the
device. It turns out that I'm on debian Jessie, which comes with dbus
5.23 (released September 2014) . After looking around a bit, it seems
most current bluez supporting libraries expect users to have at least
5.38 or higher, and sure enough, those expose different methods.

I was pretty confused by this, as I'd been
using [pygattlib](https://bitbucket.org/OscarAcena/pygattlib) with no
problems on the same linux box to write some BTLE test scripts. Turns
out, pygattlib is similar to the
C-based [gattlib](https://github.com/labapart/gattlib). Both of these
use the GATT functions from gatttool in the bluez 4 line to talk to
BTLE devices without having to go through dbus, to let older
machines/kernels talk BTLE. That's why things worked, because it was
just bypassing the dbus interface.

### Windows

tl;dr: Either hope your device requires pairing, or your code can deal
with WinRT APIs and will only run on updated Windows 10. Otherwise, do
something crazy.

Windows started supporting communicating with BTLE as of Windows 8.
However, this didn't mean you could just go talking willy-nilly to any
device you pleased. You actually had to pair with devices before they
were available to functions.

The problem is that device manufacturers are lazy and cheap, and
pairing is an optional part of the BTLE handshake process. It's also
the part that's vaguely secure, but a lot of products don't really
care about that. For many devices, you just connect, query for
services, and off you go. This is possible on both OS X and Linux, but
on windows, it was a no-go up until Windows 10 update in November
2015.

As of that update and more additions during the Anniversary update in
August 2016
(thanks [@kraln](https://twitter.com/kraln/status/795851296171589633),
WinRT started providing functions to connect without pairing, which is
how some of the platforms listed in the next section are going to
tackle this. There mention
of
[support for APIs in early 2017](https://github.com/sandeepmistry/noble/issues/84#issuecomment-181632491),
but the only source I can find for that is a comment on a bug, and I'm
not sure if that's redundant with respect to the WinRT claims.

There is one other workaround for BTLE on windows, even for
pre-windows 10 platforms, but it's not pretty. Check out the section
below on Noble for more information.

## Cross-Platform ways to access BTLE currently

Given those warnings, if you still want to access bluetooth in a
pre-written, cross-platform way, here's a few choices. This is by no
means an even partially complete list of bluetooth wrappers/libraries,
it's just what I looked up while figuring all this out..

### Qt (C++)

Qt was actually one of the first places I went to check for this, as
they're usually pretty good about supporting as much functionality as
possible across platforms.

[Qt has had support for BTLE on OS X, Linux, Android, and iOS since 5.7](http://doc.qt.io/qt-5/qtbluetooth-index.html).
Notice the lack of Windows
there?
[Looks like they'll get WinRT in 5.8, "platform" support "later".](https://bugreports.qt.io/browse/QTBUG-31674)

### WebBluetooth

There is currently
a [proposed spec](https://webbluetoothcg.github.io/web-bluetooth/)
being implemented by Google in Blink (the browser engine that backs both
Chrome and Opera) that will allow webpages to interact with BTLE
devices. This is slated
to
[ship behind a flag in Chrome 54](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/Ono3RWkejAA).
It will support Linux, OS X, Android, and ChromeOS. Windows is
apparently coming with WinRT later.

Currently,
[Edge has no stated plans to implement WebBluetooth but it is "Under Consideration"](https://developer.microsoft.com/en-us/microsoft-edge/platform/status/).
[Mozilla is pushing back on spec implementation in Firefox due to privacy concerns,](https://bugzilla.mozilla.org/show_bug.cgi?id=674737),
though [work is happening in Servo](https://szeged.github.io/servo/).

So while this API may show up in Chrome, it may also ONLY show up in
Chrome. This situation certainly hasn't stopped anyone from using APIs
before, though.

And for anyone that is saying "Wait, Kyle, didn't you implement one of
the Bluetooth stacks for FirefoxOS? What about that?", my reply is
"DON'T MENTION THE WAR." (Translation: That was an early version of a
non-standardized API that has since been removed from Gecko, Mozilla's
browser engine)

### Noble (Node.js)

[Noble](https://github.com/sandeepmistry/noble) is a node.js BTLE
library that supports OS X, Linux, and Windows.

Yes, Windows. Without WinRT. Crazy, right?

Well, yes. It actually is crazy. To use Noble on windows (which many
IoT/Maker programs do), you have to
install
[WinUSB drivers over the standard Bluetooth Dongle drivers](https://github.com/sandeepmistry/node-bluetooth-hci-socket#windows).
Noble then handles the full bluetooth stack for you, bypassing the
connection/scanning APIs missing from regular old windows. While a
clever way to do that, it's not exactly something you'd want to ship
to non-savvy end-users.

### BGAPI

Some people aren't happy to just bitbang bluetooth to a dongle though.
Instead, they go all the way and implement a specialized API
specifically for their dongle.
The
[BlueGiga BLED112 BTLE Dongle](http://www.silabs.com/products/wireless/bluetooth/bluetooth-smart-modules/Pages/bled112-bluetooth-smart-dongle.aspx) comes
with a special, proprietary API that allows users to connect to BTLE
devices on Windows (and other platforms), also routing around the lack
of OS API functionality. So, as long as your platform can talk USB, it
can also talk BTLE.

(Found this dongle
via
[an article on the PyGATT library](http://christopherpeplin.com/2015/10/22/pygatt-python-bluetooth-low-energy-ble/),
which supports both Linux dbus and BGAPI for cross platform python
bluetooth support).

## Conclusion

Well, that's the state of things for the moment. Those are some of the
reasons there's no [libusb](http://libusb.info)-equivilent for
bluetooth yet. Hopefully we'll see Microsoft fill out the Windows API
surface soon and make this article a little less sad, 'cause the WinRT
stuff is kinda painful. Until then, though, this is what we get to
deal with.

Thanks to [Sandeep Mistry](http://twitter.com/sandeepmistry) for
filling in some of the details on the Windows situation.

PS Oh, yeah, [almost forgot FreeBSD](https://github.com/takawata/FreeBSD-BLE)
