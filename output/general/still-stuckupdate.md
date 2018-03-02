## Still stuck....update
Posted on **2017-04-16 10:27:30** by **rancher**:

I'll open an issue in github Bar, but I thought I'd detail what is happening and start a discussion here so the issue/issues are more clear.



First, I'm still struggling with Z.  I am never in the material.  I have done dozens of variations of settings in Fusion360, and just now I noticed something.  I put the bit on the wood, hit Zero Z in GC.  All good.  Then I hit home.  GC retracted the bit .25 before moving home.  Makes sense.  And then I wasn't paying as much attention, but, it appeared that it reset back to zero.  Then when I hit run, it took off towards the start point without retracting again, which is one of my problems.... but then I think it did retract when it got to the start point, before the gcode z commands began?  So maybe there's part of my issue.  It seems I'm always starting way up high and can not figure out why.



Secondly, position.  I am running more tabbed flat panels to try to get them to fit together so I can check registration accuracy.  I'm hoping to use Maslow to cut some very expensive material, so I'm trying to get it good before I actuall y use it for my project.  Every time I try to do these panels, like the riser file I sent you, lately I'm getting the "lost position" circle and drifting.  Not as bad as it was weeks ago, it now catches back up.  I went down to 5ipm and still it's lost at the second corner.  



And lastly, I would like to ask again, am I the only one trying to cut with files out of Fusion360?  I think I am.  If anyone else is, I'd love to compare CAM settings notes.  Heights and smoothing and whatnot.  Thanks team!

---

Posted on **2017-04-16 10:52:34** by **Bar**:

The CAM process can be really tricky. I don't have enough experience with Fusion 360 to be able to offer specific advice, but I can say that I think it's a great piece of software and that I want to make sure it works so any issues you are having are a priority to fix. Conveniently, some people from the Fusion team are interested in what we are doing and they are coming to visit on Tuesday. It's convenient that they happen to work right down the street. 



What I am going to ask for from them is 1) a Maslow specific CAM processor so that there is no confusion about generating g-code 2) Clear instructions for designing parts and generating g-code in Fusion 360 with a focus on designing parts to be cut from a flat sheet.



The drifting circle issue sounds like it's 100% my problem. You shouldn't have to run at 5ipm, that's crazy slow. I've made an issue for the problem [here](https://github.com/MaslowCNC/GroundControl/issues/202). I know you've sent me the riser file before, but just so I'm sure I'm working on the right file, would you be willing to attach the latest version  which isn't working to that issue? 



I've also made an [issue](https://github.com/MaslowCNC/GroundControl/issues/201) for the crashing when hitting the Home button issue. I've seen that one too. I'm still a little in the dark as to what is going on, but I'm on it!

---

Posted on **2017-04-16 11:50:27** by **rancher**:

I'll attach a new file, it's something different.  



As for Fusion, like I said, I'm down to the little details now, and I think I got it, but the Z is somehow being thrown off from the start of the run.  I think it has something to do with ground controls' built in retract height?  I'm totally guessing.



I replied to crashing on home.  I saw it, it frustrated me, now it's gone.

---

Posted on **2017-04-16 12:01:26** by **blsteinhauer88**:

I am really digging Inkskape.  You can set a bunch of guide lines and use the Bezier pen to draw paths by hand. Saves as SVG and MakerCam has been processing the files fine, or you can use Easle to set up the cuts for your SVG.

---

Posted on **2017-04-16 12:10:31** by **rancher**:

How well does it do complex 3d modeling? 



edit...oh, I just checked it out.  I'm needing more than vector work for the project I intend Maslow for.  Thanks for that though, I do all my vector work on the ipad, I didn't know inkscape was free for desktop.  I'll use that for my vector stuff for sure.  Great tip!

---

Posted on **2017-04-16 12:18:46** by **blsteinhauer88**:

I am not good with 3D so that would have to be seen....😄

---

Posted on **2017-04-16 12:24:02** by **scottsm**:

What do you use for vectors on the iPad?

---

Posted on **2017-04-16 12:32:10** by **rancher**:

Graphic is my favorite, but inkpad is good too.

---

Posted on **2017-04-16 18:38:41** by **jbarchuk**:

> @rancher

> First, I'm still struggling with Z. I am never in the material. I have done dozens of variations of settings in Fusion360, and just now I noticed something. I put the bit on the wood, hit Zero Z in GC. All good. Then I hit home. GC retracted the bit .25 before moving home. Makes sense. And then I wasn't paying as much attention, but, it appeared that it reset back to zero.

I suggest taking Fusion and most of the GC out of the equation, to find out if the basic hardware is working properly.

Write some super-simple g-code.

Manually move to a position on the working material. Doesn't matter where. G-code does pen-down, pause, penup, pause. Done. Then put that in a loop or copy/paste the same code to make it do the same thing 20x in the same location. The first plunge cuts wood, and you see how the router/z-motor move. Anything that goes slightly out of repeatable is a clue. 

If that works then add several depth levels, without doing any x or y movement. Add a pause at each depth level so you can -see- that it works.

If that works then add -one- x-dimension move ment of only an inch or so. Pendown, move, penup, stop.

if -that- works add a y movement. Pendown, x move an inch, y move an inch, pen up, go back to start. Don't cut out a piece by making a complete loop because that really needs tabs so the loose part doesn't flop around.

Never mind dimensional accuracy, the point of all this is to see if the machine works mechanically.

There are two big advantages to these kinds of tests. One is that by cutting only small x and y dimensions one can fit many tests into only a few square inches of material. The other is that by moving only an inch it wastes a lot less time than moving a foot or whatever.

If all those tests work the you have confirmed basic good working hardware, albeit without measuring accuracy.

In order: crawl, toddle, walk, run. Jumping off the blocks into a full tilt boogie, and crashing, then trying to debug that, is MUCH harder to debug because the more basic malfunction may have been at the crawl or toddle level of operation.

And it COMPLETELY takes Fusion out of the mix.

if all that DOES work, then use Fusion to make g-code that does -exactly- the same very simple motions. Again it should be totally repeatable. The first time it does something 'different' is a clue. Because you've been looking at the same motions with manually entered g-code you'll be used to the sights and sounds of how the machine behaves, and anything out of the standard motion envelope will be more obvious, and those are clues.

Oh, forgot to say, one can take even the g-code out of the mix by doing similar tests with just the GC control panel. It's just more annoying having to push all those buttons, especially for many identically repeated tests.

Oh forgot to say, the FIRST time the machine does something not quite right, STOP. Don't even bother doing anything further till that clue is analysed, debugged, and the problem fixed. Heck it could be a hardware, software or firmware problem that's never been noticed before. This is a standard software debugging technique, because a list of 100 errors can very often be cut down to 10 or 3 errors by fixing the -first- bug that appears. The further 97 bugs weren't bugs at all but were artifacts -caused- -by- the first error.

---

Posted on **2017-04-16 19:44:13** by **rancher**:

You seem knowledgeable Jbarchuck.  Fusion is free.  Will you please download it and try to create and cut a file?  I would find that incredibly helpful.

---

Posted on **2017-04-17 10:38:47** by **jbarchuk**:

> @rancher

> Fusion is free. Will you please download it and try to create and cut a file?

I've already been doing Fusion for maybe 3 years. The first year was a waste SPECIFICALLY BECAUSE their tutorials did *NOT* advise what later became known as 'R.U.L.E. #1.' That phrase was actually coined by a user not by Autodesk, but Autodesk themselves did use it. (The dots don't mean it's an acronym, but for EMPHASIS how important it is.) The second year I pretty much took off because for the design I was TRYING to do there was a weird terminally serious bug, that later turned out to not be a bug but was RELATED to the frigging Rule #1 issue. Can't really complain because I did get exactly what I paid for. LOL!! I don't have anything cut yet because still dealing with OS and software issues.

Like I said though, take the design software out of the equation to make sure the hardware ducks are all lined up in a row. If that works, then use fusion to make a super-simple shape, maybe a 1" square with a hole in the center the diameter of the bit. The resultant g-code should also be s uper-simple, less than a screen's worth. If it's not super-simple and straightforward g-code then it's not impossible that may be part of the issue, that there's too much useless 'silly code' that confuses the GC.

UNfortunately if that turns out to be the case it's not as if Autodesk is gonna change -their- system to accommodate Maslow. If there are silly code issues Bar will need to figure out how to deal with it. That's not necessarily a bad thing either, because it may result with firmware that's -more- adaptable to -other- silly code. (There's a lot lot LOT more silly code out there than not.)

---

Posted on **2017-04-17 11:09:03** by **rancher**:

You've been using it for years?  Great!!  Perhaps you could walk me through setting up the z heights in the CAM?  I've set the clearance, retract, and feed heights as relative to origin rather than stock top, and the bottom of the cut typically is stock bottom.  My paths appear correct, but I suspect GC does something at the start of the file that throws it all out of whack.



As for taking the software out of the equation, that won't help me.  Nor does your speculation.  I want to use this software.  You seem eager to help with these long "you should" posts you write.  Perhaps you could use fusion to output and cut a file and walk us beginners through what worked for you since you are so experienced.  I'd sure appreciate it.  I'd love to have some dialog with someone who has used fusion from design to cut successfully.  So far I think I'm the only one.

---

Posted on **2017-04-17 13:39:00** by **rexklein**:

Z-axis I have the same problems it should have it's own setting place and not be dependant on the sled calibration. I get very different results drastically different results.  @Bar pretty please give the Zaxis its own setting menu that does not share the move distance with the sled. please...

---

Posted on **2017-04-17 13:42:51** by **rexklein**:

I think (but am not sure) that whenever I press home my z calibration is lost or at least changed in some way that requires me to seem to have to reset it every time.

---

Posted on **2017-04-17 13:51:29** by **Bar**:

Sure thing! If you make an issue for it on GitHub I will make it so :-)

---

Posted on **2017-04-17 13:53:22** by **scottsm**:

I think issue #154 on GroundControl describes this, yes?

---

Posted on **2017-04-17 14:16:09** by **Bar**:

I believe it does! Thanks for catching that.

---

Posted on **2017-04-17 17:28:19** by **Bar**:

Separating the z-axis controls out into their own thing should be added in the latest version of Ground Control. If you are running it from the source code, you can grab it now or if not it will be a part of the Wednesday release.



Good suggestion everyone!

---

