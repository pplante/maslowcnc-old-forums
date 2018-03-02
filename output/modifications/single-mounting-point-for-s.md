## Single mounting point for sled
Posted on **2017-06-09 16:22:52** by **mocajoe1**:

Has anyone tried to use a sled with a single point to mount both chains to? It seems like there is a lot of effort to design around the issue of the sled pivoting as it moves from end to end. If the chains are mounted at a single point, the center of gravity of the sled assembly becomes irrelevant, the assembly doesn't pivot at all, and the design can be further simplified with greater accuracy to boot.

---

Posted on **2017-06-09 16:49:19** by **davidlang**:

actually, in that case the sled will swing like a pendulum when it starts and stops, which is a different type of error to try and deal with.

---

Posted on **2017-06-09 17:05:18** by **mocajoe1**:

Would it? I could see that point if the cutter moved at a faster speed, plus the friction of the sled on the cutting surface would dampen any actual swinging action. Also, with center of gravity no longer a concern, the weights can be moved farther out for greater leverage, in fact you could probably go down to a single weight directly below the sled.

---

Posted on **2017-06-09 17:22:28** by **davidlang**:

moving the weights further out just makes the problem worse.



if the system is moving horizontlly at full speed and hits the end of the motion and stops, the sled will want to continue moving.



But in any case, give it a try, adjust the machine dimensions to say there is no distance between the chain anchor points.

---

Posted on **2017-06-09 17:45:48** by **glenboudreaux**:

I think I understand the mechanics he is describing... Here is my poor attempt at trying drawing it out  [Mount points](/images/Mo/X4/MoX4_mountpoints.png.jpg)

---

Posted on **2017-06-09 19:04:05** by **davidlang**:

The idea of putting bearings around the center of the sled so that the chains are always directed to the center of the sled where the bit is has been raised many times. So far nobody has built one, or at least nobody has reported the results of trying it.



We also have not had anyone do a test and report back how accurate things with the latest software (other than a note from bar that when he cut the table it was much more accurate.



So we don't know if the problem has already been solved, and we don't know how well this change in sled attachment would work.

---

Posted on **2017-06-09 19:18:52** by **mikeberg**:

I think the actual fixation points is ideal for having a good isostatism (x,y,z) with 2 chains separately and the weight of brick     those 3 points can push equally and more easily than 1 fixation on upper point  and the weight of brick down

---

Posted on **2017-06-10 12:21:40** by **ylexot**:

I don't know glenboudreaux, I read that to mean that the single mounting point would be at the top of the sled.

---

Posted on **2017-06-10 18:31:18** by **kneelo**:

I have been thinking about this issue quite a lot recently.  



Having a single mounting point for the two chains that is offset from the router bit would make it easier to calculate position but mean that the cutting force on the bit would act to rotate the sled about the chain attachment point adding inaccuracy.  You would need to move the sled COG as low as possible and slow cutting speed to try to counteract this as much as possible but you could never eliminate it.



Having the chains pivot about the router centreline is really the only solution I can see and would seem to deliver a lot more accuracy and potentially faster cutting speeds.  



I am waiting on the delivery of some motors but have a concept that would use a lasercut semicircle strip and a couple of rollers that should work and be relatively cheap and easy.

---

Posted on **2017-06-10 19:14:56** by **davidlang**:

one thing to remember with that design, the torque of the router will tend to rotate the sled until one of the chains hits a limit 



that's not necessarily a fatal flow, just something to account for.



This design has been suggested since the very early days of this forum, we just need someone to build and test it (and be able to compare the accuracy with the standard design)

---

Posted on **2017-06-10 20:06:40** by **rollandelliott**:

I will be making a lazy susan type sled when I get my maslow in a few weeks. Should the lazy susan be large or small. I can get them anywhere from 6 to 20' in diameter. I was thinking of a larger 18" one would be more stable.

---

Posted on **2017-06-10 20:50:15** by **davidlang**:

as long as it doesn't interfere with the router and is strong enough to handle the tension on the chains, the size shouldn't matter.



The biggest thing to watch out for is the strength of the bearing. They are rated for the weight they support  when flat. In this case the load is sideways, and the load can be quite a bit.



if both motors are pulling at max power (top center, trying to go higher), there is about 130 pounds of force between the two chains. Now, this has been enough to pull the wood of the sled apart, so the machine should not ever see this much load in real life, but if you are testing bearings, you should test them out to the max stress the machine could produce and have some safety margin.

---

Posted on **2017-06-10 21:00:01** by **blsteinhauer88**:

@davidlang, where on the bearing would you say the chains would best be mounted? 3 and 9 or 10 and 2

---

Posted on **2017-06-10 21:41:50** by **kneelo**:

You need to have two bearings one for each chain or it won't improve the situation. The angle between the chain varies particulary at the edge of the sheet.

---

Posted on **2017-06-11 00:30:32** by **davidlang**:

well, it is possible to only have one bearing.



the idea is that you are going to keep the chain pointing directly at the router at all times, so you need to have (at least) two parts to the sled, one for each chain. These two parts need to be able to rotate freely (this means that you can't have things like your dust collection preventing one from rotating)



one person described these as two banjo shaped parts, with the chains attached to the necks.



the angle of the chain can vary from ~10 degrees off of vertical (bottom corner nearest the motor)  to ~80 degrees off of vertical (top corner opposite the motor)

---

Posted on **2017-06-11 03:03:38** by **kneelo**:

With one bearing you will need to balance the two sled halves to make sure the COG for both coincide with the router spindle at all angles.  Also the router spindle torque will influence the half the router is attached to and I can't think of a way you can compensate for it.  This isn't an issue with the chains on separate bearings.

---

Posted on **2017-06-11 06:32:00** by **rollandelliott**:

[Screen Shot 06-11-17 at 06](/images/Zh/UW/ZhUW_screenshot061117at06.19am.png.jpg) 

these are $35 on ebay and support 500 lbs.  Once could cut 400mm inside circle out of wood and an outside doughnut that is 450mm ID and 500mm OD and expoxy them to the aluminum bearing. Alternative aluminum brackets can be welded to the lazy susan. really not that hard or expensive. I think Maslow buyers would gladly pay for such a premade part and it would give a better machine.

---

Posted on **2017-06-11 09:30:55** by **scottsm**:

I like those bearings, they sound like the right thing, but I couldn’t find the radial load rating. Are there more specs, drawings?

---

Posted on **2017-06-11 13:40:34** by **davidlang**:

that's 500 pounds if you lay them flat and pile weight on top of them, not if you pull sideways on them. some lazy susan bearings will fall apart, some will not be supported by the balls in them, but will just rub disk to disk. tests are needed before it's declared that they aolve all the problems (especially when we don't know how much of a problem remains to be solved)



you don't need to fancy cutting/welding, just make a two layer sled, attach the router and the bearing to the bottom one, and have the top one with a hole large enough to clear the router.

---

Posted on **2017-06-11 15:02:15** by **scottsm**:

The description says ‘500 pounds radial load’. That’s perpendicular to the axis, yes? Axial load would be weight piled on top, no?

---

Posted on **2017-06-11 15:19:21** by **davidlang**:

I don't see anything in the screenshot that says 500 pounds radial load, just 500 pounds load, and that almost always refers to axial load

---

Posted on **2017-06-11 22:22:13** by **scottsm**:

VBX sells thru Amazon, there’s more info there. The description specifically features the 500 pound radial load rating. You’re right about needing only one, this could work. Have to keep dust out of the races, though.

---

Posted on **2017-06-12 02:49:00** by **davidlang**:

this is something you may also want to look into http://hackaday.com/2017/06/12/big-slew-bearings-can-be-3d-printed/

---

Posted on **2017-06-12 07:55:11** by **scottsm**:

That’s a timely post, the slew bearing is very interesting. Wish I had a _very_ large format 3D printer :)

---

Posted on **2017-06-12 17:51:24** by **davidlang**:

look at the hangprinter



I'll point out that the large format printer is only needed for the disks, and they could be created with more traditional means (say a router on a pivot point)

---

Posted on **2017-06-12 21:30:49** by **scottsm**:

What material would you use for the disks? Could one get away with making the outside disk as two rings, or would the race need to be routed into the inner edge of a single ring?

---

Posted on **2017-06-12 22:10:07** by **davidlang**:

one piece would be stronger, but two pieces should work.

---

Posted on **2017-06-12 22:39:51** by **scottsm**:

It would need to be stiff to keep from spreading due to radial force. What material?

---

Posted on **2017-06-12 22:53:48** by **davidlang**:

a good hardwood would probably work in this case, you could get a usable prototype (good enough to see if it works) out of good quality plywood.



a good plastic or aluminum would last long term.

---

