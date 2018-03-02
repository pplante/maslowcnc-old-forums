## Z-Axis can't keep up?
Posted on **2017-06-18 21:27:14** by **John**:

Hello, I'm just starting to have another play with Maslow and am hitting an issue with the z-axis not being fast enough. At first I assumed I had set the z-feed rate too high in MakerCam. However, I've tried dropping the feed rate to almost nothing and it had no effect.



I also see the same issue when just cranking the z-axis in and out using the Ground Control buttons. Basically, Ground Control gives up waiting for the z-axis to finish moving long before it has reached the correct position. E.g. in GC, I set the revs/mm to 1.0, set the button depth for 10mm and hit z-in. The shaft makes 4.5 turns and stops. I set the depth to 1mm and hit z-out. The z-axis continues feeding in until it finishes the ten turns. I hit z-in again and it goes out 1mm. In other words, all the commands are being sent and the firmware/motor will eventually catch up but a long time after GC has moved on to something else. Note that GC knows what is going on, the Z-depth read out seems to match the physical position. But GC seems ignores that it hasn't gone far enough yet and moves on to the next  task regardless.



I first hit this issue with GC v0.69 or 0.70 and FW v0.67 or 0.68. I've just been running with 0.76/0.76 and it does exactly the same.

---

Posted on **2017-06-18 23:22:32** by **Bar**:

I think you've diagnosed the problem exactly right. What type of router are you using and what is the pitch per rotation?

---

Posted on **2017-06-19 00:46:43** by **John**:

Not sure how it is related to the router itself?



Either way, I was using a Bosch GMF1600 at 1.6mm/rev. However, I've come to the conclusion that it really doesn't like being cranked in/out when mounted sideways. Something would always grind between the motor and the base and cause it to jam (to the extent of requiring sanding the inside of the base down to make it smooth again!).



I have since switched to a DIY job - a scew Z-axis and CNC spindle that I picked up on ebay. Not sure what the new mm/rev is because I haven't been able to calibrate it due to the above issue! Currently GC is set for 1mm/rev so that I can move the axis by a whole number of revolutions via the Z-in/out buttons. Or at least, that's what I want to do if GC would behave!

---

Posted on **2017-06-22 15:42:08** by **mcginniwa**:

Darn. Was checking back in today to see if anyone had gotten Bosch router Z-axis working reliably yet. I had [some headaches](http://www.maslowcnc.com/forums/#!/hardware-issues:bosch-gof-1600-ce-z-axisde) with the GOF 1600 and hadn't gotten them resolved before I had to work on something else for awhile.



There's a whole lot of background (there's a link to even further detail in a previous thread in that thread), but it does sound like you are having similar problems to what I was having.

---

Posted on **2017-06-22 16:56:20** by **gero**:

Did you read the posts about the backlash in the Z? I ignored them for a while, but any kind of rubber pulling down the router and not to strong to to interfere with the Z-Motor gets rid of that issue.

---

Posted on **2017-06-22 17:07:08** by **gero**:

That Z is lowering into the cut is/was a software issue. The moves on X and Y are/were not waiting for Z to complete.

---

Posted on **2017-07-18 11:50:46** by **krkeegan**:

I am pretty sure I saw behavior last night and I have the standard ridgid router.



In my case, I was using the temporary sled without weights.  I also used Fusion 360 to generate my tool path.  



What I saw, was that at some places on the work surface, the machine had a very hard time holding position (likely because of the lack of weight).  When the z-axis is rotating, the machine would actively try and hold position which resulting in a ton of movement.



It seemed like the excessive XY movement slowed down the Z movement, almost like the controllers can only do either XY or Z at any given time.



The result was that the Z-axis would not move the entire required distance.  This happened both moving into and out of the wood.



Again, this only seemed to happen when it was difficult of the machine to hold its position, otherwise the depths were fine.



I am moving to the standard sled with the bricks tonight, but if I see this behaivor again, I will try and record it.

---

Posted on **2017-07-18 15:04:19** by **Bar**:

I think this might be related to the memory overflow issues we found and addressed yesterday. Either grabbing the very latest firmware off GitHub or using v0.81 which will come out tomorrow might fix this, it also might not so lets keep an eye on it.

---

Posted on **2017-07-19 09:45:50** by **krkeegan**:

You were right.



I did the following:

1.ran the operation again and had the same results;

2.downloaded and installed the new firmware;

3.ran it again, and everything was fixed.



In fact, many aspects seem waaay better.  This got rid of a lot of shaking that was occurring.  A significant improvement.

---

Posted on **2017-07-19 10:14:36** by **Bar**:

Woo!!!! Thank you for taking the time to run that test, I'm stoked to hear it fixed the problem :-)

---

