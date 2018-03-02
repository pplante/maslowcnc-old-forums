## limit and panic switches
Posted on *2017-03-08 23:27:34* by *jbarchuk*

> @Bar
> There are six digital IO pins accessable in the beta version of the control board. Based on community feedback, I am making the next version of the control PCB have 4 digital IO pins and 2 analog/digital IO pins available.

Excellent. I'd like one digital line dedicated to an array of limit and panic switches. The software's task when the pin is activated is to shut off all motors and then do nothing except wait to be told what to do.

There also needs to be a test mode in a maintenance menu that signals 'OK' when a switch is closed. For safety-maintenance it'd be smart to once a week run through all switches to make sure they're working properly.

I find it hard to believe that limit switches weren't added on day one. I recall mention that 'software would prevent out of work area travel.' Well, as witnessed by that broken motor arm that didn't work right. The comment after that was 'more software' or something similar.

Software fails. That's a fact. Or it crashes or gets stuck in a loop, and hardware is left in an unknown state such as a motors running.

When  software fails the next best backup is hardware activated by an outside source such as a panic or limit switch. The system needs to be used only once a year to be fabulously valuable.

---

Posted on *2017-03-09 04:24:51* by *davidlang*

defining 'out of area' with switches is going to be non-trivial, a length on one side can be 'in area' or 'out of area' depending on the length on the other side. It's also hard to set a switch to fire when a chain uses up most, but not all of it's available slack.

e-stop is good, but cutting all power is probably the easiest way to do that.

---

Posted on *2017-03-09 09:52:27* by *Bar*

I agree that having a software e-stop is ideal, and I agree that cutting the power is the best option to be sure everything stops.

@david lang is correct that it's hard to define limit switches because what's out of bounds in one place might not be in another. The software limits to keep the machine in bounds were added after the broken motor mount and haven't let us down yet, but like you said, software fails so I'm sure it will someday.

I like the idea of dedicating Aux port #1 to being a switch (or series of switches) which will stop the machine if tripped. The machine could then wait until you send it an "all clear" signal.

---

Posted on *2017-03-09 13:11:16* by *jbarchuk*

> @davidlang
> defining ‘out of area’ with switches is going to be non-trivial...
After thinking more I get it now. Limit switches are AAMOF nearly useless without the math to keep track of where out of bounds is for each chain relative to the other. The software is already there. It should be a priority for testing, maintenance and review. Panic switch will always be necessary and easy.

---

Posted on *2017-03-09 13:27:49* by *jbarchuk*

> @Bar
> I agree that having a software e-stop is ideal, and I agree that cutting the power is the best option to be sure everything stops.

Cutting all power would be ideal but as you've said it's not designed into the machine. It -would- be a trivial mod to add a relay box, that the user doesn't have to do anything more technical than connecting a cable and plugging in the mains wires.

I'd rather see power to the control board stay on for data analysis. This will be an extreeemely rare problem, but any problem that costs someone a 6hr cut and an expensive piece of material, to that person the fix is priceless.

A memory dump utility would help a LOT towards troubleshooting such a rare failure. It's really hard to find the cause that's supposed to never be allowed to happen. Every little speckle of clue helps.

>The software limits to keep the machine in bounds were added after the broken motor mount and haven't let us down yet, but like you said, software fails so I'm sure it will someday.

Has the cause of that failure been identified and fixed?

---

Posted on *2017-03-09 16:20:25* by *davidlang*

The problem with an e-stop tied into the arduino is that the router will keep spinning (since there is no motor control)

something like this https://www.amazon.com/Rockler-Safety-Power-Tool-Switch/dp/B001DT13B2/ref=sr_1_77?ie=UTF8&qid=1489105128&sr=8-77&keywords=emergency+stop+switch that both the router and the power supplies for the motor get plugged into would be a far safer thing.

---

Posted on *2017-03-09 16:43:31* by *mooselake*

Panic type limit switches seems pretty straightforwards, as long as there's at least a bit of slop at the upper cutting limits (and since you can't get the chains horizontal there should be).  Hit a switch on either the left or right side, outside the normal travel limits, and you're out of it.  By that point the motors won't turn any further so you're in trouble anyway.  Poll or use interrupts, whichever fits the firmware best.

You might consider having home switches (perhaps doubling as limit switches), one in each upper corner that determine where the two top corners are.  I have no idea if the firmware keeps both absolute machine position and relative (workspace) coordinates, but if it does then software limits are easy.  Plus if you lose power when cutting it becomes comparatively easy to rehome, edit the gcode as needed, and pick up again.

Of course, if you're already homing, forget I said any of this.

A router relay control SSR only takes one pin, and not a lot of gcode support. and is pretty handy for non-emergency situations.  From a little googling universal  motors, like the ones in routers, will dynamically brake (stop spinning faster) if you short the two power wires.  If they really do (never tried it...) that should be part of the emergency shutdown relay (one side to power, the other to shorted, so you don't short the mains of course and between the SSR and motor).

---

Posted on *2017-03-09 16:52:15* by *davidlang*

what you are missing is that the problem isn't hitting the upper limits (the chains retracting too much), the problem is hitting the lower and side limits (the chains being let out too far). If you are cutting the bottom left corner, the left chain cannot be any longer than about ~4.5 ft and the right chain cannot be any longer than ~10 ft, but if you are cutting the bottom right corner, the left side will need to be ~10 ft and the right side ~4.5 ft.

so what length of chain should you have trip your limit sensors?

---

Posted on *2017-03-10 12:15:04* by *mooselake*

When you know where you are then detecting that you've hit the limits isn't a problem, and once you know where the minimum retraction ("home") points on both sides are - assuming your geometry is configured right - then software limits will handle it.  The use of DC motors with encoders makes it a lot less likely that you'll lose position then lost steps with stepper motors.

If you still want to know when you go past a limit then push bars with switches (think conduit screwed at one end, with a spring and stop at the other side) could do it, but that'll only happen if the firmware has a bug, and they'll be an in-the-way nuisance.

---

Posted on *2017-03-10 16:14:11* by *davidlang*

@mooslake, the first half of your pose boils down to enforcing the limits in software, which is what the OP was wanting to avoid doing.

---

Posted on *2017-03-10 23:38:40* by *jbarchuk*

To clarify, not to 'avoid... software limits....' but to add another level of safety net that is a little more independent of the main driver software.

---

Posted on *2017-03-13 10:09:32* by *mooselake*

Wooden frame with clearance to slide plywood underneath that will make the router stop - the power isn't software controllable so that's as much stopping as you need.  Or pivoting stops, the conduit swinging on one end option.  Both in the way...  Or determine what the maximum chain tension can be during normal operation and add a spring controlled (spring pushing a pulley against the chain) switch that'll open (NC is a safety feature) if that tension is exceeded.

The real hazard here is the spinning router, and there's currently no way to turn it off in software.  By the time you loose position and whack into a hard limit your workpiece is ruined, and as long as you practice basic safety by keeping body parts out of the potential cutting area you're not going to get hurt.  It the router turns into a flying object and is thrown across the room with the bit spinning (not suggesting that's a likely possibility) then limit switches aren't going to make much difference.  There's a lot of smallish CNC routers that have home but no limit switches.  There just doesn't seem to  be enough power behind this machine to do a lot of damage to the machine or user (assuming common sense safety) if it gets confused and lost.  Can those chains hurt you if you get your finger stuck in a pulley?  Can they pull hard enough to do any damage?  Sure, the router can, but can the mechanics?   Not like it's tons of cast iron whipping back and forth at high speeds.  Doesn't seem like hardware limit switches are much of a priority, but fast-shutdown e-stop switches are.  Of course this isn't politics, so your opinion is just as valid as mine.

---

Posted on *2017-03-13 10:14:37* by *Bar*

Something to throw into the conversation is that the controller is powered separately than the motors (by design) so if you were to add one of those in power cord e-stop buttons which cuts power to both the motors and the router you could stop the machine immediately and turn off the router without cashing the firmware, meaning you could still resume your cut.

---

Posted on *2017-03-13 14:10:50* by *mooselake*

Wouldn't you loose your position if you did that?  The firmware wouldn't know if the motors had moved after loosing the encoder pulses.

Does the back EMF from dropping the motor power harm the controller, like it can with steppers?

Although you could recover by retracting the Z, rehoming, repositioning, and starting over.  It's a bit fuzzy, but I seem to recall that LinuxCNC would do this by saving the current position before a power loss.

---

