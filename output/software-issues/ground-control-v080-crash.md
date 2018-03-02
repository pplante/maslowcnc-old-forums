## Ground Control v0.80 Crash on Linux
Posted on **2017-07-15 03:20:33** by **jbnimble**:

Uploaded Firmware-0.80 to the Mega, closed PlatformIO, unplugged Mega. 



Installed Kivy per the [Wiki instructions](https://github.com/MaslowCNC/GroundControl/wiki/Linux) for Linux.



Plugged in Mega, verified at /dev/ttyACM0

```

$ dmesg | grep tty

[ 1087.654724] cdc_acm 2-2:1.0: ttyACM0: USB ACM device

```

Ran Ground Control.



```

$ python2.7 main.py

```



Go to Settings, changed port to /dev/ttyACM0, it connects to Mega, then crashes. Opening Ground Control again, it connects, then crashes.



Running Ubuntu

```

$ lsb_release -a 

No LSB modules are available.

Distributor ID:	Ubuntu

Description:	Ubuntu 17.04

Release:	17.04

Codename:	zesty

```



Verified version of pyserial

```

$ pip install pyserial

Requirement already satisfied: pyserial in /usr/lib/python2.7/dist-packages

```



Logs:

```

[INFO   ] Logger: Record log in /home/mymachine/.kivy/logs/kivy_17-07-15_0.txt

[INFO   ] Kivy: v1.10.0

[INFO   ] Python: v2.7.13 (default, Jan 19 2017, 14:48:08) 

[GCC 6.3.0 20170118]

[INFO   ] Factory: 194 symbols loaded

[INFO   ] Image: Providers: img_tex, img_dds, img_sdl2, img_pil, img_gif (img_ffpyplayer ignored)

[INFO   ] OSC: using <multiprocessing> for socket

[INFO   ] Window: Provider: sdl2(['window_egl_rpi'] ignored)

[INFO   ] GL: Using the "OpenGL" graphics system

[INFO   ] GL: Backend used <gl>

[INFO   ] GL: OpenGL version <3.0 Mesa 17.0.3>

[INFO   ] GL: OpenGL vendor <Intel Open Source Technology Center>

[INFO   ] GL: OpenGL renderer <Mesa DRI Intel(R) Haswell Mobile >

[INFO   ] GL: OpenGL parsed version: 3, 0

[INFO   ] GL: Shading version <1.30>

[INFO   ] GL: Texture max size <16384>

[INFO   ] GL: Texture max units <32>

[INFO   ] Window: auto add sdl2 input provider

[INFO   ] Window: virtual keyboard not allowed, single mode, not docked

[INFO   ] Text: Provider: sdl2

[INFO   ] ProbeSysfs: device match: /dev/input/event14

[INFO   ] MTD: Read event from </dev/input/event14>

[INFO   ] Base: Start application main loop

[WARNING] MTD: Unable to open device "/dev/input/event14". Please ensure you have the appropriate permissions.

[INFO   ] GL: NPOT texture support is available

[INFO   ] Base: Leaving application in progress...

[WARNING] stderr: Traceback (most recent call last):

[WARNING] stderr:   File "main.py", line 507, in <module>

[WARNING] stderr:     GroundControlApp().run()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/app.py", line 828, in run

[WARNING] stderr:     runTouchApp()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/base.py", line 504, in runTouchApp

[WARNING] stderr:     EventLoop.window.mainloop()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/core/window/window_sdl2.py", line 663, in mainloop

[WARNING] stderr:     self._mainloop()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/core/window/window_sdl2.py", line 405, in _mainloop

[WARNING] stderr:     EventLoop.idle()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/base.py", line 339, in idle

[WARNING] stderr:     Clock.tick()

[WARNING] stderr:   File "/usr/lib/python2.7/dist-packages/kivy/clock.py", line 581, in tick

[WARNING] stderr:     self._process_events()

[WARNING] stderr:   File "kivy/_clock.pyx", line 367, in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7700)

[WARNING] stderr:   File "kivy/_clock.pyx", line 397, in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7577)

[WARNING] stderr:   File "kivy/_clock.pyx", line 395, in kivy._clock.CyClockBase._process_events (kivy/_clock.c:7498)

[WARNING] stderr:   File "kivy/_clock.pyx", line 167, in kivy._clock.ClockEvent.tick (kivy/_clock.c:3490)

[WARNING] stderr:   File "main.py", line 387, in runPeriodically

[WARNING] stderr:     self.data.logger.writeToLog(message)

[WARNING] stderr:   File "/home/mymachine/Documents/GroundControl-0.80/DataStructures/logger.py ", line 33, in writeToLog

[WARNING] stderr:     self.messageBuffer = self.messageBuffer + message

[WARNING] stderr: UnicodeDecodeError: 'ascii' codec can't decode byte 0xe0 in position 0: ordinal not in range(128)



```

---

Posted on **2017-07-15 03:54:08** by **jbnimble**:

Also tried uploading Firmware-0.80 using Arduino IDE instead of PlatformIO, and no change in Ground Control error.

---

Posted on **2017-07-15 04:06:34** by **jbnimble**:

Got past the error, the problem was needed "sudo"

```

$ sudo python2.7 main.py

```

Why can't permissions be fixed, so that sudo is not required?

---

Posted on **2017-07-15 04:08:06** by **gero**:

Had at least one distro where I had to add myself to the dialout group.

But then the flashing of the Mega already did not work. Just to make sure, can you check if your user shows up with this in a terminal?

getent group dialout

---

Posted on **2017-07-15 04:08:25** by **jbnimble**:

Yes, I have dialout.

```

$ getent group dialout

dialout:x:20:myuser



```

---

Posted on **2017-07-15 04:12:14** by **gero**:

Are you on a laptop with touchpad?

---

Posted on **2017-07-15 04:13:54** by **jbnimble**:

Yes, I am on a laptop with a touchpad. I had to move to an external mouse because the Ground Control "working area" acted like I was dragging it around when I moved the mouse with the touchpad.

---

Posted on **2017-07-15 04:23:13** by **gero**:

Struggling with >>[WARNING] MTD: Unable to open device "/dev/input/event14". Please ensure you have the appropriate << That could be the touchpad. I'm no way an expert, but I would try to add my user to the input group to see if that error goes away.

---

Posted on **2017-07-15 04:35:53** by **jbnimble**:

Added user to "input" group

```

$ usermod -a -G input myuser

```

And now can start Ground Control without "sudo"

---

Posted on **2017-07-15 04:39:24** by **jbnimble**:

Updated Wiki to add usermod command for Linux instructions on Ground Control

---

Posted on **2017-07-15 04:43:50** by **gero**:

My guess is that on older hardware, the touchpad is treated as a mouse. On newer hardware, where you can pinch and stretch to zoom and do other gestures, it is treated as something else. Eventually the linux kernel and the permissions will catch up.

---

Posted on **2017-07-15 04:47:07** by **jbnimble**:

Thanks for your help @gero! Now to go buy the wood and build the frame and sled.

---

Posted on **2017-07-15 04:48:28** by **jbnimble**:

Just noticed that after adding my user to the "input" group I don't get that dragging behavior in Ground Control in the "working area".

---

