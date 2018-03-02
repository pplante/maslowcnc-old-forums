## Questions regarding Gcode
Posted on **2017-04-30 09:37:57** by **seventhram**:

I'm designing my first piece and I have several questions.

I design everything in AutoCAD, I'm going to try to DXFOUT and dxf2gcode (I'll let you know how this works)

1) MM or Inches or does it matter?

2) I'm using 1/2" thk plywood with a 1/8" bit. 

  a) two passes 1/4" deep each pass?

  b) do I manually copy/paste gcode for the second pass and adjust Z depth?

3) speed?

---

Posted on **2017-04-30 10:19:34** by **Bar**:

Great questions:



Both MM and Inches are supported. 



I recommend using a 1/4 inch bit because you can go deeper with each pass. The general rule of thumb for CNC routing is that you can go 1/2 the width of your bit with each pass. So technically with a 1/8th inch bit you should do 1/16th passes. That being said, you can push that a little depending on what the bit you are using looks like, what the wood is like, and how much you care about the finish on the final part.



Your CAM program should have a setting for how deep to cut with each pass. While it might not be exactly the same for those programs you listed, the walk through [here](https://github.com/MaslowCNC/GroundControl/wiki/Generating-G-Code-Using-www.MakerCAM.com) might be worth a read through.



Right now the speed of the machine is limited to 25ipm in software so any speed at or below that will work. It what is going to give you the best results really depends on what makes the bit happy.



Good luck! Let us know how it goes.

---

