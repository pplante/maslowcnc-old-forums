## SketchUp is friend, not foe
Posted on **2017-02-22 10:13:10** by **hannahteagle**:

So I'm incredibly new to CAD software. The first time I ever touched any CAD software was Inkscape a few months ago, and let me tell you I hated it. I've since moved on to SketchUp and for the most part really enjoy using it, but once in a while I get too hasty and think I can outsmart the CAD software. I'm pretty much always wrong.



Long story short, I designed this really cool milk crate style box with a bunch of finger joints and I drew it like 3 times on pieces of paper and I really thought it was going to fit together after I cut it out... and it didn't. So, word of advice for all of you who don't have the patience with computers or suck at visualizing things in 3d... SketchUp is your friend in this! Use it to your advantage to be certain your cuts are going to fit together BEFORE you cut them out... That was you won't go wasting trees like I did :/



*photos to come*

---

Posted on **2017-02-22 17:56:59** by **aggies979**:

Sooo...here's a dumb question. I'm new to all of this but I downloaded Sketchup and tried to install the addon like you did (Hannah) in your video a couple of weeks ago but it seems as though the plugin won't work in the newest version of sketchup. Does anyone have any suggestions? Or could someone maybe upload a video starting something from design (sketchup or fusion 360)  and how exactly to get it to ground control to start the cut? 



Hannah's video would have been great but again I can't seem to get the plugin that saves the file as an svg to work. Thanks in advance for putting up with my question!

---

Posted on **2017-02-23 05:14:46** by **TheRiflesSpiral**:

There's a branch on GitHub of that plugin that's been updated to work with versions of Sketchup after 2010.

You'll have to disable the existing one, close Sketchup and then go into the directory to delete the .rb file. (C:\Users\YOUR USERNAME\AppData\Roaming\SketchUp\SketchUp 2017\SketchUp\Plugins)

Restart Sketchup then load the .rbz file from this repository:

JoakimSoderberg/…/sketchup-svg-outline-plugin

I just tested it on my machine and it's working.

You'll know you got it right when you see the toolbar at the top with JUST the “SVG” button, and not the “SVG” and mosquito buttons.

---

