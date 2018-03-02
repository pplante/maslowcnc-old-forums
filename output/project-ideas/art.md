## Art
Posted on **2017-01-31 19:28:31** by **larry357**:

Just remebered the following half tone picture, would be awesome full size! http://jasondorie.com/page_cnc.html

---

Posted on **2017-02-01 05:55:14** by **TheRiflesSpiral**:

Whaaaa? That's so cool! It looks to me like the output is a bitmap file? How does a CNC follow a raster file? (Just curious... newb here)

---

Posted on **2017-02-01 09:54:14** by **TheRiflesSpiral**:

Sorry, more specifically, how does Maslow follow a raster file?

---

Posted on **2017-02-01 11:00:22** by **scottsm**:

I think Maslow follows a gcode file - one has to translate the raster image into gcode with other tools, like the one from the link above.

---

Posted on **2017-05-26 03:58:24** by **larry357**:

To add to the list http://wiki.evilmadscientist.com/TSP_art paint a sheet of ply a colour and start cutting 😎

---

Posted on **2017-05-26 04:31:16** by **davidlang**:

Scottsm is correct, maslow doesn't interpret raster files. There are a number of software packages that can take a raster file and convert it into g-code.



However, it's worth pointing out that the maslow is not well suited for cutting such projects. Projects that are starting from raster files tend to want to cut away the entire surface (to different depths), since the maslow sled rides on the surface of the material being cut, if you cut away the entire surface you can run into problems. You would have to make sure that enough surface is left intact for the sled to ride on (and no, I have no idea how much surface that would have to be, someone would need to experiment.

---

Posted on **2017-05-26 07:27:14** by **scottsm**:

Depending on scale, of course, an image like that one is well within the realm. I'd lay a sheet of paper over the painted surface to keep the sled from marring the paint. Not much adhesive, though, it could take _forever_ to pick the remaining paper off after the cut :p.

---

Posted on **2017-05-27 03:06:23** by **larry357**:

[Tsp2](//muut.com/u/maslowcnc/s2/:maslowcnc:Lmf8:tsp2.svg.jpg) just a test file of the program, seems to load well and creates a tool path in makercam, was trying to extrude it in fu360 but it through a hissy fit :P

---

