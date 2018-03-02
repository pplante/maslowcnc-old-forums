## how calibrate maslow on universal g-code sender?
Posted on *2017-05-29 06:40:09* by *mikeberg*



---

Posted on *2017-05-29 08:08:28* by *mattnelson*

My guess would be that you don't.  All of the maslow specific calibration stuff is going to have to happen in the Ground Control software.  Once calibrated I think you can use things like g-code sender.

---

Posted on *2017-05-29 08:52:03* by *davidlang*

look in the file CNC_Functions.h at the B commands, they are what are used for the calibration steps

---

Posted on *2017-05-29 09:22:57* by *scottsm*

An interesting question. The B commands could be used to manually accomplish the calibration that GC does programmatically, but the process would need careful instructions.

---

Posted on *2017-05-29 09:27:21* by *davidlang*

you can see the exact commands issued in the ground control source

---

Posted on *2017-05-29 09:45:44* by *scottsm*

There is some computation involved as well as setting up sprocket and chain positions. Parameters need to be changed based on previous measurements. It could be done, but it is far beyond simply running a series of B commands.
One could write a set of .nc files and a procedure to edit them and run them to achieve the calibration, a cookbook recipe to avoid Kivy and GroundControl.

---

Posted on *2017-05-29 10:54:50* by *gero*

It would be easier to set up a virtual machine or virtual box with the right python and kivy version and run GroundControl there for the calibration. That way you can keep your system clean.

---

