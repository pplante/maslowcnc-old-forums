## Does dust collection affect motor calibration?
Posted on **2017-03-29 01:36:34** by **scottsm**:

Has anyone decided whether running a dust collector actually affects the motor calibration (suction/friction)? I've watched the calibration process with and without the sucker running, and the numbers are different, but ballpark close. Wish those numbers were available to inspect somewhere in groundcontrol :)
 I haven't cut enough wood to form an opinion from experience, does anyone have an answer?

---

Posted on **2017-03-29 07:52:21** by **Bar**:

That's a great thing to investigate. I know mine behaves differently with the router running vs off too because there is a good amount of air forced through the router motor which creates something of an air cushion under the sled.

Rather than viewing the calibration numbers directly, I would like to add a metric to test how accurately the feedback control system is following the target, that way as the system improves we can track the progress

---

Posted on **2017-03-29 09:07:18** by **scottsm**:

Yes, I've watched the 'uncertainty circle', sometimes with dismay, and wished that that value were displayed along with x, y, and z. Too, if the uncertainty value rises above a threshold, (settable, of course :) ) the software would enter a 'Hold' state and prompt for user interaction. I remember one discussion where the circle might have grown beyond the screen boundaries :( - that would be pretty uncertain!

---

Posted on **2017-03-29 10:26:54** by **blsteinhauer88**:

Speaking of motor calibration, how often should this occur? And, I noticed sticking of the chain to motor gear, from dust.

---

Posted on **2017-03-29 10:34:40** by **Bar**:

In theory just once, but until I rewrite the feed back control system more often is probably good.

I think this is one of those things that we could better answer if we had a quantifiable metric for how well the system is holding position.

I find it helpful to calibrate whenever I am cutting in a different part of the sheet because the tensions will be different.

---

Posted on **2017-03-29 10:42:06** by **blsteinhauer88**:

Will that fix also when say I manual drive it up 2 inches, and it just takes of up the board without stopping? Or is that a "I lost my self" issue?

---

Posted on **2017-03-29 11:31:24** by **Bar**:

That sounds like an "I lost my self" issue. If you can find a way to make that happen consistently I would love to know. I know it's a real issue because many people have reported it. I have never seen it happen so I don't know where to start looking. I'm sure it's something simple, but I just don't know where to begin tracking it down.

---

Posted on **2017-07-13 21:34:45** by **cameronswartzell**:

If you use the method of finding your sled's center of gravity per Bar's video, you are making this measurement without the weight of the hose (which, if just hanging from the bottom is variable as the sled travels up and down). The added weight is relatively small, but may not be insignificant. My vacuums hose weighs nearly 1lb. I wonder if adjusting the center of gravity down a smidge would help in any way?

---

Posted on **2017-07-13 21:41:55** by **davidlang**:

one of the questions that the new simulation may be able to answer.

now that the kits are getting out to more people, we can hopefully get a little more testing and validate the simulator results.

---

Posted on **2017-07-13 22:19:28** by **scottsm**:

In practice I've found that keeping the hose clear of obstructions is more important than the effect of it's weight. I've been using a 2.25" hose with a reducer at the router.

---

