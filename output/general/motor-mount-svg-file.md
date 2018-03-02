## Motor Mount SVG file
Posted on *2017-03-15 12:52:37* by *mattnelson*

I opened the motor mount svg file and it does not see correct at all.  Is it just me?

---

Posted on *2017-03-15 12:59:44* by *scottsm*

I agree, it's not what it should be...

---

Posted on *2017-03-15 13:24:03* by *scottsm*

I've created an issue for this on MaslowCNC/Mechanics:
[Motor_Mount.svg file seems wrong. #7](https://github.com/MaslowCNC/Mechanics/issues/7)

---

Posted on *2017-03-15 14:27:57* by *scottsm*

@mattnelson, I put a .zip file into one of the comments for that issue (link above). Would you see if that looks correct on your end?

---

Posted on *2017-03-15 14:49:49* by *mattnelson*

That zip file looks good in Adobe Illustrator.  Thank you.

---

Posted on *2017-03-15 16:15:57* by *Bar*

Good catch! I'll fix that right now.

---

Posted on *2017-03-15 16:17:21* by *mattnelson*

Thank you!  What about the SVG files for the frame/base?  I don't see those on github.

---

Posted on *2017-03-15 16:26:12* by *Bar*

I added the missing files and regenerated the motor mount in PR #8 here, https://github.com/MaslowCNC/Mechanics/pull/8

Do those look right?

---

Posted on *2017-03-15 16:55:25* by *scottsm*

MakerCam is happy with them all. InkScape sees the stroke as 90px wide, so renders them with hugely fat lines :( 
Should there be one for the sled, as well?

---

Posted on *2017-03-15 17:12:57* by *Bar*

:-) 

There should indeed be one for the sled.

---

Posted on *2017-03-15 17:42:09* by *davidlang*

when doing CAD in inkscape (or any other drawing program), you need to keep the line widths as narrow as possible (well below 1pt), otherwise you can end up with all sorts of 'interesting' artifacts because the software gets confused over what part of the line you are referring to (I've even see it try to cut both sides of the line)

---

Posted on *2017-03-15 18:14:57* by *TheRiflesSpiral*

I just learned that lesson on our laser cutter, if I set the line width to anything more than 0.001", it defaults to raster mode and refuses to follow the line, instead going back and forth a bajillion times like an inkjet printer.

---

Posted on *2017-03-15 18:21:04* by *Bar*

I agree. For some reason the .svg exporter in sketchup seems to crash if I try to make it output a line thinner than .1 inch. I think I may have to tweak the files in inkscape

---

Posted on *2017-03-15 20:08:15* by *mattnelson*

I think the only svg file that is still missing now is the brick holders on the sled.

---

