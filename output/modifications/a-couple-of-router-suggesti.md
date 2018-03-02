## A couple of router suggestions
Posted on **2016-11-09 04:54:25** by **asleborgen**:

1: How about adding an output from the Arduino to switch the router power on and off via an SSR? 
2: For a really simple and cheap Z-axis solution, could one perhaps use an RC servo to lift the router in and out of the material? Maybe the servo pushes a couple of skids towards the plate to be cut, thus purshing the sled (and bit) out. This would of course limit you to one cutting depth "pr. job", but you woldn`t have to manually adjust in and out all the time. 

Yes yes, I hear you, the Z-axis is coming along, but it will not fit every router, and the servo solution "might" be cheaper...

-Just food for thought...

By the way, congrats on finally ending the election campaigns, now the fun begins!

---

Posted on **2016-11-09 07:35:27** by **TheRiflesSpiral**:

I love the idea of an auxiliary output... I was thinking along the lines of a dust collector but a stout enough relay would handle a router. Arduino is super simple to code... I bet it would take very little to implement!

---

Posted on **2016-11-09 20:48:13** by **Bar**:

I am planning to leave two aux outputs on the controller to make that kind of modification easy. Each aux output will have a 3 pin .1 inch header with +5volts, a gpio pin and GND, which happens to be the same as the standard servo connector (not a coincidence) :-)

I probably won't add code to turn the router on and off automatically to the main branch for safety reasons, but I will make it as easy to modify.

I can't wait to see all the cool modifications the community makes!

---

Posted on **2016-11-10 06:48:04** by **mooselake**:

The router still has it's own power switch, which will take priority over an external SSR.  A router, like all cutting tools, is dangerous in the wrong hands ("gee, wonder what happens if I set this running router down in my lap bit first", like they say you can't idiot proof everything because they keep inventing  better idiots), and the user would need to purchase and install their own SSR and associated wiring.  If you're worried about the safety of user mods, include stickers that say "turn router switch off when not in use", and a comment in the 10 page lawyer written "this'll hurt you if you do stupid things" notice.  Along with unplug this sucker when you're changing bits.

That's a long way of saying you should include the code to turn it on in  either the released, or an alternate pre-compiled firmware.  Auto power control was one of the first things I added to my G540/LinuxCNC powered Zenbot Mini.  You can build a case that it's safer, no need to handle  the router, or leave it running when the cutting's done.  Also a good idea to automatically retract the bit for Z axis users in the end g code.

---

