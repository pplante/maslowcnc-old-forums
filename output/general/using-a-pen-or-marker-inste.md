## Using a Pen or Marker instead of a router
Posted on *2017-06-01 09:12:06* by *codyrutty*

Hello all! Has anyone had experience with using some sort of writing instrument as opposed to a router? I'm very interested in using this amazing device to draw with on substrates like panel and canvas. Secondly, is it possible to configure the Maslow to operate on a true 90 degree orientation for something like a vertical wall, or horizontal for, say, cement? Thank you in advance for any input! Eager to order but I wouldn't be using it for a router. 

Cody

---

Posted on *2017-06-01 09:19:51* by *gero*

A 90 degree would need some sort of vacuum to suck it towards the wall to get the pressure on the surface for a pen or paintbrush,

---

Posted on *2017-06-01 09:20:57* by *scottsm*

Hello Cody, welcome! I've used pens, in my case to test cuts before committing to wood :). The sled slides across the work area, and that could smear the substrate if the marks don't dry rapidly. The pens I use dry pretty much instantly. The jury is still out about a true 90 degree setup, but I think not. Horizontal even less likely, as gravity working against the two chains is an important part of the design.

---

Posted on *2017-06-01 09:36:20* by *davidlang*

There are a few other devices out there that are built to run pens. They can be much smaller and lighter than the maslow as a result. But they are also much more expensive (I saw one that was $950 for example) see the comments at https://www.youtube.com/watch?v=y60q6U7NjTQ&lc=z13hwvl4lzy2x15yq04cip2hipyug5wpwi0.1496082763852771 for pointers to some names to google for.

depending on how much force your pen needs to write, going to a vertical (or near vertical) layout should be able to work.

going to something horizontal (to mark concrete) would require a very different design. I would look at the hangprinter 3d printer design for that.

---

Posted on *2017-06-02 00:16:35* by *dkchris*

Wanting to draw up murials on building walls?  Sounds to me like that's what you might be up to ;). 
I'd think a solution where the motor pulleys are placed as close to the wall surface plane as possible (perhaps on a carrier scaffold or beam and facing in towards the wall), and the attachment points are placed a suitable distance out from the pen base/work surface in the Z direction to make the pull lines deliver the inwards force ought to work. The sled design and the pull line attachment points probably have to be changed to balance the pull forces wanting to tip the sled up over its top edge with the weight placement to make it work.
As an alternative to a pen I might suggest to consider something like a single action airbrush; it's not as sensitive to surface roughness, yet can still make a fairly fine line if adjusted correctly, and could be activated/deactivated as simply as applying power to a magnetic valve. The "pen down/up" timing might take a bit of experimentation to get right though, as an airbrush takes a couple of splitseconds to siphon up the paint.
 
So me of the problems with this approach would be:
1) Chains dont bend sideways and would derail. Youd have to base it on some sort of wire/cord solution. 
2) The Maslow compensation math isn't capable of calculating the effect of the ever-changing outward angle of the pull lines as is, as it's contstructed to keep all pull line/chain movements in a single plane. It's just math/trig though, so I guess you could modify the trig part of the open source kinematic math (not the dynamic stuff) to handle this if you want.

---

Posted on *2017-06-02 06:02:40* by *dkchris*

Afterthought: Actually the combination vertical std. Maslow setup + airbrush might work nicely as is, as required penforce would be literally zero. A little bit of vacuum to reduce overspray might not be a bad idea though.

For horisontal / floor work, something like the age-old computer-turtle might actually be the ticket. Fairly versatile without work area limitations, easy to move around and doesn't need a support structure. https://angrytechnician.files.wordpress.com/2009/07/turtle.jpg . https://upload.wikimedia.org/wikipedia/commons/0/07/Turtle_draw.jpg Only issue would be how to get from G-code to turtle movements. Or, alternatively, from design to turtle movements.

---

Posted on *2017-06-02 08:55:21* by *edou*

Would a self sharpening mechanical pencil work if it was tightened with a spring? (http://www.cultpens.com/c/q/brands/uni-ball/uni-pencils/uni-kuru-toga)

---

Posted on *2017-06-02 09:11:31* by *davidlang*

the error you would get from the angle of the chains from the wall is small enough to ignore

---

Posted on *2017-06-02 09:34:50* by *scottsm*

I've found that the mechanical pencil makes a pretty faint mark, but I didn't try many different springs for different pressures. I've been using gel pens.

---

Posted on *2017-06-05 08:19:47* by *dimtick*

there is a pen version of this.  check this out:
http://www.homofaciens.de/technics-machines-v-plotter_en.htm

---

Posted on *2017-06-05 11:12:53* by *TheRiflesSpiral*

Is it weird that I read that webpage in his voice? (He has a Youtube video demonstrating the finer points of this setup)

---

Posted on *2017-06-05 13:38:57* by *nathanmiller*

there was a discussion on this some time back. If you do a search on the forums I think you'll find a great discussion on mechanical "bits" that allow you to place a pen/marker into your router. It would give you x/y/z axis without major modifications/adjustments. The only thing you must make sure of, is don't turn the router on!!! Haa haa

---

Posted on *2017-06-22 12:47:18* by *woodchuck*

I have one of these and it's great for just this application, though maybe not as accurate as Maslow, but if vector art is all you're trying to create this might be what you're looking for.  http://www.polargraph.co.uk/

---

Posted on *2017-06-22 12:55:03* by *gero*

Wow, those bearings around the centre is chalenging! A round spindle with integrated Z-Moves and huge bearings would cataplut this project to space. But also would increase the cost drasticly. Interesting find. Thanks!

---

