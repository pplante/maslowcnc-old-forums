## weight distribution on the sled
Posted on *2017-02-17 02:18:42* by *davidlang*

while the idea of using bricks is a great least-common denominator, I was wondering if having the weight higher on the sled (say level with the router) would help any?

one of the parameters for the kinemetics is where the center of gravity of the sled is compared to the cutting bit. Since this is a parameter, it obviously matters, so what would be ideal?

In many parts of the world, small barbells are readily available at thrift stores and similar and a little time with a hacksaw, drill, and tap could easily produce nice metal weights that can be bolted to the sled easily and take less space than the bricks.

---

Posted on *2017-02-17 09:24:17* by *Bar*

I think this is something worth exploring more. I'm not sure what the right answer is. Because it's compensated for in the math I think it would come down to what distribution of weight gives you the best "righting moment" if that's the word, basically what will resist the deflection of the router the most. 

The other factor to play with is where the chains mount to the sled. My gut feeling is that a wider spacing will give more righting force for a given deflection, but I haven't worked it out.

---

Posted on *2017-02-17 21:40:42* by *davidlang*

there's also the issue of 'righting movement' vs pendulum effect.

having the weight low makes the weight keep things more vertical, but it also means that when the movement changes direction (starting or stopping), the mass will lag behind what the chains are trying to have it do.

---

Posted on *2017-02-20 10:43:40* by *Bar*

Great point!

---

Posted on *2017-02-20 12:38:09* by *jbarchuk*

So is it true that to cancel the pendulum that the weight should be higher, level with the router, and as close to the router as possible?
Another effect... Let's say the router is at the center of the work area. Let's say that the chains are mounted to the sled such that they point directly at the center of the router, where the cutting tool is mounted. But of course they can't be mounted -at- the center because of the diameter of the router and base.
(My brain is sooo slow as I get older. I had to draw this next part on paper to visualise it. [sigh])
As the chains pull the router higher, the chains 'point' above the center of the router. I think that provides more stability while adding slightly to the pendulum effect.
As the chains lower the router, the chains point below the center. I think pretty definitely that that reduces stability,
Q: Is there a way to calculate the -optimum- location for the chain mounts to avoid effects that will -hurt- the routing accuracy capability?
My intuitive guess is that the chains should be mounted such that they point to the center o f the router at it's -lowest- point, to provide a baseline stability. Then as the chains pull the router up they point above the center of the router, and add stability, again as I said adding to the pendulum effect.
I'm asking about this, and the motor mount thing, because to -me- the dimensions of some things -appear- to be somewhat arbitrary. I -know- they're not arbitrary, but not being part of the math/design process I don't know what the reasons for those decisions were. For folks like me and others who are not building to 'as designed' size and aspect ratios of the machine we need to know what other dimensional changes to make such that it works on the first try. 'Bar & Co.' have already been through the design/try/fail/modify/try again process and there should be no need for anyone else to need to go through that agony.

---

Posted on *2017-02-20 16:24:41* by *Bar*

Some of those dimensions are not optimized. I've been iteratively improving them and the current dimensions are pretty good, but I'm sure there is room for improvement. My big focus has been to get quality hardware into the hands of the beta testers because as soon as you have hardware there will be more people than just me solving these problems. I've been focusing on things like "is there any flex in the chain mounting brackets" (no there is not) and less on "where they should mount" because since the machine builds it's own parts if we decide they should be mounted higher or lower everyone can cut a new sled. If the steel on the brackets wasn't think enough, it would be much harder to change that.

By the time we ship the bulk of the kits I would like to have those dimensions pinned down, but for now we're focusing on getting you hardware ASAP.

---

Posted on *2017-02-20 19:26:03* by *jbarchuk*

To paraphrase a well known project manager, 'Excellent answer!' :)

---

