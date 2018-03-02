## Make Magazine G-Code Article
Posted on **2016-11-30 08:22:21** by **TheRiflesSpiral**:

Vol. 54 (December 2016/Jan 2017 issue) has an article about G-Code on pages 50 and 51. It's a neat primer on what G-Code is and how you could even write it by hand if you wanted to.

I had no idea it was so simple, honestly! It reminds me of my early days learning PostScript at the school newspaper.

---

Posted on **2016-11-30 17:08:01** by **davidlang**:

yep, g-code is incredibly primitive. It was designed decades ago when the available computers to put into equipment were far more primitive than even the arduinos we are using. In the earliest days, the machine operator had to type the g-code into the machine manually for the job they were doing.

Now, there are variations and extensions to g-code to add neat features (circles, various drilling routines, ramp cuts, etc). But you can do a lot with the very  basic g-code manually.

I find that for a lot of jobs, it's easier to write the g-code manually and run a test cut than to fight with a drafting program, CAM converter, etc.

For other jobs, I'll start with the generated g-code, but may tweak it manually.

---

Posted on **2016-11-30 17:14:04** by **chadzimmerman**:

Do not bringith forth the name of Satan!  (PostScript) .. I still have nightmares.. Or laTEX for that matter...

That aside, some nice information here: (http://www.cnccookbook.com/CCCNCGCodeBasics.htm)

---

Posted on **2016-11-30 20:13:45** by **davidlang**:

I've done network diagrams by pulling up a text editor and typing in the postscript :-)

but g-code is really primitive, you can get by with about a half dozen statements.

---

Posted on **2016-12-01 04:05:59** by **TheRiflesSpiral**:

Thanks for that link, Chad! Sadly, I still have to deal occasionally with PostScript's angry cousin, SVG. Our variable data workflow at work is primarily native PPML which uses SVG elements for almost everything. Text transformations are especially frustrating... but I digress.

---

Posted on **2016-12-01 08:07:39** by **mooselake**:

If you really want nightmares, go read up on RS-274X (the g code "spec"), then find out that there's lots of somewhat compatible implementations and extensions.  Then there's the ones that don't understand arcs (3D printer slicers...) and do round things with many small straight lines.  Wonder what subset Bar is using?

You can get by with a half dozen commands, but you'll go buggy trying to do anything complicated by hand.

For a walk on the wild side, check out the documentation and forums on linuxcnc.com 

At least we don't need to punch holes in paper (the mylar sandwich tape lasts a lot longer) tape any more.

---

Posted on **2016-12-01 11:08:06** by **Bar**:

Oh man, let's not talk about everyone having their own standard of gcode. Big pain in my booty. I'm supporting all of them that I have found so far. If you can find a flavor of gcode that doesn't play nice, send it my way and I'll make it work. It's usually something simple like G01 can be written "g1" "g01" "g 01" "g-01" "G1" "G01"...etc so we've just got to pick up on all of those. 

Speaking of getting by with a half dozen commands and doing round things with many small straight lines, I came across a gcode generator once that ONLY used the G01 command (straight line) and nothing else.  Yuck! :-)

---

Posted on **2016-12-01 13:52:33** by **TheRiflesSpiral**:

Early Yamaha robots were that way. I had the displeasure of programming one to lay a glue line around the perimeter of a part that would eventually receive a sealing ring. I had to hand-code it in half-degree increments. What a nightmare.

---

Posted on **2016-12-02 16:39:40** by **Bar**:

Oh man that sounds like a hassle and a half. Did you have to do all the math for the kinematics by hand?

---

Posted on **2016-12-02 20:25:50** by **TheRiflesSpiral**:

I made a Lotus 123 spreadsheet (good lord I'm dating myself here) that did the calculations for me... It was basically a program that set the position of the three stepper motors (!) that drove the end effector. 

I wasn't nearly smart enough to do that on my own (still not!) and as I recall the documentation gave pretty good direction about how to pull it off.

It only lasted about a year and the engineer who followed behind me realized the part was light and symmetrical enough to put on a rotating stage... he eliminated the robot altogether and just spun the part under a nozzle at the right radius. Very elegant solution I wish I had come up with!

---

