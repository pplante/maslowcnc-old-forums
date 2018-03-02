## 'GroundControlApp' object has no attribute 'xval'
Posted on **2017-06-22 12:02:15** by **gero**:

Do I need to be concerned about this messege in the terminal, or can I start with FW/GC 0.77 calibration?

 --> unable to read error value,'GroundControlApp' object has no attribute 'xval'<-- (feels like calibration 375... I am shure I calibrateted more then I am tears old :-))

---

Posted on **2017-06-22 12:36:34** by **Bar**:

Yes, I wouldn't worry about it, but I'm going to look into it right now

---

Posted on **2017-06-22 12:50:43** by **Bar**:

I tracked down what was causing the issue, and you can ignore it and I'll make it not show up again. It has to do with the first time the machine sends it's position if it reports an error position before an actual position, Ground Control doesn't understand

---

Posted on **2017-06-22 13:00:39** by **Bar**:

I've replaced the somewhat cryptic message with one that I think is more clear and less scary sounding.



Great job keeping an eye on the terminal window for errors. It's really helpful for me to know what's popping up there

---

Posted on **2017-06-22 13:20:09** by **gero**:

So just that I understand, only a red circle shows because I have not moved anything? Sled is not attached, so I can tell if that will change.  [Red-circle](../../images/Wg/BU/WgBU_redcircle.jpg.jpg)

---

Posted on **2017-06-22 13:44:29** by **Bar**:

The red circle indicates where ground control estimates that the sled actually is, while the white circle shows where it should be.



If you just see the red one, it's probably because they are stacked on top of each other meaning the machine is exactly where it should be

---

