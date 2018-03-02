## Post options in Fusion360
Posted on **2017-03-11 06:17:55** by **rancher**:

I have been spending time this last week learning this software, my first of the type.  I'm almost through with my first try at a design from scratch to cam, and am wondering what I should choose as the NC output configuration for post processing for Maslow and Ground Control?  I output a file using "HAAS-generic", and it looks like g code, but I have no idea what I'm doing.  This is all new.  Any tips on any of this would be welcome.

---

Posted on **2017-03-12 05:34:13** by **TheRiflesSpiral**:

I think this may be relevant?

https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/Does-Fusion-360-Write-G-code.html

---

Posted on **2017-03-12 07:35:55** by **rancher**:

Thanks RS, that is the process I'm referring to.  Let me ask another way....If I output code for a shopbot will it work on Maslow?

---

Posted on **2017-03-12 07:53:25** by **TheRiflesSpiral**:

I think only Bar can answer that. My guess is no. From what I've read regarding G code, I don't believe it is a well controlled standard or maybe isn't even a "standard" the way I think of it... each machine has its own flavor with conventions for special features of a machine or a quirk here and there that only applies to a certain brand, etc.

It sounds to me like Fusion 360 doesn't have an option for exporting pure G code? (whatever that may be) I'm not a F360 user so I can't be of much help in that arena, I'm afraid. I tried it out a few weeks ago. I found the learning curve to be a bit steep for my available time commitment, whereas I picked up Sketchup in about 10 minutes.

---

Posted on **2017-03-12 07:57:44** by **rancher**:

Yeah, that's it RS.  They use a "post configuration" setting that you set from a drop down of many machines, but obviously Maslow isn't one of them.  I suspect most of them are the same, and I opened them in brackets and they have version notes that say things like "Z-axis is code..." and stuff like that, pertinent to each machine.  I suspect that most of them will work fine, but....yeah.  Once we know, we can write a configuration for Fusion360 and upload it and it should be available to all.  I think.

The learning curve is nasty.  I've spent the last three days learning it and not breaking things and screaming, but only just barely.

---

Posted on **2017-03-12 08:31:28** by **jbarchuk**:

Bar posted something one time, paraphrased, 'I've looked for and researched every g-code style and variation out there, and Maslow supports all of them.' That's the intent of the ground controller, to be versatile. There are variations like G-01, g-01, and g01. Maslow obviously can't support g-code that calls for a fourth axis motion command.

---

Posted on **2017-03-12 08:36:48** by **rancher**:

So which post option are you going to pick?

---

Posted on **2017-03-12 09:41:04** by **jbarchuk**:

Several answers... (I'm not far enough into the whole process to give an opinion. I'll learn whatever's necessary at the time, but am spending more time with other aspects of building, and software.)
The simplest answer is that it doesn't matter much in the sense that it will probably create g-code that the GC can accept, deal with, and cut out a shape. (I think I covered all my plausible deniabilities there. ;))
@Bar is the best person to answer because he has mentioned a few styles that produce horrid g-code in an efficiency sense. That's the purpose of the g-code generator, to be as efficient and accurate as possible.
I haven't been following the fusion360 forums in a while but I'm sure that's the best place to browse and search for g-code generation opinions, and others' experiences with fusion360 and other CAMs.
The next best answer is to at least for now skip the fusion360 CAM step and use makercam. Learn more about g-code using the recommended process and then later go back to see how fusion360 operates. Heck you might end up deciding to stick with makercam.
Anoth er good answer to that Q is if someone has experience with a CAM machine at the g-code level then go with that because it'll already be familiar.
-My- choice would be to go with the one with the most flexibility and widest feature set. As g-code generator software advances, those versions will probably 'win.'

---

Posted on **2017-03-12 18:35:05** by **rancher**:

So which post option are you going to pick?

---

Posted on **2017-03-12 18:35:10** by **spatialguy**:

Fusion 360 can export g-code, no worries, but I think you need to understand where and why g-code is used. 
Terms:
CNC - Computer Numeric Control (Computer controlled)
CAD - Computer Aided Drafting
CAM - Computer Aided Machining
Maslow router, laser cutter (printer), CNC mill etc...are all machines controlled by computers. 99% of the time it would be impossible to do what they do by hand. 
CAD software is used to create a part. You can use a .dxf file to share your part with others, just like you do with word documents .wor file.
CAM software is used to tell the machine that is about to make your part, where you want the machine to move, how fast it rotates, how fast it moves, what angle it is on, what tool it has in it and all the other parameters required in the manufacture of your part by that particular machine. Once the CAM software (and you) complete that, a G-Code file is normally produced and loaded into the machine for your part to be made.
In CAM software, the specifications for every machine you use must be loaded in. The Maslow CNC router is very different fr om my laser cutter and both will have a configuration file so that the gcode produced can be understood by that machine. you can write generic gcode to suit any machine but it will still have to be altered before use in that machine.
GCODE can be as simple as to plunge router to depth at the starting point then move across 10cm, up 10cm, back across 10cm and down 10cm and there you have just machined a square! A 9cm x 9cm square if you are using a 10mm diameter routing bit!
Some CAD software has CAM software built in like Fusion 360 does, or you must create your part in CAD then give your .dxf file to your CAM software so you can create your GCODE for that machine.

God I hope that helps, I am really not trying to confuse anyone...but not an author either.

Michael

---

Posted on **2017-03-12 18:36:17** by **rancher**:

So which post option are you going to pick?

---

Posted on **2017-03-12 20:20:56** by **spatialguy**:

Is that question for me rancher? I don't really understand what you mean if it is for me?

---

Posted on **2017-03-12 20:59:20** by **rancher**:

I'm new to all of this, but to make gcode with fusion360 you need to pick a post option in the drop down menu.  I picked "HAAS-Generic".  It made some gcode.  I am a total noob, so I guessed.  Another guess I might use,  I could pick "shopbot."  That is how you generate gcode in fusion360.  

So, when you get your Maslow, and you go to cut something, and you use fusion360 from start to gcode,....

...what post option do you choose from the drop down menu?

---

Posted on **2017-03-13 09:49:30** by **Bar**:

I'd like to say all of them will work. The "HAAS-Generic" is probably a good choice. Shopbot for some reason decided to not use the regular gcode standard and instead invented their own so the shopbot choices might not work as well. 

We're actually talking to the Fusion 360 team about putting in a Masow option. Their offices are conveniently in the next town over, so they came by to say hello.

If you find one that you like let us know, and if you find one that doesn't work right we'd love to know that too so we can make it work :-)

---

Posted on **2017-03-13 10:35:53** by **davidlang**:

to be fair to shopbot, g-code is cryptic and they were trying for a language that was understandable. But they saw the light and made them understand g-code as well so people are no longer locked into their software stack

---

Posted on **2017-03-13 15:15:18** by **rancher**:

Good stuff guys, thank you.

---

Posted on **2017-03-21 20:20:50** by **rancher**:

Hey guys, bumping this back up as I've been through a lot of trial and error trying to get a .nc file out of Fusion360 that Ground Control likes.  I'm totally guessing when I try the output formats, and I'm finding they vary enough that most don't work with GC.  

Has anyone had any success getting an .nc file out of Fusion360 into Ground Control?  If so, what post option did you choose?  So far, HAAS-generic has given me the best results, but I am still struggling.

---

Posted on **2017-03-21 20:38:12** by **Bar**:

Would you be willing to send me a HAAS-generic generated file? It might be easiest if I just make those work :)

---

Posted on **2017-03-21 20:57:31** by **rancher**:

I would, but....part of it is my inexperience, and I don't know when the problems are due to my original design or the output.  I have one that was output with HAAS that looks like it is all good in Ground control.  I got there by simplifying the design, and filleting and dogbone-ing all the hard corners.  The others get tripped up by details.  So...uh......do you want a good one, or a bad one?

---

Posted on **2017-03-21 21:03:25** by **rancher**:

Here's another idea, that could perhaps lead to a set of settings all could use.  In Fusion360 on the post options screen there are a list of the code parameters, and they are settable.  The dropdown is full of preconfigured options, but the settings can be tweaked manually.  Rather than fix my file, perhaps you could take a look at those options and let us know a set of settings that is likely to work?  Maybe?  I am not trying to give you more work!

---

Posted on **2017-03-21 23:02:52** by **aalbinger**:

you stated "Rather than fix my file", however, I don't think Bar was going to fix your file but rather he would make the standard HAAS-generic gcode work with the maslow firmware and then everyone using HAAS-generic would "just work" out of the box.

---

Posted on **2017-03-22 08:04:43** by **Bar**:

@aalbinger is right, I'd rather make Ground Control happy with the gcode produced by the HAAS-generic settings. It's usually something simple like recognizing 'g 1' as "G01" and if I can do it once then forever after it will just work for everyone. Maybe send me the good one and the bad one? That way I can look for the difference. I'm bar@maslowcnc.com

---

Posted on **2017-03-22 13:16:14** by **Bar**:

I think I've got it. That was a good bug :-). I think by fixing that one, a lot of other styles of gcode will be fixed too.

If you want to check out the issue I made it's [here](https://github.com/MaslowCNC/GroundControl/issues/118)

If you are running Ground Control from the source and grab the latest version it should all be working now, if you are using the compiled version I will post a new version tonight which will incorporate all the latest fixes. 

I'm not sure about the firmware side yet. I'm going to investigate the oval sleds everyone is getting first, then I'll try to run the gcode and see if it looks right.

---

Posted on **2017-03-22 13:33:44** by **rancher**:

Holy crap dude!  I'm so excited, if this means my files work.....oh my gosh.  Thank you!

---

Posted on **2017-03-22 13:34:32** by **rancher**:

I'm going to wait for the exe version of GC.  It's much smoother for me.

---

Posted on **2017-03-22 18:49:42** by **rancher**:

BAR!!  All my files, stuff I worked on the last few days and thought I totally screwed up....they all look fine in new GC.  I'm sooo stoked man, I had written off a lot of work I've done over the last few days, thinking I was messing up the design.  I can't wait to get it to the machine to test it.  Thank you!!

---

Posted on **2017-03-24 07:54:10** by **Bar**:

Thanks! And Thank you for bearing with us while we track all these things down. Everyone is going to have such a smoother setup process thanks to you contributions :)

---

