## Wiki QoL changes
Posted on *2017-07-14 22:52:25* by *mrfugu*

In advance of piles of new ppl assembling their machines, I took it upon myself to give the wiki (which is actually 5 separate wikis, for each sub section of the machine) a good once over to make it easier to jump around. In light of the current state of the searching the forum here, I would ask everyone to take a look and contribute where able.  

In particular, it would be great to get any routers other than the Ridgid22002 with functional Z-Axis listed, some more Router bits tested/reviewed and much more detailed instructions on GroundControl troubleshooting and operation, inc the new Simulator.

---

Posted on *2017-07-15 01:50:44* by *gero*

Nice! Great job! The top menu makes it much easier. Still confused if the  troubleshooting should be in Mechanics. But spreading it out, is also not good. Perhaps a separate page with guided steps to follow.

---

Posted on *2017-07-15 12:16:28* by *jwolter0*

I just grabbed the Ground Control package and dashed off a quick wiki page for installing Ground Control (based mostly on the readme.md file).  Still need to do the Linux side of that.

---

Posted on *2017-07-15 12:33:05* by *mrfugu*

please integrate your page within the context of the 'Software' Home page. ie: there are already installation pages for the 'big 3' os's, please add your instructions to them as applicable.

---

Posted on *2017-07-15 12:33:34* by *jwolter0*

Will do.

---

Posted on *2017-07-15 12:34:17* by *jwolter0*

Breaking away to mow the lawn.  The real world intervenes.

---

Posted on *2017-07-16 15:14:42* by *jwolter0*

Okay, so I fixed the "damage" I did yesterday.  I had followed a link to a missing page and jumped right in creating it, when I should have checked to be sure the page didn't exist elsewhere.  That broken link has been fixed as well.  

One question I have for the group is, "Why are the GroundControl installation instructions for Raspberry Pi a subsection of the Linux page?  Yes, I know that Raspberry Pi runs a version of Linux, but so is Android which has its own page.  It's not the most important thing in the world, but it seems more consistent to have a separate page for each O/S.  Thoughts?

---

Posted on *2017-07-16 15:35:49* by *Bar*

I agree completely that Raspberry Pi should have it's own page just like Android. That was my mistake, I didn't realize how different setup on the R-Pi was going to be when I started writing the instructions :-)

---

Posted on *2017-07-16 16:08:14* by *mrfugu*

I'll split it out, no sweat.

---

Posted on *2017-07-16 16:23:21* by *davidlang*

how different are the Raspberry Pi instructions from other Linux systems?
 
I would expect that they would be pretty close to the same as any other Debian/Ubuntu/apt based Linux system. RedHat/Fedora/rpm based systems would be very different, but the differences within each family should be fairly minor (different package names and/or versions, and these will change over time anyway)

---

Posted on *2017-07-16 16:30:48* by *scottsm*

The Raspberry Pi instructions begin by installing a distro - 'KivyPie' - that has the Kivy environment pre-installed, so on that path it really is different from the Debian/Ubuntu/apt path.

---

Posted on *2017-07-16 16:32:33* by *mrfugu*

https://github.com/MaslowCNC/GroundControl/wiki/Raspberry-Pi

---

Posted on *2017-07-16 21:13:20* by *mrfugu*

2 new pages detailing operation and accuracy considerations for the router sled and the frame. 

https://github.com/MaslowCNC/Mechanics/wiki/The-Router-Sled
https://github.com/MaslowCNC/Mechanics/wiki/The-Frame

---

Posted on *2017-07-16 21:38:53* by *Bar*

Beautiful work!

---

Posted on *2017-07-16 21:52:40* by *mrfugu*

https://github.com/MaslowCNC/Mechanics/wiki/Stock-Materials and goodnight. Rock on!

---

Posted on *2017-07-17 01:34:40* by *cameronswartzell*

So good.

---

Posted on *2017-07-17 02:27:09* by *davidlang*

I've pointed out raptor plastic nails before, they are safe to cut through without damaging your bits or running the risk of sending stuff flying.

---

Posted on *2017-07-17 02:32:59* by *davidlang*

in the page on the sled, the most likely problem from the chains being at the wrong height is that the chain will skip or come off the gears, not that they will bind up or take any noticeable extra torque to turn the motors.

This is most likely to happen near the upper corners.

the page makes it sound as if you need to adjust the mounts on the sled for every piece of wood you are cutting. This is far from the case, especially if you aren't near the upper corners, you shouldn't have to adjust the mounts unless you change the thickness of the workpiece by over an inch (very likely more, going between a 2x4 and 1/4 plywood probably does not require changing the mounts)

---

Posted on *2017-07-17 02:35:39* by *davidlang*

where does the information come from that claims that weight on the sled causes inaccuracy near the top of the workspace? I've seen no information posted suggesting that.

---

Posted on *2017-07-17 05:27:19* by *mrfugu*

@davidlang all of these are only starting points and I still have yet to receive my maslowCNC so its all hearsay as far as I'm concerned. 

 please feel free to add your expertise to any wiki page. 

the plastic nails are listed as an option on another page, i'll link to it. 

as for the sled weight/inaccuracy, i inferred it based on earlier frame flexing warnings, there will be inherently more tension on the chains, the higher on the work surface they hold the sled, any flex in the overall frame could occur with a heavier sled is used at the top of the work surface. I probably could word it better and link to the frame flexing page.

---

Posted on *2017-07-17 05:38:28* by *mribble*

The link to step 3 doesn't work on this page anymore.  http://www.maslowcnc.com/assemblyguide/

---

Posted on *2017-07-17 05:46:45* by *mrfugu*

use this to find the page you're looking for, https://github.com/MaslowCNC/GroundControl/wiki 

some pages in the wiki were renamed for clarity, and the (non wiki) assembly guide links need to be updated.

---

Posted on *2017-07-17 07:34:04* by *mrfugu*

@davidlang I reworded the Router Sled page to include you points.

---

Posted on *2017-07-17 11:41:27* by *mrfugu*

the assembly guide broken link has been fixed

---

