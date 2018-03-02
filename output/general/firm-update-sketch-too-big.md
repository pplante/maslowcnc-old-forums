## Firm update "Sketch too big" error
Posted on **2017-06-04 12:57:34** by **ledsled71**:

It always seems like I have trouble updating to the newest firmware.  Not sure where I'm going wrong.



Updated to .72, and when I upload it, at the very end it gives me a "Sketch too big" error.



Tried uploading .71 again, and get the same error.



Help needed for those not computer-savvy!

---

Posted on **2017-06-04 13:00:42** by **Bar**:

Take a look to see if the board selected in the Arduino program is the Mega 2560. If it thinks we're using one of the smaller boards it might have issues thinking the firmware is too big.

---

Posted on **2017-06-04 18:03:12** by **ledsled71**:

That was it - it was on the "Uno".  I thought it was on the correct one, but I was looking at the "Ports" dialog which showed the correct board.



Thanks so much!

---

