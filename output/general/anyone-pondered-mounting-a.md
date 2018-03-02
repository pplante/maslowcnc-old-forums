## Anyone pondered mounting a laser to it?
Posted on **2017-02-08 15:53:22** by **growbot**:



---

Posted on **2017-02-08 16:07:45** by **chauhuh**:

Yea, I plan on mounting one on so I can mark parts.

---

Posted on **2017-02-09 00:39:52** by **jamesbil**:

Sounds cool. Any more info.? Type, spec etc.

---

Posted on **2017-02-09 09:17:13** by **chauhuh**:

No, I haven't really given it much thought yet. I'll get my machine up and running properly first before modding.

---

Posted on **2017-04-09 07:21:19** by **ylexot**:

I've pondered it for wood burned designs (not for cutting), but don't quite know how to do it. Having it trace a continuous design wouldn't be difficult, but it you wanted to do something detailed, it would need to be able to turn the laser on and off.

---

Posted on **2017-04-09 09:02:03** by **jbarchuk**:

> @ylexot

> it would need to be able to turn the laser on and off.

It's very doable, though not part of the current design -yet-.

The control board has extra outputs and inputs to control and be controlled by other devices/sensors.

The g-code file would have to have extra information to tell the laser when to turn on/off. Maybe a power level control is possible.

If you can research other existing software that do these kids of things, and create an 'issue' in the git store, maybe someone will look into it.

---

Posted on **2017-04-09 19:10:17** by **davidlang**:

Laser cutters tend to want more speed than the maslow is able to provide, and you _really_ don't want the laser to be operating without a laser-safe box around it.



the maslow design is not a good fit for the needs of a laser cutter, but you could potentially build something along similar lines.



As for marking parts, just have a tool change operation and put a small v-bit in the router and have it carve part numbers in the material



or put a pen in the router and use it to mark the parts.

---

Posted on **2017-04-10 11:06:20** by **TheRiflesSpiral**:

Laser cutters and engravers are pulsed beam so speed is only a consideration for calculating the pulsewidth and timing of the pulses. Granted, the pulses will be less frequent than most laser engravers but it's doable. Light scatter on wood surfaces is minimal and while glasses would be advisable, there's no need for a light-tight enclosure if you're dealing with a low-power engraving laser (diode). Now if someone wants to strap a 30W CO2 laser to Maslow, we should have a different discussion. :)

---

Posted on **2017-04-10 14:07:29** by **rancher**:

If the laser doesn't have you nervous enough my neighbor and I are excited to hang his plasma torch from it and see what happens.

---

Posted on **2017-04-10 14:17:56** by **TheRiflesSpiral**:

I've used a CNC plasma at our maker space. That thing is terrifying. And there, I think speed might be an issue... I was getting globs all over the back of my parts and one of the students came over and cranked up the speed; viola! No more globs. It seemed like the thing was screaming fast but it did a wonderful job.

---

Posted on **2017-04-10 18:51:11** by **davidlang**:

re: wood not being reflective



That's true, until you have a piece that has a screw in it, or you cut over a screw/nail in the frame.



In theory goggles can be all you need, but making sure that you have everyone in goggles that don't have any openings at any corners and that nobody will wander in to the area is non-trivial for most people.



As for power, there are 'laser engravers' being sold on e-bay with 40w CO2 lasers, so when someone starts talking about laser engravers, I don't assume that they are talking a trivial power level

---

