## Emergency Stops
Posted on **2017-03-06 17:36:39** by **tmaker**:

Let's say that I'm in the middle of the cut and need to stop in the middle for some reason.  Is the router power in sync at all with the Ground Control software so that if I hit the stop button on the router it won't continue to try and move the bit and possibly break the bit?  Should the router or Ground Control be stopped first?  Also, let's say that I'm not happy with the cut and want to made an adjustment to the feed rate in the middle of a cut.  In this case, is the Ground Control software smart enough to continue where I left off after making the adjustment?  Or will it require that I start over completely if I need to stop and make adjustments?

---

Posted on **2017-03-06 18:03:58** by **Bar**:

The router power isn't connected to the Maslow controller PCB at all so Ground Control doesn't know if the router is on or off. I chose to do that because I didn't want to encourage people to work with high voltages and having the software control the router seems dangerous when changing bits. Using the built in power switch on the router seems like the safest way to me.



If I have a cut which is going wrong, I always stop the machine from moving by pressing the STOP button in Ground Control before turning off the router, because like you said if the machine is moving and you turn the router off it can break the bit. 



There is a feature request for the ability to change the federate in real time while cutting which I think is a good idea (and probably not too hard to implement). I would expect to be able to change the speed without stopping soon.

---

Posted on **2017-03-06 18:11:00** by **davidlang**:

@bar, will that ability to change the feedrate override the feedrate in the gcode? what will happen the next point that the gcode sets the rate?

---

Posted on **2017-03-06 18:12:52** by **Bar**:

I was wondering about that, then I saw someone else's software that had a slider that would let you scale from .25x to 5x the original file's speed. That way you aren't messing with the g-code, just fast-forwarding it which seemed like a sleeker way to do it to me.

---

Posted on **2017-03-06 23:44:16** by **davidlang**:

that would work. It's very common for the gcode to be set to a higher speed when the cutter is not in the work and then be set for a slower speed for cutting. Being able to adust this over a range would be good.



If someone specifies a speed faster than the machine can move, it should just move as fast as it can. It's good to have a setting for the machine to let you specify the max acceleration/deceleration so that you aren't zipping along at max speed and try to turn a corner or start cutting. This should be a knob that's as easy to get at as the one to override the g-code speed.

---

Posted on **2017-03-07 15:18:16** by **Bar**:

Someone in another thread "Question about cutting speed" suggested that the ability to back up a little bit might be useful. I wonder if the speed slider should range from -1x to 5x speed or something similar?

---

Posted on **2017-03-07 17:47:50** by **scottsm**:

The idea of a negative speed for reverse movement is interesting, but we should prevent using it at illogic al times, like at the start of a file...

---

Posted on **2017-03-08 00:45:14** by **jamesbil**:

Could the "stop" button in ground control take the form of an always visible big red STOP, like a road sign? When it stops the program does it lift the router out of the cut as fast as possible? It would need to if a bit breaks.



Another side point, can the z axis motor speed be controlled? 

On the ridgid with the large acme style thread one turn moves it up or down quite a bit, on other routers with, say, an m10 or m12 thread we would need a few revolutions of the shaft to move the same amount as one revolution of the acme thread.. hence the need to increase the speed of the z axis motor.

---

Posted on **2017-03-08 09:51:27** by **Bar**:

All of those changes should be well within whats possible. You can set the speed on the z-axis motor, but it is limited by how fast the motor can turn. I chose to go with a slower motor with more torque over a faster motor that could stall on some heavier routers.

---

