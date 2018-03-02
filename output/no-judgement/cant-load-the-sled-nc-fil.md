## can't load the sled .nc file
Posted on **2017-03-25 18:36:03** by **boandersen**:

My Win 10 Ground Control exits with no warning when I press load on the sled.nc file.  Below are the latest lines from the log file. I has done this 5 times. The file I try to load is "Sled-QuarterInchBit.nc" - Any advice?
...
[WARNING           ] stderr:   File "c:\python27\lib\site-packages\kivy\lang.py", line 1557, in custom_callback
[WARNING           ] stderr:     exec(__kvlang__.co_value, idmap)
[WARNING           ] stderr:   File ".\GroundControl\.\groundcontrol.kv", line 498, in <module>
[WARNING           ] stderr:     on_release: root.load(filechooser.path, filechooser.selection)
[WARNING           ] stderr:   File "C:\Users\Bar\Git\GroundControl\UIElements\viewMenu.py", line 53, in load
[WARNING           ] stderr:   File "kivy\properties.pyx", line 408, in kivy.properties.Property.__set__ (kivy\properties.c:5114)
[WARNING           ] stderr:   File "kivy\properties.pyx", line 446, in kivy.properties.Property.set (kivy\properties.c:5876)
[WARNING           ] stderr:   File "kivy\properties.pyx", line 501, in kivy.properties.Property.dispatch (kivy\properties.c :6557)
[WARNING           ] stderr:   File "kivy\_event.pyx", line 1224, in kivy._event.EventObservers.dispatch (kivy\_event.c:13497)
[WARNING           ] stderr:   File "kivy\_event.pyx", line 1130, in kivy._event.EventObservers._dispatch (kivy\_event.c:12696)
[WARNING           ] stderr:   File "C:\Users\Bar\Git\GroundControl\UIElements\frontPage.py", line 118, in onGcodeFileChange
[WARNING           ] stderr:   File "C:\Users\Bar\Git\GroundControl\UIElements\frontPage.py", line 140, in moveGcodeIndex
[WARNING           ] stderr: ValueError: could not convert string to float: 
...

---

Posted on **2017-03-25 18:46:59** by **boandersen**:

I edited the groundControl.ini file and got rid of what was in the openFile line. That allowed me to open the sled file.  - so far so good.

But i soon got another problem.. 

 [Screen](//muut.com/u/maslowcnc/s3/:maslowcnc:sgjA:screen.png.jpg) 

I had the sled and router pretty centered on the plywood, so I wanted to do a dry run without the router powered on. Both motors came on and the sled ascended, but never stopped. I cut power to the arduino and motor control board before it killed my new sled.

Should I calibrate chain length every time i has been off?

---

Posted on **2017-03-25 19:07:27** by **boandersen**:

Answering my own question... yes, it helped recalibrating the chain length after a power off. I am getting a nice pencil drawing of the sled (not circular though, but that is what others see too)

---

Posted on **2017-03-25 19:27:29** by **boandersen**:

I drew an egg :) https://goo.gl/photos/atuUWtuJHsRCW19i9

---

Posted on **2017-03-25 20:03:34** by **Bar**:

Great trouble shooting to get this far!

I've created an issue on GitHub for the problem loading the file [here](https://github.com/MaslowCNC/GroundControl/issues/133) and I think I accidentally bundled by .ini file with the latest ground control. Thank you for pointing that out, I will fix it immediately.

To solve the egg shape problem, you will need to edit the dimensions of your machine in the settings tab in GroundControl. We're still working on dialing in the process, but you should be able to achieve a close to perfect circle by adjusting those parameters.

Let me know how it goes and if you have any questions along the way.

---

Posted on **2017-03-25 20:12:33** by **Bar**:

I've deleted the .ini file from the zip file and I will track down the line which was causing the program to crash if it couldn't find the target file path. Thanks again finding that bug!

---

Posted on **2017-03-25 21:28:08** by **boandersen**:

Wondering if the egg shape is because the temp machine has a different height to width ratio - would it maybe help to reduce the height it thinks it has?

---

Posted on **2017-03-25 21:59:33** by **Bar**:

So you are still getting the egg shape after changing the settings to match the real world dimensions of the machine?

This is something I was working on the last few days. Will you do me a favor and test the latest version and see if it works for you? You can download my super secret new version of Ground Control [here](https://github.com/MaslowCNC/GroundControl/blob/build/GroundControl-Windows%20Portable.zip) . 

That version coupled with the [newest firmware](https://github.com/MaslowCNC/Firmware) will do some of the calculations in an improved way. Note that the settings have changed, it will now ask you for the total distance between the motors now.

---

Posted on **2017-03-26 07:13:55** by **boandersen**:

had to break for sleep.. I will try the secret version. I doi not really know if I had the correct settings. I found them on the wiki:
...
[Maslow Settings]
motoroffsetx = -20
motoroffsety = 30
sledwidth = 150
bedwidth = 2438.4
openfile = C:\Users\boa\Documents\Sled-QuarterInchBit.nc
sledheight = 1
zaxis = False
sledcg = 1
bedheight = 1219.2
zpitch = 20
comport = COM3
...

---

Posted on **2017-03-26 08:05:15** by **rancher**:

Don't run it with those settings.  It will tear apart.  Somewhere Bar posted a screenshot of the old defaults.  Hold on.

---

Posted on **2017-03-26 08:05:46** by **rancher**:

[Maslowcnc k7km defaultsettings](//muut.com/u/maslowcnc/s3/:maslowcnc:81Hh:maslowcnck7kmdefaultsettings.jpg.jpg.jpg)

---

Posted on **2017-03-26 08:11:18** by **rancher**:

My actual settings with 10' crossbar, motors 1' vertically and 1' horizontally from the work surface:

Motor Offset Height in mm: 380

Motor Offset Horizontal in MM: 285

CG: 25 using my cutting board sled

Otherwise I'm using what is in the photo.  Hope that helps.

---

Posted on **2017-03-26 09:09:04** by **boandersen**:

I had a success! 
With the latest firmware and build, I measures my rig and got settings right.. Here is a picture https://goo.gl/photos/ijFQMwqQdrVNaYay6
settings below:
[Maslow Settings]
sledheight = 145
bedheight = 1219.2
openfile = C:\Users\boa\Documents\Sled-QuarterInchBit.nc
motoroffsety = 430
zaxis = False
sledcg = 79
sledwidth = 235
bedwidth = 2438.4
comport = 
motorspacingx = 3017

[Advanced Settings]
gearteeth = 10
zdistperrot = 20
encodersteps = 8148.0
zencodersteps = 8148.0 
chainpitch = 6.35

---

Posted on **2017-03-26 09:27:37** by **Bar**:

Fantastic!

---

Posted on **2017-03-26 09:28:39** by **Bar**:

Thank you so much for testing that. That's going to become the default calculation method, so it's always great to know that it works for someone other than me first.

---

Posted on **2017-03-26 15:54:02** by **boandersen**:

Just a quick follow-up.. the main sled I cut out is a fairly good circle.. I measured the largest diameter to 43.5 cm and the shorter to 42.5

---

Posted on **2017-03-26 16:24:46** by **mindeye**:

I just upgraded both my firmware and GC to latest that includes this change and after decreasing my actual measurement between the motors by -100mm I ended up with a pretty accurate 3" square. Height was dead-on and width was only -1/16" of correct. I still don't really understand why reducing the motors spacing in GC yields more accurate dimensions vertically. I'm reasonably confident my measurements are not off by 4 inches...

Part of the earlier errors I was seeing were due to not using adequate tabs and only doing a single pass. Adding tabs and doing two passes with the first one using an "oversize" bit (actual bit smaller than spec'd in makercam) brought me up from -1/4" to the usable -1/16". It also reduced the number of artifacts in my cut. I still have a few to figure out, seems like sometimes the commands given are executed a split-second early giving rise to slight slants on what should be verticals, though perhaps it's just sled rotation getting worked out. If my work piece were bigger I probably wouldn't even notice.

---

Posted on **2017-03-26 18:20:45** by **davidlang**:

if it is an artifact to the sled swinging, try slowing the feed rate a bit and see if it's better.

---

Posted on **2017-03-26 19:14:32** by **mindeye**:

Seems like a reasonable hypothesis. I'll give it a try tomorrow. If this is the case perhaps it would be useful to throw some slowdowns into the firmware whenever an abrupt directional change happens.

---

Posted on **2017-03-26 22:28:46** by **davidlang**:

It's supposed to have something like that already but slowing everything down will identify if this is the problem or not.

---

