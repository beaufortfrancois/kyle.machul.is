title: Using A Firewire Phantom Omni on Windows 8/8.1/10
date: 2016-10-03 19:31:28
slug: using-a-firewire-phantom-omni-on-windows-8-10

![Sensable Phantom Omni](/images/2016-10-03-using-a-firewire-phantom-omni-on-windows-8-10/omni.jpg)

Last weekend I decided to dust off my Sensable Phantom Omni (now
the
[3D Systems Geomagic Touch](http://www.geomagic.com/en/products/phantom-omni/overview),
but I bought mine before Geomagic bought Sensable and 3D Systems
bought Geomagic), and see if it was still usable. I had to order
a
[PCIe 1394b card](https://www.amazon.com/Syba-Firewire-XIO2213B-Components-SY-PEX30016/dp/B006DQ0KD2/),
but other than that, I hooked it up, and the Phantom drivers seemed to
install correctly on Windows 10. However, when running the Phantom
demo software, anytime a program tried to access the motors, the
program would crash. Sensor reading seemed ok, but I couldn't get any
feedback.

A quick call to the Geomagic Freeform support line turned up the
solution. As with many video products that used 1394b, the Phantom
Omni requires the "Legacy" firewire drivers. These were included with
Windows up to Windows 7, but as of Windows 8 and above, are no longer
included with the operating system.

[The legacy 1394 drivers can now be retrieved from the Microsoft Support Site.](https://support.microsoft.com/en-us/kb/2970191)

After installing the drivers and changing the 1394 PCIe interface to
use the Legacy drivers
([process documented here](https://www.studio1productions.com/Articles/Firewire-1.htm)),
I rebooted and the demos worked fine, with force feedback and all!

Along the way, I also found some information on repairing internal
cable breakage in the Omni, by a research team at John Hopkins
University. The original site had died, but the instructions and
images were still
available
[at this link via the Internet Archive](https://web.archive.org/web/20100621034327/https://haptics.lcsr.jhu.edu/Repairing_a_PHANTOM_Omni).

Anyways, hope this helps others that still want to get some life out
of their haptic controllers!
