## SKP files in CAD repository
Posted on *2017-02-04 11:47:14* by *jbnimble*

TL;DR; I want to convert the [CAD Sketchup](https://github.com/MaslowCNC/CAD) files to something I can view/edit in Linux.

I am running Linux, and so Sketchup is not a friendly application (Windows & IOS only). I tried running it through Wine, but Wine did not play nice on 64bit in Ubuntu, and [Sketchup Make](http://www.sketchup.com/download/all) does not appear to come in a 32bit version. 

I tried to find a program to convert the SKP files to some other Linux friendly format, but that has brought no success. As far as my reading brought me you need Sketchup Pro to convert file formats. Maybe someone with Sketchup Pro can convert the SKP files to a more common format and add them to the Git repository?

The feeling I get from my reading is that Sketchup is not open source friendly. Would it be possible to make any SKP files in the future also available in some other more common file format that can be modified using open source software?

---

Posted on *2017-02-04 13:49:44* by *scottsm*

Do you have an idea what format you want/need? There is a free plugin for Sketchup that will make these formats:

STL  triangles. Use this for Makerbot or Reprap style 3D printers
DXF polyface mesh. This will give the most faithful reproduction of your original Sketchup model.
DXF polylines: exports the outlines of each face as a polyline, sometimes useful for CAM toolpaths.
DXF triangular mesh: breaks all the faces up into triangles
DXF lines. This option exports the edges in your model as lines.

If you like, send me a private message and I'll send you one or two to try. Zipped, they range between 86K and 166K.

---

Posted on *2017-02-04 14:06:00* by *scottsm*

Looking in Sketchup itself, it is willing to do COLLADA .dae format or Google Earth .kmz format  - would one of those work? Looks like GLCplayer would handle the .dae and .stl formats.

There is an online viewer for .stl files here:
http://www.viewstl.com

---

Posted on *2017-02-05 05:28:38* by *gero*

I finally got Sketchup to run with wine on Ubuntu MATE 16.04. The trick was to use the 2016 installer. The export to .dae seemed to work, howerver, importing in Blender, i was missing the back legs. Back to Sketchup I "exploded" the legs and exported again. This time the arms were missing. Importing both models and deleting double parts got me a model. The scale was accurate. But if I touch a property like material, the model scales up randomly. Will try my luck with Drafsight and LibreCAD tonight.

---

Posted on *2017-02-05 10:02:02* by *jbnimble*

@scottsm, no, I don't know what format would be a good fit, I was hoping someone could tell me the best open source format. I mostly wanted to be able to view the files to get a better idea of what I will eventually need to make before the cnc arrives.

@gero, wow that sounds like a lot of gyrations, I'm glad you were able to get it working.

---

Posted on *2017-02-05 10:23:44* by *Bar*

I haven't really found a good open format yet. .STP files are pretty good because they give you surfaces which can be used to generate tool paths from. If you are just looking for a way to see the model .STL files are the most widely supported because they are used for 3D printing. Adding 2D .SVG files would give you a blueprint like view of each part. 

I like the idea of having multiple file formats available to download. I'm a little worried about keeping all the files up to date. It's easy to tweak something in the CAD drawing and forget generate all of the other file types.

---

Posted on *2017-02-05 18:09:51* by *jbnimble*

I defer to the experts on formats, but svg or stl files I can handle. Agreed that having a process to update the agreed source into other formats is a great idea. Thanks all for being so responsive and flexible to support multiple platforms.

---

Posted on *2017-02-05 18:13:31* by *scottsm*

@gero, is that a 32-bit version you've got set up there? If so, then @jbnimble's issue might be solved and he could use your solution to work with the .skp files, yes?
@Bar, I agree that adding multiple formats adds to the burden of document management, best to minimize that.

---

Posted on *2017-02-06 06:49:29* by *TheRiflesSpiral*

With Sketchup being free, I would think the skp format is probably the most portable. Maybe a recommended list of plugins to export to other formats would be helpful, but managing a repository of multiple file formats sound like a nightmare.

---

Posted on *2017-02-06 07:20:56* by *jbnimble*

@gero, can you point me to some instructions on how you got sketchup working in linux? I had problems as stated above with the instructions I found previously.

@theriflespiral, the app may be free today, but there is no other app that can read, write, or convert the skp format. 

I'll do some research, maybe I can find a compromise that is not too onerous.

---

Posted on *2017-02-06 12:04:41* by *jbnimble*

This article describes the fear I have of not using an open source format for files
http://hackaday.com/2017/02/06/will-your-cad-software-company-own-your-files-too/#more-242772

---

Posted on *2017-02-07 05:28:36* by *paulhart*

I agree with @jbnimble that "free" isn't always "free"... I haven't used Sketchup very much at all, so can't comment on its qualities (specifically, what is it about sketchup that makes life easy when translating a 3d model into 2d?), but I know that other, freer applications can emit useful file formats.

On the nerdy end of the spectrum, something like OpenSCAD would probably be a good thing to support. On the other end, Inkscape provides a user-friendly way to create SVG files, and there are exporters that can take those files and generate gcode. An example of this is available here (per the URL, this was designed generate gcode to drive a laser cutter, but the concepts are the same):

http://wiki.thinkhaus.org/index.php?title=THLaser_Plugin

---

Posted on *2017-02-08 15:51:36* by *growbot*

I use onshape.com and love it.

---

