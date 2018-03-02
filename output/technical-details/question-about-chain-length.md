## Question About Chain Lengths Which Disappeared
Posted on **2016-10-26 10:38:10** by **Bar**:

Right before I went to bed last night I saw a question someone posted asking if droop in the chains was an issue. It was an awesome question and it even referenced the relevant lines of code in the firmware! Open source for the win! 



When I woke up this morning I couldn't find it. Maybe I dreamt the whole thing, maybe it's on a different forum, but I want to answer it anyway. If anyone knows what I'm talking about, let me know.



Basically the question was this (if I remember right): Is droop in the chains an issue like this:  [Fig1](../../images/7H/0x/7H0x_file_0fig1.png.jpg). 



The answer is yes and no. Yes, according to the laws of physics, there will be some droop in the chain and we should compensate for it. The no part of the answer is that there are other things I want to compensate for first, because the droop is very small, so I'm going to hijack this question and make it a post about all the math that goes into relating the chain lengths to the position on the board.



The math that relates the actuators to xyz coordinates is called kinematics. There are two types of kinematics, forward an d reverse (or inverse). Basically one equation answers "I know the lengths of the chains, where is the tool?" and the second answers "I know where I want the tool to go, what length do I make the chains?".



For a standard hanging plotter you just make a triangle with the two motors at the corners and the pen a the third corner and do basic trig to find out your position. That works ok, but it misses a LOT of nuance that matters. First, the tool is not actually at the tip of the triangle because the chains don't anchor to the tool, they anchor to the sled. Second, the tension in the two chains is not equal at all times which cause the sled to have a tilt as you move toward the extreme left or right (this is noticeable if you look carefully in the wine rack video). It's important that the two anchor points be away from the tool, because the anchor points being further out makes the sled more stable, but it complicates the math.



If you want to go hardcore nerdy, you can see my whole (but not complete) derivation of the math here: http://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter/10858?noredirect=1#comment19575_10858



And you can see the GitHub branch where I am implementing that system in software here: https://github.com/MaslowCNC/Firmware/tree/kinematics-for-y-axis-compenstion . 



I got a little side tracked with wanting to demo a z-axis because it seems like that is the thing everyone wants to see most, but when I get back to catching bugs, this is the first one I'm after. If someone else wanted to have at it that would be awesome, but if nobody is in the mood, that's ok.

---

Posted on **2016-10-26 13:24:46** by **bdillahu**:

Since several of the accuracy "issues" seem to be around the sled tilting as forces change, would it be feasible to approach this from the other direction... i.e. change the sled.



I understand putting the chain mounts farther out for stability, but instead would you gain anything by making the chains attach very close to the router, but have the sled just extend "under" the chains farther out.



Even have the sled attach twice to each chain (once close to the bit and once farther out).



I expect I don't know what I'm talking about, but wanted to provide the idea.

---

Posted on **2016-10-26 15:18:14** by **rancher**:

How about we design plywood linkage that has the router base as the hinge pin?  Like, two plywood arms with bearings at each end.  One bearing is the chain mount, the other the router base as a pivot.



Disclaimer:  I have no idea what I'm talking about!

---

Posted on **2016-10-26 15:32:36** by **TheRiflesSpiral**:

Bar: "It's important that the two anchor points be away from the tool, because the anchor points being further out makes the sled more stable, but it complicates the math." I think if your anchor points were allowed to slide around eachother with the bit as the axis, this would accomplish both simplifying the math (no need to calculate an offset) and improve the stability because any instability is now centered around the bit, not the crossing point of the chains. This is illustrated in the hanging pen plotter video you posted.



I like the current sled but I think it will probably be one of the first things I go to work on for tweaking.

---

Posted on **2016-10-28 10:52:27** by **TheRiflesSpiral**:

Wow I just noticed the comments on that StackExchange thread got downright testy! Passionate people, I guess... :)

---

Posted on **2016-10-29 14:47:58** by **TheRiflesSpiral**:

For anyone following this thread; look for my Über Sled post; that's where I'll chase this down.

---

Posted on **2016-10-29 22:09:52** by **jgunnr**:

Embed two optical mouse sensors in the sled at opposite sides of the router bit center. Easily get about 0.001" position and rotation (comparing the difference in movement of the two) feedback for every move. The system could ideally learn it's own function for the chains, or at least correct itself on the fly.

---

Posted on **2016-10-30 09:14:36** by **Bar**:

Right!? That sounds amazing, and pretty cheap to test out. I'd worry a little about it working with every type of material, but when it does work you could get incredible resolution. 



A big part of the reason we are open source is to create a platform for you to test things like this. Our code is intentionally really easy to modify. Each aspect of the machine is broken out into an object so if you want to test something like this you can just pull out the encoder block and put in an optical sensor block. You don't need to mess with the PID controller or the motor controllers or the g-code interpretation.



If you go for this, and have any questions along the way, I'd love to help.

---

Posted on **2016-10-30 11:56:43** by **jgunnr**:

Yeah there would definitely be materials that would be problematic like opaque acrylic (but most wood should work great) . That's why ideally it would re-learn the functions periodically by running a calibration routine on the backing board alone. This would alleviate changes over time like chain stretch, router/weight changes, etc. Huge plus would be just knowing the exact position of the endmill by the midpoint of the two sensors for near real-time feedback. 



Guess I should've backed the beta instead of the standard reward to try this out earlier  :)

---

Posted on **2016-10-30 15:11:19** by **jgunnr**:

Just realized you were talking about replacing the encoder block... think this would probably just be something to augment it. I was thinking it would be feedback for error-correction and calibration with the encoders still driving motor movement (so they still function similar to stepper motors). Haven't looked at the code yet but hopefully it wouldn't be too hard to add in that way.

---

Posted on **2016-10-30 15:48:36** by **larry357**:

for the tilt solution, how about using two retractable dog leashes from the bottom two corners up to the sled? or something similar?

---

Posted on **2016-10-31 05:14:02** by **electronrancher**:

@jgunnr:  Based on some previous experimentation with mouse sensors, the sled will vibrate too much for them to capture the proper movement data.  Their refresh rate will alias the 10-30kHz of the router and the output will be chopped jitter so the motion engine will have a hard time giving delta x and y.



@Bar awesome description, and thanks for the links to your stack and mathworks derivations!

---

Posted on **2016-10-31 20:58:40** by **jgunnr**:

@electronrancher bummer for real time feedback, but still wouldn't preclude using it in the optimal scenario as calibration or function learning. The router wouldn't be on. For various places in the x/y plane, run a sequence of expected vs. measured gcode movements with the router bit retracted. Tweak functional parameters that ultimately drive the motors/encoders based on the feedback. Repeat until within a desired tolerance. The system would then be better calibrated to run some actual cutting paths without the mouse sensors.

---

Posted on **2016-11-01 05:15:26** by **asleborgen**:

How about putting in a sharpie (or similar) instead of the router bit and drawing a 50*50mm square grid over the entire work surface?

 This should give quite clear (and measurable) feedback. This could in turn be put into a sort of "calibration table" in the software.



Disclaimer: I know a thing or 12 about measuring, but i am a COMPLETE IDIOT when it comes to software, so this might not be as simple in real life as it is in my mind...

---

Posted on **2016-11-01 10:04:11** by **scottsm**:

I've been thinking that using a Sharpie to 'preflight' cuts in expensive material might be a good idea.

---

Posted on **2016-11-02 11:24:04** by **TheRiflesSpiral**:

I love this idea... how cool would it be to have something that slips into the router base that holds a spring-loaded sharpie or contractors pecil?

---

Posted on **2016-11-02 12:35:00** by **scottsm**:

Aaaaand we're back to the hanging pen-plotter!

---

Posted on **2016-11-02 14:06:03** by **TheRiflesSpiral**:

LOL that was fast. ;)

---

Posted on **2016-11-02 18:14:02** by **jwboyce**:

I was thinking a stain pen might be fun.

---

Posted on **2016-11-03 01:46:28** by **asleborgen**:

Boy that escalated quickly! 

Anywhoo: Since software is free, shouldn`t it be possible (and easier) to make a correction table in sw, rather than making one off solutions for every router and sled?

---

Posted on **2016-11-03 06:52:49** by **rancher**:

Regarding software calibration/correction, perhaps there is something to the idea of a simple method of drawing a registration file on a sheet of paper, then scanning that and using software to calculate and calibrate.  Seems cheaper than sensors and constant feedback, but, I have no idea.  It also will probably only be necessary for a fraction of users, judging by Bar's demonstrations.  It looks like it's already good enough for my sloppy work.

---

Posted on **2016-11-03 12:32:02** by **Bar**:

I'm certainly pursuing an all software approach, but I'd love to see all the cool hardware modifications that are being discussed. Sometimes those cool "hmmm I wonder what happens if I do _____" projects end up being fantastic.



I really like the idea of using a piece of printed paper as a reference for calibrating. I just use a tape measure, but we could even include a couple pieces of paper in the box for calibration. Something like glue one of these in the bottom left and top right corners of your bed and move the machine to the x at the center...press a button...move to the next...press a button. You could get very precise calibration with minimal effort. Great suggestion :-)!

---

