## Cutting bit size / feed rate / cutter head RPM
Posted on **2017-03-21 11:15:08** by **thatoneguydavid**:

Folks, i have been communicating for several months with Bar but this is my first community post.



the other day Bar and i were talking about what tool he is using and at the time he was primarily using a 0.5" up cutter.   He had found that the router motor was not able to spin fast enough to achieve efficient cut speed with the smaller 0.125" or 0.25" bits he had originally been using.   Using a cutter head with a larger diameter the cutting surface is moving much faster... i dont exactly remember the tangent velocity equation, but it make intuitive sense.    



this prompted me to thing about how the cutter is cutting.  it is my understanding that currently the software controlling the cut uses the radius of the cutter head to calculate the offset from the line to be cut.   Any cut that is made in this way will by definition have 180° of cutting surface as it is cutting a channel through a sheet of material.  

my proposal is to change this slightly.  it will require a method of retaining the work piece (tabs should work fine).  the idea is that the initial cuts be made  some fraction of the cutter head diameter away from the line.  this would mean that the first passes with 180° of cutting surface would be 'rough' cuts.  once these rough cuts have been made the tool offset would be adjusted and a final cut would be made.  this would mean that the finish cut would have drastically lower force, potentially improving the cut surface while using a smaller bit.



i do not yet have my system set up as im currently working on a solution for Z height control.  (see my other post)  



is there someone in the community able to test this theory?

---

Posted on **2017-03-21 11:42:06** by **davidlang**:

That is up to the software that's creating the toolpath, not the maslow software.



But yes, it is common practice to make a cut just slightly larger than what you want the final dimensions to be and then do another pass to the final dimensions. Tabs work well to support this.

---

Posted on **2017-03-21 14:58:35** by **rollandelliott**:

just make two drawing files that that is slightly bigger. many drawing programs have a countour command that would allow you to do this takes all of ten seconds.

---

Posted on **2017-03-21 15:02:55** by **rollandelliott**:

[Screen Shot 03-21-17 at 03](//muut.com/u/maslowcnc/s3/:maslowcnc:qcxJ:screenshot032117at03.01pm.png.jpg) 

here is a sample, red line is the countrour cut out spaced .3" out from the final cut.

---

Posted on **2017-03-21 15:05:26** by **rollandelliott**:

I am very surprised to hear that 1/4" bit was not sufficient and a 1/2" bit needed to be used. actually shocked. can't wait to try out my machine.

I often do a rough cut and then a final cut when cutting out aluminum sheet metal and it makes a world of difference but I was hoping to avoid that step with maslow.

---

Posted on **2017-03-21 15:06:25** by **rollandelliott**:

I guess the real question is how well can maslow register two cuts so the second cut is perfectly centered over the previous one?

---

Posted on **2017-03-21 15:14:58** by **Bar**:

I actually almost always use a 1/4 inch bit. I think the 1/2 inch bit gives a slightly nicer edge finish, but it's fairly comparable. 1/8th inch bits work well for thinner materials like 1/4 inch plywood.



The registration should be pretty good. I've found that when cutting a part in multiple passes it follows the same path very closely. There's a little bit of jitter because the feedback control system is pretty rough around the edges right now, but I expect that to go away pretty quickly.

---

Posted on **2017-03-21 15:15:57** by **Bar**:

Another simple way to set up the cut would be to set the tool size to .05 inches larger than the real size, when the gcode is generated, an offset will be added

---

Posted on **2017-03-22 19:16:56** by **traviscadden**:

I was just going to mention this: Create a "roughing" tool with a size slightly larger than your actual bit, build the toolpath, then a "tool change"  where the machine just pauses and then a second pass at the correct tool size. You can also set the depth of cut on the first size to slightly less than final depth if your cam software doesn't do good tabs, but that is a bit trickier.

---

