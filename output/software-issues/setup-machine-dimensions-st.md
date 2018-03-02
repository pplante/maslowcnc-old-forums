## Setup Machine Dimensions Step 8 of 9, diagonal cut going off the work area
Posted on *2017-07-15 13:25:20* by *jbnimble*

Performing step 8 of 9 with temporary sled and temporary frame, following all instructions on the wiki, and I am having a problem.

When I start the "cut test pattern", the machine starts cutting upward towards the 2 o'clock direction for 7 inches, and then switches direction towards 10 o'clock, and keeps going until it runs off the top of the plywood, and I have to manually stop the cut.

I was under the impression these cuts were horizontal and vertical lines, not diagonal. I went through the previous steps multiple times, so I feel mostly confident that steps 1 through 7 are correct.

What might be going wrong?

---

Posted on *2017-07-15 17:01:02* by *jbnimble*

I ended up manually measuring distances, the chain derived numbers were not working. The test cut appears to be working, but it is not clear to me where to measure the horizontal and vertical lines based on the graphic. I made a best guess, and am moving on.

---

Posted on *2017-07-16 14:34:55* by *jbnimble*

Turns out this was user error, from a manually moving the Z-Axis perspective, and I did not grok that the "cut test pattern" is meant to be run repeatedly until the numbers are equal... RTFM.

---

Posted on *2017-07-16 14:56:42* by *Bar*

That just means the text in the box isn't clear enough! Can you think of how to word that text to make it stand out more that it needs to be run repeatedly?

---

Posted on *2017-07-16 14:56:53* by *Bar*

If you thought it was confusing, others will too!

---

Posted on *2017-07-16 18:31:53* by *jbnimble*

I have a lot of opinions on the calibration wizard, and I'll probably open some GitHub issues with ideas for changes. There is a lot of text, and some of the images are useful. From a UX perspective TL;DR; is real... so being succinct is important. 

In general I feel like having the main UI controls be used/re-used in the wizard as a means to familiarize new users on how to use Ground Control could be a good first step.

For example, I've done the configuration wizard a bunch, so I basically know how many millimeters for the left chain to get across... so being able to manually change the distance to more than 1/10/100/1000 would be useful, and showing new users how to use the main controls at the same time... doubly useful.

---

Posted on *2017-07-16 18:47:10* by *Bar*

Love it! If you make separate issues for each suggestion it's easiest for me to make sure I don't miss anything

---

