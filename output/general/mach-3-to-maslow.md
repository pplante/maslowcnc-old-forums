## Mach 3 to Maslow?
Posted on **2017-03-28 16:28:23** by **jessbussert**:

So, I've used Mach 3 in the past and really like the UI and numerous features found within.  Can any of you code jockeys out there think of a way to modify a Maslow to be controlled by Mach 3?

The big challenge for doing so would be a complete rewrite of the Maslow firmware.  Maslow currently receives raw g-code as input while Mach 3 reads encoder signals and outputs logical steps/pulses.  As such, the Maslow firmware would need to be rewritten to emulate this control process.

It's been a long time since I messed with Mach 3.  At the time it was firmly rooted in a Cartesian coordinate system vs. Maslow's triangular approach.  I don't know how this might muck things up as well.

---

Posted on **2017-03-28 17:16:01** by **TheRiflesSpiral**:

Would it maybe be easier instead to describe the features you like about Mach 3 and see if Bar can emulate them? The architecture change sounds like a complete forklift of the existing code.

---

Posted on **2017-03-28 20:30:44** by **davidlang**:

detecting pulse signals and changing that to motor controls would be a very inefficient way of doing things. It would end up leaving a lot of the capabilities of the maslow on the floor (the ability to move faster for some sorts of things, being able to detect the tension needed, for example)

---

