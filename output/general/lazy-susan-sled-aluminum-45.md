## lazy susan sled aluminum 450mm settings for ground control?
Posted on **2017-07-06 14:38:44** by **rollandelliott**:

I got my aluminum lazy susan and it is very strong, should be very easy to mount the router and chains to it. $25 plus $20 shipping from CA. I actually bought two, one is a little stiff, and smoemtimes snags,  but other one is perfect. 

Since the current code is meant to compensate for the standard sled, what changes need to be input for a lazy susan type design? space between chains should be set to ZERO? in ground control? 



 http://www.ebay.com/itm/450mm-Lazy-Susan-Aluminum-Bearing-500-lbs-Turntable-Bearings-11282/400574167764?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649. 

So

---

Posted on **2017-07-06 15:42:51** by **Bar**:

I haven't actually tried it, but I would guess that just setting the spacing to zero should do the trick. If you have issues with zero (maybe a divide by zero error somewhere in the calculations) try a very small number like .01 as a work around until we can add proper support

---

Posted on **2017-07-06 16:00:56** by **scottsm**:

@rollandelliott, I’ve got one of those on the way too. I’m wondering how to accommodate the bricks - if I fasten them to one or both of the pivoting portions, that might affect the dynamics. What do you think about this?

 Looks like it will need some work-around for the dust collection attachment as well.

---

Posted on **2017-07-06 19:00:03** by **rollandelliott**:

Im going to use some concentric lead weights or maybe make the  sled out of steel plate. The key is making the weight circular otherwise it creates a torque arm

---

Posted on **2017-07-07 09:38:58** by **stanleykazmierczyk**:

I have just received a reply from a VXB rep regarding radial loads for their lazy susan bearings, specifically the 450mm model mentioned. 

"Unfortunately all of our lazy susan bearings are only designed for axial load. We have had customers use them in a radial application, but applied maybe 10lbs to them, or so." 



I am looking at using a smaller diameter bearing that provides a 2" diameter opening for the router bit and a 90mm outer ring that can be inserted into the 92mm opening in the Ridgid R2200 router metal base.



I am not an engineer, but I believe this type of bearing is more suited for a larger radial load, and a smaller axial load, which is the reverse of the lazy susan type bearings.  Here is one bearing under consideration: 



http://www.ebay.com/itm/TRITAN-ER31-Insert-Ball-Brng-ER-1-15-16-dia-Setscrew-/271877140825?hash=item3f4d23f159

---

Posted on **2017-07-07 10:01:22** by **davidlang**:

it seems that what we want for this design is a slew bearing



https://www.youtube.com/watch?v=5o4Fj8OxkB8&t=14s

---

Posted on **2017-07-07 10:02:31** by **rollandelliott**:

they are very strong easily 30 to 40 lbs, why do you want sucha  small bearing? McMaster.com might have it.

---

Posted on **2017-07-07 10:04:25** by **rollandelliott**:

https://www.mcmaster.com/#5709k92/=18e9ihx 

here you go, they have other sizes and types.

---

Posted on **2017-07-07 10:12:13** by **stanleykazmierczyk**:

Are you saying that the 450mm lazy susan bearings will take 30 to 40 lbs of radial load?

---

Posted on **2017-07-07 10:12:53** by **scottsm**:

I’ve measured 55 pounds of force when my sled is pulled to the point that the bit is at the top edge of the 4x8 sheet. I’m thinking the 450mm bearing will carry that load.

---

Posted on **2017-07-07 10:14:11** by **rollandelliott**:

it's just a guess from me pushing on it while rotating it. way more than the 10 lbs you mentioned.

---

Posted on **2017-07-07 10:16:10** by **rollandelliott**:

if one attaches the bricks and router to the inner bearing circle it will be harder to turn than the other bearing which has less weight and thus less intertia to overcome. depending on speed the maslow is run at one might need two bearings.

---

Posted on **2017-07-07 10:21:31** by **scottsm**:

I’m thinking two bearings will be needed. Might need two different sizes to address the problem of mounting them concentrically...

---

Posted on **2017-07-07 12:37:49** by **davidlang**:

things move slowly enough that the inertia of the different rings is not going to matter.

---

Posted on **2017-07-07 13:22:44** by **scottsm**:

@davidlang, would the torque arm created by attaching the bricks to one or both the pivoting rings make a difference? Can you think of a way to cancel that effect out?

---

Posted on **2017-07-07 14:16:45** by **larry357**:

Just mount it all on a widget spinner 😛

---

Posted on **2017-07-07 15:54:18** by **rollandelliott**:

just mount the two bearings on top of each other with a small space so you can mount the chain L bracket.

---

Posted on **2017-07-07 16:26:20** by **davidlang**:

Taking this approach, you don't want the bricks hanging below the router, you need to have the router and the center of gravity at the point the arms would cross.



So put one brick on one side of the router, and the other brick exactly opposite it so that they balance, no mater how that half of the mount is rotated..

---

Posted on **2017-07-07 17:31:58** by **scottsm**:

I'm not certain I follow - is [this](/images/Qk/Cg/QkCg_maslowswivelsled2.jpg.jpg) the idea? The bricks are balanced with respect to the circle they are mounted to.

---

Posted on **2017-07-07 23:35:50** by **davidlang**:

yes

---

Posted on **2017-07-08 09:24:58** by **scottsm**:

Thanks, that’s doable, then.

---

Posted on **2017-07-08 09:36:58** by **scottsm**:

It looks like good radial support of the bearing races will be important - I bought a ‘used, like new’ unit from a warehouse site and it was ovalled by .75” when it arrived. A poor try at saving money... I’ll have to return that and pony up the full price to a different vendor. 

The aluminum is soft so I guess I’ll look at insetting it to try to prevent deformation.

---

