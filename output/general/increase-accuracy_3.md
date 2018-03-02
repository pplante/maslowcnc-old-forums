## Increase Accuracy
Posted on **2017-05-23 15:38:48** by **cpt_adama**:

Ultimately, if you want to increase the accuracy especially at the edges your going to have to replace the bricks with the motor and chain assembly at the other two corners. You need that router to be able to traverse the diagonals very accurately and having 4 chain and motor setup should solve this problem.

---

Posted on **2017-05-23 15:54:56** by **davidlang**:

show your explanation, not just assert this.

yes, in the bottom corners the forces of the chain are lower, but why does that mean less accuracy rather than just a lower speed requirement?

---

Posted on **2017-05-23 15:55:10** by **justinlauzet**:

(This forum has a button that nukes your reply with no warning!). 

I'll try to recreate my 1st reply.

You seriously beat me by just a few minutes with this suggestion - I was trying to get logged in, and once I did your msg was 2m old:-). 

I think you don't need 4 chains, I think you need 1 chain and 4 motors, and can lose the counterweights (bungies).

The four motors go on the corners, and there's an extra sprocket on the router sled (under the hose pipe).

 If I label the corners with motors with compass directions, and call the router C, it would connect like this: 

NE -> C -> NW -> SW -> C -> SE -> NE

I think the length of chain is constant.  Losing the bungies would get rid of a lot of slop.

Now you now longer need a motor infinitely strong to get near the edge.

---

Posted on **2017-05-23 15:57:53** by **davidlang**:

the length of the chain is not constant, as your triangles change, the total length of the sides change.

do the math, plot out if you are in the center vs at one of the left or right edges and you will see that the total length would be different.

In addition, how do you change the position of the sled on the chain to get chain from one side of the sled to the other?

---

Posted on **2017-05-23 16:02:06** by **davidlang**:

The chain length calculations are far uglier than you can imagine without trying to work through them yourself, especially once you take into account the different tensions involved on each side and the resulting sled tilt.

---

Posted on **2017-05-23 16:02:46** by **davidlang**:

but again, this is all open source, try it and see. I could be wrong and your way will be afar better.

---

Posted on **2017-05-23 16:02:52** by **justinlauzet**:

Yes, the triangles change, but there are corresponding triangles changing on the other side... 

The sled moves the same way as it does now - the sides of the triangles get bigger.

---

Posted on **2017-05-23 16:05:44** by **davidlang**:

but not by the same amount that the others get smaller. And with a single chain, how do you get the extra length from one side of the sled t the other?

---

Posted on **2017-05-23 16:09:24** by **davidlang**:

and if this design with twice as many motors is more accurate, how much more accurate will it be? does it improve accuracy from 1/64" to 1/128" or from 1/64" to 1/70"?

---

Posted on **2017-05-23 16:10:45** by **justinlauzet**:

So you can't imagine how it works, but it must be wrong in 2 different ways, is about the gist I'm getting.

There's no extra length. If you want the sled to drop,   NW and SW rotate Clockwise, and NE and SE rotate counter clockewise

> and if this design... 

Wow guy, what's your deal? 

How would I know this? It's an idea on a forum on a website.

---

Posted on **2017-05-23 16:23:12** by **davidlang**:

trig functions are not linear, if you increase the height of a triangle by 2x the length of the sides do not increase by the same amount that taking another triangle down to a flat line would decrease.

you haven't modeled this or calculated the chain lengths for any of the situations, but are asserting that the total chain length is constant. I've done the math and it isn't.

You also say you can run a single chain around four motors and the sled and then run the motors in different directions at different speeds. If they are solidly connected by chains, you can't do that.

you say that if you want the sled to drop, NW and SW rotate in one direction and NE and SE rotate in the other direction, but if you want it to move left to right, now NE and SE will need to move in opposite directions.

So the single-chain approach you are suggesting, does fail in two different ways.

Even if you have four different chains, nobody has explained why this will result in more accuracy (I agree that it can result in more force), let alone how much more accuracy this will result in. I do n't see how the additional force results in more accuracy, but am willing to admit that I could be wrong.

I can easily see a 4-chain machine moving faster, but since it would double the cost of the machine (or at least come very close to doing so), I don't see that as a must-have.

---

Posted on **2017-05-23 17:28:11** by **scottsm**:

@justinlauzet, this sounds sort of like the mechanism behind a [parallel drafting ruler](//muut.com/u/maslowcnc/s1/:maslowcnc:seMZ:parallelstraightedge.jpg.jpg) . Is that right?

---

Posted on **2017-05-23 17:39:00** by **justinlauzet**:

I modeled a few scenarios, and you're right that the length of the chain as I explained it would need to vary - seemingly impossibly. The shortest chain gets you to the center, and moving towards a corner requires a longer chain. I'm not remotely bent out of shape about this. From my POV, I was spitballing on a friendly forum where discussions and spitballing takes place (or should). 

> but if you want it to move left to right, now NE and SE will need to move in opposite directions.

This isn't true for what I was describing. If you want it to move right, all motors would have turned clockwise, just at different speeds. The sled would terminate chain and the clockwise on NE would shorten it, the clockwise on SE would pass the length through the sprocket back on the sled, giving the length to the other side. But NE and SE can't turn at differnet speeds, obviously. It would take more engineering to solve this problem. 

Anyway, it doesn't matter, I agree one chain is out. It was an interesting idea while it lasted.

I still think 4 motors is worth thinking about.  Even if  one can't say the % of accuracy improved until it's attempted and observed. 

The benfit isn't speed for me (but if you get speed too.... people will like that), but accuracy at the edges, which sounds like the issue if what he (Bar) said in the Tested video is accurate. It's not just this project - other "vplotters" have issues with edges too; From what I've seen they just ignore this and make the plotter wider, since most of these are for drawing with sharpies and not something that should be as accurate as possible like a CNC mill should be.  

The idea why (why more accurate) is that additional motors can pull the motor more snugly towards the edges.

Imagine going left.  The more left it goes, the more difficult left becomes to go.  

Is that not the issue in a nutshell? (not a sarcastic question)

The current design requires gravity to pull the slack given by the NE motor. Another motor in the SW corner means it can pull that slack accurately. A SW motor gives you a truer westward force that stays more accurate further to the edges (It seems that way, anyway).

As for cost, anything sub $1000 is a huge win if it competes with a 4x8 table in terms of accuracy all the way to the edges. And when we're talkign about routers my main goal would be accuracy. And yeah, give me an extra 64th of an inch even that's all an idea gets me - but I got the impression the edges were a bigger issue.

---

Posted on **2017-05-23 17:40:11** by **justinlauzet**:

@scottsm yeah - thats similar to what I was describing :). It does seem to fail with left/right movement however.

---

Posted on **2017-05-23 18:06:29** by **larry357**:

best is to put a couple of screws in a bit of wood and put string around it, to see how it will move and work. An other idea which someone on this forum is already doing is mounting the motors directly on the sled.

---

Posted on **2017-05-23 18:24:18** by **Bar**:

It might be worth checking out the CoreXY system which is similar

---

Posted on **2017-05-23 18:28:44** by **davidlang**:

Ok, now we can discuss things :-) Jumping in and "you are doing it wrong" with your first post isn't a good discussion opening.

In theory, the limitations of accuracy at the edges is due to the chain being slack (sag in the chain), but with the current software, that's not the limit we are running into (and we could compute the sag in any case). The limitations of accuracy from that are well below where we are (around 1/40" per my calculations, very close to where we are aiming)

we aren't running primarily into position errors left-to-right (which is what  too little tension would result in), we are seeing variation top to bottom, even in the center where tension is not a problem.

The new PID loops should help a lot (once we get them tuned so they don't chatter as they currently do), and then we can see how close we are.

---

Posted on **2017-05-23 18:31:19** by **davidlang**:

@bar, CoreXY is designed for a machine with rails, it requires a cartesian movement framework. in theory (if the tension is high enough) you may be able to get away without the outer rails, but you still need the crossbar and the movement along it for the second axis.

---

Posted on **2017-05-23 18:32:53** by **davidlang**:

As far as the 4-chain setup being faster, I think a lot of people would sacrifice speed for 1/2 the cost of the machine

---

Posted on **2017-05-23 18:36:42** by **davidlang**:

you could try to attach the NW and SE chains together (and NE/SW pair) with a spring/bungee cord, but since the resulting tension of the second chain would be unpredictable (or at the very least, variable based on where you are), which would make the nasty math even harder to figure out.

---

Posted on **2017-05-23 18:42:19** by **davidlang**:

for those new to the conversation, let me point out http://lang.hm/maslow/maslow.png and http://lang.hm/maslow/v-plotter.py

This plots out what a machine of this basic design is able to cut, given the min/max tensions motor spacing/power encoder accuracy and desired final accuracy. It's very easy to increase the cut area by just moving the motors a little further apart.

But we have had accuracy problems even in the good areas, so increased tensions with incorrect math won't help us.

---

Posted on **2017-05-23 19:50:32** by **TheRiflesSpiral**:

CoreXY accomplishes bi-directional force with stationary motors; the current designs are all suspended spindle but I think it could be adapted to drag a router over a surface instead (likely with the motors on the sled?)

---

Posted on **2017-05-23 22:03:10** by **davidlang**:

Assuming that the setup is as documented at http://corexy.com/theory.html (for consistancy), the relationship between the pullys on the cross bar and the router must remain the same, as the router moves up and down, the pullys must move up and down by the same amount. They also have to resist quite a bit of tension.

This pretty much guarantees that you have to have a solid bar across the machine. It may be possible to float that bar on the driving lines, but I would not trust that to remain accurately positioned and not at least shimmy side to side (and given the accuracy we are aiming for, it will move side to side FAR more than our allowed error). The only think keeping it moving side to side is the tension * sin(angle of error), and at tiny angles, that's not much force.

If I was looking to make a gantry version of the maslow, I would seriously consider this (a horizontal rail across the top of the machine and then a vertical moving rail down from there)

---

