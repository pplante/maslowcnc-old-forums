## Introduction plus Headless Raspberry Pi 3
Posted on *2017-01-02 11:10:39* by *jessbussert*

Hey folks,

This is Jessica.  I'm a geeky, maker chica.  I've designed and built a few other CNC machines in the past (anyone remember the ULN2003?) but I'm excited to finally get my hands on a machine that can cut large format pieces!  I've been messing in the background for a while but Bar recently asked me to post a few things I've been working on here to the forums.

My intended build is to mount controllers, motors, and everything on the sled itself for improved portability.  I also plan on having each motor mounted on a swivel arm (think of a lazy Susan bearing) so I can keep a pure triangular geometry.  This last should allow me to increase both the speed and the accuracy of the machine.  Or at least I hope so!

To this end I've dedicated a headless RPi 3 to act as the host controller.  Since this will be mounted on the actual sled I won't have a place for a keyboard or display.  As such I'll be using VNC from my laptop or phone to control the mill.

Getting the base configuration was pretty simple.  I've got another headless RPi working as a firewall and the buil d instructions for this kind of configuration are all over the web.  Trying to get Kivy up and running has been another thing entirely.  So far I've been able to get a Kivy display up in a second, concurrent VNC session.  Unfortunately, I can't get any mouse or keyboard response to this 2nd display and I currently don't know why.

Since I didn't know I was going to be posting my efforts up for anyone else's use I sadly haven't taken very good notes so far.  Sorry for that.  A few tips that might help someone else trying to accomplish the same thing:

1)	On a RPi you won't have "kivy.deps.sdl2".  Instead you'll need to use "sudo apt-get install libsdl2-2.0-0"
2)	Similarly, you also won't have "kivy.deps.glew".  I used " sudo apt-get install --upgrade libglew1.10" and "sudo apt-get install --upgrade libglewmx1.10".  I really don't know if you need both of these.  I installed both cuz I was tired and didn't want to futz around with it.
3)	You need to make sure your user has access to the serial port.  I used "sudo usermod -a -G dialout "${USER}" #" to accomplish this.
4)	Finally, I had to start a special X windows session for Kivy to use as a display.  The one that seems to work is called DispmanX.  You can find a write up for installing it here: http://raspmer.blogspot.com/2015/07/vnc-server-for-raspberry-pi-with.html
5)	The Freenode IRC channels #raspberrypi and #arduino were both helpful in my efforts so far.  If you see "JessicaRN" give me a shout!

All in all, I don't know how much effort I'm going to put into Ground Control.  I don't much like it (sorry Bar!) and it seems like there are better tools available.  Since Bar came up with this amazing idea to just send pure G-Code to the Maslow board it seems to me that it would be a fairly easy task to mod one of the existing open source CNC simulators to simply output their G-Code line by line to the serial port.  I'm going to spend some time looking into this as a possibility and I'll report what I find here.

What do the rest of you think about hacking up a simulator and using it as a controller?

Also, would any of you be interested in organizing a weekly chat on Google Hangouts to exchange ideas?  I would only want to do it if enough people were interested.  Personally I wouldn't be able to attend all the time anyway.  I'm an ER nurse and I have a crazy, chaotic work schedule.

I look forward to hearing back from you all.

Ciao,
Jessica

---

Posted on *2017-01-02 16:16:45* by *TomTheWhittler*

Hi Jessica,
you wrote "Unfortunately, I can't get any mouse or keyboard response to this 2nd display and I currently don't know why."

 You should check out on the Maslowcnc forum the topic of "Raspberry Pi 3 setup for Ground Control".
TheRiflesSpiral is working on getting mouse and keyboard going for Kivy and he might be one day away from getting it to work once he gets back to work.
Check out bCNC.

---

Posted on *2017-01-02 18:12:21* by *jessbussert*

Thanks Tom,
I'll check that out.  Things are a bit different in my config because I have no physical display.  That said, it might still be the same solution.

---

Posted on *2017-01-03 11:47:19* by *TomTheWhittler*

The "Raspberry Pi 3 setup for Ground Control"
is under the forum link on maslowcnc  of Dev
http://www.maslowcnc.com/forums/#!/dev

---

Posted on *2017-01-04 09:02:47* by *TheRiflesSpiral*

Hi, Jessica. I think your keyboard events are probably making it to Kivy, as well as your mouse events... try this; launch Ground Control and don't move the mouse. Hold the mouse button down then drag... does the stage move? (The area with the crosshairs and center mark)

Also, try pressing F1 on your keyboard (or however you get function commands into the VNC environment... I know sometimes the F keys don't work like they're supposed to) You should get the GroundControl Settings window.

---

Posted on *2017-01-04 09:03:58* by *TheRiflesSpiral*

If those things work then you've got the same situation I have. I can walk you through getting a mouse cursor to show up when you mousedown but that's as far as I've been able to get.

---

