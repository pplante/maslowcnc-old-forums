## upgraded the firmware, installed rye newest ground control, shows me connected,
Posted on **2017-05-20 13:34:34** by **ledsled71**:

Installed the newest firmware, installed rye newest ground control, shows me connected, but motors won't budge given any command.  Any troubleshooting tips?

---

Posted on **2017-05-20 15:49:11** by **scottsm**:

12V power supply plugged into the Maslow board, not the Mega, yes? 



There's a troubleshooting tool 'test_electronics_firmware' included in the Firmware .zip that will run the motors to test the hardware. Read the description at he top of the file. I found that useful to confirm that I had the electronics correctly connected.

---

Posted on **2017-05-20 18:29:36** by **ledsled71**:

Had it running yesterday with the old versions, haven't changed any connections.



Verified the 12v is still lit up at the transformer, still plugged into maslow board.



Ran the test and it says connection good, but motors did nothing

---

Posted on **2017-05-20 18:36:57** by **scottsm**:

That is puzzling. GroundControl v0.72 requires Firmware v70 as the serial speed changed with these versions. Do the previous versions work (GC0.71 and Firmwarev69)?

---

Posted on **2017-05-21 08:35:31** by **ledsled71**:

I'm so confused.



Noticed that a restart of my pc triggers a response from both motors, so I'm definitely connected and have power



Ground Control main screen says I'm connected to com port 3, but when I go into the actions screen and click ports, it says none available.

---

Posted on **2017-05-21 10:22:06** by **scottsm**:

I think that since you're connected to COM3 it isn't listed as 'available' by Windows. Confusing indeed. 

If you disconnect the USB cable wait a moment or two, then connect again, you should see several lines about the connection disappearing and coming back and a line giving the firmware version number. Is that there, is the version number what you expect?

---

Posted on **2017-05-21 11:54:13** by **ledsled71**:

Unplugged, says disconnected, plugged back in, says reconnected, grblv1

---

Posted on **2017-05-21 14:05:21** by **scottsm**:

What happens if you do the 'Calibrate Machine Dimensions' sequence?

---

Posted on **2017-05-21 19:24:10** by **ledsled71**:

Tried virtually everything, test motors, calibrate chain lengths, manual jog one all axes, nothing happens

---

Posted on **2017-05-21 20:26:42** by **scottsm**:

I set up with a Windows machine and an uninitialized Maslow and I'm able to duplicate what you are seeing. Before you go further, I'd suggest that you disconnect the chains and disable the z-axis if you have that or at least note the 'STOP' button on the screen, a useful tool when things start acting strangely.

I found that after I had opened a file 'Actions/Open' and clicked the 'load' button at the bottom, my motors came to life. They might have been running a stack of commands that I tried before opening the file; I used the 'STOP' button to get control back.

This issue is new to the GC0.72/Firmwarev70 release, I loaded up 71/69 and the motors responded without the need to open a file. I've opened issue [#288](https://github.com/MaslowCNC/GroundControl/issues/288) on github for this.

I think this will get you running. Sorry it's been such a struggle so far :(

---

Posted on **2017-05-22 05:27:47** by **ledsled71**:

The stop button triggered a response from the motors.  Still couldn't jog the machine, but didn't have time to try to load a file.



Will try later today.



Thanks so much!

---

Posted on **2017-05-22 06:49:22** by **scottsm**:

That sounds promising, hope to hear of your success!

---

Posted on **2017-05-22 15:33:22** by **ledsled71**:

Works like a charm with the file loaded.  Thanks so much!!

---

Posted on **2017-05-22 15:54:00** by **scottsm**:

Great news! Make many wood chips :)!

---

