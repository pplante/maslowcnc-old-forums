## Right motor issue
Posted on **2017-07-07 09:11:48** by **blsteinhauer88**:

I've been on vacation so I've been using firmware version 73, I remember having trouble with 76, and I missed the one in between . So I uploaded 79 both firmware and ground control. The right motor will not turn counter clockwise. It only turns clockwise  for the movement it was given. Has anyone else seen this problem. If I tell it to test the motors in ground control it turns just fine.  So I re-loaded firmware version 73 and left ground control version 79, and the motor turns just fine both direction?

---

Posted on **2017-07-07 09:58:48** by **Bar**:

That is very strange :-/. Are you seeing that behavior during the calibration process, or also when the machine is running a program?

---

Posted on **2017-07-07 10:15:16** by **gero**:

Can confirm that it either does not turn CCW, or first CW then CCW. Clicking CCW several times in a row makes it wiggle left and right until you get CCW

---

Posted on **2017-07-07 10:53:40** by **Bar**:

@gero Are you seeing that behavior just during the calibration process or when a file is being run also?

---

Posted on **2017-07-07 14:00:40** by **gero**:

@Bar, I only checked calibration. Will do a test run tomorrow.

---

Posted on **2017-07-07 14:12:20** by **Bar**:

Ok, when I tried to recreate the issue I saw some weird behavior during calibration which I'm looking into, but everything ran normally when cutting. If you get not optimal behavior during the calibration, but are able to finish the process, the calibration will be good. The encoders are always keeping track of the motor positions so even if something acts up, it still knows where it is

---

Posted on **2017-07-07 16:07:33** by **blsteinhauer88**:

All the time. Pressing arrows to move also.

---

Posted on **2017-07-07 16:19:29** by **blsteinhauer88**:

Bar, I had a running machine, zero'd and calibrated.  I updated the firmware and ground control.  I then tried to drive the sled by using the arrow keys.  the motors turned in all directions, except the right motor CCW.  This of course caused my red and white cross-hairs to separate and.  I tried the motor test, and the motors all turned as they are supposed to.  I then went to the calibration program, I tried to turn the motors using all the buttons, ccw, cw, both right left, but, right motor would not turn to adjust CCW.  I rolled back the firmware only to .73, wala!  All worked fire again.  I did a manual chain adjustment and back in business.  I confirmed it was not the hardware, it was in the Firmware, that was the only change.  Interesting the Motor test runs both motors both directions, but the right motor won't work on its own.

---

Posted on **2017-07-07 20:00:57** by **blsteinhauer88**:

I confirmed the right motor problem.  I built the new arms and motor mounts  [IMG_0255](/images/qy/qyii_img_0255.jpg.jpg) 

Then I loaded the FW 79 and GC 79. I ran through the Calibration of machine dimensions. Right motor would not turn ccw in the initial zero of the gear. I got through the rest of the settings and then to Chain calibration. The right motor does not move as shown here. https://m.youtube.com/watch?v=ByZ8BJGZfAA



Switched back to FW 73 and it works again!

---

Posted on **2017-07-07 20:05:05** by **blsteinhauer88**:

I missed FW 78 on vacation. Loaded it to test just now and it works!!

---

Posted on **2017-07-07 20:38:07** by **Bar**:

Weird! So .79 doesn't work unless you install .78 and then upgrade to .79? That is so strange

---

Posted on **2017-07-07 20:45:40** by **blsteinhauer88**:

No, 79 is still not working for me, but 78 is running

---

Posted on **2017-07-07 20:47:52** by **blsteinhauer88**:

I should try that though

---

Posted on **2017-07-07 21:11:18** by **blsteinhauer88**:

Tried 79 again , no go !!

---

Posted on **2017-07-07 23:08:44** by **Bar**:

Ok, perfect. So the issue is absolutely something that .79 introduced. The good news is that the only real benefit of .79 over .78 is that .79 can detect the Arduino Shield version which you don't need. 



It's possible that maybe the firmware isn't detecting the PCB version right.



When your machine connects do you see the words "Beta PCB v1.0 detected" right after "Connected on ..."? You might have to scroll up in the Ground Control terminal to see it.

---

Posted on **2017-07-08 08:36:03** by **blsteinhauer88**:

I think I remember seeing that yes.

---

Posted on **2017-07-08 10:54:18** by **Bar**:

Hmmmmm let's be sure of that before we move on because if it says "PCB v1.1 detected" instead of 1.0 then I know exactly what's going  on :-)

---

Posted on **2017-07-08 11:13:51** by **gero**:

In my case it says 1.0. (Sadly no cuts or moves since the sled is still off :-() Just fired GC up to check.

---

Posted on **2017-07-08 11:47:05** by **blsteinhauer88**:

I just reloaded and confirmed that it detected the beta board.  [Screenshot 2017-07-08 11](/images/us/usag_screenshot2017070811.45.54.png.jpg) [Screenshot 2017-07-08 11](/images/pg/pg4o_screenshot2017070811.46.10.png.jpg)

---

Posted on **2017-07-08 12:41:24** by **Bar**:

Darn that's exactly correct, I thought I had it figured out but now I'm stumped again

---

Posted on **2017-07-12 14:42:33** by **Bar**:

I just wanted to bump this back up to the top and check in that this is still an issue we're seeing. I'd really like to fix it before the update today, but I can't seem to get it to happen. Does anyone have any new information that might help?

---

Posted on **2017-07-15 06:31:05** by **scottbramall**:

Not sure if this is related to my issue of not been able to calibrate the right motor?

---

Posted on **2017-07-15 17:44:25** by **blsteinhauer88**:

If you are using FW 79 or 80 and you right motor won't turn CCW, then yes report your issue here so Bar knows it's not just mine. Thanks!

---

