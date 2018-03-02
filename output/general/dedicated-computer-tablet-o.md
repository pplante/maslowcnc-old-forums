## Dedicated Computer Tablet Options
Posted on *2017-03-09 11:25:41* by *tmaker*

Guys and Gals - I'm very excited to be receiving my beta tester kit here soon!  I was thinking about purchasing a dedicated computer tablet that I can leave on the Maslow so that I don't tie up my Macbook Pro when making cuts.  Is there a particular tablet that comes recommended based on low cost and features that make it a good option to mount on your Maslow as a dedicated unit?  I think I remember Bar mentioning that his was somewhere around $100 but that he couldn't keep the power plugged in because it uses the same usb port.  I'm trying to find something that's cheap but also allows it to stay plugged into power and obviously, has a sufficient amount of power under the hood to do what it needs to do.  I won't be using it for anything else other than to be the brains powering my Maslow machine.  Thank you!

---

Posted on *2017-03-09 11:43:06* by *Bar*

I've switched over to a Raspberry Pi 3 with the touch screen attachment and so far I'm pretty happy with it. I haven't got that much experience using it because we don't have internet in the building yet so transferring files with thumb drives is more trouble than just using my computer. I think that the total cost was around $140 for all the parts (pi, SD card, screen, power supply) so it was a little more expensive, but getting to use a Pi was a cool experience

---

Posted on *2017-03-09 11:50:39* by *tmaker*

I'm not that familiar with Raspberry Pi.  Does it run windows?  How much typing is is typically involved in running the Maslow from the tablet?  I'm curious if I would at all benefit from one of those tablets with the detachable keyboard like this: https://www.amazon.com/Cambio-Windows-Touchscreen-Computer-Bluetooth/dp/B0188NA4DS/ref=sr_1_8?s=pc&ie=UTF8&qid=1489086968&sr=1-8&keywords=windows+tablet

---

Posted on *2017-03-09 16:07:31* by *davidlang*

The Pi can run the IoT version of windows, but 99%+ of people run Linux on it. At the moment there's a fair amount of work needed to get it running, but as soon as I can get my hands on the info, I'll simplify it for people.

The pi has an HDMI output, so if you have a TV in the area, you cna use that for the display. The basic Pi runs ~$35 (not counting a USB power supply, keyboard/mouse, microSD card and monitor)

---

Posted on *2017-03-09 16:14:07* by *mooselake*

A refurbished or cast-off home PC (you know, the one the kids won't touch) might be a good choice.  Older desktop PCs are popular with the LinuxCNC crowd - while that has as much to do with having a parallel port as the PC it proves they're powerful enough to work.  If you'll settle for a CRT monitor they're pretty much giveaways these days.

---

Posted on *2017-03-09 16:53:19* by *davidlang*

@mooelake, true, but you'll end up spending as much in power as you would to buy a Pi before too long :-)

---

Posted on *2017-03-09 17:50:16* by *tmaker*

How much processing power is really needed to run the Ground Control software?  I'm thinking about this: https://www.amazon.com/Lenovo-Ideapad-110s-Laptop-Storage/dp/B01N05RBC4/ref=sr_1_1?ie=UTF8&qid=1489109630&sr=8-1&keywords=lenovo+110s

Here's the same thing but the 2 core processor version: https://www.amazon.com/dp/B01MQTJXWZ/ref=psdc_13896615011_t1_B01N05RBC4

---

Posted on *2017-03-09 17:55:32* by *Bar*

Not much processing power is needed. I use a windows 10 netbook like that (an eebook) as my laptop so it should run great :-)

---

Posted on *2017-03-10 03:50:40* by *tmaker*

I went ahead a ordered the 2 core processor version just thinking that one day it might come in handy if I ever decide to use the machine for something else that needs a little more power.

---

Posted on *2017-03-10 09:53:06* by *Bar*

Having the extra processing power is probably a good thing :-)

---

Posted on *2017-03-10 12:06:02* by *mooselake*

@davidlang, probably not if you turn it off when you're not using it.    Here in REA land we pay $0.25/kw, or a nickel an hour to run a 200W PC.  Say $50 (low in my experience) for a RPi, decent SD card, power supply that's a thousand hours.  Anybody with reasonable power costs will get a lot more.  Not to diss the RPi, I have a V2 that's on all the time running my Ubiquiti AP controller.  By the time you add a display you're close to the new gen Netbook above.

What are the chances Ground Control will run on a Chromebook?

---

Posted on *2017-03-10 16:12:10* by *davidlang*

I understand that chromebooks are able to run android apps nowdays, so it should be good.

---

Posted on *2017-03-10 17:44:39* by *tmaker*

Android apps?  I was under the impression that Ground Control required OSX or Windows (not Android)

---

Posted on *2017-03-10 19:33:22* by *davidlang*

the Pi version runs on Linux, and the Tablet version would be Android

---

Posted on *2017-03-10 20:48:03* by *tmaker*

Back in November I asked Bar if it would run on Android.  Here's the conversation: http://www.maslowcnc.com/forums/#!/technical-details:can-i-run-the-software-on-a/its-python-which-has-a-lot

---

Posted on *2017-03-11 02:51:06* by *TheRiflesSpiral*

@jbnimble has since worked out an install for android. http://www.maslowcnc.com/forums/#!/software-issues:problems-running-ground-con

---

Posted on *2017-03-11 10:38:20* by *jbnimble*

Instructions for [building an Android APK are in the Wiki](https://github.com/MaslowCNC/GroundControl/wiki/Building-Executables) and there are TODO's for anyone that wants to write up instructions for other platforms (hint hint)

---

