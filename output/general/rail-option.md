## Rail option
Posted on **2017-05-22 06:06:54** by **danstuart**:



---

Posted on **2017-05-22 06:09:13** by **danstuart**:

New to CNC. Looking for a cheaper option then then manufactured ones. How difficult would this system be to change over to rail system, I have the plans already to build the rails worked out, just not sure about all the programming stuff.

---

Posted on **2017-05-22 06:22:32** by **davidlang**:

It would be a complete re-write of the motion software. you would be better off looking at the grbl firmware to drive a traditional gantry machine.

---

Posted on **2017-05-22 06:50:22** by **danstuart**:

But the hardware could all be used correct? My understanding is that's what you're paying for. As the software is open source. So I could get the kit and use the other mothin software instead? Sorry for all the newb questions. Like I said, new to this....great with my hands, just not much into programming stuff.

---

Posted on **2017-05-22 06:52:18** by **scottsm**:

Gantry systems typically use stepper motors, this system uses conventional motors. A pretty big difference, not much of the hardware would cross over :(.

---

Posted on **2017-05-22 06:52:47** by **davidlang**:

yes, but the other motion software probably won't talk to this hardware.



almost all other CNC machines are based on stepper motors, this is based on worm gear driven motors and encoders, you aren't going to find other software that knows how to talk to it. you would have to do all the programming from scratch.



Since you say that the programming stuff is not what you are sure about, this would be a bad place to start

---

Posted on **2017-05-22 07:00:58** by **danstuart**:

Well crap. Thanks anyway

---

Posted on **2017-05-22 10:06:46** by **rollandelliott**:

There are several companies that sell control boxes for stepper motors that are around $500

---

Posted on **2017-05-22 10:46:38** by **jwolter0**:

You won't be the only one to abandon a gantry type CNC after having bought some of the parts, if you choose to do so.  We had already bought DIN rail and v-groove bearings when we discovered Maslow.  Fortunately, we hadn't bought our motors or controllers yet.  Eventually the parts we bought will go into a 2-axis CNC drill press table, though that project is a lot lower on our priority list.

---

Posted on **2017-05-22 14:31:10** by **gero**:

The Rial option for the current hardware and design is following me since I built the frame. At least a rail-supported option.  [RailMSLW](/images/3n/3nfz_railmslw.jpg.jpg) 

The challenges would be not only that plenty of the math have to be changed. There is also the fact that the 4 horizontal tubes would be around 3m, so a droop is expected. The top and down one can be supported, but not the 2 at the sled. Bought bearings for this job would cost quite an amount. Not sure if DIY V-bearings could be done.

Advantages would be: No tilt of the sled, less friction, 2.5D cutting as the sled is not resting on the material. Still the challenges are too many for me, but dreaming is allowed.

---

Posted on **2017-05-22 15:35:48** by **thejuggler**:

The other possibility for a rail like option would be to build a picture frame around the main backing board that was part of the main frame, then modify the sled to have arms that extended and sat on this border.  Then whole thing may have to be higher off the ground due to the arms, meaning a pretty high ceiling in the room it's in, but then there's no need for the new math, the sled will still rotate, but it would remain above the surface of the work, so you're not running on top of the cuts.  Obviously if the border is smaller,  meaning the work surface is smaller, all of this is easier :)

---

