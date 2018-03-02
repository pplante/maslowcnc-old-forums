## The weekly Wednesday update is up!
Posted on **2017-01-18 18:08:06** by **Bar**:

This week Hannah takes us all the way from a idea to an object. You can check it out here:



https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1787186

---

Posted on **2017-01-19 06:47:38** by **sjsandman**:

Great video, Having problems adding sketchup-svg-outline-plugin

to SketchUp Maker 2017. Has anyone been successful?

---

Posted on **2017-01-19 06:50:43** by **sjsandman**:

I have tried adding the .rb to :

SketchUp 2017: C:\Users\YOUR USERNAME\AppData\Roaming\SketchUp\SketchUp 2017\SketchUp\Plugins

---

Posted on **2017-01-19 06:52:10** by **sjsandman**:

Using : https://github.com/JoakimSoderberg/sketchup-svg-outline-plugin/issues

---

Posted on **2017-01-19 10:46:38** by **TheRiflesSpiral**:

Download the RBZ file. Go to Window > Extension Manager and click "Install Extension." Navigate to the .rbz file and click open.

---

Posted on **2017-01-19 12:24:30** by **sjsandman**:

Hi, thanks for the reply. I did try that and I can see the plugin, but it says it is unsigned. Not sure what that means. [Plugin](/images/hj/hjjk_plugin.jpg.jpg)

---

Posted on **2017-01-19 12:42:31** by **TheRiflesSpiral**:

It only means you didn't get it from their plugin explorer. After you add it, go back to the drawing space. You should see a new toolbar with the "SVG" text and another icon on it.

---

Posted on **2017-01-19 14:20:08** by **TheRiflesSpiral**:

For some reason on my install, the new toolbar wasn't at the top with the rest, it was hovering out in the drawing space. If you drag it up to the toolbar it will snap in with the rest.

---

Posted on **2017-01-19 14:20:50** by **TheRiflesSpiral**:

If that doesn't work, right-click on the toolbar and make sure the "FlightsOfIdeas" toolbar is checked.

---

Posted on **2017-01-19 14:57:35** by **sjsandman**:

Got it working, thanks for you help!

---

Posted on **2017-01-19 15:39:28** by **TheRiflesSpiral**:

Great news! I'm fairly new to Sketchup and I find the plugin ecosystem a bit odd. But I come from the AutoCad world which is so closed-off and black-box... Sketchup is really refreshing in a lot of ways.

---

Posted on **2017-01-25 12:49:20** by **hannahteagle**:

Hey everyone. I got the .rbz installed in the Extension Manager but when i select the piece I want to save and try to save as an .svg, nothing happens. In the video I was recording off of Bar's computer, but I have a mac and just downloaded the newest version of SketchUp. It's possible the extension just isn't compatible anymore? Any ideas?

---

Posted on **2017-01-25 13:03:01** by **TheRiflesSpiral**:

Hannah, I have a PC and Mac install of Sketchup so I can test both... what version are you using?

---

Posted on **2017-01-25 13:29:49** by **hannahteagle**:

I'm using SketchUp Make 17.1.173. Thanks for the help!

---

Posted on **2017-01-26 07:05:04** by **TheRiflesSpiral**:

On PC I'm at 17.1.174 64-bit.



This is really weird... when I save a file but then search for it, I get shortcuts in the Recent Items and Recent folders but no actual file.



I also don't get a file in Illustrator when I choose it as an editor.



Looks like maybe this plugin is broken in the new version. I'll try my Mac tonight.

---

Posted on **2017-01-26 07:06:28** by **TheRiflesSpiral**:

...and the Flights Of Ideas website redirects me to a web search for "Cheap Flights" on Yahoo. Bummer.



Well, off to look for a new export tool!

---

Posted on **2017-01-26 07:56:51** by **TheRiflesSpiral**:

Got it working... There's a branch on GitHub of that plugin that's been updated to work with versions of Sketchup after 2010.



You'll have to disable the existing one, close Sketchup and then go into the directory to delete the .rb file. (C:\Users\YOUR USERNAME\AppData\Roaming\SketchUp\SketchUp 2017\SketchUp\Plugins)



Restart Sketchup then load the .rbz file from this repository:

https://github.com/JoakimSoderberg/sketchup-svg-outline-plugin



I just tested it on my machine and it's working.



You'll know you got it right when you see the toolbar at the top with JUST the "SVG" button, and not the "SVG" and mosquito buttons.

---

Posted on **2017-01-26 09:09:41** by **TheRiflesSpiral**:

I'll test out the Mac tonight.

---

Posted on **2017-01-26 09:31:19** by **hannahteagle**:

Thanks so much! I'm about to give this a go.

---

Posted on **2017-01-26 09:41:40** by **hannahteagle**:

It works! Much appreciated.

---

