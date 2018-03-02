## Some thoughts on the firmware
Posted on **2017-05-26 22:00:01** by **seware74**:

I won't pretend to know much about kinematics and the math going on in the firmware. But I do have professional background in writing embedded code (albeit a few years back now). After perusing the source for several hours today, I came to the conclusion that it is going to be difficult to ensure meeting of the target design specs under dynamic circumstance, if the system is not deterministic. I will readily admit I don't know much about the Arduino, but I read enough to know that it will be difficult to keep the different tasks that this firmware is doing, smoothly cooperating, with nothing but loop(), delay() and millis() as your toolset. Don't hate on this suggestion; it's based on my idealistic nature and a desire to see this project succeed. 



I seriously think that the Maslow firmware needs to be running on an RTOS in order to separate the lighter weight and less important tasks from those that are critical and heavy duty, in a way that will make them behave predictably and consistently. 



Something like FreeRTOS appears to be robust, lightweight and available for  the Mega. I did not do any analysis to see what limitations that this particular RTOS might impose on Maslow; I only noted that it was available for this hardware. 



Scheduling and prioritizing tasks is key to any embedded system that is doing multiple tasks, not to mention protection of shared resources (motors control, UART, memory regions).  It would be a bit of effort to implement, but if there is a suitable RTOS for this hardware, I think it would significantly benefit the firmware. I might even be inclined to port it, if nobody can convince me that this would be a misstep.



I welcome your thoughts.

---

Posted on **2017-05-26 23:08:46** by **scottsm**:

It's certainly not a misstep, this is just the reason for a project like this to be open source! 

That said, I've seen an estimate that the present setup accomplishes calculations at around 6kHz, updating the motors at this rate.

It looks like the FreeRTOS is limited to a minimum of 15ms for a task time slot due to an Arduino limitation. Isn't there a mismatch in time scales there? 

Because my background is hardware, I've been tempted to try porting to a different hardware platform :) . That's on a back burner for now, though, as I've been enjoying the progress happening with the present platform.

---

Posted on **2017-05-26 23:17:47** by **scottsm**:

There is a very mature CNC software project, [grbl](https://github.com/grbl/grbl), that has become a standard. There has been some discussion here about forking that and adapting the Maslow motor driving and kinematic code to that. Your embedded experience might be very helpful in evaluating that path.

---

Posted on **2017-05-27 01:23:53** by **davidlang**:

I expect that adding any OS between the existing logic and the hardware will slow things down. Everything right now is Interrupt/timer driven so it's not quite as bad as you are thinking.

---

Posted on **2017-05-27 06:37:00** by **seware74**:

Admittedly my thoughts are based in assumption and observation, not system analysis. I may pick up hardware or find a simulator on my own and do some  testing.  My point is not that performance is bad. On the contrary nothing is faster than running on bare metal.  But issues like chattering and not completing instructions point me toward a solution that allows each task to run independently, coordinating when necessary. Perhaps of more importance is protecting access to the motor driver using mutexes. 

Sure an RTOS adds overhead and FreeRTOS may not suitable... it was merely the first one I came across that was familiar with and was accessible for arduino

As for testing different hardware... Yes, something with SIMD instructions would be fantastic for matrix operations.  But that does begin to push on Bar's desire to keep it cheap. In beta stage I always prefer to try to solve in better software than throw hardware at it. Like pilots often say,  "I would rather fl y on the wing  than fly on the prop."

Btw, I don't think our suggestions do much for accuracy... mostly speed and predictable behavior.

Enjoy the memorial day weekend!

---

Posted on **2017-05-27 10:11:35** by **davidlang**:

ahh, the chattering is mostly caused b other problems.



It's only last week that we split the single motor control loop from a single PID loop to a location PID loop and a speed PID loop. Such loops need to be tuned to be stable, and when they aren't tuned, they cause chatter. Per Bar's post, the speed PID loop is really a PI loop, the speed signal needs some filtering (in software) to make it able to be used.



We have another problem in that we don't currently implement acceleration planning, it just goes from stop to full speed as fast as it can (and stops similarly, which will cause overshoot), and when combined with gcode that has lots of short line segments, it was not processing the gcode fast enough and jerking a lot, which resulted in problems similar to the PID loop chatter.



We know this is software, not hardware. The talk about going to faster hardware was in part driven by my miscalculation as to the distance ahead that the firmware could plan before it ran out of cpu (I slipped a decimal or something and thought that at 48 ipm it was planning every 3mm), sin ce the planning is _very_ calculation extensive, a faster board would help there. But with it now exceeding 6KHz, it's now fast enough (and improving).

---

