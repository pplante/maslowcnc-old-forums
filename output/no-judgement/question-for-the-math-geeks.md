## Question for the math geeks
Posted on **2017-05-05 06:59:52** by **gero**:

Would this approach provide enough information to calculate the dimensions of the machine?

The distance of the mounting points of the brackets measured.
1) drill a hole in the center of the sheet, the same diameter as the router bit
2) calibrate chain length
3) mount the sled and use the buttons to move sled, until you can push the bit into the drilled hole

---

Posted on **2017-05-05 08:16:37** by **blsteinhauer88**:

I actually do something similar.  I set the router on the chains to dead center, then I use the manual calibration.  The machine then sets that to 0,0.   At least it has been working for me.  If I use the auto calibrate, the router is not in the center of the sheet.

---

Posted on **2017-05-05 10:38:42** by **Bar**:

Technically I think we need to know motor spacing, sled attachment point spacing, distance to router bit, and center of gravity.  The motor offset from the top of the work area is used just to move where the (0,0) point is up and down so that doesn't factor into the real math, but wold move that center point.

My instinct is that we need n+1 equations to solve for n variables so I think for our 5 unknowns we would need 6 test points. That being said, it's not like we don't have estimates for the rest of those values so one point or two might be enough to give us "good enough" values.

---

Posted on **2017-05-05 19:30:11** by **jwolter0**:

If you have n equations and n unknowns, the system can be solved, at least in theory. If you have more equations than unknowns, then the system is indeterminate. Usually you can use the "extra information" as a check or a means to establish error estimates.

---

