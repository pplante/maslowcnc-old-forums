## Curious about encoder placement
Posted on **2016-10-19 07:50:26** by **TheRiflesSpiral**:

Hello!

I was looking at the videos today and something caught my eye that I am curious about; you mention that you originally wanted to put an encoder on the sprocket drive but ended up with a servo...

What's the rationale behind monitoring the motor's motion as opposed to the sprocket? Wouldn't gear/chain lash be better represented in data by monitoring it there instead? (I'm not suggesting there are positional errors in Maslow; just curious is all.)

---

Posted on **2016-10-19 11:56:42** by **Bar**:

Great question! 

Backlash should be an issue if we were using a standard CNC design where the torque changes direction as the motor changes direction. 

We have the unique (and wonderful) situation that with the router and bricks hanging from the sprocket, the torque is always in the same direction.

If the router were to ever move downwards so fast that the router and bricks were in free fall, the direction of torque would reverse, but we never move even close to that fast.

The net effect is that the slop in the gear train is always taken up in the same direction.

So that's why we CAN move the encoder to the back of the gear box without loosing resolution, but why SHOULD we. 

Being brutal about reducing the complexity of the machine is key to getting as many people building things as possible. The simpler the machine is, the easier it is to put together, the easier it is to use, and the cheaper it is.

One of the parts of the design that I am most proud of is how simple it is. We've engineered away almost everything. Every piece serves a critical purpose.

By incorp orating the encoder into the motor, we got rid of an extra wiring harness, and extra PCB with associated mounting hardware, and a magnet (which had to be aligned precisely). We also ended up with higher resolution at a lower price which is always nice :-)

P.S. Don't worry about offending us with questions. We're an open project, we have no secrets :-)

---

Posted on **2016-10-20 05:35:23** by **TheRiflesSpiral**:

That makes total sense. Low speeds and lightweight chain should prevent chain lash too. Then it becomes a matter of weight and friction. (And a nice, sharp bit, of course). Thanks for the insight!

---

Posted on **2016-11-18 05:15:31** by **boblq**:

I love your goals. But how best to reach them? 

Mass produced DC motors for windshield wipers are hard to beat for cost. 

So how to monitor the position of the chain? 

An LED/photocell on a single printed circuit can do that. It could be an extension of the arduino (or whatever is the main microcomputer) printed circuit board so no wiring harness is required. The chain position is just a matter of software, right?

---

Posted on **2016-11-18 05:37:40** by **boblq**:

Now for the other stuff. Z-axis. 

I am not advocating any of these "ideas" I am just throwing them out for consideration. 

The most obvious thing to do is have another chain that can lift the router in the Z direction. Then all that is needed is software.

Indeed all of the existing systems can be reused. Very little perhaps no hardware design in needed beyond a frame for the z axis. 

Then it is all just software/

This is the beginnings of  a limited xyz carving machine. 

Limited because of issues of access to the entire volume. 

So it goes.

---

Posted on **2016-11-18 05:45:59** by **boblq**:

If we imagine the hanging router being suspended by three chains form the ceiling then the router can obviously be moved any where in a 3D volume described by the chains. 

Now suppose he router is mounted on a plate that can rotate around a vertical axis. The the router can point at any point in the space. 

By controlling the chains the router can move in any direction. Thus we can build a 3D carving machine.

---

Posted on **2016-11-18 05:46:27** by **boblq**:

Ain't this fun ;-)

---

Posted on **2016-11-18 05:51:55** by **TomTheWhittler**:

There are other geared motors with encoding already build in that are fairly cheap.
http://www.ebay.com/itm/262494873809?
Why re-invent the wheel..
This is about that same type of motor as Bar was showing in the design video although Bar did stated he had them custom made with encoder.
I am sure you could get any geared motor to work (like car window motor) as long as you have an encoder feedback.

---

Posted on **2016-11-18 05:53:27** by **boblq**:

For some purposes it would be useful to allow the router to be rotated around other axis as well as the vertical axis. 

Use cases will help sort this out. 

A lot of these problems are quite analogous to those that must be solved to point a camera on a drone. So perhaps some of the needed software can be lifted directly from the drone folk.

e,g, https://github.com/yck011522/drone

---

Posted on **2016-11-18 06:13:48** by **boblq**:

A final comment then to sleep. I am a 75 year old man living in the Philippines. 

With the addition of a resin squirting head the 3D verson could also become a 3D printer. 

I note that while 4x8 is a perfect size for the DIY guy in garage, this thing can scale to mega size :) 

Brilliant work BAR,

---

