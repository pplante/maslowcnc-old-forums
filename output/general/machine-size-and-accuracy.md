## Machine Size and Accuracy
Posted on **2017-04-02 07:47:31** by **rancher**:

I'm running a non standard frame at the moment, and am experiencing some significant accuracy errors as I move away from the origin.  I have adjusted my offset settings as best I can and I can't quite get it.



I'm assuming that the settings default to the proper frame size, and the machine is accurate at those dimensions.  I intend to modify my frame to those dimensions for my next cuts.  



I brought this up to open up the dialog again about accuracy and machine dimensions, and to get verification that most likely that is my issue.  As well, if someone could post the actual motor offsets in ft/in, and appropriate settings values, I would be forever grateful.  Thanks all.

---

Posted on **2017-04-02 08:04:33** by **Bar**:

That might not be a just you issue. I had everything pretty dialed in for my machine originally, but everyone else was seeing oval circles. When I changed the way the measurements are done it fixed the problem of everyone getting really oval ciecles, but now when I cut a new circular sled it's off by about 1/16th to 1/8th inch which it wasn't before. I haven't tested at the extremes of the bed yet, but I'd assume it's worse there.



It might be worth filing a bug in the firmware for this, because it's something we need to look into.

---

Posted on **2017-04-02 08:26:59** by **scottsm**:

I see the same kind of accuracy issue. I'm hot to help address it.

 What would you like for information in the issue? Should we create and use a standard 'check shape'? What shape would be simplest, quickest most informative to test with - circle, square or rotated square, or dogbone for instance? Would you like measurements taken from the center of the work area as well as the four corners? Which measurements will be the most helpful, which not? Should we do a motor cal at each location?

---

Posted on **2017-04-02 08:28:01** by **rancher**:

I would love to know the measurements of the accurate machine as well, so I can modify my frame and make some stuff while this is sorted.  Please.

---

Posted on **2017-04-02 08:47:42** by **Bar**:

@scottsm I have been testing with a circle because it is an easy shape to measure inacruacy in, a square could also work well. I've also been playing around with the idea of using the machine to draw a grid across a very large piece of paper, that way we could "see" the distortion in an intuitive way.



@rancher I didn't change the machine dimensions, just the way the calculations in the firmware are done. The default values are still my machine dimensions. In theory the changes I made shouldn't have changed how the underlying math works, just how the setup is done, but that's only in theory.

---

Posted on **2017-04-02 08:54:01** by **rancher**:

Okay, great, thank you.  I wasn't clear due the "crossbar" temp version you had posted way back at the start of all this.  So, you are getting accuracy issues on the standard size frame as well?  I see.  



I didn't/don't want to put you onto another issue before everyone else is up to speed on assembly, which is why I was hoping to just modify my frame.

---

Posted on **2017-04-02 09:04:17** by **scottsm**:

I've got a roll of 44" wide butcher paper, I can chuck up a pencil and plot a grid. My sled makes it hard to get all the way to the bottom, though. What grid size would you like? Do you want mm and inches both? Is feed rate an important variable?

---

Posted on **2017-04-02 09:29:47** by **Bar**:

Y'all are awesome. I have no idea what I did to deserve this incredible group of beta testers. Thank you.



I think we could start pretty corse with maybe 1 foot squares with the goal of getting a sense of where the distortion is concentrated. The feedrate shouldn't matter too much, but I would keep it at around 20ipm just so we know we're really seeing the kinematics and not the feedback control system when we see distortion.

---

Posted on **2017-04-02 09:41:31** by **blsteinhauer88**:

I can confirm people will have an issue using the Temp Maslow.  My 'like'  parts were off when I cut and assembled my frame.  Also in the arms, when I was measuring, one motor platform ended up 1/2 inch low er that the other, so I had to add board under the motor to lift it to match the other.  It made building the final frame more difficult.  The frame parts for the 2x4's were also a little off each other.  I screwed those together on top of each other to get matching angles.

---

Posted on **2017-04-02 09:59:46** by **Bar**:

Are you seeing better or worse results with the final frame?

---

Posted on **2017-04-02 16:49:26** by **blsteinhauer88**:

Better with the frame, cut a small box, bit size was the issue.  All the dimensions though seemed much better!

---

Posted on **2017-04-02 18:35:13** by **mindeye**:

Yeah, I'm definitely at my wits end with accuracy at this point. My measurements are definitely good and a calibrated the motors immediately before the cut but my latest cut of a motor mount was horribly askew on top and bottom, while the sides were plumb. Overall sizing is mostly correct (within a 1/4") but for some reason horizontal cuts are totally wonky. [IMG_20170402_180952767](/images/6z/6zca_img_20170402_180952767.jpg.jpg)

---

Posted on **2017-04-02 18:52:20** by **mindeye**:

Staring at that image a bit more, I'm beginning to wonder if my left motor is somehow letting out too much chain when cutting top / pulling too little chain in when cutting bottom and then pulling the excess back to true once it rounds the corner to a side. I'd think the calibrate motors would handle this but maybe over only longer distances it's an issue?

---

Posted on **2017-04-02 18:52:44** by **davidlang**:

@rancher, what size frame did you use?

---

Posted on **2017-04-02 18:54:55** by **mindeye**:

That's also the second attempt at the motor mount and the angle on top / bottom was different between the two attempts. The first attempt, 8" higher on the board was steeper.

---

Posted on **2017-04-02 19:58:38** by **Bar**:

Hmmmm

---

Posted on **2017-04-02 20:04:14** by **Bar**:

How does the positional accuracy circle look while the cut is going on? Does the feedback system think it's holding position well? It might be a feedrate thing, if the commanded feedrate is faster than the system can keep up with you will get those type of slanted cuts while one motor can't feed out or take up chain fast enough.

---

Posted on **2017-04-02 20:09:18** by **Bar**:

The more I think about it, the more this feels like a feedrate issue. Does that idea fit with what you were seeing?

---

Posted on **2017-04-02 20:16:03** by **rancher**:

> @davidlang

> what size frame did you use?

I used a crossbar that is 10' long so the Horizontal measurement is the same, but my height offset is lower than default at 370mm.

---

Posted on **2017-04-02 20:56:43** by **Bar**:

@mindseye I've added a constraint to the firmware so that if the machine is commanded to move faster that it is able to without loosing positional accuracy it will now automatically run at a slower speed and give a warning message, hopefully preventing anyone from running into the same issue in the future. Thank you for catching that!

---

Posted on **2017-04-02 21:15:25** by **mindeye**:

@bar, that seems extremely likely. I was running a half inch mill really fast to get a nice cut. I'll give it another spin tomorrow but slow the feedrate down to what I've seen work in the past. That never would have occurred to me, thanks!

---

Posted on **2017-04-02 21:21:40** by **Bar**:

Awesome! Let me know how it goes. When I saw the picture my first thought was "it's not the right shape, but what a beautiful edge finish" ;)

---

Posted on **2017-04-02 22:22:46** by **davidlang**:

a different height offset should not make much of a difference, that just affects how high you can go on the workpiece.

---

Posted on **2017-04-03 11:47:58** by **blsteinhauer88**:

Did your mounts come out like this? (Your photo did not load in my computer) [IMG_0493](/images/iu/iu4r_img_0493.jpg.jpg) [IMG_0495](/images/qf/qf3e_img_0495.jpg.jpg)

---

Posted on **2017-04-03 11:49:32** by **blsteinhauer88**:

Mine ended up fixing with the new measurement system(between motors) and lower on a piece. I got skewed cuts on the top of the temp frame when the motors were at the top of the work area. Once we moved them up to the updated temp frame, and I cut them lower on the work area they were better.

---

Posted on **2017-04-03 11:50:33** by **blsteinhauer88**:

The height was affecting. Higher motors are, better the cut was.

---

Posted on **2017-04-03 12:15:33** by **mindeye**:

All images are currently busted it seems: "muut.com uses an invalid security certificate. The certificate expired on Monday, April 03, 2017 11:21 AM. The current time is Monday, April 03, 2017 12:15 PM. (Error code: sec_error_expired_certificate)"

---

Posted on **2017-04-03 12:20:01** by **mindeye**:

I posted in muut's forums, hopefully they'll clear it up.

---

Posted on **2017-04-03 12:48:59** by **Bar**:

Thanks for letting them know

---

Posted on **2017-04-03 18:42:35** by **mindeye**:

And feedrate was 99% of the issue. Slow it down to 20 ipm instead of 60 and it's just fine. It's actually very close to square... My picture taking ability isn't. [IMG_20170403_183909895](/images/6j/6jmk_img_20170403_183909895.jpg.jpg)

---

Posted on **2017-04-03 19:12:20** by **Bar**:

Very cool!

---

Posted on **2017-04-03 21:36:38** by **scottsm**:

I've plotted a grid of twelve 12" squares spread across the workarea, from X-44 Y-20 to X44 Y20 They all came out slightly stretched in the vertical direction, typically 12.125" high and 12" wide. This was done with a pen; I could route the tracks in wood if that would add value.

---

Posted on **2017-04-03 22:38:25** by **davidlang**:

the maslow theoretically will dow 48 ipm with the current configuration/hardware.



Once I get mine, I'm going to experiment with larger sprocket on the motors, since they have more resolution than they will ever need, and have enough power with the standard gears to rip a sled to pieces, using a larger sprocket that trades resolution and power for speed should be a win.

---

Posted on **2017-04-03 22:56:07** by **Bar**:

@scottsm that's fantastic. Great work! I'm not 100% sure what that means yet, but I'll sleep on it and think about it. It's very interesting that the pattern is consistent. I would have expected the distortion to change with location. That's a valuable data point. Thank you for doing that test.

---

Posted on **2017-04-03 23:16:02** by **jbarchuk**:

> @scottsm

> They all came out slightly stretched in the vertical direction, typically 12.125” high and 12" wide.

Aside from dimension off a little, are all the lines straight and corners square? (You can get accurate gauge of squareness by measuring diagonally across opposite corners, and they should both be equal.)

---

Posted on **2017-04-04 00:43:25** by **davidlang**:

I also would have expected differences in the distortion at different places. The distortion we've seen so far seems to be from the match not matching reality, so the amount of chain let out mispositions the bit/pen.



the fact that it's off so consistancly makes me think there's an error in the math and we have some other error that counters it in our common dimensions.



can you try deliberately distorting the config values and see if everything is still a consistent error?



the critical values should be the distance between the motors, the distance between the sled attachments, and to a much lesser degree the distances down to the bit and the center of gravity of the sled. (I would expect errors on these last two to make the lines a little wavy horizontally as the tilt of the sled is miscalculated)

---

Posted on **2017-04-04 01:15:09** by **jbarchuk**:

> @scottsm

> They all came out slightly stretched in the vertical direction, typically 12.125” high and 12" wide.

Another Q. I know you're using a pen but what size is your router bit set to? If my guess of 1/4" is right then it's an 'off by 1 radius' error.

The next question is whether it's in the +y or -y quadrants, or both.

The way to find that is to draw an x at the center of the square, and see if one side (top or bottom) is 1/8" oversize, or possible split between the two (meaning each top/bottom half being 1/16" oversize.)

---

Posted on **2017-04-04 02:30:01** by **davidlang**:

I suspect that he's using plain g-code, not something that involves defining a bit size.

---

Posted on **2017-04-04 07:03:00** by **rancher**:

> @scottsm

> I've plotted a grid of twelve 12“ squares

Scott, would you kindly share that gcode?  Perhaps it could be incorporated into the Ground Control zip with the example gcode files.

---

Posted on **2017-04-04 14:41:08** by **Bar**:

I started working on the next step in the instructions and immediately ran into this problem. I'm getting very oval circles on my temporary frame. I tested very carefully that I was getting consistently round circles last week so it's a bit of a mystery what changed at this point. My results back up what @scottsm saw with the error being consistent across the work area. I cut two circles one at the very center and one at the right side and they both came out with  [similar dimensions](/images/wi/wi40_similardimensions.jpg.jpg) but both were  [very oval](/images/zx/zxya_veryoval.jpg.jpg) .



I'm going to try to play around with it more and see if I can figure out what is going on.

---

Posted on **2017-04-05 08:34:18** by **scottsm**:

I've written up the pen plot data [here](/images/kp/kp9e_penplotdata.png.jpg). I had trouble with the z-axis so I had to change one square to avoid the tear, and the crushed pen tip made very wide lines - hard to get accurate numbers from fat lines.



 I made a version to cut outside the lines with a 1/8"bit and the [result](/images/i0/i0kh_img_0482.jpg.jpg) was surprising at first. The [left](/images/dl/dlkb_img_0485.jpg.jpg) and [right](/images/aj/ajte_img_0483.jpg.jpg) edges were unusable and the [top center](/images/z2/z2p2_img_0484.jpg.jpg) kept jumping the sprocket of the left motor - notice the stairstep path.



 The [accuracy](/images/nb/nb7a_routerdata.png.jpg) in the center and lower middle is quite good, though. I'm not sure why the pen was able to work in places the bit didn't. It was chucked up in the router, but not spinning. The machine is still the 'beginner model', so it's only 3010mm wide and 422mm to the motors. I used the main software branches as of the evening of 4/1. The plywood workarea sheet has 1.5" of bow across the width, and the ply I was routing was warped as well; I had to tack it down to the workarea sheet.



 I’m going to have to plan how to get the large arm  parts cut out of the ‘sweet spot’ of the work area, and I think I’ll try to have a flat workarea on my final machine.

---

Posted on **2017-04-05 08:47:05** by **gero**:

@scottsm What a great detailed test over the sheet!

---

Posted on **2017-04-05 08:58:43** by **blsteinhauer88**:

I haven't done a test like that, but I have noticed, "the sweet spot" is in the center and lower.  it seemed the higher it got and the more left and right the more skewed the parts, Nice Test.

---

Posted on **2017-04-05 09:02:45** by **blsteinhauer88**:

This is what caused one of my arms to be smaller than the other when cutting the full version parts.  I had to add a half inch shelf to the right arm so my motors were exactly the same distance from the work area.

---

Posted on **2017-04-05 10:40:02** by **Bar**:

What a fantastic and thorough test! Awesome work.



It seems like you are getting better accuracy than I am right now. You results seem pretty in line with what I've seen on the temporary frame in the past, but now I'm getting VERY oval circles. What are all of your setting values? I want to try to replicate your results to figure out why I'm getting such stark ovals. 



I think that the squares that didn't come out fall into three issue categories.



1) Chain skipped (top center and corners) - Plan to fix: adding a second roller to increase the amount of chain wrapped around the sprocket and keeping the chain "in plane" so making sure the motors are in line with the chain mounting points on the sled, and that the extra chain is pulled into plane by the bungee



2) Not enough tension in long chain (bottom left and right) - Plan to address: reducing friction between the sled and the wood, changing the angle of the frame to reduce friction between sled and wood, moving where chains mount on sled to increase the righting force.



3) General distortion. Plan to address: Improve s elf measuring of machine? Add a calibration routine which is independent of entering measurements? 



I've tested the adding a second roller to increase the amount of chain wrapped around the sprocket using a nylon spacer from the hardware store with good results. I haven't had the chain skip since adding it. Has anyone else experimented with a slicker sled surface or changing the angle of the frame and seen an improvement?

---

Posted on **2017-04-05 12:06:48** by **scottsm**:

My motors are at the ends of the 10' 2x4 as in the pictures' the 2x4 bottom is 12" from the edge of the sheet. My settings are:

[Maslow Settings]

openfile = 

motoroffsety = 422

sledwidth = 322

bedwidth = 2438.4

comport = /dev/tty.usbmodem1461

zaxis = 1

sledcg = 85

zdistperrot = 3.17

bedheight = 1219.2

sledheight = 130.6

motorspacingx = 3010



[Advanced Settings]

gearteeth = 10

encodersteps = 8148.0

zencodersteps = 7550.0

chainpitch = 6.35

 

I've tried a 'pre-roller', but on the slack end. The jumps I saw were on the taught end, the rollers did not prevent the jump. My sled is the circular pattern made to the plan with a 1/8" UHMW face rounded over at a 1/16" radius. The frame is at 17 degrees from vertical.

---

Posted on **2017-04-05 12:23:49** by **blsteinhauer88**:

Bar, on my temp frame I was also getting mostly ovals.  even though I put in the distance between the motors, I too installed them at the ends of the 10 footer.  I found that there was almost a 3/4 inch difference between the corner of the working area and the motors, as the 10 footer was not exactly 10 feet and was not exactly in the center.  When I fixted this centering and distance from work area, it was much better.

---

Posted on **2017-04-05 21:45:22** by **davidlang**:

@blsteinhauer88 can you quantify the size and location of 'the sweet spot'? we know that it gets harder the higher up you are (more tension on the chains), and when you get to the outer edges (very low tension on the chains), but if you can figure out about where the limits are (given a particular machine dimension), then I can fiddle around with the models and get a fair approximation of what the min/max tension numbers are. From there we can model other machine sizes and/or build instructions to produce the most accurate parts.

---

Posted on **2017-04-08 08:50:46** by **rancher**:

Hey guys, any further progress or discoveries along these lines?  I cut a quarter sheet project that was too far off to use which inspired me to start this thread.  I've been on hold waiting to see if you guys are getting reasonable accuracy with the full size frame before I go down and modify mine.  Anybody have any updates along the lines of accuracy improvements?

---

Posted on **2017-04-08 08:58:55** by **scottsm**:

I'm rebuilding my frame by raising the top bar 3" or so, adding extenders to the ends of the top bar to spread the motors by a few inches (piece #1 from the cut 2x4) and changing to a much less warped of plywood. I'll do some testing to see what difference this makes.

---

Posted on **2017-04-08 11:02:37** by **Bar**:

On my end, I think we need a better calibration routine which doesn't require us to enter any measurements. With the current system I get different results every time I do the calibration which is no good. To make an automatic calibration system work I'll need to add quite a bit of code to the feedback system so we can detect things like tension in the chains so it might be a couple days, but it's on the top of my to-do list.

---

Posted on **2017-04-08 12:36:48** by **rancher**:

Thanks guys.  If there's anything I can do to help the process, let me know.

---

Posted on **2017-04-09 12:30:22** by **blsteinhauer88**:

I am using Maslow as designed. Except for my furniture movers on the sled. I think with the last few tweets by bar. The accuracy is dialed in.  I did a bench, which only failed because I for got to scale width of wood with my other scale reduction. Still cut 9 I sent iCal parts running up the wood. I'm impressed Bar!  [IMG_0528](/images/ti/ti5d_img_0528.jpg.jpg) [IMG_0533](/images/bd/bd1z_img_0533.jpg.jpg) [IMG_0534](/images/gs/gskj_img_0534.jpg.jpg)

---

Posted on **2017-04-09 12:30:24** by **blsteinhauer88**:

I like how it slows the rate to keep on track!

---

Posted on **2017-04-09 13:10:34** by **rancher**:

OH HEY!  It's working!  I might run down to my shop right now, I've been waiting to see some accuracy.  That looks great!  Thank you for the update.

---

Posted on **2017-04-09 15:00:09** by **Bar**:

That looks AMAZING! Great work!

---

Posted on **2017-04-09 15:35:54** by **rancher**:

I modified my frame to match both of yours, and it's looking good so far.  I didn't make any critical cuts so I'm not 100% yet, but it was looking good.  I also put some "feet" that extend out from the lower corners to mount the lower hooks of the tension system, so the angle at the motor gear was more favorable.  It seemed to help.

---

