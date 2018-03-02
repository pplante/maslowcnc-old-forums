## Idea for accuracy improvements/calibration
Posted on **2017-05-23 16:53:27** by **pyrosrock**:

I don't have my Maslow yet so I could be totally wrong with my theory.
Can someone tell me, the inaccuracy with the outsides of the cutting area, are they consistent or random? I saw the post of someone doing some testing cutting the squares and drilling a hole in the centre after each square showing that the drift was not over time but due to the area.

I have done a bit of work with GIS software packages overlaying areal imagery on maps. Small images are easier with minimal distortion, but as you get to larger images or images with undulating terrain a distortion map is required. To do this known points are marked on the imagery and matched on the map. The more points matched the better the distortion overlay.
My thoughts being could we do this in groundcontrol by cutting a series of points and then measuring the actual location of where they are cut. from this a distortion map can be created as part of the calibration process.
Of course this only works if the distortion around the edges are replicable and the same every time not just random.

---

Posted on **2017-05-23 17:03:15** by **davidlang**:

we are still working out all the software issues, right now the accuracy is about 1/16" across the 4'x8' work area, the design goal is 1/64".

the hardware is able to adjust the chain lenths to about 0.002", or about 7x the accuracy needed for 1/64", but right now the software isn't able to position things that accurately.

there was a major change in the software last week that should significantly improve things (replacing one position PID loop with a position PID loop and a speed PID loop), but until we get the PID loops tuned properly, we won't know how good we are.

Personally, I suspect that there are probably multiple things missed in the hairy math needed to calculate the chain lengths, but it is very nasty math and takes a lot of skull sweat to understand. I know we don't take chain droop into account, but that doesn't seem like it accounts for the errors we are seeing.

All the efforts of people cutting different test shapes was finding the scope of the problem and short-term workarounds that seem to work fairly well near the center of the sheet, but not so wel l near the edges (since they involve lying to the software about what the machine dimensions are, that's not surprising) 

take a look at https://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter/10858#10858?newreg=13734dd331424a0ea0d2ddc79c562910 and the file Kinematics.cpp, we should be trying to account for everything predicatively rather than through a distortion map

---

Posted on **2017-05-23 17:10:47** by **Bar**:

@pyrosrock you are thinking exactly the same thing I am.

The distortion is very consistent so a 'straight' line cut from one end of the plywood to the other will have a slight curve to it, but the curve will always be the same. Because the distortion is very repeatable we can correct for it.

I'd like to try to come up with a clever calibration technique to get everything exactly dialed in, but if we have to we can use a distortion map. I have reservations about any plan which relies too heavily on measuring things by hand because that would mean the machine's accuracy would be limited to what we can measure accurately. It's easy to say that measuring accurately is easy, but in my experience it's difficult.

Right now I'm working on a python implementation of the kinematics math so that we can easily plot what the effects of errors in different terms have. Cutting test shapes is fun, but if we can see it on the screen as we change things we can iterate faster. 

 I won't have it done by tomorrow's release, but hopefully I'll have something to show before next week's update.

---

Posted on **2017-05-23 17:29:20** by **pyrosrock**:

A line... why didn't I think of that!
You can cut a line then put a known straight edge against it and measure the deviation and length. This is easier for most people. but I suspect that if you got a few measurements and corection values from people then you would see a trend which you could code in as default values

---

Posted on **2017-05-23 21:55:04** by **davidlang**:

keep in mind that we are talking an error of 1/16" (hopefully less) over about 8', that's not easy to measure. It takes a _long_ straightedge to see that, or a stringline, or optical approach.

---

Posted on **2017-05-23 23:05:01** by **pyrosrock**:

hmm, having no clue about what 1/16" is in real terms. I have a number of known straight edges but it is true that most people will not.
that said detecting anything less than 1mm over 2 or more meters can be challenging without the correct equipment.

---

Posted on **2017-05-23 23:26:03** by **davidlang**:

1/16" is approximately 1.6mm

---

Posted on **2017-05-23 23:26:51** by **davidlang**:

so we are aiming for a final accuracy of ~1.4 that, or about 0.4mm

---

Posted on **2017-05-23 23:28:34** by **lostpath**:

To find the curve, shoot a laser from one end of the line to the other, and then measure the deviation at the center. Add more points along the way if you want a better model of the curve~~~~~~~ however it is still going to be hard to measure.

---

Posted on **2017-05-23 23:38:23** by **davidlang**:

I really don't like the idea of trying to map a distortion on to the field, since we don't know what's causing it, we have no reason to believe that it's going to be consistent from one set of machine dimensions to the next. And having everyone try to measure their machines to this level of precision seems _hard_

---

Posted on **2017-05-23 23:39:48** by **davidlang**:

@lostpath, exactly, and most people aren't going to have a laser available, let alone precision measuring equipment to figure out how far off they are.

---

Posted on **2017-05-24 00:13:50** by **dkchris**:

It might or might not be the ideal solution for the actual software, who knows at this point? But gathering the information (And yes, preferrably on as high a number of different rigs as possible/reasonable for better statistical data quality. But it probably doesn't have to be everybody who recieved a kit.) could probably be just the tool needed to figure out both the root cause and the solution for the inaccuracy! I'd figure if you make a reference Gcode file with well thought out central reference markings and an even raster pattern across the entire work surface, have the testers set up a large sheet of paper in stead of plywood and replace the router bit with some sort of fine point pen, you could have them mail in their results folded and rolled up in a cardboard tube and keep the actual measuring work inhouse that way. And even if they don't have their  setting dialled in completely alike, you'll still get data for the RELATIVE variations. There just has got to be some knowledge hidden in those numbers.

---

Posted on **2017-05-26 13:16:06** by **jamesmiles**:

Feels like a mechanical engineering problem. As one chain is played out long and the other is short the vectors shift. Variables, the weight of the chain, the slack in the chain, and the twist of the sled.  Feels like the motors would need to turn slightly less when the chain was played out to keep the tension.  The differences could be expressed as a set of concentric circles each with a slightly different gear ratio between the paired motors.

---

Posted on **2017-05-26 14:05:11** by **TheRiflesSpiral**:

> @jamesmiles
> Feels like the motors would need to turn slightly less when the chain was played out to keep the tension

This would result in an incorrect position. The sag will be present irrespective of the motion of the motor; this is determined by the weight, angle, length of and tension on the chain. That sag takes up length so that length must be added back to the distance.

Software is the place to take care of this.

Alternatively one of the other variables could be affected; lighter chain could be used but this only reduces (not eliminates) the sag. The angle/length are noise variables... they must change in order for the machine to function. Or the tension can be increased. There is an argument to be made about this, though... theoretically no reasonable amount of tension would eliminate all the sag.

---

Posted on **2017-05-26 15:40:49** by **davidlang**:

we do take all these things into account (or try to), the math is at
https://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter/10858#10858?newreg=13734dd331424a0ea0d2ddc79c562910

the code is the function inverse() https://github.com/MaslowCNC/Firmware/blob/master/cnc_ctrl_v1/Kinematics.cpp

we re-run the calculation at a rate of about 6KHz, at 48 ips this amounts to about every 1.5mm.

At this point the chain sag is a small error compared to what we currently have. We currently have a calculation error (either a bug in the math or problems in measuring the machine) that is causing a position error as we move around the sheet.

---

Posted on **2017-05-26 15:48:15** by **Bar**:

If I remember right we're doing the calculation more often than every 1.5mm even at 48 ipm (note that's ipm not ips. 48 ips would be very fast)

---

Posted on **2017-05-26 16:47:55** by **davidlang**:

you are right, it's ~0.2mm, I must have slipped a decimal place when I calculated the distance with the prior setting. That's actually reasonable

---

Posted on **2017-05-26 16:52:31** by **Bar**:

I'm glad the revision is in the good direction :)

---

Posted on **2017-06-08 19:59:32** by **gordonthiesfeld**:

I hope no one minds me reviving this thread, but I found this article and I thought it might be useful.  [New low cost sensing head and taut wire method for automated straightness measurement of machine tool axes](http://www.sciencedirect.com/science/article/pii/S0143816613000766?via%3Dihub#f0015).  

It sort of combines the stringline and the optical approach that davidlang had mentioned for determining straightness.  I'm not an engineer, so this may be an old idea, but it's new to me. :)

I was thinking you could have the electronics mounted to a sled, with the filament wire strung across the frame using guitar tuning pegs to tension them.

---

Posted on **2017-06-08 20:26:25** by **gordonthiesfeld**:

Also, maybe instead of the optical sensors, you could use a usb microscope similar to [this setup](http://beatty-robotics.com/zeroing-a-cnc/).  you could attach a ruler on the sled so that it could be seen behind the microscope.  You would line the microscope crosshairs up with the taut filament, then move the sled from one end to the other.

---

Posted on **2017-06-08 20:44:31** by **gordonthiesfeld**:

> @gordonthiesfeld
> you could attach a ruler on the sled so that it could be seen behind the microscope
Let me try that again: You could attach a ruler to the sled with the wire in front of it so that both are visible to the microscope.

---

Posted on **2017-06-09 01:35:09** by **davidlang**:

The problem with trying to use this approach is that the sled rotates depending on where on the workspace it is, so getting the sensor aligned with the wire is non-trivial

---

Posted on **2017-06-09 05:54:21** by **gordonthiesfeld**:

Oh, I see.  Possibly a test pattern of concentric circles instead of a ruler?  Though I suppose that could be difficult to create accurately at the appropriate scale.

---

Posted on **2017-07-13 21:16:04** by **cameronswartzell**:

A relatively easy (though potentially somewhat wasteful) way to measure map accuracy across an entire sheet might be to cut your own peg board, then compare your result (in say 1/8" underlay, which is at least cheap) with factory pegboard. All you'd need to do is create a file with the same hole spacing,  and just have the router do simple holes rather than measuring deviations on a long line cut. 

Overlaying factory pegboard you could see how the grid stretches or bows in various directions

---

Posted on **2017-07-14 01:37:01** by **cameronswartzell**:

.

---

Posted on **2017-07-14 02:44:33** by **davidlang**:

remember, we are aiming for an accuracy of ~0.4mm here, that's hard to measure no matter what you do, especially over an 8' span

---

Posted on **2017-07-14 09:08:43** by **Bar**:

@davidlang hit the nail on the head for the issue I've been having. Basically I've hit the limit of what I can measure reliably. I'm hoping that the simulation I've been working on will help us better understand what measurements to take to and what to do with the results (for example maybe instead of doing a full sheet of peg board we can do just the five or six most important points)

---

Posted on **2017-07-14 10:18:04** by **TomTheWhittler**:

You could take a digital caliper and add this somewhat expensive attachment
https://www.mscdirect.com/product/details/48464150 
I suppose you could "roll your own" with some aluminum flat stock.

---

Posted on **2017-07-14 10:48:02** by **Bar**:

I've never seen one of those before, but it's a great idea. Cool suggestion, I'm going to be keeping that in mind

---

Posted on **2017-07-14 10:48:14** by **cameronswartzell**:

After discovering I can jam a pencil in a 1/4" collet I am actually going to try my pegboard grid idea. No cutting necessary, so I can perform repeated tests 'quickly'. I'm assuming hole spacing and diameter on pegboard is uniform with enough accuracy to use it as a measuring metric. If the Machine puts a dot on every space, or maybe just every other it should be easy to lay a sheet of real pegboard on top and eyeball the results. The holes are 3/16" in diameter, so 3/32" in radius. Just eyeballing "this one is about 25% low of center, and it trends that way over the next 4 feet" gives you a simultaneous whole sheet measuring tool with I think decent accuracy (dependent on calibration of your eyeballs)

I've got pegboard around, so this is pretty convenient. Colored pencils can allow quick adjustment

---

Posted on **2017-07-14 14:51:51** by **rollandelliott**:

Pegboard is made out of Masonite ght which swells with moisture I wouldn't use it as a reference

---

Posted on **2017-07-17 01:43:29** by **cameronswartzell**:

Man, if I can get my machine to mark across a full sheet so accurately that I have to consider the horizontal expansion of moist Masonite I'll jump for joy! Point taken, but the expansion should be less than 1/64th laterally. It's still a pretty cumbersome idea, there's certainly got to be easier tests.

---

Posted on **2017-07-17 02:46:20** by **davidlang**:

I would love to see the results of tests. I think we are at the point where an accurately measured machine should be down to an error of around 1mm anywhere on the sheet, but we do not have many test reports to go by, and per the simulation, any measurement error on the machine translates pretty directly into errors in the cuts (sometimes the error in the cut can be larger than the error in the machine measurement).

The least accurate measurement is the position of the chains, since there isn't a clean pivot point for them (they don't really pivot much at the bracket, but instead pivot mostly, but not entirely at the chain link outside the bracket) and this also throws off the measurement of the distance between the chain mounts and the center of the bit.

---

