## CNC Base Plans
Posted on **2017-01-07 18:14:16** by **brianhurewitz**:

I backed as a beta, and I'd like to get a jump on building the base/CNC setup in prep for the arrival in Feb. Do you have shop drawings ready? Thx

---

Posted on **2017-01-08 04:37:33** by **rollandelliott**:

download the google sketch up drawing off the web site and you can use the measure tool to figgure it all out is what I've read.

---

Posted on **2017-01-08 18:46:03** by **Bar**:

rollandelliot is right, the CAD models to make the machine can be found here https://github.com/MaslowCNC/CAD. But I'm betting they aren't really the shop drawings you are looking for. If you take a look at them there isn't really a straight line in there and it would be a big hassle to build. It's like they were designed to be cut on a CNC router :-). The trick is that the machine builds itself. Basically you plug in the electronics, attach the motors to the corners of a 4x8 (or any size) sheet of plywood and attach the chains to your router and it cuts out the parts to make itself. You have to hold the router to provide the equivalent of the force of gravity, but other than that you don't have to do anything. We'll make a step by step instruction video.

If that's not really your cup of tea, or your really want to be ready to go 10 minutes after opening the box, feel free to take some liberties with the design and build one similar. The dimensions of the machine  are a software setting, so if you build something that's a different size than the plans it shouldn't be a big problem.

---

Posted on **2017-01-11 16:44:08** by **chadzimmerman**:

Working on a more "CAD drawing" version.  I am dimming out in Sketchup and will put it together in a PDF.  3D is nice, but I prefer my building plans more traditional.

But looking at the model more... I think I am going to redo some of the designs to make the base more stable and secure.  Also going to add in some cross supports (plywood around here seems to want to bow and warp on me).

---

Posted on **2017-01-19 13:22:36** by **brianhurewitz**:

Thanks everyone. This all makes clear sense.

---

Posted on **2017-01-20 04:09:27** by **davidlang**:

@chadzimmerman

please share your changes and why you think they make things better.

---

Posted on **2017-01-20 08:17:18** by **chadzimmerman**:

I will when I get done.  I have had an interesting last few weeks. Has put me behind on several trains of thought.  Also working on a sled design to make it more versatile.  (I want to also do laser engraving)

---

Posted on **2017-01-27 08:03:36** by **gero**:

Greetings from the always sunny Bahrain, also trying to have the base ready before the kit arrives. I've dumped my windoozel clients and servers a decade ago in favor of linux and on ubuntu 16 can't get sketchup to run (crossover, wine and playonlinux failed). I would be happy with a JPG or even a hand drawn sketch with dimensions for the base. Isn't the distance and angles of the arms crucial for the correct positioning of the router? Any help highly appreciated

---

Posted on **2017-01-27 09:12:46** by **chauhuh**:

I was going to do this for everyone. Bar made some design changes to the sled so I was going to hold off until he made a final commit to the git.

---

Posted on **2017-01-27 10:12:12** by **chadzimmerman**:

I am working on bigger changes for the sled.. I am taking the Z axis design from a CNC I was going to initially build and incorporating it into the Maslow sled.

https://1drv.ms/f/s!AncWsnmIIFfongtcF9JqwNHZd6Pf

I am forcing myself to work on this stuff today.

---

Posted on **2017-01-27 21:59:01** by **scottsm**:

@gero, if you like I can send you a .zipped 3D render in .dae file format that will give you a good idea. It's about 64k compressed.

@bar, I wonder if it would be worthwhile to put a rendering, or some jpg snaps from several angles, into the CAD folder for folks without Sketchup?

 Too, I wonder how much of this machine I need to have ready to mount the items that will be coming in the kit? Will the arms and sled be in the kit or should I be making those along with the easel? What are the critical measurements for the motor mounts?

---

Posted on **2017-01-29 18:35:35** by **mindeye**:

What version of Sketchup was used to create Machine.skp and Sled.skp?

I'm unable to load them in either Make 2015 (15.3.329) or 2017 (17.1.1730) and can't find a mac download for 2016. I'm mostly curious just to rough out the base platform to get a feel for placement in my shop.

---

Posted on **2017-01-29 21:45:03** by **scottsm**:

When opened, Make says the files were created with version 16.1.1449; I've been able to open them (.skp files) with 17.1.173 on a Mac. What is the error the Make throws?

---

Posted on **2017-01-30 08:09:15** by **mindeye**:

Something to the effect of "Not a Sketchup file". Unfortunately, won't be back at that machine until much later today. It must be an issue with something on my machine, whether that be the application or my copy of the file or the OS I don't currently know. Thanks for letting me know it's working for you under roughly the same conditions.

---

Posted on **2017-01-30 08:47:45** by **scottsm**:

For some reason the source has a .skb file (backup?) that Sketchup doesn't like. I renamed it and could open it, a close look at a motor mount.

---

Posted on **2017-01-30 09:37:29** by **Bar**:

Thanks for catching that the backup file could be an issue. I'll remove those from the repo and set it up to ignore .skb files in the future.

---

Posted on **2017-01-30 17:42:28** by **mindeye**:

Alright, in case anyone else runs into this, this is an issue where many download clients (chrome in my case) like to change line-end characters inside of the .skp file when directly downloaded which leads SketchUp to believe that the file is corrupted or otherwise not a valid file. You can avoid this by either cloning the repo via git or downloading a zip of the entire folder and then unzipping it into a folder on your local machine and opening the file from that folder.

---

Posted on **2017-02-01 13:19:42** by **jbarchuk**:

Mac availability and version.

First screencap, I downloaded literally yesterday and it offered a mac version.

[Sketchup-01-mac-download](//muut.com/u/maslowcnc/s1/:maslowcnc:WEcF:sketchup01macdownload.png.jpg) 

Second screencap shows the version inside the file. Well, that doesn't state what the current mac version might be, so maybe if not updated there's an incompatibility.

 [Sketchup-02-win-version](//muut.com/u/maslowcnc/s1/:maslowcnc:BdtQ:sketchup02winversion.png.jpg)

---

Posted on **2017-02-01 13:29:17** by **TheRiflesSpiral**:

Mac and PC versions of Sketchup have been synchronized. I think my 2017 update for my Mac was a day(?) behind the PC.

---

Posted on **2017-02-15 06:21:40** by **gero**:

3 Maslow Base Measurements please
My apologies if I come across as impatient. I only have a few hours on the weekends for this exiting project. I want to start this weekend to build the Maslow base.
Sketchup does not work for me as a start for construction (Linux). It shows me the volume of an object, so it must know the width, length and thickness, but refuses to reveal this data. I have tried dimensioning plugins with mixed to no results and the tape measure seems to give me random numbers. Exporting to .obj or .dae fails because of “non solid objects”. (Might all be Linux issues)
Since I have one object, the 8x4 plywood sheet, I think I known the dimensions (2440mm x 1220mm) I had a start on remodelling the base in Blender. (will share the mod on a different post)
I would like to stay as close as possible to the Mother-Maslow with:
a) Does it fit into the room I will designate for the Maslow? One Sektchup plugin gave me some “real world dimensions” as seen in the pic. Could someone kindly confirm that they are right?
b) The distance between the centre of the two motor  sprockets
c) The distance from the centre of the motor sprocket to upper side of the down beam
Thanks in advance and greetings from this temporary flooded Island. [Maslow-CNC-base-question](//muut.com/u/maslowcnc/s2/:maslowcnc:ukqf:maslowcncbasequestion.jpg.jpg)

---

Posted on **2017-02-15 07:07:26** by **TheRiflesSpiral**:

Gero,

The sketchup model does not have the motors in it so I can only measure the base for you. If we knew the distance from the motor base to the sprocket center, it would be simple to calculate total dims.

The total depth of the machine is 524mm (Back of the motor mount to the front of the ledge)
 [RCapture](//muut.com/u/maslowcnc/s1/:maslowcnc:OqDG:rcapture.jpg.jpg) 

The total width of the machine is 3,147mm (Far left extent of the "arms" to the far right extent)
 [GCapture](//muut.com/u/maslowcnc/s1/:maslowcnc:M8K7:gcapture.jpg.jpg) 

The total height of the machine is 2,007mm (Bottom of base to top of motor mount)
 [ISOCapture](//muut.com/u/maslowcnc/s1/:maslowcnc:IwO0:isocapture.jpg.jpg)

---

Posted on **2017-02-15 07:10:39** by **gero**:

@TheRiflesSpiral,
Thank you! It fits in the room! Nr 1 (a) is solved :-)

---

Posted on **2017-02-15 07:11:23** by **TheRiflesSpiral**:

Happy to help!

---

Posted on **2017-02-15 07:16:24** by **gero**:

A teaser for the Base-Mod ;-) [Teaser](//muut.com/u/maslowcnc/s3/:maslowcnc:EEbr:teaser.jpg.jpg)

---

Posted on **2017-02-15 08:06:41** by **scottsm**:

Your teaser has me interested... I'll be watching for developments!

---

Posted on **2017-02-15 09:02:29** by **davidlang**:

the current code defines the spacing of the motor centers to be 9.77 ft, The current chain supports add a couple of inches to each side (but could be tweaked) so 10.3 ft total width is reasonable

---

Posted on **2017-02-16 23:55:33** by **scottsm**:

What about a page in the Mechanical wiki with exports or rendered views of the machine and sled? Folks without Sketchup could view these images and contribute translated file formats.

---

