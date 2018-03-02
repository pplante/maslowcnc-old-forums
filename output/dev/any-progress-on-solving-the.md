## any progress on solving the chattering?
Posted on **2017-05-25 10:40:52** by **davidlang**:

While Bar was busy traveling in the last week, we had some people trying the new double-pid firmware and reporting that when the Z axis was moving (and the machine should have otherwise been still), the motors were moving around a bit.



Has anyone had success in tweaking the PID loops to stabilize it?



Does this solve the inaccuracies we were seeing in Y positioning?

---

Posted on **2017-05-25 10:43:55** by **blsteinhauer88**:

Im am about to run a cut on the new update release.  I have not done any thing else so far so we will see if something is fixed.  I did notice it was more smooth during a motor calibration with no chattering.

---

Posted on **2017-05-25 10:45:36** by **davidlang**:

motor calibration should no longer be needed (there is an update today that rips that code out as no longer needed)

---

Posted on **2017-05-25 10:51:33** by **blsteinhauer88**:

Thanks, well just moving the sled to "home" along horizontal center, the Z motor is chattering...

---

Posted on **2017-05-25 10:55:02** by **blsteinhauer88**:

Z at 0, sled moving, no chatter on z motor.  Z retracted in Home movement, sled moving, there is chattering in the motor until it returns to 0

---

Posted on **2017-05-25 11:11:01** by **blsteinhauer88**:

Still some chattering on motors during a z adjustment.  will have to learn how to play with the PID adjust.

---

Posted on **2017-05-25 11:32:45** by **blsteinhauer88**:

It is now processing so fast that when I pressed hold, it stopped the line number int he code, but the machine still performed several movements and z adjustments before it caught up to the place I told it to hold.  This was after a bit break because it did not retract the bit to move to the next cut.

---

Posted on **2017-05-25 11:40:54** by **blsteinhauer88**:

It also is SKIPPING CODE!  Will post a photo in a minute.

---

Posted on **2017-05-25 11:43:46** by **Bar**:

Chattering and the delay between hold and the machine pausing are both issues on my list. Skipping code is new to me and sounds like a top priority issue.



Reducing the step size for yesterday's version should help the chattering somewhat, but the PID still needs to be tuned. 



If we want to get technical I think that the issue comes from Kd being 0 for the speed control. Kd is zero because the speed measurements are pretty noisy so we need to add some software filtering before the signal is going to be clean enough to use with derivative feedback.



The delay between when we press the hold button and when the machine stops is because the machine now has multiple lines of gcode in it's internal buffer. Pressing hold stops sending code to the machine, but it will still run what it has in buffer. That used to be just the line it was already running, which wasn't so bad. We may want to implement a hold feature in firmware that pauses the machine immediately.

---

Posted on **2017-05-25 11:46:23** by **Bar**:

Stop will still halt the machine immediately

---

Posted on **2017-05-25 11:56:53** by **blsteinhauer88**:

http://www.youtube.com/watch?v=oeWjRDynUso

---

Posted on **2017-05-25 12:01:41** by **blsteinhauer88**:

broke bit too :(

---

Posted on **2017-05-25 12:02:14** by **Bar**:

:( Very strange! It seems like you are absolutely correct that it skipped that  last area. Do you have the file that it was running so I can try to duplicate the issue?



Was the chattering still happening?

---

Posted on **2017-05-25 12:06:13** by **blsteinhauer88**:

Yes it was, I will attach the file, it happened near as I can tell at about 850 are to 925 line code.  it has success fully cut once, but ramped a couple of the movements.  It was not fully Z retracted and started its movement.  https://www.dropbox.com/s/1669epchl10jsbx/sun%20moon%20stars%20.5ply%20.125bit.nc?dl=0

---

Posted on **2017-05-25 12:07:50** by **blsteinhauer88**:

[IMG_9136](//muut.com/u/maslowcnc/s3/:maslowcnc:3NC2:img_9136.jpg.jpg)

---

Posted on **2017-05-25 12:10:57** by **Bar**:

Ok, I will try to duplicate the issue. The z-axis ramping issue is one that I had hoped we solved, I hadn't seen it in a little while so good to know that is still a thing.



Beautiful design, sorry for the issue.

---

Posted on **2017-05-25 12:11:13** by **Bar**:

*issues :-(

---

Posted on **2017-05-25 12:18:13** by **blsteinhauer88**:

It's all part of making it great!

---

Posted on **2017-05-25 15:06:31** by **Bar**:

This is a great file to test on. I haven't been seeing anything near the level of chattering that this file produces on other files. This should help me track down what's happening. Thank you for passing it along.

---

Posted on **2017-05-25 15:21:23** by **Bar**:

I think the issue has to do with the fact that this file uses only the G1 command so that curves are made up of many very small line segments which aren't being run smoothly. Instead there is a slight pause between the execution of each line which is causing the motors to move jerkily. 



The fact that there are so many line segments is also causing the self calibration process to behave strangely. 



Why this is affecting the z-axis is a mystery to me, because that should be a separate system.



We may need to add path planning and look-ahead to to get this to be truly smooth. We can start by making lines process faster, and look into why the PID loops are acting so weird.

---

Posted on **2017-05-25 15:58:29** by **blsteinhauer88**:

Sure

---

Posted on **2017-05-25 16:34:30** by **davidlang**:

@bar, I'll repeat the suggestion I made earlier about trying to transplant the motor control to run inside the grbl framework. They have extensive work on supporting a lot of g-code and a sophisticated planner that has acceleration limits, and can carry speed over from one line segment to the next, depending on the angle of the two segments.

---

Posted on **2017-05-25 16:38:35** by **davidlang**:

note grbl is GPL3+ so we can freely borrow code/fork it as needed.

---

Posted on **2017-05-25 16:43:20** by **Bar**:

I think that's a great idea that I wish I had done more of from the beginning. The biggest drawback to Grbl is pretty chip specific (lots of addressing registers directly) if I remember right. Can you even compile your own version of Grbl with the Arduino IDE? I vaguely remember it relying on some closed compiler.



Neither of those things would prevent us from using their path planning and gcode reading code.

---

Posted on **2017-05-25 17:10:42** by **davidlang**:

apparently you can now.

https://github.com/gnea/grbl/wiki/Compiling-Grbl

---

Posted on **2017-05-25 17:17:45** by **Bar**:

Very cool! If you ever want to pull any of their code into the firmware that's always welcome. I'm going to be looking at speeding up line execution this week and I'll spend some time seeing how they do it.

---

Posted on **2017-05-25 17:21:53** by **davidlang**:

I I did some digging on this topic a little while ago, and I ended up deciding that it would be easier to implement maslow movement inside grbl than to try and move the gcode processing and planning the other way. see the topic implement maslow kinematics in grbl?



The chip specific things will only matter if/when we try to move off of the standard arduino boards to something significantly faster

---

Posted on **2017-05-25 17:46:01** by **blsteinhauer88**:

This code was rendered in easel.

---

Posted on **2017-05-26 13:49:59** by **blsteinhauer88**:

Any Luck with the file? Did you get it to cut?

---

Posted on **2017-05-26 14:35:33** by **Bar**:

Yep! I'm merging in the changes I made to fix the problem and uploading the video now.

---

Posted on **2017-05-26 14:37:40** by **Bar**:

Here's the picture of mine  [sun moon stars cut](//muut.com/u/maslowcnc/s3/:maslowcnc:Vrym:screenshot_20170526143611.png.jpg)

---

Posted on **2017-05-26 14:50:13** by **Bar**:

Alright, I believe that the latest firmware and GC should take care of the chattering. 



There were a two issues 1) when dealing with files like those in which arcs are made up of many small lines the firmware wasn't processing the lines quickly enough (or really it wasn't requesting the next line early enough). 2) The motors weren't dis-engaging when they aren't needed



The result of fixing both those things is that we can cut faster and smoother. Here's a video of part of my test cut of that file: https://www.youtube.com/watch?v=FE2s2nwuZ3g



Sorry about the video quality, it was shot on my phone.

---

Posted on **2017-05-26 18:08:16** by **Bar**:

Did the new firmware/software combo solve the issue for you @blsteinhauer88?

---

Posted on **2017-05-28 20:51:10** by **blsteinhauer88**:

Bar?  Did you look outside?&quest;  Ha Ha, Grandkids in the pool last couple days..I will try it tonight or tomorrow.  For the rest of you, We have been Greyscale about since last October, We had a couple sunny days in April, Now we have been in the upper 80's and Low 90's.   Yahoo!

---

Posted on **2017-05-28 21:26:30** by **Bar**:

I know! It's way too nice out to be inside.



No rush, aslong as you aren't waiting on me :)

---

Posted on **2017-05-29 03:46:09** by **gero**:

@blsteinhauer88

I love the opposites :-) Here it climes to a spring 40C/104F. We will not see a cloud again until November. It is the holy month of Ramadan, so no cigarette, no eating or drinking outside from sunrise to sundown. No way you will find me outside until October! The air-conditioned Maslow-Room is the place to be, if it's not the office or the car.

---

Posted on **2017-05-29 13:25:19** by **blsteinhauer88**:

Lol, and I try to stay outside and eat and drink, cook outside. What differences in culture, and Bar brought us all together chipping wood!

---

Posted on **2017-05-29 13:49:11** by **rancher**:

Right there with you B.



 [IMG_4134s](//muut.com/u/maslowcnc/s3/:maslowcnc:ReZT:img_4134s.jpg.jpg)



 [IMG_4140s](//muut.com/u/maslowcnc/s3/:maslowcnc:KNa8:img_4140s.jpg.jpg)

---

Posted on **2017-05-29 14:00:00** by **scottsm**:

That's an interesting grill...

---

Posted on **2017-05-29 15:12:32** by **rancher**:

CNC'd wood burning power head for various applications.  Ergo Maslow.

---

Posted on **2017-05-29 15:35:20** by **scottsm**:

Is that the fire box in the base? Do you smoke with it as well as grilling?

---

Posted on **2017-05-29 15:50:29** by **rancher**:

Yes and yes.  You can see the fuel and fire in those photos.



Smoking requires a different configuration, and believe me, I have a few of them!

---

