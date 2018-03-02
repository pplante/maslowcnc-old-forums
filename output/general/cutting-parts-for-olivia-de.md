## Cutting Parts for Olivia Desk from Open Desk
Posted on *2017-05-28 22:08:03* by *Bar*

I've been holding off getting a desk until I could find the time to build one, and as part of testing today I cut the parts for the [Olivia Desk](https://www.opendesk.cc/lean/olivia-desk#get-it-made) from Open Desk. 

The parts were all cut as one continuous cut over 3.5-4 hrs at 35ipm with a .15in step down from 3/4 inch AC plywood.

Things went smoothly, other than one pass on one of the legs deciding to cut a corner off. I'll probably recut that leg and get some footage of it cutting real speed to give a better sense of how fast the machine is moving, but here's the raw [timelapse](https://youtu.be/uvIdXtmOdSw)

Hopefully I can get it put together and put a coat of polyurethane on it for the update on Wednesday!

---

Posted on *2017-05-28 22:37:15* by *blsteinhauer88*

what programs did you use on your downloads?

---

Posted on *2017-05-28 22:37:41* by *blsteinhauer88*

Looks Great across the cutting area!

---

Posted on *2017-05-28 23:26:50* by *mattnelson*

Impressive!  Why did that one corner do that?  Issue with the maslow or the gcode?

---

Posted on *2017-05-29 02:34:23* by *davidlang*

Ok, from watching the video in slow motion, it looks like only the second pass had a problem. that makes it unlikely that it's a g-code error. I'd bet that it's not going to be easily repeatable (I hope I'm wrong). I'd suggest watching for errors on the console as the cut is made. If there's any way to capture all the errors (both from GC and anything reported from the firmware), that should be done.

---

Posted on *2017-05-29 02:37:38* by *davidlang*

I still think you are cutting too shallow in each pass :-) but the recommendations are all over the map. I see a lot of suggestions of no more than 1/2 cutter diameter, several suggestions if 1*cutter, and a lot of tables that list 2*cutter as normal :-)

I think the ones suggesting 1/2 cutter diamter are not assuming cuts like we are making, but rather enlarging a hole or cutting in from the edge.

---

Posted on *2017-05-31 12:13:20* by *Bar*

I think you are right that we can probably push the depth further. I did some tests yesterday with .2 inch passes 18k rpm on the router, and those looked great.

---

Posted on *2017-05-31 12:14:46* by *Bar*

I'm pretty sure the issue was on our end, not in the gcode because everything rendered correctly in Ground Control. My guess is that something went off in the serial connection and a letter got lost. We may need to add some sort of a check sum to make sure that the line is complete before executing it

---

Posted on *2017-05-31 12:18:20* by *Bar*

Here's the final [desk](//muut.com/u/maslowcnc/s3/:maslowcnc:etfJ:img_20170531_084952612_hdr.jpg.jpg) ! I also made a [video of the build process](https://www.youtube.com/watch?v=CIQC5ZyzfDM&) for the Kickstarter update today.

I'm really pleased with how it turned out. It fits the space well and I'm looking forward to using it. Plus, the chair was getting lonely. 

I think I'll do a dining room table and a full set of chairs next :-p

---

Posted on *2017-05-31 12:20:20* by *gero*

Wow, how did the connections fit? Loose, sanding or brute force? ;-)

---

Posted on *2017-05-31 12:22:55* by *gero*

Sorry Bar, looks like perfect fit in the video.

---

Posted on *2017-05-31 12:23:51* by *Bar*

They were actually perfect on the first try which was totally luck. Plywood varies in thickness so much batch to batch I try to avoid those types of press fit, but all the open desk furniture uses a lot of them

---

Posted on *2017-05-31 12:55:49* by *gero*

I have read the article and it was very enlightening. In this part of the world I am dealing with imported crap, that the rest of the world has rejected. FreeCad however lets me adjust every single constrain within minutes and generate the Gcode.
A wonderful Desk and you challenged me to eventually start to build.

---

Posted on *2017-05-31 13:26:28* by *TheRiflesSpiral*

Aker has a test fit file that doesn't take up too much room that will help you determine how to set up your tool paths with materials of odd frequencies for these press-fit applications. https://akerkits.com/collections/source-files/products/clearances-test-file-source-file-pack

---

Posted on *2017-05-31 14:13:42* by *mindeye*

What was the cutter's diameter?

---

Posted on *2017-05-31 15:15:27* by *davidlang*

I just noticed that the forum butchered by comment

I was trying to say that my research shows a few comments that this sort of cutting at a dept equal to the bit diameter (0.25" in this case), and quite a number that talk about cutting at a dept equal to twice the bit diameter (which would be 0.5" per pass.)

a while ago you showed an example of a 1/4" bit cutting 3/4 plywood at 48 ipm in a single pass and were uncomfortable with the result. My research on the topic says that 3/4" is a bit on the aggressive side for a 1/4" bit, but would probably be fine if you used a 1/2" bit

but you should be able to cut through 3/4" plywood in two passes with a 1/4" bit comfortably

---

Posted on *2017-05-31 15:52:54* by *gero*

The Maslow is a different league from my opinion. RPMs and feeds need to be redefined. Same goes for the depths. Horizontal CNC can be brought in as a reference on how to start. On my tilt, now increased from 6 to 10 degree, the speeds that I have cleaner cuts are far higher then recommended. I have cutter moves off the line when the bit goes into the material. Feed can be increased to the limit off wiggling the sled at corners at direction changes. A series of the same .nc file on different Maslows, to achieve comparable results (davidlang) could be a approach to get recommendations for this amazing machine.

---

Posted on *2017-05-31 16:58:28* by *blsteinhauer88*

I am at 10 degrees also and am happy with the quality of the cut,  more was too much friction, and less as I understood'Gero' to say , the bit can start to 'steer' the sled at the higher speed, not a clean.

---

Posted on *2017-05-31 16:59:16* by *davidlang*

what do you mean by "the speeds that I have cleaner cuts are far higher then recommended"?

are you talking about feed rate? rpm? is this based on chip load calculations?

---

Posted on *2017-05-31 18:51:51* by *rollandelliott*

What kind of blue stain is that?
looks awesome!

---

Posted on *2017-05-31 18:51:57* by *scottsm*

@Bar, there were lots of long straight horizontal cuts in that desk. How straight did they come out?
The checksum idea seems good, but would that interfere with grbl compatibility? I've had several odd cuts like you saw lately, and captured the console output during a couple. I opened a issue with the data from one. 
 I've been wishing GC had an option to log outgoing and incoming lines.

---

Posted on *2017-05-31 18:54:24* by *davidlang*

possibly a debug mode in the firmware that echos back every line it processes as well?&quest;?
If we are loosing data over the USB cable, there is something very wrong here, we should not be loosing anything at these speeds.

---

Posted on *2017-05-31 20:28:24* by *scottsm*

I think we have that echo already. It would be nice if the lines could be logged to disk to aid post-mortem. Without that, you have to be present and watching for the error, and take a screen shot before hitting ‘STOP’.
 If the lines included line numbers, GC might be able to validate them against the appropriate line in the code array and take action.
 I eliminated the USB extension and used a high quality USB cable and the issue still crops up. I’ve been thinking of stepping back to an earlier release to see where along the line the issue comes up, but haven’t had time yet.

---

Posted on *2017-05-31 21:31:30* by *mattnelson*

Is it possible we are getting interference from the router?  I once had a vandergraph generator 15 feet away screw up my serial communication to an arduino.

---

Posted on *2017-05-31 23:17:16* by *scottsm*

In my instance, no. I'm running my sled with pens instead of a router :) .

---

Posted on *2017-06-01 10:47:27* by *Bar*

@scottsm I redid the calibration process (as part of testing something else) just before running these cuts and they came out notably straighter than I've seen in the past. I didn't measure any bend at all with a quick check with the straight edge.

The logger is a great idea. I've added it to Ground Control. All messages sent from the machine are now recorded in the file "log.txt".

I'm betting we started loosing more bits when we bumped the serial speed up to 57,600 from 19,200 a few weeks back. The issue could be RF interference or it could be something in our code. 

The first step is to find a way to make the problem repeatable, then we can narrow it down. 

@rollandelliot Thanks! I like it too. I just took the picture of the [slim chair](https://www.opendesk.cc/regaliz/slim-chair) to the guys at the paint store and asked for the same color Open Desk used, and they did their best to match it off my phone screen :-p

---

Posted on *2017-06-01 13:24:34* by *scottsm*

I tried the logger just now, it opens a file but doesn't write to it :(. 

The good news is that problem is completely repeatable :). So far I've tried every GC/Firmware release pair since F69/GC71 and my test file works correctly in all except F72/GC74. I checked with F71 and GC74 and there was no error. In F72/GC74 I've tried 19200 baud and that made no difference. (FWIW 115200 works with GC74 and F71  :), but the error crops up with F72...). 

 By this I think I've narrowed the issue down to something in F72 besides the baud rate. Watching the console, I've seen what looks like middle or end portions of a line missing. See the screen shots in the issue I opened.

---

Posted on *2017-06-01 13:32:22* by *scottsm*

Unfortunately I moved the issue to GC back before donig this research. Currently find it as issue#300 in GC. Perhaps I should reopen the Firmware issue#234 to keep things straight?

---

Posted on *2017-06-01 14:20:09* by *Bar*

Good catch on the logger not logging. I wasn't actually starting the thread which does the writing to disk. I believe it's fixed now.

I'll take another look at [#300](https://github.com/MaslowCNC/GroundControl/issues/300) I was hoping that it would solve itself as part of the buffer overflow / arc calculation re-do fixes with this week's firmware. Since it didn't, let's track it down!

---

Posted on *2017-06-01 22:19:37* by *davidlang*

take a look at https://github.com/MaslowCNC/GroundControl/issues/309 that looks like it may account for this problem.

---

Posted on *2017-06-01 22:41:33* by *scottsm*

While this is a good find, making the proposed change to Ringbuffer.h does not solve the issue in #300. Tested twice. Darn, I had such hopes!

---

