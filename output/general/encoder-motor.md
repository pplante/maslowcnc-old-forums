## Encoder Motor
Posted on *2017-04-27 19:10:19* by *stevenu*

Hello - What is the DC motor and gearbox used in the Maslow CNC?  I have been trying to determine the model without much luck.  I want to determine the specifications to build my own unit.  Thank you all

Steven

---

Posted on *2017-04-27 19:30:16* by *davidlang*

it's a custom motor. 12v DC (~1A IIRC) with a 200:1 gear on it producing 30Kg/cm torque with an encoder on the motor that results in 8148 steps/rev and able to rotate at ~20 rpm

this has more torque than is needed (enough to rip the sled apart), so something with less gearing that produces higher speeds would work.

This is also a much higher resolution than is needed (they mounted the encoder on the motor, so it benefits from the 200:1 gear ratio as well)

you could put something like this encoder (2400 steps/rev) on the output shaft of any gear motor of about the right speed and power http://www.ebay.com/itm/360-600P-R-Photoelectric-Incremental-Rotary-Encoder-5-24V-AB-Two-Phases-Shaft-/142133029511?var=&hash=item2117c9ea87:m:miAAqDospQN2_5XmhdmG4HQ

---

Posted on *2017-04-27 19:30:18* by *rollandelliott*

Its custom made

---

Posted on *2017-04-27 19:32:14* by *davidlang*

the critical parameter is to be able to wire the encoder up to the arduino so that it knows how much the motor/shaft has actually turned, and to be able to control the speed of the motor in both directions.

---

Posted on *2017-04-27 23:16:33* by *Bar*

We have ours custom made because I couldn't find anything off the shelf that was good enough. The specs listed above are great. One caution if you are building your own, some of the higher resolution AMS magnetic encoders are really non-linear in ways that aren't clear on the data sheet. That's where I started and it was a lot of hours.

---

Posted on *2017-04-29 13:35:32* by *stevenu*

I appreciate the information.  I am looking into the CUI encoders and off the shelf gear motor with a dual shaft system.  I will keep every up to date.

---

Posted on *2017-04-29 13:46:38* by *davidlang*

what sort of issues were you seeing with those sorts of encoders?

---

Posted on *2017-04-29 13:50:17* by *Bar*

Those CUI ones look good. I was using the AMS magnetic encoders and I was seeing all sorts of issues with the magnet position having big effects on the positioning accuracy, and variation from one magnet to the next. The CUI ones are capacitive and fully packaged as a unit so you shouldn't have those issues.

---

Posted on *2017-04-29 14:31:40* by *davidlang*

ahh, you are talking about the sensors that were used on the makesmith, thanks.

---

Posted on *2017-04-29 14:46:56* by *Bar*

Yeah, oh Makesmith they were fine because each rotation was only 1/20th of an inch, but on Maslow slight non-linearity made a big difference :)

---

