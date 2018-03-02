## Full sheet usability
Posted on *2016-11-09 20:00:24* by *wblosch*

The example videos are mostly parts taken from the center of a board. Is there any loss of resolution / accuracy toward the corners of a full sheet of plywood?

---

Posted on *2016-11-10 10:50:06* by *chadzimmerman*

There is coverage on that [here](http://www.maslowcnc.com/forums/#!/hardware-issues:accuracy-towards-extreme-of)

---

Posted on *2017-02-11 10:13:02* by *ian8*

The link above doesn't seem to work anymore.  Can the machine cut to the extreme edges or does the sled become unstable or impact the bottom frame?

---

Posted on *2017-02-11 16:08:57* by *555555*

I would also be curious to see how it does. According to http://2e5.com/plotter/V/design/  it seems only a small section in the middle will give you accurate cuts.

---

Posted on *2017-02-11 16:29:26* by *TheRiflesSpiral*

It's here: http://www.maslowcnc.com/forums/#!/technical-details:accuracy-towards-extreme-of

---

Posted on *2017-02-11 16:42:11* by *chadzimmerman*

Beat me by 15 minutes :P

---

Posted on *2017-02-12 09:22:08* by *ian8*

My question isn't really about the accuracy or the reproducability, but can the sled go right to the edge, or is it going to fall off the edge?  Does the 2x4 along the bottom prevent routing at the extreme bottom edge of the 4x8 worksheet?  Does the backer board need to be enlarged to provide the sled with support at the edges?

---

Posted on *2017-02-13 09:05:33* by *TheRiflesSpiral*

If you absolutely must cut right to the edge of a sheet, you'll need to do some thinking about how to support the router at those extreme edges. 

There are two challenges as I see it:

1) As currently presented, I think you're right that the sled travel at the bottom would be limited if the 2x4 support protrudes past the workpiece. The larger the sled, the more limited you'll be. You could either use a 1x4 instead of a 2x4 or add a filler piece that takes up the distance you need to get the bit all the way to the edge.

2) At the top and sides, it might be good practice to add filler pieces for the sled to rest on past the extremes of the workpiece. This is always the case with a router; if the base isn't supported, cuts become inaccurate and there's a risk of the tool tipping.

The solutions to both of these challenges either a) effectively decreases the usable area of Maslow or b) requires a larger stage on which to place your pieces. If you're only working wit h 4'x8' material, you've got some planning to do. If you can work with smaller pieces, then it's just a matter of creating a stage that incorporates the filler pieces.

---

Posted on *2017-02-13 09:55:12* by *Bar*

+1 for everything TheRiflesSpiral said. The only thing I would add is that to make the sled not hit the 2x4 at the bottom I add a waste sheet behind the main piece of wood being cut which pushes the wood forward enough. 

The 2x4 (really 1.5x3.5) protrudes 3/4inch so when you are cutting 3/4 plywood the sled won't hit it and in fact, the 2x4 provides support for the sled when you are cutting all the way to the bottom. For thinner materials a waste sheet of either 1/2in or 1/4in will make everything align. 

I haven't really got a good system worked out for not falling off the edges yet.

That link to 2e5.com resource is a good one. That is the reason that the motors are lifted up and away from corners of the plywood. We can expand that area a little because the resolution of our encoders are much higher than the stepper motors that simulation is run for, our chains can handle more tension than the string in the simulation and our router/bricks are much heavier than the pen in the simulation. I think the general shape is accurate. The current design of the arms to hold th e motors seems to work well, but we are shipping with one extra foot of roller chain for each motor to allow for the possibility of moving the motors either further out to the left and right, or further up if it can be shown that doing so would give better performance.

---

Posted on *2017-03-23 14:07:11* by *spyker*

I planned to see how it runs first, then possibly extend the sacrificial canvas with another sheet to make it a foot wider in each direction. Then I can have pieces the same thickness of my cut piece to clamp on to support the sled.

---

Posted on *2017-03-24 06:38:49* by *rollandelliott*

looking at the round sled which appears to be about 18" in diameter you would have to increase the work surface about a foot on each side and a foot on the bottom so instead of 4x8, plan on making a 5x10 surface. unfortunately plywood that size is hard to come by, only way to do it is with putting together cuts., however aluminum and steel come in those sizes, but will cost a lot of money and you need to have the machinery to move it.

---

