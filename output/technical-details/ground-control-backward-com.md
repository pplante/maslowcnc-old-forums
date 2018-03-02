## Ground Control Backward Compatibility
Posted on **2017-01-10 08:26:37** by **stevet44**:

I'm building a 2'x4' XYZ router using the MakeSmith control system.  I was wondering if the Maslow version of Ground Control would be backward compatible with the R/C servo based system used in MakeSmith?

---

Posted on **2017-01-10 21:37:08** by **Bar**:

Yes, not only will it be backward compatible, but I would like to maintain support for a conventional XYZ setup into the future. It would be relatively easy to take the motors from Maslow and use them to control a more conventional XYZ type CNC router. 



I like the idea that you could get your Maslow kit, use it to cut out the parts for a 4x8 (or any size) CNC gantry and then do 3d relief work if you really wanted to.



Keep us posted with how your build turns out, and let me know if you have any issues.

---

Posted on **2017-01-12 12:55:52** by **stevet44**:

Only issue so far is that the MakeSmith PCB files have disappeared off of GitHub.  Is there another source for them?  I need the power distro board file (or schematic).

---

Posted on **2017-01-12 22:26:09** by **Bar**:

Yeah, that's an issue. You can find them under the "releases" tab here: https://github.com/MaslowCNC/PCBs/releases. Because the goal is to continue support for conventional XYZ style machines I chose to not make a new repository, but instead build on the old one. 



That made more sense early on because the original prototypes for Maslow used the same encoders as Makesmith and so the PCBs were derivatives of the Makesmith boards (in fact the first working prototype was built entirely from electronics scavenged from a Makesmith). As the design evolved, I chose to use higher resolution encoders built into the motors and all the PCBs changed meaning some of the obvious reasons to share a repository were lost.

---

Posted on **2017-01-13 13:33:25** by **stevet44**:

Thanks for the link.  FYI, I'll be using the AMS encoder eval boards and a three channel r/c motor controller in my project.  Here's the links in case someone else wants to go down this road.



http://www.digikey.com/product-detail/en/ams/AS5048B-TS_EK_AB/AS5048B-AB-1.0-ND/3188613

http://robotpower.com/products/hydra_info.html

---

Posted on **2017-01-13 16:06:45** by **Bar**:

Those eval boards are sweet. I didn't know about those. I ended up migrating away from the AMS encoders because the output is actually pretty not linear, so while the resolution seems good enough, I was always ending up with wavy cuts. In the data sheet there is a little " *with external linearization " I wasn't prepared for just how inaccurate the output of that chip is without the linearization and I sunk a couple weeks into it, so if you start seeing wavy cuts, swap the encoders and it will go away.

---

Posted on **2017-01-14 06:33:08** by **stevet44**:

Not linear huh?  Well I guess since I already ordered the AMS boards I'll see how much of an issue it is on a mid-sized gantry router.  The encoders could be placed before the mechanical reduction to minimize the issue but then the software needs to take into account for backlash. Will be thinking about this.  Which encoders are you using for Maslow?

---

Posted on **2017-01-16 11:13:46** by **Bar**:

Yeah, I'd say go for it and see. No point in solving an issue that hasn't cropped up yet :-). We're using encoders which are built into the motors so I can't give you a part number or anything. Basically the encoders we're using are a disk of NSNSNS oriented magnets which pass by two hall effect transistors to generate the pulse train. They are pretty much as simple and solid as you can get which I like about them.

---

