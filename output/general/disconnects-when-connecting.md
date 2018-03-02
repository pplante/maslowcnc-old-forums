## Disconnects when connecting to COM 3
Posted on **2017-07-17 12:38:47** by **taylor47**:

I am trying to do my initial calibration and my connection to COM 3 keeps timing out every few seconds. On a windows 10 machine

 [Timed out](//muut.com/u/maslowcnc/s1/:maslowcnc:QXRD:timedout.png.jpg)

---

Posted on **2017-07-17 12:53:28** by **Bar**:

Its running so you are making progress! Great work!



Were you able to install the firmware successfully?

---

Posted on **2017-07-17 13:02:57** by **taylor47**:

Which set of firmware? I am trying to setup the machine dimensions and I am unable to get the motors to turn

---

Posted on **2017-07-17 13:14:55** by **Bar**:

If we're seeing the disconnect issue, and neither motor is moving at all I think it's possible that the firmware didn't properly end up on the Arduino. When the firmware upload was complete did it look like this:  [Done Uploading](//muut.com/u/maslowcnc/s1/:maslowcnc:2sRs:doneuploading.jpg.jpg)

---

Posted on **2017-07-17 13:23:18** by **taylor47**:

Here is what I am seeing after the firmware update

 [Arduino](//muut.com/u/maslowcnc/s3/:maslowcnc:QaAE:arduino.png.jpg)

---

Posted on **2017-07-17 14:34:25** by **Bar**:

Thanks for the picture! That seems like it's our issue for sure. One quirk of the Arduino program is that when you do file -> open it opens the file in a new instance of the program. I think you are uploading the firmware perfectly, but the right file doesn't seem to be open. You want the cnc_ctrl_v1.ino file open in the Arduno program. Double clicking the cnc_ctrl_v1.ino file to open the Arduino program should ensure that the file is open

---

