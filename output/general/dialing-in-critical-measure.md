## Dialing in Critical Measurements
Posted on **2017-04-16 15:06:25** by **rexklein**:

1. Adding the furniture pads really helped the the @Rex frame.

2.It would be really cool if there was some kind of measurement order list for example if your getting ovals then check this etc. How about creating a maslow.nc pattern with a know pattern maybe a square and a circle from this known cut if it's oval check this or if it is not level check that etc.



3. Sprocket sensitivity I am thinking of making a very adjustable motor mount to get the vibrations out of the chain. As tension increases I get more vibration.



Finally here is my progression pic. 



https://goo.gl/photos/cxUnnzyALs9hx6XF9

---

Posted on **2017-04-16 15:07:03** by **rexklein**:

again sorry my typos suck.

---

Posted on **2017-04-16 16:29:45** by **Bar**:

I am a big supporter of the idea of a test shape. What would be the ideal shape?

---

Posted on **2017-04-16 16:30:52** by **carlosrivers**:

I think a square, it would be easy to measure the sides and corners with a 90 degree tool.

---

Posted on **2017-04-16 17:59:57** by **jbarchuk**:

Carlosrivers, exactly-exactly. I'd thought about this before, seeing all the circles folks were cutting, but didn't think about it enough to mention it.

A square is drastically easier to eyeball-measure than a circle. With a circle it's harder to find the two 'opposite points' that define the diameter. Not impossible of course, but the square is purely easier.

Further, a circle could be egg shaped by a few mm, with different radii at different points, and that effect be nearly invisible.

Further, the egg could be rotated a couple of degrees and be nearly invisible.

A faulty square could have several faults and come out as a parallelogram or trapezoid, or even have curved edges. Those non-90 degree angles are much easier to gauge and measure.

The story I heard many years ago was that when the ancient Greeks first thought about optics they started by trying to study spheres because they *thought* it was the cleanest, simplest shape. Turned out that of the simple sha pes it's actually the most complex in the geometric sense, and they never got very far with it. Or at least not as far and fast and they -could- have if they'd started out with simpler cubes. and triangles.

---

Posted on **2017-04-16 21:45:32** by **scottsm**:

I suggest a square with a smaller circle centered within it. The square is an easy test of size accuracy and the circle of smooth following a (slightly) more complicated path. As the circle is centered, it is easy to measure its diameter in a couple directions to confirm what is found with the square's measurements. That said, the test figure built into the newest release is part rectangle, part circle. It should show whether two sides are at a right angle, and how smooth a partial circle is.

---

Posted on **2017-04-16 22:00:45** by **Bar**:

I was thinking that the half square half circle was the way to go when I made the test shape for running the feedback system test, but I agree that a square is probably the simplest when it comes to a basic shape we can measure easily.

---

Posted on **2017-04-17 07:04:56** by **rexklein**:

Actually @bar I think square is the way to go however. if a person has a zaxis I think the ideal shape would be a diameter circle inside a square of the same dimensions. As long as tabs are present I think that if a circle was cut that would  touch the square at tangents  the user would know at a glance the accuracy of the setup. if a circle is oval it would be easy to see. The square is a no brainer a circle inside a square gives you more information without measuring.  Best of both worlds.

---

Posted on **2017-04-17 08:23:21** by **Bar**:

I agree, that sounds like the way to go.

---

Posted on **2017-04-17 08:33:24** by **scottsm**:

I've just been cutting tests by routing twice around the shape, not all the way through. This tests the z as well, as I can measure the depth of the cut. I'm thrifty (cheap) :) so it lets me move over and run an overlapping pattern when I test a change. Without the z-axis, one could choose whether to continue the test shape or stop at each depth change and between the square and the circle.

---

Posted on **2017-04-17 08:51:17** by **rexklein**:

I like the idea of not going all the way through. So how about a square with a circle at tangents and a cross hair at system 0,0. I too dont like to waste material. However an uncalibrated Maslow is the definition of wasting material

---

Posted on **2017-04-17 08:56:51** by **davidlang**:

@rexklein, the problem is that the distortions are in the way the maslow is positioning things, having it cut multiple shapes is not going to let you see the flaws because all the shapes are going to be off by the same amount



a square that can easily be measured and checked for square (measuring from opposite corners) is what's needed

---

Posted on **2017-04-17 09:06:37** by **scottsm**:

If the circle is centered in the square, one can find its center with a ruler from opposite corners. Once that point is pencilled in, check diameters from various directions across the circle through it. The point is 'close enough' even when the square is oblong or slightly rhombic. I think keeping the circle diameter different would keep issues affecting the two geometries separated.

---

Posted on **2017-04-17 09:20:12** by **gero**:

I like the square and circle idea. All using the same .nc file, firmware and GC version. Then a spreadsheet with variations on x and y, motor distance and hight. What else? Weight of the complete sled?

---

Posted on **2017-04-17 10:09:07** by **rexklein**:

One part that can not be over looked is a maslow inc sourced NC. I don't know about everyone else but getting my g-code right (i am trying all kinds of tools) is my own educational journey. knowing I have the machine "to spec" would allow me to evaluate my gcode efforts @Bar never claimed CADCAM and I think it will save him untold support hours  to backers to be working from one file versus 100's of files people will coble together

---

Posted on **2017-04-17 11:23:16** by **rancher**:

Rex, I agree and have been on this band wagon for weeks now.  One universal test file that we can report measurements and whatnot on and use to calibrate and evaluate.  I would love to see Scott's grid of squares, or something similar, as part of the set up protocol.

---

Posted on **2017-04-17 13:35:03** by **rexklein**:

@Rancher thanks, it's easy to forget were beta testers for the roll out to backers. The first order of business is a built calibrated machine. with as little struggle as possible. As I look back on it most of the struggles were of my own making because I wanted to get down to the business of "making" things. So I have allocated way to much time to generating G-code etc. This discovery is a lot of fun, but the goal is for maslow to ship-assemble-and be calibrated so there is a clean stopping point for maslow support.

---

Posted on **2017-04-17 23:32:59** by **scottsm**:

I ran this [.nc file](https://github.com/MaslowCNC/Mechanics/commit/fe0ebd1173eb2a99638eae437987ec535bcd3829) with an 1/8" bit and got a creditable 6 1/8" square around a 3 5/8" circle. My z depth came to a shade under .3", instead of the expected .25"; this could be my z-drive settings. Nicely done @Bar!

---

Posted on **2017-04-18 08:02:43** by **Bar**:

We're getting closer every day! (Thanks to you guys). Have I mentioned that you are all amazing recently?

---

Posted on **2017-04-18 08:10:17** by **scottsm**:

I've been looking for a way to calibrate the z-axis for depth. What approaches have folks used?

---

Posted on **2017-04-18 08:50:58** by **Bar**:

I used the measurements off the knob on the router. I believe each rotation was marked as 1/8th inch so I just converted that length to mm and entered it as the thread pitch. 



I've found it to work well with the exception that it's important to keep in mind that an up spiral bit will pull the router into the wood so any backlash in the router adjustment will be taken up in the into the wood direction. That's important when setting the z-axis zero point.

---

Posted on **2017-04-18 08:58:57** by **scottsm**:

How much backlash do you see? What steps do you take to counteract it or account for it?

---

Posted on **2017-04-18 09:29:57** by **Bar**:

My router has a LOT of backlash. Maybe 1/8th inch. I counteract it by pushing in on the back of the router when I'm setting the z-axis zero point at the surface of the wood. After that it seems to be pretty much ok. When it lifts up to move from one cut to another the height is probably off, but as long as the "safety height" is set high enough it isn't an issue. My feelings on the backlash are that it's pretty terable that the router has so much play in it, but as long as you are using an up spiral or down spiral bit the backlash will be pulled one way or the other which means that while cutting, the amount the axis moves is very consistent.

---

Posted on **2017-04-18 10:23:01** by **scottsm**:

Good to know. Explains why the "Home" button steps out so far before traversing, a very good thing. I've gouged a few things apparently by ignoring/forgetting/not knowing this. I'll use a higher 'safety height' when I create gcodes. I'm going to check the test file for this right now :) Looks like it uses Z0.15 What do folks think about increasing that to say Z0.2?

---

Posted on **2017-04-18 10:26:00** by **jbarchuk**:

> @Bar

> important to keep in mind that an up spiral bit will pull the router into the wood so any backlash in the router adjustment will be taken up in the into the wood direction. That's important when setting the z-axis zero point.

*Emphasis!!!* This is related to a recent comment about how important 'new user' docs will be as regards cal and ops and saving support time. This whole project has MORE UNCONTROLLED VARIABLES than any other project I've ever seen. Between routers, bits, materials, speeds, frame design and build, no two machines will ever be the same. Similar but not identical. The more variables that can be described and explained in the docs, the easier user support will be.



For users for whom z-depths are important (or even critical) I think it's very important to describe as many of these effects as possible in the z-cal docs. Touching the (stationary) router bit to the working surface does not suffice. Materials such as flakeboard have an extremely variable surface. Other materials such as plywood will have a more regular surface, but there will still  be variation based on whether it's a solid soft or hard wood, or plywood. A -test- cut using MDF or falkeboard, and then a -final- cut on plywood, will have varying effects.



Z-cal will require running the motor and doing plunges and measuring them, recording notes, and doing similar tests for different bits/materials.



*IDEA* Rather than the user keeping manual records of this, how about the GC keeps a user-managed table of bits/materials? The user names a material, and the cal process keeps record of them? When the user cuts something, the GC displays the material it's using the calibrations as previously recorded. Should I write an issue? Or is this too much work -and- too much variability that there's a threat of Useless Feature Creep?

---

Posted on **2017-04-18 10:38:36** by **scottsm**:

There is indeed a steep learning curve, but this beta! python, Kivy, Arduino, github, chain-drive, router bit dynamics - a firehose of new and interesting things to learn/remember , and _wood chips_! Lots of wood chips....

---

Posted on **2017-04-18 10:54:07** by **Bar**:

@scottsm I think upping the z-axis lift to .2 is a great suggestion. Do you want to make a PR for it or should I just change it?



@jbarchuck I couldn't agree more that we need more user documentation about how to get started. I think we need to walk the line between the fact that if we write too much a lot of people won't read it all, and not saying enough. I think maybe a concise "Getting Started" wiki page which has links to other pages with more details. Eg "What kind of router bit should I use? Use a 1/4 inch up spiral, or click [here](www.google.com) to learn about other options"



I'd like to keep GC as simple as possible for now because like you said, there are already SO MANY new things to explore. I do think that a materials GitHub page so that we can all share experiences would be a great idea though.

---

Posted on **2017-04-18 11:23:12** by **rancher**:

Look what I just did.  Downforce!



[DownZ1](/images/PN/49/PN49_downz1.jpg.jpg) [DownZ2](/images/fr/mL/frmL_downz2.jpg.jpg) [DownZ3](/images/NG/2Z/NG2Z_downz3.jpg.jpg)

---

Posted on **2017-04-18 11:24:57** by **rancher**:

My square/circle was 6.5x5.5 and 3.25x3.75.  Yikes.

---

Posted on **2017-04-18 11:58:33** by **mindeye**:

That's awesome @rancher! Old bicycle inner tubes are a great material. I've used them for lashing bits of boats together or lashing things to my car's rack for some time now.

---

Posted on **2017-04-18 12:10:00** by **rexklein**:

@rancher great thinking. Going to do that myself now that you have shown me how

---

Posted on **2017-04-18 12:18:59** by **jbarchuk**:

> @rancher

> Look what I just did. Downforce!

*BAR!! LOOK AT THIS!!! IT'S A GAME CHANGER!!!* THE ROUTER Z-AXIS BACKLASH WAS THE ONLY UNCONTROLLABLE/UNMEASURABLE BACKLASH ITEM IN THE WHOLE SYSTEM!!! THIS IS A MEGA-FIX!!!

Rancher, You are SOOOO LUCKY that you wrote 'just did.' I've thought about this literally for months. But being a metals-mechanical kinda guy all I could think about was springs, levers, adjustment screws and all that complicated crap. *IF* you had said, 'Oh, yeah, I did this weeks ago...' I woulda had to box you SEVERELY about the head and shoulders, and I HATE any kind of violent activity. Instead... (back in a few minutes...)

---

Posted on **2017-04-18 12:52:33** by **Bar**:

That looks awesome! Great solution!

---

Posted on **2017-04-18 13:13:01** by **scottsm**:

@jbarchuk, I'm interested in temporarily rigging a dial indicator to study the z-axis. It sounds like you've got lots of experience there - can you give me any tips or pointers?

---

Posted on **2017-04-18 13:15:33** by **rexklein**:

I have a set of digital calipers they could easily be attached I think I got them at (no judgement) harbor freight. They were cheap but they would accomplish the objective

---

Posted on **2017-04-18 13:16:27** by **rexklein**:

they can be zeroed at any point of extension.

---

Posted on **2017-04-18 13:29:02** by **jbarchuk**:

> @scottsm

> can you give me any tips or pointers?

Not really. I'm better at seeing -potential- problems or issues than sometimes finding fixes. A solid state pressure gauge is also an option. A kitchen scale with a 5# or 10# range should work. It doesn't take much pressure to hold the router down. That's static testing though -- with the route running and chains pulling there a a billion milligrams of pressures flying in all directions. Very tiny distances, but measurable enough to confuse an analog or digital gauge. With a scratchbuilt digital gauge software could dampen and average the numbers, but that's a ton of work. Static should be good enough.

---

Posted on **2017-04-18 13:32:48** by **jbarchuk**:

> @rancher

> Look what I just did. Downforce!

I said I'd be back. Rancher, congratulations, you are the first recipient of the *Maslow User Contribution Gold Star Award!* (Pronounced 'mugs.') So I edited your icon. Here are two different file formats depending on what you need.

 [Rancher-icon-01](/images/DO/oY/DOoY_ranchericon01.jpg.jpg) [Rancher-icon-01](/images/GL/xj/GLxj_ranchericon01.png.jpg)

---

Posted on **2017-04-18 13:37:33** by **jbarchuk**:

> @scottsm

> rigging a dial indicator

SORRY! I MISREAD THAT! As I thought about it in the past I never had any concern over -distance-, only the -pressure- required to lock down the router. Once it's solid the backlash is zero. But the TRADEOFF is that anything we attach fights the penUP motion. There's a balance where enough is fine and too much will wear out threads muuuuch faster.

---

Posted on **2017-04-18 13:52:30** by **rexklein**:

quick and dirty test move distance set to 100mm so I expected 10mm

---

Posted on **2017-04-18 13:53:31** by **rexklein**:

https://goo.gl/photos/aCTvPoNHWZ3Qh4UZ6

https://goo.gl/photos/zfDupcWj2tyRgMnx6

---

Posted on **2017-04-18 13:54:30** by **rexklein**:

I never said it was pretty

---

Posted on **2017-04-18 13:57:02** by **rexklein**:

now I know why I have either not gone through or went way way through clearly my thread-pitch is off. I am using the STD GC settings

---

Posted on **2017-04-18 13:59:15** by **rexklein**:

maybe a bronze star for that one?

---

Posted on **2017-04-18 14:30:58** by **Bar**:

I would expect the standard settings to work because we're both using the exact same router. One good way to test could be to watch the motor and if you command it to move .125 inches it should make one full rotation.

---

Posted on **2017-04-18 14:32:13** by **scottsm**:

@rexklein, that's the idea I'm looking for - bronze star for you, in my book! I'm interested in tracking how far the router moves for one rotation of the z-coupler. I'll also need to figure a way to accurately, repeatably _cause_ one rotation, or to see and record the number of steps moved for a distance command.

---

Posted on **2017-04-18 14:33:49** by **Bar**:

If you set the z-axis pitch to something easy to enter like 5mm then send the command to move 5mm you should see exactly one rotation

---

Posted on **2017-04-18 14:43:54** by **rexklein**:

I will test it with tomorrows release

---

Posted on **2017-04-18 14:51:08** by **scottsm**:

Thanks, @Bar, that will do it. I can then measure the actual travel and update the value :)

---

Posted on **2017-04-18 15:26:09** by **rancher**:

> @jbarchuk

> Maslow User Contribution Gold Star Award!

Well if that isn't the coolest thing!  Thank you!

---

Posted on **2017-04-19 08:29:48** by **jbarchuk**:

> @rancher

> Well if that isn't the coolest thing! Thank you!

YVW. That really is an awesome mod and fixes a major problem.

---

Posted on **2017-04-19 09:01:24** by **rancher**:

Okay gang, so....we have a test shape.  Now what?



I just spent the last couple hours in the shop, tweaking parameters slowly, and trying to see a pattern and figure out how to dial in the accuracy.  I got nowhere.  My circle/square is wider than tall, and I could make it change a bit with the H and V offsets, but......I sure could not get it close enough to build something.  



Does anyone have any clues on how to improve accuracy?  Do we have a plan for how we are going to get there?  I'm a bit lost as to the next step.  I was sorta hoping I just had to go beat my head against it and put the work in, but I cut a dozen of those little suckers and am no closer to a useable machine.  What's next?

---

Posted on **2017-04-19 09:30:17** by **scottsm**:

I'm puzzled as well. Day before yesterday I cut a perfect square and circle. Yesterday, on the same panel the same file was oblong. I've run a newer version of firmware and software, but don't think that's the cause. Digging into it...

---

Posted on **2017-04-19 09:35:59** by **rancher**:

Thank you Scott, that's reassuring.  I've had better cuts in the past, right now things are really oblong.  Let me know if you get anywhere.

---

Posted on **2017-04-19 09:46:52** by **Bar**:

I'm in the same boat. It seems like some days are better than others and I have no idea why.



The next step I'm working on is fully automating the calibration process with a step by step process in Ground Control which will look like  [this](/images/B5/t5/B5t5_stepbystepprocedure.jpg.jpg) . All of the measurements will be done by the machine itself. I think that having at least a repeatable procedure where the last step is to cut a test shape will go a long way towards reducing variability. 



I'm glad (well not glad) to hear that you are seeing the same behavior where what works one day might be off the next. I was worried that I was the only one seeing that issue because I keep changing everything about my machine so often. Maybe we should go back to hard coding the machine dimensions in the firmware as a test to see if something is going wrong with how the settings are sent to the machine? If we are truly seeing different results every day it would be nice to KNOW with absolute certainty that the math is being set up the same way every time.

---

Posted on **2017-04-19 09:54:09** by **Bar**:

I'm thinking it might be an issue with the way the settings are sent to the machine because I never had these problems before making it possible to change the machine dimensions in the settings. Then again I also only had the one machine with the one set of measurements that I dialed in over time.

---

Posted on **2017-04-19 09:59:40** by **blsteinhauer88**:

@rancher can you send me the .nc file of the test shape and Ill run it on mine after work.

---

Posted on **2017-04-19 10:03:05** by **blsteinhauer88**:

I found it in Git Hub nevermind...

---

Posted on **2017-04-19 10:04:59** by **scottsm**:

One thing I noticed was that over night, the sled had 'crept up' so that the home position was 6" to 8" above the center. I had hung the sled on a nail with the chains slack. Do you leave your sled hanging? I wonder whether this is a factor? 

These are the things I can see to try; any thoughts about which order to apply them? Any other things to check or try?

- Verify measurements recorded in groundcontrol.ini

- Recalibrate chain length, automatic

- Wipe Eprom

---

Posted on **2017-04-19 10:14:31** by **rancher**:

Hmmm, that's interesting about the overnight creep.  With slack on the router side, the tension side could have been slowly backing the chain down.   I thought the motors were locked when not powered, but maybe not.



I agree with you Bar, that things got weird once the settings became a variable.  I also have a non standard frame, and even though I tried to copy your measurements, I feel I may be off by a few mm.  Due to that, I thought I might be able to adjust it out in the settings, but no luck so far.



Perhaps the answer is not to try to make it perfect but to "stretch" it to fit?  I don't know anything about the firmware/software.  But is it possible to measure our shape, then push/pull X or Y to calibrate it.  It would seem that rather than worry about chains and position, it could be as simple as x1"=x1.12" or whatever.  Totally just brainstorming, that probably wouldn't work due to complicated stuff I don't understand.  There ya go though!

---

Posted on **2017-04-19 10:20:57** by **Bar**:

The motors are in theory locked when they aren't powered. There is a worm gear in the gearbox so it shouldn't be possible to back drive the motor from the shaft. That being said, if you saw it move then it moved and we shouldn't discount it. 



I'm going to try to make a version of the firmware which has the dimensions hardcoded in the firmware and see what happens then.

---

Posted on **2017-04-19 10:23:58** by **blsteinhauer88**:

I also notice something has changed.  My original chain calibration, I painted the links at the 12 o'clock.  Now the painted link is at the 3'oclock-right and 9- left as facing it.  Then, after then a motor calibration, right motor stays at 3 and left is a about 7, two links lower?  Is this the machine compensating?

---

Posted on **2017-04-19 10:27:41** by **blsteinhauer88**:

I left is like this so my 0,0 is not 0,0 on the sheet of ply, but my circles were very close.  1/8 inch wider than tall.

---

Posted on **2017-04-19 10:33:13** by **gero**:

Did all from A - Z, new Firmware, new GroundControl, Calibrate chain length, confirmed and entered all measurements.  [Test-cut](/images/w4/j9/w4j9_testcut.jpg.jpg)

---

Posted on **2017-04-19 10:43:27** by **gero**:

Stupid question, does the difference increase with size, or is the percentage the same?

---

Posted on **2017-04-19 10:45:35** by **Bar**:

That's not a stupid question at all. I'm not sure. My guess would be that its a percentage, but I really don't know.



I'm working through the same process right now. I just confirmed all the measurements, calibrated chain lengths and measured them, now I'm going to run the test cut.

---

Posted on **2017-04-19 10:56:16** by **scottsm**:

This is great! Let me know how best to add to the effort - standing by.

---

Posted on **2017-04-19 11:13:53** by **Bar**:

I've got good news and bad news. The bad news is that I definitely messed something up. I'm not sure what yet, but something in the math is wrong. The good news is that if you use the original values that the math was computed with the results are pretty good.



Here are my test results:  [square-x](/images/fO/hI/fOhI_img_20170419_105831366_hdr.jpg.jpg)  [square-y](/images/F1/0b/F10b_img_20170419_105858474_hdr.jpg.jpg)  [circle-x](/images/vK/Ss/vKSs_img_20170419_105929898_hdr.jpg.jpg)  [circle-y](/images/yP/4x/yP4x_img_20170419_110003070_hdr.jpg.jpg)  [Settings](/images/IH/IA/IHIA_settings.jpg.jpg) 



The square is almost unbelievably good, the circle is a little more off (but very consistent). I think that the error in the circle probably has more to do with my ability to measure exactly across the widest part than with the real dimensions. 



So what do we do now? What can we do in the next 2ish hours before this week's release to make it as productive a week as possible for everyone? Do we just recommend making your motor spacing the same as mine, and disable the settings panel altogether?



Would someone be willing to fudge their motor spacing to match mine and try to replicate my re sults?



In terms of a long term fix, I need to reach out to Keith (our resident math genius) and get his input on what I did wrong.

---

Posted on **2017-04-19 11:26:11** by **scottsm**:

I can pretty easily change my motor spacing, what measurements do I need to match?

---

Posted on **2017-04-19 11:27:32** by **Bar**:

I think that the big ones would be the distance between the motors and the distance between the mounting points on the sled

---

Posted on **2017-04-19 11:28:07** by **scottsm**:

OK, shoot!

---

Posted on **2017-04-19 11:29:15** by **Bar**:

Even if you can't match all the dimensions exactly I would say put all the settings in exactly the same as mine. I think something non-linear is going on in the math so any differences might be amplified, while a real world difference will probably have less effect. Here are my [settings](/images/Oy/1V/Oy1V_settings.jpg.jpg)

---

Posted on **2017-04-19 11:29:46** by **Bar**:

Thank you so much for being willing to test that!

---

Posted on **2017-04-19 11:35:07** by **scottsm**:

Myb sled measurement matches yours. My motors were 3306, I'll pull them in to 2978. Will I need to do any of the calibrations?

---

Posted on **2017-04-19 11:38:05** by **Bar**:

I would re-calibrate the chain lengths, and then just make all of the other settings match mine. If your CG is very different than mine, it might be worth cutting closer to the center of the machine where the CG matters less.

---

Posted on **2017-04-19 11:42:57** by **Bar**:

By "match mine" I don't mean in the real world, just change them to match in software so that the internal calculations are all done identically to how mine were

---

Posted on **2017-04-19 11:53:26** by **scottsm**:

Moving the motors was easy and just finished. I'm starting the chain cal now.

---

Posted on **2017-04-19 12:10:04** by **scottsm**:

My CG matches yours but I'll cut near the center anyway. I've got Firmware 0.65. I've got this morning's version of GroundControl. Is that right? If so, I'm ready to cut.

---

Posted on **2017-04-19 12:11:07** by **Bar**:

Yep, that sounds right. Those are the same versions I used.

---

Posted on **2017-04-19 12:11:51** by **scottsm**:

I didn't change the motor offset height - mine is 503.5. Does that matter?

---

Posted on **2017-04-19 12:13:43** by **Bar**:

I don't think it matters, but I would put my value of 463 in the settings anyway just to keep everything identical

---

Posted on **2017-04-19 12:14:33** by **Bar**:

It should just translate where the math thinks the center of the wood is up

---

Posted on **2017-04-19 12:16:25** by **Bar**:

I think you should be safe to not re-do the chain length calibration

---

Posted on **2017-04-19 12:16:25** by **scottsm**:

OK, I'll edit that but not change the frame. Should I re-home after making the edit?

---

Posted on **2017-04-19 12:16:50** by **scottsm**:

OK, I'll run the cut and let you know

---

Posted on **2017-04-19 12:17:29** by **Bar**:

I'm on pins and needles!

---

Posted on **2017-04-19 12:34:09** by **scottsm**:

Within the accuracy of unsanded MDF and my shaky caliper reading, the circle is 3.795" both directions, the square 6.797" in both directions. :)

---

Posted on **2017-04-19 12:34:48** by **Bar**:

This is with a 1/8th inch bit or a 1/4 inch bit?

---

Posted on **2017-04-19 12:35:18** by **scottsm**:

With a 1/4" bit.

---

Posted on **2017-04-19 12:35:23** by **Bar**:

At least we're getting the same dimensions in both directions now :-)

---

Posted on **2017-04-19 12:36:36** by **Bar**:

What could possibly be giving us different results on my machine vs your machine?

---

Posted on **2017-04-19 12:37:38** by **Bar**:

This is progress, at least we're seeing good consistency where the square is square and the circle is round not oval

---

Posted on **2017-04-19 12:37:48** by **scottsm**:

I can modify the motor height to match yours and recal the chains if you want...

---

Posted on **2017-04-19 12:38:19** by **rancher**:

Mine is easily moveable too, if more data will help.  I really need to buy a metric tape measure!

---

Posted on **2017-04-19 12:40:32** by **Bar**:

Let's think about it for a minute and make sure we're doing the right thing before we do anything else. What are all the things which could be different between our machines?



Where does the number .795 come from? Your circle and square were both measured almost exactly .795 which is interesting.

---

Posted on **2017-04-19 12:42:17** by **rancher**:

1/4" is about one chain segment length.

---

Posted on **2017-04-19 12:43:25** by **rancher**:

I don't know what the test shape is supposed to measure, but maybe it's the difference of one tooth on the measuring process?

---

Posted on **2017-04-19 12:45:18** by **Bar**:

The test shape should be 6in by 3.5in

---

Posted on **2017-04-19 12:45:45** by **Bar**:

The idea that it could be off by one tooth is interesting.

---

Posted on **2017-04-19 12:46:07** by **rancher**:

Scott's is bigger by 3/4" in all dimensions?  Weird.

---

Posted on **2017-04-19 12:46:20** by **blsteinhauer88**:

Bar move yours one tooth off and recut

---

Posted on **2017-04-19 12:46:28** by **Bar**:

Sorry to be clear it should be a 6"x6" square with a 3.5" circle in the ctner

---

Posted on **2017-04-19 12:47:01** by **scottsm**:

Let's don't chase my caliper readings too hard. It's a 6" caliper and I ran off the end trying to get the square :( Using a millimeter ruler and sanding the edges, I feel pretty good about the square being 152mm both ways, and the circle being 88mm across the flats and 88.5mm across the points.

---

Posted on **2017-04-19 12:47:49** by **Bar**:

Oh! Well in that case we've nailed it!

---

Posted on **2017-04-19 12:47:58** by **Bar**:

:-)

:-)

:-)

---

Posted on **2017-04-19 12:48:37** by **Bar**:

152mm is 5.98425"

---

Posted on **2017-04-19 12:48:45** by **rancher**:

You guys.  MM or In please!  Thank you BAr!

---

Posted on **2017-04-19 12:49:06** by **rancher**:

So.  It was pretty much right on?

---

Posted on **2017-04-19 12:49:36** by **Bar**:

Pretty much right on. Good job everyone!

---

Posted on **2017-04-19 12:50:16** by **Bar**:

.016" off or about 1/64th

---

Posted on **2017-04-19 12:50:43** by **blsteinhauer88**:

So you set the settings in GC?

---

Posted on **2017-04-19 12:50:48** by **Bar**:

@scottsm thank you so much for running that test! I think we're really getting somewhere

---

Posted on **2017-04-19 12:52:25** by **rancher**:

Bar, for sure the settings were going back to default H3040 V473 with every new GC update.  I know that was part of my issue.  Just FYI, when you are digging into the fix.

---

Posted on **2017-04-19 12:53:13** by **Bar**:

@scottsm actually fixed that issue this morning so now the settings will stay the same when you update GC

---

Posted on **2017-04-19 12:53:35** by **scottsm**:

Remember, though, that two days ago, I was [very close](/images/Z7/B4/Z7B4_img_0504.jpeg.jpg)  (middle cut) but yesterday off (left cut) and today good again (right cut). Since yesterday I altered the dimensions and did a chain re-cal.

---

Posted on **2017-04-19 12:54:37** by **blsteinhauer88**:

Will these settings work with the temporary frame when cutting Maslow parts?

---

Posted on **2017-04-19 12:54:46** by **scottsm**:

I've got some circles that were oval yesterday, I'll try them to see what happens.

---

Posted on **2017-04-19 12:55:58** by **rancher**:

So what we have now is that the motors were moved Horizontally to match Bar's setting, and that combined with matching Bar's setting values resulted in Scott's accurate test.

---

Posted on **2017-04-19 12:56:59** by **Bar**:

@blsteinhauer88 The theory right now is that changing the settings to anything other than the defaults messes with the internal math. If you use my default [settings](/images/yP/N2/yPN2_settings.jpg.jpg) and try to make your machine physically match mine as closely as possible you will get [good results](/images/gu/1u/gu1u_squarex.jpg.jpg) . What I broke in the internal math is yet to be determined.

---

Posted on **2017-04-19 12:58:38** by **Bar**:

@blsteinhauer88 and @rancher, would either of you guys be willing to try to replicate @scottsm's results and see if making your machine the same dimensions as mine, then using all the same settings gives you good results?

---

Posted on **2017-04-19 12:59:00** by **rancher**:

Yeah, I can go do that now.

---

Posted on **2017-04-19 12:59:56** by **blsteinhauer88**:

I will, but have to be later.  Reading all this on my lunch.

---

Posted on **2017-04-19 13:00:07** by **Bar**:

I believe the procedure is:

1) Enter all the settings like [this](/images/xf/EQ/xfEQ_settings.jpg.jpg) 

2) Calibrate chain lengths - automatic

2) Run the test shape with a 1/4 inch bit

---

Posted on **2017-04-19 13:02:38** by **rancher**:

How wide are the motors?  9' 9"+ a hair?

---

Posted on **2017-04-19 13:05:13** by **Bar**:

117.259 inches which is a hair over 9' 9 1/4"

---

Posted on **2017-04-19 13:05:51** by **rancher**:

Thank you.  On my way down to the shop now.  I'll report back.

---

Posted on **2017-04-19 13:06:03** by **Bar**:

Best of luck!

---

Posted on **2017-04-19 13:08:17** by **Bar**:

Keith already got back to me about the math (what a guy!) so we're pushing on wards towards getting everything fixed.

---

Posted on **2017-04-19 13:19:31** by **blsteinhauer88**:

That is why mine are so close, mine are 116.5 inch

---

Posted on **2017-04-19 13:27:49** by **Bar**:

I was thinking that. You've been getting the best results because your frame is the most like mine.

---

Posted on **2017-04-19 13:32:21** by **gero**:

If someone can replicate this, it might help. I had a wrong distance of the chains on the sled. Putting the right on I got close. Bumping up a little I am spot on. Still needs to be confirmed on part farther away from the center.  [Spot-on](/images/CO/xF/COxF_spoton.jpg.jpg)

---

Posted on **2017-04-19 14:14:31** by **MakerMark**:

Here are my results using the Groundcontrol settings Bar posted.  

square-x = 5.945 inches

square-y = 5.984 inches

circle-x=3.493

circle-y=3.513

My actual motorspacingx = 3048 and sledwidth = 324.

---

Posted on **2017-04-19 14:14:54** by **Bar**:

Oh WOW!

---

Posted on **2017-04-19 14:15:28** by **Bar**:

So that was without actually adjusting the real motor spacing to match the settings, just using the settings?

---

Posted on **2017-04-19 14:16:14** by **MakerMark**:

I only matched the software settings and didn't change anything physical.

---

Posted on **2017-04-19 14:18:08** by **Bar**:

That's a huge result. So it looks like you are better off using the default settings even if they aren't right than to change them. Thanks for running that test.

---

Posted on **2017-04-19 14:21:03** by **Bar**:

Basically measuring the difference between the motors wrong by 50+mm (2+in) only results in a +-.016in (.4mm) error.

---

Posted on **2017-04-19 14:27:49** by **rancher**:

I had a good run gang!  I forgot the card in my camera, and I don't own a micrometer, but it was real close using a steel rule.  Less than 1/16" out by my best quick measure.  I moved my motors to match and changed my settings to Bar's.

---

Posted on **2017-04-19 14:37:34** by **Bar**:

Fantastic! So basically what we've learned is that if you move your motors to match my spacing and use my settings you will get good results. Even if you don't move your motors you should still probably use my settings because something is off in the math.

---

Posted on **2017-04-19 14:40:58** by **Bar**:

I am going to put a quick spot in the update this week to let everyone know what we found here today and I'll find out what's going on with the math and get if fixed ASAP.



How do we make sure everyone knows what's going on? I don't want anyone wasting time mucking about with oval circles now that we know what the fix is.

---

Posted on **2017-04-19 14:47:42** by **MakerMark**:

Weekly update should catch most. Possibly a message in this weeks release notes for Groundcontrol and Firmware?

---

Posted on **2017-04-19 14:55:05** by **rancher**:

How hard would it be to just default and disable those settings for the time being?

---

Posted on **2017-04-19 14:58:12** by **davidlang**:

probably better to leave it in the config and fix the math than to go to the effort to eliminate the config for a short time (few days probably)

---

Posted on **2017-04-19 15:03:47** by **rancher**:

Easy for you to say, you didn't hike up and down the hill because you forgot the .jpg of Bar's settings and were trying to remember 2973.4 because the default is 3040.

---

Posted on **2017-04-19 15:04:02** by **rancher**:

:)

---

Posted on **2017-04-19 15:06:02** by **Bar**:

It wouldn't be hard at all to disable them. We could do it on either the Ground Control side (make the options grey and unchangeable) or on the firmware side (just ignore command to change them). Doing it in GC seems like the more transparent thing to do, but part of me wants to just disable it in the firmware, that way people won't get out of the habit of adjusting the settings.



I think that the most transparent thing we can do is to tell everyone what's going on. I say we leave the settings in for the next few days. If we haven't got a complete fix by next Wednesday we force it to the defaults to prevent undue hill climbing.

---

Posted on **2017-04-19 15:07:59** by **rancher**:

I did not mean to imply that it should be hidden.  It makes sense since it offers the best results across the board.  I spent a LOT of time this morning trying to make the settings match real measurements, then tweaking from there, to no avail.



I think just grey them out for now, and make a note that optimal performance is achieved with correct motor spacing.  Somewhere.  :)

---

Posted on **2017-04-19 15:37:41** by **Bar**:

You are right. If it saves even one person from having to mess with them we should grey them out. I'll make the change right now.

---

Posted on **2017-04-19 15:57:19** by **Bar**:

The settings are now disabled like [this](/images/pW/vS/pWvS_settings.jpg.jpg) in the newest version of Ground Control. The default values are now also used by the latest firmware. When the command to change the settings is sent to the latest firmware it will respond with "Settings Not Updated" to make it clear that the command was not accepted.



I'm going to run a test cut with both right now to make sure everything is good to go, then I'll release a new version.

---

Posted on **2017-04-19 16:19:34** by **Bar**:

Looks good

---

Posted on **2017-04-19 16:23:17** by **scottsm**:

Will that be the release for next week (release number already bumped...)?

---

Posted on **2017-04-19 16:25:02** by **Bar**:

I was thinking of just doing another one right now. That way the latest version has the settings greyed out, but if someone really wanted to be able to access them they could go back one version. What do you think?

---

Posted on **2017-04-19 16:30:08** by **scottsm**:

I like it!

---

Posted on **2017-04-19 16:32:23** by **rancher**:

Me too!

---

Posted on **2017-04-19 16:41:01** by **scottsm**:

I could wish there was a way to put the release number into the name of the .dmg file...

---

Posted on **2017-04-19 16:42:14** by **Bar**:

We could just put it in there like GroundControl0_68.dmg or something like that

---

Posted on **2017-04-19 16:42:20** by **Bar**:

I've been thinking that too

---

Posted on **2017-04-19 16:48:20** by **scottsm**:

I was hoping for a way to have buildozer automate it - you've seen that I'm prone to mistakes :)

---

Posted on **2017-04-19 16:56:59** by **Bar**:

Hahah I'm a huge fan of automating things. Us humans seem to be pretty forgetful. I don't know of any way to do it unless we wrote a batch file to edit the text of the file for us, then we could have it change the file name and update the text. We're getting off the original thread topic tho :-)

---

Posted on **2017-04-19 18:05:29** by **bdillahu**:

I just wanted to thank all of you guys... as a non-beta person, you don't know how much I appreciate you working out stuff like this (and having the knowledge to figure it out). Something like the non-circle circles slipping through to "production" would have been highly disappointing to a lot of people, and gotten some bad press.



So now it's all narrowed down (soon to be fixed, I'm sure) :-)

---

Posted on **2017-04-20 16:30:53** by **gero**:

If it could to help to circle in, I have space to go out and up with the motor mounts. Going down and more narrow there is plenty of space. If anyone would like me to try specific measurements, let me know. Even a series of mounting points.  [IMAG0659](/images/8B/ZZ/8BZZ_imag0659.jpg.jpg)

---

Posted on **2017-04-20 16:41:36** by **Bar**:

Slick! I've got a fix that I think works, I'm just working on updating the wiki page now, then I would absolutely love help testing it to make sure it truly works. Give me maybe 20 minutes to get things squared away?



Your work in dialing in the sled mounting points was incredibly helpful today so thanks for sharing that yesterday!

---

Posted on **2017-04-20 17:28:54** by **Bar**:

Alright I think I've got things tracked down, but I'd like at least two other people to agree before we move on. 



I think that we were dealing with two issues. 



1) There was a bug in the way the settings were transmitted to the machine thanks to some help from Keith who worked out the math initially, I think I've tracked down. 100% my fault, not his.



2) We needed a clear testing procedure for what to do when the calibration is off. Thanks to @gero's contribution yesterday I've determined that the most critical measurement is the spacing between where the chains  mount onto the sled, which is also a difficult distance to measure accurately. I've taken gero's method of iteratively cutting the test shape and tweaking spacing based on the result and made it a "Check Calibration" step in the instructions [here](https://github.com/MaslowCNC/Mechanics/wiki/Using-the-Temporary-Frame-to-Cut-Parts#step-9-check-the-calibration)



Based on these two methods I've been able to get good cuts on my temporary frame which has a 3025mm motor spacing and a 200mm sled mount spacing.



Would  anyone else be willing to confirm that these two fixes in conjunction solve the problems we were seeing yesterday?



The steps to test are:

1) Update to the very latest version of Ground Control and the Firmware  

2) Enter your machine's true dimensions

3) Follow the calibration testing instructions  [here in step #9](https://github.com/MaslowCNC/Mechanics/wiki/Using-the-Temporary-Frame-to-Cut-Parts#step-9-check-the-calibration)

---

Posted on **2017-04-20 17:37:13** by **rancher**:

I can do it tomorrow if it still needs done in the morning.

---

Posted on **2017-04-20 18:42:46** by **blsteinhauer88**:

Me too, Day Off To Play!

---

Posted on **2017-04-20 19:13:13** by **scottsm**:

I got good cuts with my 3306mm motor spacing and my 310mm sled.

---

Posted on **2017-04-20 19:30:06** by **Bar**:

Fantastic! That's great news. Thank you so much for testing it. 



165+ messages to get it tracked down, great work everyone!

---

Posted on **2017-04-21 07:23:55** by **scottsm**:

@Bar, is there a linear relationship between the sled measurement and the error? I'm going to tune up a difference of 0.024" today, about 0.61mm. Is this even the right place to tune?

From a different angle, what a difference your recent work has made! Here I am, chasing a half a millimeter... :) Exciting times...

---

Posted on **2017-04-21 07:47:47** by **Bar**:

It is exciting times! Don't give me too much credit, I just do what you guys tell me to :)



There is a relationship between the sled measurement and the amount of error, but I think it's very non-linear and I haven't determined what exactly the relationship is yet. @jbarchuck recommend last night that it would be great to have an option in Ground Control to enter the measured sizes of the test part and have it tell you what the right setting is. I've filed an issue for that idea, I think it's a great one.



Any insight you have about how the changes effect the outcome are more than welcome!

---

Posted on **2017-04-21 08:02:59** by **blsteinhauer88**:

I cutting test now.  I used the Master firmware and GC so I could enter exact measurements.  this is correct?

---

Posted on **2017-04-21 08:05:41** by **scottsm**:

Since this measurement is critical, how about putting up measured drawings of a starter sled and the finished sled with the important geometry called out? Accurate center marks for the chain bracket bolts, measured from each other and the router bit seem like important numbers to get right, since every user will need these numbers and success and satisfaction are so closely tied to them. Something along the lines of "drill these holes very carefully in your piece of wood" and the rest of the starter sled is more forgiving.

Much more detailed info (pictures) of _exactly_ how and where to make this measurement might help as well. 

Or a one-piece chain-attachment fixture with the measurement fixed instead of separate chain brackets? A piece of flat stock with the bracket holes to put onto the sled and locate the existing brackets? Bolt that to a piece of wood and success for the beginner is much closer...

---

Posted on **2017-04-21 08:17:17** by **Bar**:

@blsteinhauer88 Thank you so much for testing everything. The way you are doing it sounds perfect (master firmware, master GC)

---

Posted on **2017-04-21 08:21:15** by **Bar**:

@scottsm that's a great idea. I will post a picture with all of the dimensions for the starter sled. I really like the idea of a one piece bracket which would ensure that the dimension is perfect every time.



Ultimately I think we need to ship the sled with the machine. If we move the motors to mount on the sled and ship it, the whole assembly process will be so much easier. That's going to require a lot of design changes.

---

Posted on **2017-04-21 08:24:38** by **rancher**:

Bar, do we need to re measure chains?  Is the sequence set the settings, then measure?  Is that important?  What happens with measure then settings?  Or settings and no measure?

---

Posted on **2017-04-21 08:26:21** by **blsteinhauer88**:

I have painted my links.  There is a Manual Chain Cal that I use now and just set the painted links to their places.

---

Posted on **2017-04-21 08:27:02** by **rancher**:

Yeah, mine are chalked.  I was wondering if it changes with different settings.   No?

---

Posted on **2017-04-21 08:31:25** by **Bar**:

That's a great question. You shouldn't need to do a chain recalibration between changing settings values

---

Posted on **2017-04-21 08:32:06** by **Bar**:

You might want to click the arrow buttons a couple times to let the machine settle into it's new size of the change is a big one

---

Posted on **2017-04-21 08:33:17** by **Bar**:

The chain lengths are stored by a separate part of the program than the machine dimensions.

---

Posted on **2017-04-21 08:33:50** by **rancher**:

Thank you Bar.

---

Posted on **2017-04-21 08:51:45** by **blsteinhauer88**:

Well I am confirming sled mount measurement does make a difference, the 'set' sized mount is looking like a great idea!  So is @gero idea of the adjustable motor mount.  Sled width too wide, make square skinny.

---

Posted on **2017-04-21 08:54:21** by **blsteinhauer88**:

Down Pressure a God send, Depth are spot on to .001 ths of an inch.

---

Posted on **2017-04-21 09:05:00** by **Bar**:

How close to 6" are you guys seeing your test shapes come out?

---

Posted on **2017-04-21 09:24:14** by **blsteinhauer88**:

Started with:

circle H 3.541 w 3.4

Square h 6.103 w 5.891

After 4 adjustments of about 3-4 mm smaller distance 

circle h 3.472 and w 3.495



I think I'm pretty much there...

---

Posted on **2017-04-21 09:25:17** by **blsteinhauer88**:

square h 5.944 and w 6.008

---

Posted on **2017-04-21 09:27:28** by **blsteinhauer88**:

I notice it all got smaller my the hundreths place when I wien up 8 inches from the last cut.  Workspace coord.  x16 y13

---

Posted on **2017-04-21 09:30:42** by **blsteinhauer88**:

by the hundreths place on the height measurement and it had bee at the 3.5 mark all the other times for the circle.  The square was also smaller as i went up the workspace.  in the 6 inch for height ehtn dropped to 5.944.  Not much, just interesting.

---

Posted on **2017-04-21 09:33:11** by **Bar**:

Very cool!

---

Posted on **2017-04-21 09:33:28** by **Bar**:

Thank you so much for testing that!

---

Posted on **2017-04-21 09:33:52** by **blsteinhauer88**:

[IMG_0673](/images/pF/Zj/pFZj_img_0673.jpg.jpg) [IMG_0674](/images/dt/qu/dtqu_img_0674.jpg.jpg) [IMG_0675](/images/wv/iY/wviY_img_0675.jpg.jpg)

---

Posted on **2017-04-21 09:33:54** by **blsteinhauer88**:

Photos if you can read my chicken scratch!  You bet!

---

Posted on **2017-04-21 09:39:10** by **Bar**:

Beautiful!



That's a really good point about the size changing as a function of position. We should investigate that further. Maybe there is one part of the sheet where it is the most sensitive and we should recommend calibrating there, or maybe we need to do calibrations in multiple locations to get things 100% dialed in.

---

Posted on **2017-04-21 09:40:11** by **blsteinhauer88**:

I will leave my settings and try the center and 4 corners

---

Posted on **2017-04-21 10:23:44** by **davidlang**:

once we have the math properly figured out, any dimensions will work, as long as they are measured properly.



I think that trying to ship a sled would cause all sorts of grief (mounting for the different routers, shipping costs and sizes, etc)



the idea of a temporary sled template that you print out on letter/A4 paper (and then measure something on it to find out how much your printing process distorted it to fit it on the page) is a great one.



Now that the error in communicating the dimensions from the user software to the firmware has been fixed, can someone test with 'standard' machine dimensions, make sure they are getting an accurate test, and then move one of the motors substantially (a foot or something similarly extreme), enter the new machine dimensions and see if they still get an accurate cut?



After that, it would be wonderful to have someone do a study of how the four critical measurements affect the test pattern.



We have



1. the distance between the two motors



2. the distance between the two chains on the sled



3. the distance from where the chains conn ect down to the center of the router bit



4. the distance from where the chains connect down to the center of gravity of the sled.



around the center of the work area, #3 and #4 are not going to matter much, but at the edges (and I would guess especially the lower edges where the tension is the lowest on the chains) where the sled tilts more, the lower three measurements will matter a lot more.



we know that if the distance between the motors is wrong, the cuts get distorted vertically. I expect that if the other dimensions are too far off, the result is going to be that a stright line across the workspace isn't actually going to be straight, but we need either modeling, or someone experimenting to see exactly what happens. 



And it's faster for someone with a working machine to experiment than to build the model (and you still have to test the model against reality) :-)

---

Posted on **2017-04-21 10:37:23** by **rancher**:

My results are in.  My measurements are pretty much default, with the exception of height which for me is 450mm.  I can't measure motor distance in mm, but I moved mine to match the 9'91/4" the other day.  Bar, is it possible to make those settings selectable mm or in?  It's driving me crazy, still, after all this time.  I can deal though.



Okay, so my sled settings are the same.  I did three tests vertically, the center was close, one 4" below was a little off, one 8" above was way off.  By about half an inch.  None were good enough to build something.



Yesterday was better.

---

Posted on **2017-04-21 10:46:48** by **Bar**:

Hmmmm that's not great.



Making the units select-able is on my todo list. I think that the first step is to make the default that you don't measure it at all using a tape measure but instead string the chain from one sprocket to the other and the encoder measures the distance. That way we're all working from the exact same system.



Were you able to tweak the setting for the sled spacing based on the values in the guide and see improvements?

---

Posted on **2017-04-21 10:48:45** by **rancher**:

I didn't.  I didn't know what to do.  My measurements are actually exactly the defaults, since you dictated them to me when I built my first one.  I could have gone back to mindlessly changing settings, but I spent hours doing that this week already.  I didn't think it would help, but if it does, tell me what to do.

---

Posted on **2017-04-21 10:51:45** by **Bar**:

I agree that mindlessly changing things is not the way to go. We're working towards dialing in exactly what to change under what circumstances. If you tweak your results based the method described in step number 10 [here](https://github.com/MaslowCNC/Mechanics/wiki/Using-the-Temporary-Frame-to-Cut-Parts#step-10-check-the-calibration) do you see improvements?

---

Posted on **2017-04-21 10:57:23** by **rancher**:

I did not because the center positioned test was as close as I've gotten to correct, and the top one was way out.  I also do have a metric steel rule and I double checked my sled measurements, so I would have been moving towards incorrect settings.....I dunno.

---

Posted on **2017-04-21 10:58:27** by **Bar**:

Those are really good points

---

Posted on **2017-04-21 10:59:00** by **Bar**:

I'm working on testing getting everything dialed in at the center right now and then moving out to the edges to see how things change right now

---

Posted on **2017-04-21 11:11:21** by **blsteinhauer88**:

Here is an edge test! Not bad!!!  [IMG_0676](/images/Am/c9/Amc9_img_0676.jpg.jpg) [IMG_0677](/images/a3/D8/a3D8_img_0677.jpg.jpg) [IMG_0678](/images/dl/Te/dlTe_img_0678.jpg.jpg)

---

Posted on **2017-04-21 11:11:46** by **blsteinhauer88**:

Taller and thinner but good!😀

---

Posted on **2017-04-21 11:14:08** by **blsteinhauer88**:

Sorry, here is center... [IMG_0679](/images/oO/E4/oOE4_img_0679.jpg.jpg)

---

Posted on **2017-04-21 11:20:51** by **Bar**:

Not bad at all!

---

Posted on **2017-04-21 11:21:05** by **Bar**:

We're really getting there now!

---

Posted on **2017-04-21 11:22:51** by **Bar**:

I'm working on the same exact test right now

---

Posted on **2017-04-21 11:57:29** by **rancher**:

I went from bad to worse....



I was gonna leave it alone, but I had to go down and get the chicken feed.  I was thinking....maybe I was out, I skipped a tooth or something.  I hadn't measured or calibrated for the last three runs.



So, I set the chains on my chalk points, did "Manual Chain" and got the 1900mm pop-up.  Hit Home, Z retracts, and.....the sled takes off up, giant position circle.  It tried to tear itself apart again!  I had the position circle closed and the thing was at the top of the sheet, I hit down, it went up again.  



I'm back to loss of position, random UP, and sled tearing.

---

Posted on **2017-04-21 12:07:45** by **Bar**:

:-(

---

Posted on **2017-04-21 12:09:03** by **Bar**:

I'm ready to make figuring out what's going on my only goal for the rest of the day. We've got to get to the bottom of this.

---

Posted on **2017-04-21 12:10:02** by **Bar**:

What are all of your settings right now? Send a screen shot?

---

Posted on **2017-04-21 12:20:06** by **rancher**:

My settings are default except V offset is 450.

---

Posted on **2017-04-21 12:20:18** by **Bar**:

For dialing things in with the test shape I recommend moving down and diagonally with each test. That way it's easy to track your progress and it uses minimal material like  [this](/images/np/WH/npWH_img_20170421_121522123_hdr.jpg.jpg)

---

Posted on **2017-04-21 12:20:39** by **Bar**:

@rancher Ok, I'm going to make mine match

---

Posted on **2017-04-21 12:22:17** by **blsteinhauer88**:

Lower right weird!! [IMG_0681](/images/rH/xk/rHxk_img_0681.jpg.jpg) [IMG_0682](/images/Lq/5u/Lq5u_img_0682.jpg.jpg)

---

Posted on **2017-04-21 12:22:18** by **blsteinhauer88**:

Get rancher going tho!

---

Posted on **2017-04-21 12:24:07** by **Bar**:

That is a strange shape. I was able to replicate your results in the top corner, but I haven't tried the bottom corner yet.

---

Posted on **2017-04-21 12:24:52** by **Bar**:

@rancher I'm going to do a manual chain length calibration to see if I can replicate what you saw

---

Posted on **2017-04-21 12:35:02** by **Bar**:

I saw the same thing which is great news, because that means that I will be able to track down what's happening.



Here's what I did to make it happen. I moved the sled to the very top right corner, then powered everything off, then reset the chains manually to the center, then clicked "calibrate chain lengths - manual", saw the popup (which is a bug because the machine wasn't plugged in yet, it shouldn't say it's done it until the command has been sent and processed), then clicked one of the arrow keys and the sled tried to go off the top. 



I don't know what the cause is yet. I'll keep you posted as I investigate.

---

Posted on **2017-04-21 12:37:24** by **rancher**:

I was so sure it was me again.  Dude.  Thank you.

---

Posted on **2017-04-21 12:42:30** by **Bar**:

It's never you! Whenever something isn't working the way you expect it to it's either because the instructions weren't clear enough, the design isn't intuitive enough, or something is broken. The best way to fix any of those problems is to let me know that it needs to be better, so thank YOU for finding the problem!

---

Posted on **2017-04-21 12:48:59** by **Bar**:

The marks on your chains, how far from where the sled mounts to the chain are they? I want to replicate everything as exactly as I can.

---

Posted on **2017-04-21 12:52:23** by **rancher**:

I don't know.  I used "measure chains-auto" when I first marked them.  I'm not down there now, but I imagine they are whatever they are supposed to be.

---

Posted on **2017-04-21 12:53:55** by **Bar**:

Perfect, that's all I needed to know :-)

---

Posted on **2017-04-21 12:59:34** by **davidlang**:

@blsteinhauer88

for that error in the bottom right, I'll bet it was cutting the bottom before the right side and the sled stuck instead of sliding, then when it started pulling up on the side, it moved, resulting in that rounded corner

---

Posted on **2017-04-21 13:16:17** by **Bar**:

@rancher I think I've got it worked out, give me a few minutes to clean everything up and let's test it?



Are you running Ground Control from the source or from the compiled version?

---

Posted on **2017-04-21 13:20:13** by **blsteinhauer88**:

@davidlang you may be right.  I was watching the bit when it did that and did not pay attention to see if the sled was catching...Thanks I will watch for that on another test.

---

Posted on **2017-04-21 13:23:54** by **rancher**:

Bar, I just delete the GC folder each time, put the new one in the computer, and double click main.py.  Don't hurry on my part, I may not get back to the machine today, and I sure don't need to.  That said, I could go test if you needed it done.

---

Posted on **2017-04-21 13:36:00** by **Bar**:

@rancher

That's perfect. 



I think I've fixed the problem which you saw where the sled was running away. The short version is that it was possible to see the "chain lengths calibrated" window without the lengths having been actually updated, but it isn't anymore. 



Getting you up and fully calibrated is my *top* priority right now, I think we can get everything worked out if we go through everything on our machines at the same time. I can do it now or any other time, just let me know when.



When you do go back to the machine I would recommend these steps:

1) Take the latest version of the firmware and Ground Control

2) Run the automatic chain length calibration at least one more time just because it's the most tested method

3) Give the method of cutting the test shape and tweaking the setting for sled mounting points a try. I know it seems wrong to mess with a length that you measured carefully, but it seems to work. Maybe there is something we don't yet understan d at play like the last link in the chain isn't bending. Adding 11mm to mine made all the difference in the world.



I really think that if we go through it at the same time we can figure out what's up

---

Posted on **2017-04-21 13:37:57** by **rancher**:

Okay, I can do another test.  Is there new firmware and GC since yesterday?  I grabbed the latest this morning.

---

Posted on **2017-04-21 13:38:27** by **rancher**:

Oh, I see it.

---

Posted on **2017-04-21 13:39:21** by **Bar**:

Fantastic! Let's get things worked out!

---

Posted on **2017-04-21 13:40:52** by **Bar**:

I'm going to do everything at the same time. If we see different results, we'll know that's where something has gone wrong

---

Posted on **2017-04-21 13:42:18** by **rancher**:

Okay, so....how do you want me to test exactly?  From center?

---

Posted on **2017-04-21 13:42:47** by **Bar**:

You are going to loose internet when you go to the machine, right?

---

Posted on **2017-04-21 13:42:57** by **rancher**:

Yeah.

---

Posted on **2017-04-21 13:43:46** by **Bar**:

Hmmm, let me think for a second about what the best way to do things is

---

Posted on **2017-04-21 13:44:29** by **Bar**:

I think we want to have really clear steps ahead of time

---

Posted on **2017-04-21 13:45:15** by **Bar**:

What if I take notes on exactly what I do, and if you read along with them, then if you see different behavior at any point we'll know that's where things went wrong?

---

Posted on **2017-04-21 13:45:44** by **rancher**:

[IMG_1452](/images/T4/2x/T42x_img_1452.jpg.jpg) 



I go down there.

---

Posted on **2017-04-21 13:45:45** by **rancher**:

That works.

---

Posted on **2017-04-21 13:46:20** by **Bar**:

What a beautiful place

---

Posted on **2017-04-21 13:48:03** by **Bar**:

I'm starting to write up my process now, it might take me 10 or 15 minutes to have everything written up

---

Posted on **2017-04-21 13:48:35** by **rancher**:

Take your time.

---

Posted on **2017-04-21 14:23:29** by **Bar**:

Here are the steps I followed: 



1)Upload the latest firmware by clicking the upload firmware button in GC

2) Hook the first link of each chain on the sprocket tooth at 12:00

3) Launch the latest version of Ground Control

4) Click *Actions -> Calibrate Chain Lengths - Automatic*

5) The terminal in GC will say "Measuring out left chain" and the left sprocket will start to turn. When it finishes the length "1650.xx" mm will be added below. The xx may be any decimal. This number is the exact length of chain measured out, the decimal value isn't particularly important as long as the system knows what it is.

6) The same process will repeat on the right

7) Attach the sled

8) Click the left arrow once and then the right arrow once. This will let the machine adjust the chain lengths to put the machine in the center. You may see the position error circle shrink, but it should correct quickly and not try to run off the top or anything crazy like that.

9) Enter all the settings values as best you measure them

10) Open the test shape

11) Run the test shape

12) Measure it, ignore the  circle part and just focus on the square part because it's much easier to measure

13) Adjust the distance between sled mounting points as described on the wiki page. I did 5mm steps at first, then 1mm steps to dial it in

14) Return the sled to the start by clicking the "Home" button

15) Move it down and right by 3/4 of an inch and click define origin to move the shape over. This will save you from using a ton of wood to dial it in

16) Repeat 11-16 until the test shape comes out square



Let me know how it goes, if it goes. Best case scenario this method works for you. Worst case scenario, it doesn't work at all, but at least we'll have a good repeatable set of conditions to try to figure out what went wrong.

---

Posted on **2017-04-21 14:26:08** by **Bar**:

Things to take with you would be latest firmware/software, the text here and a copy of the picture from the wiki page [here](https://github.com/MaslowCNC/Mechanics/wiki/Using-the-Temporary-Frame-to-Cut-Parts#step-10-check-the-calibration) showing which way to adjust.

---

Posted on **2017-04-21 14:27:14** by **Bar**:

Thank you so much for being willing to give it a go. Best case we can get things worked out, worst case I'll have a better understanding of where to start fixing things.

---

Posted on **2017-04-21 14:28:34** by **rancher**:

Thanks for all of your hard work Bar.  I'm on my way down now.

---

Posted on **2017-04-21 14:30:05** by **Bar**:

Thank you!

---

Posted on **2017-04-21 14:36:53** by **Bar**:

I want to call an issue to everyone's attention that I just found which could trip us up. Because the settings are sent to the machine when GC is first launched, if you unplug the machine, don't close GC, plug the machine back in the machine has lost track of it's settings, but GC doesn't send them again.



I think the proper solution is that the machine should store it's settings in the EEPROM. That way each machine "knows" it's own dimensions.



I'm hesitant to start digging into it until we've got everyone up and running as is. It seems like were so close to having things work the way they are that I don't want to throw everything into chaos again by breaking something. This change would be a pretty big one in terms of how things are done, so I want to wait until after the Wednesday release.



Let's keep this issue in mind to make sure it's not tripping us up. 



I've made an issue for it [here](https://github.com/MaslowCNC/Firmware/issues/183)

---

Posted on **2017-04-21 14:45:48** by **Bar**:

I've updated Ground Control so that the settings are sent to the machine again when it reconnects.

---

Posted on **2017-04-21 14:47:35** by **Bar**:

I am going to leave the issue open, because I think storing the settings on the machine is really the right approach. I'm imaging issues where one machine is controlling two machines or where two different computers are controlling the same machine but sending different settings.

---

Posted on **2017-04-21 15:21:43** by **blsteinhauer88**:

That explained a lot of runaways!!!!!!!!

---

Posted on **2017-04-21 16:23:29** by **rancher**:

Okay,  here we go....

Center cut was pretty dang great.

 [IMG_3785](/images/ms/A0/msA0_img_3785.jpg.jpg) [IMG_3787](/images/YX/qM/YXqM_img_3787.jpg.jpg) [IMG_3788](/images/fp/dU/fpdU_img_3788.jpg.jpg)



Then I went up 8 inches and tried again.

[Upper y](/images/Ye/Ap/YeAp_uppery.jpg.jpg) 



And changed sled width wider by 3, then 6.  Same results.  Not too bad, but it didn't get any better.  Have you guys tried one up high center?

 [IMG_3796](/images/zA/hH/zAhH_img_3796.jpg.jpg) 



The new flock hit the pond for the first time while I cut.

 [IMG_3801](/images/Ee/97/Ee97_img_3801.jpg.jpg)

---

Posted on **2017-04-21 16:24:40** by **rancher**:

I also started with a crazy Z runaway.  I was cutting, 3/4 of the way through the circle, when things started sounding wrong.  The Z was grinding away and the router was buried and smoking.  It was like the other runaways, but Z.  That was not a good start.

---

Posted on **2017-04-21 16:29:20** by **Bar**:

It seems like z-run away might be the next thing on my to fix list.



Overall that feel like we made some progress. We still have some room to improve, but I think we're getting there.



My experience was that the higher you go, the more any error is exaggerated. That makes sense because high and in the center is where the chains have to move the least to move the sled a given distance. I haven't tried high and in the center yet, but I will right now.



Maybe we should recommend running the calibration in the middle towards the top, that way if it looks good there it will look good everywhere?

---

Posted on **2017-04-21 16:30:03** by **Bar**:

Thank you again for trying that. I feel good that the avenue that we're moving down is a good one.

---

Posted on **2017-04-21 16:30:34** by **Bar**:

What kind of birds are those? I don't think we have them here.

---

Posted on **2017-04-21 16:31:41** by **rancher**:

No problem.  I wasn't able to get it close enough for me at that location.  I am hoping you will try calibrating there, or BLS, or someone.  Show me it's possible!  My measurements remained the same throughout on that upper cut.



Muscovey Ducks, straight out of Hadlock!

---

Posted on **2017-04-21 16:32:59** by **rancher**:

I mean, I bought them from a farm in PH.  They are a popular farm breed.  Good layers, mothers, and good eatin'.

---

Posted on **2017-04-21 16:34:50** by **gero**:

Thumbs up for this exceptional collaboration!

Will throw this in and if it is is only good for laughter, it still had a good purpose.

I wasted the entire night confusing ‘define origin’ with ‘Set Home’.

For me ‘Home’ is the centre of the sheet from where I would like to start all tests.

After chain and motor calibration.

Am I missing the ‘Set Home’ button? Since my sled chain mounts are closer to the cutter (I might even turn them to get more close to the cutter), after chain calibration, I am in the middle horizontal and above centre vertical. With the original mounting, is the sled at the centre of the sheet? [Home](/images/qj/aK/qjaK_home.jpg.jpg)

---

Posted on **2017-04-21 16:36:35** by **Bar**:

I think that's a GREAT point. Anyone opposed to renaming the "Define Origin" button to "Set Home"?

---

Posted on **2017-04-21 16:37:00** by **rancher**:

I have been hoping for both define and return to center, or whatever.

---

Posted on **2017-04-21 16:37:28** by **rancher**:

Also, the transport buttons are worthless and scary for me.  Is it just me?  Can others skip ahead and just do the square?

---

Posted on **2017-04-21 16:37:46** by **gero**:

I don't think it is that right now

---

Posted on **2017-04-21 16:39:21** by **Bar**:

Right now the behavior is that clicking "Home" takes you back to wherever the "Define Origin" button was last clicked so calling it "Set Home" makes sense.



There is a "Return To Center" button under "Actions" which will always return the machine to the center of the sheet.



Is this the behavior we want?

---

Posted on **2017-04-21 16:40:09** by **gero**:

Set center is what I am looking for

---

Posted on **2017-04-21 16:41:07** by **Bar**:

There is no "define the center of the sheet" button right now. I had one in the past, but I found that it lead to wonky cut's because actually finding the perfect center and getting the machine lined perfectly with that point is hard enough that I could never do it consistently.



What is the situation where you are looking for that button?

---

Posted on **2017-04-21 16:45:48** by **gero**:

I moved the sled to my personal center and, then moving left or right I first had the sled go down. Confirmed that 3 time. Always after "define  Origin" and closing and opening ground control. Other tests then moved the sled up.... After chain calibration and closing and opening GC. I think the software does not know where my home is.

---

Posted on **2017-04-21 16:45:54** by **rancher**:

When I'm finished cutting off center somewhere and am wanting to send it to the center out of the way and ready for the next job.

---

Posted on **2017-04-21 16:46:52** by **Bar**:

@rancher the button you are looking for is *Actions -> Return To Center*

---

Posted on **2017-04-21 16:47:30** by **Bar**:

@gero that's an interesting issue

---

Posted on **2017-04-21 16:47:57** by **rancher**:

Yes, yes it is!  Thank you.

---

Posted on **2017-04-21 16:48:58** by **gero**:

will create a detailed structured test in the morning of the steps, tonight is wasted and I am too :-)

---

Posted on **2017-04-21 16:49:54** by **Bar**:

@gero that sounds like something I want to look into further. Thank you. If you will make a structured test and put it in an issue, I will pursue it and find out what is going on

---

Posted on **2017-04-21 16:52:21** by **gero**:

that the sled sacked down by only clicking right, with the software telling me that Y is 0 is what prevented me to cut my 6th test pattern

---

Posted on **2017-04-21 16:53:09** by **MakerMark**:

Took 8 cuts to get mine dialed-in to within 1/64th on x and y. I'm stopping there to finish cutting out a project that I need to complete by tomorrow. Great job guys!

---

Posted on **2017-04-21 16:57:58** by **gero**:

From which point does the math start its work and how is that defined?

---

Posted on **2017-04-21 17:00:08** by **Bar**:

Good question, I'm not entirely sure I understand. Do you mean under what circumstances is the math controlling the machine's position?

---

Posted on **2017-04-21 17:02:12** by **gero**:

From which origin. The structure of the design lets me think it started from the center of the cutting sheet.

---

Posted on **2017-04-21 17:03:03** by **Bar**:

Oh, I understand! Yes. The center of the sheet is the point (0,0) for the internal math

---

Posted on **2017-04-21 17:03:37** by **Bar**:

The digital position readout on the right hand side is always displaying the position as understood by the internal math

---

Posted on **2017-04-21 17:04:47** by **Bar**:

Where that point is located is defined by 1/2 the distance between the motors, and then down 1/2 of the specified work area + the y motor offset in the settings

---

Posted on **2017-04-21 17:05:49** by **gero**:

as far as i see it i don't have the option to tell where 0,0 is

---

Posted on **2017-04-21 17:06:13** by **gero**:

Oh, I will measure that :-)

---

Posted on **2017-04-21 17:06:35** by **Bar**:

:-)

---

Posted on **2017-04-21 17:07:50** by **Bar**:

I would update to the latest version of Ground Control before doing any tests, I fixed a bug today which was causing the machine to forget it's settings if it was unplugged and re-plugged without reopening GC which could possible have effects similar to what you are describing

---

Posted on **2017-04-21 17:09:49** by **gero**:

shutting down the laptop is like unplugging i guess, but after boot today came firmware and GC update

---

Posted on **2017-04-21 17:11:13** by **Bar**:

I think it happened any time the arduino lost power which could be when closing the computer. I didn't catch the bug until about 4pm so it was a late in the day fix, might still be worth updating

---

Posted on **2017-04-21 17:13:20** by **gero**:

today is relative :-), there is some huge time gap between our locations, hopefully more tomorrow and thanks for this amazing machine!

---

Posted on **2017-04-21 17:17:58** by **Bar**:

That's a great point! Haha I hadn't thought of the fact that we might be in different days. Two hours prior to now :-)



You are more than welcome. Thank you guys for making it work. Getting to build this project has been one of the coolest, most rewarding, most exhausting, and most exciting things I've ever done. I could never do it without everyone here's help.

---

Posted on **2017-04-21 19:16:35** by **blsteinhauer88**:

I vote for "Set Home" also.

---

Posted on **2017-04-21 19:18:05** by **blsteinhauer88**:

I have pushed the home button a couple times today and it went home after a stop, at the depth of the last cut.  It then reset to the safety height after it got there, then back to zero.  Glitch?

---

Posted on **2017-04-21 19:46:12** by **Bar**:

That sounds like a glitch

---

Posted on **2017-04-21 19:46:34** by **Bar**:

I will look into it

---

Posted on **2017-04-21 19:48:03** by **MakerMark**:

How about icons instead of words?  [SetHome](/images/EZ/VO/EZVO_sethome.png.jpg)

---

Posted on **2017-04-21 20:07:23** by **carlosrivers**:

I think Words are probably better. Some of this stuff is already too confusing.

---

Posted on **2017-04-21 20:30:38** by **Bar**:

Slick icon tho! I think at some point once we've got all the genuine issues locked down we're going to want to do a whole UI review to make everything look pretty. Let's not forget about that idea.

---

Posted on **2017-04-21 23:14:34** by **scottsm**:

While we're discussing 'Home' and 'Return to Center', it sure is inconvenient that the 'Return to Center' zeroes the z-axis before traversing. I have to remember to unlatch and lift the router before using that useful command. Best would be to lift the z as the 'Home' button does, or at least leave the z alone until the x and y travel are complete before landing the bit.

---

Posted on **2017-04-22 00:19:29** by **scottsm**:

I put in a PR to have 'Return to Center" lift z before traversing.

---

Posted on **2017-04-22 00:30:54** by **gero**:

Waking up this morning I was hoping that it was the wine that got me confused last night. After the second coffee and rereading the last quarter of this thread this morning, I am still confused.

Home, define origin, return to center, Set Home...

Where is center and does it stay there for the math?

Let's say the standard Maslow has the cutter at the center of the sheet after calibrations.

All math is calculated from that point 0,0. Now I want to cut a square  10 x 10 in the lower left from the center.

I move the sled to X-10 and Y-10. Then I click 'Define Origin'. I see X and Y are zero now, but does the software still know that I am at X-10 and Y-10 for the math?

Define Origin has it's great job of showing me where on the sheet I am about to cut and the origin of my part and path, but it should not tell the software to do the math from this point, or am I wrong?

Home should bring the cutter to 'Origin' if it was defined, if not Home and Center are the same, 'Retur n to Center' should bring it back to the center of the sheet, no matter on which part of the sheet I clicked 'Define Origin' right?

---

Posted on **2017-04-22 06:53:30** by **rancher**:

> @gero

> Home should bring the cutter to ‘Origin’ if it was defined, if not Home and Center are the same, ‘Retur n to Center’ should bring it back to the center of the sheet, no matter on which part of the sheet I clicked ‘Define Origin’ right?



This is correct Gero.

---

Posted on **2017-04-22 09:01:21** by **gero**:

Did all from Bar’s list except ‘1)Upload the latest firmware by clicking the upload firmware button in GC’ (Can’t find that so I used Aruino IDE).

On ‘8) Click the left arrow once’ the sled sacked down, moved left and went down again, without any changes of X on the screen . After chain calibration I am above the real center of the sheet because my chain brackets are closer to the cutter. I think the software was already trying to get me to my center, but was now a bit to low. I was surprised to find all my settings. After cutting 6 shapes dialing in, a ‘Return to center’ surprised me by bringing the sled spot on where the center of my sheet is. I confirmed a second perfect 6 inch square, but with a 6mm cutter, so scale might be off.

So what is next? Find the second parameter that produces ellipsis and then tweak both to get the dimensions right?

---

Posted on **2017-04-22 09:02:51** by **Bar**:

Good catch gero! That's a typo for upload the latest firmware

---

Posted on **2017-04-22 09:04:00** by **Bar**:

That sounds like some good progress gero! Great work!

---

Posted on **2017-04-22 09:05:04** by **Bar**:

@scottsm is to thank for making the settings stay when you update GC, hopefully from now on they'll just be there

---

Posted on **2017-04-22 09:06:28** by **Bar**:

I'm not sure what the second parameter is, do you mean you are getting perfect squares, but the circle inside the square is still an ellipse?

---

Posted on **2017-04-22 09:11:52** by **gero**:

No, I am measuring 6inch but with a 6mm cutter, if I had your cutter which I think is 6.33mm I would have a square slightly under 6inch, right?

---

Posted on **2017-04-22 09:14:46** by **Bar**:

Oh, got it so it's a perfect square it seems like it's slightly too big

---

Posted on **2017-04-22 09:17:54** by **Bar**:

I would recommend regenerating the test shape gcode for a 6mm cutter using the .Svg in the same folder before reading into it too much

---

Posted on **2017-04-22 09:18:34** by **Bar**:

I agree that I would expect the shape to be .33mm less, but sometimes those things are counter intuitive

---

Posted on **2017-04-22 09:20:42** by **Bar**:

That .33 mm is also less than the 1/64th inch accuracy that we're targeting. I think it's possible to do better than our target accuracy, but still good job for hitting the target!

---

Posted on **2017-04-22 09:27:27** by **gero**:

The mm file is exactly what I am going to try. Back to my cad/cam issues :-). I will get it one day. I have received now following collets 1/4', 1/2', 6mm, 8mm. I can now go crazy ordering cutters. The tools I could find for the original 12mm collet are perhaps good for cutting Owl-holes into tree trunks...

---

Posted on **2017-04-22 09:36:45** by **Bar**:

Hahaha, yeah that's a big bit

---

Posted on **2017-04-22 09:38:16** by **Bar**:

If you still see a square which is bigger in all dimensions, I wonder if playing with the motor spacing would help?

---

Posted on **2017-04-22 10:59:32** by **Bar**:

My guess is that the distortion we're seeing is a percentage of the size of the object.



Should we be testing with a large shape say a 2 foot by 2 foot square? It might be easier to really dial everything in that way.

---

Posted on **2017-04-22 21:17:19** by **davidlang**:

I think in this case a sanity check with say a 3" square (since that can be measured with the calipers) and possibly a very large square (2' or 3' a side) would be useful. If we are off by the same fraction of a mm on all of them, we can say it's stable (other than checking if cutting on the edges works or not)



if the g-code is set up for a 6.25mm (1/4") bit, and you use a 6mm bit, the part should be oversized in all directions by 0.25mm (the radius difference * 2, which also equals the diameter difference)., which is ~0.005" with the target goal of 1/64" being 0.015", so this is well within the margin of error, and I think should be considered 'good enough' at least for now (until the new control loops are implemented)



But the biggest problem we've been fighting has been the vertical movement not matching the horizontal movement.



so do you have similar accuracy at the corners of the workpiece?

---

Posted on **2017-04-24 04:22:50** by **gero**:

I had 0.5mm off on left up and left down, but with ridiculous slow speed.

After the quick fix I was 1mm off on right up and right down with F450. Wondering if it was the speed. With my own 100mm x 100mm square and hand written gcode. No 'I' or 'J', pure X and Y moves. I want to use my caliper and that does not go 6'. This is the plan for tonight.  [Testpattern](/images/5H/SA/5HSA_testpattern.jpg.jpg)  Just a rough sketch, the .nc will have exact distances for the squares.

Handwritten code in a spread sheet, exported to .csv, so not only the squares can be compared, also the distance between them.

---

Posted on **2017-04-24 04:23:52** by **gero**:

Wondering if I should return to center after each square, or just cut all in one go.

---

Posted on **2017-04-24 04:29:31** by **davidlang**:

in theory it doesn't matter, but you know theory vs practice :-)



I would have it return to center and do a quick cut down into the wood. If you see this center hole growing, you know that the maslow is loosing track of where it really is.

---

Posted on **2017-04-24 04:40:52** by **gero**:

Great idea to add 15 Z-Down and up. I could still do it in one file by adding X0 Y0 between each cut, right? Or does 'Return to center do anything else then scratching over my workpiece ;-) ?

---

Posted on **2017-04-24 05:12:30** by **davidlang**:

I would move Z up before doing the xy move.



but return to center should not do anything else

---

Posted on **2017-04-24 08:25:21** by **scottsm**:

'Return to Center' goes to X0,Y0,Z0 . I've put in a PR to have it lift z before traversing and not drop z until it arrives, but that's not quite ready yet. For now, I try to remember to unlatch and lift the router before using 'Return to Center'. Adding Zup, X0 Y0, Zdown between each cut like you suggest seems good to me.

---

Posted on **2017-04-24 08:40:47** by **Bar**:

Adding a X0 Y0 would bring it back to the center, that's really all "Return To Center" does :-)

---

Posted on **2017-04-24 08:43:04** by **Bar**:

Awesome work writing all that gcode by hand! I saw your post yesterday about generating gcode still being confusing and I made a new wiki page [here](https://github.com/MaslowCNC/GroundControl/wiki/Generating-G-Code-Using-www.MakerCAM.com) in the hopes of clarifying it for others. Let me know how it could be better.

---

Posted on **2017-04-26 02:45:26** by **gero**:

Sorry that I need to keep you waiting for the report, but I need to sit back and enjoy this picture for a while  [IMAG0672](/images/5U/Ds/5UDs_imag0672.jpg.jpg) 

The center hole is drilled 16 times  [IMAG0673](/images/lS/Vo/lSVo_imag0673.jpg.jpg) and measures 6.5 mm, it's a 6mm cutter! I am not measuring the squares and distances between them now, because I am to drunk of happiness right now.

---

Posted on **2017-04-26 03:03:10** by **gero**:

@Bar, for my test pattern I wanted clear dimensions and distances.

A 100 x 100 square in mm in partcam gives me code like this:

G1 X100.18274111675127 Y-2.868020304568528 F1500

G3 X103.18274111675126 Y0.1319796954314721 I0 J3

G1 X103.18274111675126 Y100.13197969543148

G3 X100.18274111675127 Y103.13197969543147 I-3 J0

G1 X0.18274111675126906 Y103.13197969543147

Why if working with mm would I need 17 digits after the point and why are those numbers so cryptic? Am sure there are CNC's that can operate within those parameters, my guess is the Maslow can work with less.

My gcode made with a spread sheet, is something I can read:

G0X0Y0

G1Z-3F300

G1Z3F300

G0X-53Y-53

G1Z-3F300

G1X53Y-53F500

G1X53Y53F500

G1X-53Y53F500

G1X-53Y-53F500

G1Z3F300

Hope that makes sense.

---

Posted on **2017-04-26 03:57:23** by **gero**:

@Bar, The Wiki is very clear and easy to follow. Nice work! For building stuff, a very good starting point and am going to use it. I am not going to write gcode by hand to build my rocking chair. :-) Was just for dialing in.

---

Posted on **2017-04-26 06:52:14** by **MakerMark**:

@gero Congratulations on your setup! I'd like to know how many bottles of wine the project required? Thanks for sharing the pics and your trials along the way. I'm sure your feedback will help others to finish more quickly and save more drinks for celebrating after dialing in their machine.

---

Posted on **2017-04-26 07:06:22** by **Bar**:

That is fantastic news @gero! Great work! Thank you for sharing.



What an awesome thing to wake up to.



Would it be ok for me to put that picture in the email update today and give you credit for figuring out the method of tweaking the settings based on the test shape dimensions that has gotten us so far in the last few days?

---

Posted on **2017-04-26 08:42:40** by **gero**:

Take anything, going to measure the truth now :-)

---

Posted on **2017-04-26 10:18:04** by **TomTheWhittler**:

"Take anything, going to measure the truth now )"

Is that one glass or two ;)

---

Posted on **2017-04-26 10:19:30** by **TheRiflesSpiral**:

So is it possible to boil down these 331 messages into a best practices checklist? :D

---

Posted on **2017-04-26 10:20:40** by **TomTheWhittler**:

" best practices checklist? "

That would be awesome.

---

Posted on **2017-04-26 10:21:38** by **Bar**:

Yes! Even better, I'm building a wizard which where you do what it says on the screen then click "next" until everything is dialed in. It won't be ready for today's release, but hopefully in the next few days I'll have something we can all play with.



I'm not sure that the wizard fully replaces the "best practices checklist", we'll still probably want one of those. Wiki page?

---

Posted on **2017-04-26 10:39:47** by **TheRiflesSpiral**:

Automation! I love it. I think a best practices checklist would be great... the beta testers have contributed so much and if their collective knowledge were gathered somewhere (other than here) it will make life easier for your other users for sure!

---

Posted on **2017-04-26 12:02:17** by **gero**:

After cutting the pattern, I ordered Booze. No need to explain what happed after :-).  [IMAG0675](/images/S5/ed/S5ed_imag0675.jpg.jpg)

---

Posted on **2017-04-26 12:08:09** by **gero**:

I discontinued to take the distances. Because they are from the sides of the cuts. Not taking into account the variation of the squares. Should have drilled a center hole in each square. Will do that in the morning.

I think I tried to make a point that if we compare results, they should be under comparable conditions. Comparing squares on different parts of the sheet is comparing apples to oranges.

---

Posted on **2017-04-26 12:09:25** by **gero**:

The image has the center of the squares as reference. The cuts in the gcode are -53 or + 53 from there.

---

Posted on **2017-04-26 12:12:30** by **gero**:

There are so many things that I discovered, but it will take me the morning to sum them up. I have told my boss I need Maslow holidays and he gave me three days, so after the second coffee in the morning, stay tuned for more.

---

Posted on **2017-04-26 12:16:48** by **Bar**:

Beautiful! Fantastic work. I can't thank you enough for everything you are doing. 



I agree that we should have set coordinates at which to run the test file when we want to compare.



I'm seeing some clear patterns in the drift looking at one dimension from left to right or top to bottom which is exciting. I think that we can use that pattern to dial things in further. I'm eagerly awaiting your full debrief. 



Awesome.

---

Posted on **2017-04-26 12:20:59** by **gero**:

9 out of 15 squares within a mm is the result of all the amazing team, not mine.

---

Posted on **2017-04-26 12:24:45** by **TomTheWhittler**:

Bar, Gero, TheRiflesSpiral, rexklein and all the rest of the Beta testers (and some non-Beta as well) I wish to convey a whole heartily "THANK YOU" so all the tremendous work you are doing. I only wish I had not gone the cheap route and gotten the non-Beta MaslowCNCt as I would be having fun with this along with you. This has got to be one of the most awesomely supported Kickstarters that I have ever backed. Thanks to you all I will be able to jump into creating projects instead of having to fix bugs. Although fixing bugs can be challenging and fun in its own way.

---

Posted on **2017-04-26 12:24:51** by **Bar**:

Yes, I am continually overwhelmed by the amazing people in the community. I don't know what I ever did to get such an amazing group of beta testers, but we're the luckiest project there is. Thank you everyone!

---

Posted on **2017-04-26 12:27:22** by **davidlang**:

Thanks for doing this. This gives us much more information than we had before on the variability across the workpiece.



I think that this will improve when Bar gets time to implement the two-stage controller, but I think we also need to look very closely at the modeling in the firmware to make sure that it's matching the physical layout.

---

Posted on **2017-04-26 12:38:03** by **gero**:

After faking my distance of the motor mount on the sled, I am not in MY center of the worksheet anymore. It was very accurate before. Brings me back to the point where I would like to stet MY home, X0Y0, and let the math go from there.

---

Posted on **2017-04-26 12:40:00** by **gero**:

chain mount that is.. tzzzz

---

Posted on **2017-04-26 12:41:39** by **Bar**:

I've made an issue to add that button [here](https://github.com/MaslowCNC/GroundControl/issues/231), does the description in the issue describe describe the ideal behavior correctly?

---

Posted on **2017-04-26 12:42:53** by **gero**:

i put a thumb up on that one, fantastic

---

Posted on **2017-04-26 12:44:50** by **gero**:

with the chain calibration and the measurements put into GC, plus where home is, could be something.

---

Posted on **2017-04-26 12:49:27** by **gero**:

I have off until Monday. I you want me to cut, change settings or so let me know.

---

Posted on **2017-04-26 15:10:11** by **scottsm**:

Maslow holidays - I like it! An important job benefit, that is benefitting us all :)

---

Posted on **2017-04-28 08:36:19** by **blsteinhauer88**:

So I cut that 24 inch circle for the logo and it was a half inch taller than it was wide. If we do test circles and I was in a small margin of error how can we keep that small margin as we Make the part bigger?

---

Posted on **2017-04-28 08:38:07** by **blsteinhauer88**:

And that was cut about center sheet of ply.

---

Posted on **2017-04-28 09:06:24** by **Bar**:

I think that we might need a small test shape (6 in) to get things started, then a bigger test shape (3'?) To get things really dialed in. What does everyone think?

---

Posted on **2017-04-28 09:08:35** by **blsteinhauer88**:

I will run a 3foot square with 2.5 circle

---

Posted on **2017-04-28 10:44:51** by **blsteinhauer88**:

OK my 3 ft  Square was 36.2 inches wide and 35.75 tall.  The circle was a 30 inch circle and it up 30.1 inches wide and 29.75 tall .  My regular sized test pattern was wide by 1/16 of an inch.  The one 16th turned into .25 inch at six times the size  if that math is right.

---

Posted on **2017-04-28 11:08:10** by **scottsm**:

That suggests that the error scales, so we can use larger test patterns to dial in accuracy.

---

Posted on **2017-04-28 12:05:40** by **davidlang**:

I'll point out that we don't have to cut full squares to dial things in. We could cut small lines (say a 1/2"-3/4" or so long to fit the hook of a tape measure) horizontally and vertically, then shift a bit for the next set. We will just need to fix the control loops so that we can cut over the whole work area a bit more accurately than we do now.



let me think about this a bit and try to come up with suitable g-code

---

Posted on **2017-04-28 12:13:31** by **scottsm**:

Great idea - that will save a lot of material!

---

Posted on **2017-04-28 12:27:59** by **Bar**:

That is a fantastic point!

---

Posted on **2017-04-28 14:21:39** by **davidlang**:

could someone test the file http://lang.hm/maslow/testpattern2.nc



If I have it right, it should move up and left ~18", cut a slot, move down ~3' cut another slot, move up to the right, cut a vertical slot, move left, cut a fourth slot, then move left further to get out of the way and prompt for a tool change



This should let you measure the distance between the slots (900mm in each direction, not counting tool diameter) 



After you do the tool change (and potentially tweak the system dimensions), you tell it that you've changed the tool and it will repeat the cuts, offset slightly both horizontally and vertically.



I decided to do this in metric because everyone's tape measure will have mm on it, and I think it's going to be easier to read and enter accurate mm than inches and fractions.



If this works, I can trivially extend it to repeat several more times and will be looking at other improvements (making it handle cutter dimensions, etc)

---

Posted on **2017-04-28 15:26:29** by **scottsm**:

I can do this, what bit size? I've got 1/8" or 1/4" handy...

---

Posted on **2017-04-28 15:43:15** by **scottsm**:

davidlang, I bailed out because it looks to me like some of the measurements are [off the sheet](/images/5S/1a/5S1a_screenshot20170428at3.39.03pm.png.jpg) :( ?

---

Posted on **2017-04-28 15:45:34** by **scottsm**:

The Y direction is limited to +- 609mm on my 4'x8' frame with home in the center.

---

Posted on **2017-04-28 16:57:19** by **davidlang**:

hmm, I wonder if the maslow firmware isn't able to handle the G91 code (switching to relative addressing). This should only be moving between about +-450mm  (moving down 18mm each cut)

---

Posted on **2017-04-28 17:20:03** by **scottsm**:

G91 is trapped in line 709 of cnc_ctrl_v1/CNC_Functions.h to set a flag 'useRelativeUnits'. That flag is tested in line 397 of the same file. You might want to look at that section, it looks to me like it doesn't handle a negative value correctly?&quest; (Haven't looked very deeply, I'm multi-tasking...)

---

Posted on **2017-04-28 18:10:51** by **scottsm**:

Never mind that last, I misread the code.

---

Posted on **2017-04-28 18:27:53** by **scottsm**:

The .nc file looks [different](/images/ja/3Z/ja3Z_screenshot20170428at6.20.58pm.png.jpg) in [this g-code simulator](https://nraynaud.github.io/webgcode/), but when I ran it my sled headed [off the edge of the worksheet](/images/d3/ZG/d3ZG_screenshot20170428at6.15.21pm.png.jpg) :(...

davidlang, do you want to open the issue in Firmware, or shall I?

---

Posted on **2017-04-28 18:29:30** by **davidlang**:

I'm suspecting that the problem could be in GroundControl



Currently we have two different g-code interpreters, one written in python in ground control, and a different one written in C in the firmware



I opened a couple tickets in the firmware, one for G91, one for the difference between g0 and g1 (g0 should move at max speed, g1 should move at the defined feedrate) and also one to not silently ignore unknown g-code.

---

Posted on **2017-04-28 18:32:35** by **scottsm**:

That should catch it then. Certainly the picture on the screen is GroundControl, and is wrong.

---

Posted on **2017-04-28 18:36:58** by **davidlang**:

I made a slight update to the file and now the simulator shows it working the way I would expect it to.



If I change the g91 to g90, I get a picture that matches Ground Control

---

Posted on **2017-04-28 18:39:54** by **davidlang**:

it moves up and to the right for the second test when I meant to move down and to the right, but it doesn't really matter :-)

---

Posted on **2017-04-28 19:00:46** by **scottsm**:

I can run it later this evening, if that's OK

---

Posted on **2017-04-28 19:11:26** by **davidlang**:

whenever :-)



by the way, it looks as if GroundControl looks for G90/G91 and sets self.absoluteFlag but I can't find anywhere in the code that uses this flag.

---

Posted on **2017-04-28 22:23:15** by **scottsm**:

I've run the new file and it works as you describe except that it doesn't wait for the tool change. FWIW I read 893.5 vertical by 904.5 horizontal. Cutting 8mm deep was too deep for my stock so I zeroed above the surface. 

At the end of the file the sled remains in the upper left corner. 'Return to Center' and 'Home' do not move it from that location. Using the arrows to move by as little as 0.1mm away from that location causes 'Return...' or 'Home' to work correctly. Does this seem correct?

---

Posted on **2017-04-28 22:31:13** by **davidlang**:

it's supposed to be cutting 3mm deep, starting from 5mm above the surface (it should move the bit to 5mm above the surface as the first thing it does, then make the first move to the top corner, and then do everything else)



it looks like the firmware ignores T (tool) commands and M6 (tool change) commands



return to center not working sounds like another relative vs absolute movement bug (doing a move x0y0 in relative position mode won't do anything)



if you are using a 1/4" bit, the 893.5 vertical is just about dead on ( 0.25mm error, close enough to be within the margin of error for reading it), when you do the standard test pattern, does it show the square just a little wider than it is tall? It would only be off by about 1mm at 6" if it scales linearly

---

Posted on **2017-04-28 23:25:22** by **scottsm**:

I think that G1 Z-8 would go to 8mm below the Z zero point which is commonly the surface of the stock. I haven't looked - does the file redefine Z0? The first version did what you described (it uses G1 Z5 and G1 Z-3) but the new version uses G1 Z8 and G1 Z-8.

Other than printing a line on the screen, it does seem to ignore the T and M commands. This will be a GroundControl issue, maybe an enhancement.

There does seem to be an issue in the relative vs. absolute area. I wonder whether it matters whether the machine is left in relative mode at the end of a program? 

I measured from edge to matching edge (bottom to bottom and left to left) in order to remove the tool size from the equation, yes? Should I be measuring nearest edges instead? I don't remember the 6" square measurement, I'll look it up in the morning. 

Thanks for creating this test!

---

Posted on **2017-04-29 00:06:14** by **davidlang**:

ahh, your way of measuring is better (nice tweak to not have to worry about the bit size). I assumed you measured closest edge to closest edge. If this scales linearly to the 6" square, you would be off by ~2mm there.



the test that was posted earlier (that did many boxes across the sheet) used z5 for moving and z-3 for cutting, so I just did the same.



When I was cleaning it up I realized that in relative mode, doing z5 z-3 would end up marching the router to the limits of the Z eventually, so I changed the movements after going into relative mode to z-8 z8, before going into relative mode, it does the following:

G40

G0 Z5

G17

G0 X-900 Y450



the G40 G17 were from the initial file I copied from, so it should start out with the bit 5mm above the sheet and about 3' to the left and 1.5' up from the center.



It then switches to relative mode, does the tool change, turns on the spindle, and does one set of cuts

G0 X450

G1 Z-8

G1 X18

G0 Z8

G0 X-18 Y-900

G1 Z-8

G1 X18 

G0 Z8

G0 X900 Y900

G1 Z-8

G1 Y18

G0 Z8

G0 X-900 Y-18

G1 Z-8

G1 Y18

G0 Z8

G0 X-432



this should end up 18mm high and to the right of where it started (if you add up all the X and Z changes) and the same height

---

Posted on **2017-04-29 00:07:51** by **davidlang**:

a thought on the sled width setting, I wonder if some of the error is the difference between where the metal brackets are and where the hinge points of the chain are that stick through the brackets. that's only a few mm, but it seems like that sort of difference matters more than we thought it would.

---

Posted on **2017-04-29 05:55:04** by **rancher**:

David, the current best settings for accuracy don't have much to do with real world measurements.  Gero had the best results with sled width +15mm.  I did try real measurements on both sides of the chain mount hole and did not see a difference.

---

Posted on **2017-04-29 11:03:50** by **Bar**:

I've been thinking that the hinge points where the chains stick through the brackets might be a contributing factor to why we all seem to need to increase the spacing setting. Mine ended up being about +10mm from what I measured which would be about right for where that last link is bending.

---

Posted on **2017-04-29 12:05:56** by **scottsm**:

davidlang, my 6" square was wider than tall by ~1.24mm - in the ballpark of your prediction :).

---

Posted on **2017-04-29 12:30:39** by **davidlang**:

@scottm, so the question is which is easier to measure, the small square with calipers or the large slots with a tape measure?



I'd guess that since we're aiming for people with very little equipment, the tape measure is going to be better (more familiar to people and more likely to be on hand)

---

Posted on **2017-04-29 12:32:37** by **davidlang**:

I also suspect that with a 6" square, people are going to be willing to stop calibration when they get to within a 1/2mm or so, not realizing that that translates into several mm of error across the full sheet.

---

Posted on **2017-04-29 12:44:02** by **Bar**:

Great points. It seems like we're favoring the large square then?

---

Posted on **2017-04-29 12:57:18** by **davidlang**:

we don't even need a full square, the g-code I created makes two small slots horizontally, and two vertically centered 900mm apart. If you hook a tape measure to one and read the far side of the other slot, you will see your actual position error as it differs from 900mm.



I picked mm because even US tape measures have mm on them, and it's easier to enter mm than it is to measure fractions and convert for entry.



the file is at http://lang.hm/maslow/testpattern2.nc it does two passes, but since it uses relative positioning, it's trivial to repeat as many passes as needed, just change the tool number so that the machine pauses

---

Posted on **2017-04-29 12:59:26** by **davidlang**:

I think there are going to be people who prefer the small square, or a small version of my test due to the increased accuracy of calipers vs a tape measure, so I think both should be supported.



to convert my testpattern to something that will fit calipers, change the 900 to 100 and the 450 to 50 (except for the very first one that moves it from the parking location)

---

Posted on **2017-04-29 13:08:37** by **davidlang**:

I made a testpattern2-small.nc that does the same thing at 100mm. it's at http://lang.hm/maslow/testpattern2-small.nc

---

Posted on **2017-04-29 13:15:41** by **Bar**:

Very cool. I think that the idea of not needing to cut the full square is a great one. I'm going to try to take your ideas and build them into Ground Control so that the cutting of the test pattern is automated. Great point that doing things with relative commands makes it much easier to move and repeat the pattern.

---

