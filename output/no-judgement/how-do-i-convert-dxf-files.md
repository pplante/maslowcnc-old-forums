## How do I convert DXF files to G-Code?
Posted on **2017-03-20 18:09:26** by **carlosrivers**:

I have Sketchup downloaded, but Im not seeing any SVG export options.

Thank you

---

Posted on **2017-03-20 20:59:52** by **Bar**:

Great question! It's a little bit tricky, but Hannah has you covered with this video: https://www.youtube.com/watch?v=W0mW_mm1iBI 

The key part is that you need to grab and svg export plugin for which there are links in the description of the video :-)

---

Posted on **2017-03-20 21:14:52** by **Bar**:

*the svg export plugin

---

Posted on **2017-03-21 12:14:37** by **TheRiflesSpiral**:

There's a branch on GitHub of that plugin that's been updated to work with versions of Sketchup after 2010.
If you've already installed the other one, you'll have to disable the existing one, close Sketchup and then go into the directory to delete the .rb file. (C:\Users\YOUR USERNAME\AppData\Roaming\SketchUp\SketchUp 2017\SketchUp\Plugins)
Restart Sketchup then load the .rbz file from this repository:
JoakimSoderberg/…/sketchup-svg-outline-plugin
I just tested it on my machine and it's working.
You'll know you got it right when you see the toolbar at the top with JUST the “SVG” button, and not the “SVG” and mosquito buttons.

---

