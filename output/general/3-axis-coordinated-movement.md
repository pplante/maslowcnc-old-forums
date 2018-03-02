## 3-axis Coordinated movement?
Posted on **2017-04-27 18:11:41** by **mindeye**:

Has anybody tested this yet? I vaguely remember only seeing this being coded up for X and Y axis at the same time and some of gcode I just generated using Fusion 360 is moving all 3 axis at the same time. Won't really have a chance to give it a whirl on the machine until tomorrow but if it's going to cause issues I'll hold off.

---

Posted on **2017-04-27 18:13:40** by **mindeye**:

Actually, looking at the next conversation down, it seems like this does work and I can recall going back to home moving all 3 axis too so I suppose it must. I'll just leave this here in case anybody else thinks to ask.

---

Posted on **2017-04-27 19:57:07** by **tomtribute**:

That would be really cool if that is possible.

---

Posted on **2017-04-27 23:12:55** by **Bar**:

The way it's coded right now the z-axisFix isn't fully coordinated with the XY movement because I was imagining more of a "cut a pass,move down, repeat" work flow, but there's no reason we can't cordinate all three, it's 100% possible. If it's something you'd like to see just file a bug for it describe how you want it to work and I'll make it so!

---

Posted on **2017-04-27 23:19:24** by **davidlang**:

yes, all three should be fully coordinated, if you give

g1x0y0z0

g1x1y1z1



the result should be a continuous slope in all three axis from the starting position to the ending position.



now, it's less important to factor the z movement in when computing the feed rate (bit it wouldn't hurt).



do you want it filed under the firmware or another repo?

---

Posted on **2017-04-28 05:18:34** by **TomTheWhittler**:

I second the vote for all three fully coordinated otherwise you will not be able to do relief work like lithophane or Relief Sculptures like (http://www.metmuseum.org/toah/works-of-art/2002.445/)

---

Posted on **2017-04-28 07:46:43** by **Bar**:

Perfect! I think putting it under firmware sounds like the thing to do. It shouldn't be too hard from a software side. 



I really designed the machine to cut sheet goods so that kind of 3D relief work is really pushing the limits, but there's no reason to restrict the software capabilities.

---

Posted on **2017-04-28 08:10:35** by **TomTheWhittler**:

Bar wrote : "I really designed the machine to cut sheet goods..."

I understand that and at first I will be using the MaslowCNC to that end. 

With a X/Y/Z and other output control I can see all sorts of other possibility. 

For example I can see a carriage that has either four nozzles or one nozzle with with a mixer. You have a MaslowCNC on a sliding carriage that you can press the frame against a wall then paint any  Mural picture on the wall.

The key here is to be able to expand the MaslowCNC with longer chains and you could in theory create giant works of art or carvings.

---

Posted on **2017-04-28 08:18:18** by **mindeye**:

So I don't think I even strictly need it at the moment, it just happens to be how Fusion 360 output the gcode - I highly suspect if it does all three axis movements but Z not coordinated the cut will come out just fine still. I'm currently just testing cutting a slope into one of the sides of the piece (well, rather very, very tiny terraces but it approximates a slope close enough for me - especially once sanded).



Probably still give it a try later today (while keeping a very close eye on it). Having the ability to cut slopes into the sides of pieces allowed me to move from 3 parts to just 1 which both works better and will look way better.



Thanks for the confirmation that this is indeed not totally there yet!

---

Posted on **2017-04-28 08:38:30** by **Bar**:

Very cool! Just let me know ow what you guys need and we'll make it happen.



For shaping the sides of parts I had some good luck playing around with roundover bits to give the parts a rounded edges or 45 degree v-bits to give the edge a 45 degree angle which might be worth playing with :)

---

Posted on **2017-04-28 08:39:23** by **mindeye**:

Hah, yeah, if only they made a 26 degree angle bit I'd be in business :)

---

Posted on **2017-04-28 08:46:38** by **mindeye**:

I've created the issue for the firmware over at github. Thanks!

---

Posted on **2017-04-28 17:35:59** by **MakerMark**:

I'll put my vote in for this feature as well. Looking back at my speed test of 100ipm, most of the wildly inaccurate cuts were preceded by 3d axis movement g-code commands. Thx!

---

Posted on **2017-04-28 18:35:11** by **mindeye**:

So here's the 26 degree angle slope test.

Works well enough to put it into a real design! [IMG_20170428_182838564](//muut.com/u/maslowcnc/s3/:maslowcnc:tiGV:img_20170428_182838564.jpg.jpg)

---

