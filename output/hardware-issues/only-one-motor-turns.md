## Only one motor turns
Posted on **2017-03-19 12:01:59** by **Bar**:

@blsteinhauer88 has been having an issue where only one motor seems to respond as expected. The other motor will rotate under some circumstances, which makes me think it could be a software thing and not a hardware problem, but hardware is not ruled out.



I've add a "Test Motors" button Ground Control which will give us more information about what's going on. If you can grab the latest version of Ground Control from https://github.com/MaslowCNC/GroundControl and the latest firmware from https://github.com/MaslowCNC/Firmware I think we can find out more. 



After clicking the "Test Motors" button in the "Actions" menu I would expect to see something like:



Testing Left-axis motor:

Direction 1  - Pass

Direction 2 - Pass

Testing Right-axis motor:

Direction 1  - Pass

Direction 2 - Pass

Testing Z-axis motor:

Direction 1  - Fail

Direction 2 - Fail

Tests complete.

---

Posted on **2017-03-19 17:39:02** by **blsteinhauer88**:

[Image](/images/xI/g4/xIg4_image.jpg.jpg)

---

Posted on **2017-03-19 17:39:45** by **blsteinhauer88**:

Curious, says left motor failed but the left one is the only one moving.

---

Posted on **2017-03-19 17:40:01** by **blsteinhauer88**:

I have the new ground control and I uploaded the new firmware.

---

Posted on **2017-03-19 18:02:00** by **blsteinhauer88**:

Here is the arduino serial monitor.

---

Posted on **2017-03-19 18:04:08** by **blsteinhauer88**:

[IMG_0435](/images/tC/6s/tC6s_img_0435.jpg.jpg)

---

Posted on **2017-03-19 18:27:26** by **Bar**:

Ok, what happens if you plug the motor which isn't moving into the z-axis plug (the middle one which isn't currently used)?

---

Posted on **2017-03-19 18:29:26** by **blsteinhauer88**:

It moved

---

Posted on **2017-03-19 18:30:31** by **blsteinhauer88**:

It also states over and over" unable to resolve position error"

---

Posted on **2017-03-19 18:30:32** by **Bar**:

Perfect!



Did it say test passed for the z-axis?

---

Posted on **2017-03-19 18:30:51** by **Bar**:

Excellent!

---

Posted on **2017-03-19 18:31:23** by **blsteinhauer88**:

And actually said z-axis failed let me run it again it went fast

---

Posted on **2017-03-19 18:31:46** by **Bar**:

I know that doesn't seem like an excellent thing, but it used to just hide the problem and not move, but now at least it tells us something is wrong

---

Posted on **2017-03-19 18:32:11** by **Bar**:

I'm going to run the same thing on my setup and see if mine says pass or fail with one motor plugged into the z-axis port

---

Posted on **2017-03-19 18:32:52** by **blsteinhauer88**:

[IMG_0436](/images/R3/09/R309_img_0436.jpg.jpg)

---

Posted on **2017-03-19 18:37:32** by **Bar**:

Interesting, I'm seeing different behavior. Mine looks like this:

---

Posted on **2017-03-19 18:38:04** by **Bar**:

[Motor tests](/images/Ko/aN/KoaN_motortests.jpg.jpg)

---

Posted on **2017-03-19 18:38:17** by **Bar**:

If you swap the motors do you see the same thing?

---

Posted on **2017-03-20 08:45:19** by **blsteinhauer88**:

First thanks for the test motors.  It is simple and helped me track down problems.  



So after several combinations of motors and cables.  I found a bad cable.  Assuming the yellow wire is #1, the orange wire (#3), has no continuity from connector to connector.  I assume this is why when this cable was used, the test rendered movement but a fail report to the test request.  Next I learned that as the Maslow Board (motor controller) is set up, Left control cable attached to port #1, Z axis is port #2, and Right  cable is attached to port #3, #4 is open.  If this is true...My left port reports from the test at the right port, Z axis is correct, and port #3 reports as left port.



These are my results I am not a programmer, I am more the End User type tester, So to me I have a bad cable and a bad board.  



Re the cable Bar, I not only tested the Orange wire by the connector, but also behind the connector into the wire itself, so there is a break somewhere in the shielded area.

---

Posted on **2017-03-20 08:52:38** by **Bar**:

Great deduction! 



I'm going to express ship you a new board and a new wire first thing this morning.



I think the board is OK, the directions should be reversed because it mounts on the back of the machine (which flips the directions) but I'd rather not take any chances. I'll feel better knowing that you are using the board I've been using which is pretty throughly tested at this point. 



Our apologies again for the trouble and great deduction!

---

Posted on **2017-03-20 09:10:37** by **blsteinhauer88**:

If I interpreted the board wrong I can swap the leads.  Thanks for getting those to me.

---

Posted on **2017-03-20 10:09:55** by **jbarchuk**:

> @blsteinhauer88

>  I found a bad cable. Assuming the yellow wire is #1, the orange wire (#3), has no continuity from connector to connector.

That's a moderately frightening symptom. Frightening in two senses.

First, this is a very easy mechanical assembly process. Easy when the equipment is set up properly, BUT with wrong setup or using wrong tools can cause broken strands either immediately OR...

Second, it can cause strand breakage LATER during assembly or operation. Meaning the strands were damaged when the wire was crimped, and a few strands broken, then more strands break later.

The scary part is when it fails later, machine stops working for no apparent reason, and can start working again when wires are wiggled. Troubleshooting is a biiiiitch. The easy fix is to change the cable, but there's no way to know HOW MANY cables were assembled that way!!

These are actually very nice looking cables, commercial quality not consumer quality. Very nice wire, braid and connectors. That shrink tubing that covers the braid and the wires, that's not plain vanilla shrink. There' s -adhesive- inside the tubing that when heated melts into the braid and also -grips- the wires -much- better.

This is very weird, that a nice cable has a bad crimp, but accidents happen. Let's just hope it's a one-off and not a widespread issue.

It'd be a good idea to add a note to the assembly wiki, that IF the machine exhibits odd, occasional unrepeatable operational behavior that the cable continuity should be tested while bending and twisting the cable a little.

---

Posted on **2017-03-20 10:11:20** by **jbarchuk**:

> @blsteinhauer88

> If I interpreted the board wrong I can swap the leads. 

Unclear: Is there still an open connection?

---

Posted on **2017-03-20 10:16:04** by **Bar**:

Im supprised too. Wouldnt expect to see a bad cable. I think we need an automated system tester like a bulked up version of the "Test Motors" function. It should be pretty easy to diagnose with the right set of steps. It could work something like test both motors, if one doesn't work, swap the motors, if the problem switches side, we know it's a motor, if not swap the wires, if the problem moves with the wire it's a wire thing, if not it's a board thing. Having a clear set of steps/tests could get us an answer quickly.

---

Posted on **2017-03-20 10:44:23** by **scottsm**:

Certainly getting the faulty cable to Bar would help identify the issue, whether workmanship or material defect.

---

Posted on **2017-03-20 11:08:42** by **Bar**:

Would you be willing to hang onto the bad one until we have an open house or meetup so I can take a look at it?

---

Posted on **2017-03-20 11:24:55** by **blsteinhauer88**:

Being an average mechanically inclined person,  It would be help full to self diagnose an issue if the test would also tell if the correct voltage was being applied to the motor and turning the gear right or left as you look at it.  This would make sure the motor is running the direction it is supposed to be driving.  Instead of Direction 1 and Direction 2, "Left of Right. 



On the Test results also Mine says Test Complete as Bar's did, then mine starts this string of text "Unable to resolve position error".  I does this over and over until the test results are off the small window to view it.  A scroll feature to look back would be helpful.  I assume the reason for that text was related to the cable?



Back to the wire cable, I can run the cable to you this Friday Bar if your going to be at the art center.

---

Posted on **2017-03-20 11:31:40** by **Bar**:

Great suggestion! I will make it say clockwise and counter clockwise. 



The "unable to resolve position error" happens when the chain lengths need to be calibrated. Basically the internal math can't find a solution for where the router is if the chain lengths are unknown. You can make it go away by running the "calibrate chain lengths" procedure (with working cables :-( ) I added that error yesterday because before it wouldn't tell you anything was wrong, but it's super annoying how it just keeps saying it over and over again so I need to find a better solution, hopefully today.



If you are willing to drop it off, that would be fantastic! Thanks so much.

---

Posted on **2017-03-20 11:34:30** by **blsteinhauer88**:

And because I could never complete the calibration of the chain due the wire, it was giving me the error..GOT IT.   No prob, it will bring the cable and a coffee for you and Hanna if you like... :)

---

Posted on **2017-03-20 11:41:10** by **Bar**:

Deal, but really we should get YOU coffee for sticking with it! How about we drink the coffee from the communal pot in the kitchen and pick your brain about how everything is going and what steps we can make simpler?

---

Posted on **2017-03-20 11:48:27** by **blsteinhauer88**:

Deal!

---

Posted on **2017-03-21 08:42:04** by **blsteinhauer88**:

Bar, I spliced the orange wire which, as you saw, was completely cut in the middle.  The braided  case was no damaged so I think the manufacturer just somehow got a damage piece in there.  Anyway that one Orange wire was the entire problem.  The board is fine.  I got it to calibrate the motor, it measured the chain on both sides, and  when I installed the temporary sled it ran one of your practice Gcodes perfectly.  I cant wait to cut the sled out tonight after work.

---

Posted on **2017-03-21 08:49:04** by **Bar**:

So cool!!!! Great work tracking that down and then solving it :-)

---

Posted on **2017-03-21 15:41:38** by **jbarchuk**:

> @blsteinhauer88

> Bar, I spliced the orange wire which, as you saw, was completely cut in the middle. The braided case was no damaged so I think the manufacturer just somehow got a damage piece in there.

That's extreeeemely weird. To the point of being not possible. It's almost impossible to think that an operator would have a wire cut in two pieces, crimp the pins on one end of all the wires, insert all the wires into the braid with the loose ends of wire hanging free, then crimp the wires at the other end without noticing that that one wire wasn't lining up nicely.

That couldn't have been an accident. Something skanky happened.

I worked in a place making guitar amps. Some people didn't like me because my work looked 'too good.' One day I looked at some amps on the 'finished' shelf, and one that had a tag with my name on it was CLEARLY not mine. I looked around and found the one that was mine, with a different tag on it. I didn't say anything about it because there was no way to say that the person with that other name on my part was the person who actually changed th e tags. The point is that there can be nefarious skuiduggery hiding around any corner waiting to pounce. That cut wire could have been done as deliberate sabotage to make someone look bad.

---

