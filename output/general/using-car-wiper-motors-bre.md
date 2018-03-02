## Using car wiper motors, breadboard and H-bridges while waiting for the kit.
Posted on **2017-05-23 09:51:09** by **dougl**:

I just ordered a kit(#01782) instead of a first time DIY attempt and look forward to building from the validated parts provided. 

But I also love to DIY so while I wait for the kit, I have some 12V automotive windshield wiper motors(worm geared) which turn at 30 RPM which I'll see about putting a magnetic shaft encoder on. I'll also be hacking together a test system using an Arduino and H-bridges I already use with the wiper motors.  

BTW, the Z-axis addon was what brought be back to Maslow and the kit purchase. And if the kit arrives in time, I will sign up for showcasing it at the San Diego Maker Faire in Oct including doing a talk/discussion on one of the stages.  Thanks Bar and Team Maslow!

---

Posted on **2017-05-23 10:03:12** by **davidlang**:

If you have to put the encoder on the output shaft, you will need a fairly high-res encoder ( something like http://www.ebay.com/itm/360-600P-R-Photoelectric-Incremental-Rotary-Encoder-5-24V-AB-Two-Phases-Shaft/142133029511?_trksid=p2481888.c100678.m3607&_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908131621%26meid%3Da377d4c94fee4918830b672e8873c218%26pid%3D100678%26rk%3D1%26rkt%3D4%26sd%3D441209388746&var=441209388746&_trkparms=pageci%253A0bbe6748-3fd9-11e7-a477-74dbd180bd54%257Cparentrq%253A363ee0fa15c0aa472cd566cffffaa35d%257Ciid%253A1 would probably work as it gives 2400 pulses/rev but one that is encoded for 1000 lines/rev instead of this 600 lines/rev would be better)

If you can put the encoder on the motor shaft rather than the output shaft, you can go with a much lower resolution encoder the stock motors are something like 10 lines/rev

---

Posted on **2017-05-23 10:31:34** by **dougl**:

I will try one of these at 1024 ticks/rev since it just requires a magnet epoxied on the end of the shaft. 
 http://www.ecomorder.com/techref/ecomprice.asp?p=416078

---

Posted on **2017-05-23 10:36:08** by **davidlang**:

the resolution of the machine is going to suffer a little from that, you won't be able to get the 1/64" that is the maslow target, but you may be able to get to 1/32" or 1/16"

Bar used something very similar to those magnet sensors for the makesmith CNC and he was grumbling about the accuracy problems he had with them. it turns out that in practice, they are far from linear in their steps

---

Posted on **2017-05-23 10:41:21** by **dougl**:

I will ask the guy doing the boards if he's seen or tested for non linearity. Wondering if the magnets are the key to that... I also have the possibility of opening a hole in the motor case and mounting the sensor on the drive motor and use the 360 tick/rev version of the board.

---

Posted on **2017-05-23 12:29:30** by **davidlang**:

if you can put the encoder on the motor instead of the output gear, you only need ~10 lines (40 edges) per rev with a 200:1 gear ratio

---

Posted on **2017-05-24 10:29:56** by **dougl**:

Any idea what the ID of sprocket is( or OD of the motor output shaft )?

---

Posted on **2017-05-24 10:31:29** by **davidlang**:

no, I've been wondering that myself. I intend to put larger sprockets on the motors, sacrificing force for speed

---

Posted on **2017-05-24 10:37:37** by **dougl**:

@davidlang, I saw another post where you talk about using a Teensy, are you working on a DIY version?  I've ordered the kit but thought I'd do just that, a DIY from parts sourced elsewhere.  If so, maybe we should maybe create a github fork and work out kinks together.

---

Posted on **2017-05-24 10:46:58** by **scottsm**:

I just measured the ID of the sprocket: 0.315"

---

Posted on **2017-05-24 11:03:36** by **davidlang**:

Ok, an 8mm shaft

---

Posted on **2017-05-24 11:18:34** by **dougl**:

I a motor close, sort of.  12V, 30 RPM, 200:1 ratio with encoder but only 10 kg/cm torque and 6mm output shaft... http://r.ebay.com/gAi81l  But I also heard the current motors can ripe the sled apart so maybe 20 kg/cm is overkill.

---

Posted on **2017-05-24 11:36:25** by **davidlang**:

it's worth trying, if you find it doesn't have enough power, you can go with a smaller sprocket, and move the motors higher above the work area (the max torque is needed at the top center of the work area

---

Posted on **2017-05-24 19:10:34** by **TomTheWhittler**:

I got a couple of those Ebay motors thinking I would roll my own before my MaslowCnc arrived. The main gear on mine was metal but the worm gear coming off the motor was nylon. Unless you are moving a Dremel sled it will not last moving a full size router.

---

Posted on **2017-05-24 19:25:38** by **TomTheWhittler**:

This was the only Ebay geared motor I could find that actually showed the inside of their gear box (all metal) but no encoder. Even then it looks cheapish. 
www.ebay.com/itm/381265109244?

---

Posted on **2017-05-24 19:28:37** by **TomTheWhittler**:

Even them you are looking at a motor that fits easily inside your hand.
http://www.ebay.com/itm/331910918012?
Which leads me to believe they will not hold up for hours and hours of moving a heavy router around with bricks.

---

Posted on **2017-05-24 20:39:44** by **dougl**:

well, it looks like I just bought myself a couple of window blind openers then.

---

Posted on **2017-05-24 20:49:15** by **dougl**:

The auto wiper motor might not last too long either since from the pics I've seen googling, the worm shaft is metal but the worm gear is plastic.

---

