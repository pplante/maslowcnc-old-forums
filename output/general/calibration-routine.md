## Calibration routine?
Posted on *2017-06-09 07:59:23* by *rancher*

Okay guys, I hung back after my +15mm post because I was cutting accurately enough for me.  I'm ready to catch up, and did the basic auto calibrate a week ago, but got hung up on the "self-adjusting" test pattern.  It didn't get square after four tries, and the way it moves down and over had it off my sheet.  I gave up on that, but I want to get back to cutting.   I am not sure after the Wed. update that we are back online?  Are we?  How do I get there fastest?  Is there a simple test pattern that will self calibrate that we are using now, or do I need to go through the chain measure steps again.  Also, the test pattern had no Z zero step, and I could not reset to work piece center, both of which made it impossible for me to finish. 

So, where are we at, and what is my best path to get back to making stuff?

---

Posted on *2017-06-09 08:11:07* by *mrfugu*

A good starting point would be to download the latest GC (0.75) and Firmware (0.73). I don't have a Maslow myself yet, but I'd expect that for the foreseeable future this will be a weekly ritual.

---

Posted on *2017-06-09 08:13:20* by *rancher*

Yep, that's the normal routine.  But.....have you made a good cut with it?  That's my question.  Also, calibration without going through initial set up for the umpteenth time.  Where are we at?  Do we have a new test shape?  Where is it?  What is the protocol, or is it back through the new auto-calibrate with no z-zero and no return to center?  Because that doesn't work for me.

---

Posted on *2017-06-09 08:22:27* by *scottsm*

The auto-calibration really does want to cut a 600mm x 600mm pattern and steps 10 or 20 mm southeast with each iteration. It really did a good job of calibration for me. It is adjusting the distance between sled mounting points using the difference between the horizontal and vertical measurements.
For the chain calibration, I had marked the two 'home links' with a white paint pen during an automatic calibration session, now I put those onto the top of the sprockets, use the controls in Step 1 to rotate them to the very top of the sprocket, then skip out and finish the automatic session and use the Advanced/Calibrate-manual to re-establish the workarea center point.

---

Posted on *2017-06-09 08:39:13* by *rancher*

Super helpful Scott, thank you.  I did not have a thick enough sheet on for calibration the last time, so I was starting to drag bricks on the stock shelf at the bottom of my frame.  I can fix that, and re do.  I should still be TDC on the chains and settings, I was just 10mm off vertically on the auto-cal, and never resolved it.  So, skip out>advanced/calibrate>return to center/zero-z.....then back to set up and skip to auto-cal > run until square?

---

Posted on *2017-06-09 09:23:47* by *scottsm*

That should work. The chain calibration just puts you in the center of the sheet, the auto-cal routine micro-tunes the sled attachment value so that x- and y-scale are equal. It repeats the cuts until the two measurements you enter are within a half mm or so. You can choose to use inches instead, but this is where your very best attempt at accurate measurements will pay off. I’m usually of the “close enough is good enough” school, but I took pains with this and it payed off.

---

Posted on *2017-06-09 09:26:29* by *gero*

I did a calibration with last weeks FW and GC and hardly got through because turning one sprocket spoiled the position of the other. With this weeks stuff I have totally strange moves. Need to calibrate again to see if that resolves it.

---

Posted on *2017-06-09 09:58:59* by *gero*

There is still an issue with the calibration. Expanding or retracting the left chain gives an interference with the right motor, most noticeable at the end of the retract or expand.

---

Posted on *2017-06-09 10:16:41* by *gero*

Whil calibrating right chain, motor was stuttering :-/. Will try to upload a video

---

Posted on *2017-06-09 10:39:00* by *gero*

https://youtu.be/-W4ZikYg5hk

---

Posted on *2017-06-09 10:51:06* by *rancher*

Whoah, looks like maybe I should wait a bit longer!

---

Posted on *2017-06-09 10:53:06* by *gero*

Looks like I can't get a functioning GC downloaded in the workshop. This could be the cause of my issues and connected only to me, so please ignore my comments.

---

Posted on *2017-06-09 12:34:01* by *Bar*

I've added a step to the calibration process to adjust the z-axis depth. Great point that it was missing.

I've also moved the starting point for the calibration up and to the left 36mm to give some more space to run the process. I don't want to make it user definable because I think the process has enough variables already, and having everyone doing their calibration in different places seems like asking for trouble.

I've seen that stop and start behavior with my motors too during the calibration process. It comes from the PID controller expecting the weight of the sled, but not finding it. Think like picking up a soda can that you expect to be full, when it's actually empty. I'll look into making that go away right now, but it shouldn't effect the measurements being taken. The encoder readings should still be correct.

---

Posted on *2017-06-09 15:17:52* by *rancher*

Thank you Bar.

---

Posted on *2017-06-09 17:25:08* by *mikeberg*

I agree with scottsm the auto calibration take a while to adjust but now maslow run like a charm! mine is now. 5 mm precise in x and y axis! I will never return to the 6 inch square and circle method for adjusting axis

---

