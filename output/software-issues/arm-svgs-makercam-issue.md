## Arm SVGs -> MakerCAM issue
Posted on **2017-03-25 19:06:31** by **chadheiser**:

So we've got the temporary Maslow built and have cut the full sled (from provided Gcode) and the brick holders (from svg->MakerCam). All of that is correctly sized and assembled, I have also run MakerCAM on Arm_Front and Arm_Back with the same settings as the brick holder. 



When we attempt to cut Arm_Front the sled moves way too far (headed up/right from origin, we haven't rotated the svg) so we hit stop on ground control which does stop the sled. However, and here's the part I don't understand, the sled is now dangerously high so I jog it down 1 inch (to test) and it continues to move showing no signs of stopping. We stop the process after 16+ inches of travel. Ground control shows the cutter moving 16+ inches, and the sled moves 16+ inches but any value we put into Ground Control is ignored (or multiplied). We have to close GC and restart to be able to jog properly again.



I'm not 100% sure that this isn't an issue created by our importing the SVG into MakerCAM , but we followed the same steps as the brick holder which still cuts perfectly. Has anyone else cut the arms? What would cause GC to move 16+ inches when we call for 1 (it usually is nearly perfect with jog commands)

---

Posted on **2017-03-25 20:13:40** by **Bar**:

Hmmm, that's not the behavior we want

---

Posted on **2017-03-25 20:16:11** by **Bar**:

It might have something to do with the way the gcode is generated, but the machine still shouldn't behave strangely when you jog it like that.



Does the part to cut show up inside the 4x8 sheet on Ground Control?



If you open a different file, maybe the sled file you know works do things behave as expected?

---

Posted on **2017-03-25 20:20:55** by **Bar**:

...I guess you said the brick holder still cuts perfectly so that answers my question

---

Posted on **2017-03-25 20:21:01** by **chadheiser**:

The part does fit within the 4x8 sheet, but it might be a bit larger than actual size (I'm not sure of the actual dimensions of the arm.)



If I open either the sled (that was pregenerated) or the brick holder (that I generated) the machine behaves perfectly, cuts as expected and can be jogged in accurate dimensions. I've even tried stopping the cut like I did with the arm and jogging and it still behaves normally.



I've generated Gcode with both the svg in Github and the svg in the zip in github.

---

Posted on **2017-03-25 20:22:06** by **chadheiser**:

I am moving the origin point on both the brick holder (straight down) and the arm (down and to the left) I don't know if that somehow causes the issue.

---

Posted on **2017-03-25 20:24:06** by **Bar**:

What you are doing sounds like the right thing. 



Excellent job finding something I can fix! If it happens every time with the same file, would you be willing to make an issue and attach the file (you can just drag and drop it on the text box), that way I can give it a go and see if I can make it do the same thing.

---

Posted on **2017-03-25 20:25:14** by **chadheiser**:

Sure. I plan to work on this tomorrow myself. I write Python/web apps for a living so I'll take a look at the source while I'm at it, but I will file an issue report (unless I figure it out)

---

Posted on **2017-03-25 20:26:11** by **Bar**:

Thanks! If you can beat me to it, that's great :-)



I'm at home, but I will run it first thing in the morning and see what's going on. I can take a look at the file right now.

---

Posted on **2017-03-25 20:27:19** by **chadheiser**:

Alright, I'll file an issue in Github now with the file then. Should I also include my brickholder.nc?

---

Posted on **2017-03-25 20:27:51** by **Bar**:

It can't hurt!

---

Posted on **2017-03-25 20:28:19** by **chadheiser**:

Sounds good. Thanks! You've really put a ton of thought into the Maslow and so far it has been awesome!

---

Posted on **2017-03-25 20:29:14** by **Bar**:

Thanks! We do our best. You guys are the real champs tho. Thank you for bearing with us while we get everything dialed in.

---

Posted on **2017-03-25 20:30:53** by **Bar**:

If you are going to jump into tracking down the issue, the first thing I would look at is what is the first line of gcode sent to the machine when it goes rogue. It will probably be something like 

---

G01 X10.0 Y25.0

---

Which just basically says go to the XY coordinates (10.0,25.0).



If it's being sent to rogue coordinates then the problem is on the Ground Control side and the machine is just doing what it's told. If the coordinates look right then its a firmware issue.

---

Posted on **2017-03-25 20:32:02** by **chadheiser**:

G0 X22.0273 Y27.8897

---

Posted on **2017-03-25 20:32:48** by **Bar**:

That looks like it's being sent up and to the right so it's probably on the Ground Control side

---

Posted on **2017-03-25 20:34:59** by **chadheiser**:

Yeah it moves up/right like I would expect, but it seems like it's not going to stop. I'd almost swear it's a ramping issue, where as it gets moving it starts increasing speed (and so is travelling farther than expected) but I could be wrong. I'm usually the one manning the computer and I can't see clearly what the sled is doing other than it's on it's way to crash at the top the board when it should be a good foot and a half from there.

---

Posted on **2017-03-25 20:36:37** by **rancher**:

Chad, have you set the dimensions in the settings area?

---

Posted on **2017-03-25 20:38:10** by **Bar**:

Rancher, are you asking because of the auto stopping when it hits the edges of the area?

---

Posted on **2017-03-25 20:40:18** by **rancher**:

No, I haven't given a full report on all my testing this week, but the "drifting" you guys were discussing earlier, going up always, and this behavior, are all stuff I experienced.  I actually pulled a cotter pin through the bracket but didn't want to scare you!  It was after you made the dimensions settable.  Remember how I commented on how it took me a while to figure out that changed?  I took that photo you posted and took it to the shop and got back to close, and it stopped trying to climb off the sheet.

---

Posted on **2017-03-25 20:40:21** by **chadheiser**:

I have set the dimensions in the settings area. I have measured each as described in the software and other files are cutting correctly.

---

Posted on **2017-03-25 20:41:21** by **Bar**:

You pulled a cotter pin THROUGH the bracket! Wow!

---

Posted on **2017-03-25 20:42:06** by **chadheiser**:

We originally had issues with the screenshotted settings from the instructions (for the temp build), but after measuring everything we have gotten good results. Except for this (and we haven't tried anything else after, it was getting late)

---

Posted on **2017-03-25 20:42:56** by **chadheiser**:

Yeah, we had the motors attempt to rip our MDF temp sled apart, but managed to stop it with just some cracking and separation. Once we set the measurements everything has been great, and now we have the full sled.

---

Posted on **2017-03-25 20:43:37** by **chadheiser**:

https://github.com/MaslowCNC/GroundControl/issues/134 (for future reference)

---

Posted on **2017-03-25 20:44:07** by **Bar**:

Beautiful, thank you!

---

Posted on **2017-03-25 20:44:48** by **chadheiser**:

Not a problem. I'm fully willing to admit the file may be wrong due to something I did/didn't do, but the jogging issue was still puzzling.

---

Posted on **2017-03-25 20:46:21** by **rancher**:

What I observed is that jogging issue seems to manifest when it appeared position had been lost.  Sometimes that was due to those stops I was experiencing.  I believe that the circle that displays how far off position it is is so big when that happens that we don't see it due to scale.  Somehow it gets really, really lost.  Sometimes it would drift towards the bottom, sometimes towards the top.

---

Posted on **2017-03-25 20:48:07** by **Bar**:

I think you are spot on that the error circle is so big you can't see it. I've had that happen a few times too, but I never saw it as related to the open gcode file.

---

Posted on **2017-03-25 20:48:37** by **chadheiser**:

That would make sense. I can see the head move in GC after I specify 1 inch and it just keeps going (so GC thinks the distance is still within 1 inch)

---

Posted on **2017-03-25 20:48:58** by **rancher**:

It wants to find out where it is before it responds, it appears.

---

Posted on **2017-03-25 20:49:05** by **chadheiser**:

I can run the file tomorrow, stop it per usual and then zoom out to see the circle

---

Posted on **2017-03-25 20:51:14** by **Bar**:

It might be infinity large

---

Posted on **2017-03-25 20:51:31** by **chadheiser**:

Ah yeah...

---

Posted on **2017-03-25 20:51:38** by **rancher**:

I think it is, I think I tried that.

---

Posted on **2017-03-25 20:52:08** by **rancher**:

The question is why it's getting lost, and Bar, I'm sorta inclined to think it's related to that J thing, or something like it.

---

Posted on **2017-03-25 20:54:01** by **Bar**:

That's a really interesting idea

---

Posted on **2017-03-25 20:54:32** by **chadheiser**:

Hmm first instance of a J command is 165 lines in, we're stopping it before it gets to line 11

---

Posted on **2017-03-25 20:54:52** by **chadheiser**:

But it could be related

---

Posted on **2017-03-26 07:58:30** by **rancher**:

Forget the J specifically.  My observations lead me to believe that part of the positioning problem is related to code handling.  I have been referring to those "stops" in my cuts.  When that happens, if I don't Pause/Run right away, the time that passes is time the machine is losing it's place.  The longer it is, the more lost it is.



Bar, I believe this is perhaps related to code output and code handling.  I believe that if you have not yet, you should download Fusion360 and look at those post options.   There is both a large list of presets, then 20 or so settable fields in each.  I played with lots of settings, "space after G", "Allow feedrate", etc. and they all manifest dramatically differently in GC, even if I'm still on HAAS-Generic.



To my mind, the best way forward that ensures we all learn how to generate codes that comply, is to clearly define what G-code parameters we are going to use.  The code is so simple that after a few days now I understand that I can go in there and spot problems, so......yeah.



I might be totally off base on all of this.  I'm brand n ew to every aspect, so I expect to be wrong.  However, hopefully there is some value in what I have experienced this past week.

---

Posted on **2017-03-26 08:24:44** by **Bar**:

I think what you are experiencing makes sense. My computer doesn't meet the minimum system requirements to run Fusion 360, but I bet I can find a computer in the building that does. Ideally I would like to make my gcode interpreter more robust so that rather than specifying exactly which post options will work, they will all work. There are literally thousands of programs which generate gcode, so if I can make the firmware handle them generally I think it will save people more time. Would you be willing to generate gcode for a simple shape I can test like a circle, and I will make that gcode work?

---

Posted on **2017-03-26 08:25:32** by **davidlang**:

bar can't test every g-code generator out there, that's what beta testers are for :-)



sending him sample g-code that doesn't work is the best thing to do.

---

Posted on **2017-03-26 08:42:13** by **rancher**:

You misunderstand David.  I don't want him to test the generator.  I want to know what to generate.  His files won't cut anymore either.  Fusion360 just happens to give us a lot of control over it, so we can talk about it.  Makercam.....you get what you get.

---

Posted on **2017-03-26 08:43:42** by **rancher**:

> @Bar

> Would you be willing to generate gcode for a simple shape I can test like a circle, and I will make that gcode work?



Circles cut fine.  Bar, your example files exhibit the same behavior.  



Why do I feel like I'm the only one running the machine?  Am I the only one who can't run those example files?  We need a test file.

---

Posted on **2017-03-26 08:57:34** by **Bar**:

That's a really good point. I misunderstood also.



The more boring the gcode, the better so we're looking for something like:

---

G01 X10 Y21.5 F123

---



I think the thing that Fusion 360 is doing that is probably causing the most issues is that it's putting section numbers in front of the lines like 



---

N25 G01 X10 Y21.5 F123

---

---

Posted on **2017-03-26 08:58:18** by **Bar**:

Another problem is that fusion 360 might be using some of the more exotic commands like G18 which switches from the XY plane to the YZ plane of motion

---

Posted on **2017-03-26 09:00:54** by **Bar**:

It seems very strange to me that my files won't cut anymore either. There are some gcodes which set things which can persist between files like G20, G21 which will switch from metric to imperial units or G90/G91 which switch the coordinate system to be relative or absolute

---

Posted on **2017-03-26 09:02:25** by **davidlang**:

There isn't really a 'standard' g-code that software creates, there are a lot of dialects. The more that the maslow can understand the better.



there needs to be clearer error messages when it hits something it doesn't understand.



It would also be handy to make a stand-alone program that uses the maslow g-code interpreter code to go through a file and report if it hits anything it doesn't understand.

---

Posted on **2017-03-26 09:03:38** by **rancher**:

Bar, the reason I want you to look in Fusion is because it has a super long, comprehensive list of all of the output options.  You can open them in brackets and they have notes outlining all the functions and commands.  The variety is dazzling.  The idea that all are going to work is nuts.  That's why you need to go look, pick a direction, and work within those parameters.



I originally chose two, randomly, from the list, remember?  Shopbot and HAAS,  one was a no go, and one is close.  Format matters.  A lot.  



Let's define our format, please.

---

Posted on **2017-03-26 09:04:16** by **Bar**:

I agree

---

Posted on **2017-03-26 09:05:40** by **Bar**:

I will track down a copy of Fusion 360 today and look at what kinds of options are available. I've also been in touch with the Fusion 360 people about adding a "Maslow" option which would reduce the confusion considerably.

---

Posted on **2017-03-26 09:06:29** by **Bar**:

I'll need to tell them which settings to use for the Maslow option so I need to find the right ones anyway

---

Posted on **2017-03-26 09:06:43** by **rancher**:

Phew!  Exactly.

---

Posted on **2017-03-26 09:11:46** by **davidlang**:

but we also need to be able to use things other than fusion 360, so adding a maslow option there doesn't solve the root problem.



Maslow doesn't need to be able to handle every type of g-code out there, but it does need to be able to handle "enough" of the common g-code generators out there.



have you looked at what other g-code interpreters are out there with opensource licenses? Linuxcnc has a pretty robust one, there are a bunch of them out there for arduinos that are used in 3d printing, etc.

---

Posted on **2017-03-26 09:19:31** by **Bar**:

We do need to support more types of gcode in general. 



I haven't played around with too many of them, but I think if we make a general rule that if you find a file that won't work and make an issue for it I'll make it work we'll catch most of them pretty quickly, or at least the ones that people are using

---

Posted on **2017-03-26 09:22:56** by **rancher**:

Here's the download page for the Fusion trial.



http://www.autodesk.com/products/fusion-360/free-trial

---

Posted on **2017-03-26 09:25:42** by **davidlang**:

@bar, I think that's exactly the way to do it. Initially identify a program that works (just to give people something to use) and then consider any g-code from any source that doesn't work a bug, and work to fix it.



As programs are tested and work, they get added to the "known good" list (recognizing that the next release of those programs may break something)

---

Posted on **2017-03-26 11:17:41** by **Bar**:

I wanted to keep you guys updated, I've got Fusion 360 running, and from looking at the built in post-processors the GRBL-generic one looks pretty good, but it wants to use the G17 and G18 commands a lot to switch the plane from XY to XZ which isn't something we support yet...still investigating

---

Posted on **2017-03-26 11:27:09** by **Bar**:

The latest firmware will ignore G18 commands and give you an error message. Digging into the code behind the post-processor is a little overwhelming so I've reached out to the guy we know at Fusion to see if they can give me a bit of guidance. It being Sunday, I don't really expect to hear back until Monday.

---

Posted on **2017-03-26 11:46:58** by **rancher**:

Thank you so much Bar.

---

Posted on **2017-03-26 11:51:17** by **Bar**:

Thank YOU

---

Posted on **2017-03-26 11:51:53** by **chadheiser**:

Well, we were just able to cut the part we had trouble with by turning the SVG on it's side in MakerCAM and generating from there, so that might lead to Gcode interpretation issues as you guys are thinking. I'll drop the working .nc in the Github issue page.



On another note, can anyone confirm the size of the Arm_Front piece? We printed a pdf poster of the SVG and then cut the new gcode and ended up with two different sizes. I've attached some photos of the differences. The physical piece is not quite square, but that could be an artifact from how we spun the svg or the same reason we get slightly oval cuts. Anyways, still testing. Thanks. [20170326_141853](//muut.com/u/maslowcnc/s3/:maslowcnc:lcBq:20170326_141853.jpg.jpg) [20170326_141808](//muut.com/u/maslowcnc/s1/:maslowcnc:ZykH:20170326_141808.jpg.jpg)  [20170326_141905](//muut.com/u/maslowcnc/s3/:maslowcnc:UmLb:20170326_141905.jpg.jpg)

---

Posted on **2017-03-26 11:54:46** by **Bar**:

Gorgeous! I'll check the measurements right now

---

Posted on **2017-03-26 11:58:44** by **Bar**:

The sketchup model says the correct distance for that opening is  [120mm](//muut.com/u/maslowcnc/s1/:maslowcnc:stNf:120mm.jpg.jpg) which is about 4.7inches so I would say the wood one is correct

---

Posted on **2017-03-26 11:59:21** by **chadheiser**:

Well that's great news then! Thanks for checking that.

---

Posted on **2017-03-26 11:59:37** by **Bar**:

It is! :-)



I'm investigating the weird behavior you were seeing with the original model right now

---

Posted on **2017-03-26 12:08:53** by **chadheiser**:

The actual measurement of that opening is between .5 and .25 mm on the small side, so I'd say that's a pretty good result! [20170326_150203](//muut.com/u/maslowcnc/s3/:maslowcnc:5Qui:20170326_150203.jpg.jpg) [20170326_150218](//muut.com/u/maslowcnc/s3/:maslowcnc:EOXP:20170326_150218.jpg.jpg) Also I set the hole for the U-bolt to cut on the outside and it looks to be a bit large, most likely should have cut inside on that. The edges are pretty uniform as well, there isn't really any difference between the cuts through the layers (we had some issues earlier when we had the temporary sled.)

---

Posted on **2017-03-26 12:13:01** by **Bar**:

Looks like we're getting there!



That hole for the U-bolt looks a little wonky and oval. I would recommend cutting on the inside for sure, but it should still be rounder than that. Was it acting strange for that part at all?

---

Posted on **2017-03-26 12:15:55** by **chadheiser**:

Not that I noticed, it seemed to act fine. I did cut it as a separate profile operation. We are still getting slightly oval shapes, do you think measuring everything more accurately (we measured in inches and then  converted to MM) would correct that? We are much closer to true now than when we started, and the measurements in that screenshot in the instructions for some reason were WAY off for us.

---

Posted on **2017-03-26 12:18:50** by **Bar**:

I really need to update that screen shot

---

Posted on **2017-03-26 12:20:17** by **Bar**:

Those dimensions don't seem to be right for anyone else. I added some text to indicate that they shouldn't be used this morning. I'm changing the way the dimensions are calculated probably tomorrow tho so I think I will update the screenshot once the new way is in place



Are you running ground control from the source code or from one of the pre-compiled versions?

---

Posted on **2017-03-26 12:23:10** by **chadheiser**:

I think we are still running from a pre-compiled version that I downloaded on Thursday the 23rd. I'll update and after replacing the board I'll try that file again plus I'll look for oval issues.

---

Posted on **2017-03-26 12:23:58** by **chadheiser**:

Also I'll update firmware. We had computer issues and had to jump to another machine so updating got lost in the process.

---

Posted on **2017-03-26 12:40:12** by **davidlang**:

people have shown that having the measurements off by an inch or so causes them to cut ovals instead of circles

---

Posted on **2017-03-26 12:46:56** by **chadheiser**:

That makes sense. I'll try to get more accurate measurements and run that.

---

Posted on **2017-03-26 12:57:08** by **Bar**:

The latest version from the source actually improves the way the calculations are done. I compiled a "between releases" version in [this](http://www.maslowcnc.com/forums/#!/no-judgement:cant-load-the-sled-nc-fil) forum conversation that seems to have helped there

---

Posted on **2017-03-26 13:22:38** by **jbarchuk**:

> @chadheiser

> I think we are still running from a pre-compiled version that I downloaded on Thursday the 23rd.

All downloadable files should have a version embedded in the name to make keeping older files for fallback easier.

All screen based software should have the version right there so there's no uncertainty.

---

Posted on **2017-03-26 13:33:03** by **rexklein**:

Second to the idea of firmware versioning. This again will be a big help for future tech support.

---

Posted on **2017-03-26 13:36:11** by **Bar**:

+1

---

Posted on **2017-03-26 13:39:24** by **Bar**:

I've created issues in both the firmware and Ground Control for this [here](https://github.com/MaslowCNC/GroundControl/issues/138) and [here](https://github.com/MaslowCNC/Firmware/issues/149)

---

Posted on **2017-03-27 12:04:08** by **rancher**:

> @Bar

> the GRBL-generic one looks pretty good



This one is a no go.  Open paths at the fillets again.

---

Posted on **2017-03-27 12:22:27** by **Bar**:

:-(

---

Posted on **2017-03-27 12:24:57** by **Bar**:

Autocad hasn't responded yet, but I'll let everyone know as soon as they do. Until then, would you be willing to make an [issue](https://github.com/MaslowCNC/GroundControl/issues) for that and attach the file?

---

Posted on **2017-03-28 09:55:30** by **allensparks**:

Just so people try the print issue compared to the actual cut above is not unexpected. I tested 10 printers once for work same settings same pdf 10 different prints, this is why good print shops still exist because there is as much experience behind producing what the customer wanted as there is in setting up a cnc router :)

---

