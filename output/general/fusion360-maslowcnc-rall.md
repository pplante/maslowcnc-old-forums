## Fusion360 + MaslowCNC: Rally Here!
Posted on **2017-07-07 10:29:52** by **mrfugu**:

Hey folks,  I've updated the 'unofficial' Fusion360 MaslowCNC file here: 



http://a360.co/2sV4YRd



I've added the latest parts models from last week, and refined the tool paths to include both 'simple' and 'advanced ' paths. The 'simple' paths will cut the parts and leave the countersinks to you. The 'advanced' paths incorporate pockets for the Rigid Router sled, mounting hardware, engraved angle brace numbers (soon) round-overs with a v-bit and other refinements as the machine evolves.



I've also found a 2nd Fusion360 > GRBL post processor that purports to be a refinement over the one included by Autodesk, I'm hoping that we can further tweak this for GC. 



https://github.com/Strooom/GRBL-Post-Processor



Anyway, until a new forum comes along, let's use this thread to collaborate on Fusion360 settings to get the best results out of MaslowCNC.  Please feel free to contact me within Fusion360 via the file above if you wish to contribute or collaborate on the 'unofficial' file. 



cheers

---

Posted on **2017-07-09 09:37:56** by **heidenmason**:

Yay, I love Fusion360

---

Posted on **2017-07-09 14:57:47** by **spyker**:

Fusion360 is my CAD of choice!

---

Posted on **2017-07-13 10:34:28** by **Meticulous Maynard**:

This is a great idea! Good to have everything in one spot. I like the work you did for the different toolpaths.



I have been using Solidworks now for years although given the built-in CAM functionality I am beginning to switch over. There are quite a lot of similarities between the programs so I should be up to speed in no time. One of the nicest things about Fusion is it will allow us to work collabortatively on the project.



Do you want the model of the machine in your Maslow folder? I imported a STEP file of the entire machine from GITHub, could be useful if you're trying to plan out shop layouts or something. In my case it was most useful because I'm changing my machine quite a bit from the stock version. I only have 112" wide for my machine so I need to narrow it down a little. I would also like to make a plasma cutter sled for mine, so I made the frame from steel.

---

Posted on **2017-07-13 11:20:35** by **mrfugu**:

excellent! Yeah, my long term goal was to incorporate the entire machine as a 3D model, and then construction layouts for the parts on a sheet complete with paths and whatnot, everything short of the .nc file exports. I think it will give people new to Fusion360 a good overview of everything that can be done with it and growing out MaslowCNC as it evolves. I just finished a revision to things for the /Mechanics folder, and included a new section with Add-ins and Scripts, and will try to get the Maslow Router Bits into tool definitions, so yeah, lets aim for the whole kit-and-kaboodle!

---

Posted on **2017-07-13 14:34:56** by **Bar**:

The guys over at Fusion are asking what post processor most people are using and I wasn't sure. What post processor is everyone using in Fusion?

---

Posted on **2017-07-13 16:07:34** by **mrfugu**:

As I understand it, there are currently 2 GRBL post processors: 



One is included with Fusion 360, and the other is linked from my unofficial Fusion page, I just found it on the web, and it claims to 'solve some issues with the built in one' that apparently lingered long enough for someone to attempt another.  



Unfortuinately, I don't have a MaslowCNC yet, (order #01853 btw if you want to encourage me to continue 'at pace' =) 



Really the 'guys at Fusion' are going to be the best ppl to ask about a custom Post Processor,  I assume that an effective one is going to take into account many aspects of Maslow, and allow for the outputting of Gcode that doesn't exceed our necessary levels of precision, tolerance, and the technical limitations, and shortcomings of the hardware.

---

Posted on **2017-07-13 16:47:29** by **Meticulous Maynard**:

@Bar: I'm still learning Fusion so I don't know too much. I watched the video Rancher made back in April but that's about the extent of my knowledge. I'm one of the kickstarter backers so I should be getting my Maslow soon and begin experimenting with it. I'll let you know what I figure out.



@mrfugu: Do we have an A360 group setup for the Maslow yet? I was able to download your file. I have my STEP file import here: http://a360.co/2uf7Ahg For some reason one of the arms didn't import, so I still have to go and mirror it.

---

Posted on **2017-07-13 17:01:01** by **rancher**:

I use the GRBL-Generic still.  It is working well.

---

Posted on **2017-07-13 17:17:47** by **mrfugu**:

@Meticulous Maynard, no A360 group yet, I thought that could be initiated via the dl link but i guess not, send your login and i'll invite you.

---

Posted on **2017-07-13 18:05:45** by **Meticulous Maynard**:

i believe that's maynardmetalmodel@gmail.com? That's what i use to sign in. Saw this short video about groups doing some quick research: https://www.youtube.com/watch?v=n4kgoJeT7Jo 

May be more than we need?

---

Posted on **2017-07-13 18:28:07** by **mrfugu**:

invite sent

---

