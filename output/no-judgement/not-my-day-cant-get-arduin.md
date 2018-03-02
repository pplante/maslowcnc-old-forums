## Not my day: Cant get arduino to connect
Posted on **2017-04-14 11:07:07** by **boandersen**:

I am suddenly getting this in windows 10. I did not have the arduino connected for about a week, and now I get this every time. Windows has installed updates.. I do not think the arduino has faulted, because it does its motor init when connected..

Anyone seen this?



Windows has stopped this device because it has reported problems. (Code 43)



A request for the USB device descriptor failed.

---

Posted on **2017-04-14 11:29:32** by **Bar**:

I'm sorry you are having such a rocky day. I have not seen that error before. I would try uninstalling and reinstalling the Arduino IDE program. It should come with all of the drivers you need.

---

Posted on **2017-04-14 11:30:08** by **Bar**:

This forum post [here](http://forum.arduino.cc/index.php?topic=207505.0) says that trying a different USB port could help

---

Posted on **2017-04-14 17:04:36** by **rexklein**:

Here is what I did. 

Win10 Hardware properties. 

unplug USB

then delete com ports that are left over

plug in usb

see the com port for the arduino

advanced com port settings set it to 1 or 3 

with a speed of I 19200

in ground control type in the com port you now know it is for sure.

---

Posted on **2017-04-14 17:09:30** by **rexklein**:

https://goo.gl/photos/nY9eYWRGdVnZVLZW6

---

Posted on **2017-04-15 05:50:02** by **boandersen**:

Thanks. I'll try your suggestions

---

Posted on **2017-04-16 09:53:39** by **boandersen**:

Turns out that my problem was the cable. I first tried with my laptop and the long cable - that worked fine - then I tried connecting the arduino to the "garage pc" with a shorter cable - it worked too, but garage pc with the long cable is a no go even though it used to work. I wonder if a powered hub would help.

---

Posted on **2017-04-16 10:51:05** by **TheRiflesSpiral**:

I'd say it's likely a function of electrical noise more than length. Try a ferrite core filter on each end. https://www.amazon.com/Gino-Suppressor-Ferrite-Filters-a12071000ux1058/dp/B009ENG6TI

---

Posted on **2017-04-16 10:51:49** by **rexklein**:

I use a powered hub with a very long extension. My long extension is a high quality shielded cable. as well

---

Posted on **2017-04-16 10:54:00** by **Bar**:

Good debugging! I'm glad to hear you tracked it down :)

---

