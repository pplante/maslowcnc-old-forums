## 1/2 inch bits
Posted on **2017-02-24 12:06:15** by **Bar**:

Someone asked about using bigger bits so I bummed some 1/2 inch tooling from the custom fab shop next door  [1-2 Inch Mills](//muut.com/u/maslowcnc/s1/:maslowcnc:Yxsj:12inchmills.jpg.jpg). From left to right are the 1/4 inch up-cut bit I used in the update, a 1/2 inch straight bit, and a 1/2 inch compression bit. 



They said they almost never run the 1/2 inch compression bits because you have to cut at least 1/2 inch plywood in a single pass before the bit fully engages which is more depth than they like to do. 



I ran the same test as in the update in MDF with the 1/2 inch straight bit and the cut quality looks even a little better than it did with the 1/4 inch bit.  [1-2 Inch MDF](//muut.com/u/maslowcnc/s1/:maslowcnc:cyRc:12inchmdf.jpg.jpg) 



The dimensions are a little wonkey because I didn't regenerate the gcode for the larger bit, but that lets you see how thin you can go. The MDF was starting to fall apart so I think any parts smaller than that are going to turn to dust.

---

Posted on **2017-02-25 14:56:08** by **cfrey**:

Any comments on which type of bit works better? Straight, Up-Cut, Down-Cut, Compression? I have only used a straight bit before but hear spiral is better for plunge cuts.

---

Posted on **2017-02-25 17:29:56** by **davidlang**:

they have tradeoffs.



a spiral cutter will make cleaner cuts (more shaving, less chopping)



spiral down will push the chips down into the cut where they will cause more grief, and will cause tearout on the backside if you are cutting all the way through.



spiral up will cause more tearout on the upper surface. but will clear the cut a bit better.



compression cut tries to be spiral up on the bottom and down on the top to get clean edges on both sides, but you have to be cutting through everything to get it working well.



it depends a lot on the material,

---

Posted on **2017-02-27 10:45:46** by **Bar**:

The width of the bit seems to matter more than I expected. 1/4" inch bits seem to leave cleaner cuts than 1/8th" and 1/2" seems to be better than 1/4". I started out with very small bits because I was worried about having enough power to use larger bits, but that doesn't seem to be as much of an issue as I thought.

---

Posted on **2017-02-27 13:14:14** by **jbarchuk**:

For the same RPM, double the diameter = double the IPS of the cutting edge = cleaner cut.

---

Posted on **2017-02-27 13:30:09** by **Bar**:

Great point!

---

Posted on **2017-02-27 13:34:17** by **davidlang**:

the router has more than enough power to spin the large bits, the part I'd be concerned about is if the resulting torque causes positioning errors.



@jbarchuk, the larger bits also have more of their volume available for the chips to go into (even relative to their size), so they are able to cut more aggressively before they start choking on their own chips.



a good video on this topic (focused on badsaw blades, but the concept is the same) is https://www.youtube.com/watch?v=fK9m5PadmiI&t=10s

---

