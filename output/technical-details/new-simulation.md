## New Simulation
Posted on **2017-07-13 18:42:18** by **Bar**:

Hey Everyone!



I wrote a simulation of how errors in the measurements produced by the calibration process will affect the final cut to help keep refining the calibration system.



It looks like this when you run it [Simulation](/images/En/sj/Ensj_simulation.jpg.jpg) 



Shown in green are the how a grid would cut using the correct kinematics, and shown in red are how it would cut with the error introduced using the sliders on the right hand side.



You can check it out by running the file "simulation.py" in the simulation folder of Ground Control if you are running Ground Control from the source.



So far the most interesting thing I've learned is that if the error in the measured distance between the motors is identical to the error in the measured distance between the sled mounting points, they nearly cancel each-other out which I wouldn't have expected.



Give it a spin and let's all see what we can learn! :-)

---

Posted on **2017-07-13 18:43:15** by **Bar**:

Oh, and big bonus points to anyone who can make it so the simulation launches in the center of the screen. I couldn't get that to play nice, so you've got to drag it into the middle every time :-/

---

Posted on **2017-07-13 19:13:56** by **rollandelliott**:

looks pretty cool.

---

Posted on **2017-07-13 20:51:56** by **davidlang**:

I'm pretty sure the position error is the result of 0,0 being in the middle of the grid, but in the bottom left of the canvas. I believe that you would need to offset all your plots to make it centered (and take the scale factor into account to keep it in place as you zoom)

---

Posted on **2017-07-13 21:12:35** by **davidlang**:

trying to set the chain mounts to the 3/9 oclock positions (i.e. the router directly in line with them) results in divide by zero errors

---

Posted on **2017-07-13 22:14:41** by **scottsm**:

This is a great tool! It really points out the importance of accurately measuring the distance between motors and between sled attachments. I'll be taking a very close look at these measurements on my setup!

---

Posted on **2017-07-13 22:36:30** by **davidlang**:

ideally the machine parameters should be pulled out of the kinematics routine and made into top-level variables (so that they can be displayed, and experimented with for those wanting non-standard machine sizes)

---

Posted on **2017-07-13 22:51:42** by **scottsm**:

I think the parameters you're talking about are all available for configuring in the 'Settings' panel.

---

Posted on **2017-07-13 23:28:53** by **scottsm**:

Sorry, I just realized that you’re talking about the simulation and I’m in GroundControl.

---

Posted on **2017-07-13 23:41:11** by **davidlang**:

I've got a pull request submitted that adds a CG slider (as well as a few other tweaks), and one interesting thing is that if the CG setting is off, it only affects the outer edges, but gets substantially worse as you go down the sheet, so the bottom corners can be off quite a bit from a bad CG number.

---

Posted on **2017-07-13 23:45:45** by **davidlang**:

also, a 2mm error in the bit to chain mount position can result in an error of over 1mm in the X direction in the bottom corners. We have been adjusting the distance between the chains to account for the horizontal error between where the chain mounts are and where the chains actually pivot, but we have not touched the vertical error.



This simulation is showing that the machine is extremely sensitive to these errors, I'm going to cut some bolts with holes in them so that the chain has a solid, stable place to pivot on, it looks to me like the slop of the pivoting point is going to cause enough error to be noticeable.

---

Posted on **2017-07-14 02:50:55** by **davidlang**:

I'm getting occasional errors like the one below. I can reproduce it with the exact same slider options, but shifting the slider just slightly can change were in the point array the error happens



I'm guessing that             Clock.schedule_once(self.plotNextPoint)

 in simulationCanvas.py is causing this in that not all the points are getting plotted fast enough. but I'm not sure how to fix it.

---

   File "simulation.py", line 37, in <module>

     SimulationApp().run()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/app.py", line 828, in run

     runTouchApp()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/base.py", line 487, in runTouchApp

     EventLoop.window.mainloop()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/core/window/windo w_pygame.py", line 403, in mainloop

     self._mainloop()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/core/window/windo w_pygame.py", line 290, in _mainloop

     EventLoop.idle()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/base.py", line 327, in idle

     Clock.t ick()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/clock.py", line 515, in tick

     self._process_events()

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/clock.py", line 647, in _process_events

     event.tick(self._last_tick, remove)

   File "/home/dlang/.local/lib/python2.7/site-packages/kivy/clock.py", line 406, in tick

     ret = callback(self._dt)

   File "/home/dlang/arduino/arduino-1.8.1/cnc/maslow/GroundControl/Simulation /simulationCanvas.py", line 101, in plotNextPoint

     pointPlotted, distortedPoint = self.testPointGenerator.plotPoint(xValue, yValue)

   File "/home/dlang/arduino/arduino-1.8.1/cnc/maslow/GroundControl/Simulation /testPoint.py", line 39, in plotPoint

     correctPosX, correctPosY = self.correctKinematics.forward(chainALength, chainBLength)

   File "/home/dlang/arduino/arduino-1.8.1/cnc/maslow/GroundControl/Simulation /kinematics.py", line 285, in forward

     guessLengthA, guessLengthB = self.inverse(xGuess, yGuess)

 TypeError: 'NoneType' object is not iterable

---

---

Posted on **2017-07-14 04:59:19** by **gero**:

Any value for Motor-spacing from -38 till -50 lets the simulation crash with  TypeError: 'NoneType' object is not iterable

---

Posted on **2017-07-14 05:04:47** by **gero**:

Same for a positive value of 50 in Vert dist to bit. 49mm plots, while 50mm crashes the simulation.

---

Posted on **2017-07-14 05:12:04** by **gero**:

Certain combination of extreme values crash the simulation. Example: 

Motor-spacing -37, Motor Vertical 50, Sled Mount -50, Vert dist to bit 49

---

Posted on **2017-07-14 05:13:59** by **gero**:

I love the simulation though :-). Great thanks. Gives some valuable insight on where to tweak.

---

Posted on **2017-07-14 08:07:02** by **davidlang**:

I'm wondering if the 'nonetype' errors are due to it not finding it's position with enough accuracy.



the accuracy seems to vary from run to run. I had one run where just the back and forth through the ideal machine generated a 5mm error at one spot.

---

Posted on **2017-07-14 08:43:30** by **TheRiflesSpiral**:

> @davidlang

> the accuracy seems to vary from run to run



That's... weird. Is there some kind of randomization in the sim's calcs of real-world variables?

---

Posted on **2017-07-14 09:04:24** by **Bar**:

There shouldn't be any variation run to run :-/, the simulation is very beta at this point so let's take it's results with a grain of salt until we can fully verify that it is working correctly

---

Posted on **2017-07-14 10:43:20** by **davidlang**:

it may be varying based on the grid size (on of the commits in the PR I submitted allows this to be variable), it seems that the errors are much higher with larger distances between the points. The 5mm error was with a point every 300mm

---

Posted on **2017-07-15 15:23:19** by **davidlang**:

one thing this simulation is showing me is that errors in any machine dimension translate very strongly into errors in the position, so even a couple mm of flex in the arms (or warping the plywood of the frame) will translate into position errors (at least half the machine dimension errors)



so I'm thinking that having a solid piece of wood betwen the motors is a big improvement for the real-world accuracy.



I am thinking that I will eliminate the rectangular plywood motor mounts entirely and just get a piece of 2x6 or 2x8 (depending on sled balance) material and mount it across the arms.



I'm even considering splurging and getting a piece of LVL engineered lumber for this as it is more rigid.



The other option is laminating plywood, but since this would need to be ~10' long, it would end up pieced together, and I'm not as comfortable with that, so I may just spring for the LVL if I decide not to go with a simple 2x.



If I build a 'wall type' rectangular frame, a 2x10 or 2x12 on top of 2x4 studs would be about right

---

Posted on **2017-07-15 17:51:37** by **cameronswartzell**:

@david Constructed my wall type frame today, though thats as far as I got. Hope to have it all running by the end of Monday, I am currently awaiting some added chain as I suspect 10' wont do me. My frame is 12'x6'6", leaving 10" at the bottom for the sled to travel far enough for the bit go all the way down, and placing the motors 18" above the top of the cutting area, 24" out on either side. This is somewhat wider than the recomendation, but not by much. I couldnt stomach a 14' wide frame and balked cutting it back. Will likely have to roll it on its end and store it vertically when not in use 



The motors will be mounted just directly to the top horizontal framing member so are pulling against one another on a single solid piece. May add some 3/8" gussets to the rear of the frame in the corners to keep it square.

---

Posted on **2017-07-15 18:12:17** by **davidlang**:

the stock frame is just a little under 10' wide, so you have gone a good bit wider, which should help you.

---

Posted on **2017-07-16 04:10:05** by **davidlang**:

I've updated my pull request, 7 commits now



`	modify display routines to plot in the window ￼		d91d821`

`	output details to the console 		796f157`

`	Improve output by showing orig target 		3876819`

`	add CG slider 		79751ec`

`	add machine details to the output 		69dc1fa`

`	make the grid size dynamic 		b7f6479`

`	2x speedup and center grid (and clean trailing whitespace) 		c083326`



In doing more digging into things, I'm seeing a couple different errors crop up



I'm running into divide by zero errors where self.Jac[] is zero



I'm also running into the NoneType error, I can sometimes eliminate that error by increasing the number of iterations that kinemetics does before giving up, so there is some codepath in there that is not returning a value, I've run into this now in a couple different routines, but have not been able to track it down

---

Posted on **2017-07-16 04:53:57** by **davidlang**:

I think I found the problem that was causing the NoneType errors, python's significant whitespace strikes again :-)



in kinematics.py the while loop included things that it should not have because it was indented too far. see commit 	0133f3a for details.

---

Posted on **2017-07-16 07:07:55** by **davidlang**:

I've identified that there is one other error, when X=0 the chains are not equal length.



I haven't found the cause if this yet.

---

Posted on **2017-07-16 08:19:03** by **davidlang**:

it turns out this is much more of a problem when the bit is near the line between the chains, something is off in the math, but I can't tell what right now (as s and h3 get small, the current calculations break)

---

