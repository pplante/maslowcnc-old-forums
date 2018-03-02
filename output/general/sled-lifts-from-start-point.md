## Sled lifts from start point
Posted on *2017-06-09 11:36:27* by *blsteinhauer88*

[IMG_0016](//muut.com/u/maslowcnc/s3/:maslowcnc:ee5q:img_0016.jpg.jpg) [IMG_0017](//muut.com/u/maslowcnc/s3/:maslowcnc:RwT5:img_0017.jpg.jpg)

I made this for daughter wedding. I have been getting the drooping cuts at the bottom of patterns. Not just this one. The bit enters the wood after traversing to the location. Then lifts as it starts to move through the cut. Then ends , and relaxes into the initial hole. I have this in other patterns too.  Thought it was from my arms being loose, but now they are tight and still occurring. Unknown if in code, chain slack, or GC/firmware? Anyone have ideas?

---

Posted on *2017-06-09 11:41:23* by *blsteinhauer88*

[Image](//muut.com/u/maslowcnc/s3/:maslowcnc:WylW:image.jpg.jpg) 
Happens on front and back of straight lines.

---

Posted on *2017-06-09 11:41:57* by *gero*

Nice woodart. Strange Z behavior. I have a feeling that my Z moves create slight xy moves, but can not confirm that yet. Different from your detailed observation.

---

Posted on *2017-06-09 11:47:16* by *blsteinhauer88*

Just a bit of chatter also in some of the letters.

---

Posted on *2017-06-09 12:38:39* by *Bar*

I've seen this happen also. I will look into it and see what I can find out.

---

Posted on *2017-06-09 13:39:18* by *blsteinhauer88*

By the way, if I hit stop, then home, it is not picking up the bit until it gets to home again.

---

Posted on *2017-06-09 14:33:40* by *davidlang*

a few questions

what depth of cut are you using?
is the sled remaining flat to the workpiece?
can you tell if the sled is twisting?
can you check that your bit is a plunge bit (looking at the bottom of it, is there a cutting surface all the way across? or only at the edges?)
where on the workpiece are you cutting? (is this all near the center? or is near one of the edges?)

---

Posted on *2017-06-09 15:56:37* by *blsteinhauer88*

cutting in center, flat surface flat sled, cut was .1 inches per pass. 1/8th end mill bit. sled not twisting, being pulled up a bit when the chain starts pulling.

---

Posted on *2017-06-09 16:24:37* by *davidlang*

I'm not completely sure I understand what you mean when you say "pulled up a bit", do you mean the sled is moving towards the top of the machine as it starts moving?

when the machine drives the bit down into the wood, does it go down and cut the hole cleanly?

can you get a video of this problem happening?

---

Posted on *2017-06-09 17:16:48* by *blsteinhauer88*

Yes, and yes. See the "c,e, c,d" all have a clean hole. That is the start as it plunges into the wood. When it starts moving, it moves the bit in the "x" direction then starts the cut pass. When done it stops the pass in the same "start" spot by moving "-x" direction, then plunges to next depth, and repeat until done. Leaving the small "Divot" in the letter.

---

Posted on *2017-06-09 17:20:06* by *blsteinhauer88*

[IMG_0019](//muut.com/u/maslowcnc/s3/:maslowcnc:nzCN:img_0019.png.jpg) it happened in the next project as well on the straight lines. See the end of the line.  The beginning had same "divot".

---

Posted on *2017-06-09 17:20:37* by *blsteinhauer88*

That was not designed turn down in the line

---

Posted on *2017-06-10 05:44:47* by *mikeberg*

Did you use an outline wood frame for lifting the router beside the wood slice

---

Posted on *2017-06-10 07:16:33* by *blsteinhauer88*

Yes, I keep some scrap of each thickness to support the sled cutting to the edge of pieces. The slice was .75 like the ply scrap frame. The sled was not rocking when it cut the problem divots. Every thing I can find is a slight movement in motors or a take up of some chain slack is the cause.

---

Posted on *2017-06-11 12:05:55* by *plefort27*

Hi i don't own a machine yet , but i think a possible cause can be a Z axis overshoot. Can you check the Z behaviour when plunging

---

Posted on *2017-06-11 15:11:22* by *blsteinhauer88*

The sled moves to new position. Then it plunges, then starts to move, the movement includes a lift, then move, then a relax at the end of movement to the plunge location, not much just enough to leave a Divot.   It should start movement from plunge coordinate, just started doing this.

---

Posted on *2017-06-12 16:52:18* by *Bar*

I had a go at making the machines motions during the calibration process smoother, and hopefully (fingers crossed) fixed the issue with the machine moving when the bit is plunging. I'll be keeping an eye on it. If you still see it happening after updating the firmware, let me know.

---

Posted on *2017-06-12 17:08:40* by *blsteinhauer88*

Will do sir, BTW I cleaned up the gcode on that sun moon if you want to try it again.  Got rid of a bunch of points and some the single point holes it was drilling.

---

