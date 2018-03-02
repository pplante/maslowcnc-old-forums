## Having a hard time getting my Cam to cut as designed.
Posted on **2017-06-20 14:34:41** by **carlosrivers**:

So I am working on my sign project and I cant seem to get the cam to work out in Fusion 360.



Here's some pictures. [Screen Shot 2017-06-20 at 2](//muut.com/u/maslowcnc/s3/:maslowcnc:3vhg:screenshot20170620at2.37.25pm.png.jpg)  [Screen Shot 2017-06-20 at 2](//muut.com/u/maslowcnc/s3/:maslowcnc:PbU1:screenshot20170620at2.37.18pm.png.jpg)

---

Posted on **2017-06-20 15:27:41** by **rancher**:

It's hard to tell what's going on there so it's tough to help you Carlos.  On my machine the green line is the tool travel above the work, cuts should show as blue lines.  I'm inclined to suspect your depth settings in the 2d contour settings, but I have no idea what you are up to there so I could be way off.

---

Posted on **2017-06-20 16:01:00** by **carlosrivers**:

Basically I am trying to clear the entire selected letter. The problem I am having, is that there is still material inside the letter. How do I pick a letter and clear the material so there that it is a true engraving?



I saw the engraving option in 2D cuts, but I dont have that bit and I dont like how it is at an angle. 2D engraving doesnt allow me to use a flat head bit.

---

Posted on **2017-06-20 16:04:47** by **rancher**:

Try a pocket operation.  You will need a bit smaller than the line width.

---

Posted on **2017-06-20 16:05:28** by **carlosrivers**:

[Screen Shot 2017-06-20 at 4](//muut.com/u/maslowcnc/s3/:maslowcnc:b4Ni:screenshot20170620at4.06.38pm.png.jpg) 



In this picture I get very close by messing with the "Stock to leave" option in the Passes section. I have it set to -.07



Perhaps I am trying to do one size fits all for my different sizes of letters. Is it not possible to have a setting where I click a letter and have that entire area clear at my -.75 depth?

---

Posted on **2017-06-20 16:16:54** by **carlosrivers**:

Okay, I think Im closer, I need to use 2D pocket.

---

Posted on **2017-06-20 18:27:38** by **carlosrivers**:

https://drive.google.com/open?id=0By4wTqIjhYwnTW1GNDl6R1R5VTg



Any idea why this has some hiccups? When I put it into Camotics theres some obvious issues.

---

Posted on **2017-06-20 19:02:03** by **rancher**:

I can't see it Carlos, can you post a screenshot?

---

Posted on **2017-06-20 19:17:47** by **carlosrivers**:

[Screen Shot 2017-06-20 at 7](//muut.com/u/maslowcnc/s1/:maslowcnc:4vXA:screenshot20170620at7.21.12pm.png.jpg)  [Screen Shot 2017-06-20 at 7](//muut.com/u/maslowcnc/s3/:maslowcnc:ihmf:screenshot20170620at7.21.01pm.png.jpg)

---

Posted on **2017-06-20 19:22:01** by **rancher**:

I think it looks like you are doing pretty well.  It's hard to tell, but it looks like the weird edges are a function of the rough font you used and the way the bit does or doesn't fit in the valleys.  I'm just guessing.  You might have to try running it and see how it translates to wood.

---

Posted on **2017-06-20 20:10:07** by **carlosrivers**:

Rancher really want to thank you for your feedback. 



Heres a photo of it in GC



In Gc it does look pretty good... [Screen Shot 2017-06-20 at 8](//muut.com/u/maslowcnc/s3/:maslowcnc:FCwt:screenshot20170620at8.12.36pm.png.jpg)

---

Posted on **2017-06-20 20:22:26** by **carlosrivers**:

[Screen Shot 2017-06-20 at 8](//muut.com/u/maslowcnc/s3/:maslowcnc:ZplI:screenshot20170620at8.23.07pm.png.jpg) 



That last nc file had too many lines of code.



I made my depth cuts to .15 I think that should be fine, with a 1/8th inch flat bit.....right lol?

---

Posted on **2017-06-20 21:44:02** by **davidlang**:

generally, when cutting out letters you end up with nicer results using a v-bit or a bullnose (rouded bottom) bit instead of a flat bit.



A flat-bottom bit or a bullnose work well when you cut the letter to the same depth everywhere, a v-bit can do nice things with variable depth (making very nice sharp points coming off of the edges of the letters)

---

Posted on **2017-06-21 05:27:13** by **rancher**:

That looks great Carlos.  I'm glad I could help.

---

