## Weight Positioning
Posted on **2017-07-15 19:03:44** by **cameronswartzell**:

Thought I'd start a thread on weight positioning. Firstly, what is the function of the weights? Is it primarily to keep the sled flat to cutting surface? To make sure there is enough tension on the chain (seems like router weight alone is sufficient here)? To help correct the rotation of the sled due to tension differential? I'd like to know what the various reasons are for the added weight, so we can think how it can best be distributed. 

The current design has all the weight below the cutting bit. To me, and this is just intuitively, there are three obvious candidates for positioning: 
A) Two weights they are in Bar's unit, at say 4 and 8 o'clock. I could see this being useful if having the weights on either side help maintain the orientation of the sled with 6 o'clock pointed straight down to the ground)
B) A single weight with its center of gravity directly below the cutting point. Somewhat easier to mount if separation of the weights doesn't buy us anything, but having the weight below the cutting point IS important.
C) Weight in such a way that the center of gravi ty of the sled is as close as possible to the center of the cutting bit. This would, of course, be harder to achieve, but building a heavier balanced sled may eliminate the need to add weights.

---

Posted on **2017-07-15 19:08:16** by **cameronswartzell**:

According to David's modified simulation.py, placing the CG at zero A) does not crash anything as I was worried it might, and B) indicates that a CG at zero distance from the bit is not any more affected by measuring errors to the CG than the default CG distance (79mm).

---

Posted on **2017-07-15 19:21:34** by **davidlang**:

the bricks are to add weight to keep enough tension on the chains, and enough side force on the sled so that it moves rather than sticks.

The current sled puts the weight below the bit, but this is a convenience for mounting, and a legacy of the early X shaped sled (symmetry of the sled with the chain anchors on the top arms and the bricks on the bottom arms)

we have not really explored different sled geometry. I think it would be very interesting to explore where the chains , bit and CG are all in line (it would simplify the math significantly)

---

