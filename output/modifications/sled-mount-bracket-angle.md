## Sled Mount Bracket Angle
Posted on **2017-03-27 06:48:53** by **jknox**:

I did a little layout with the sled in extreme positions on the cutting area and I discovered that the mount brackets were more often too close together and rarely too far apart (The assumption I'm working with is that getting the chains to point directly at the center of the sled is best, but that's just what seems right to me). Here's the [original sled](//muut.com/u/maslowcnc/s2/:maslowcnc:JGLX:sledanglesoriginal90.jpg.jpg), when the sled it at the top center the chains will pull outward 33 degrees out of alignment with center, and at a lower corner they pull inward 13 degrees out of alignment. By changing the included angle between brackets on the sled from 90 degrees to 110 degrees these worst case out of alignment issues balance out. Here's a [modified sled](//muut.com/u/maslowcnc/s2/:maslowcnc:oYE7:sledanglesmod110.jpg.jpg), the same worst case locations are pretty much even, and at the center neutral position it's almost perfectly aligned.

I would guess that with a square work area 90 degrees would be fine, but since our work area is wider a wid er mount angle may work better, what do you all think? Also, will this affect the math controlling the sled, or will performing the normal calibration take care of it?

---

Posted on **2017-03-27 08:43:19** by **Bar**:

Great work!

I don't think the math should be affected because what is important for the math is just the anchor points spacing, but I thin that the chain will behave better with the angle wider. Part of me thinks that because the chain can flex there the difference will be small, but I'm really not sure.

What type of test can we do to compare performance?

---

Posted on **2017-03-27 09:29:53** by **jknox**:

My guess is that the sled will twist slightly less since the force is being applied more in line with the center (in most locations). And perhaps that twisting will have a little less effect on router location since it will twist slightly closer to the center of the sled. But, if nothing else it'll just put less sideways force on the L-brackets.

---

Posted on **2017-03-27 09:30:33** by **Bar**:

I agree.

---

