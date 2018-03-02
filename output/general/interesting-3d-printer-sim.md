## interesting 3d printer, similar concepts to maslow
Posted on **2017-04-01 02:27:38** by **davidlang**:

image

https://camo.githubusercontent.com/f84865d0937855f81b79986262bdf947ec273e52/68747470733a2f2f766974616e612e73652f6f707233642f74626561722f62696c6465722f53696465766965775f726f745f6c6974656e2e4a5047



video of it in action with interview/explination

https://www.youtube.com/watch?v=Jk4fhQvNoaM



github repo of the code/instructions

https://github.com/tobbelobb/hangprinter



instead of having a set of rails, this printer is suspended from overhead with three tethers going horizontally. With motors for each of the four lines (all mounted on the center), it can move around in 3d and print throughout a large area.



Once we get our maslow kits up and running, it would be interesting to consider extending the concept to true 3d capabilities like the hangprinter has.



It's interesting that he talks about measurements being +- 1cm as being "good enough" for his printing, but he does limit the printing to a reasonably small area of the overall footprint.

---

Posted on **2017-04-01 08:28:06** by **Bar**:

What a cool idea! I think he reached out in the KS comments during the campaign so I know he's interested in collaborating if the Maslow community wants to work together with him. What a cool guy!

---

Posted on **2017-04-02 17:33:44** by **nathanmiller**:

what a fascinating idea!!!

---

Posted on **2017-04-02 17:36:44** by **nathanmiller**:

Of course, the thought then is could heavier wire/cable move a Rigid router around and cut wood? (totally removing the need to build a frame)

---

Posted on **2017-04-02 18:47:04** by **davidlang**:

I've been thinking along similar lines. 



Using chain would be a lot harder (not too hard on the horizontal lines, if you make teach end able to swivil)



what to do with the extra chain after you take it up is a hard problem



and the vertical axis would be a much harder thing to do.



but if I'm seeing the prices correctly, the 3d printer should be able to be built for <$100

---

Posted on **2017-04-03 13:02:32** by **nathanmiller**:

The way they have everything tensioned it seems like cable would work really well. But one doesn't really know until it's tested.

---

Posted on **2017-04-03 17:56:54** by **davidlang**:

The problem with cable is gripping it and winding it.



On the hangprinter, they have a problem even using thin fishing line that as they wind it around the pulley, one rotation of the pulley winds more line than the prior rotation. they even have a problem that one of the three vertical lines is consistently taken up a little more than the other two (they did a 20' tall print and noticed that the printer started tilting as it went higher)



using heavier lines like a router would need would make the problem worse.



If instead of winding a line around a big pulley and counting the rotation o the big pulley to get your amount of line, you were to just use the big pulley as to take up the slack, and used something else to do the pulling and measure the amount of line, you would avoid some of this problem, but you would have the problem of how to accurately grip and measure the cable.

---

Posted on **2017-04-03 20:29:03** by **nathanmiller**:

@davidlang Excellent points. I never would have thought about the spool creating a problematic variable over time. Very interesting.

---

Posted on **2017-04-04 19:14:06** by **kc8kzn**:

the drum is good for pulling, but bad at positional accuracy. a pinch roller would be horrible for pulling but can track motion very accurately. use an encoder on a pinch roller to track the cable, use the drum for uptake and pulling. control the drum motor with the signal from the pinch roller.

---

Posted on **2017-04-04 19:24:47** by **Bar**:

Slick idea!

---

Posted on **2017-04-04 19:26:54** by **kc8kzn**:

not really mine. i have seen DRO systems on knee mills working this way simple rough wheel running on the back of the table

---

Posted on **2017-04-04 19:28:39** by **Bar**:

Still, great transfer of the idea to this application. Plus, if you use a small radius pinch roller, the point the cable feeds out from is very constant unlike a large spool where the feed off point might move by several mm.

---

Posted on **2017-04-04 22:05:09** by **davidlang**:

in this design they run all the lines through the types of loops you use on a fishing pole, so they don't move very much.

---

Posted on **2017-04-04 22:06:01** by **davidlang**:

they are talking about a future version using servos or motors with encoders rather than steppers. They think that will translate into significant weight savings, which will let them move faster.

---

