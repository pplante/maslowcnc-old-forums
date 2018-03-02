## Brand New - Where do you source parts?
Posted on **2017-06-28 08:34:10** by **spankurmonkey**:

I just found this and would like to build but I am confused.... is there a parts list or is there some sort of waiting list to get a kit to build?   I have built a MPCNC but this format for simple 4x8 sheet cutting seems like a pretty easy way to go.   I know I can read and read, etc just need someone to educate me if you have a moment.

---

Posted on **2017-06-28 08:55:08** by **davidlang**:

right now all the available kits have been purchased (but not yet shipped),



There is a bill of materials at https://github.com/MaslowCNC/Mechanics/blob/master/BOM.txt



But this includes two custom parts, the motors and the motor driver board. The motors are only available from the manufacturer in quatities of 1000+, the motor driver board is custom manufactured (but all the design files for it are on github)



see the topic "found the dc motor gearbos with encoder" and the topic "open source parts"

---

Posted on **2017-06-28 10:13:50** by **rollandelliott**:

as usual davidlang is right, while the project is described as open source in theory, in reality unless you want have thousands of dollars you can't get the parts in order to make it unless you buy it from the founders.  Even if the motors are only $10 each that is $10,000 minimum order ad they probably cost 2x to 3x that.

---

Posted on **2017-06-28 10:40:59** by **TomTheWhittler**:

That is not necessarily true that it requires custom parts.

A while back Bar wrote that his first version used a standard Arduino and a standard Ebay H-bridge. He also used some standard off the shelf  motors until he came across ones that seemed to worked well. That is not saying that there are other motors that might work as well. Bar did open source the PCB layout and schematic. Being open source you can substitute alternates.



So you could use a standard Ardunio and a couple of these Ebay H-bridges that do 5 amps.

http://www.ebay.com/itm/DC-12-30V-5A-H-bridge-Brush-Motor-Driver-PWM-Brake-For-Smart-Car-Arduino-/170916785405?

and then a couple of these motors.

http://www.ebay.com/itm/High-Torque-Turbo-Worm-Gear-Motor-100RPM-DC24V-3-43NM-GW6280-with-Sensor-DIY-New/112043801280?

You will have to do your own wiring harnesses but you should be able to "roll your own". The software may have to be tweaked for the motor encoder used but that should not be to hard to change.

---

Posted on **2017-06-28 12:15:18** by **rollandelliott**:

Well obviously it's a little bit harder than one might guess otherwise people would already be doing it

---

Posted on **2017-06-28 14:04:32** by **TomTheWhittler**:

RollandElliot, I suppose you could be right that it maybe a littler harder.  There were a couple forum members that missed the betas and were trying to build their own. Forum users raidonchrome, garyw17, and kiwimaker were a few that indicated at one time they were going to try to roll their own from post in the technical section.

It could be people have done it but just are not communication the fact.

---

Posted on **2017-06-28 15:09:30** by **davidlang**:

The hardware isn't that hard, the software to drive it is where a lot of the real complexity is. The good news is that now it's written, it can be used and adapted to run other similar machines.



There's already one person who has forked it to run with stepper motors and gearboxes instead of the initial brushed dc motors and encoders.

---

Posted on **2017-06-29 17:36:09** by **jwolter0**:

It also should be noted that Bar has stated that he intends on establishing a store with a vendor for people to buy replacement parts, which would also be useful to those who wish to roll their own.  With the Kickstarter orders for non-beta testers almost, but not yet filled, I imagine he's been a little busy to get that in place. :-)

---

Posted on **2017-06-30 08:54:06** by **mooselake**:

I wouldn't expect them to be anywhere near the $10 mentioned above, or the $13.50 price mentioned on Alibaba - that's FOB in China (less shipping, stands for free on board as in sitting on their shipping dock).  Besides the shipping cost, interest, overhead, storage, time away from the kits, etc.  Bar's taking a risk if he's bought many more than are sold/preordered/DOA spares, and it's unlikely he's got a few thousands (or tens of thousands) of $$ to order very many motors on spec in this batch.



The wait list page is linked from their home page, or look at https://www.maslowcnc.com/reservations/maslow-cnc-reservation



If  you're going to roll your own you'll need to experiment with motors that you can find/scrounge/dumpster dive for.   Post the results.  Have fun!

---

Posted on **2017-06-30 09:29:57** by **davidlang**:

Also, Bar is going to be pricing the parts to encourage people to buy the full kit rather than the parts individually.



He may also find it necessary to raise the price of the kits after the kickstarter (for the kickstarter, he knows how many he needs, and doesn't have money sunk in inventory sitting around, after  the kickstarter, he has to pay for storage, account for the cost of money that's sunk in the inventory, etc)

---

