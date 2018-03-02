## Calibrating distance
Posted on **2017-07-14 17:20:09** by **umindedstrikesagain**:

I have put a 1000CPR encoder on the sprocket shaft but don't know what to change for calibration. The firmware I updated to 1000 and in groundcontrol but during calibration 1degree is 2 rotations and 10mm is about 150mm.

---

Posted on **2017-07-14 21:11:23** by **davidlang**:

look at the top of CNC_Functions.h where encodersteps are defined.

---

Posted on **2017-07-15 09:53:48** by **umindedstrikesagain**:

Yup, changed that in firmware and in the groundcontrol settings. 



The firmware math says "7*291*4 --- 7ppr, 291:1 gear ratio, quadrature encoding" I tried 1000 and it was not correct so I will try 1000x4 as ENCODERSTEPS could be in ppr.

---

Posted on **2017-07-15 15:00:41** by **davidlang**:

if you have a 1000 pulse/rev encoder, that translates to 4000 steps/rev (each output has a pulse train of 1000 pulses, and we detect going up and coming down, that's 2x, and the two outputs are out of step with each other, so that results in another 2x)

---

Posted on **2017-07-16 13:44:55** by **umindedstrikesagain**:

I get the same results with 4000 as this 1000 when changed in both firmware and groundcontrol. During calibration "Rotate 1 degree" is one rotation and "extend 10mm" is over 150mm.

---

Posted on **2017-07-16 14:03:07** by **Bar**:

Have you messed with the encoder resolution settings in Ground Control?

---

Posted on **2017-07-16 16:03:11** by **mrfugu**:

this sounds like a job for a detailed Calibration Wiki page...

---

Posted on **2017-07-16 16:07:39** by **mrfugu**:

sorry, i see that this is currently an active issue, nm.

---

Posted on **2017-07-18 17:53:49** by **umindedstrikesagain**:

> @Bar

> Have you messed with the encoder resolution settings in Ground Control?



Why are there encoder resolution settings in both firmware and software? I tried 1000 and 4000 in each and nothing changed. There is a bit of slop on the encoder mounting, is the PID getting its feedback from the encoder?

---

Posted on **2017-07-18 21:16:22** by **Bar**:

Really the ones in the software are the ones I would recommend changing, the ones in the firmware are available to be changed mostly because since the whole machine is open source, really anything can be changed if you dig deep enough.



The PID does get it's feedback from the encoders, so there is some slop on your encoder mountings I would fix that. I haven't had much experience with the effect of slop there since our encoders are built into the motor, but I could imagine that causing problems.

---

