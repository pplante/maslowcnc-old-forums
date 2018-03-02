## Lazy Susan
Posted on **2017-06-03 03:53:49** by **stevejorgy**:

Just found your CNC router, Wow.
My first question.
If the chain cables always pointed thru the router bit by using two pairs of Lazy Susans, would not the math become simple and bit position would not be affected by change in drag or cg position?

---

Posted on **2017-06-03 04:18:01** by **TheRiflesSpiral**:

The math would be simpler, yes. The other metrics have yet to be measured... several (including myself) have plans to create a sled of this type once we ge our hands on one.

The primary issue is that a sled like that could be costly or complex (or both).

---

Posted on **2017-06-03 05:23:15** by **stevejorgy**:

Quick look and found a whole selection for $30 a bearing. Select two concentric bear sizes and secure to the plywood sled.  
https://www.vxb.com/450mm-Lazy-Susan-Aluminum-500-lbs-Turntable-p/kit11282.htm
Has anybody done this before.  I am assuming this explains accuracy issues at extreme travel.  My second question is the accuracy.
I see people measuring 6" squares in different location on a panel.
I hear the squares in the sweet spot are good to +/-  1/64 and +/- 1/16 at the extremes. You can think of accuracy as absolute (machine slop) or scaling issue such as paper plotter. I hear the accuracy being discuss is it the change in the 6" square (the 6" dimension)? So if I have pattern of squares and the two end squares are modeled 7 feet apart should I be expecting them to be 7' +/- 1/64" (slop method) or the percent method ((1/64)/6") 7' +/- .219"? Please tell me it is not percent.

---

Posted on **2017-06-03 05:29:31** by **TheRiflesSpiral**:

"I am assuming this explains accuracy issues at extreme travel"

No, I don't believe so. As far as I've been able to glean from discussions surrounding the remaining variances, the critical variables have to do with dimensions (between the motors, between the chain attachment points on the sled, etc) and perhaps the shift in pivot angle around the sprocket.

I think if anyone believed the calculations surrounding the sled mounting method was the cause of the variance, one of the beta testers would have tested a sled that eliminated it.

---

Posted on **2017-06-03 05:43:40** by **stevejorgy**:

What about accuracy question? Is it percent or absolute?

---

Posted on **2017-06-03 07:25:55** by **Bar**:

I think the lazy suzan is a great idea. I'm holding out that a software soultion will keep the cost and complexity of the machine down, but part of being open source is that we encourage everyone to try different things. It's possible I'm wrong and the lazy Susan will make the machine even better.

The accuracy question is a good one. It's a bit of both. We're not looking at an issue where say the encoders are %1 off or something like that where the error would be a constant percentage of the size of shape. Instead TheRiflesSpiral is right the accuracy has to do with how well the self calibration routine can determine the machines true dimensions. The positioning error does end up scaling with the size of the shape being cut, but not in the way one might think. The x accuracy is quite good, and the y accuracy scales in relation size of the shape being cut so a 7' run horizontal is likely to have 1/16th inch of vertical error or bend to it. The distortion is very non-linearly distributed across the sheet so more at the edges. Worst case cenario we can cut a grid, measure  the distance between each of the points on the grid and add a correction term to the internal math. I think we can come up with something more elegant and less time consuming than that. The first step in that direction is to write a graphical simulation of the machine so that we can observe the effects of error in different measurements without having to run a test cut every time.

---

Posted on **2017-06-03 08:09:35** by **TheRiflesSpiral**:

Ooooooooohhhhh simulations... that's fun stuff. Is there a software package you're using to do that or is it something you're developing?

---

Posted on **2017-06-03 08:51:05** by **stevejorgy**:

I would think each machine will have different total sled weight (sled + router + bricks) this variable would distort position map for every machine. Do to high chain stress condition at top middle compared to low stress bottom right or left. You would need to add weight value for starting input. I would think carefully putting in all these starting variables is too hard and will never eliminate distortion just minimize it. I would think starting with carefully drawn 12" grid points on the base panel would step one. Then record the both sprocket positions for each 32 grid points manual targeting each point. Now we can have the computer (excel spread sheet) review the best correction constant to be added to the governing formulas to produce square and accurate cuts.

---

Posted on **2017-06-03 09:07:50** by **davidlang**:

If you go through the math, you will find that the weight of the sled cancels out and doesn't appear in the final calculations.

The droop of the chain does have an effect, but it's on the order of +- 1/32 of an inch at the extreme bottom corners. That doesn't account for the errors that we saw a few weeks ago when we last did a bunch of tests.

Bar has mentioned that after the recent updates, things are better, but we haven't had any testing for accuracy done since the major changes a couple weeks ago.

One problem with trying to use the lazy susan bearings is that they are designed for vertical loads, not side loads, and many of them will fail and pull apart under side loads.

---

Posted on **2017-06-03 09:34:16** by **davidlang**:

The math is much simpler if the chains do point directly at the bit.

We don't know if that would solve the accuracy issues or not, nobody has built such a sled yet.

---

Posted on **2017-06-03 18:30:32** by **rollandelliott**:

http://www.ebay.com/itm/350mm-Lazy-Susan-Aluminum-Bearing-400-lbs-Turntable-Hardware-Parts-13-8-inch-/360690938708?hash=item53fadaf354:m:m5ce7D9JjwipoK-4j91n6MQ

---

Posted on **2017-06-03 18:31:26** by **rollandelliott**:

400mm lazy Susan enclosed bearings $23 on eBay I have one just waiting for my kit to arrive to test out

---

Posted on **2017-06-03 18:33:46** by **rollandelliott**:

In bulk two laser cut circles to attach chains to lazy Susan might add another $20 to cost.

---

Posted on **2017-06-05 15:23:02** by **stevejorgy**:

When does your kit arrive?  Can't wait for your results. You are planning to buy two concentric bearings, one for each chain, Right?

---

Posted on **2017-06-05 16:18:02** by **gero**:

I would like some feedback on how the Lazy Susan, from your opinion would react to squares, meaning direct x-move to y-move changes. From my novice opinion it would add overshoots at the corners. My initial thought was having a wire ring with v-carved bearings to attach the chains. Since I had fantastic results on low speed, I dropped the idea because wanting to go faster. Kindly share you thoughts.

---

Posted on **2017-06-05 16:48:48** by **mrfugu**:

It would seem to me that the proper place for low cost and simplicity to locate any bearing system would be at the chain attachment point to the sled.

---

Posted on **2017-06-05 16:52:35** by **fly-fast**:

> @stevejorgy
> the math become simple
You are correct.  Interesting approach.  When does your Maslow arrive?  Can you take lots of pictures and post results?

---

Posted on **2017-06-05 17:05:43** by **davidlang**:

Last I heard they were waiting on the motor controller boards, so expecting late july or august for shipping out kits.

---

