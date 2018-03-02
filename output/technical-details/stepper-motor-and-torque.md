## Stepper motor and torque
Posted on **2017-06-07 23:34:53** by **davebone**:

As the Maslow cnc is not currently available to order, I am wanting to make somthing similar, I know the Maslow motors are 30kg /cm torque, but will this motor be suitable( NEMA23 - 425 oz-in torque).

https://www.aliexpress.com/item/CNC-Router-Kit-3-Axis-kit-ST-M5045-replace-2M542-driver-5-axis-breakout-board-Nema23/32297927235.html?spm=2114.01010208.3.298.AVVxQ4&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_10151_10130_10068_5010019_10136_10137_10060_10138_10131_10155_10062_10132_10133_437_10154_10056_10055_10054_10059_303_100031_10099_10103_10102_10096_10052_10053_10050_10107_10142_10051_10084_10083_10119_10080_10082_10081_10110_519_10175_10111_10112_10113_10114_10182_10078_10079_10073_5030019_10123_10120_10189_142-10120,searchweb201603_2,ppcSwitch_3&btsid=9f101de4-61cf-4a94-aaa9-2db8e9c168e1&algo_expid=53c2cff4-0393-4928-9d5f-ade6335bbabd-41&algo_pvid=53c2cff4-0393-4928-9d5f-ade6335bbabd

Thanks

---

Posted on **2017-06-08 01:59:20** by **dennisbingham**:

@davebone someone else recently asked about stepper motors, and they said the software changes to run them could be pretty extensive. If you're looking at prices like that, you might look at servocity.com. they have a whole section of encoder motors with decent oomph and they stock a worm gear assembly that seems pretty sturdy.

---

Posted on **2017-06-08 01:59:32** by **davidlang**:

well, since the maslow firmware won't drive stepper motors, not without a lot of work. that's in the ballpark for the right amount of torque, but someone would need to add an option to the maslow firmware to driver steppers instead of a closed-loop motor.

you would also be going from 8k steps/rev to 400 steps/rev or so, so your accuracy would suffer.

It would be good to have someone include such an option, but nobody has started work on it yet.

---

Posted on **2017-06-08 08:29:25** by **Bar**:

The biggest thing I would worry about with steppers is that when the machine looses power the sled is going to fall to the floor which seems like a safety issue. Running steppers through a gearbox with a worm gear in it could solve the issue, but then you are doing a lot of work to use the steppers and still have to sorce a gearbox

---

Posted on **2017-06-10 08:26:12** by **kentthoresen**:

would anyone be interested in making the stepper motor adjustment for money?

---

Posted on **2017-06-12 07:29:11** by **kentthoresen**:

Never mind i hired a programmer to add stepper motors as an option it will be forked on github and open source free for all. (except me)

---

Posted on **2017-06-18 15:43:19** by **davidthomasgross**:

It would be nice if one could use Mach 3 or linux cnc I have a cnc I built but if I get the Maslow I'll just add gc to that computer

---

Posted on **2017-06-18 15:49:39** by **davidthomasgross**:

I would like to use those motors on my cnc I constantly loose steps and a close loop system might help with that an idea might be a mini Maslow like 4'x2' or even 2'x2' just for like signs and stuff I'm pretty sure I read its scalable

---

Posted on **2017-06-18 16:49:37** by **davidlang**:

unfortunantly neither Mach3 or LinuxCNC have the ability to handle the geometry of this machine. It's not just a matter of stepper motors vs brushed DC motors/encoders.

---

Posted on **2017-06-20 11:16:02** by **kentthoresen**:

I have released the stepper motor version on glip please help test it if you can

---

Posted on **2017-06-24 05:51:22** by **netzbasteln**:

very cool! can you provide an url?

---

Posted on **2017-06-24 06:44:32** by **kentthoresen**:

the tread is called "Stepper motor with gearbox" just search the forum.

---

