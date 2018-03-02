## cut request, exploring the machine limits
Posted on *2017-02-22 19:21:18* by *davidlang*

I'd like to see a test that explores the machine limits, using something like:

https://www.amazon.com/Woodtek-Forming-Diameter-90-Degree-V-Groove/dp/B0084IUSBG/ref=sr_1_21?ie=UTF8&qid=1487680250&sr=8-21&keywords=v-groove+router+bit+1%2F2-inch+shank+90-degree

I'd like to see full-depth cuts in a single pass and see the fastest the machine will cut reliably under adverse conditions.

Since the limit to accuracy is when a chain is under very little tension, the worst area is the bottom corners. I'd like to see you shift the wood to the left a foot or two and do cuts outside what is the normal cutting area.

I'd also be interested to learn where the limits to the cutting area would be if you left off the weight of the bricks.

In part, this is to learn where the limits are, and try to reverse engineer the proper parameters for the v-plotter.py software, but it's also to be able to get pictures and video to show how to tell when you are running into problems, what it looks like both on the finished product and as the machine is cutting.

for accuracy, it sounds like cutting  circles that result in a small diameter of uncut wood is a good test.

another test I was thinking of was seeing the bit transition from a cut area to an uncut area, or from clear wood to a knot (perhaps do a test cutting on a piece of 2x12 with knots instead of plywood?&quest;)

and another test is that different angles/directions of cuts probably result in different loads on the chains (I would guess worse as the chain with low tension is being let out) so a star/asterisk of cuts from a central point out to different angles and see how straight they are may be an interesting test

---

Posted on *2017-02-23 06:15:43* by *paulhart*

Agreed, it would be good to see a full-range test. There's been a lot of discussion on this topic already, for instance this page:

http://www.maslowcnc.com/forums/#!/modifications:rabbit-ear-motor-mount-dime

I'm curious to know if the comments made there are accurate - they suggest that the working area of the Maslow design is almost the entire sheet.

---

Posted on *2017-02-23 09:21:56* by *davidlang*

well, the design is that the working area should be the full sheet, the parameters I picked for that plot are based on the idea that the full sheet is usable.

And while I use 0.2 * sled weight as the minimum tension, that shows the bottom corners being marginal, but I didn't feel like bothering to tweak it down to additional decimal points, since I don't really know where the limit is.

That's why I'm asking for this sort of test, to find where the limits really are.

---

Posted on *2017-02-23 11:21:52* by *Bar*

I think those are great suggestions. I'll add them to my list.

---

