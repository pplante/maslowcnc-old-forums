## Cannot get ground control to run
Posted on *2017-06-09 14:04:55* by *aktroy*

Hi folks:

I spoke to Bar directly about not being able to run ground control and all that he said was update my drivers. Well, on one computer I could not do that,  but on the other I was able to upgrade. Despite the upgrade,  I still cannot run ground control. On one computer I can actually see the  error message that talks about upgrading the driver, but on the second one I cannot see what the error messages, as it simply closes the dialog box before I can even glance at what it says. 

My understanding is the main problem is with OpenGL, and probably older systems. There was talk in another thread about changing a few lines of code to make it run. (I'm on windows)  Admittedly, I'm no computer programmer, and don't have any clue as to how to add lines of code to the program. I of course can follow instructions if somebody can give me detailed instructions of how to do this.

The only other option left is to buy a new computer, and with three separate computers at the house here I hate to have to spend more money just to run ground control. It seems like a pretty basic  program otherwise.

Any help appreciated, as I'm dead in the water until I can get ground control running.

Also, is there some minimum requirement for ground control to run? I'd really like to use an older XP laptop that I can dedicate just the the cnc. Definitely not practical to use my desktop computer. Not sure if android is an option at this point or not, but would be great to use my tablet as well. 

Thanks!

Troy

---

Posted on *2017-06-10 05:18:07* by *mikeberg*

What brand of processor did you use in your computer?

---

Posted on *2017-06-11 11:03:22* by *gero*

There is still hope. Currently testing with kubuntu on some old machine. Pentium something. If you don't want to lose your xp you could install aside of windows. You can test the linux from and usb drive before installing and deciding. Kivy is giving me a critical warning that OpenGL 2.0 is not found and 1.4 is detected. It even tells me "The application will leave now" but CG stays open and looks fine and draws the loaded file nicely. Sadly can't test moves as I am stuck with the a dropping connection to the Arduino.

---

Posted on *2017-06-11 12:08:58* by *gero*

Just confirmed that I can run GC on an old PC
Intel(R) Pentium(R) Dual  CPU  E2220  @ 2.40GHz
PCI bridge: Intel Corporation NM10/ICH7 Family PCI Express Port 1 (rev 01)
VGA compatible controller: Intel Corporation 82G33/G31 Express Integrated Graphics Controller (rev 10)
The Graphics Controller only supports Open GL1.4

@ aktroy You could also plug in some cheap graphic card from a garage sale if you search that it supports OpenGL 2.

---

Posted on *2017-06-11 12:20:28* by *mikeberg*

For me on Linux the issue I was found is the lack of connectivity too... All  the rest has been good, all driver was found automatically when I installed Linux os nothing to say about that

---

Posted on *2017-06-11 12:31:53* by *gero*

I love the fact that I can get my laptop back out of the workshop by recycling some old junk with the help of Linux. Yes, I can't use Sketchup or Fusion but have my workarounds.

---

Posted on *2017-06-11 15:27:19* by *mikeberg*

Totally agree 👍  and no cost fee for Linux software

---

Posted on *2017-06-12 10:40:04* by *gero*

Well the joy was short. With Ground Control Version 0.75 Kubuntu 14.04 LTS was knocked out off the supported platforms. It is running in Ubuntu Mate, but thats probably not a good choice for old hardware.

---

Posted on *2017-06-12 12:10:07* by *mikeberg*

For older computer I suggest you lxde desktop , simple and stable

---

Posted on *2017-06-12 12:21:08* by *mikeberg*

Did you try windows 7. Is a compromise between elegance and stable . I control ground control with my cellphone everywhere in my house with VNC, good server and it's free , when in cutting In my garage I can look it and do something else in same time

---

Posted on *2017-06-12 13:56:54* by *gero*

Thanks @mikeberg, I will give lxde desktop a try. Installing a new OS is quite time consuming and after a working day not the task I am up to. Plus on my labptop I would have to secure plenty of data first. As long as I can't track the issue to its source, different distros are like fishing in the dark. Since I have nothing to loose, I might check with updating the Kernel on the old PC. Windows is not an option for me, besides the fantastic idea, it was the Cross-Platform that got me hooked up with the Maslow.

---

Posted on *2017-06-12 15:47:02* by *scottsm*

@gero, would there be any benefit to trying to update pyserial and Arduino on the Kubuntu box?

---

Posted on *2017-06-12 17:18:10* by *mikeberg*

I tried Linux manjaro is based on arch-linux and it's very friendly to use, stable, and it based on updating automatically

---

Posted on *2017-06-12 17:22:24* by *mikeberg*

All was good with ground control except connecting USB device and connecting on port,we haved maybe the same problem

---

Posted on *2017-06-12 23:06:56* by *gero*

@scottsm I will try pyserial. Arduino IDE is the latest and works fine and the serial monitor gives me what the firmware sends. Also no issue sending commands to the Arduino in the monitor. That could be a hint on python. Just need time to test. Saturday is coming. I'll also ubgrade to 16.04 to if that changes something. I'll skip the learning curve to sniff the communication for the moment. Although that could be useful in other projects as well.

---

Posted on *2017-06-12 23:10:09* by *gero*

@mikeberg On the weekend I'll circle in on why GC is working on newer distros.

---

Posted on *2017-06-13 09:46:45* by *gero*

Warning! This (fix?) is not recommended as it is unclear if it might break more then it fixes. On Kubuntu 14.04LTS pyserial 2.6 was the installed version. On Ubuntu-Mate 16.10 and Kubuntu 16.04LTS the version is pyserial 3.3. The command "sudo pip install pyserial --upgrade" uninstalled 2.6 and installed 3.3. GC is not dropping the connection anymore on Kubuntu 14.04LTS. Great thanks to @scottsm!!!
P.S. Do not try this at home!!! :-o

---

Posted on *2017-06-13 09:51:34* by *gero*

@mikeberg On lubuntu-17.04 sadly the installation of Kivy failed with:
"The following packages have unmet dependencies:
 python-kivy : Depends: python-gst0.10 but it is not installable
E: Unable to correct problems, you have held broken packages." :-(

---

Posted on *2017-06-13 10:25:07* by *Bar*

Just so I can better understand and advise anyone if the issue pops up in the future. The issues that we to be running Pyserial 3.3? 

Pyserial 2.6 causes the dropped connection? 

It seems strange that we're seeing the issue only with newer Ground Control versions. I wonder what we changed.....OHHHHHH I know exactly what's happening. We're reading the amount of data held in the computer's internal buffer now, and I remember reading in the documentation that pyserial changed the way that interface works between 2.x and 3.x.

How can we make it clear in the future that pyserial 3.x is needed?

---

Posted on *2017-06-13 10:32:13* by *gero*

As long as I am the only one using a rather old 14.04, I would not bother. The 2 newer releases 16.04LTS and 16.10 I have tried have the pyserial3.3 by default. The problem with all this linux flavors is that they keep different packages of different stuff. The good thing is I ran and installed everything from and on a USB-drive, so you can test without installing anything on the hard drive.

---

Posted on *2017-06-13 10:37:07* by *gero*

On a side note, in a linux terminal >>> pip list <<< gives the versions of modules installed like:
alabaster (0.7.8)
appdirs (1.4.3)
Babel (2.3.4)
beautifulsoup4 (4.5.1)
boto (2.40.0)
chardet (2.3.0)
configobj (5.0.6)
cryptography (1.5)
cycler (0.10.0)
deja-dup-caja (0.0.4)
dnspython (1.14.0)
docutils (0.12)
duplicity (0.7.6)
enum34 (1.1.6)
folder-color-caja (0.0.79)
folder-color-common (0.0.79)
html5lib (0.999)
idna (2.1)
imagesize (0.7.1) 
ipaddress (1.0.16)
Jinja2 (2.8)
Kivy (1.10.0)
Kivy-Garden (0.1.4)
kiwi (1.9.22)
lockfile (0.12.2)
lxml (3.6.4)
MarkupSafe (0.23)
mate-menu (16.10.1)
matplotlib (1.5.2rc2)
mercurial (3.9.1)
ndg-httpsclient (0.4.2)
numpy (1.11.1rc1)
packaging (16.8)
Pillow (3.3.1)
pip (9.0.1)
Pivy (0.5.0)
pyasn1 (0.1.9)
pycrypto (2.6.1)
pygame (1.9.3)
Pygments (2.1.3)
pygobject (3.22.0)
PyODE (1.2.0)
PyOpenGL (3.1.0)
pyOpenSSL (16.1.0)
pyparsing (2.2.0)
pyserial (3.3)
python-cloudfiles (1.7.10)
python-dateutil (2.4.2)
python-xlib (0.14)
pytz (2014.10)
pyxdg (0.25)
requests (2.10.0)
roman (2.0.0)
setproctitle (1.1.8)
setuptools (35.0.2)
six (1.10.0)
Sphinx (1.4.8)
sphinx-rtd-theme (0.1.9)
urllib3 (1.15.1)
virtualenv (15.1.0)
wheel (0.29.0)

---

Posted on *2017-06-13 15:39:01* by *scottsm*

For what it’s worth, I’m using Python 2.7 on OS X. Not sure how to check the pyserial version, though.

---

Posted on *2017-06-13 15:45:40* by *scottsm*

Pyserial doesn’t show up in the pip list.

---

Posted on *2017-06-13 16:40:08* by *gero*

On the tested Linux that work with the new GC the Python v2.7.12 (default, Nov 19 2016, 06:48:10) comes with pyserial (3.3). The one that dropped the connection was Python v2.7.6 (default, Oct 26 2016, 20:30:19) and came with pyserial (2.6). What a difference less then a month can make :-)

---

