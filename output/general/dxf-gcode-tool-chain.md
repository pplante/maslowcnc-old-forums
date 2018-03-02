## DXF --> Gcode tool chain
Posted on **2017-07-03 21:02:00** by **Bar**:

How is everyone generating their G-code?



I've started using OnShape which can't export a .svg file like Sketchup can, so I've been doing OnShape --> .DXF file -> convert to .svg using https://cloudconvert.com/dxf-to-svg --> Generate gcode in www.makerCAM.com



It's a lot of steps, and the .DXF -> .SVG conversion changes the scaling of everything so I've got to scale it back which is a hassle.



Ideally we add CAM to Ground Control for importing both .SVG and .DXF files, but until we can do that I'd like to come up with a better system. 



What is everyone else using now?

---

Posted on **2017-07-03 22:09:14** by **scottsm**:

I'm using Easel, both to draw and to import .SVG

---

Posted on **2017-07-03 22:13:30** by **scottsm**:

Have you looked at any of the .STL-to-.SVG converters online?

---

Posted on **2017-07-03 22:24:13** by **mrfugu**:

Fusion360> Gcode. No MaslowCNC, so purely theoretical at this point, but so far it looks like its what it should be. (unsure about things like how detailed circles need to be vs how the code looks, etc, and aware Fusion360 *could* over complicate everything as it's attempting to be 'metal machining' accurate. Will relay results as soon as I have a MaslowCNC built.

---

Posted on **2017-07-04 02:34:15** by **akphoffman**:

DXF to SVG with Inkscape then makercam.com for gcode

---

Posted on **2017-07-04 05:04:25** by **gero**:

Design in FreeCAD, generates gcode

---

Posted on **2017-07-04 05:24:55** by **rancher**:

I'm using Fusion360.  .svg and .dxf are a bit of a complicated process, but it works well for me.

---

Posted on **2017-07-04 09:17:32** by **mfpiechowski**:

I usually draw in Sketchup, then I export to a DXF with a free plugin. I generate my GCode in EstlCAM.

---

Posted on **2017-07-04 11:28:41** by **Bar**:

It's funny that it seems like we've pretty much each got our own system. Probably a sign that there isn't really a clear 'best' way to do it.



@akphoffman's recommendation of inkscape seems to be doing the conversion from DXF to SVG for me pretty well, but I had to change the import setting in MakerCAM to 96 px/inch to get things to import at the right size by clicking *Edit -> Edit Preferences -> SVG Import Resolution* which took me a while to find 



Thanks for the suggestions everyone!



Is everyone's gcode from all of these different sources opening and running ok in Ground Control?

---

Posted on **2017-07-04 12:51:45** by **akphoffman**:

Yes the dip preference needs to be adjusted before importing.  I think the actual scale i saw online for Inkscape was 90px/inch.  is 96 better?

---

Posted on **2017-07-04 14:32:59** by **gero**:

@Bar If you want to implement opening a dxf in GC and start cutting :-) take a look at bCNC for inspiration. Although grbl I can't get it to run :-(

https://github.com/vlachoudis/bCNC

---

Posted on **2017-07-04 14:41:18** by **mfpiechowski**:

No Maslow here (yet), but the GCode I generate with EstlCAM (standard GRBL) runs fine on my OpenBuilds C-Beam. I use bCNC as my machine controller and GCode streamer, I run the CNC on a Raspberry Pi3. 



@gero:   What sort of problems are you having with bCNC?

---

Posted on **2017-07-04 14:47:25** by **gero**:

@mfpiechowski Can't answer that because it was a few weeks ago. I had only one day test and did not take notes. Most of the time was spent getting a linux disto that would run bCNC. By the time I had the software running I just established a connection with the Arduino, but nothing moved. A quick look at the settings did not help me and since then I did not try again.

---

Posted on **2017-07-04 14:51:37** by **mfpiechowski**:

Ahhh, OK. 



I have things working the way I want them to now, but it took me a bit of effort to get there. I run it on the Protoneer Raspberry Pi image that works with my setup. It wasn't exactly plug and play, but it was a lot easier than installing it from scratch. I also have run bCNC on a Windows desktop, but never used that as a machine controller.

---

Posted on **2017-07-04 14:55:23** by **gero**:

bCNC is worth some more investigation from my opinion. Will sure put more time into it. Good to see you :-)

---

Posted on **2017-07-04 16:24:37** by **cyberbipe**:

Hello i am eagerly waiting for my kit. I missed thr whole kickstarter so I am in thr internet group. I think you should check out a Sketchup plugin called Sketchucam. I used it on a smaller cnc machine but i am planning on at least trying it when i get my machine up and running. Sketchucam generates gcode right in sketchup.

www.sketchucam.com

---

Posted on **2017-07-04 16:31:39** by **cyberbipe**:

oops gave you an old web address. Need to go to 

www.phlatfourm.com

poke around there to get the latest version of sketchucam. Its free and open source.

---

Posted on **2017-07-14 17:23:25** by **umindedstrikesagain**:

Check out LaserWeb. I wrote the DXF import code and they have added routing capabilities to the CAM package.

---

