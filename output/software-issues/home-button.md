## Home button
Posted on **2017-05-06 18:34:05** by **boandersen**:

Just finished cutting my first front arm. I do not know what I did wrong - this is my first day of the most recent firmware/GC build. I am cuttin 23/32 plywood (as usual) and had my depth at .8 with .12 increments.. For some reason It had cut through already after one less iteration that the software thought. 

I hit stop and the Home button. 

Previously, this would retract the bit, but this time it did not. I had to lift the router/sled until it was home, then use z-out a couple of time to retract..

---

Posted on **2017-05-06 18:39:23** by **Bar**:

Hmmm. Do you still have Ground Control open? Can you tell me what the text in the bottom right console says?

---

Posted on **2017-05-06 20:02:07** by **blsteinhauer88**:

I had the same thing a few minutes ago. I did not like the way a bit was working and the placement on the wood. I hit the stop button. The hit home. It dragged the bit without retracting it. I am using the latest firm and GC.

---

Posted on **2017-05-06 20:20:11** by **Bar**:

I will look into it and see what I can track down.



Does it do it consistently or only sometimes?

---

Posted on **2017-05-06 20:50:35** by **blsteinhauer88**:

After one press and it goes home. Then retracts. Then it works the second press by retracting then moving. It the initial after the stop button.

---

Posted on **2017-05-06 20:51:18** by **Bar**:

Perfect. Knowing that I'm sure I can track it down.

---

Posted on **2017-05-06 20:52:25** by **blsteinhauer88**:

You might check the return to Center also, it happens just on an initial press after a stop command. I seem to remember it did that to me using that returned to Center command also.

---

Posted on **2017-05-06 21:23:07** by **mcginniwa**:

I just made an attempt at cutting the sled and I noticed Z-axis adjustment during travel between cuts. It's possible that's it's my Z-axis pitch since I'm not using the Ridgid ... but I thought I would mention it.



 [IMG_5604](//muut.com/u/maslowcnc/s3/:maslowcnc:UAg0:img_5604.jpg.jpg) 



I watched the Z-axis measurement in GC during the cutting and I definitely saw it move on the X and Y before reaching the safety height in Z. So doesn't seem like it's simply bad calibration on my part. However, it could easily be that I generated a bad gcode file though since I don't really know what I'm doing. ;)

---

Posted on **2017-05-06 22:12:32** by **blsteinhauer88**:

looks like drifting.  There is play in the ridgid and we have to keep down pressure on the motor to keep the slop out.  I used bungie from the handles to the top of the motor, rancher used an old bike tube.  Set up the down pressure then set the Z to zero.  It will not travel like that since it is kept pressed against the gear that raises and lowers it.

---

Posted on **2017-05-06 22:14:36** by **blsteinhauer88**:

[IMG_0668](//muut.com/u/maslowcnc/s3/:maslowcnc:q1I7:img_0668.jpg.jpg) [IMG_0670](//muut.com/u/maslowcnc/s3/:maslowcnc:dWP5:img_0670.jpg.jpg)

---

Posted on **2017-05-06 22:53:56** by **mcginniwa**:

Thanks @blsteinhauer88. Will try that next and report back in [this thread on Z-axis and my router](http://www.maslowcnc.com/forums/#!/hardware-issues:bosch-gof-1600-ce-z-axisde).

---

