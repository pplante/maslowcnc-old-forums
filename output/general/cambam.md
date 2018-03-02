## CamBam
Posted on **2017-07-08 05:59:52** by **brandonmc**:

I know CamBam isn't open source but I really like the work flow of dxf to g-code. My first question is there a open source program with dxf to g-code? My second question profile settings for CamBam. I copied the default Makercam settings is that a good idea?

---

Posted on **2017-07-08 09:34:51** by **rollandelliott**:

looks cool, but I guess its' not worth $150?

---

Posted on **2017-07-08 09:43:30** by **gero**:

Hi brandonmc, the magic pill for dxf to g-code is what I am searching for ages. I have determined myself to FreeCAD now as it is open source and cross platform. It is under development, so bugs are expected. The learning curve seems heavy at the start, but eases after a few tutorials form YouBooze. Regarding dxf import, in FreeCAD you might have to join a lot of lines to create your solid in order to get the g-code. I need to put in this work because my current project was designed in Blender and the export to dxf creates hundreds of lines and vertexes. My next design I will do in FreeCAD and skip all that extra work.
You might want to look at https://sourceforge.net/projects/dxf2gcode/ and Python scripts are also available that attempt it all in one step.
My guess is that the outcome highly depends on the source of the dxf file.

---

Posted on **2017-07-08 10:52:38** by **Bar**:

I played around with CamBam a little and I liked it too, but I've been trying to restrict myself to free software so I can recommend free options to everyone. As for the default settings, I've been doing most of my cuts at 30ipm, with a .15 in step down 

My current dxf -> gcode system is to open the dxf in inkscape, then save it as a .svg file for MakerCAM. When importing the file in makercam change the "pixels to inches" value to 96 in the settings to get everything scaled right

---

Posted on **2017-07-08 14:31:09** by **mfpiechowski**:

I use EstlCam to convert DXF to Gcode. There's a free demo option, the full purchase price is $60. As far as free/open-source options, it is my understanding that bCNC can generate GCode from a DXF, but I haven't tried using it for that yet. I figured out EstlCam and haven't worried about learning anything else.

---

Posted on **2017-07-08 16:11:43** by **brandonmc**:

Thanks everybody for your input. I'm going to try bCNC it looks promising. Llibrecad can convert dxf to svg it has a built-in makercam svg export. I have been drawing with Qcad, then using Librecad to export svg, then Makercam for g-code. The lonely problem I've found so far is Librecad does not work with some fonts. That being said I like CamBam but I don't like the price.

---

Posted on **2017-07-08 17:45:21** by **Bar**:

Librecad looks very interesting. I didn't know about that one so thanks for the tip. I'm going to give it a try now.

Did you have any issues with the .svg files and scaling when using Librecad with makerCAM?

---

Posted on **2017-07-08 17:50:09** by **brandonmc**:

The svg export is made for makercam. Seems to work well. The only thing about Librecad is it doesn't support ttf fonts.

---

