## so... can we see a photo of the controller itself?
Posted on **2016-11-04 16:59:43** by **khammer**:

Am I just missing it in a video somewhere? I'm assuming it's not just a couple of stepper motors and a raspberry pi bolted together, but I would love to see some more photos of the controller machine before pledging. Inspiring stuff so far, i'm excited about getting my hands on one!

---

Posted on **2016-11-04 17:08:09** by **khammer**:

I see motors and a quick shot of a motherboard in the main campaign video... Can we see a shot of everything in the kit?

---

Posted on **2016-11-05 10:07:16** by **Bar**:

Thanks for being stoked!



It's a dual H-bridge shield on an Mega R3 with some extra traces added to route the encoders to the right pins. I'm going to be working on software from a coffee shop today, but I'll try to remember to snap a picture tomorrow. You can see see pictures of the schematics and layout on our github page here: https://github.com/MaslowCNC/PCBs.



The motors are actually regular DC motors with encoders not stepper motors, which makes them a little easier to drive on the hardware side and a little more complicated on the software side :-)

---

Posted on **2016-11-06 07:08:13** by **mooselake**:

Will it have a third driver for the Z axis?

---

Posted on **2016-11-06 12:43:37** by **Bar**:

Yes. The H-bridge is actually 2-channel so you will get four channels on the Z-axis version. I'm not sure what to do with that 4th axis, but I'm sure someone will come up with something amazing

---

Posted on **2016-11-14 17:38:18** by **Bar**:

And here is a photo of the PCB  [DSC00338](/images/c8/TX/c8TX_dsc00338.jpg.jpg)

---

