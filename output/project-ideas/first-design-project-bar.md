## first design project - bar stool
Posted on **2017-02-18 07:21:33** by **nathanmiller**:

I decided I need to try designing my own CNC project. I'm generally capable in Sketchup but mostly for construction projects and framing. Detailed work like furniture requires more accuracy than I'm used to...

Regardless I dove into creating a bar stool. After about 10 attempts, I came up with this design. It's for 3/4" plywood and all measurements are in inches. If I did things right a lot of pieces should be nest-able and pretty efficient on a 4x8 sheet. There are still some issues with the design (for example, where the 4 piece rings go around the legs I need to notch the ring sections so that they don't overlap the legs, and I should add some screw pilot holes), and I have no idea if it's strong enough to actually sit on! Haa haa. 

At any rate, here's the concept: 



https://drive.google.com/file/d/0B-ZcXNFKzjU9WV9lclRGLUhfZGc/view?usp=sharing



If anyone wants to mess with the design you're welcome to it. It was more of an exercise in creating with Sketchup and thinking through problems. 



 [Stool_06_-_SketchUp_Make_2017](/images/yy/yyay_stool_06__sketchup_make_2017.png.jpg)

---

Posted on **2017-02-20 06:44:36** by **TheRiflesSpiral**:

Remember that for curves rendered in Sketchup, the number of segments in the arc/circle/etc will impact how smoothly the part comes out on the CNC... your seat has 28 segments which means it will be cut with 28 straight lines.



It's good to get into the habit of setting the number of segments to an appropriate number immediately after drawing a curve. (Arc/circle/etc)

---

Posted on **2017-02-20 10:38:44** by **hannahteagle**:

Love this! Bar and I have been trying to decide what to do with our dining room space at home (using it as just a dining room is waaay too boring ;) ) and recently chatted about building a bar. The stool is great inspiration!

---

Posted on **2017-02-28 12:55:02** by **nathanmiller**:

@TheRiflesSpiral I had no idea that's how Sketchup would output an arc. Thanks for the heads up! Do you have a recommended number of segments per 360 degree turn? Is there a good rule of thumb?

---

Posted on **2017-02-28 15:11:47** by **davidlang**:

it depends on the size of the circle, and how smooth you need it to be. There's no good rule of thumb, you'll have to try some values and see how you like the results. Sometimes you deliberately want a low value

---

Posted on **2017-02-28 16:39:04** by **TheRiflesSpiral**:

@nathanmiller like david said, it depends on the size of the part. I try not to let line segments get longer than 1/8". So for an 8" diameter circle (25" circumference) I would set something like 200 segments.

---

Posted on **2017-03-01 07:03:42** by **nathanmiller**:

Good points. Thanks. I like the rule of thumb 1/8" line segments. Do you know if it's possible to have the router produce an arc or does it always translate into small line segments?

---

Posted on **2017-03-01 07:41:25** by **TheRiflesSpiral**:

Ground Control always moves in a straight line from point A to B. The distance between A and B is dictated by the GCode sent to the controller.



Now, some applications can create bezier curves (which aren't line segments) but I'm not sure I understand completely how those are translated into GCode... I think they're turned into bunch of line segments.



For instance, If I make a bezier curve in Inkscape, import the curve into makercam and make a tool path then export GCode, I see lots of lines of code in the .nc file that are small moves from one place to the next. If GCode supported true bezier curves, I would expect one line of code with the formula describing the geometry of that line (more like PostScript)



Even drawing a simple circle in makercam and exporting gcode of the toolpath makes a file with 970ish lines to make that circle... again if GCode supported true vector commands I would expect to see one line of code that describes the circle, not how to go a round it.



I think Sketchup just skips the whole bezier curve thing and just makes line segments instead. Not sure why, but that's how it handles them.

---

Posted on **2017-03-01 07:50:05** by **nathanmiller**:

That's exactly what I was wondering. Thanks! 

Based on what you're saying it would seem one should expect to explicitly express line segments for any curve. Finding a way to express it as a vector calculation will likely not translate into gCode so one shouldn't bother.

---

Posted on **2017-03-01 07:58:27** by **TheRiflesSpiral**:

In Sketchup you don't have a choice. The drawback to using that architecture is that it's not easy to edit the curve. You're forced to either scale or re-draw a lot. So in Illustrator/Corel Draw/InkScape/Other Vector Illustration Tool you can simply grab a node on a curve and change it's shape. Like this:  [Bezier](/images/rz/rzyo_bezier.jpg.jpg) 



I don't have any idea how you would do that in Sketchup without re-drawing it.

---

