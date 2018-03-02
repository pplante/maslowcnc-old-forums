## where to buy pcb?
Posted on **2016-11-19 20:56:58** by **rollandelliott**:

I dont' think I can wait 6months to a year for this machine it is that cool;. where can I get the circuit boards on git hub made at? I think I cna do the rest of the projec t.

---

Posted on **2016-11-20 05:04:53** by **TomTheWhittler**:

I doubt that Bar is going to sell the main PCB boards until after the delivery of the backer rewards. It looks like he is going to need about 1100 just for the Kickstarter campaign. Being "open source" the main PCB board is posted on Gethub (https://github.com/MaslowCNC/PCBs) so you could get your own made and then populate it. The project is evolving so that main PCB may change before the rewards ship. Of course that still leaves the encoder PCB's. Lets just hope that Bar was just overly cautious in his time frame and the rewards will be delivered early.

---

Posted on **2016-11-20 09:55:39** by **rollandelliott**:

sounds logical and fair, just can't wait, LOL!

---

Posted on **2016-11-20 11:23:10** by **alstaxi**:

I hope the date is over estimated also. Want this now!! Like my 7 y/o nephew.

---

Posted on **2016-11-20 15:02:03** by **TheRiflesSpiral**:

rollandelliott, there are several tutorials on the net that explain how to make PCB's from copper-clad boards from materials you probably have around the house. If you're looking to do some DIY, that might be the way to go.

If you're not up for that, a quick Google search came up with rushpcb.com, pcbway.com, allpcb.com and sunstone.com/pcb and about a dozen others.

Finally, you wouldn't necessarily need to use a PCB... you might be able to breadboard it out.

---

Posted on **2016-11-21 05:01:14** by **rollandelliott**:

Yes I kind of new that, Just dont' know enough about electronics to figgure out how to solder on all that stuff in the right order, looks like the board has a few resistors, capacitors and H gate chip? can a nerd actually make this off the website details right now? seems like its' missing all the components and specs?

---

Posted on **2016-11-21 05:02:43** by **rollandelliott**:

basically I"m asking if I told rushpcb.,com look at the git hub page would they be able to make it off that documentation?

---

Posted on **2016-11-21 06:24:52** by **TomTheWhittler**:

"Just dont' know enough about electronics.."  That is going to be the tough part. The schematics are there : https://github.com/MaslowCNC/PCBs/blob/master/PowerDistributionBoardSchematic.JPG
The Bill of Materials (BOM) is there : https://github.com/MaslowCNC/PCBs/blob/master/BOM.txt
The firmware is there : https://github.com/MaslowCNC/Firmware
The picture of the PCB shows the parts direction silkscreen.
The PCB and schematic for the motor encoders does not appear to be there but I am sure Bar will eventually get these posted..
Since this is an "evolving" project all of this information is in a state of "flux" so if you "build it" now it may be different than what version Bar finally releases and supports. That could leave you still waiting for a working PCB.
 Kickstarters are not a "off-the-shelf" product. They take time to finish the development as we can see from Bar working out the bugs of the "Z" axis control. That is the purpose of the Kickstarter is to help push that development along at a bit faster rate then a "work it on the weekend" project.
I think Bar might b e a little overwhelmed at this point as I do not think he was thinking this idea was going to be so hot. 
So you really need that have a little "patients".

---

Posted on **2016-11-21 14:23:14** by **TomTheWhittler**:

In case you are really wanting to build your own version the BOM listed seem to be Digi-key parts numbers.
The H-bridge is Digi-key: 497-1395-5-ND that translates into L298N
Searching Ebay for the L298N returns already made driver boards using that part and for interfacing to an Arduino. Some already made Arduino interface boards are for steppers motors and some for DC motors.
There is still a lot of work to go from point A to point B even if you got a set of these boards to control the axis.
I'm am just going to wait till Bar delivers the rewards, Lots to do until then anyways.

---

Posted on **2016-11-21 14:37:08** by **TomTheWhittler**:

This instructables  explains how to get an Raspberry Pi to interface with one of those Ebay modules to drive a DC toy motor.
http://www.instructables.com/id/Raspberry-PI-L298N-Dual-H-Bridge-DC-Motor/
Also a youtube video
https://www.youtube.com/watch?v=AZSiqj0NZgU

This instructables  explains how to get an Arduino Pi to interface with one of those Ebay modules to drive a DC toy motor.
http://www.instructables.com/id/Arduino-Modules-L298N-Dual-H-Bridge-Motor-Controll/
another video on how to interface one of those Ebay modules to an Arduino.
https://www.youtube.com/watch?v=kv-9mxVaVzE

---

Posted on **2016-11-21 14:40:22** by **TomTheWhittler**:

An example of Ebay 298N module interface with Arduino code with some more details..
http://www.allaboutcircuits.com/projects/control-a-motor-with-an-arduino/

---

Posted on **2016-11-21 16:38:00** by **TheRiflesSpiral**:

rollandelliott: I think you're setting yourself up for failure here... I'm not aware of any company, rush PCB or otherwise, that's going to take the information from a website, even under an open source "free use" license, and produce those parts at any price. Basically, if you want it now, you're going to have to (with the help you can get here and on the internet) make it yourself.

---

Posted on **2016-11-22 00:18:13** by **asleborgen**:

PCBs can be manufactured here: https://oshpark.com/

---

Posted on **2016-11-22 11:04:03** by **Bar**:

I'll vouch for those ebay L298N modules, those are what I used on the early prototypes. Getting all the wires hooked up right takes some care but the schematics are up on github. If you are going to DIY one, I would certainly recommend going with the ebay L298N modules over going to all the trouble to have PCBs made.

---

