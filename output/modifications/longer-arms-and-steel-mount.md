## Longer arms and steel mount plate?
Posted on *2017-05-23 03:19:01* by *jamescampbell*

Hi All,

I came across this ingenious device while searching for a cnc option for our local community mens shed and think it will be a hit with the guys!

In a youtube video, there was mention of a loss of accuracy as you drifted up into the corners of the board. We have no shortage of wall space so assuming I maintained acceptable stiffness, could the motor mounts are be lifted significantly higher (and maybe outboard further too) to help with this? My gut tells me this would increase the working space of the router where both motors have similar effect on the routers positioning.

Secondly, we are quite lucky to have a decent metal fabrication set up, would there be any downsides to creating our own router mount from suitable steel plate to mimic the weight of the bricks in a lower profile design?

Thanks!
James

---

Posted on *2017-05-23 03:30:13* by *davidlang*

Yes, moving the routers out will help the accuracy a lot, up will help some, but too far up and you end up loosing accuracy due to too little tension on the chain when you are at the far bottom corner. You may need to get some more chain, but that's pretty cheap.

There is no downside to using metal instead of wood (or brick), if you are making a metal sled, just make sure it stays slick (care for the bottom of the sled like you would the surface of a table saw) . There is at least one person who has built a metal frame already.

it's worth noting that we are currently experimenting with different angles and weights, so experiment away.

---

Posted on *2017-05-23 03:35:59* by *davidlang*

it's important to keep in mind what the cost is of failing on an alternate frame design.

Not much.

So give it a try!

---

Posted on *2017-05-23 14:16:39* by *silverwarior*

Why not modify the design of your contraption to be able to use four chains (one for each corner)? 

By using four chains you will retain perfect precision in any position since the chains will keep each other perfectly tensioned.
Another benefit of such design is that it could be used both in vertical or horizontal position of the cutting material.

Sure the drawback of such design is greater cost since you now have four chain driving motors. But you can always provide this four chain design as a pro package and also provide sort of upgrade package for people who first bought standard two chain design but need more precision so would like to upgrade to four chain design.

From the software point of view you can just add additional setting which tells the software whether it is only controlling two motors (standard design) or four motors (pro design).

---

Posted on *2017-05-23 14:18:22* by *blsteinhauer88*

That has been suggested,  Creator wants to get the two working first then explore that later.

---

Posted on *2017-05-23 14:35:08* by *silverwarior*

I see. Well I have just found out about this project few minutes ago from a Youtube video and I'm pretty hyped about it. Why? Because recently I was looking about buying or perhaps making my own tabletop CNC machine for cutting wood. But I have never imagined that there could be such cheap and easy solution to this.
Any way because I will require good precision across the entire surface I'm afraid that two chain design would not be good enough. But if creator decides to go out with four chain design I'm definitely buying it. That is if creator will also be chipping to Europe. If not I'm considering of using creators software (if I'm allowed) and creating the chain driving motors myself.

---

Posted on *2017-05-23 14:38:49* by *pyrosrock*

the software is opensource so take what you want and report back on your findings then everyone wins!

---

Posted on *2017-05-23 14:40:13* by *Bar*

Hey @silverwarior, welcome!

All our software, firmware, electronics and mechanical design is completely open source so feel more than free to use any or all of it. You can find the source on our GitHub page [here](https://github.com/MaslowCNC)

I do want to explore the four chain option, but I need to focus fixing all the bugs with the two chain version first.

If you build a four chain one, let us know how we can help and keep us posted with how it's going. There's a great community here that can probably give some good advice along the way, and which would love to see that build.

---

Posted on *2017-05-23 14:44:07* by *davidlang*

what makes you think a 4 chain version will be more accurate than the 2 chain version?

The math is complex enough as-is with the 2-chain version, with the 4-chain version needing twice the calculation (assuming that the math doesn't get any more complex, figuring out the sled tilt on a 4-chain machine seems like it's going to be even messier than on the 2-chain machine) it can only do so by either being less accurate or going half as fast (we're already hitting the processing limits of the arduino in use)

a 4-chain system will be overconstrained, which brings it's own kind of grief to the table

---

Posted on *2017-05-23 15:35:03* by *silverwarior*

Currently with two chain design you lose precision when sled moves close below one of the chain motors because you require much les force to move the sled in the direction of other chain motor which can reduce the tension of that chain.
You can observe this by simply hanging an object on a single rope and then applying horizontal force to it and you will se that at the beginning you need very little force to move this hanging object sideways but higher it gets on its circular motion around the point to which it is attached by rope. Why? Because it is like if your hanged object would actually be on a hill. While on a hill it is ground that it pushing your object in the direction away from ground on a rope it is the rope that is puling your object toward the rope anchor. You can learn more about this by checking the physics of a pendulum object.

But as I mention before with four chain design it is the opposite chains that are keeping each other tensioned since each of them is puling away from your central object (sled). 
It is pretty much like when you are handling with t ablecloth. If you hold your tablecloth only on two corners it will be nicely stretched on center if both of the corners are at the same height. But of you offset height of one corner slightly the table cloth won't be so nicely stretched any more. And in no scenario will that tablecloth be also nicely stretched on the edges.
But if you grab your tablecloth on all four corners you can have it stretched perfectly not only on center but even on the edges.

Any way at first I was thinking about suggesting the use of three chains which would be minimal to achieve decent accuracy over entire work area but setting up three chains (where bottom one would have to be centered perfectly) would be to complicated and could lead to many problems. Why? Because if bottom chain motor would be of center it would lead to uneven tensions on the chains which would lead to even worse accuracy. And in worst case it could even lead to overtentioning of the chains which could then result in damage of the entire contraption.

As for your problems with calculation power I'll take a look at your calculations algorithms to see if they might be further optimized but I can't promise any results since I'm much more versed in Object Pascal programming than in C++ programing that you used.

---

Posted on *2017-05-23 15:48:02* by *Bar*

I talked to the creator of zar plotter a bit at Maker Faire. he's building a four cable machine which you can read about [here](https://www.zarplotter.com/)

---

Posted on *2017-05-23 15:53:16* by *davidlang*

you have less force as the sled is low under a motor, but that doesn't automatically translate to less accuracy.

if you go with three chains, the tension of the bottom chain will be working in the wrong direction when the sled is in a bottom corner, gravity is better there.

if the calculations are correct, and we either have little enough chain sag to not matter, or include it in the calculation, the accuracy will be there (we may just need to lower the allowed acceleration to recognize the limits)

---

Posted on *2017-05-23 16:10:17* by *davidlang*

$950 for the zar plotter, any info on his source code?

---

Posted on *2017-05-23 16:56:33* by *jamescampbell*

Thanks for the input regarding the arms and steel sled everyone, very helpful indeed. I'll measure up the shed walls and see what we can achieve. A quick sketch and a few assumptions having never used the device showed that with the current setup is most accurate when the ratio of the two chain lengths is at a ratio of 2:1 or less (with the top corners currently exceeding 3:1) but if I reposition the motors twice the distance from the corner of the board I would get the chain length ratio back to 2:1 in the top corners. 

As Davidlang said, the cost of a failure is low so worst case scenario is I'd end up with a larger frame and can test multiple motor position along the arm until I am happy!

---

Posted on *2017-05-24 00:34:35* by *silverwarior*

@davidlang
The acceleration is not the only factor that can lower the accuracy. 
The router is also constantly aplying some force to the sled. And that force can be big enough to lower accuracy when sled is under one of motors. And what is worse you can't predict the amount of this force that the router is causing as it is heavly dependant on the wood composition at that perticular spot.

---

Posted on *2017-05-24 05:09:45* by *davidlang*

@silverwarior True about the router imposing some force, but as long as the force is small enough relative to the force from gravity, we should be Ok.

the chain angles range from ~10 degrees to ~80 degrees, that works out to ~3.5 pounds of force sideways in the worst case (based on ~20 pound sled weight)

if you look for the topic "test request" you will see a test that I requested that  someone make to check the worst-case performance in this area. It shows that with two bricks at 15 degrees, or one brick at 10 degrees this does not seem to be a problem (note that the friction of the sled to the wood being cut seems to be a significant factor in this worst-case area)

---

Posted on *2017-07-08 10:19:42* by *rollandelliott*

if you make the sled out of 1/8" thick steel with 18" diameter then it will weight 8.8 lbs. The bricks weigh about ten pounds and one user MakerMark did testing and found that 7lbs is the lightest the bricks can be.  also be aware that 7 lbs weight does not include the plywood sled weight which is around 1.5 lbs. if you used 3/16 or 1/4" steel plate it would be way too heavy. You can always decrease the tilt a little as well.

---

Posted on *2017-07-14 00:06:09* by *cameronswartzell*

Have people experimented with significantly wider spacing of the motors? It seems like much of the trouble with the accuracy in the lower corners is due to one chain being nearly vertical. There have been some suggestions that a wider distance between motors might help the issue. If I were to build my frame to have the motors 18" further out on either side would I need to lengthen the chain? I'm wondering this will cause more issues than it solves, but I can always cut the frame down. Presumably I should move the motors up as well as out. 

I'm building my frame this weekend, likely more in the "stud wall" style seen here https://github.com/MaslowCNC/Mechanics/wiki/Alternative-Frame-design-from-Beta-Testers for a variety of reasons. If anyone has any experiments they would like me to try to implement and report on I can try to incorporate those. I'm already trying a UHMW circular sled.

---

Posted on *2017-07-14 00:27:08* by *davidlang*

play around with the new simulator tool, it appears that the software knowing the precise measurements of the sled make the biggest difference.

---

