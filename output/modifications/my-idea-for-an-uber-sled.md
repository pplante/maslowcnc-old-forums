## My idea for an Über Sled...
Posted on **2016-10-27 21:17:59** by **TheRiflesSpiral**:

I love how simple the current sled design is. The one drawback I see is that the chains don't pivot around the tool, making any instability caused by terrible materials or dull tools a potential for positional malfeasance. My solution is quite a bit more complex but accomplishes the goal. I'm sure others will see it and simplify it. I don't think it's too bad for my first Sketchup drawing. :)



This would require 3/4" ply, some 6" schedule 40 pipe, six R6-2RS bearings and some fasteners. (And a Maslow to cut it out) ;-) I think the handles would have to come off the router base too.



I attached an image, but I can make the drawing available as well... not sure how to share it though. [Über Sled](/images/e8/e8uc_ubersled.png.jpg)

---

Posted on **2016-10-27 23:45:58** by **Bar**:

That is awesome! So cool. I love the idea that you would build the standard sled and then use it to cut out parts for an improved one. Can't wait to see it, open source at it's finest!

---

Posted on **2016-10-28 09:42:52** by **rancher**:

Love it RS.  Way better than the crappy one I had in my brain.  Thank you.

---

Posted on **2016-10-28 10:50:15** by **TheRiflesSpiral**:

LOL! It's got a ways to go yet but I'm sourcing fasteners now. I originally started with just two pieces; one with the router/weights/chain anchor and the other just attaching to the chain... until I realized the bricks would crash into eachother at a point about half way up the sheet. *sigh* So 3 pieces it is!

---

Posted on **2016-10-28 15:56:31** by **David Bernard**:

Great design! I like how you have the small bearings ride on the larger pipe. You may want to adjust the position of the bearings moving the two on the bottom closer together to better support the load (always in tension through an arc of 90deg).



Bar: How would this affect the software dynamics? Have you figured out a way to account for the rotation of the sled?

---

Posted on **2016-10-28 18:59:18** by **Bar**:

I haven't got it fully implemented, but I have got plan for how to make the software account for the tilt of the sled. I think this is an awesome idea and I want to support it. It would be easy for me to throw a switch in the software which turned on and off the tilt compensation for testing things like this.

---

Posted on **2016-10-28 23:50:36** by **David Bernard**:

Sounds great! 



Thinking about it more; the load on the bearings will always be directly opposite the chain attachment point.

---

Posted on **2016-10-29 11:43:20** by **TheRiflesSpiral**:

David, that would be true if the sled were supported by only one point; the weight is actually spread between two points and unevenly, depending on where the sled's position is. There's a third force, gravity, that we have to accout for as well. I did, however, rotate the bearings around 60º to place two nearer the forces, rather than one. [Screen Shot 2016-10-29 at 1](/images/tn/tnqj_screenshot20161029at1.40.30pm.png.jpg)

---

Posted on **2016-10-29 14:03:54** by **TheRiflesSpiral**:

Can someone with that Ryobi router measure the base, please?

---

Posted on **2016-11-09 07:43:14** by **TheRiflesSpiral**:

Just FYI if anyone's interested: I visited a Tools Direct this weekend and measured some routers... the base plate on the Ridgid has an OD of just over 6" (I would guess more like 6.0625"). The other router they had was a 1.5hp Ryobi for $58 (a steal at that price!) and its base plate was more like 6.125")



Since I plan on dedicating a router to Maslow, I'll likely pick up the Ryobi, which has the exact same Z-axis lead screw as the Ridgid.

---

Posted on **2016-11-15 16:06:20** by **davidlang**:

IIRC, the ryobi has a 1/4" collet instead of the 1/2" of the ridgid

---

Posted on **2016-11-15 21:12:01** by **karlthorp**:

I love the concept of the über sled but I'm a little concerned that having the arms pivot one over the other might cause some unwanted twisting as one chain pulls over the other, you might be better off having the pivot points nested on the same plane and have the connecting arms on top of the pivots again on the same plane.



All in all, I don't think it would be THAT big of a concern, I just worry about the possibility of the bit binding while cutting

---

Posted on **2016-11-16 11:52:52** by **TheRiflesSpiral**:

I've addressed this with a ring of UMHW (or nylatron) on each of the pivot plates. I haven't posted an update to this design in a bit... I'll do that this evening. I've considered eliminating the bearings altogether and making both pivot plates from one of those slippy plastics; elongation is an issue in that configuration but once I work out the mechanicals I think that would be a better way to go. Much simpler.

---

Posted on **2016-11-16 12:36:03** by **TheRiflesSpiral**:

One thing worth noting is that the purpose of Übersled is to greatly diminish positional inaccuracies when there is a disturbance to the sled... Take a look here: https://www.youtube.com/watch?v=heicyEEYcoM&t=208



At the start is the situation I'm trying to replicate... The situation we have now with Maslow is similar to what you see at 4:09 in that video. Given the weight and forces involved, I expect positional malfeasance to be minimal, and when Bar has the math worked out for the offset angle, really we're probably splitting hairs. The Über sled is purely meant to account for those times when poor materials or a dull bit or uneven surface causes instability in the sled. In these cases, the standard sled could cause positional inaccuracies whereas Über sled may not.



All this remains to be seen... Can't wait to get my hands on one!

---

Posted on **2016-11-16 12:38:06** by **TheRiflesSpiral**:

DavidLang, yes you're correct. With 1/8" bits, it's pretty irrelevant for me since I plan on dedicating a router to Maslow.

---

