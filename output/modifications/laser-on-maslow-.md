## Laser on Maslow :-)
Posted on **2017-05-29 06:35:19** by **celiossaurus**:

Hello ALL People working at Maslow, just a two cents question, have you thought about installing a litle solid state laser for engraving or cutting thin wood or fabric/plastic/acrilics ?

---

Posted on **2017-05-29 08:51:14** by **davidlang**:

people have though of a lot of things, I haven't heard of anyone doing it yet.

---

Posted on **2017-05-29 10:43:47** by **danychouinard**:

I imagine the Z-Axis code could be fiddle to fire the laser beam, but I would worry a lot about the time the head is spending at the same place.  You could perce a hole throught the panel, the back panel, the shop wall all the way into the neighbor bathroom...

---

Posted on **2017-05-29 12:59:42** by **davidlang**:

you over estimate the power of these lasers

---

Posted on **2017-05-29 23:42:46** by **docnasty**:

Actually guys, the easiest way to do this, would be to get a laser package from JTechPhotonics... Like a 3.8w Diode laser.  You control the intensity of the laser with the Spindle Speed.  M3 S2000 Would be 20% strength, M3 S10000 would be full.  M5 turns it off.  I use mine with Fusion 360 on a regular CNC all the time.  I can't imagine this would be any different.

---

Posted on **2017-05-30 11:24:56** by **TomTheWhittler**:

I am not sure but I do not think the Maslow controller hardware supports spindle speed (or even turning off/on a router) so the g-code M3 would have no effect.

Since there is a fourth motor control it maybe possible to use that to control a laser with some software glue for g-code M3..

---

Posted on **2017-05-30 12:08:32** by **davidlang**:

well, if we're adding software, we could implement M3 using one of the available pins far easier than trying to hijack the 4th motor controller.

---

Posted on **2017-05-30 12:31:34** by **TomTheWhittler**:

I forgot that Bar brought out all the available pins so that should be workable.

---

