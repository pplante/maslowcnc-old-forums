## Scaled down Maslow for RC and other modelling?
Posted on *2017-05-18 02:25:53* by *dkchris*

Hi - just sort of stumbled onto this great project.

I must admit the very first thing that occured to me was the possibility to scale down the concept, specifically with "2.5D" cutting of foam sheets in mind. The lighter and softer material require far less force to cut and support, cutting down cost allround for motors/drivers, backing plywood gauge and the router itself etc, with the control electronics being the only major difference. Typical raw material sheet sizes would be in the range 20"x30"(Adams Readi-board known from Dollar tree stores) to 80x120cm (Pallet sized Depron or Fan-fold foam sheets for isolation).

A solution like this would be a great fabricator tool for modelling, be it for architects, students, artists, or as in my case RC aircraft modellers. Might i suggest to check out www.flitetest.com - building RC aircraft from folded up foam sheet has become quite the craze in recent years. And Cad/Cam has become a growing part of this movement.

The RC world already has spawned a couple of such specialized CNC solutions, most notably the PhlatPrinter. And  as far as I can see a scaled down Maslow design would have them beat by a long run for at least 3 reasons:
1) Simplicity and ease of build - most other designs require you to either buy an expensive structural parts kit or already have access to CNC equipment to even make the parts for it.
2) Space taken up in use and storage. For most modelers I know, their Hobby space is limited, and gantrys and similar solutions are heavy, bulky  and difficult to find storage space for. This is pretty much just a router unit and a plate. Easy to store. And the upright, scaled design could probably be run on a ordinary tabletop, not requiring extra floorspace.
3) Cost. Even if small, gantry structural kits are usually expensive to both buy and ship. And electronics cost would be at least the same.

Another idea that came to me as well was to replace the router unit with a needle cutter unit (Think sewing machine concept) like this: http://forum.flitetest.com/showthread.php?24251-Cutting-foam-sheets-with-a-needle!
For RC'ist, the Z-axis would probably be more straightforward if implemented as a standard Servo solution, but as far as I can tell, Ground control does not support this(?)

Your opinions would be valued :)

Christian Christensen, Denmark
Aeromodeller

---

Posted on *2017-05-18 02:33:01* by *dkchris*

Bit of nonsense to edit: "..the control electronics being the only major exception" .....not "difference". Sorry.

---

Posted on *2017-05-18 03:37:07* by *davidlang*

The router is already overkill for cutting full size stock, mounting a different cutting head would be trivial to do.

There are already a couple of beta testers who have made the maslow frame hinged (one to the wall, the other to the cealing)

One thing to remember is that the maslow is limited to cutting such that the sled is still supported by the uncut stock, so it's great for cutting through anything in whatever shape, but it's not that good for cutting a 3d shape (cutting a wing could be done if you make sure the panels are large enough that the sled never falls into the cut area for example)

This is already using the smallest roller chain available, so you aren't going to shrink things down there much, you could go with smaller motors, and the existing motors are already overkill, but they aren't that expensive so you won't really save much.

The existing software supports different size machines (everything is parameterized) so you could build a smaller machine if you wanted to bery trivially.

But remember, the current cost of the maslow kit does not include th e lumber to build the frame (which is a sheet of flat stock to hold your spoilboard, legs to hold it up, and a couple of 2x4s to hold the motor), so building a smaller machine isn't going to save you very much money

one thing you may not be aware of, the workspace available to you from a given motor position is dependent on how powerful the motors are, and how accurate they are, the less powerful the motor, the higher the motors need to be above the cut area. The current maslow design has the motors a little over a foot above the cut area and just under a foot outside the cut area.

The current machine is roughly 6' tall by 10' long, for a 4'x8' cut area. Change this to a 2'x4' cut area and the machine is still going to be 4' tall by 6' long (and if you use less powerful motors, taller)

---

Posted on *2017-05-18 04:57:29* by *jwolter0*

I had wondered once about using "bead chain" if you wanted to make a smaller machine, involving lower forces.  Don't know if that would save any money, but...

---

Posted on *2017-05-18 05:05:48* by *dkchris*

Quote, davidlang:"One thing to remember is that the maslow is limited to cutting such that the sled is still supported by the uncut stock, so it's great for cutting through anything in whatever shape, but it's not that good for cutting a 3d shape (cutting a wing could be done if you make sure the panels are large enough that the sled never falls into the cut area for example)"

I am aware of this limitation; For that specific use a hotwire cutter is the way to go for the vast majority of constructions; This setup with a small router head would be usable to cut ply templates for manual hotwire cutting, however.

For the use i'm proposing, all that is needed is to be able to cut narrow traces either all the way through or about halfway through (for hinging etc.) , hence the "2.5D"  in my first post.

Thank you for the info on motor offset distances. From what I gather, this would mean that a setup capable of cutting an 80x120cm sheet would have to be somewhere in the range of 140x180cm or 4.5 by 6 feet. Thats roughly 3/4 of a sheet of plywood with a couple of extra ½ foot  extensions for  height. A bit of  the large side, but not unacceptable.

In RC I have seen similar types of suspended setups for hotwire cutting(4-axis with 2 sets of lines) succesfully using cord wound on spools in stead of the rather heavy chains. Wouldn't this combined with a far lighter router assembly improve the lifting capability a bit?

A different and probably more functional solution could actually be to have the motors/pull lines suspended from the ceiling, and just have plain plywood sheet to setup with reference marks or fittings to lock in the right position on the countertop or floor relative to the ceiling reference points. That's actually how the above mentioned hotwire setups were rigged.

---

Posted on *2017-05-18 05:10:24* by *davidlang*

the nice thing is that the design and software is fully open, so you can experiment on this.

one thing is that the forces at the top center can be far higher than you expect. grab the program at lang.hm/maslow/v-plotter.py

play around with the settings at the top of the file and see what size the resulting cutting area would be as you change the settings. You will want to play around with the tension settings, they are defined as a multiple of the sled weight, if you go with much less powerful motors (and weaker chains), you won't be able to put as much tension on things as the maslow, and that can affect the available cutting area.

---

Posted on *2017-05-18 05:29:03* by *dkchris*

Yeah, I get the part about the need for the angle between the chains/lines to not get to far into the obtuse, as the motors increasingly work against each other rather than providing lift as the router unit moves up, as well as the need for a minimum outwards angle towards the nearest suspension point as the router moves towards the horisontal ends to maintain sufficient tension in the chains/lines to keep the .
I'll look into your V-plotter (calculator?) program, thanks  :)

"Sadly" I'm currently about midway into another CNC build, classic gantry style (Goodenoughcnc Hybrid), but this'll definitely go on my "want to do" list, as i as mentioned can see this having possibilities in the RC community.

---

Posted on *2017-05-18 07:13:30* by *Bar*

A big part of the reason we are open source is to encourage others (even companies) to adapt the idea for different markets. 

I used to build foam airplanes and I can completely relate to the need.

I think that there is a space for a scaled down machine which uses a Dremel type cutting tool and possibly an even smaller version which could compete with the small low wattage laser cutters like Me Beam. Even a few watt laser could cut foam quite well I think.

I can't wait to see all the ways other companies addapt the idea to serve different communities.

---

Posted on *2017-05-18 07:51:43* by *dkchris*

And we appriciate your efforts :)
Flite test currently use inhouse industrial grade laser cutters to create precut kits for their planes, but have recently started up FT stem http://www.fliteteststem.com/, an educational initiative aimed at primary and secondary school students, partly to broaden the awareness of the hobby, but primarily to make use of the many opportunities to teach design, construction and the many other disciplines incorporated in our hobby.
These Stem units would benefit a lot, both on cost, possibilities and educationally from a cnc solution like a Maslow "light". Heck, even the name contains a lesson :)

Quote, jwolter: "I had wondered once about using “bead chain” if you wanted to make a smaller machine, involving lower forces. Don't know if that would save any money, but…"

Someone else had the same idea:
https://www.youtube.com/watch?v=7DIV2-xWDak

---

Posted on *2017-05-18 07:59:57* by *TheRiflesSpiral*

For a very small area like you're suggesting, the router sled could be much larger than the workpiece. This would allow standoffs to be mounted in the corners. The sled would ride on those supports rather than the workpiece. This would allow Maslow to be truly 3-axis in this configuration.

---

Posted on *2017-05-22 09:56:04* by *rowandoughty*

This is the exact thought I had when I saw the maslow last night! I just recently built myself an FT Explorer and Versa Wing and whilst they were really fun to build, I have to admit marking and cutting out the boards was a little tedious. I have to say though I'd be more interested in building a full size maslow but with a swappable cutting head with something like a dremel or foredom power carver on it but I don't know quite how I'd secure the foam board in the middle. And like you say maybe the weight will be an issue resting on the foam. The idea of a little laser like Bar suggested is really interesting though...

---

Posted on *2017-05-22 10:05:54* by *rollandelliott*

Just use doublesided tape

---

