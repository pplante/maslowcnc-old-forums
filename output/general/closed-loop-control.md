## Closed loop control
Posted on **2017-02-13 20:53:01** by **lsimonetto**:

As someone new to this community... I don't know what the Maslow's control type is, but I imagine at this price it is probably open loop (i.e. steppers move a certain amount and where the tool ends up, it ends up). The advertised accuracy of +/-0.015" is not bad at the price... but being me, I'd want to try for more. Hearing that friction is a prime source of backlash... no problem. There's ways around that, and if the idea of ball casters under the router base work out, I will share the details.. buuuuut... in my old metalworking CNC world, closed loop control was king. 

Has anyone tried any form of closed loop control, via any kind of active measurement of tool location? If so, any success in making the system work?

---

Posted on **2017-02-13 21:20:41** by **davidlang**:

nope, this is cosed loop control with motors and shaft encoders instead of steppers.



the issue for accuracy here is the friction of the router sled against the workpiece and the bowing of the chains under their own weight (against the tension in them)



The other significant error source is the fact that the router and sled can twist under the motor torque (especially as the cutter hits varying densities). the closer the chains are mounted to the center, the less of a factor this will be.



These motors have 8148 encoder steps/rev and are driving 10 pin type 25 roller chain sprockets. This is an accuracy of 0.0003" per counter step (but the controls will probably not hold it accurate to a single counter step)



backlash is not a factor in this design, because the chains/motors/gears are always under tension in the same direction.



The error sources for this design are significantly different than in a 'normal' CNC

---

Posted on **2017-02-13 21:24:14** by **davidlang**:

I would not expect ball castors under the sled to work out well as they will have to rid against the material that's being cut. This means that they would fall into the cut areas and catch. If you mount a LOT of them, you may avoid this, but you are depending on having at least a tripod worth of them in contact with the uncut surface at all times (and not having enough spring in the others that they would catch as they transition from a cut area to an uncut area)



my personal opinion is that a slippery plastic surface is going to end up being the least friction solution

---

Posted on **2017-02-14 20:42:48** by **lsimonetto**:

!

Closed loop at this price! Gladdest I've been to be wrong in a long time... That is amazing. Reality 1, Assumptions 0. The assumptions cheering section abruptly switches sides. 



re ball castors: I agree, a number of them will not be in contact with the material as they pass over cuts. The basic counter to that issue is to use a bunch of them. there's no penalty for excessive points of contact, and they are dirt cheap. This is a case of no penalty for trying.. Failing that, a thin coat of car wax buffed on to a metal surface (machined aluminum, ground steel) makes it decidedly more slippery over wood. Would like to see if delrin or nylon would meaningfully benefit



re: the sled twist - to be clear, you mean the sled will twist slightly under the torque of the motor when the load on the router abruptly rises? interesting approach on bringing the chains close to centre.. the chain bend is also interesting; wondering if there are some chain size and material tradeo ffs that could be optimized here... 

Thank you for the info! Looking forward to getting my paws on this kit soon!!!

---

Posted on **2017-02-15 04:03:22** by **TheRiflesSpiral**:

The twist he's referring to is the rocking movement of the sled due to the cutting tool position being below the convergence point of the two chain vectors.



Ideally you could draw a straight line from the drive gears through the attachment points and if extended they would cross through the cutter.



The current sled hangs the router below this point.

---

Posted on **2017-02-15 08:58:09** by **davidlang**:

no, I wasn't referring to the rocking motion due to the cutter being below the point where the chains cross.



I am referring to the fact that as the motor spins and experiences different loads, the torque will be twisting the motor in the opposite direction of the cutter by an unpredictable amount.



even if the chains crossed at the cutter center, there would still be inaccuracies as a result of the fact that the pivot point is not around the center, so as the motor torque rotates the router, the chains are effectively shortened a tiny bit as the line from the motors to the cutter center is no longer  a straight line.



Another point of error that I had not thought of is the fact that the chains hang from the gears, and so the actual starting position of the chains is not the center of the gear, but rather the tangent of the edge of the gear, which is a different point depending on the angle of the chain.



now, is this going to matter for woodworking? not likely, but is it a source of error, yes.

---

Posted on **2017-02-15 10:22:01** by **Bar**:

The fact that the chain feeds off of the side of the gear and that the point the chain is tangent to the gear changes as the machine moves is actually compensated for by the internal math. I can't claim credit for that one, our resident mathematician Keith worked out that brilliant piece of work (yay open source!).



The rocking of the sled is almost entirely a result of friction between the surface of the sled and the material being cut (at least as far as I can tell). Right now I'm using a sled which is a big disk of unlubricated plywood which is pretty far from ideal. I think the next thing I want to try is to pocket out the interior of the sled so that only a ring around the edge is in contact with the surface. The space left between the center of the sled and the surface will be hooked up to the dust collection system to improve dust collection. There are also some waxes that have been recommended elsewhere I would like to try to condition the wood.



I think many ball casters or using a material like nylon is a great idea. I'm constraining myself to just wood because  I wouldn't feel good about using anything that isn't included in the kit or can't be easily made using the machine itself, but I'm excited to see the improvements everyone else makes!

---

Posted on **2017-02-15 11:54:48** by **davidlang**:

it's nice that the system takes into account the gear tangent issue.



as you decrease friction on the sled, it will 'kick' more as it transitions through different densities. deeper cuts and bigger bits will show this. create a g-code file that has it cross a hole it's already cut and look for the kick as it contacts the fresh wood on the other side of the cut.



As for limiting the material to things that can be made on the machine itself, the router will cut plastic well (as long as you don't get it too hot), as well as things like the melamine coated particle board (better with a laminate bit)

---

Posted on **2017-02-15 17:15:32** by **neveroddoreven**:

Agree that kickback will increase with reductions in sled friction (which is likely in most sled innovations).  Kickback might be limited by isolating it from the sled using a large ring bearing to isolate both the router and the bricks together from the sled and its chain connections.  The idea is that when a knot or an edge transition is encountered, the router will temporarily spin around a little, but not by much since the bricks won't let it go far, without causing chain deflections.  Thoughts?

---

Posted on **2017-02-15 18:17:19** by **davidlang**:

it's all speculation until we get the machines in our hands and can play with them.



remember that perfect is the enemy of good enough

---

Posted on **2017-02-16 05:57:45** by **lsimonetto**:

Love the discussion this started :)

I'm absolutely positive there are solutions to all of the issues covered here; Where I might struggle is making them simple enough to fit with the concept and beauty of the Maslow - simple and cheap solution to an old complicated problem... with a little luck i'd like to post drawings soon for one concept I hope can be improved by better ideas and critiques from here!

---

Posted on **2017-02-16 12:43:29** by **mooselake**:

The original question, is it open or closed loop, seems to have been missed.  It's closed loop, dc motors with encoders, right?

---

Posted on **2017-02-16 12:52:50** by **TheRiflesSpiral**:

Yes, motor control is closed loop. This gives a high degree of confidence that positioning is accurate. I should point out that the loop does not encompass the actual position of the cutting tool itself. That's a feature that hasn't made it into any consumer-grade CNC/Laser Cutting/3D Printing hardware yet that I'm aware of.

---

