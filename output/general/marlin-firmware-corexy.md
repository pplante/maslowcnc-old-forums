## Marlin firmware: CoreXY
Posted on **2016-11-21 06:23:17** by **tilkor**:

I was wondering why you did not use some existing open source software like Marlin and the CoreXY configuration, I know this is not a true CoreXY but very close. I think this would be relatively easy to adapt the software for your project. Marlin already has the ability for a stand alone system and LCD display.

---

Posted on **2016-11-21 16:53:21** by **TheRiflesSpiral**:

As a point of clarification, this is not the first project for the Maslow team; they successfully launched the Makesmith CNC on Kickstarter prior to Maslow. As far as I can tell, the CoreXY config does not support the type of kinematics required of a triangulating system like Maslow.

---

Posted on **2016-11-21 17:42:03** by **tilkor**:

Well yeah it would have to converted to polar coordinates, here is a guy that already added a pen plotter or polargraphic to marlin. https://github.com/RickMcConney/PenPlotter

---

Posted on **2016-11-21 17:50:45** by **tilkor**:

Sorry in my originally post I could not remember the mechanical configuration name, CoreXY/delta 2d/scara was the closest thing I could think of.

---

Posted on **2016-11-21 18:02:54** by **TheRiflesSpiral**:

Nice! I haven't seen that.

---

