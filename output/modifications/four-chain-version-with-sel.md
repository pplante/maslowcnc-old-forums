## Four chain version with self-tensioning bottom chains
Posted on **2017-06-23 03:15:20** by **silverwarior**:

Some time ago I recommended development of four chain version of Maslow CNC router in order to avoid inaccuracies when sled moves below one of the chain motors which is caused due the fact that tension on the longer chain decreases.



At the time there were some concerns that controlling four chain motors might be problematic due to limited processing capability of arduino controller as it would require double the math.



I have been thinking about this a lot lately and I come up with the idea for four chain design which would not require any changes in existing software whatsoever. 

How can that be done? 

You make bottom two chain motors aware of the chain tensions so they can pull-in or release their chains in order to maintain desired chain tension.



So how to make the chain motor be aware of the tension it is making?

First instead of attaching the motor directly onto the corner you make sure that there is a spring between the motor and the attachment point. 

So when tension on the chain increases the spring will stretch and when decreases the spring will contract. Then  all you need to do is detect how much stretched the spring is. There are multiple ways of doing this. 



You can use sliding potentiometer. 

The advantage is that it would give you precise reading of how stretched the spring is so you could fine control the speed of the motor so it would be possible to correct the chain tension as fast as possible. 

The disadvantage is that if for some reason you stretch or contract the spring too much you could easily damage the potentiometer.



Another approach would be to use carefully positioned switches to give you approximate information of how stretched the spring is. 

I would recommend using of four switches for this placed so that they would be enabled/disabled based on how stretched the spring is.

Switch 1 should be enabled when there is no tension on the chain (spring isn't stretched). This switch would send signal to controller to stop working because there always needs to be some tension of the chain.

Switch 2 should be enabled when there is very little tension on the chain (spring is stretched a little). While enabled chain motor should be quickly reeling in the chain in order to increase its tension.

Switch 3 should be enabled when the tension of the chain is reaching (increasing) close to desired tension (spring is stretched some more). While enabled chain motor should still be reeling the chain in but now at slower speed.

Once the chain tension reaches desired tension (spring is stretched to desired length) none of the switches is enabled. At this time the chain motor is stopped.

Switch 4 should be enabled when the tension on the chain starts increasing past the desired tension (spring is stretched more than desired). While enabled the chain motor should be slowly reeling out the chain in order to reducing the tension on the chain.

Switch 5 should be enabled when there is high tension on the chain (spring is stretched way past the desired length). While enabled the chain motor should be quickly reeling out the chain in order to quickly reducing the chain tension.

Switch 6 should be enabled when chain tension passes the safe level (spring is stretched a lot). Once this happens a signal should be sent to controller to stop working. This switch acts more like a fail safe to prevent the contraption from literally tearing itself apart.



If you have any further questions about this idea please do me know.

---

Posted on **2017-06-23 03:50:26** by **davidlang**:

The biggest issue with the 4-chain approach is cost. It will roughly double the cost of building a maslow.



Yes, it will allow the router to be moved faster (no need to depend on weak gravity-based forces at near vertical angles), but beyond that are there any other advantages?



Some people have claimed that it would make the machine more accurate, but I have never seen anything to back it up.



Please build such a machine and show that it is significantly better (enough better to be worth doubling the costs)

---

Posted on **2017-06-23 04:08:52** by **silverwarior**:

Yes I agree with your claim that this will increase the cost of the machine. But my idea is formed in a way that this four chain setup actually acts as an optional upgrade of existing low cost two chain version. 

So only people who actually needs such high precision would be buying/using it.



As for building and showing it myself. Currently I'm working on some other projects but I'll definitely do this someday in the future.

---

Posted on **2017-06-23 04:09:59** by **davidlang**:

why would a 4-chain machine be any more accurate than a 2-chain machine?

---

Posted on **2017-06-23 14:51:56** by **silverwarior**:

We already discussed this in "Longer arms and steel mount plate" thread before.

---

