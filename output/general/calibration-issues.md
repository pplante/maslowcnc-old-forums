## Calibration Issues
Posted on **2017-06-20 21:01:09** by **Bar**:

As we all know I broke the calibration process in last week's release, and I we've all been miserable ever since.



I really really really want to make sure we've got it fixed for this week. I've run the process a couple times now on different computers and different machines, and I'll get Hannah to do it without me giving any advice first thing in the morning, but I would love another set of eyes if anyone has the chance to take a look the version currently on GitHub.



It's not perfect, the motors are still a little jittery without the load of the sled sometimes and there's room for improvement in some other areas too, but I want to make sure this version is a good stable one for everyone to work from next week.



You'll know you are running the right version because [the version numbers will be 0.77](../../images/4V/1n/4V1n_version0.77.jpg.jpg) 



If you have a chance to give it a go, I would love to hear if it works or does not for you.

---

Posted on **2017-06-20 22:32:28** by **carlosrivers**:

Im not seeing a new version up.

---

Posted on **2017-06-20 22:38:31** by **carlosrivers**:

Sorry firmware, I was checking ground control.

---

Posted on **2017-06-20 22:46:13** by **scottsm**:

@carlosrivers, use the green 'Clone or download' button on the github code page.

@Bar, I just completed the cal sequence, three cuts to arrive at 0.3mm difference between horizontal and vertical. The calibration seems to work correctly in the GC77/FW77 pair. I saw an odd twitch during the z-axis calibration step, but after the calibration the z-axis seems to behave normally.

---

Posted on **2017-06-20 23:00:42** by **Bar**:

Thank you so much for running it! I'm glad to hear we're not seeing the kind of catistrophic issues we were before :-)

---

Posted on **2017-06-20 23:06:21** by **scottsm**:

I also ran the file that gave me so much trouble with the buffering branch, and it runs correctly. Good work on this one 👍🏻

---

Posted on **2017-06-21 05:25:59** by **rancher**:

I can go give it a go shortly here, I'll report back while it's still way too early, probably.  :)  Thank you Bar, thank you.

---

Posted on **2017-06-21 07:42:30** by **rancher**:

Well, sorry to report it's a no go for me Bar.  GC is cycling between connected/not-connected on a regular rhythm.  1bps or so.  Checked all connections.  Rechecked ports, tried connect, etc.  Same behavior.  No action from any commands.  Tried calibrate just to see, no motor spin.  Motors did buzz on PC power up.  Let me know if I can give you more info.

---

Posted on **2017-06-21 07:49:09** by **Bar**:

Ok, not ideal, but good to know.



I'll try to whip up a test file here to see what we can learn. 



What do you see when you open the serial monitor by clicking the magnifying glass like icon in the upper right corner of the Arduino program?



 It will let you see the commands being sent by the machine directly to confirm that the machine is sending it's position

---

Posted on **2017-06-21 08:01:33** by **rancher**:

I will have to hike back down there to check.  I can totally do that, but should I wait for your test file?  I'm here all day and up and down is no problem, just let me know what gets you the most info the quickest.

---

Posted on **2017-06-21 08:02:30** by **rancher**:

I should watch the serial monitor while opening and running GC?  Or just, by itself?

---

Posted on **2017-06-21 08:04:22** by **rancher**:

brb

---

Posted on **2017-06-21 08:21:49** by **rancher**:

[IMG_4244](../../images/9j/A6/9jA6_img_4244.jpg.jpg)

---

Posted on **2017-06-21 08:29:46** by **Bar**:

Try changing that baud rate in the bottom right corner to 57600. If you see text (which I think you will, judging from that garbled stuff in the screenshot), I would try opening Ground Control again. Sometimes just opening the serial connection in the Arduino program seems to make my computer happier about connecting

---

Posted on **2017-06-21 08:31:53** by **Bar**:

We're a couple hours behind here so I'm about to bike to the shop and I won't have a test file for a little bit, but if you want to wait before hiking down again I'm coming up with a list of things to try in my head

---

Posted on **2017-06-21 09:10:20** by **rancher**:

Okay, I'll wait a bit.  No hurry on my end.

---

Posted on **2017-06-21 09:58:10** by **gero**:

@rancher Had the same symptoms with last weeks GC.

On my elderly Ubuntu 14.04 the module version of pyserial was 2.6.

Trying newer Linux from USB-Stick I was able to stay connected again.

Checking the pyserial version I found out that it was pyserial 3.3.

What OS are you running? On linux the >>>pip show pyserial<<< tells the version number.

No to be confused with the Python version. We are still on 2.7 with that and Python 3.3 does not work.

---

Posted on **2017-06-21 09:59:49** by **Bar**:

Yes! Gero you are a genius. That's a great thing to test. I'll see if I can work that test into Ground Control itself so if the wrong version of pyserial is installed it will say something

---

Posted on **2017-06-21 10:24:58** by **Bar**:

Ok, I think I've got something worth testing. Give this branch of Ground Control a try when you have a chance: https://github.com/MaslowCNC/GroundControl/tree/display-more-information-on-serial-disconect



One of three things is going on. 



1) Gero is right and it's a pyserial version issue. I've added a test which will now check your version of pyserial for you and display a message if it's < 3.0 which is the old ones. That's a good thing to have in general



2) Something fishy is going on with the serial port on the windows side. I've seen this behavior happen and then go away when opening and closing the the  [serial monitor like this](../../images/7F/GC/7FGC_serialmonitor.jpg.jpg) a couple of times or restarting the computer (I know right, turn it off and back on again...)



3) Something new and weird is going on in which case the information that will help me track it down is 

        a) What is shown in the serial monitor text  [like this](../../images/cA/ec/cAec_serialmonitortext.jpg.jpg) 

        b) What is displayed in the Ground Control text monitor  [like this](../../images/4W/x1/4Wx1_gctext.jpg.jpg) 

        c) What is displayed in the command  prompt terminal that opens with Ground Control  [like this](../../images/iV/SF/iVSF_cmdtext.jpg.jpg) 



When you have a chance, let me know how those things go and we'll work from there!

---

Posted on **2017-06-21 10:31:46** by **rancher**:

Computer is new for Maslow, windows 10, but off the internet now for a couple months so no new updates.  Python will still be original, I would think, but I'm on my way down now.  I'll report back shortly!

---

Posted on **2017-06-21 10:52:17** by **davidlang**:

Bar, is there any way to detect the version of pyserial in use and send the right parameter for the version you have rather than just throwing an error?

---

Posted on **2017-06-21 11:01:24** by **Bar**:

I was thinking about that. The feature we need in version 3.x is actually available in 2.x under a different name so we could put an "if this...then this" type of statement in there, but I think it would be ugly and likely to cause as many issues as it fixes. I'm open to the idea though

---

Posted on **2017-06-21 11:02:49** by **rancher**:

Looks like Python version is an issue somehow.  My machine has been off the internet since it went down to the shop for good a few months ago.  This is new behavior for me.



[Ground control display](../../images/LD/mx/LDmx_groundcontroldisplay.jpg.jpg)



 [Python Start1](../../images/kE/7W/kE7W_pythonstart1.jpg.jpg)



 [Python start2](../../images/GK/o6/GKo6_pythonstart2.jpg.jpg)



 [Serial monitor GC running](../../images/Ot/hl/Othl_serialmonitorgcrunning.jpg.jpg)



 [Serial monitor on start](../../images/ve/dh/vedh_serialmonitoronstart.jpg.jpg)



  [Bonus](../../images/w4/YC/w4YC_bonus.jpg.jpg)

---

Posted on **2017-06-21 11:17:33** by **gero**:

Love the bonus :-)

Pyserial version.... not Python version...

---

Posted on **2017-06-21 11:20:51** by **Bar**:

Perfect! Love the bonus.



So now we need to decide what the solution is. 



I'm going to merge the version which gives the error in right now because having a good error message that makes it clear what is going on is key.



How hard is it to connect that computer to the internet?

---

Posted on **2017-06-21 11:34:45** by **davidlang**:

I suspect that we had something change in GC that made the pyserial version matter (some new option getting set that wasn't in an old version), which is why you find that a setup that worked on older versions no longer works.

---

Posted on **2017-06-21 11:45:09** by **rancher**:

I can run it up here and connect.  I can bring the boards if need be, but would probably not bring the motors.

---

Posted on **2017-06-21 11:51:59** by **davidlang**:

I think the idea is to connect and see if you can update the python/pyserial version and then take it back and try it with the machine.

---

Posted on **2017-06-21 11:54:15** by **gero**:

For checking the connection you don't need the motors or the shield. I have a second Mega in the office now, just to see if GC runs and connects.

---

Posted on **2017-06-21 12:13:00** by **Bar**:

@davidlang is right we're using more of the pyserial features now and one of them is pyserial 3+ specific



@rancher to update pyserial, type:

---

>pip install pyserial --upgrade

---



in the terminal like this:  [like this](../../images/8G/Ds/8GDs_pyserial.jpg.jpg) when the computer is connected to the internet. Just bringing the Arduino to make sure it connects is enough to know if things are working

---

Posted on **2017-06-21 13:03:53** by **rancher**:

Oh geez, I'm already over my head with the cmd thing.  But, I'm there..." 'pip' is not recognized as an internal or external command..etc."

---

Posted on **2017-06-21 13:04:58** by **rancher**:

Should mine say git\groundcontrol\ like yours does?  Mine just shows my c\users\me.

---

Posted on **2017-06-21 13:16:28** by **gero**:

I think the \git is when you clone, so I would not worry.

10 years away for win, but could the pip be a path environment thing?

---

Posted on **2017-06-21 13:17:02** by **rancher**:

I don't understand Gero.  I am getting nowhere with this, but I'm trying.

---

Posted on **2017-06-21 13:20:17** by **gero**:

@rancher Don't worry, we are all here by your side :-). The path environment thing was for the windows geeks here. Could work if you have your terminal open in a different folder. The win guys are going to sort that out.

---

Posted on **2017-06-21 13:21:22** by **rancher**:

I think it is that.  The cmd thing is open in a folder?  I found python27.  Do I open cmd in there?  How?

---

Posted on **2017-06-21 13:24:32** by **gero**:

Don't have a window to check. It might be even in hidden folders. If I have to, I can set up a win in a virtrual box and report back in a day or 2, hahah... give the guys a few minutes

---

Posted on **2017-06-21 13:25:03** by **rancher**:

Thanks Gero, I'm in no hurry.

---

Posted on **2017-06-21 13:27:11** by **gero**:

Unkle Googe says: Hold Shift + Right Click the folder you want it opened on, and click "open command window here".

---

Posted on **2017-06-21 13:28:32** by **gero**:

But if python27 is the right folder to find pip, I can't tell

---

Posted on **2017-06-21 13:30:12** by **davidlang**:

pip is a tool to manage python libraries



here is a video that says it walks you through installing it (I don't run windows on anything so I can't vouch for it's accuracy), search python pip windows and you will find lots of info

---

Posted on **2017-06-21 13:32:33** by **rancher**:

Success



python -m pip install pyserial --upgrade

---

Posted on **2017-06-21 13:33:01** by **rancher**:

Successfully installed pyserial - 3.3

---

Posted on **2017-06-21 13:33:15** by **rancher**:

Now what?

---

Posted on **2017-06-21 13:33:29** by **Bar**:

I feel you on the command line stuff, it can be a lot.



For anyone following along, running ground control from installer version doesn't require any of this.



@rancher What happens if you type "python -m pip"?

---

Posted on **2017-06-21 13:33:50** by **gero**:

Plug in the Mega and start GC

---

Posted on **2017-06-21 13:34:14** by **rancher**:

Big long list of stuff, what info do you need?

---

Posted on **2017-06-21 13:38:12** by **Bar**:

Perfect! I just needed to know that it didn't say command not found

---

Posted on **2017-06-21 13:38:26** by **rancher**:

Okay, clear for GC run?

---

Posted on **2017-06-21 13:38:43** by **Bar**:

Try putting "python -m pip..." In front of the command from before

---

Posted on **2017-06-21 13:39:07** by **Bar**:

Oh wait, I totally missed that you already got it installed

---

Posted on **2017-06-21 13:39:12** by **Bar**:

Ignore me

---

Posted on **2017-06-21 13:39:25** by **rancher**:

Lol.  I was like...?&quest;?&quest;?&quest;

---

Posted on **2017-06-21 13:39:42** by **rancher**:

Mega plugged in, green light.  Should I open GC?

---

Posted on **2017-06-21 13:39:53** by **Bar**:

Gero is right, you should be done and ready to use GC again

---

Posted on **2017-06-21 13:40:07** by **Bar**:

👍👍👍

---

Posted on **2017-06-21 13:41:19** by **rancher**:

Connected!

---

Posted on **2017-06-21 13:41:59** by **rancher**:

I can go down and run calibration start to finish any time now if it will help.

---

Posted on **2017-06-21 13:42:13** by **rancher**:

Whenever we are done doing what we can here.

---

Posted on **2017-06-21 13:43:23** by **davidlang**:

give it a try

---

Posted on **2017-06-21 13:45:02** by **rancher**:

Should I get the GC you just merged Bar, "clarify calibration"?  I am running "display more info.." version from an hour ago.

---

Posted on **2017-06-21 13:45:24** by **Bar**:

Yes! Give it a go, and let us know!

---

Posted on **2017-06-21 13:49:23** by **rancher**:

Newest version is connected as well.  I'm heading down in a few minutes, and will go through the whole thing.  Might take an hour or so.

---

Posted on **2017-06-21 15:49:33** by **rancher**:

Nailed it Bar!  It was smooth, 600mm on the nose first time through.



Here are some notes:



 *  Put the chain wrap warning in the first chain feed action, measuring motors left motor feed.  Also, wrap is a problem as we get dustier.  It would be great to have OH CRAP STOP! button right on that page as well as Unwind.



 * If the calibration routine/Ground Control window is minimized the routine window disappears and must be started over.  Didn't cause a problem to skip to lost step, but made me nervous.



 * Perhaps a warning about vertical distance measure being thrown off by chain wrap guides leading chain away from motor.  Sorta obvious, but I might have missed it last time.



*Return to center does nothing until home is defined.  I defined home as center, then rtc worked regardless of home.  I did not try define home away from center then home.  But neither rtc nor home worked until home was defined after calibration.



* Long motor stutter on Z, occasionally.



That's all I have right now.  Thank you so much for getting me back on board!

---

Posted on **2017-06-21 15:50:04** by **rancher**:

Accidental bolds there, trying to make bullets, or something.

---

Posted on **2017-06-21 16:01:28** by **Bar**:

Fantastic! I'm glad to hear it. Thank you for the suggestions, copied and pasted directly into my todo list!

---

Posted on **2017-06-21 17:29:21** by **rancher**:

It's cutting better than it ever has Bar.  I whipped out this 45 box in some scrap as a test.  Plan to redo in nice material soon, I think Maslow is ready!  I built the table while Maslow cut the box.



  [Table and Box](../../images/40/T9/40T9_tableandbox.jpg.jpg)

---

Posted on **2017-06-21 17:34:56** by **Bar**:

Fantastic! I'm glad to hear you say that, it's been a long week.



Oh man, I wish I had waited another hour to post the update. We could have had a project of the week :-)



Great work, and thanks for sharing the picture. Seeing the stuff you guys build is always my favorite

---

Posted on **2017-06-21 19:01:43** by **blsteinhauer88**:

Just loaded the most recent FW and GC and competed the calibration.  Entered the real dimensions of my mount to bit.  Test pattern like @rancher 600 mm each way.  Only thing I saw was when zeroing the gear in the first step.  It wanted to turn CCW, when asked to go CW it did not move but the motors whined.  Other than that gonna cut another Sun Moon piece now.

---

Posted on **2017-06-21 20:37:39** by **blsteinhauer88**:

A little jittery, but cut great! Thanks @bar

 [IMG_0045](../../images/rX/jc/rXjc_img_0045.jpg.jpg)

---

Posted on **2017-06-21 21:48:01** by **davidlang**:

the current fix for the communications problem slows down the rate that GC sends lines to the firmware. In your case, you have thousands of tiny cuts and so this slowdown means that GC can't send the data fast enough to keep things going.



But it's better to be slow and jittery than to be truncating data and cutting incorrectly.

---

Posted on **2017-06-21 22:50:06** by **Bar**:

@davidlang is right I had to slow things down for the serial fix which is the jitters you are seeing when running a file like that with many tiny movements. Hopefully we can get ease our way back up to full speed next week with lots of testing along the way to make sure the serial issue doesn't come back :-)

---

Posted on **2017-06-22 05:55:22** by **blsteinhauer88**:

That makes sense. It was not too bad, as I removed about 1000 points in the code to clean it up! Looks great. Going to Mexico and Disneyland so won't be a tester for a couple weeks. Bee back on the 4th of July!!

---

