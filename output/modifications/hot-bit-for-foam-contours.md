## hot bit for foam contours
Posted on **2017-06-01 09:46:32** by **jimfred**:

I'm contemplating trying a soldering iron instead of a router bit to shape polystyrene foam. I'm thinking that it would generate less dust and would result in a cleaner surface. Hot-wire foam cutters typically leave a nice smooth surface. If the soldering iron tip is at the same temperature, it might be possible to get smooth contoured surface. Has anybody tried anything like this?

---

Posted on **2017-06-01 10:05:50** by **scottsm**:

The sled drags across the surface of the material being cut. Would that matter to the process?

---

Posted on **2017-06-01 10:07:34** by **mooselake**:

Polystyrene foam, both extruded and beadboard, cuts very well with a router, and way faster than the Maslow will move.



If you go the hot knife route a soldering iron might make a big mess.  Something like https://www.harborfreight.com/130-watt-heavy-duty-hot-knife-60313.html (yes, Horror Fright, there's other sources...) could be a better choice.



Phlatboyz.com used to sell a cnc hot wire cutter; the principles went on to start Openbuilds but still have a forum at http://phlatforum.com/xenforo/ .  In the past it was a great source for CNC foam model cutting, don't know how the reincarnated forum is but it's worth a look.



This forum doesn't  support BBCode.  Is there a way to insert links?

---

Posted on **2017-06-01 10:25:33** by **davidlang**:

The maslow is a bad design for controuring the surface, if you cut away too much of the surface, the sled will fall down into the cut area, and now your depth is wrong and you end up cutting deeper than you want (and the sled may end up getting stuck as it tries to get out of the cut area)



As for cutting foam.



hot knives work well as they only melt a small amount of the foam, trying to melt away all the foam between the desired depth and the surface would be a huge mess (where will the liquid plastic go to before it cools and solidifies again for example)



In theory you could mount a hot wire loop to the sled and adjust it's height to cut the appropriate depth, but then you will run into the other problem with the maslow design, the sled twists as it moves from side to side across the workpiece, so your hot wire loop will not always be facing the same direction.



You really want a Cartesian gantry CNC machine for doing that sort of cutting with a hot wire.

---

Posted on **2017-06-01 10:27:08** by **davidlang**:

@mooselake, to insert a link, just paste in the URL and the forum takes care of things (as you did in your post)

---

Posted on **2017-06-01 10:28:13** by **davidlang**:

also, you can click on the question mark in the text entry box and it will pop up a small window showing you the markup that's available. It does include putting in a link.

---

Posted on **2017-06-01 10:57:50** by **rollandelliott**:

Stinky gooiey  mess just use router and flame edgea after if wanted

---

Posted on **2017-06-01 11:11:51** by **mooselake**:

I assumed he meant cutting at right angles to the surface, just like it was cutting plywood.  I agree, anything else doesn't make a lot of sense.



A couple years ago I made forms out of 2" styrofoam for foaming underground outdoor boiler pipes.  Besides extra insulation it kept the expensive closed cell foam in a fixed size area rather than filling the whole width of the trench.  Think 12" high sides with half high notched spacers to hold the pipe in the center.  It would have been handy to have a foam cutting Maslow rather than using table and circular saws.

---

Posted on **2017-06-01 18:39:10** by **gotzero**:

I had thought about using Maslow to cut XPS foam but never some of the thinner more pliable stuff. If it works I will be redoing/improving every shadowed tool drawer of mine which will make Maslow worth the money for that task alone, I would happily never use my hot wire cutter again.

---

Posted on **2017-06-02 07:09:07** by **dkchris**:

A big issue with both hotwire and hot knife/hot "pen" work on both EPS and XPS is the necessity for constant, even speed movement to obtain a fairly constant kerf size(going very slow and reducing heat can to some degree compensate for this........but then you're going VERY slow). Another is that mutiple-pass cuts wont work with a typical hot knife/pen/soldering iron type tool unless your surface has rather destinct "slip" angles, as the next deeper pass will have the knife/pen/sold.iron stem increasing the kerf of the already performed "cut". Also, the stem of such a tool is usually hotter than the tip, making the effect even worse.

If you could figure out how to make a tool with a small hot tip and a cold stem, this might solve some of the issues.

---

Posted on **2017-06-02 07:14:59** by **dkchris**:

Oh, and I'd definitely suggest a cartesian gantry, something like the hangprinter 3D printer setup or another true 3D setup with some depth range.

---

Posted on **2017-06-02 07:31:07** by **dkchris**:

David is right though; the melted styrene will end up as an uneven thickness hard surface on your foam. The thicker this layer gets in a certain area, the less kerf you will see in the area, with possible risk of collision. I'd suggest to try and make a cutting tool and experiment freehand on some large leftover/scrap foam chunks.

Idea for the tool: a Vaping wire coil at the end of a set of large gauge supply leads supported by something and with a suitable adjustable current source. Some of the many diy vaping pages can probably give a hint to what combination of wire and supply might work.

---

