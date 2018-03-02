## open source parts
Posted on **2017-05-21 18:37:41** by **anotherchavez**:

As this is an open source project, are there links with a detailed parts list anywhere so we can buy our own motors and other hardware?

---

Posted on **2017-05-21 19:03:10** by **davidlang**:

Just a note that they opened up sales of these kits last week again.



The motors are custom built, as is the motor controller board. Everything else is trivial off-the-shelf items (brackets, screws, chain, sprockets, arduino)



But people have built machines already using other parts.



The motors are worm gear motors with an encoder on the motor. they are 200:1 gear ratio motors with a final drive torque of 30 Kg/cm and 8148 pulses per revolution (you could go down to ~2K pulses/rev without loosing much, if any resolution. They put the encoder on the motor, not the output shaft so that a low res encoder gives them lots of accuracy in the final drive (due to the consistent load from the weight of the sled, backlash isn't a factor)



the motor controller sets takes direction (two pins, high/low or low/high) + a pwm input and applies power in the appropriate direction to the motors. you can duplicate the board from the project documentation, or build your own from scratch. This is actually a dangerous hardware design because if a software bug were to set the two direction pin s to the same level and then pulse the pwm pin, the board would fry itself. but absent such software bugs, it works.

---

Posted on **2017-05-23 09:43:16** by **dougl**:

I too am looking for a more complete parts list even if just describing things like chain length and size.

---

Posted on **2017-05-23 09:57:22** by **davidlang**:

the stock setup is

Arduino Mega

custom motor driver board

wires

two motors, 200:1 gear ratio (so about 30 rpm output, 20 Kg-cm torque)

two sprockets (~1cm radius, so 10 or 11 tooth gears)

type 25 roller chain, 2x 10 ft (a little longer than needed)

some 1.25" wood screws

some 2.5 or 2.75" wood screws

brackets to hold the motors to the wood

two brackets to put on the sled, these have holes large enough for the chain to go through with a clip going through the chain to hold it in place (look at pictures of the finished sled and this explanation will make sense)



I think that's what's included (I don't have a beta-test kit so I may be missing some minor part)

---

Posted on **2017-05-23 10:04:27** by **dougl**:

Thanks @davidlang.  I'd just found a BOM.txt file on github which stated the change size and length( https://github.com/MaslowCNC/Mechanics/blob/master/BOM.txt ).  Your data on the motor previous about the 200:1 and 30RPM got me thinking about my wiper motors. I currently use them as a servo motor to steer PRS-RC cars. They have plastic gears so I'm not sure how durable in the long run they will be on a Maslow but good enough for a DIY hack while I wait for the kit. Thanks.

---

Posted on **2017-05-23 10:05:56** by **davidlang**:

oh yeah, I forgot the power supply

---

Posted on **2017-05-23 12:00:40** by **Bar**:

As you go through your build, feel free to edit things which are unclear or could be made better. Pull requests are more than welcome. I know that you are not alone in looking for more information for scratch building the machine.

---

Posted on **2017-05-24 11:30:30** by **dougl**:

I ordered some 10Kg*cm motors to try out. I found them on ebay and besides the lower torque they output shaft is 6mm OD instead of 8mm. I'm also looking at adding AS5047P encoders to wiper motors I already have. The wiper motors used to cost $25ea but are now $35ea and the encoder boards are $15ea. That's $50ea so approaching the edge of what we'd want to spend on the motors. I'll be working with both these motors to see how they do.  link to 10Kg*cm motor: 

http://r.ebay.com/gAi81l

---

Posted on **2017-06-13 15:14:53** by **willishf**:

Looking for a part number for the motors/worm gear. Really just need the worm gear. My google searching isn't turning anything up.

---

Posted on **2017-06-13 15:19:37** by **davidlang**:

as mentioned above, the motor/gear/encoder unit is custom built, there isn't a part number for you to look for and order, please read the discussion above.

---

Posted on **2017-06-13 15:24:24** by **willishf**:

Surprised to hear that it required custom building a worm gear. Can't believe everything you read!!!!

---

Posted on **2017-06-13 15:36:56** by **dougl**:

Having looked myself it would seem nobody makes a steel geared setup with the needed 20Kgcm power at 30RPM. There are things much bigger which do that and very expensive but not any of the more compact ones. The higher power requirements come into play at the top of the cutting area.  Also, the 2 bricks probably greatly improve the cutting accuracy by limiting torque on the sled and providing cable tension. So, maybe if you're good with +/- 1/8" or more inaccuracy maybe smaller motors will work if you use one or fewer bricks.

---

Posted on **2017-06-13 16:42:32** by **TheRiflesSpiral**:

The worm gear isn't the custom part... it's the whole motor/encoder/gearbox/connector that is custom. This isn't a case of: choose motor, bolt on encoder, bolt on gearbox (though you could do that if you wanted to) but a complete unit that can't be bought off the shelf.

---

Posted on **2017-06-13 23:23:53** by **gilbertjm**:

For me it looks like it is the model ET-WGM58A-1220.6 from ETONM Motors (compare http://www.etonm.com/products_detail/productId=104.html ).The encoder could be the ET-MY37. Can be found on alibaba.com, for example. But it is problematic to buy in small quantities. They normaly have a minimum order quantity of 1000.

---

Posted on **2017-06-14 02:26:34** by **davidlang**:

very plausable, Bar has said that they have to order them 1000 at a time.



@Dougl, people have tested with one brick and gotten very good results, also tilting the sled closer to vertical will require less force.



One problem with the current firmware is that it doesn't consider acceleration, so it's going to run into pendulum effects at starting, and overshooting at ending since the sled can't start and stop instantly. At lower speeds you won't notice this.

---

Posted on **2017-06-19 13:10:26** by **netzbasteln**:

It is indeed ET-WGM58A-E (the E standing for encoder) and ET-SGM37F+E for optional Z-Axis. I ordered those three directly at ETONM via Alibaba last week. Sample price (so yo can order small quantities) is $30 for the bigger motors and $20 for the smaller motor. Shipping about $35 to Europe. Makes $115 total. Really looking forward, totally appreciating the great work which was done by the original Maslow team. Thank you!

---

Posted on **2017-06-22 12:58:27** by **DirkD**:

Contacted ETONM yesterday about the motors. got the responce below:



" I know what you look for. we recieved many inquiries already.

 As there are too many samples orders in our sample department,     now we have passed these gear motors samples orders to our  customers in America, you can contact them for samples. "



folowed by a link to maslow ;-)



When will the motor be available? what will they cost?

Thanks

---

Posted on **2017-06-22 13:27:29** by **davidlang**:

unfortunately the first shipment of motors is sold out, and since they have to be ordered 1000 at a time, they probably won't order more until after all the initial orders ship

---

Posted on **2017-06-22 13:42:25** by **Bar**:

They contacted us and told us to stop sending telling people to contact them, we said we weren't but explained the idea of an open source project. They thought it was a cool idea, but said they loose money making samples so unless people are really interested in buying in bulk they don't want to do it any more. (which is why I've been pretty mum about pointing people to the exact motor model, even though it is engraved on the side of each motor)



We are working making them available individually, but goal number one is supporting our existing community and getting these machines sent out, so I can't give you a date other than as soon as possible :-p

---

Posted on **2017-06-24 05:34:50** by **netzbasteln**:

@Bar Thanks for explaining, it's more complicated than it should be. Didnt know Etonm is loosing money shipping samples.

---

Posted on **2017-06-24 06:21:05** by **davidlang**:

very few companies are setup to ship small quantities. They don't have anything close to an efficient process for it. As a result, they end up paying someone who's main job is payed far more to package and ship their samples.

---

