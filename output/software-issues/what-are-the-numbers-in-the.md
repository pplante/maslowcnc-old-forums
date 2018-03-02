## What are the numbers in the Konsole?
Posted on **2017-05-18 10:42:05** by **gero**:

The Konsole I start main.py from fills up the buffer with 4 to 5 '255' per second. Sometimes a bunch of '245' and sometimes in between a single 'Unable to plot position on screen'

Firmware and GC from yesterday.

---

Posted on **2017-05-18 10:51:15** by **Bar**:

Those are the number of characters currently available in the Aruduino character buffer. You can pretty much just ignore them, I just put them in to keep an eye on what was going on

---

