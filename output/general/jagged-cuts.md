## Jagged cuts
Posted on **2017-04-02 15:42:37** by **ledsled71**:

Cut my first part today (sled), and the quality of the cut was less than desirable.  I noticed on dry runs that the motors would start and stop (quickly), which causes the temporary sled to rock back and forth.  On portions of the cut, the motors run smoothly and the cut was much nicer.  



Any way to get the motors to run at a slower& steadier pace?

---

Posted on **2017-04-02 16:02:57** by **carlosrivers**:

Can you put up a picture of it?

---

Posted on **2017-04-02 17:12:49** by **ledsled71**:

[14911782805501627729086](/images/c7/c7ml_14911782805501627729086.jpg.jpg)

---

Posted on **2017-04-02 17:15:24** by **ledsled71**:

You can see that each of the four passes has the same pattern

---

Posted on **2017-04-02 17:25:04** by **nathanmiller**:

what software did you use in creating the arc/circle? I recently learned that some software converts bezier curves to a small number of straight lines (and you must manually tell it to use a whole bunch of small lines instead). Since each pass is doing the same pattern I cannot help but wonder if it has more to do with the design/software and/or how it's being translated into G-code.

---

Posted on **2017-04-02 17:34:12** by **Bar**:

Running the calibrate motors function near where you plan to cut will help, but smoother motion control will really hinge on rewriting the motion control sustem to use both a position PID loop and a motor speed PID loop. You should be able to get smoother cuts than that, but I still see a slight wave on most of my cuts. Hopefully it will disappear soon with a firmware update.

---

Posted on **2017-04-02 17:48:23** by **ledsled71**:

Nathan, I was running the gcode bar provided for the sled

---

Posted on **2017-04-02 17:49:12** by **ledsled71**:

I thought a slower speed might help, but that isn't controllable in ground control

---

Posted on **2017-04-02 17:51:50** by **nathanmiller**:

Ah I see. Somehow I missed the part where you said it was printing the sled (now that I look back at your original post it's blatantly obvious! Sorry about that). Yeah, that's G-Code should be solid.

---

