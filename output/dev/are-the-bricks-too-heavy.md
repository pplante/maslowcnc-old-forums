## Are the bricks too heavy?
Posted on *2017-04-21 16:15:28* by *Bar*

I've been playing around with the temporary sled as I've been writing the next part of the instructions and it works remarkably well without any bricks attached at all, especially towards the top of the sheet where we've been having issues with the tension being so high that we're slipping chain links, so my question is:

Are two bricks too much weight? Can we get as good or better performance with just one?

---

Posted on *2017-04-21 17:27:04* by *rancher*

I've been wondering the same.  Seems like a lot of load.

---

Posted on *2017-04-21 18:11:25* by *nathanmiller*

very interesting! It's surprising how the whole thing is getting simpler and more efficient. I'm itching to get mine in June.. driving me nuts!! But I'm glad to see so many kinks are being worked out by the beta testers. Really cool to watch the process happen.

---

Posted on *2017-04-21 20:31:48* by *scottsm*

I've got paving bricks that are half the normal thickness; I've been using two on each side. I can take two out and run some tests.

---

Posted on *2017-04-21 20:34:42* by *Bar*

That would be a really interesting test. I think the other variable that might be worth playing with at the same time is the tilt of the bed. My guess is that less weight at a shallower angle might be something to explore

---

Posted on *2017-04-21 20:37:20* by *scottsm*

Ok, I'll run a series. I'm at 17 degrees now, what other angle(s) are interesting?

---

Posted on *2017-04-21 20:39:36* by *Bar*

I would be interested to see how close to vertical we can go

---

Posted on *2017-04-21 20:40:13* by *Bar*

The closer to vertical we get the less friction there is between the sled and the wood

---

Posted on *2017-04-21 20:40:41* by *Bar*

But the less force there is pushing the router into the wood

---

Posted on *2017-04-21 20:53:11* by *mcginniwa*

With this in mind, I wonder if we should track weight of the router on the [Tested Routers List](https://github.com/MaslowCNC/Mechanics/wiki/Tested-Routers-List) as well.

The Bosch GOF 1600 CE I'm going to be working with is 5.8 Kg according to the manual (I haven't weighed the actual fixed base set up yet). What's the Ridged R22002 weigh?

---

Posted on *2017-04-21 20:55:12* by *mcginniwa*

Looks like Ridged R22002 weighs 10.05 lb. or 4.56 kg.

---

Posted on *2017-04-21 21:19:43* by *rollandelliott*

When i get mine in june i think im goimg to try a 1/4" steel base. Heavy but lowest possible center of gravity so high tilt possible

---

Posted on *2017-04-22 00:39:48* by *gero*

Since I have the heavy, 7 kg GOF 2000 CE, I was thinking the same thing after bending one of my motor mounts by going to the top of the sheet. Focused on the calibration right now, but this is next on the list.

---

Posted on *2017-04-22 02:53:47* by *larry357*

Just on my scales minus me 😁, the GOF 1600 is 3.6kg for the router, with cable; 1.3kg for the fixed base and 2.9kg for the plunge base. Then to consider z axis, brackets, platform, chains :)

---

Posted on *2017-04-22 06:43:02* by *davidlang*

The bricks are there to create enough tension on the chains to keep them from sagging and an attempt to keep the sled from sticking.

Going to a slicker sled, tilting the whole assembly closer to vertical, or improving the shape of the sled all reduce the sticking problem (and since the amount of friction is is part based on the weight applied, it's not clear that the bricks help more than hurt)

If the problem ends up being sag in the chains, then we should model it and add it to the math.

So beta testers, try your machines closer to vertical and with fewer bricks, see what happens. The problem areas are going to be the lower corners, and the direction of cut is going to matter. You are going to have more trouble moving away from the opposite motor when the tension is low. Cutting the test shape in the bottom right has been a problem for one person (the bottom right corner ended up being rounded), so I believe that it cuts this in the counter-clockwise direction.

---

Posted on *2017-04-22 08:28:41* by *gero*

The complete mounted sled with the Bosch GOF 2000 CE and 2 interlock bricks is 15.3 kg :-o

---

Posted on *2017-04-23 17:37:58* by *bryanhaven*

Has anyone make their sleds out of Delrin or similar material? High wear resistance and very slick.

---

Posted on *2017-04-29 19:38:26* by *MakerMark*

I lowered the weight of the bricks by over half and have not seen an impact to the cutting quality. I've finished 8hrs of cutting at 45ipm (modified firmware) with an 1/8th bit since the change.  I captured the motor PID data from running the calibration before and after. I'm not sure what all the numbers represent exactly, but figured I'd shared. They might be helpful to someone here ;)
Left 4.5lbs = 72 & -31
Right 4.8lbs = 77 & -28
Left 1.1lbs = 56 & -31
Right 1.1lbs = 63 & -32
@bryanhaven - I hope to build a new sled next week using PTFE. A friend set aside a remnant from a project for me to test. I'll post the updates here.

---

Posted on *2017-04-29 19:40:23* by *Bar*

That's a fantastic result! Quantitatively the numbers really just tell you that the machine noticed the lower weight of the bricks, but the fact that the cut quality was the same is great news! Thanks for sharing those results.

---

Posted on *2017-05-03 09:07:05* by *MakerMark*

As an update, I had issues with the lighter sled when using a 1/4in bit @ 25ipm with 1/4in depth cuts.  The top of the sled would lean away from the cutting surface. Adding the weight back to the sled corrected the issue @25ipm. With the added weight I was even able to increase the speed to 45ipm without issues. I'll run a few tests tonight to determine the minimum weight needed for the 1/4in bit @ 45ipm.

My MaslowCNC continues to be a workhorse! Last night I ran a 6hrs continuous job running using a 1/4in bit @ 45ipm. I estimate that I have ~35hrs of cutting time on mine. To improve it's longevity, my next modification will be to replace the screws that hold down the motor mount with bolts. I've had to tighten down the screws after each long cut job. Minor tweak to handle all the abuse that I give it ;)

---

Posted on *2017-05-03 09:10:48* by *Bar*

Beautiful! Thanks for the update, keep us posted as you learn more.

---

Posted on *2017-05-03 09:41:13* by *scottsm*

6 hrs at 45ipm - that's a quarter of a mile! It sounds like an interesting project to be sure.
 Let's add an odometer to the enhancements list :)

---

Posted on *2017-05-03 09:53:22* by *gero*

No bricks would force me either to go quite a bit out with the chains on the brackets and the motor mounts, or increase my angle heavy.  [No-bricks](//muut.com/u/maslowcnc/s3/:maslowcnc:pNFB:nobricks.jpg.jpg)  Can't wait to catch up with you guys.

---

Posted on *2017-05-03 14:35:16* by *rollandelliott*

Gero wow big gap! Id fix that cant be good for long time usage. Maybe recess motors. Higher chains just makes for more slack right?

---

Posted on *2017-05-03 22:33:03* by *davidlang*

no, moving the chains out from the workpiece doesn't add more slack (especially if you move the motors out as well)

---

Posted on *2017-05-04 01:11:45* by *gero*

@rollandelliott I was not planing to cut like that :-). Was just a look at the sled without bricks. If I wanted to cut without bricks I have 5 options to get the sled back flat on the  sheet. 1 ) tilt the frame more out (am at 6`), 2) move the chain on the sled out to the last hole (move motor-mounts out the same distance), 3) move the brackets to the edge of the sled (they are closer to the router now), 4) put weight back on, 5) a combination of the other 4.

---

Posted on *2017-05-04 04:23:40* by *rollandelliott*

Slack was the wrong term. The Higher the chains the less stable sled becomes. Creates unecessary torque moments.
In theory one wants the mounting points as low as possible.

With any design optimally the sled should be flat with or without weights

---

Posted on *2017-05-04 05:42:41* by *MakerMark*

3.4lbs bricks were the minimum weight needed to keep my sled stable at 45ipm using a 1/4in bit.

---

Posted on *2017-05-04 07:09:18* by *scottsm*

That's two bricks of that size, right?

---

Posted on *2017-05-04 09:53:48* by *MakerMark*

Correct. 2 bricks that weight 3.4lbs each totaling 6.8lbs.

---

Posted on *2017-05-04 12:28:55* by *davidlang*

@rollandellitott,

having the chains further from the workpiece doesn't increase the torque on the router, it does give the chain a longer lever arm on the brackets, so if they are not strong enough, they can flex.

but if you remove half the weight from the sled, and move the chains out twice as far, your flexing force should be the same (chain tension scales with totoal sled weight and the bricks are about as heavy as the router).

so I don't think that this is likely to be a significant factor. If it is, it's also something that's relatively easy to fix with stronger brackets.

---

Posted on *2017-05-04 12:50:49* by *scottsm*

The brackets are 0.225 inch steel.  I haven't seen any flexing there.

---

Posted on *2017-07-08 10:01:13* by *rollandelliott*

so has anyone tried changing the tilt? I'm guessing two standard bricks weight 10 lbs? so MakerMark says you can save about 3 lbs. anyone done testing?

---

Posted on *2017-07-08 11:41:02* by *gero*

I have reduced the weight of the bricks by ~ 60% and increased the tilt from 6 degree to 10 degree. It means nothing because it can't be compared.
There are 2 ways to go about this. The main question is if we take modified builds into account, or only compare standard builds.
In any case there should be a group of at least 10 to do the same defined tests with different parameters to get a hint on where to go. A spreadsheet with all parameters is a must, including things like the center of gravity.
I have a pretty heavy router and the bricks here are some local invention with no standard weight. At some point we should start actually weighing.
Someone (I am not looking at David :-)) needs to create a series of tests going + and - 25% to see where we are and where the target is.

---

Posted on *2017-07-08 11:51:33* by *blsteinhauer88*

I did a tilt test for Davidlang at the extreme lower edges of the board.  It showed more weight and about 10 % was best.  I will try and find that. photo of results.

---

Posted on *2017-07-08 11:55:13* by *blsteinhauer88*

[IMG_0256](//muut.com/u/maslowcnc/s3/:maslowcnc:7Y1h:img_0256.jpg.jpg)

---

Posted on *2017-07-10 08:10:21* by *khandam*

thanks,, but test was done with out sliders, and I think most people will be using sliders, so i will have to redo some testing.

---

Posted on *2017-07-10 10:36:52* by *blsteinhauer88*

I used furniture sliders in the beginning but left them off my next sled  because after several uses the wood actually scratched them up and they weren't as useful anymore. A good sanded plywood sled on sanded plywood slides just fine.  But give it a shot and see what yours looks like.

---

Posted on *2017-07-10 12:17:52* by *mrfugu*

I don't have my MaslowCNC yet, but as part of the process of pre-building my 1st stage sled I took the opportunity to cover the surface with some packing tape (clear plastic) and have a fairly slick surface with the added benefit of covering over the recesses for the mounting bolts.

---

Posted on *2017-07-12 21:09:27* by *jamesmcguire*

couldn't using something like a sink cut-out or something with formica on one side be slick enough?

---

Posted on *2017-07-12 22:16:49* by *davidlang*

anything that decreases the friction is an improvement, we've had lots of different suggestions, but only a few tried so far.

---

