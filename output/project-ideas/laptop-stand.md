## Laptop stand
Posted on **2017-04-11 07:42:34** by **mindeye**:

Just sharing a quick project from last night. Designed and cut in about an hour! It needs a few tweaks but pretty good for a prototype.

 [IMG_20170410_210822261](//muut.com/u/maslowcnc/s3/:maslowcnc:mKD2:img_20170410_210822261.jpg.jpg)  [IMG_20170410_210851054](//muut.com/u/maslowcnc/s3/:maslowcnc:8CXL:img_20170410_210851054.jpg.jpg)  [IMG_20170410_210948273](//muut.com/u/maslowcnc/s3/:maslowcnc:OQxf:img_20170410_210948273.jpg.jpg)

---

Posted on **2017-04-11 07:57:14** by **scottsm**:

That looks good! What size bit did you Use? How deep at each pass?

---

Posted on **2017-04-11 08:08:03** by **Bar**:

That looks fantastic! Great concept. Thank you for sharing. What a great way to start my day!

---

Posted on **2017-04-11 08:17:38** by **mindeye**:

1/2" spiral upcut bit, only 0.1" each pass but I think I'll bump it up to 0.15 for v2. Feedrate of 20 ipm. Lots of annoying bits of woodfuzz but a quick sanding pass removed most of those. I'm toying with the idea of dropping down to a 1/4" bit to get more detailed cutout portions but my current one doesn't have the necessary depth.

---

Posted on **2017-04-11 09:07:00** by **scottsm**:

I've wondered about creating two gcode files, one where I declare the bit size a shade larger than truth, say 5/16", and the other true 1/4". If I use a 1/4" bit for both, would I avoid the woodfuzz? Haven't tried yet, but it's 'on the list'.

---

Posted on **2017-04-11 09:10:38** by **mindeye**:

I actually tried that and found good success with it but then I had one particular cut go really crazy and cut right through the middle of my part for some reason and stopped using it. I expect it was unrelated and I probably fat-fingered a setting in makercam but it put me off that approach for a bit. You've also got to make sure you create tabs on both passes in the same place if you're using tabs to hold your work.

---

Posted on **2017-04-11 10:15:11** by **scottsm**:

Interesting about the wandering cut. GroundControl has always done a good job showing gcode paths for me. I've forgotten to raise the z-axis at the end of a cut and cut a groove going home, before the version that raises the z-axis at the start of the home command. I've had the z-axis go crazy when the connector came loose, but so far the xy motors haven't acted up for me - gotta go knock on some wood!

Your project's got me rarin' to go, I'll have to go get some more plywood :)

---

Posted on **2017-04-11 16:39:17** by **Bar**:

@mindseye Would it be OK if I were to show a picture of your laptop stand in the update tomorrow? (and give you credit of course)

---

Posted on **2017-04-11 17:56:16** by **mindeye**:

Totally! I posted it in part as a way to encourage the community to start building stuff. That lines up perfectly.

---

Posted on **2017-04-11 18:22:02** by **rollandelliott**:

very cool to see people already making stuff. I'd add a top brace and bottom cross brace to make it really stable.

---

Posted on **2017-04-11 20:17:02** by **mindeye**:

I was shooting to make it collapsible for flat pack transport. To that end I added some 1/4" dowels and holes for them. I'd probably use 3/8" in a final design but it's good enough for now. In truth the length of the whole design needs another 2" anyhow. Currently, the laptop when fully opened puts the center of gravity behind the end of the stand which makes the laptop likely to skip over the front stops when shaken. [IMG_20170411_195859574](//muut.com/u/maslowcnc/s3/:maslowcnc:Fhkl:img_20170411_195859574.jpg.jpg)

---

Posted on **2017-04-11 20:40:28** by **Bar**:

That's the beauty of CNC, you can revisit the design to more the CG or change the size of the front stops if you want, and once you've got it dialed in, if you are willing to share the files nobody ever has to solve that problem again :)

---

Posted on **2017-04-12 07:19:45** by **nathanmiller**:

This post makes me so happy. I have a million project ideas in my head so it's encouraging to see ideas springing from the minds of users into real life!!

---

Posted on **2017-05-22 05:20:57** by **chrisbourke**:

Hi Nathan,

---

Posted on **2017-05-22 06:08:04** by **nathanmiller**:

hi there. :)

---

Posted on **2017-05-22 21:01:23** by **chrisbourke**:

Ha! Sorry i must have posted my last comment well before i had finished it. Nathan, Mindeye and Bar i thought i would post up my laptop stand which I published on opendesk a couple years ago. They have removed that section from their website now unfortunately, but it did garner a quite a lot of votes in that time. The design makes use of the ability that laptops have to open their screens up to an obtuse angle. It would be awesome to see some others try it out and get some feedback! Uses 12mm ply stock. Follow this link to view images and download files. https://goo.gl/0HUnC9

---

Posted on **2017-05-22 21:58:54** by **chrisbourke**:

Sorry last link was directly to a .dxf file. See this link for images too. 

https://goo.gl/2FQnkW

---

