## Who is cutting, and what are you using for CAM?
Posted on **2017-03-29 07:10:54** by **rancher**:

I'm stuck, and dying to try the machine on something of my own.  I can do a basic makercam part, but anything complex I have designed in Fusion360 and they won't run in GC.  I also have used some vector programs on my ipad to create SVGs which I tried to convert using makercam and fusion with no luck.  



So.  Who has had success cutting their own design?  Can you share your process?

---

Posted on **2017-03-29 07:55:50** by **rancher**:

GRBL looks better now after the "zero offset for circles" change yesterday.  I'll go test now and report back.

---

Posted on **2017-03-29 08:16:02** by **mindeye**:

I've had mostly good luck with a sketchup -> svg -> makercam flow so far. Occasionally, makercam can't handle certain tight spaces well though and freezes up. I've also started doing dogbones as a 45 degree offset square instead of a circle as curves get treated as a super slow operation which leads to the bit burning the wood badly in that area.

---

Posted on **2017-03-29 08:21:50** by **Bar**:

When you get files that give you undesirable behavior (like going too slow and burns in the corners) I would love to see them so I can figure out what is going on. If you make an issue and attach them (in a zip file) they will become part of my to-do list and I'll fix what's wrong.



In the short term things like a 45 degree offset are good workarounds.

---

Posted on **2017-03-29 08:35:46** by **mindeye**:

I'll send them your way when I'm back at home this evening. What are you using for a feedrate / speed these days? When I consult other CNC resources on the web it seems like the originally suggested settings are way too slow but seeing as I'm still getting weird artifacts in cuts I'm hesitant to bump them up to what seems to be recommended. I'm also curious if you've experimented with climb vs conventional milling and noticed any result.

---

Posted on **2017-03-29 08:39:41** by **rancher**:

I was having endless trouble with the dogbones.  WAS!



Bar, I think that did it.  I just tested two files output from Fusion360 using the GRBL generic setting.  There was some strange Z handling at the start of the cut, up and down a bunch.  It may be an issue with my file output setting.  Otherwise, it was right on!  Dogbones and small curves and everything that was giving it trouble before. 



I also struggled getting a useable file out of Makercam if there was much detail.  I don't know if that was me or it.

---

Posted on **2017-03-29 08:45:37** by **Bar**:

Awesome!



 I was seeing the same strange z-axis behavior but I looked into the code and all those up down z-axis moves are in the gcode, not sure why but at least it's doing what it's told.



@mindseye you are right that you really should be cutting faster, probably the full speed of the machine most of the time. Right now the feedback control system can't keep up so you start to loose accuracy as you go faster, but I'll have that part of the code improved as soon as we get everyone cutting things as is.

---

Posted on **2017-03-29 08:49:50** by **mindeye**:

That's excellent news Bar! I really appreciate how active and responsive you've been throughout this process. I can't imagine anybody doing a better job.

---

Posted on **2017-03-29 08:58:24** by **rancher**:

Seconded!

---

Posted on **2017-03-29 09:32:07** by **scottsm**:

+1 ... great support!

---

Posted on **2017-03-29 09:51:22** by **Bar**:

Thanks guys, I do my best. Thank YOU for giving us the feedback and guidance about what to focus on that makes it all possible. There's no way I could do it alone.

---

Posted on **2017-03-29 10:00:39** by **blsteinhauer88**:

I cut this before the circle fix with Makercam. [IMG_0486](../../images/Mj/Rp/MjRp_img_0486.jpg.jpg) a bit oval but looks good. Will try it again. 

Last night just trying to cut the Motor mounts ended up like this,  [IMG_0493](../../images/LM/C4/LMC4_img_0493.jpg.jpg) [IMG_0495](../../images/Aa/gx/Aagx_img_0495.jpg.jpg)

Cut from top center. Ground control was even showing the error circle. Don't know if just friction or what.  I cut again from bottom center and they are ok. 



Am almost finished with Maslow frame and will recut the VW emblem. 



[51225858978__B006AC36-B3D0-4128-B5FA-5E2256AA4C99](51225858978__b006ac36b3d04128b5fa5e2256aa4c99

.jpg) this turned out cool with an intentional oval.

---

Posted on **2017-03-29 15:32:17** by **MakerMark**:

I've tried the following:

Makercam - mixed results. tabs seem to cause random depth and direction changes.

Easel - works great. no issues so far.

Aspire / vCarvePro - both work great when using NC-Easy format.



To be fair, I haven't tried Makercam using the latest firmware and Ground Control.

---

Posted on **2017-03-29 15:47:15** by **rancher**:

Wow, Easel looks really interesting!  Thank you.

---

Posted on **2017-03-29 19:31:07** by **blsteinhauer88**:

DrawSVG.org is a simple program to male and sketch svg files.  Makercam is what Ive been using, but love the look of Easel.  Thanks!

---

Posted on **2017-03-30 14:04:46** by **scottsm**:

Thanks @makermark for the tip about Easel. It's a very nice tool and feels more robust than Makercam. I like being able to arrange and align the objects. I'm interested to try the 'Image Trace' import method.

---

Posted on **2017-03-30 16:11:45** by **alstaxi**:

www.tinkercad.com



really simply and easy

---

Posted on **2017-03-31 10:30:32** by **blsteinhauer88**:

I used easel last night after the tip here from @makermark. So much better than makercam! You can actually see how gig you dimensions are, and not count tiny blocks to determine size. It also imports in at correct size. You can easily set up the pieces in a specific work space, and export Gcode. It worked great.

---

Posted on **2017-03-31 11:59:44** by **blsteinhauer88**:

[IMG_0501](../../images/yf/iy/yfiy_img_0501.jpg.jpg)

---

Posted on **2017-03-31 16:07:49** by **davidmarkman**:

I'm just a future backer, but I use Fusion360 to output gCode for my Shapeoko, does that not work for the Maslow?

---

Posted on **2017-03-31 16:20:01** by **davidlang**:

we're trying to figure out what output settings for fusion360 will work



we also don't want to be dependent on one source.

---

Posted on **2017-03-31 16:26:03** by **davidmarkman**:

@davidlang, nice first name.



Thanks for answering my question.  I thought that gCode was gCode, and the source of the gCode does not matter.  I thought the Maslow had a gCode interpreter.

---

Posted on **2017-03-31 17:04:28** by **davidlang**:

unfortunately not all gcode is the same. different machines understand different subsets of all possible gcode.



simple CAM programs tend to output only the simplest gcode, the fancier the CAM program (and fusion360 is among the fanciest) will use more sophisticated gcode features. This is why fusion360 has a large pull-down menu asking you what type of machine you have.



Part of the machine setting is setting limits/defaults for things like speed, but part of it is what subset of gcode to use

---

Posted on **2017-03-31 17:39:42** by **Bar**:

It seems like the grbl-generic gcode generator in Fusion 360 works, but we're working with them to add a Maslow option to make the choice more clear. It seems like Fusion 360 is a popular platform and we'll make sure it works smoothly

---

Posted on **2017-03-31 18:08:19** by **rancher**:

Fusion360 and Ground Control/Maslow are getting along great after all of Bar's hard work.  If you are using Fusion360, when setting up your post process, use the Post Configuration "grbl.cps - Generic Grbl".

---

