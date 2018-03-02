## Rotating Sled Chain Mount
Posted on **2017-04-24 21:50:00** by **jbnimble**:

I was inspired by @jessbussert and @jknox in the thread where they [discussed @jessbussert's Maslow](https://www.maslowcnc.com/forums/#!/general:my-maslow-is-up-and-running). I started designing my sled in [OpenSCAD](http://www.openscad.org) based on the [sled in the repository](https://github.com/MaslowCNC/Mechanics/tree/master/SVG%20Files), and decided to add a [chain rotation feature](//muut.com/u/maslowcnc/s1/:maslowcnc:Q8rs:maslowsledbearingrotate.svg.jpg).

The pieces in the image would stack, and bearings would be flat on the upper surface and perpendicular on the lower surface of the sliders.

Let me know if you think this idea could be improved. I like that it simplifies the geometry, and theoretically might aid in minimizing kickback.

---

Posted on **2017-04-25 04:07:42** by **TheRiflesSpiral**:

I started down this path too...

https://muut.com/maslowcnc#!/modifications:my-idea-for-an-uber-sled

No machine to test it yet so it hasn't gone much farther than a sketchup drawing. :D

---

Posted on **2017-04-25 06:12:27** by **jbnimble**:

Nice! How did I miss that thread? Thanks for linking it. Your design is very similar to what @jessbussert was doing with the lazy susans. That VPlotter video was very good at explaining the basics, and well done.

My hope is to eventually have all the electronics/motors on the sled as a portable unit, we shall see.

---

Posted on **2017-04-25 06:38:47** by **davidlang**:

just a note on this approach, since there is nothing to stop the whole sled from rotating, I would expect that eventually the sled is going to rotate until it hits the limits of your movement (from the router torque)

while I think this is an experiment worth doing, I expect that if it does work any better than the existing sled design, improvements to the internal math should fix it. It's worth doing some experimenting with to see if it does show any flaws in the current math.

---

Posted on **2017-04-25 08:08:34** by **jbnimble**:

The bricks on the base should bring the sled back to a neutral point, right? I see your point that a big twist could hit the limit of the sliders, maybe some built in friction to slow the spin enough for the brick weight to right the sled.

---

Posted on **2017-04-25 08:13:17** by **scottsm**:

I think the bricks would affect the rotation and dampen the torque. If the bit is accurately centered, the effect on accuracy of some small amount of twist would be small.

---

Posted on **2017-04-25 09:08:37** by **TheRiflesSpiral**:

My intent for this simplified geometry is to account for unexpected positional inaccuracy. (Density changes in the material, a bit that's dulling, etc) Situations that would, if known, alter the geometry to account for it.

The internal math can't account for those things because they are unknown. Take a look here at about 4:09...

https://www.youtube.com/watch?v=heicyEEYcoM&t=208

Imagine that pen drawing over a rough surface... the torque lateral to the direction of travel will cause inaccuracy in position because the pivot point of the drive system is not incident with the end effector. Whereas with the geometry simplified, the forces are incidental, reducing positional error.

That's the theory anyway.

---

Posted on **2017-04-25 09:09:45** by **Bar**:

I think that makes a lot of sense

---

Posted on **2017-04-25 10:46:59** by **davidlang**:

it's looking like the bricks may not be needed (except in this sled design to try and prevent the rotation)

we'll have to see how much 'kick' can take place with different setups.

with a 1/4" bit making cuts less than 1/4" deep, I sure wouldn't expect any noticable kick. If you were using a large bit, deep cut, and agressive feed rate, I could see it happening, but I think that would also result in problems with the chain tension.

but the purpose of the beta cycle is to have people experiment and find these things out. "it works for me" beats theory any day. :-)

---

Posted on **2017-04-26 07:51:31** by **TheRiflesSpiral**:

If the bricks truly aren't needed, I would probably go back to my original design with just two pieces. The router is mounted to one of the arms and the other arm pivots around the router.

---

