## chain skips tooth or jumps sprocket - analysis and fix
Posted on **2017-04-05 20:00:18** by **jbarchuk**:

> scottsm9ha+2!

> ...the top center kept jumping the sprocket of the left motor – notice the stairstep path.

This is a few instances I've read about the chain skipping teeth. I have a few observations and suggestions.

The chain is fastened/anchored/attached at four points. (The 'floating sprocket' is irrelevant to this issue because it's not fastened down in 3 dimensions.)

I think...

1) The plane of the sprocket should dictate where the endpoints of the chain are mounted. I think the sprocket and chains going out from it in two directions should be as -parallel- as possible.

2) I think the typical non-parallel chains can cause skipped teeth.

3) Unless taken into account I think that the chains being not parallel to the sprocket can cause distortion of the cut path.

For reference, in the pic below are three of those four chain mount points. 

The red circle is the 'deck' or working surface.

The green circle at the bottom-left is the 'corner anchor.'

The green circle at the top-center is the motor sprocket.

The green circle on the sled bracket is the sled anchor.

I'm thinki ng about the distances in the z dimension from the motor sprocket to each mounting point, and the angles that that causes..

I'll use the deck, the red circle, as a reference.

The sprocket is located a few inches in front of the deck.

The corner anchor area is about 3/4" behind the deck.

The sled anchor, given the bracket provided and as I've seen in a few pics, is mounted 2-4" off the deck.

My biggest concern is the difference between the sled anchor to corner anchor, referenced from the sprocket, which are +3" and -3/4" respectively, which is a total delta of nearly 4 (or more) inches.

The result is that the chain is nowhere -near- in line with the sprocket.

The plane defined by the motor sprocket, floating sprocket, and cuphook anchor is fixed. The offset is there but that doesn't change.

When the sled anchor is at its -farthest- -distance- from the motor sprocket, the angle caused by not being inline is at its -smallest- value.

As the sled is pulled closer to a motor sprocket, to its -closest- distance, the -angle- created is at its -largest-.

Anecdotally, effects of these offsets appear the most significant the closer sled gets to the motor sprocket.

I believe that that angle is what causes the skipped teeth.

I believe the fix is to align the motor sprocket and the anchor points in a parallel plane.

The motor is the hardest to move, so deal with the issue at the other two points.

The sled bracket has various holes to mount the chain, that's easy.

For the corner anchor, see the blue bit of wood in the pic below. Lap in a piece of 1x4, and remount the cup hooks on the -front- of that piece of wood. Or the top, if that's 'more parallel' with the motor sprocket.

UPDATE!!! I was slightly wrong above but I'm not going to change it. The fix doesn't change. Follow this thought.

The tooth skipping problem happens when the sled is at its closes to the motor sprocket. That makes the error angle larger, but in the vid I saw it was the -outside- chain segment that slipped, that goes to the corner anchor, -not- the sled side. That means is wasn't -just- the error angle that caused the skip.

When the sled is closest to the motor, the bungee system is at its most relaxed, with least pull on the chain segment that goes to the sprocket. I think it was that less pull that, with a slight alignment inaccuracy, allowed the chain to catch on the corner of one tooth and ride up over the sprocket.

That doesn't mean that the correct fix is to add more weight to the corner anchor side of things. :) It's not even that easy to do because one can't simply attach weight where the bungee attaches to the chain. Regardless, part of the fix above is to move the corner anchors closer to parallel with the motor sprocket. [Mcnc-chain-path-02](/images/oy/oyp8_mcncchainpath02.png.jpg)

---

Posted on **2017-04-05 20:41:05** by **Bar**:

I completely agree with this assessment of what's happening and how we can fix it.

---

Posted on **2017-04-05 23:06:53** by **scottsm**:

I think you've put our finger right on it!

 In the video showing the chain slip, the motor was feeding chain out, and the skip happened on the 'bungee' side of the sprocket. Bar added a roller to that side to address this. In my case, the skip happened when the chain was reeling in, the skip on the sled side of the sprocket. The first time it happened I added a roller to the bungee side, but I had another skip with that in place so I removed it. I had a third skip in the same work location when I tried moving the sled attachment points to the lowest hole. I've learned that my workarea plywood is quite bowed there, putting the sled a further 1.5" behind the motor - I guess moving the sled attachment points actually made the chain angle worse. This agrees with the idea that alignment is one of the causes, and suggests that there are several factors to consider.

 - Is the choice of sled attachment point purely a matter of chain angle, or is there some other balance geometry besides? When I played around with the lower mounting holes in the lower middle of the workarea the s led seemed 'light in the nose' - I found a gap under the upper edge.

 - How flat is the workarea, how flat is the sheet stock being cut?

 - How thick is the sheet stock, how does this change the chain angle?

 - What is a reasonable range for chain angle and how does the angle vary across the workarea if it is non-zero at the home position?

---

Posted on **2017-04-05 23:34:12** by **davidlang**:

the chain/sled attachment is chain angle and sled balance both.



you had this problem trying to cut the arms, correct? This means you are using the temporary setup. Once you move the motors out and up (~12" up and 18" out) the chain angle should be much less of an issue. also mounting the motors to the mounts instead of right to the temporary frame should move them out, allowing you to move the chains out (improving the balance) while keeping the angle the same.

---

Posted on **2017-04-06 07:44:08** by **Bar**:

@davidlang is right that moving the motors up and was done primarily to help with the chain jumping issue. We can fine tune the system once we're all using the final frame by adjusting the size of the motor mounts. We could even add multiple mounting holes for the U-bolts to allow the motor mounts to move in and out and be adjustable

---

Posted on **2017-04-06 10:28:27** by **mattnelson**:

Speaking of the final frame... what's the eta on the assembly instructions for building the final frame?

---

Posted on **2017-04-06 11:09:07** by **Bar**:

I need to get the calibration figured out because on my temporary frame right now I'm getting very oval circles which won't work for doing the write up, and I think writing instructions that I myself can't follow isn't productive.



 I think the solution is to switch from the user measuring the distance between the motors to the machine self calibrating as described in [this](https://github.com/MaslowCNC/GroundControl/issues/127) issue.  Once I've got the calibration working consistently I'll write the next step.



What's your advice on the best way to go forward? Is your temporary frame working well enough that you feel comfortable moving on to cutting the parts for the final frame? Would you rather see directions created which describe cutting out all the parts even if it means faking the process using my fully built machine to get parts which are the correct size?

---

Posted on **2017-04-06 12:43:29** by **mindeye**:

I realize I'm not the intended recipient here but using my final frame (just miter sawed legs to right angles) + temporary arms (45 degree 2x4 with flat top) I ran into such bad chain slippage yesterday while cutting a final arm front 2/3rds of the way up the board and maybe 8" from the edge of the board that I took the arm front that successfully cut out below it and traced it so that I could cut a chunk around the bad arm you using my circular saw, then used my jigsaw to trace the good arm onto the front arm. Even though my calibration is 95% good, the z-offset between the motors and the sled caused some really scary slips.



If you stick mostly to the middle, lower 50% of the machine I think you can use the temp frame to cut the final parts but if you've got the tools I'd just cut one arm part out using your temp maslow then fab the rest by tracing it with other tools. Quicker and more repeatably accurate.

---

Posted on **2017-04-06 13:34:39** by **scottsm**:

I'm still on a frame built to the instructions, with a round sled built using other tools. My plywood has potato-chipped by about 1.5". I might be able to cut the arms, with careful placement, but comfortable - no. I'll wait for your writeup :) .

---

