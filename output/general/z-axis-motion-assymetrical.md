## Z axis motion assymetrical
Posted on *2017-05-01 17:15:22* by *garyw17*

I just got my Z axis connected, and notice that the motion is not symmetrical.  Commanding it to go "IN" results in a bit more motion than "OUT"  After only a couple of cycles this becomes very pronounced.  My machine is scratch built, using a Pololu motor with 10,986 pulse count for Z motion.  I have the Z axis pitch in GC set at 3.17 mm per revolution.  So commanding a Z motion of 3.17 mm seems like I should get exactly 1 rev of the shaft in both directions.  Anyone else see something similar or have any thoughts?  Thanks

---

Posted on *2017-05-01 17:43:21* by *Bar*

I saw some similar behavior during the build process when I was loosing pules in the wires. I was using 14,000 ppr encoders initially and loosing steps because the wire didn't have enough bandwidth for pulses that short. Try running the motors slower and see if the problem goes away.

---

Posted on *2017-05-01 17:51:49* by *garyw17*

Thanks Bar.  So, I am moving the Z axis with GC.  I do not see a setting for the speed.  I assume it is set somewhere in the firmware?

---

Posted on *2017-05-01 18:01:40* by *Bar*

Yep, you are looking for line 421 in the file CNC_functions.h 

---
singleAxisMove(&zAxis, zgoto,45);
---

45 is the speed in mm/minute

---

Posted on *2017-05-02 00:16:15* by *davidlang*

it's not just the wires, the arduino is a pretty slow processor, so if you send it too many interrupts it can't keep up with them

---

Posted on *2017-05-02 05:45:07* by *garyw17*

Thanks guys.  It was my own stupidity.  Somehow I connected the wire shield on the cable to the black wire coming from the Z axis motor.  Obviously that wire has a PWM signal on it, so it is pretty much the opposite of ground, and no surprise, it messed up the encoder pulse count.  Things are much better now :)

---

