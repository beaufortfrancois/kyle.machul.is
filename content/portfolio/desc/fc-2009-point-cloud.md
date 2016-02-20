title: FC 2009 Point Cloud
slug: fc-2009-point-cloud
template: project

Assuming you were at Further Confusion 2009 and around during the
fursuit parade, you may've seen a beat up truck with some spinny
things on it. Or, you may've been in a fursuit and told to get in a
line around the median and then a guy with a bullhorn walked around
and yelled "HOLD YOUR POSE" constantly without really explaining what
was going on. Or, maybe you weren't even there.

You should've been. It was fun.

Either way, this page should answer any questions you have about the
above paragraph.

# The Event<a id="orgheadline2"></a>

The follow story took place at
[Further Confusion 2009](http://www.furtherconfusion.org/fc2009/), a
yearly furry fandom convention held in San Jose, CA. Specifically,
this happened during the fursuit parade (for those not familiar with
fursuit parades,
[there's a description here](http://en.wikifur.com/wiki/Fursuit_parade).
Ignore the footnote. I totally count.). To say the experience is
surreal is an understatement.

[![img](/portfolio/img/fc-2009-point-cloud/post-parade.jpg "[Image via Kyreeth/Tugrik](http://www.furaffinity.net/view/1961292/)")](http://www.furaffinity.net/view/1961292/)

At the 2009 con, there were 530 suits in the parade, and over 2500
attendees overall.

I've been going to Further Confusion for the past 3 years (for the
record,
[I'm a cube](http://www.flickr.com/photos/qdot76367/366743514/in/set-72157594495327675/)),
and it always ends up being an interesting time. While I was working
at [Linden Lab](http://www.lindenlab.com), I ran the Second Life
panel, which was one of the few times I was subjected to real life,
phsyical griefing attacks. In 2006, I managed to
[video a line dance](http://www.youtube.com/watch?v=y9pCuRHmQvw),
[get sued for doing so](../electric-slide-lawsuit) and then thanks to
the EFF, win the case and open source the dance under the Creative
Commons License. I even have
[a cubesuit](http://www.flickr.com/photos/qdot76367/367648572/in/set-72157594495327675/)
that I wear in the fursuit parade, which, in 3 years of use (sadly, as
of 2009, the cubesuit is dead. Long live cubesuit v2, to be seen at
FC2010) has somehow has not gotten me beaten senseless by everyone
else in the parade. *Yet.*

Like I said. Interesting time. I just couldn't let this year go by
being any less interesting.

# The People with the Truck<a id="orgheadline3"></a>

The scanning system was created by [510 Systems](http://www.510systems.com), a navigation,
robotics, and controls research lab located in Berkeley, CA, who I was
working for at the time. They research and create solutions related to
problems in high accuracy navigation, surveying, and geographic data
analysis.

Or, more to the point, there's some robotic bulldozers and cars that
drive themselves and lasers. Lots of lasers.

To give you an idea of some of the things this company has done:

-   [Velodyne LIDAR Processing on the Radiohead House of Cards Video](http://code.google.com/creative/radiohead/)
-   [Work on the self-driving PriBot that was featured on the Discovery Channel's Prototype This](http://news.cnet.com/8301-11386_3-10042320-76.html?tag=newsLeadStoriesArea.0)

They also have vehicle mounted systems that can create a 3D "point
cloud" of the area surrounding the vehicle, through a combination of
specialized hardware, sensors, and processing software. It looks
something like this.

[![img](/portfolio/img/fc-2009-point-cloud/510building_cloud.jpg)](http://www.510systems.com)

The week before FC2009, I was telling some of my con stories to a
couple of coworkers over lunch. After explaining the fursuit parade, I
joked that we should take one of our scanning vehicles and create a 3d
scan of the fursuit parade. To my surprise, this got a positive
reaction, plans were made, and come Saturday, the truck showed up.

Holy crap, we were actually gonna do this thing.

# The Truck<a id="orgheadline4"></a>

This is the truck, and more importantly, this is our system that is
attached to the truck.

![img](/portfolio/img/fc-2009-point-cloud/truck1.jpg)

And from the side:

![img](/portfolio/img/fc-2009-point-cloud/truck2.jpg)

The rig in those pictures consists of (to get an idea of placement, go
to the flickr picture in the first link):

-   IP-S2 Integrated Positioning System
    -   The heart and brains of the operation. This is the box everything
        connects to. The box takes all of the data coming from all of the
        sensors, timestamps it with a very accurate timestamp, and sends it
        out a network port to be logged on a computer.
-   Velodyne LIDAR
    -   A 360 degree spinning LIDAR with 64 lasers. Capable of spinning at
        between 5-15 rotations per second, and outputting ~1.5 million
        points per second, each with a maximum distance of ~180m. Each
        point represents a distance in space with a certain amount of
        reflectivity. For example, the LIDAR can tell you that when a
        laser fired, it was rotated at 34 degrees from top, and that there
        was something 64.21m away at that distance, with a reflectivity
        based on whatever the laser bounced off of. For more information,
        see the [House of Cards Making-Of Video](http://www.youtube.com/watch?v=cyQoTGdQywY&hl)
-   SICK LIDAR
    -   In this specific case, ~90 degree LIDAR. Pointed at the street,
        and not rendered in distributed point sets. Unless you really want
        accurate shots of the street
-   GPS
    -   For positioning of the vehicle. Most everyone is familiar with
        these nowadays.
-   IMU
    -   An IMU is made up of 3 accelerometers and 3 gyros. It gives you an
        idea of which direction you're headed, and how you're rotated
        while heading that direction.
-   Wheel Encoders
    -   Attached to the hubs of the back wheels. Gives you information
        about exactly how fast you were going at a point in time.

This isn't all the sensors the IP-S2 can handle, but reflects the set
we had on the truck that day. As the truck is driven around, all of
the sensors listed above feed data into the IP-S2, which then feeds it
into another computer. All of this data is very, very accurately
timestamped.

# The Data<a id="orgheadline5"></a>

What does this get us?

-   The ability to reconstruct what's around us at a certain time. We
    can take our place in the world as found by the GPS at time A, match
    that with a laser scan taken as close to time A as possible, which
    gives us distance, and use math to give back a geographically
    referenced version of that point. Multiply that times thousands if
    not millions of points, and you can have a 3D model of a town with a
    single drive through. Images taken by a system controlled camera can
    also be matched to this model so that it can be colorized (like in
    the image in the point cloud image earlier in this document).
-   If GPS drops out, as it often does in environments with "things" and
    "stuff" (especially of the tall, opaque variety) in them, we can use
    the rest of the sensors to approximate our position. We do this
    using [magic](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=10668).
-   Much, much more, but this is about a specific event, not the system
    in general, so I'll stop. But it's freaking awesome, isn't it?

To give you an idea of uses for this system&#x2026; Say you're a department
of transportation, and you want to know where your streets are
painted, with what, and if they need to be repainted. Now, you could
send drivers out to eyeball this. But, with the system above, when all
of the data comes back together, you can see things like this:

![img](/portfolio/img/fc-2009-point-cloud/streetpc.jpg)

The scan above is from the Doubletree Hotel parking lot, taken during
the parade. Each one of those points that make up the image scan is
georeferenced, and you can see both the old arrow and the newly
repainted ones. With some processing, you can even have software pick
out features these features, and possibly have it give back a rating
of the quality, so that if something needs to be repainted, the
software can add that to a schedule automatically.

![img](/portfolio/img/fc-2009-point-cloud/screenshot.jpg)

Or you can take scans of people in fursuits. Isn't living in the
future fun?

# The FC Scans<a id="orgheadline9"></a>

Ok, down to business. Here's the information on the scans we took at FC.

## Scan 1 - Pre-fursuit Parade<a id="orgheadline6"></a>

![img](/portfolio/img/fc-2009-point-cloud/kmlrun1.jpg)

-   **Point Count:** ?
-   **Information:** Taken before the fursuit parade, while the lineup was
    just starting. Interesting view of the back area of the hotel. This
    honestly ends up looking more like a zombie attack than a fursuit
    parade, especially when played in real time.

## Scan 2 - Pre-fursuit Parade<a id="orgheadline7"></a>

![img](/portfolio/img/fc-2009-point-cloud/kmlrun2.jpg)

-   **Point Count:** ?
-   **Information:** Taken while the fursuit parade was entering the
    hotel. The honking was not our fault: blame the wolf in the dragon
    suit. :)

## Scan 3 - Post-fursuit Parade<a id="orgheadline8"></a>

![img](/portfolio/img/fc-2009-point-cloud/kmlrun3.jpg)

-   **Point Count:** 331 Million Points
-   **Information:** The cloud that's been in the pictures and videos so
    far. This was taken after the fursuit parade, when all of the
    suiters were lined up around the median in the parking lot. 3 sets
    of scans were taken of this (once clockwise around, two
    counterclockwise around).

# What data is available?<a id="orgheadline10"></a>

Before we can go into what can be done with the data, we need to
discuss what data is available. The data is presented on a per-point
basis, but the main question, what data can be used where? Well, let's
take a look at a couple of pictures.

![img](/portfolio/img/fc-2009-point-cloud/hocviewer.jpg)

This cloud is made up of 5 million points, about the maximum the House
of Cards Renderer (see the Available Software Section) can handle
before choking. We call this number our point budget. Now, you're
probably saying /"BUT I CAN RUN THE CRYSIS ENGINE AT MAXIMUM WHY
CAN'T I RENDER MANY POINTS WAAAAAAAAAAAAAAH."/. Well, get ahold of
yourself. When rendering point clouds, it's a completely different
ballgame. Since the points are disconnected, you can't use point
indexing. Since there's no polygons, there's none of the pipeline
optimizations inherent in using triangles. Of course, there's
solutions for these problems, mainly having to do with spacial data
structures and compression that can easily deal with hundreds of
millions of points, but since the easiest way for everyone on every
platform to view the clouds was using the prewritten, Processing (and
therefore java) based House of Cards viewer&#x2026; Well, there you go.

So, yeah, 5000000 points up there. If you look at the larger version
of it (available on flickr), you'll notice that we're blowing a TON of
our point budget on the large, flat surfaces in the surrounding
world. The road, the hotel, things like that. Now, a point reduced
version.

![img](/portfolio/img/fc-2009-point-cloud/fullrun.jpg)

This is a zoomed out version of the full first pass of the fursuit
parade. This *whole view* is only 3,405,808 points. This was
created by isolating the usable scan angles to a 30 degree arc, and
limiting the maximum acceptable scan distance to around 5m from the
sensor position at the time of laser firing. This still gets all of
the suit data into the cloud, while eliminating the road, the hotel
detail, other people, etc&#x2026;

Now, this data can sometimes be interesting. For instance, this shot
taken during the second run:

![img](/portfolio/img/fc-2009-point-cloud/demo.jpg)

This shot got the whole back of the hotel, which, while filling up the
point budget quick, looks really cool.
