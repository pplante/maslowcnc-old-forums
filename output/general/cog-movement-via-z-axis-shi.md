## CoG movement via Z-axis shift
Posted on *2017-06-10 07:32:40* by *mrfugu*

Just spitballing here, but is Maslow calculating the change in CoG via z-axis movement?

I'm no physicist but I assume Maslow would need to know about the Router Weight vs (Sled+Brick Weight) in order to come up with something close to accurate.

I imagine the router has enough mass that an approx 1"  change from  Safe travel height and the bottom of a 3/4" cut piece could be as much as 15+% of the total height of the sled assembly, surely that could change the overall CoG somewhere in the >milti-mm range.. 

thoughts?

---

Posted on *2017-06-10 12:00:44* by *davidlang*

the weight of the sled cancels out in the position math, so it's not something we have to measure.

the height of the CG from the workpiece should not matter, the position math is 2d, not 3d. the Z axis will not change the position of the CG from a 2D perspective.

---

