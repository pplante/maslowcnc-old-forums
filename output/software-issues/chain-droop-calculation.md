## chain droop calculation
Posted on **2017-05-21 20:42:32** by **davidlang**:

we aren't to the point of really needing to worry about this yet, but according to the cable droop calculator at https://www.spaceagecontrol.com/calccabl.htm we can have enough sag at full extension (right chain when cutting on the lower left) to through off the calculated position by a noticeable amount.



once we get the PID loops tuned we will need to look at adding a droop compensation to the desired chain length.

---

Posted on **2017-05-21 20:46:59** by **scottsm**:

Is it possible that sag is part of the inaccuracy we see at the top of the work area?

---

Posted on **2017-05-22 06:21:26** by **davidlang**:

no, sag would be the worst at the longest chain and lowest tension, and in any case, we are talking about something on the order or 1/32 inch. enough to throw us off from our target of 1/64" accuracy, but probably not enough to cause our current 1/16" accuracy.



The new PID loops need to be tuned to be stable everywhere, and after that stabilizes, we'll see what the accuracy looks like.

---

Posted on **2017-05-22 08:01:22** by **scottsm**:

What are the odds that the PID values for 'uphill' travel will be the same as for 'downhill '? Or for different regions of the work area? Do we need scalars for some of these? I've noticed that there is a judder during downhill travel proportional to the distance above the center.

---

Posted on **2017-05-22 12:54:02** by **blsteinhauer88**:

I was thinking about ... What if... the chain was longer so as the left chain left the sled it went to the left motor, and instead of the bungie, it traveled around on sprockets to the lower right part of the sled.  and the right one vise versa.  This theoretically could keep the chains taught, and possibly keep the sled agains the workspace?&quest;? Thoughts?  Would it change, youe are still using two motors, the force is keeping it tight as it travels...?&quest;?

---

Posted on **2017-05-22 23:17:50** by **davidlang**:

@scottsm, the PID settings that give absolute maximum performance will differ under different conditions, but a PID loop is designed to adapt to real-world conditions, so you don't try to tweak it for the absolute best performance, you tweak it to make it stable under all conditions and accept the performance that results.



The video that Bar linked to in the weekly update talked about tuning the pid loop by increasing values by 10x until it became unstable and then backing down and increasing by 2x as the 'fine turning' of the loop

---

Posted on **2017-05-23 06:58:20** by **scottsm**:

Thanks for pointing out that video, it is well done - a reasonable set of steps for tuning.

---

