## Question about Accuracy / Reproducibility
Posted on **2016-10-17 16:48:14** by **paulhart**:

Hi!

The Maslow is a great idea, I'm looking forward to supporting it on KickStarter very soon! As mentioned in the title, a couple of questions related to accuracy (as came up in the HN discussion)...

The demo video shows you cutting a relatively small logo out of a 4x8 sheet; what happens to the accuracy of the router position as you tend towards the edges of the sheet? Also, given two separate cuts on different sheets, how do they compare?

If it's still "too soon" to discuss that, I understand, but I feel like a lot of KS prospects will be more likely to back the project if there's a sense that it's going to be more than a toy.

I've seen some videos of hanging pen plotters that work very well when near the bottom of their work area, but are kind of terrible at the top. There was a huge amount of slop in those designs, and it looks like the weighting you've added to your design should mitigate a lot of those issues, but I'm still curious.

A video showing a s eries of concentric rectangles being cut out of the sheet would be awesome for showing how things may be.

Thanks,

Paul

---

Posted on **2016-10-18 08:06:58** by **nathanmiller**:

I was curious about the accuracy at the corners of the sheet too. I expect it to be ok of the controlling servos are far enough away from the panel being cut.

---

Posted on **2016-10-19 13:06:47** by **Bar**:

That is a series of excellent questions. You clearly have a solid understanding of what to ask about. 

I'm going to try to answer them in order, but first here is a video I made yesterday that addresses our most asked technical questions which you might think is interesting: https://www.youtube.com/watch?v=pzCtc_V7rzs . 

*"What happens to the accuracy of the router position as you tend towards the edges of the sheet?"* Basically it stays the same. I'm not 100% pleased with the performance within about 2 inches of the bottom left and right corners of the sheet, but that's probably just me being picky. 

*"Also, given two separate cuts on different sheets, how do they compare?"* In theory they should be identical. The machine stores it's location in its eeprom (non-volatile memory) when it finishes cutting, so if you power it off and come back in a couple days it will remember where it is on the sheet and be able to perform the exact same cut again.

*"If it's still “too soon” to discuss that, I understand"* I appreciate that. We are 3 months away from beta testers so I  expect to see quite a bit of improvement. Even at this early stage, it's far from a toy and I want to help communicate that. We're an open project, we have no secrets so ask away! :-)

*"I've seen some videos of hanging pen plotters that work very well when near the bottom of their work area, but are kind of terrible at the top. There was a huge amount of slop in those designs"*  I've seen that too. The top of the work area is where precision matters most. Hanging plotters usually biff it in a couple ways. 1) They are winding the string onto a spool and at the top of the work area the size of the spool is not the same anymore because it has string on it now. Worse, the string isn't evenly wound so the size might not even be consistent within one rotation. 2) String has a lot of stretch to it which is an issue when there is tension at the top 3) Micro-stepping stepper motors works great for low torque applications, but the amount of torque a stepper motor can provide falls off exponentially (If I remember that right) as the step size decreases so lower down, you get great resolution, high up the motors can't provide the torque to micro-step and you loose resolution or get strange motor behavior because they are running outside spec. For the sake of full disclosure, we have a similar issue which is that the dynamics of the closed loop controller change as you move to the top of the sheet which means the PID gains really should be dynamic as a function of the XY coordinates (mostly Y). That's on the ToDo list and should be done before beta testers get their hands on the machine.

"*A video showing a series of concentric rectangles being cut out of the sheet would be awesome for showing how things may be."* You aren't the first to request rectangles. I did the weird loopy shape for the wine bottle holder because I thought if I did rectangles nobody would be impressed, but it looks like their are probably rectangles in the future. Because of the way the machine works you will see the same tolerances regardless of shape. Basically what the software is doing is splitting each square MM in the 4x8 sheet into 100 "pixels" and then continuously calculating it's exact position now and the target pixel it needs to be in. Because of the non-linear transform the computer is doing to translate XY coordinates into chain lengths, what looks like a straight line to us is represented mathematically as some series of non-linear motions so a straight line, a curve, and a spline are all processed identically. For a sense of what the tolerances look like when applied to a straight line, here's something from the scrap pile with a straight edge next to it for comparison: https://s22.postimg.org/92rmzfujl/DSC00224.jpg

Think I used enough words :-)

Really tho. Great, insightful questions.

---

Posted on **2016-10-19 14:29:33** by **matthewrr**:

I'm hoping this will be a solution for me. I'm looking to remake all of our Burn furniture in 3/4" plywood. The designs like http://playatech.com/downloads/playa-pew/ utilize the entire sheet. Can the Maslow handle such a task with precision?

---

Posted on **2016-10-19 19:16:25** by **paulhart**:

Bar,

Thanks so much for that thorough response, it was enough words :)

I know that one of the best traits of this new generation of computer-controlled tools is that evolutions can come in software rather than hardware - so we can contribute to improvements over time.

Thanks for posting the video, the wine rack pieces look really good!

Most of all, thanks for acknowledging the areas that you know are still "opportunities" for the Maslow - transparency is the best thing.

Paul

---

Posted on **2016-10-19 19:42:10** by **mattyp**:

Great video posted showing the accuracy of the wine stand cutout. I noticed the router is sometimes jerking and twisting ever so slightly. Is it possible it catches on the rough ply sheet or just friction of the routers plywood base sliding over the work surface causing that? Could that be minimised if so by a smoother finish to the router base?

---

Posted on **2016-10-20 05:25:02** by **TheRiflesSpiral**:

I wondered the same thing... I'm planning to add a ring of UHMW to the base so there's less friction against the piece. (CoF of UHMW is 0.15 compared to plywood at around 0.5)

---

Posted on **2016-10-20 09:46:50** by **Bar**:

@matthewrr that furniture looks awesome. From a quick look over, that seems like something you could make with Maslow easily.

@paulhart I completely agree. Pushing practically everything into software is huge because like you said, you can always we can all contribute improvements over time. Something else I'm excited about is the idea that we can also all contribute hardware improvements too. Because the machine can print most of it's own parts, we can improve things like the shape of the sled which holds the router too.

@mattyp @TheRiflesSpiral You are both correct, the router does twist ever so slightly, and it is because it catches on the rough plywood. The video was of the D grade side of CDX plywood which is really rough. I chose to cut on the D grade side to show exactly this. The router rests on it's original base which is some sort of low friction plastic. The twist doesn't seem to have a big effect on the final cut quality because the router bit is ver y close to the center of rotation. What looks like a small but noticeable movement out at the edge of the bricks, is really a very tiny motion at the at the router bit.

---

Posted on **2016-10-20 11:27:00** by **TheRiflesSpiral**:

So the router base is what's contacting the material... great. Saves me the trouble!

---

