## CALLING ALL RASPBERRY PI USERS
Posted on *2017-04-06 11:29:34* by *TheRiflesSpiral*

If you're using a Raspberry Pi for Ground Control, please sound off with the following info:

What version of board? (RPi 2/3/etc)
What's your distro? (post output of 'uname -a')
When you use the keyboard to type values, do you get double-input? (Click "Dist to move" then type (don't touch/click) numbers)
When you use the mouse to click buttons, do you get double-clicks? (Click "Dist to move" then click a number (don't touch/type)

I can't seem to get Kivypie functioning without double click/type issues regardless of the ~/.kivy/kivy.ini content and I need to find a pattern.

---

Posted on *2017-04-06 12:42:25* by *scottsm*

I'm using a Pi 3 B, my distro is:
Linux kivypie 4.4.50-v7+ #970 SMP Mon Feb 20 19:18:29 GMT 2017 armv7l GNU/Linux

I had double keystrokes and mouse clicks before applying your ~/.kivi/config.ini fix. After the edit, both are corrected.

---

Posted on *2017-04-06 21:17:23* by *scottsm*

Further info - I edited the .kivy/config.ini for the only user, named 'sysop' and when I ran groundcontrol from the command line, all worked correctly.
 I also have a line in /etc/rc.local to run groundcontrol on bootup, and that one had doubles until I thought to do the same edits in /root/.kivy/config.ini; now no doubles in my bootup version either.

---

Posted on *2017-04-07 06:12:53* by *TheRiflesSpiral*

Could you hear my massive head smack from where you are?

I've been running Ground Control as the root user so of COURSE the /root/... config file is being used.

Thanks for jogging my (clearly dusty) memory about how Linux works.

Good grief. I'll update the instructions on the wiki.

Thanks again!

---

Posted on *2017-04-07 06:18:39* by *scottsm*

I was gobsmacked when after my first post that all was well, I rebooted and went into settings for an adjustment and "saw double"... look at the time difference between my posts to see that it took a while to figure out :)

---

Posted on *2017-04-07 08:41:57* by *Bar*

Great work!

---

Posted on *2017-04-07 09:46:43* by *TheRiflesSpiral*

Scott, is scrolling (to zoom the canvas) working for you? I was getting zooming instead of dragging before now I'm getting dragging but zooming doesn't work.

---

Posted on *2017-04-07 11:04:24* by *scottsm*

With the touch screen, both actions are as expected. 
With the mouse, click-drag scrolls but the wheel does not zoom. Not sure if this is a kivy or a groundcontrol thing?

---

Posted on *2017-04-07 11:06:38* by *Bar*

I'm not sure either. I know on windows and mac the scroll events are picked up correctly, has anyone tested generic linux (ubuntu or such) to confirm that the mouse scroll works there?

---

Posted on *2017-04-07 11:48:37* by *TheRiflesSpiral*

I have a SD card with Raspbian (Debian Jessie) and one with Ubuntu Mate and they both scroll in their respective window managers. I was looking through the Kivy examples to see if I could find one that used the scroll wheel but haven't found one yet.

---

Posted on *2017-04-07 11:50:09* by *scottsm*

All works correctly on a desktop machine running Ubuntu 16.04

---

Posted on *2017-04-07 11:50:16* by *TheRiflesSpiral*

Holy moly! On a whim I just decided to "startx" in Kivypie to see if there was an X server installed. There is! And the scroll wheel works in the file manager (mc)

---

Posted on *2017-04-07 11:51:56* by *scottsm*

Bonus points if you can reach the screen running groundcontrol remotely! That's what I _really_ want...

---

Posted on *2017-04-07 11:56:09* by *TheRiflesSpiral*

sudo apt-get install vnc4server

---

Posted on *2017-04-07 11:56:36* by *TheRiflesSpiral*

Oh, wait... it's not in a window. That won't work.

---

Posted on *2017-04-07 12:54:29* by *scottsm*

kivy-examples/demo/pictures scroll and zoom both work with the touchscreen but zoom doesn't work with the mouse

---

Posted on *2017-04-07 13:27:26* by *Bar*

That's a good test. It might be that we are simply not getting mouse scroll events to kivy on the pi. Is there another way we could add zoom capability beyond the mouse wheel and touch pinch?

Onscreen + and - buttons seem clunky but they would work.

---

Posted on *2017-04-07 14:01:59* by *TheRiflesSpiral*

Nice sleuthing. I wonder if the kivypie folks have that on a list...

---

Posted on *2017-04-07 16:05:05* by *TheRiflesSpiral*

Page up and page down come to mind. Or if you can capture left and right click at the same time, make Lclick+Rclick "zoom" mode where up and down mouse moves are the equivalent of scroll wheel up and scroll wheel down?

---

Posted on *2017-04-07 16:08:50* by *scottsm*

I like the page-up/down idea :)

---

Posted on *2017-04-07 16:17:08* by *TheRiflesSpiral*

Scott, I found this regarding VNC with Kivy apps: it looks like you need the X11vnc and launch GroundControl from the GUI? Might be worth the experiment. https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=146749

---

Posted on *2017-04-07 16:24:05* by *Bar*

Both of those zooming suggestions are great, both are better than the add more buttons idea to the screen. Glad I asked! I'll start with page up/down because that will be easier to do. I've made an issue for the idea [here](https://github.com/MaslowCNC/GroundControl/issues/178) so I won't forget

---

