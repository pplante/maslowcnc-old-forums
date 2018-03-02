## Motor shield
Posted on *2017-06-06 21:28:18* by *eserv*

Is the motor shield available separately? I have another project that it would work just dandy for!

---

Posted on *2017-06-07 03:17:57* by *davidlang*

not at this time, it's a custom built item (all opensource, so the details are all available on github)

see https://github.com/MaslowCNC/Mechanics/issues/52 for another option that's out there.

---

Posted on *2017-06-07 07:33:36* by *Bar*

@davidlang is right but we're hoping to have them available as a replacement part soon, so if you need one you should be able to get one in a couple weeks

---

Posted on *2017-06-08 01:39:01* by *dennisbingham*

@Bar that would be amazing. I didn't know this project existed until the Tested video, and by the time I decided I definitely wanted in, I missed the Kickstarter. 
I've been able to figure out a something that isn't too far from spec for most parts to at least get started trying the design out, but your motor controller is the thing that I was really worried about trying to substitute. I'm really excited that you might have extras available soon.

---

Posted on *2017-06-08 02:01:00* by *davidlang*

the motor controller is fairly simple, it drives brushed DC motors and has two bits for direction and a PWM signal for speed. you can find many motor controllers that will do this (or build your own, the parts and pinouts are available on github)

---

Posted on *2017-06-08 02:13:52* by *dennisbingham*

@davidlang thanks for the explanation. I'm sure I could get there eventually, but the electronics portion of this isn't exactly my core competency. *Flashbacks of solder puddles*

---

Posted on *2017-06-08 02:16:13* by *davidlang*

look at the link above, that looks like a readily available controller that should work

---

Posted on *2017-06-08 18:22:13* by *eserv*

Do they make a encoder/dc motor drive that works with the arduino cnc stepper motor shield like the one  Makeblock has? By the way,  I use an outrunner model airplane motor as a spindle on my "other " homebuilt cnc machine. I only ever use 1/8" bits in it anyway so I don't require a 1 or 2 hp rig! an added bonus the airplane motor is much quieter!. I will try the same setup if I actually build one of these.

---

Posted on *2017-06-09 01:27:27* by *davidlang*

Which arduino cnc stepper motor shield ? :-)

but since steppers need very different interfaces than DC/encoder motors, there are not many boards that support both (the one mentioned in the second post in this topic is an arduino/shield combination and it can have both stepper and dc/encoder motors on it.

---

Posted on *2017-06-09 06:19:06* by *eserv*

You'll have to excuse my ignorance re arduino and it's programing! I am just started at it in the last month. all my experience with cnc over the last 8 years has been with mach3 and parellel ports. the specific shield I was asking about is this one : http://www.ebay.ca/itm/Red-V2-V3-V4-CNC-Shield-Engraver-3D-Printer-Expansion-Board-A4988-Driver-Arduino-/152473878756?var=&hash=item238026c0e4:m:m4N1ZCtKYhRvQ4IkgmjJH3w

---

Posted on *2017-06-09 14:27:00* by *davidlang*

Ok, that board does not support DC/encoder motors, only steppers.

---

