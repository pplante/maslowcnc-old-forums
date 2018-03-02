## Slow feedrate for metric back?
Posted on **2017-05-13 08:03:25** by **gero**:

Just trying a design and with F500 it is moving at ~ 1mm/sec

---

Posted on **2017-05-13 08:04:15** by **gero**:

In my timezone GC and firmware from yesterday

---

Posted on **2017-05-13 08:11:27** by **Bar**:

Thanks for the heads up! I will find out why that's happened.



Is this with the release version or the version from GitHub master branch?

---

Posted on **2017-05-13 08:12:23** by **gero**:

Master it is

---

Posted on **2017-05-13 08:14:33** by **gero**:

If that is what the green download button does 8)

---

Posted on **2017-05-13 08:20:01** by **gero**:

Don't get nervous to soon, testing F-Carve (V-Carve). It nice for seeing coordinated x,y,z moves. Could come from the program that made the gcode. Starts like:

G90

G21

G17 G64 P0.001 M3 S3000 

F500.0

G0 Z5.000

G0 X0.000 Y140.000

G1 Z-0.000

G1 X0.000 Y140.000 Z-0.000

G1 X3.000 Y140.254 Z-3.000

G1 Y276.951

---

Posted on **2017-05-13 08:28:25** by **blsteinhauer88**:

F is feed right? 500 mm per min?

---

Posted on **2017-05-13 08:31:50** by **gero**:

Yes, 500mm/min should make like 8.3 per second

---

Posted on **2017-05-13 08:33:59** by **gero**:

G0, when Z is safe, is faster. Only affects the G1 moves

---

Posted on **2017-05-13 08:39:17** by **gero**:

[Bf](../../images/dB/az/dBaz_bf.jpg.jpg)  :-)

---

Posted on **2017-05-13 08:42:24** by **blsteinhauer88**:

I notice Maslow slows a lot to corner, there is a lot of cornering there! Ha ha!

---

Posted on **2017-05-13 08:44:30** by **gero**:

Ya, and with a V-bit it tries to make very thin lines. Could be just the file with all these curves. A lot of math to do :p

---

Posted on **2017-05-13 08:44:57** by **blsteinhauer88**:

It will be nice!

---

Posted on **2017-05-13 08:46:45** by **gero**:

Although the outside is a square frame, it cut that lame as well. Its just filling gaps between test patterns to learn a bit more.

---

Posted on **2017-05-13 09:35:09** by **gero**:

@blsteinhauer88 If you are open mined enough to be able to see the beauty in imperfection and know enough about art to understand 'Abstract' ... yes... it is nice, hahaha  [IMAG0748](../../images/yV/RU/yVRU_imag0748.jpg.jpg)

---

Posted on **2017-05-13 09:41:14** by **blsteinhauer88**:

Right on!

---

Posted on **2017-05-13 09:43:13** by **gero**:

I must admit, I did not take care of the Z-backlash until today. The rubber band is going on right now.

---

Posted on **2017-05-13 10:12:05** by **gero**:

Bar! False alarm, I am sorry. It is the file. After this endless butterfly, my test square cuts fast.

---

Posted on **2017-05-13 10:17:14** by **Bar**:

I think I know what's going on. Maslow is expecting the F command to be a part of a move command like 

---

G01 X10 Y2.3 F500 

---



so it's not picking up the feedrate. It should be an easy fix.

---

Posted on **2017-05-13 10:21:18** by **gero**:

In the square i have it behind the moves, so as a separate F500 it gets ignored?

---

Posted on **2017-05-13 10:29:21** by **Bar**:

As long as there is a G0 or G1 command before the F500 it will get caught, but because there is a G17 before in the first file It tries to figure out what F500 means when applied to G17 and it can't decide. It's a pretty weird corner case, but it shouldn't be too hard to correct

---

Posted on **2017-05-13 10:30:18** by **gero**:

It's a pretty old python program. FYI http://www.scorchworks.com/Fengrave/fengrave.html

---

Posted on **2017-05-13 10:40:43** by **Bar**:

I'm thinking that we're going to want to integrate G-code generation from both .svg and .dxf files into Ground Control pretty soon so it's nice to keep an eye on which python program are out there that we could build off of

---

Posted on **2017-05-13 14:50:04** by **davidlang**:

feed rate can be given as part of a G1 command (g0 is defined as the fastest the machine can go, so feed rate doesn't apply there), but it's also legit to set it separately.

---

