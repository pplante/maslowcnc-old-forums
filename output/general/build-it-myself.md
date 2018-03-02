## Build it myself?
Posted on **2017-03-09 11:02:30** by **nloding**:

I found about this project too late - I was looking at building the MPCNC in the next couple months, but this might work better for my purposes and space, and is slightly cheaper altogether. Everything I read said it was open source, but is that the firmware only? I haven't found any parts list outside of the additional hardware that needs to be purchased.



I'm absolutely willing to source my own parts and build it myself and be a beta tester in that regard. All I need is a parts list! I should be able to piece together the PDU and whatnot with an Arduino Mega, the schematics don't look like the board provides additional logic.

---

Posted on **2017-03-09 11:03:43** by **chauhuh**:

Here is a link to the hardware BOM.



https://github.com/MaslowCNC/Mechanics/blob/master/BOM.txt

---

Posted on **2017-03-09 11:07:42** by **nloding**:

Thanks - do they list what brand/models of those that work? What came in the kits, for instance? "3 meters of stretchy tensioning cord" is extremely vague.

---

Posted on **2017-03-09 11:09:13** by **chauhuh**:

I don't think so. If it was of import I think it would be more specific but it isn't so it probably doesn't matter too much. This might help as well.



http://www.maslowcnc.com/whatsinthebox

---

Posted on **2017-03-09 11:12:01** by **chauhuh**:

The hardest part to source will be the arduino shield most likely as Maslow had them custom made. For this reason alone for most people it will be easier to just order the kit. Perhaps he will sell this as a standalone in the future after things have settled.

---

Posted on **2017-03-09 11:13:24** by **nloding**:

I can breadboard any shield :) That BOM is underwhelming, unfortunately. Looking at the MPCNC parts list, for instance, there is a drastic difference. Hopefully they publish something a bit more comprehensive! I'd love to join this project over MPCNC, but can't right now due to the waiting period :/

---

Posted on **2017-03-09 11:17:25** by **chauhuh**:

That is only the hardware BOM. You can find everything that is needed from the last link I posted. Compared to the other CNC machines I've put together this will be the easiest I think due to the simplicity of the machine. Other BOMs can be found in their respective categories.



https://github.com/MaslowCNC



Wish I had your breadboarding skills...

---

Posted on **2017-03-09 11:23:34** by **nloding**:

The "What's in the box" link isn't loading for me right now, just a blank page. I'll try back. In my experience, the particular motors/steppers/gearbox, sizes of the sprockets and chains, those things make all the difference in the world. Not having any data available makes a manual build outside of a kit extremely difficult.

---

Posted on **2017-03-09 11:34:01** by **nloding**:

The "what's in the box" page just say "2 motors" - but what motors?!

---

Posted on **2017-03-09 11:40:47** by **chauhuh**:

I don't recall off the top of my head but he says in one of his videos. Probably not the best place for that information.

---

Posted on **2017-03-09 11:47:36** by **Bar**:

We are using custom made motors/encoder/gear box combo so we can't link a part number or supplier :-/ 



The minimum order quantity for the motors is 1,000 pcs so we can't sell them individually until we do another group buy of parts.



I'm happy to look at any motor and see if I think it would work. I know that it's frustrating to not be able buy the parts directly.

---

Posted on **2017-03-09 11:57:45** by **nloding**:

Thanks Bar - do you know the specs of those motors? Are they 30 kg-cm of torque at 30 rpm as quoted in another thread?

---

Posted on **2017-03-09 12:16:37** by **Bar**:

I believe that they are in fact 30kgcm at 22rpm

---

Posted on **2017-03-09 12:17:40** by **Bar**:

but as a credit to the original poster, I before that I guessed 30-30 before. Looking at the actual response data this week made me look into it again.

---

Posted on **2017-03-09 16:11:11** by **davidlang**:

the motors have a 200-1 reduction on them and then about a 40 position sensor on the motor shaft

---

