## What torque is required?
Posted on *2017-04-02 05:40:54* by *raidonchrome*

Hi! I want to build a similar CNC, and I need to know what torque is required to be able to cut wood with a router? I am planning on using stepper motors, and I can't find any data on the DC motors used in Maslow..

---

Posted on *2017-06-03 08:36:24* by *nocturnal42*

https://github.com/MaslowCNC/Mechanics/blob/master/BOM.txt

---

Posted on *2017-06-03 09:41:15* by *davidlang*

The motors used on the maslow produce ~30Kg-cm force at full power. That's been enough to rip the wood of the sleds apart on some beta-tester's machines when things went wrong enough.

note that you will not be able to use the maslow firmware with your steppers, you will have to end up writing your own (but it is all open source)

---

