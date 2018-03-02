## CUTTER HEAD REGISTRATION
Posted on **2017-03-05 18:23:08** by **spatialguy**:

Good afternoon all, I'm wondering if someone can tell me: If I manually move the cutter head (router end mill) to a random location, can that point be registered by 'x' software and be used in my design. It's kind or the reverse of what normally happens. I move the cutter to point 'a' and some software knows exactly where 'a' is and can record the position accurately for use in my design. Anyone?&quest; Thanks, Michael Owen

---

Posted on **2017-03-05 18:54:37** by **davidlang**:

you move the cutter head to a point, tell the software that it's at location X,Y and the software will believe you and cut per it's program based on the assumption that you told it the truth.

---

Posted on **2017-03-05 19:08:18** by **Bar**:

I'm not 100% sure I understand, but I think davidlang's answer is right. You can also see the exact coordinates on the position digital readout so if you wanted to measure the distance between two points, you could.

---

Posted on **2017-03-06 00:57:43** by **spatialguy**:

I stick a large sheet of paper to my board to be cut. I mark out 12 random points that I want cut out as r50mm circles. I manually move my router to that point, press a button, move to the next point, press a button etc until done. Now I want to use those 12 points in my design to be r50mm circles within my design. I'm assuming with the z-axis, after a previous cut it raises the cutter, moves to the next point, plunges, cuts, raises, moves, plunges, cuts, raises until done. 



I'm not good at explaining, but I can see it clearly in my head, does that help...



M

---

Posted on **2017-03-06 05:22:55** by **TheRiflesSpiral**:

I think what you would want to do in that situation is to have your r50mm circle loaded into Ground Control with the center of the circle at "zero" (in software). There's a function in Ground Control to set where zero is on the workpiece. So then you would manually move the router to your randomly chosen point and tell Ground Control that's where zero is.

---

Posted on **2017-03-06 08:14:48** by **spatialguy**:

Sorry, I don't follow you. I don't want to touch the router through the whole circle cutting process or the cutting of the surrounding shape. Are you saying manually do that for every circle.

?&quest; or register the first circle 0,0 and the rest will register themselves as I move the router. I don't know what ground control is TRS...sorry, (where's the no judgement forum when you need it)

---

Posted on **2017-03-06 08:29:44** by **TheRiflesSpiral**:

Ground Control is the software that controls the motors. GCode is uploaded to the software and that's what's cut.



If you don't want to touch the router between cuts, you'll need a file with all the circles on it already, in the positions you want them. You'll end up defining multiple cut paths and the Ground Control will happily cut one right after another.



What you're describing (with moving the router, setting a reference point, moving the router again, setting another reference point) isn't supported in Ground control... There's one reference: zero.

---

Posted on **2017-03-06 08:36:40** by **spatialguy**:

You guys (TRS especially) are very very patient, thank you. 



That's what I figured re only one ref point. I just wish I could communicate better...you say I need a file with all the circle positions on it already - I agree  >> can I put the circles on that file by manually moving the router to each point and say to the software/file, put a circle here...and here...and here...then save the file and print/cut 'Prut' it.

---

Posted on **2017-03-06 08:42:57** by **TheRiflesSpiral**:

Oh, I see the disconnect...



The file you're going to cut isn't created at Maslow. Ground control isn't CAD/CAM software, it's machine control software.



Do you use AutoCAD or Sketchup or any other illustration tools? That's where you need to start. If not, you can start right in MakerCAM if you want...



Start by inserting a 96"x48" rectangle to represent the cutting surface then insert your circles wherever you like. [SpatialGuy1](../../images/Lj/nc/Ljnc_spatialguy1.jpg.jpg) 



Then you define your cut paths, save a GCode file and upload it to Ground Control.

---

Posted on **2017-03-06 08:51:16** by **TheRiflesSpiral**:

Sorry, should have been more clear. MakerCAM is web-based CAM software. Check it out at www.makercam.com

---

Posted on **2017-03-06 08:51:52** by **spatialguy**:

I use plain old AutoCAD, Inventor Pro and Fusion 360. I'm aware of the process well enough...design, convert, upload, print. I'll just do my random hand drawn design, measure and scale the circle centres and add to my design file. I like doing my designs by hand and then drawing in my design software and was looking to cut a corner. Never mind, I'm satisfied with that. Thanks for the help, hope you haven't pulled all of your hair out!!

---

Posted on **2017-03-06 08:56:39** by **TheRiflesSpiral**:

No problem. What you're describing is a neat concept... sort of using the machine as a design tool.



I think that Kickstarter project (Glow Forge or something like that?) has that kind of functionality. I think it uses a camera to image the design you put under it then the software lets you define what to do with the laser.



But in terms of using a CNC as a sort of coordinate measuring machine where moves at the end effector translate to content creation, no, I'm not aware of anything like that.

---

Posted on **2017-03-06 09:02:42** by **spatialguy**:

Thanks again, I shouldn't have taken so much of your, and others, time. Thanks again. I have been yapping a lot on this forum, I think I'm just excited at the size and possibilities of this router. I have a small desktop router and a 3D Printer but this is a proper practical usable size! It's awesome!! I have 3000 ideas already...

---

Posted on **2017-03-06 09:13:02** by **spatialguy**:

A ha - found it, have you seen this http://makezine.com/2015/05/17/self-aligning-handheld-router-gets-new-look-name/

---

Posted on **2017-03-06 09:39:20** by **TheRiflesSpiral**:

Oh yes... shaper. I'm not sure we've ever really debated it's merits here on the Maslow forums but I'm personally skeptical it has a market.



Having used a router by hand for extended periods of time, this looks like a really quick way to get a backache!

---

Posted on **2017-03-06 09:59:06** by **spatialguy**:

lol, pessimist :-)

---

Posted on **2017-03-06 12:32:56** by **Bar**:

My favorite thing about CNC is that it does the work while I hang out on the forums : ) The shaper is a very cool idea. 



I like how they have some basic CAD/CAM functionality built right into their control software. That is something I would like to explore adding, but probably not until we get all the bugs worked out with the basic use case.

---

Posted on **2017-03-06 14:23:45** by **davidlang**:

unfortunately there is already a woodworking tool called a shaper, so hanging that name on this semi-manual router is bad marketing at best.



the problem I have with it is that it only has a little bit of adjustment, so it can only cut correctly if you have the router pretty close to where it needs to be (within an inch or so), and you still have to do all the design work that you would need to do to use a 'real' CNC device. The only thing you possibly save is the step to convert the design to g-code, and that is getting better and better.

---

Posted on **2017-03-06 14:56:52** by **TheRiflesSpiral**:

Not to pile on... but I will. :)



The whole "spread this goofy looking tape all over your project so Shaper can see where it's going" thing seems like an unnecessary raw material to justify continuous patronage. Sorry.. I'll stop now.

---

Posted on **2017-03-06 16:11:28** by **TomTheWhittler**:

But wait. I got an idea for a Maslowcnc improvement. Use cheap painters tape to mark your design on your plywood. If you control with a Rasphberry Pi 3 then  the use the Pi camera to view the tape and control Maslowcnc. Sort of like those tape following robots. ;)

---

Posted on **2017-05-22 17:06:36** by **thejuggler**:

While the topic here seems to have moved on a little there is one interesting point that was never really answered, which is can the Ground Control software take feedback from the motors to receive positional information?  We understand that based on the geometry entered, during calibration, it knows the centre of the workspace, so can  you move the sled, and have the GC software read the position based on how the motors moved?

My guess is no as the motors are not powered so the encoder would not be active .... still I can see some interesting applications if it were possible.

---

Posted on **2017-05-22 18:39:51** by **TheRiflesSpiral**:

The gearbox between the motor and gear prevent the sled from moving. (except when driven by the motors.) The Ground Control software has a means of moving the sled arbitrarily so the position can be easily changed while retaining positional data. The missing piece relevant to this topic is a means of recording a series of points.



One way to accomplish what OP is looking for is to make a simple file with a circle centered at 0x0y then move the sled manually with GC to the center of where the circle should go, then re-define center. GC would then cut in that location.

---

Posted on **2017-05-23 06:59:33** by **thejuggler**:

Thanks TRS.  I assumed that was the case.

---

