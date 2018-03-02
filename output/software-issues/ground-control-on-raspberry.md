## Ground Control on Raspberry Pi
Posted on **2017-03-28 17:37:38** by **Bar**:

Instructions for setting up Ground Control on a Raspberry Pi are up! You can find them [here](https://github.com/MaslowCNC/GroundControl/wiki/Linux)

---

Posted on **2017-03-28 18:53:16** by **TheRiflesSpiral**:

"...As of this writing the current version of KivyPi does not actually come with Kivy installed for python 2..."



LOL whoops!

---

Posted on **2017-03-28 18:54:33** by **Bar**:

I know, right? They had one job!

---

Posted on **2017-03-29 11:21:03** by **mikeberg**:

i'm so happy now my raspberry pi 1 model b+ can open ground countrol with no problem with your instruction

---

Posted on **2017-03-29 11:28:35** by **Bar**:

That is FANTASTIC NEWS! Thank you for letting me know

---

Posted on **2017-03-29 14:25:20** by **mikeberg**:

i have issue with the cursor is not  able to open top left pannel,it open like an half second

---

Posted on **2017-03-29 14:26:10** by **mikeberg**:

I'm using mouse and keyboard

---

Posted on **2017-03-29 15:15:53** by **mikeberg**:

i sugest to add the path before do main.py in your tutorial for make it more easy to follow(cd /home/sysop/groundcontrol/)

---

Posted on **2017-03-29 15:18:13** by **mikeberg**:

And replace main.py for sudo python main.py

---

Posted on **2017-03-29 15:37:41** by **Bar**:

You can edit the wiki page directly if you would like, I can also update it as soon as I finish the update for today

---

Posted on **2017-03-29 16:39:51** by **TomTheWhittler**:

Make sure you use a separate USB keyboard and separate USB mouse. Those USB mouse plugged into a USB keyboard (like some apple and others) will not work correctly.

---

Posted on **2017-03-29 16:49:09** by **TomTheWhittler**:

Ones like the Dell  keyboard one with 2x USB ports on it will not work as it drains to much power from a single Raspberry Pi port.

---

Posted on **2017-03-29 16:50:39** by **TomTheWhittler**:

Not that this is your problem but a general shout out in case people see a flaky mouse/keyboard.

---

Posted on **2017-03-29 17:13:33** by **scottsm**:

I'm using a touch screen, and the touch is spot on. The mouse cursor is offset however - that is, the the click action occurs northwest of the blue cursor circle. Not sure what's going on there, a Kivy thing I guess. Since I'm using the touch screen, I've dodged that bullet :)

---

Posted on **2017-03-29 17:24:38** by **mikeberg**:

do you think i should buy one usb hub with power independent

---

Posted on **2017-03-29 17:26:10** by **mikeberg**:

The circle is offset for me to

---

Posted on **2017-03-29 17:37:10** by **scottsm**:

That offset circle can bite one when clicking on the control buttons! Easy to get the wrong one... :(

---

Posted on **2017-03-29 18:49:03** by **scottsm**:

Too, on my setup the touch screen cuts off the bottom of the Actions and Settings panes. The keyboard enters double characters - makes it impossible to type in values for settings. Is this the same for others? If so we should open issues on these.

---

Posted on **2017-03-29 19:12:59** by **TheRiflesSpiral**:

As I recall when trying to get Kivy working on Raspbian, there's a folder that holds the image files that appear during touches and when the cursor moves... I think they're separate. It might make sense to edit that image so it's more clear where the click/tap occurs.

---

Posted on **2017-03-29 21:24:18** by **Bar**:

@theriflesspiral that's a great suggestion.



@everyone, please open issues! If we have issues open for things like the text being off screen an no touch screen way to edit settings we will be sure to fix them!

---

Posted on **2017-03-29 23:40:46** by **scottsm**:

You're right of course. Issues for the dursoe click, screen size, and keyboard duly entered.

---

Posted on **2017-03-30 09:03:16** by **TheRiflesSpiral**:

I updated the GitHub issue for both the mouse cursor and the double-typing issue. They both require some digging into the Kivy filesystem though. I've tested the solution on my RPi (built using Bar's instructions) and I'll give it a shot in windows. The challenging part is the paths, which is the detail I'll add when I get a chance.

---

Posted on **2017-03-30 09:42:09** by **scottsm**:

You're an ace, @TheRifleSpiral! 

For posterity, on my kivypie, (but I think it's generic) the location to put the defaulttheme-0.png file is:

/usr/local/lib/python2.7/dist-packages/kivy/data/images

---

Posted on **2017-03-30 09:50:39** by **TheRiflesSpiral**:

That's where I found it as well. Is this only an issue with the Pi or are Windows users having the same issue?

---

Posted on **2017-03-30 10:04:59** by **scottsm**:

Once again, you've done it with regard to the keyboard double-keystroke issue.  👍 

For posterity, on my (generic) kivypie setup, I edited

/home/sysop/.kivy/config.ini and commented out the line:

%(name)s=probesysfs,provider=hidinput



 Note that this change also corrected an issue with mouse-clicking which affected the mouse but not the touchscreen, causing double-clicks instead of single clicks.

---

Posted on **2017-03-30 10:05:59** by **scottsm**:

I haven't seen these issues on Win10.

---

Posted on **2017-03-30 10:07:02** by **TheRiflesSpiral**:

Ah yes... I hadn't considered that. The %(names) wildcard exists for support of joysticks, I think. I'm sure one day someone will be controlling Maslow with an XBox controller. :D

---

Posted on **2017-03-30 10:29:20** by **TheRiflesSpiral**:

I'm sorry @Bar I'm a GitHub newbie... I see you that you merged my changes but when I try to fork MaslowCNC/GroundControl I get different contents. There's a note that says "This branch is 8 commits behind MaslowCNC:master"



How do I synchronize my branch with the current one?

---

Posted on **2017-03-30 10:39:35** by **Bar**:

Hmm, are you using the github desktop?

---

Posted on **2017-03-30 10:44:27** by **Bar**:

I think you may just want to click the  [sync](//muut.com/u/maslowcnc/s2/:maslowcnc:nOKB:sync.jpg.jpg) button when you are on master. That should download all of the latest changes.

---

Posted on **2017-03-30 10:50:01** by **Bar**:

After doing that if you have a branch that is now out of date you can click the  [update from  master](//muut.com/u/maslowcnc/s2/:maslowcnc:UkwJ:afterthat.jpg.jpg) button to add all of the changes everyone has made to the branch (usually not necessary)

---

Posted on **2017-03-30 11:09:02** by **TheRiflesSpiral**:

Oh, no I was using the website. I'll get the desktop app and work it out.

---

Posted on **2017-03-30 11:18:48** by **Bar**:

There is a guide [here](http://www.maslowcnc.com/howtocontribute) that might be helpful

---

Posted on **2017-03-30 11:23:29** by **mikeberg**:

scottsm you are saying you haved resolved the problem when we click on action button it now doing just one click .for me its like if its clicking two time the page cannot appear is frustrating a bit

---

Posted on **2017-03-30 11:36:20** by **Bar**:

@mikeberg, you might want to check out [this issue](https://github.com/MaslowCNC/GroundControl/issues/160) on GitHub which describes the solution

---

Posted on **2017-03-30 11:44:21** by **jbarchuk**:

> @TheRiflesSpiral

> I'm a GitHub newbie…

Me too mostly. I'm getting a grip on command line because it's faster and more versatile than the GUI and the GUI is not intuitive.

The screen isn't laid out very well IMO. Or a least there're points where I'd move things around on the screens.

I commented once that Bar's tutorial got me through the process fairly straightforward. I'll read it again and see what looks thin or awkward on the explanation and description sides of things. Any Qs or problems you have by all means ask away.

---

Posted on **2017-03-30 12:02:53** by **TheRiflesSpiral**:

My main issue at the moment is that when I look at my branch of MaslowCNC/GroundControl (TheRiflesSpiral/GroundControl) it says it's 10 commits behind yet when I go to the desktop app and click "sync" it says I'm up to date. There are also obvious changes to the file structure on the web that aren't in my local copy.

---

Posted on **2017-03-30 12:05:16** by **Bar**:

Hmmm

---

Posted on **2017-03-30 12:05:36** by **Bar**:

I don't have much experience with making actual changes on the web side

---

Posted on **2017-03-30 12:06:49** by **Bar**:

It might be easiest to just ignore the web side and make the changes locally. It doesn't answer your question, but it might be the fastest way

---

Posted on **2017-03-30 12:28:54** by **TheRiflesSpiral**:

Happy to try it out. I'll add the Images folder and the images themselves and do a pull request and see how it merges.

---

Posted on **2017-03-30 13:54:37** by **scottsm**:

@mikeberg, did you have success with the mouse-click issue?

---

Posted on **2017-03-30 15:12:20** by **mikeberg**:

I didn't try maybe tonight

---

Posted on **2017-03-30 15:20:44** by **mikeberg**:

if it working i will make it know

---

Posted on **2017-03-30 15:34:19** by **mikeberg**:

hey folks what model of raspberry pi did you use with groundcontrol and did you test it with real cut

---

Posted on **2017-03-30 16:43:56** by **TheRiflesSpiral**:

All my testing (And Bar's as well) has been with a Raspberry Pi 3. I don't have a machine, though so I can't test anything past the GUI.

---

Posted on **2017-03-30 17:30:31** by **mikeberg**:

Hey @TheRiflesSpiral are you able to make one simulation with a g code program with no issue !?

---

Posted on **2017-03-30 17:46:23** by **scottsm**:

I'm cutting one of the sample files right now. I had to edit the groundcontrol.ini file from the command line because the screen size issue makes some of the values impossible to reach within GroundControl :( Other than that, it is working as well as I have hoped.

---

Posted on **2017-03-31 03:50:56** by **TheRiflesSpiral**:

@mikeberg I'll try that this morning and let you know.

---

Posted on **2017-03-31 15:16:06** by **mikeberg**:

I tested to removed the double input file in configuration.ini and I'm not able to open the action bottom in kivy when I click on it

---

Posted on **2017-03-31 15:22:35** by **TheRiflesSpiral**:

Mike, I'm having the same issue today. I'm also getting double keyboard input. I have to do some digging.

---

Posted on **2017-03-31 15:44:24** by **mikeberg**:

Action button isn't functioning but setting bottom yes its really weird

---

Posted on **2017-04-05 22:18:30** by **scottsm**:

Should we keep this issue open on github, or close it? Anyone for keeping it open?

---

Posted on **2017-04-06 03:36:54** by **TheRiflesSpiral**:

The double-typing/clicking fix didn't work for me but it worked for some. I'm going to start from scratch on a blank card and see what happens. I'm okay either way. (keep open/close)

---

Posted on **2017-04-06 07:41:02** by **Bar**:

Let's keep it open until we're sure of the solution

---

Posted on **2017-06-29 09:41:32** by **ak_thor**:

I don't expect to receive my Maslow until Sept. or later. However, I am eager enough that I have GC installed on a Raspberry Pi 3 with a touch screen. It looks Okay. I am having difficulty in trying to figure out how to install GC updates. Please provide the lines of code( i.e. "sudo.....") or similar.

---

Posted on **2017-06-29 11:03:32** by **scottsm**:

I use the browser to download the most recent release [from this page](https://github.com/MaslowCNC/GroundControl/releases), then extract that into my home directory. Then in a terminal session, I cd into that directory and run it with ‘python main.py’. Not sure how you’d do the first part from the command line, to find the URL of the most recent release.

---

Posted on **2017-06-29 11:06:09** by **scottsm**:

I use a similar process to get the release of the firmware. I use the Arduino GUI to upload that.

---

Posted on **2017-06-29 11:45:24** by **TheRiflesSpiral**:

I *think* you can just

---

git pull GroundControl

---

from a terminal window. That will update your clone to the newest revision. If you want to keep your versions separate (from release to release) then you'll have to use a browser to download the repository.

---

Posted on **2017-06-29 13:57:26** by **davidlang**:

you shouldn't need to keep your versions separate, you can always switch to a specific version by doing git checkout v0.73 or similar

---

Posted on **2017-06-29 14:13:50** by **TheRiflesSpiral**:

Nice tip, David. 



On my system, I had to

---

git remote update

git fetch

git checkout v0.73

---

And that did it. Prior to remote update and fetch I was getting a pathspec error.

---

