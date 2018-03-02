## Beta Assembly Attempt
Posted on **2017-03-19 18:13:45** by **flyingavatar**:

Attempted to do the assembly this evening and figured it might be helpful to report on my progress and give feedback on the guides:



Step 1: Electronics - No problems here.



Step 2: Programming the Arduino - No problems here, though I am wonder if I should be building from source as I expect as it is beta I might be making changes / tweaks.



Step 3: Installing Ground Control - Using the Mac DMG this was no problem, but I switched to source later on which I will detail.



Step 4: Building the Temporary Frame - This all went pretty well.  I ended up buying (3) 2x4x8' as they were cheaper and easier to transport than (2) 2x4x10's.  I think you already fixed the instructions, because on step 6, I swear I couldn't figure out which screws to use.  I ended up using the longer ones (even though the instructions now say to use the short ones) because they were a little too short to attach solidly.



In my mind, a drill and drilling pilot holes is a necessity.  I ended up drilling 1/16" pilot holes for the cup hooks as well since they were really hard to screw by hand into actual pl ywood.  In OSB, I think it would be easier.



A diagram of how to tie the strings would have helped a littler, but not too hard to figure out.



Step 5: Using the Temporary Frame to Cut Parts - This is where I am stuck for now.  I got Ground Control talking to the Arduino.  I was not able to get the Calibrate Chain Lengths to work.  The motors did not move and there was no indication anything was happening.  At one point one of the motors did move.



I ended up using Ground Control from trunk after I saw a post from Bar about adding a Test Motors function.  When I tried that I saw this output in the console:



---

Connected on port /dev/tty.usbmodem1421



Sending: B03 A2438.4 C1219.2 D270 E463 F310 G139 H79



Sending: G21



Sending: B04



bad data

bad data

bad data

bad data

bad data

bad data

bad data

bad data

---



I will try to debug the motors later on as I had to leave the shop.  Brought the motors and controllers home to try and debug further.

---

Posted on **2017-03-19 18:46:59** by **Bar**:

The line "bad data" means that Ground Control is unable to understand the characters being sent by the controller board. If you open the serial monitor in the Arduino program what do you see? You can open the serial monitor by clicking the circle thing (magnifying glass?) in the upper right corner of the Arduino program. You will need to change the speed to 19200 or all the characters will look garbled which is done from the drop down in the bottom right like so:  [Serial monitor](/images/aw/awde_serialmonitor.jpg.jpg)

---

Posted on **2017-03-19 18:49:56** by **flyingavatar**:

Yeah, so if I close Ground Control and switch to Arudino, it repeats this over and over:



ready

pz(nan, nan, -0.80, 0.00)mm

pz(nan, nan, -0.80, 0.00)mm

pz(nan, nan, -0.80, 0.00)mm

pz(nan, nan, -0.80, 0.00)mm

---

Posted on **2017-03-19 18:50:21** by **flyingavatar**:

To clarify, it doesn't repeat the "ready", just the pz...

---

Posted on **2017-03-19 18:52:27** by **Bar**:

Does the "bad data" repeat over and over too?

---

Posted on **2017-03-19 18:53:28** by **flyingavatar**:

So, I am unable to get GroundControl to report anything useful now.  It seems to be trying to send commands, but I can't tell if it's seeing anything back.

---

Posted on **2017-03-19 18:57:15** by **flyingavatar**:

Now, I am getting some weird stuff.  Killed GroundControl and reset the Arduino and started over.  Now I am seeing a few "bad data" interspersed with data on the console that looks garbled.

---

Posted on **2017-03-19 18:57:31** by **flyingavatar**:

[Screen Shot 2017-03-19 at 9](/images/zp/zpow_screenshot20170319at9.56.00pm.png.jpg)

---

Posted on **2017-03-19 18:58:26** by **Bar**:

That looks like some genuinely bad data

---

Posted on **2017-03-19 18:58:55** by **Bar**:

Are you using the USB extender cable? It might be worth trying with just the short cable

---

Posted on **2017-03-19 18:59:43** by **flyingavatar**:

It looks like the serial port is breaking up the data strangely.  The characters are correct, just they're not completely messages.

I wonder if it's a difference of using pyserial on a Mac?

---

Posted on **2017-03-19 19:00:37** by **flyingavatar**:

Haven't looked at the code, so I am spitballing.  Though if it's being separated by carriage returns, which it seems it was in the Arduino console, I can't see what the problem would be.

---

Posted on **2017-03-19 19:01:02** by **Bar**:

I think that pyserial is a good guess. I know we had some weirdness on Hannah's Mac at first, but I got it to settle down by changing some of the timeouts settings

---

Posted on **2017-03-19 19:02:32** by **Bar**:

She had an interesting problem which was that if I used my power drill near the cable it would drop the serial connection. Other big electronics (the router, dust collector...etc) weren't an issue so I blamed the drill but that's why I suggested the shorter cable

---

Posted on **2017-03-19 19:04:48** by **flyingavatar**:

Yeah, if I switch back to serial monitor in the Arduino IDE, it all looks fine.  I'll see if I can play around with the serial code.  



Strange about the cable.  The first thing I tried was removing the USB extension to see if that was the problem.  



I've tested it in the Arduino console now with and without the extension, and the data seems perfectly fine, so I am suspecting something weird with Ground Control.

---

Posted on **2017-03-19 19:06:59** by **Bar**:

I think that's a good guess too. If you feel comfortable messing with the code directly, the file to start in is connection/serialPortThread.py . That's where all of the serial port is handled

---

Posted on **2017-03-19 19:08:14** by **flyingavatar**:

Haha, this inspires confidence in pyserial:



---

            self.serialInstance.parity = serial.PARITY_ODD #This is something you have to do to get the connection to open properly. I have no idea why.

            self.serialInstance.close()

            self.serialInstance.open()

            self.serialInstance.close()

            self.serialInstance.parity = serial.PARITY_NONE

            self.serialInstance.open()

---

Posted on **2017-03-19 19:11:58** by **Bar**:

Yeah, pyserial is pretty touchy when it comes to configuration things. It seems like once it's happy it says happy, but it's not all that clear on why the things it likes are the things it likes.



You can also send commands to the board from the Arduino software if you just want to see it move. The  [Line ending](/images/kc/kc9f_lineending.jpg.jpg) setting is important. "B04 " might be a good place to start, it will test the motors

---

Posted on **2017-03-19 19:12:57** by **Bar**:

I'm sitting in the parking lot right now so I'm going to drive home, but I'll be back online as soon as I get to my house :-)

---

Posted on **2017-03-19 19:24:36** by **scottsm**:

@ flyingavatar, what is the serial window open behind the groundcontrol window? Is there more than one process on that serial port? Is groundcontrol running from the Release version of the .dmg?

---

Posted on **2017-03-19 19:43:03** by **Bar**:

@scottsm I believe that is the terminal side of Ground Control and I think you have a really good point about the possibility of multiple processes accessing the serial port. 



When I went to look at what was in the background I noticed something that I think may be relevant. 



It seems that the  [Connection was lost](/images/3w/3w8l_connectionwaslost.jpg.jpg) and then Ground Control reconnected automatically. I know we had some issues a while ago with multiple threads accessing the serial port simultaneously which gave exactly the kind of weird garbled junk you are seeing. @scottsm might be able to give you more guidance than I can there because he's on Mac and actually found the issue initially

---

Posted on **2017-03-19 20:01:39** by **flyingavatar**:

@scottsm, it's my understanding in OSX if you are using a /dev/tty* device, it can only be used by a single process at a time.  I am only able to use the Arduino console or Ground Control on the port, otherwise the port is not available.  The console I am referring to when using Ground Control is the terminal output running from trunk.  The release version I have had no success with.

---

Posted on **2017-03-19 20:08:21** by **flyingavatar**:

By "trunk" I mean the master branch from GitHub.



So it seems the problem might be Kivy related.  I added a debug print whenever a serial message was received.  When Ground Control starts up, I can see the pz messages printing in the console.



The second I press "Actions" to get to the Test Button, I see this:



---

input: pz(nan, nan, -0.80, 0.00)mm



input: pz(nan, nan, -0.80, 0.00)mm



input: pz(nan, nan, -0.80, 0.00)mm



Initialized: <Screen name=''>

[WARNING] <UIElements.viewMenu.ViewMenu object at 0x1195b7b40> have no cols or rows set, layout is not triggered.

[WARNING] <UIElements.viewMenu.ViewMenu object at 0x1195b7b40> have no cols or rows set, layout is not triggered.

[WARNING] <UIElements.viewMenu.ViewMenu object at 0x1195b7b40> have no cols or rows set, layout is not triggered.

[WARNING] <UIElements.viewMenu.ViewMenu object at 0x1195b7b40> have no cols or rows set, layout is not triggered.

[WARNING] <UIElements.viewMenu.ViewMenu object at 0x1195b7b40> have no cols or rows set, layout is not triggered.

---

 

I had been ignoring those WARNING messages before, but I wonder if something is happening.  Once those are printed, all serial input is no longer printed.

---

Posted on **2017-03-19 20:11:12** by **Bar**:

very interesting. I have been ignoring those warnings also (never a good idea). Good tracking down of the issue.

---

Posted on **2017-03-19 20:15:50** by **scottsm**:

agree about the single process. I too see the WARNING messages when I run from the terminal, have ignored that.

What is the symptom when running the packaged app?

---

Posted on **2017-03-19 20:16:57** by **flyingavatar**:

Packaged app, literally I cannot see anything happening, so I have no means of determining if anything works or not.

---

Posted on **2017-03-19 20:19:32** by **flyingavatar**:

So interestingly, if I unplug the Mega after the error, this happens:



---

Sending: B04



write issue

connection lost

---



The "Sending" bit doesn't occur until I unplug.



When I plug back in, it resumes being happy:



---

Connected on port /dev/tty.usbmodem1421



input:

input:

input:

input: ready



input: gready



Sending: G21 



input: G21



input: gready

---

---

Posted on **2017-03-19 20:26:01** by **Bar**:

So I started digging into what was causing the warning and fixed it so if you grab master you won't see the warning, but I have a hunch that the problem won't go away. I think the issue is related to line 15 in otherFeatures.py which is the name for the "Actions" window (it used to be called "Other Features") . Line 15 is:

---

self.connectmenu.updatePorts()

---

which triggers a refresh of the list of available COM ports. How that is breaking the serial connection I'm not sure, but it does touch the serial port list AND happen when you click the *Actions* button which seems like a big coincidence

---

Posted on **2017-03-19 20:26:51** by **Bar**:

If you comment that line out you should still connect automatically

---

Posted on **2017-03-19 20:30:34** by **flyingavatar**:

Ok, that fixed serial going away.

---

Posted on **2017-03-19 20:36:59** by **flyingavatar**:

Ok, I have both motors running.

---

Posted on **2017-03-19 20:37:16** by **Bar**:

Wooo! 



Well that's good! We've still got to figure out why it's breaking your connection because if we take it out of master then nobody else will be able to connect :-)

---

Posted on **2017-03-19 20:40:10** by **flyingavatar**:

You're saying it's an OS X thing?  Why does it work for me?

---

Posted on **2017-03-19 20:40:54** by **flyingavatar**:

Also, what exactly is Test Motors supposed to do?  Do I need to flash a new firmware to make it work as well?

---

Posted on **2017-03-19 20:43:56** by **flyingavatar**:

Doing calibrate motors gets them both going but "Test" just echos the command back.

---

Posted on **2017-03-19 21:10:57** by **Bar**:

I would maybe grab the latest firmware, that was a feature I added pretty late in the day.



Test motors should rotate both motors each direction and use the encoder readings to confirm that they move.

---

Posted on **2017-03-20 04:10:13** by **flyingavatar**:

So it looks like my issues were indeed caused by having multiple apps trying to access the serial port.  I started to have the same problem this morning until I closed the Arduino IDE.



Regarding the firmware, I installed latest as of 7am EST and Test Motors still does nothing.  Looking at the Firmware repo, it seems like the last commit to master was a few days ago, maybe I should be using another branch?

---

Posted on **2017-03-20 07:43:02** by **Bar**:

That is strange, but good to know. Does that mean the you can open the 'Actions' menu without issue as long as the Arduino program isn't also open? I guess that's good news, but I'd like to make it more stable. I had some ideas about more things to investigate as I was going to sleep so I'm going to keep looking into it.



You can get the latest firmware here: https://github.com/MaslowCNC/Firmware where the latest version should be about 16hrs old. I'm guessing you are looking at the releases page which is the smart thing to do, but for now things are changing so fast right now that it makes more sense not to wait for a release. There are instructions here: https://github.com/MaslowCNC/Firmware/wiki/Firmware-Setup for how to grab the very latest. :-)

---

Posted on **2017-03-20 13:47:09** by **scottsm**:

I see the issue with 'self.connectmenu.updatePorts()' breaking the serial connection on OS X, and I've opened an issue on it:

[Actions tab breaks serial connection #114](https://github.com/MaslowCNC/GroundControl/issues/114)

I think I've got a fix for it, described in the issue. I'll put together a PR, but wonder whether it should be against the build-OSX or master?

---

Posted on **2017-03-20 13:58:12** by **Bar**:

Fantastic! I'd make a pull request against master just to keep all the code in master. 



Great work!

---

Posted on **2017-03-20 19:00:34** by **blsteinhauer88**:

Bar I was going to add a jumper to use the broken cable. When I pulled on the offending orange wire a little, it came out!! You can see it was actually severed in the braided protector about 9-10 inches from the other end.  [IMG_0446](/images/re/relx_img_0446.jpg.jpg)

---

Posted on **2017-03-20 19:00:49** by **blsteinhauer88**:

I'm going to splice back together so I can get testing again.

---

Posted on **2017-03-20 19:03:27** by **blsteinhauer88**:

[Image](/images/sd/sdk9_image.jpg.jpg) this is pulled straight out of the loom.

---

Posted on **2017-03-20 19:13:28** by **blsteinhauer88**:

Posted in the wrong spot, supposed to be in one motor not working. Sorry

---

Posted on **2017-03-20 20:54:39** by **Bar**:

That looks like it took a beating. I feel better that the wire was cut in the middle than if it were a bad crimp in one of the connectors. I wonder how that happened. The crate they came in looked like it was in good shape so hopefully you got the one that got run over by a forklift in the factory or something. The new ones are in route so if the splice doesn't hold up, you should have a new one by tomorrow, or Wednesday at the latest!

---

Posted on **2017-03-21 15:51:41** by **jbarchuk**:

> @flyingavatar

> In my mind, a drill and drilling pilot holes is a necessity.

I added a note to the wiki to word that a little more strongly. I know the house framing carpenter type people zip in those self drilling screws as fast as they can pick up the next screw, but they -have- to do it super fast. We have a little more leisure. Heck, whenever possible I do the pilot on the drill press to make sure the pilot is square, but most people don't have that luxury.

Walmart has a Yankee style push drill for $12.

---

Posted on **2017-03-21 16:03:48** by **flyingavatar**:

Yeah, the cup hooks would have been a particular challenge without pre-drilling.  I'm sure I could do the drywall screws without it, but for the extra couple minutes of pre-drilling, the reduced risk of messing up and improved accuracy seems worth it.  :)

---

Posted on **2017-03-22 10:57:39** by **blsteinhauer88**:

Thanks Bar for the new wire.  I cut my sled out yesterday and mine also came out oval.  But it was sure fun to cut out. I downloaded the SVG files from github but maker cam would not open them.  Is there a way to package those up in a zip file available somewhere for download? Or does it already exist and I missed it? Thanks!  [IMG_0459](/images/hq/hq0b_img_0459.jpg.jpg) [IMG_0461](/images/4b/4b9z_img_0461.jpg.jpg)

---

Posted on **2017-03-22 11:32:56** by **Bar**:

:-)



That's really really oval. I may have messed something up in the changing the machine dimensions part of the math. I'll look into it.



Having a zip file of all the parts is a great idea. There wasn't one, but there is now :) It's [here](https://github.com/MaslowCNC/Mechanics/blob/master/AllPartsSVG.zip)

---

Posted on **2017-03-22 13:25:55** by **jbarchuk**:

> @flyingavatar

> Yeah, the cup hooks would have been a particular challenge without pre-drilling.

Holding the hook and trying to drive it in can even be painful on the fingers. I've never tried it but I'd guess it's possible to hold the hook with a plier and drive it in. For something that small there are other ways to make a pilot hole. Tap in a tiny brad and pull it out with a plier. Heck even an ice pick could make a small shallow hole in the wood.

Tiny holes are where I immediately go for the Yankee drill. No heavy drill, no power cord or disappointment at finding a discharged battery, no chuck key. Pop in a bit, push-push-push, done. This pic is one of the first 'more than a screwdriver' tools my Dad let me use. That was more than 50 years ago and it still has all the original bits. A little worn :) but still works great. All anyone makes now is plastic. Yuck. [Yankee-push-drill-01](/images/eq/eq5r_yankeepushdrill01.png.jpg) 

> ... the reduced risk of messing up ...

The WORST risk is splitting a marginal piece of wood and having to start over! :(

---

Posted on **2017-03-22 13:39:28** by **scottsm**:

I used one of the long wood screws to make my cup hook pilot holes. About 1/4" in made a good enough to get a good start with the hook, and using the shaft of the screwdriver as a bar in the hook for leverage saves the fingers

---

Posted on **2017-03-22 14:08:12** by **jbarchuk**:

> @scottsm

> ...using the shaft of the screwdriver as a bar in the hook for leverage saves the fingers

Clever. Work with whatcha got. :)

---

