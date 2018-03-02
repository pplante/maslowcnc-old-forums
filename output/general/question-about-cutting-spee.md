## Question about cutting speed.
Posted on *2017-03-06 05:44:57* by *carlosrivers*

What will ultimately allow me to cut faster?

There is a file for a bed frame (http://atfab.co/?portfolio=silver-lining-bed) that requires 6 sheets to be cut, and I'd like to speed up the process as much as I can, but without sacrificing quality cuts.

Thank you for helping a newbie!

---

Posted on *2017-03-06 09:57:04* by *TheRiflesSpiral*

Larger cutters (larger diameter) afford faster chip removal and higher speeds at the cutting surface which usually means higher feed speeds.

A more powerful router will maintain rotational speed at higher feed rates, which usually means higher feed speeds.

Neither of these things take motion control into consideration, which is firmly in the realm of Bar and his development of the firmware.

---

Posted on *2017-03-06 10:01:55* by *spatialguy*

Hi Carlos, have a read of this. I hope it answers some questions for you. http://makezine.com/2014/09/10/endmills/

---

Posted on *2017-03-06 10:57:17* by *scottsm*

It looks like the design is sensitive to the tool diameter - I imagine the tool path info they send to beta users would mention this.

---

Posted on *2017-03-06 12:22:41* by *Bar*

The current limitation on the speed is how well the firmware's feedback control system can track a position, but I expect that to not be a limitation for much longer. After that we're limited by how fast the motors can turn.

@TheRiflesSpiral is right that the bigger the cutter you are using, the faster you can cut and the deeper you can cut with each pass.

@scottsm is right that some designs are sensitive to the size of the cutter. A smaller cutter will be slower, but lets you cut finer details. 

No matter what you do, cutting up 6 full sheets will take a good amount of time. Keep in mind that CNC cutting time is different from your time. It's important to stay near the machine while it's running for safety, but you are free to work on other things like sanding, staining or assembling the parts which have already been cut.

---

Posted on *2017-03-06 14:17:52* by *davidlang*

The R2200 router has lots of power to be able to handle a large bit at a fast cutting speed.

you can also do a 2-pass approach (especially if you have a powered Z and leave tabs to hold things in place)

do one pass (or set of passes, depending on how close to full depth you can go) quickly with a large bit, ideally cutting everything 1/16 oversized.

Then do a second pass with a very sharp, small bit. This will get any details the first pass misses and the edge will be much cleaner if you do a full-depth cut that only has to trim a little bit off of the work.

---

Posted on *2017-03-06 16:52:46* by *tmaker*

I thought I remember reading somewhere that the max speed was 48 inches per minute.  Is that specific limitation a motor max limitation?  Or is that a firmware limitation that will eventually get raised?  After there are no speed related firmware issues, what can we expect the max motor speed to be?

---

Posted on *2017-03-06 18:09:18* by *davidlang*

That's the firmware limitation that Bar was referring to above.

---

Posted on *2017-03-06 18:10:27* by *Bar*

That maximum feedrate is limited to 48ipm by the motors, BUT because of the way the machine is laid out it's actually able to move much faster in some directions. For example, moving left to right is much slower than moving up or down so we could add an "as fast as possible" option which would cut more quickly in some directions than others. You could probably go more than 100ipm in the up/down direction towards the top, but I'd need to look into that more.

---

Posted on *2017-03-07 15:13:42* by *jamesbil*

A quick late-night-not-thoughtout-thought.. could you build in a one click "reverse" button/setting that would back track the router along its path, maybe at a slower feed rate to clean up a cut?

---

Posted on *2017-03-07 15:16:08* by *Bar*

That's a great idea! It might be a little tricky to implement because gcode is only designed to be read in one direction, but I'm sure we can figure it out!

---

Posted on *2017-03-07 15:17:52* by *jamesbil*

Would also help clearing chips from a narrow groove/cut

---

Posted on *2017-03-07 15:28:12* by *davidlang*

doing an additional cleanup pass is common.

reversing gcode is going to be non-trival, there is potentially a lot of state that you would have to remember in order to undo things (not just the prior speeds, but also where the zero is off the top of my head)

it's not just a matter of looking at the locations and moving in the opposite order.

---

Posted on *2017-03-07 17:43:57* by *rollandelliott*

It's more than just bit size. spiral upcut bits will evacuate chips faster than a straight edge. Multiple flutes will evacuate even faster, but if you dont' move the bit fast enough it will cause burning.

---

Posted on *2017-03-07 17:44:30* by *rollandelliott*

My experience has been opposite what most people are saying above. The smaller the bit the faster you can cut. because the bit is smaller there is less force against it, and can thus travel faster. For example trying to force a 1/2" bit through 1/2" plywood requires a good amount of force. Switch to a 1/4" and you can go faster.

---

Posted on *2017-03-07 17:47:41* by *rollandelliott*

but only up to a certain point anything smaller than 1/8 tends to break. 1/4 or 3/16 diameter seems to be the sweet spot to me.

---

Posted on *2017-03-07 20:06:28* by *spatialguy*

Im pretty sure the more flutes, the better the cut but the slower the slower the chip evacuation. As for smaller diameter bits, I get what you are saying about small = speed but there's like a break even point when using different types and thicknesses of material. A small bit will just break if pushed quickly where a larger bit will chew through it comfortably, also a large bit in easily to cut material will take a deeper (horizontal) cut per revolution than a small bit even though it has to remove more material per revolution. 

It seems to me that what you are saying has some merit if the discussion was about twist drills only used for drilling holes; but with cutting bits, while what you are saying might SEEM intuitive, you are way off base and you (all of us) should be cautious with opinions or assumptions presented as hard fact. 

There are plenty of people here who have no experience and this is their first adventure in this area. I'm actually the same, I've had plenty of machinest experience but read and listen keenly to anything said about the control software a nd how it interfaces with the Maslow router because I an totally new at it. If someone led me down the wrong track by stating opinions/guesses as fact, it would make things very confusing and unnecessarily make my learning curve a lot longer.

---

Posted on *2017-03-08 06:52:01* by *rollandelliott*

I've been using routers for years, and my comments are definitely not guesses!  Basically the answer is dependent n material. Aluminum sheet metal works best with Single flute upcut bit that is about 2x the thickenss of material trying to cut.  so 3/16" about for 1/16" material. Using multiple flutes on aluminum will just cl;og it up. And least not forget about different alloys. 3000 serioes is softer than 6061. 

soft wood vs hardwoods? in general wood works better with multiple flutes and 1/4" or bigger bit depends on depth of cut. 

How about plastics. There are hundreds of them. HDPE or poluycarbonate which is soft can be cut faster than  you can push the router. 
all of this based on experience, not opinion.
basically do your homework on what material you plan to cut.

---

Posted on *2017-03-08 10:27:32* by *spatialguy*

Hmmm, OK.

---

Posted on *2017-03-09 18:56:28* by *dayglow238*

a solid carbide upcut bit will cut the fastest.  1/4" is thick enough to handle the heat build up (as mentioned before). That is the bit I use  most commonly on my horizontal mortising machine. Those always come double fluted.  Just be aware that plywood dulls bits faster than solid wood (the adhesives are harder to cut through). Carbide bits will last a long time and can be resharpened for a reasonable price. That bed design does look cool, but using 6 sheets of plywood it will be weighty!

---

Posted on *2017-03-10 03:28:20* by *rollandelliott*

https://m.aliexpress.com/search.htm?keywords=6mm+upcut+bit#/

---

