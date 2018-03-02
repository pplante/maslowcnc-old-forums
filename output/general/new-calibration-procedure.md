## New Calibration Procedure
Posted on **2017-05-04 14:46:23** by **Bar**:

I've been working on a new calibration procedure that rolls all the things we've learned into an easy to follow set of instructions. The community created so much great knowledge about how to setup and calibrate the machine and I wanted to make sure that knowledge was easy for future generations to pick up. 

I've created a wizard type system where you click next and do what it asks in each step to calibrate the machine. You can now access it by clicking *Actions -> Calibrate Machine Dimensions*.

It's not 100% done yet, but I would still love everyone's feedback about how it works for you, what could be made more clear, and what could make it better.

---

Posted on **2017-05-04 18:05:41** by **Bar**:

I found a pretty significant issue with the way this works, the settings weren't getting pushed to the machine when they were updated. It should be fixed now, but maybe hold off until tomorrow before trying it, I'd like to test it again thoroughly first to make sure it works before taking up your time.

---

Posted on **2017-05-05 04:26:53** by **gero**:

Could not hold off 8)

---

Posted on **2017-05-05 05:06:09** by **gero**:

Where should Z be to cut the test shape?

---

Posted on **2017-05-05 08:58:10** by **scottsm**:

It looks to me like the test pattern includes a command to lower z by 7mm to start cutting, and raise by 7mm at the end of cutting. I'm putting the bit 3mm above the surface and the marks are deep enough to measure but not deep enough to hook a tape measure. Simple to hold by hand, though.

---

Posted on **2017-05-05 10:33:11** by **Bar**:

Good point about the z-axis needing to be set. Z=0 should be the surface of the wood.

I think the process is ready to be tested. I just finished running it and ended up with values true to as close as I could measure with the tape  measure ~.5mm.

If you are going to test it, be sure to grab the latest version!

---

Posted on **2017-05-05 12:56:51** by **Bar**:

Here are my results after testing the new system.

I ran the calibration process until it completed so both of my ~600mm measurements were within .5mm of each-other (or about the limit of what I can measure with my tape measure). I didn't do any calibration other than to step through the calibration process and do what it said to do in each step.

Then I ran the the straight line test and cut 80inch (~2000mmm) straight lines across the board at Y= +14 Inches, Y = 0, Y = -14inchs. [Straight line test](//muut.com/u/maslowcnc/s3/:maslowcnc:Wdz1:fourcuts.jpg.jpg) 

I borrowed a giant straight edge from the cabinet makers next door to measure the bend in each cut.

The bottom line domed up .096 Inches in the middle of the 80 inch span  [Bottom](//muut.com/u/maslowcnc/s3/:maslowcnc:b6QX:bottom.jpg.jpg) 

The middle line domed up .041 Inches in the middle of the 80 inch span [Middle](//muut.com/u/maslowcnc/s3/:maslowcnc:Mo6y:middle.jpg.jpg) 

The top line had some weird funkiness to it that I think has to do with the feedback system so I couldn't measure it accurately  [Top](//muut.com/u/maslowcnc/s3/:maslowcnc:xGNU:top.jpg.jpg) 

I'd love to be able to say everything is perfect, but we are at least seeing significant progress. We've gone from being 1/4inch  out on a 6-inch test shape to 1/16-1/32 out on an 80 inch test shape.

*Here's what I think is next:*

I think we should do the same thing we did with the 6-inch test shape and instead of cutting the whole line, we just need to make a mark out at +-40 inches and in the center. From that we can measure the bow over that span and see do the same kind of automated correction we do on the other test shape. The hard part is that it's tough to measure 1/32 bend over an 80 inch span. Using my tape measure as a straight edge, I really couldn't tell and not everyone can borrow a giant straight edge from the cabinet shop. Is there another way we could measure?

---

Posted on **2017-05-05 12:58:19** by **Bar**:

Has anyone else had good or bad luck with the new calibration method?

---

Posted on **2017-05-05 13:00:05** by **scottsm**:

That sounds great! How many times did you have to run the cal cuts to get to .5mm? This was from "count the links" for a sled measurement, right?

---

Posted on **2017-05-05 13:14:38** by **Bar**:

Yes, it was from a count the links sled measurement (mine does 49 links) and it took me three test patterns to get to within the .5mm target

---

Posted on **2017-05-05 14:10:17** by **davidlang**:

the top cut looks almost like a chain slip, that is where there is the most tension

---

Posted on **2017-05-05 14:14:53** by **davidlang**:

for measuring the error, drill down on the ends, find a bolt/rod that is a tight fit, take a string line (chalk line) and stretch it tight over the top of the two bolts and snap a line onto the wood

This will give you a straight line that 'should' be exactly even with the top of the cut.

now, as close as we are getting, this still may not be enough, but it's the best we can do short of light based checks

as a light based check, drill three holes (ends and middle) put good tight pegs/bolts into all three and sight down the length of the board, you will be able to tell if they are all exactly lined up or not

---

Posted on **2017-05-05 15:37:14** by **rollandelliott**:

I agree a chalk line or even a roll of dental floss will work :)

---

Posted on **2017-05-05 17:16:14** by **Bar**:

Dental floss is a great idea!

---

Posted on **2017-05-05 17:17:17** by **Bar**:

Has anyone else tried the new calibration and had it work for them?

---

Posted on **2017-05-05 17:54:36** by **scottsm**:

I'm wading through it, taking notes. I swear my right motor sprocket got pulled a half a degree counter clockwise, and the chain popped. I remember that my last adjustment to it was a CCW turn; shouldn't have backlash, should it? I've noticed that if I stop the calibration and leave that section, when I come back, the calibration cuts are over the top of the previous ones, even if I've moved 'Home' in the mean time. I'm working on a sheet of 2mm ply screwed to the work area; I guess the assumption is that I would slide the ply over so the new cuts will be discernible from the previous set :) . I'll move and finish the cal steps. A warning about chain over-wraps when starting into the left chain movements will help those who haven't yet experienced that. Measuring the motor height didn't flow smoothly; is the assumption that the chain hasn't yet been retracted from the motor measurement and sled measurement? I used the 500mm move (six times :( ) to reel in the chai n to make the measurement, and the measurement was 20mm+ long.
 Sorry to have such a gray list - the many many parts that worked well and correctly are a separate list :) :) !

---

Posted on **2017-05-05 18:04:13** by **davidlang**:

The calibration routines are working from the absolute machine dimensions and are going to be used to figure out where home is. This is why changing the home doesn't change any of the cuts.

there is only no backlash if the machine is fully setup and you have the tension on the chains from the weight of the sled. That keeps the gears pulled towards the center and makes backlash a non-issue.

---

Posted on **2017-05-05 18:12:18** by **Bar**:

Better to know than to not know!

Right now the test pattern isn't affected by the home position, but maybe that should be more clear, or there should be an option to move the design over.

Adding a note about being careful about the chain wrapping is a great idea.

Concerning about the measure motor height measurement coming out wrong. I will double check those. The idea is that you have the chain extended fully at that point and reel it back in to where it is the right height. It seems like more clear wording in the instructions is needed for each of these steps at the very least. 

Thank you for the advice!

---

Posted on **2017-05-05 18:33:37** by **Bar**:

Something that might be contributing to motor height offset calculation is that we used to be measuring to the center of the motor, now we're measuring to the top of the sprocket.

---

Posted on **2017-05-05 18:34:01** by **scottsm**:

There is an option to move the chain th the sled measurement step between the motor y measurement and the motor x measurement. I reeled in the chain 'one button click' before doing the sled measurement and moving on. Later when I went back in to re-do the motor x, I watched the .ini file contents. I'm not sure all of the 'reduce chain' clicks reduced the value stored, some seemed to increase it instead. I was interrupted before I could make sure of what I thought I saw, though. It did seem odd that there is only a 1mm extend, but 10mm, 100mm, and 500mm retract.

---

Posted on **2017-05-05 18:35:49** by **scottsm**:

Top of the sprocket, that's part of the difference.

---

Posted on **2017-05-06 07:34:19** by **gero**:

Finlay I got to catch up a bit. The is a lot of activity on GitHub and I could not go through all, so first here to avoid duplicates:

1) 3-8 Detach chain from right sprocket? That just popped off.
2)4-8 Could use reel back 1000 or more. I went out 3010 and back -7 till it popped.
3) 6-8 is misleading. Hook right chain to right sprocket and click calibrate is not correct. At this point the left chain is still hanging from the motor hight measurement. Both chains should be hooked at 12:00 before clicking. This brings me to the most interesting point.
6-8 is also missing a "Mount the sled"
4) Going back to 1-8 to bring the left sprocket to 12:00 changes the value for Vertical Offset. It is just overwritten in the .ini file.
But after motor hight, my left sprocket has a gap between the teeth at 12:00. So calibrate chain length did not seem right.

Ignoring the changed Vertical Offset (from first 477.65mm to then 475.31 after turning left CCW) it took 4 cuts to get from H67/V59 to H60.5/V60.5

Nice calibration path though.

---

Posted on **2017-05-06 09:30:46** by **Bar**:

Perfect feedback! 

I'm going to go through and make all of those changes right now.

---

Posted on **2017-05-06 10:33:39** by **Bar**:

I've added the changes you suggested. I'm going to try to replace the poping off mechanism in 2-8 with an automatic pull tight system.

Something that your feedback made me realize wasn't clear is that 6-8 needed to be re-worded. You actually don't have to move the left chain back to 12:00, it can just stay the length it is but that wasn't clear at all in the text. Hopefully it's clearer now and you've saved someone in the future from being confused  :-)

---

Posted on **2017-05-06 13:54:07** by **gero**:

Since i moved my brackets to the outside of the sled, i was lucky to go through all again. Looks great now! On 4-8 you removed the 500 and put the 1000, i think i ended up with the same amount of clicks 8).
Can go through tomorrow again, forgot the bungees and had chain jumps :-)

---

Posted on **2017-05-06 14:17:00** by **Bar**:

If it looks great it's thanks to your feedback :-p

---

Posted on **2017-05-06 14:17:45** by **Bar**:

We could do a 500 and a 1000 but I thought I'd keep it consistent with the other ones

---

Posted on **2017-05-07 09:01:35** by **gero**:

Pull chain tight does nothing :-(

---

Posted on **2017-05-07 09:04:48** by **gero**:

It sends a B11 S50 T3 no moves or noises, new firmware?

---

Posted on **2017-05-07 09:09:03** by **gero**:

Yup, answering myself...tzzz...

---

Posted on **2017-05-07 10:42:46** by **gero**:

5-8 shows the previous vertical offset, it gets updated if you leave 5-8 and come back

---

Posted on **2017-05-07 15:50:13** by **Bar**:

Great catch, I believe it should be fixed now :-)

---

Posted on **2017-05-08 09:31:25** by **gero**:

This is form yesterday, so if it is fixed, forgive me, as I can not be THE CALIBRATOR today :-(
On 3-8 I would add a 'extend left chain' before the detach. I went up the ladder first, looked at the chain and decided to go down again and check what buttons are there :-)
If not fixed by now, there is some metric confusion on 7-8. The day before, I entered numbers like 59.5 and 60. 5 and automatic came to the finish page, Yesterday I thought, wait a moment, the unit is mm, but what did I enter before? I entered cm and 60.5 cm is 605 mm. I tried 605 this time and CG was happy. So the rage GC accepts is in the range of 1cm = 10mm.
On the tape i measured 60.05 cm or 600.5 mm.

---

Posted on **2017-05-08 09:34:07** by **gero**:

Oh, I almost forgot this one... can you add, just for me, after 'attach the sled', GERO! DON'T FORGET THE RUBBER! RUBBER CAN SAVE YOU!

---

Posted on **2017-05-08 12:07:04** by **davidlang**:

sanity checking the input to see if it's close to the expected range (as opposed to being off by a factor of 10x like Gero was) would be a good thing. Have the ability to say "yes I really meant that" for odd machine dimensions, but we have a fairly good idea what these numbers should be.

---

Posted on **2017-05-12 09:31:59** by **blsteinhauer88**:

Ok,  I just finally tried the new calibration.  Wow.  Nice from a user point of view.  It was easy to understand and follow.  The end result was that it made a couple very small but important for the math, adjustments to the measurements.   My test cut came out calibrated on the first try.  
I recommend others to got through it if they are having some accuracy issues. 
I suggest only maybe a way to zero the Z in the Wizard also.  ( I saw something grayed out in the settings?&quest;?)  

After thought, This also put my 0,0 in the center of the work-space! (unlike with just the chain calibration before)  Nice!!!

---

Posted on **2017-05-12 10:22:50** by **rancher**:

Nice report B!  I was on hold since I just got to where I could cut the few things on my list, like that sign.  I'm past that now and hoping to try the new routine in the next day or two.  Anything special I should wait for or that you'd like tested, Bar?

---

Posted on **2017-05-12 10:32:20** by **blsteinhauer88**:

I am building the new arms today @rancher, and will repeat the process.

---

Posted on **2017-05-12 10:36:28** by **Bar**:

@blsteinhauer88 great point about the z-axis being calibrated as part of the same process. 

@rancher Go for it! I'd say use the firmware and software from Wednesday's release because I'm making all kinds of improvements to the feedback control system right now so Master on GitHub is a little untested. Let me know if there are any steps you think could be more clear.

---

