## Raspberry Pi 3 setup for Ground Control
Posted on **2016-12-29 08:03:09** by **TheRiflesSpiral**:

I'm documenting my work to get Ground Control working on a Raspberry Pi 3 in this thread. Just getting started so stay tuned.

---

Posted on **2016-12-29 08:04:31** by **TheRiflesSpiral**:

I'm starting with a fresh out-of-the-box RPi 3. The one I bought came with a 4gb SD card with Noobs pre-installed. I've selected the default OS (Raspbian Jessie) and installed.

---

Posted on **2016-12-29 08:37:07** by **TheRiflesSpiral**:

I'm going to do this all from the command line so if you chose to install and go straight to the GUI you can open a terminal window from X.



I chose to install the included Rasbian distro instead of connecting to the internet and installing the newest releases so once the install was done, I had to use the Raspbian package manager (apt-get) to update and upgrade with:

---

>sudo apt-get update

>sudo apt-get upgrade

---

After that, I headed over to Bar's instructions on installing Python in Windows as a guide for setting up the Pi. https://github.com/MaslowCNC/GroundControl



I decided to update the Python package manager (pip) before doing any of the package management in Python with:

---

>sudo python -m pip install --upgrade pip

---

That was a success so on to the installations...

---

Posted on **2016-12-29 08:40:27** by **TheRiflesSpiral**:

The Raspbian package manager apparently also manages some Python packages (not surprising, as the Raspbian distro included the runtime and an IDE for Python out of the box) so when I went to install pyserial with:

---

>python -m pip install pyserial

---

I was happily greeted with "Requirement already satisfied: pyserial in  /usr/lib/python2.7/dist-packages"

---

Posted on **2016-12-29 08:49:15** by **TheRiflesSpiral**:

Time to update wheel and setuptools with:

---

>python -m pip install --upgrade wheel setuptools

---

No issues there so on to some Kivy dependencies...

---

>python -m pip install docutils pygments

---

Here's where I deviated from Bar's instructions since the remaining dependencies are Windows-specific. pypiwin32 is a library that exposes the Win32 API to Python; helpful for all kinds of Windows-specific things like registry editing, etc but irrelevant in a *nix environment.



sdl2 and glew are also in Bar's list of requirements and I suspect they're included as part of the display of cutting paths since they're both meant to work with OpenGL. I'm going to skip those for now and move on to Kivy.

---

Posted on **2016-12-29 09:08:31** by **TheRiflesSpiral**:

The command to install Kivy:

---

>python -m pip install kivy

---

Returned a bevy of dependency issues... so I went on over to the Kivy docs page to find help and: lo and behold! A setup doc! https://kivy.org/docs/installation/installation-rpi.html



Following that to get Kivy installed... Here's the process for Jessie (there are also instructions for Wheezy)



First, the dependencies:

---

>sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \

   pkg-config libgl1-mesa-dev libgles2-mesa-dev \

   python-setuptools libgstreamer1.0-dev git-core \

   gstreamer1.0-plugins-{bad,base,good,ugly} \

   gstreamer1.0-{omx,alsa} python-dev cython

---

That list of dependencies also relies on quite a few other libraries... the install process took a bit of time.



Now on to Kivy itself:

---

>sudo pip install git+https://github.com/kivy/kivy.git@master

---

At this point, the Kivy installer is complaining about the Cython version: "Detected Cython version 0.21.1..." Apparently version 0.23 is required in order for Kivy to compile.

---

Posted on **2016-12-29 09:17:30** by **TheRiflesSpiral**:

I just noticed that the MUUT forum code feature is wrapping lines when it really shouldn't... if you're unfamiliar with terminal commands, note that pressing return (enter) on the keyboard will execute your commands, not wrap to another line...

---

Posted on **2016-12-29 09:25:46** by **TheRiflesSpiral**:

The recommended version of Cython (A Compiler to give Python C capabilities) didn't completely install... the command suggested by the error message when installing Kivy:

---

>sudo pip install -I Cython==0.23

---

Hangs when attempting to build wheel.



Headed over to the Cython docs to see what needs to be done...

---

Posted on **2016-12-29 09:35:11** by **TheRiflesSpiral**:

I just noticed that several sdl libraries are in the list of dependencies for installing Kivy, so that takes care of everything but glew.



>libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

---

Posted on **2016-12-29 10:34:45** by **TheRiflesSpiral**:

Cython is the sticking point at the moment. I've removed the included cython distribution with:

---

>sudo apt-get remove cython

---

And now I'm attempting to install a newer version of Cython with:

---

>sudo pip install -I Cython==0.23

---

It's been chugging away for a bit so I'm going to leave it while. Currently, if I open another terminal session and look at current processes with:

---

>top

---

I see a root process consuming 99%+ of CPU and 20%+ of memory and the command keeps updating (currently "ccl") so I have to think it's doing something productive!

---

Posted on **2016-12-29 11:16:51** by **TheRiflesSpiral**:

That did the trick with regards to Cython. (removing then installing)



I suspect 2 things:

1) the initial attempt at installing 0.23 would have been successful had I simply been more patient and

2) this is an illustration of the somewhat limited nature of the ARM processor with regards to compile speed. I'm so used to compiling on i7 processors (both Win and Mac) that I wasn't expecting such a long install time.



Time to install Kivy now with:

---

>sudo pip install git+https://github.com/kivy/kivy.git@master

---

Which is going to necessitate several re-compiles so I expect it to take a while as well.

---

Posted on **2016-12-29 11:39:46** by **TomTheWhittler**:

Maybe once you have it done you can make a SD image and post it somewhere. That could save a bunch of time for everyone.

---

Posted on **2016-12-29 11:54:53** by **TheRiflesSpiral**:

I'd be happy to... it would be limited to use on the RPi 3 but I think that's the one everyone wants to get their hands on anyway. :)

---

Posted on **2016-12-29 12:28:24** by **TheRiflesSpiral**:

Okay, Kivy is working properly... or at least the demos are working fine.



The next step is to get GroundControl from the repository with:

---

>sudo git clone https://github.com/MaslowCNC/GroundControl.git

---

Then finally run the software with:

---

>cd /GroundControl/

>python cncgc.py

---

I'm getting a full-screen app popping up now that looks like the screenshots I've seen but there's no mouse cursor and it appears as if none of the keyboard commands are making it to the app.



When I start, I get several "INFO," "WARNING" and "CRITICAL" messages so I'm going to dig through those for clues.

---

Posted on **2016-12-29 13:12:15** by **TheRiflesSpiral**:

I forgot about glew not being installed in the kivy dependencies  step. So off to the glew sourceforge repository for installation instructions. http://glew.sourceforge.net/index.html



You have to first make the descriptor files from the OpenGL registry then build and install glew afterwards, then reboot:

---

>sudo git clone https://github.com/nigels-com/glew.git glew

>cd /glew/config/

>sudo make all

>cd ..

>sudo make all

>sudo install.all

>sudo reboot

---

With glew installed I'm still not getting a mouse cursor or keyboard response and the warnings are the same. I'll post the warnings below.

---

Posted on **2016-12-29 13:16:00** by **TheRiflesSpiral**:

Hoping Bar can chime in here with some insight as I'm stuck at this point...



---

 $ sudo python cncgc.py

[INFO   ] [Logger      ] Record log in /root/.kivy/logs/kivy_16-12-29_1.txt

[INFO   ] [Kivy        ] v1.9.2-dev0

[INFO   ] [Python      ] v2.7.9 (default, Sep 17 2016, 20:26:04)

[GCC 4.9.2]

[INFO   ] [Factory     ] 193 symbols loaded

[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_pil, img_gif (img_ffpyplayer ignored)

[INFO   ] [Window      ] Provider: egl_rpi

[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system

[INFO   ] [GL          ] Backend used <gl>

[INFO   ] [GL          ] OpenGL version <OpenGL ES 2.0>

[INFO   ] [GL          ] OpenGL vendor <Broadcom>

[INFO   ] [GL          ] OpenGL renderer <VideoCore IV HW>

[INFO   ] [GL          ] OpenGL parsed version: 2, 0

[INFO   ] [GL          ] Shading version <OpenGL ES GLSL ES 1.00>

[INFO   ] [GL          ] Texture max size <2048>

[INFO   ] [GL          ] Texture max units <8>

[INFO   ] [Shader      ] fragment shader: <Compiled> 

[INFO   ] [Shader      ] vertex shader: <Compiled>

[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked

[INFO   ] [Text        ] Provider: sdl2

[WARNING] [Window      ] maximize() is not implemented in the current window provider.

Unable to init server: Could not connect: Connection refused

Unable to init server: Could not connect: Connection refused



(cncgc.py:1012): Gtk-CRITICAL **: gtk_clipboard_get_for_display: assertion 'display != NULL' failed

[INFO   ] [Clipboard   ] Provider: gtk3(['clipboard_dbusklipper'] ignored)

[CRITICAL] [Cutbuffer   ] Unable to find any valuable Cutbuffer provider.

xclip - OSError: [Errno 2] No such file or directory

  File "/usr/local/lib/python2.7/dist-packages/kivy/core/__init__.py", line 59, in core_select_lib

    fromlist=[modulename], level=0)

  File "/usr/local/lib/python2.7/dist-packages/kivy/core/clipboard/clipboard_ xclip.py", line 17, in <module>

    p = subprocess.Popen(['xclip', '-version'], stdout=subprocess.PIPE)

  File "/usr/lib/python2.7/subprocess.py", line 710, in __init__

    errread, errwrite)

  File "/usr/lib/python2.7/subprocess.py", line 1335, in _execute_child

    raise child_exception



xsel - OSError: [Errno 2] No such file or directory

  File "/usr/local/lib/python2.7/dist-packages/kivy/core/__init__.py", line 59, in core_select_lib

    fromlist=[modulename], level=0)

  File "/usr/local/lib/python2.7/dist-packages/kivy/core/clipboard/clipboard_ xsel.py", line 16, in <module>

    p = subprocess.Popen(['xsel'], stdout=subprocess.PIPE)

  File "/usr/lib/python2.7/subprocess.py", line 710, in __init__

    errread, errwrite)

  File "/usr/lib/python2.7/subprocess.py", line 1335, in _execute_child

    raise child_exception



[INFO   ] [GL          ] NPOT texture support is available

Cannot reopen gcode file. It may have been moved or deleted. To locate it or open a different file use File > Open G-code

[INFO   ] [OSC         ] using <multiprocessing> for socket

[INFO   ] [ProbeSysfs  ] device match: /dev/input/event0

[INFO   ] [HIDInput    ] Read event from </dev/input/event0>

[INFO   ] [ProbeSysfs  ] device match: /dev/input/event1

[INFO   ] [HIDInput    ] Read event from </dev/input/event1>

[INFO   ] [Base        ] Start application main loop

[INFO   ] [HIDMotionEvent] using <Microsoft  Microsoft Basic Optical Mouse v2.0 >

[INFO   ] [HIDMotionEvent] using <CHICONY USB NetVista Full Width Keyboard>

[INFO   ] [Base        ] Leaving application in progress...

 Traceback (most recent call last):

   File "cncgc.py", line 232, in <module>

     GroundControlApp().run()

   File "/usr/local/lib/python2.7/dist-packages/kivy/app.py", line 828, in run

     runTouchApp()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 504, in runTouchApp

     EventLoop.window.mainloop()

   File "/usr/local/lib/python2.7/dist-packages/kivy/core/window/window_egl_rp i.py", line 90, in mainloop

     self._mainloop()

   File "/usr/local/lib/python2.7/dist-packages/kivy/core/window/window_egl_rp i.py", line 85, in _mainloop

     EventLoop.idle()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 342, in idle

     self.dispatch_input()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 316, in dispatch_input

     provider.update(dispatch_fn=self._dispatch_input)

   File "/usr/local/lib/python2.7/dist-packages/kivy/input/providers/hidinput. py", line 708, in update

     Window.dispatch('on_keyboard', *args)

   File "kivy/_event.pyx", line 714, in kivy._event.EventDispatcher.dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:7681)

   File "kivy/_event.pyx", line 1225, in kivy._event.EventObservers.dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:13524)

   File "kivy/_event.pyx", line 1149, in kivy._event.EventObservers._dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:13050)

   File "/usr/local/lib/python2.7/dist-packages/kivy/app.py", line 1038, in _on_keyboard_settings

     return self.close_settings()

 TypeError: close_settings() takes exactly 2 arguments (1 given)



---

---

Posted on **2016-12-29 13:34:07** by **TheRiflesSpiral**:

Running through these error messages:



The xclip and xsel errors for /usr/local/lib/python2.7/dist-packages/kivy/core/__init__.py don't make much sense since the file does exist. /usr/lib/python2.7/subprocess.py also exists but perhaps has a permissions issue? (both read and write errors) I'm not sure what the "child_exception" error is and I can't find it in any of the .py source code so it must be specific to xclip and xsel.

---

Posted on **2016-12-29 13:37:11** by **TheRiflesSpiral**:

Okay, fixed those... it turns out that xsel and xclip are left out of the dependencies list for kivy even though they're required. Okay... so:

---

>sudo apt-get install xsel xclip

---

Sorts that bit out.

---

Posted on **2016-12-29 13:41:43** by **TheRiflesSpiral**:

Okay so I'm only getting one warning now, but I'm still not seeing any mouse cursor and keyboard commands aren't making it to the app. (I don't think)



---

$ sudo python cncgc.py

[INFO   ] [Logger      ] Record log in /root/.kivy/logs/kivy_16-12-29_2.txt

[INFO   ] [Kivy        ] v1.9.2-dev0

[INFO   ] [Python      ] v2.7.9 (default, Sep 17 2016, 20:26:04)

[GCC 4.9.2]

[INFO   ] [Factory     ] 193 symbols loaded

[INFO   ] [Image       ] Providers: img_tex, img_dds, img_sdl2, img_pil, img_gif                                                             (img_ffpyplayer ignored)

[INFO   ] [Window      ] Provider: egl_rpi

[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system

[INFO   ] [GL          ] Backend used <gl>

[INFO   ] [GL          ] OpenGL version <OpenGL ES 2.0>

[INFO   ] [GL          ] OpenGL vendor <Broadcom>

[INFO   ] [GL          ] OpenGL renderer <VideoCore IV HW>

[INFO   ] [GL          ] OpenGL parsed version: 2, 0

[INFO   ] [GL          ] Shading version <OpenGL ES GLSL ES 1.00>

[INFO   ] [GL          ] Texture max size <2048>

[INFO   ] [GL          ]  Texture max units <8>

[INFO   ] [Shader      ] fragment shader: <Compiled>

[INFO   ] [Shader      ] vertex shader: <Compiled>

[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked

[INFO   ] [Text        ] Provider: sdl2

[WARNING] [Window      ] maximize() is not implemented in the current window pro                                                            vider.

Unable to init server: Could not connect: Connection refused

Unable to init server: Could not connect: Connection refused



(cncgc.py:2573): Gtk-CRITICAL **: gtk_clipboard_get_for_display: assertion 'disp                                                            lay != NULL' failed

[INFO   ] [Clipboard   ] Provider: gtk3(['clipboard_dbusklipper'] ignored)

xclip version 0.12

Copyright (C) 2001-2008 Kim Saunders et al.

Distributed under the terms of the GNU GPL

[INFO   ] [Cutbuffer   ] Provider: xclip

[INFO   ] [CutBuffer   ] cut buffer support enabled

[INFO   ] [GL          ] NPOT texture support is available

Cannot reopen gcode file. It may have been moved or deleted. To locate it or ope                                                            n a different file use File > Open G-code

[INFO   ] [OSC         ] using <multiprocessing> for socket

[INFO   ] [ProbeSysfs  ] device match: /dev/input/event0

[INFO   ] [HIDInput    ] Read event from </dev/input/event0>

[INFO   ] [ProbeSysfs  ] device match: /dev/input/event1

[INFO   ] [HIDInput    ] Read event from </dev/input/event1>

[INFO   ] [Base        ] Start application main loop

[INFO   ] [HIDMotionEvent] using <Microsoft  Microsoft Basic Optical Mouse v2.0                                                             >

[INFO   ] [HIDMotionEvent] using <CHICONY USB NetVista Full Width Keyboard>

---

---

Posted on **2016-12-29 13:58:13** by **TheRiflesSpiral**:

A little progress... apparently keyboard commands are making it to the app. Pressing F1 gives me a different window "Makesmith Settings" but I can't find a keypress to exit that screen gracefully. (Both F1 and Esc kill the app):

---

[INFO   ] [Base        ] Leaving application in progress...

 Traceback (most recent call last):

   File "cncgc.py", line 232, in <module>

     GroundControlApp().run()

   File "/usr/local/lib/python2.7/dist-packages/kivy/app.py", line 828, in run

     runTouchApp()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 504, in runTouchApp

     EventLoop.window.mainloop()

   File "/usr/local/lib/python2.7/dist-packages/kivy/core/window/window_egl_rp i.py", line 90, in mainloop

     self._mainloop()

   File "/usr/local/lib/python2.7/dist-packages/kivy/core/window/window_egl_rp i.py", line 85, in _mainloop

     EventLoop.idle()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 342, in idle

     self.dispatch_input()

   File "/usr/local/lib/python2.7/dist-packages/kivy/base.py", line 316, in dispatch_input

     prov ider.update(dispatch_fn=self._dispatch_input)

   File "/usr/local/lib/python2.7/dist-packages/kivy/input/providers/hidinput. py", line 708, in update

     Window.dispatch('on_keyboard', *args)

   File "kivy/_event.pyx", line 714, in kivy._event.EventDispatcher.dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:7681)

   File "kivy/_event.pyx", line 1225, in kivy._event.EventObservers.dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:13524)

   File "kivy/_event.pyx", line 1149, in kivy._event.EventObservers._dispatch (/tmp/pip-aekAnD-build/kivy/_event.c:13050)

   File "/usr/local/lib/python2.7/dist-packages/kivy/app.py", line 1035, in _on_keyboard_settings

     self.close_settings()

 TypeError: close_settings() takes exactly 2 arguments (1 given)

---



Also, pressing the Control key on the keyboard locks the app with a different trace:

---

 Exception in thread Thread-2:

 Traceback (most recent call last):

   File "/usr/lib/python2.7/threading.py", line 810, in __bootstrap_inner

     self.run()

   File "/usr/lib/python2.7/threading.py", line 763, in run

     self.__target(*self.__args, **self.__kwargs)

   File "/usr/local/lib/python2.7/dist-packages/kivy/input/providers/hidinput. py", line 697, in _thread_run

     process_as_mouse_or_keyboard(*infos)

   File "/usr/local/lib/python2.7/dist-packages/kivy/input/providers/hidinput. py", line 553, in process_as_mouse_or_keyboard

     Keyboard.keycodes[z.lower()], ev_code,

 KeyError: 'ctrl'

---



I wouldn't be surprised if both of these are related to the window provider error. I'll dig into that next.

---

Posted on **2016-12-29 14:44:44** by **TheRiflesSpiral**:

The issue with the crash when pressing the ctrl key is a known issue with Kivy: https://github.com/kivy/kivy/issues/4007 It appears to stem from the fact that the keyboard provider for RPi does not differentiate between lctrl or rctrl and instead sends an unknown "ctrl" identifier.



This could be remedied in the kivy input provider hidinput.py and then re-build from the source.



Not sure if Ctrl is used in GroundControl but that might be an issue.

---

Posted on **2016-12-29 14:57:06** by **TheRiflesSpiral**:

Last update for today then I'm going to pick it up tomorrow:



There is *some* response from the mouse; still no cursor or indicator at all of the mouse position, but when I click and drag, the stage moves. (The dotted box/crosshairs and circle/x)



I think the issue is just that the mouse cursor itself isn't visible... if I start the app, slowly moving my mouse straight up and clicking ever few mm, I can eventually get the Makesmith Settings screen to come up.



I also managed just now to dive into the Kivy setting screen from the settings screen. "Mouse cursor" is on. I managed to guess my way over to that toggle switch and switched it off/on in hopes that would kick the cursor into visibility but no.

---

Posted on **2016-12-29 16:52:42** by **TheRiflesSpiral**:

Okay so I just realized I'm a complete idiot. It occurred to me on the way home that since Kivy is a TOUCH interface for Python, it's not intended to have a visible cursor.



I've found a few suggestions for modifying the ~/.kivy/config.ini file to let touchring display the cursor so I'll try that tomorrow.



That won't work, however, if the GroundControl code explicitly hides the cursor so I'll dig into that tomorrow as well.



Suffice it to say that having a visible cursor is pretty important if you're going to be doing any development or actual use with a system that doesn't have a touch screen. I'd have to say that's likely to be the norm. (Keyboard/mouse interaction) so I'm in favor of allowing the cursor to show.

---

Posted on **2016-12-29 18:54:47** by **Bar**:

This is great. I haven't explicitly hid the cursor or explicitly displayed it, I believe that behavior is handled by kivy. When I run GC on my laptop I can see the cursor, but when I run it on a tablet, no cursor is displayed and it is a touch only interface.



I agree with you that allowing the cursor to show is important. I'll look into how Kivy handles this more.

---

Posted on **2016-12-29 19:46:18** by **TheRiflesSpiral**:

Good to know. I'll slay that beast tomorrow, hopefully, and post a doc with step-by-step commands for getting GroundControl on PI.



Any thoughts about the window provider error? I started researching that but didn't get very far.

---

Posted on **2016-12-30 06:16:37** by **TheRiflesSpiral**:

Good morning! Back to it with some research I did last night. The error:

---

(cncgc.py:1012): Gtk-CRITICAL **: gtk_clipboard_get_for_display: assertion 'display != NULL' failed

---

Is solved by running the X server (GUI) and launching GroundControl from a terminal window. The X server needs to be running and is required by xclip.



So if you're in the GUI, you wouldn't receive this error but if you're working from the command line as I am, you simply start the GUI with:

---

>startx

---

And then click on the computer monitor in the toolbar at the top. (Terminal). Issue your commands from there to start GroundControl.



I'm still getting a warning about the maximize() function not being supported in the window provider so I'm going to work on that one next.

---

Posted on **2016-12-30 06:45:49** by **TheRiflesSpiral**:

As best I can tell the concept of "Maximize" doesn't exist in python on Raspbian. You can set an app to "fullscreen" (hiding the title bar) or set a window's "zoomed" attribute to true or simply set the dimensions of the window to match the screen but this appears to be troublesome in some situations.



To remedy this particular error, I commented line 70: "Window.maximize()" in cncgc.py.

---

def build(self):

    '''

    Window.maximize()

    '''



    interface           =  FloatLayout()...

---

And the error goes away. The app still launches fullscreen.

---

Posted on **2016-12-30 07:54:10** by **TheRiflesSpiral**:

Regarding the mouse cursor: all the information I can find (from at least 2 years ago) is that the Touchring module for Kivy should be able to handle this. Touchring is the module that puts a ring around the location(s) where touches are detected but can also display the cursor. I've tried this but with no effect. The process is to edit the config.ini file in the hidden .kivy directory of the user:

---

>sudo nano ~/.kivy/config.ini

---

Then in the empty [modules] section, add the following:

---

[modules]

touchring = show_cursor=true

---

I was editing the default (~) user's config.ini (pi) but realized that I was usually running python with root privileges so I also edited /root/.kivy/config.ini but with no effect.



I'm digging into touchring a bit now, it appears that you might have to specify an image as a widget to use as the mouse cursor.

---

Posted on **2016-12-30 08:32:57** by **TheRiflesSpiral**:

Making progres... the default image to display for the cursor (a ring) is usually found at <kivy>/data/images/ring.png but in my install that image isn't present. In that directory is an image called "cursor.png" that looks like a white mouse cursor.



Updating the kivy config.ini file as follows actually accomplishes the task touchring was designed for: when you click, the mouse cursor briefly appears where you clicked!



So once again, update the config file with:

---

>sudo nano ~/.kivy/config.ini

---

And update the modules section, adding the following:

---

[modules]

touchring = show_cursor=1,image=/usr/local/lib/python2.7/dist-packages/kivy/data/i mages/cursor.png,scale=1,alpha=1

---

---

Posted on **2016-12-30 09:07:44** by **TheRiflesSpiral**:

I got tired of typing paths over and over so I did some housekeeping on my system... just putting this here to help anyone who hates typing stuff over and over as much as I do!



First, add the location of cncgc.py to your $PATH variable by adding it to ~/.profile

---

>sudo nano ~/.profile

---

Then:

---

...

PATH=$PATH:/usr/local/lib/python2.7/dist-packages/kivy/GroundControl

---

Next, edit cncgc.py with the shebang necessary to find Python when executed; you first have to find the location of Python:

---

> which python2

---

This should return something like "/usr/bin/python2". Whatever this is, that's what you'll add to cncgc.py:

---

>sudo nano /usr/local/lib/python2.7/dist-packages/kivy/GroundControl/cncgc.py

---

And add that path to the very top, preceded by #!

---

#! /usr/bin/python2

'''



Kivy Imports...

---

Since the Python scripts for Ground Control were written in a Windows environment the line breaks are funky... you can easily fix this with the fromdos command in the tofrodos package. If you don't have it, install it...

---

>sudo apt-get update

>sudo apt-get upgra de

>sudo apt-get tofrodos

---

Then "fix" the script with

---

>sudo fromdos /usr/local/lib/python2.7/dist-packages/kivy/GroundControl/cncgc.py

---

And finally, "bless" the script with the executable switch:

---

>sudo chmod +x /usr/local/lib/python2.7/dist-packages/kivy/GroundControl/cncgc.py

---

Whew!



Now I can launch Ground Control from any directory by simply typing:

---

>cncgc.py

---

---

Posted on **2016-12-30 09:49:04** by **TheRiflesSpiral**:

This mouse thing has me stumped. I can get the cursor to show up and move around if I hold a mouse button down. That at least lets me go off-screen, hold a button down and then drag to the area of the screen I want to click then release and click. Not ideal.



I've posted to the Kivy Google users group to see if there's any insight in that group.



At this point it will work with a touch-screen of your choosing but I want to work out this mouse thing before I publish any kind of setup guide.



I'll check in once I've heard from the Kivy folks.

---

Posted on **2017-01-02 05:28:37** by **TomTheWhittler**:

Does this help ?

http://stackoverflow.com/questions/34662672/kivy-python-mouse-position

---

Posted on **2017-01-02 05:32:36** by **TomTheWhittler**:

or this

https://www.reddit.com/r/raspberry_pi/comments/2mzw22/fixed_configuring_kivy_on_the_raspberry_pi_to/

---

Posted on **2017-01-02 05:59:56** by **TheRiflesSpiral**:

Hi, Tom. Thanks for those. The reddit thread is what pointed me to the config file in the first place but I missed the OpenGLES mention since I had just configured GLEW. It's possible that I need to install that package as well.



I'm off today but I'll check it out tomorrow.

---

Posted on **2017-01-03 13:22:59** by **TheRiflesSpiral**:

Happy New Year to everyone! I'm back at it this evening but unfortunately no love from the OpenGLES library; it's installed as part of the Raspbian image and it's up-to-date. I'm going to check into DispmanX mentioned by Jessica. I'm wondering if the gui isn't interfering with the mouse display, perhaps showing it underneath the ground control window or what...

---

Posted on **2017-01-03 14:07:00** by **TheRiflesSpiral**:

After some troubleshooting I'm now of the opinion that the GUI is not to blame for obscuring the cursor. I managed to start the Xserver without loading the GUI by setting up a config file for X that simply launches a terminal window and keyboard/mouse support:

---

>sudo nano ~/.xinitrc

---

Then:

---

#!/bin/sh



lxterminal

---

When running startx (which usually launches the GUI):

---

>startx

---

I get a terminal window and mouse cursor. Starting cncgc.py from that terminal (where an Xserver is already started) I get no mouse cursor and the Touchring config isn't functioning either. (No cursor at all... not even on mouse-down)



This has to be a Kivy issue and I've not got any feedback from them yet. I'll post over at the Raspberry forums too, to see if anyone has any clues.



As a last-ditch effort, I'm going to dig into the touchring.py script to see how mouse movement is handled. Perhaps a customized touchring script will do the job?



I also wanted to reiterate that  what I've done thus far SHOULD WORK for a touchscreen setup... there's no reason to avoid a Raspberry Pi as a control device right now.

---

Posted on **2017-01-21 07:13:53** by **paulhart**:

This might be a silly question given your last sentence above, but do you think everything would be okay if you were to use a touchscreen with the Pi? I'm thinking specifically of the official display, which is $60 from MCM:



http://www.mcmelectronics.com/product/83-16872



Admittedly this is only an 800x480 display, which some folks may not appreciate, but it's a possible start.

---

Posted on **2017-01-22 11:57:28** by **TheRiflesSpiral**:

Yes, I don't see any reason it wouldn't work, provided your display plays nice with Kivy. I've just about given up getting any help from the Kivy users group and when I get a moment, I'm going to see about a custom function in the touchring module to do cursor tracking.



In the meantime I'll put a more concise guide together for the RPi that others can build on when they get their touchscreens.

---

Posted on **2017-03-06 12:38:38** by **Bar**:

I got a build up and running using Kivy Pi (http://kivypie.mitako.eu/) which shows the mouse cursor, and supports multi-touch screens (only tested on the official Pi touch screen so far).



I want to make a .dmg file to share the image with everyone, but I can't figure out how to make one. Does anyone know? Sorry if this is a dumb question, this is my first time playing with the Pi.

---

Posted on **2017-03-06 13:01:08** by **TheRiflesSpiral**:

You can use Win32DiskImager and a card reader to make a disk image on Windows. The only issue is that the image will be as big as the card you're using. (A 16GB card will make a 16GB .dmg file :O )

---

Posted on **2017-03-06 13:02:47** by **TheRiflesSpiral**:

The file system on Pi is FAT32 so you can use any imaging tool, really, and get a .dmg file.

---

Posted on **2017-03-06 13:09:05** by **TheRiflesSpiral**:

We're using an RPi3B as a wireless AirPrint server on our photo booth product and the two pieces of software I use are Win32DiskImager and SDFormatter.

---

Process for Making a Disk Image

1) Shut down RPi and pull the power

2) Pull the SD card and put it in the card reader

3) In Win32DiskImager, choose the card reader as the device and click "Read" (you may have to specify a save name/location)



Process for writing a Disk Image

1) Put new SD card in card reader

2) In SDFormatter, Click "Format" (Quick format is okay)

3) In Win32DiskImager, choose card reader as the device. Load the disk image and click "Write"

---

Posted on **2017-03-06 13:15:24** by **TheRiflesSpiral**:

Actually, it looks like pipaOS uses ext4 non-journal file system... Not sure how Win32DiskImager will handle that. Definitely want to go through a read/write test.

---

Posted on **2017-03-06 13:32:58** by **Bar**:

Do you know if there is any way to make it smaller than the SD card? My SD card is 64GB but my laptop HD is only 40GB :-(

---

Posted on **2017-03-06 13:56:16** by **TomTheWhittler**:

You could go out and buy a 128gb USB flash drive from WallyWorld for $ 35.00 and create the image on that. After the image is created you can try to zip it to try to make it smaller. Best Buy has a 256gb one for $ 55.00

---

Posted on **2017-03-06 14:07:04** by **scottsm**:

I've used Clonezilla for this sort of thing.

---

Posted on **2017-03-06 14:08:14** by **Bar**:

That is not a bad idea. If I understand correctly making an image of my 64GB sd card the image will only work for other people who also have a 64GB SD card, right?

---

Posted on **2017-03-06 14:11:26** by **Bar**:

Clonezilla looks like it might be what I need, thanks for the tip!

---

Posted on **2017-03-06 14:28:10** by **davidlang**:

Yes, an image from a 64G card will not fit on a smaller card



if you make the image available to me, I can do the work to shrink it down.



I can also define packages so that the software (and it's dependencies) can be installed on any raspian/debian/ubuntu system through the package manager (this is the type of things I do in my day job)

---

Posted on **2017-03-06 14:36:11** by **traviscadden**:

@davidlang - I would be forever in your debt if you could do this! I really want to use a Pi3 as my host for Maslow (And a 3d printer to be determined later)

---

Posted on **2017-03-06 14:53:26** by **TheRiflesSpiral**:

I'm going to suggest a different approach:



pipaOS is purposefully a tiny, limited feature OS designed to fit on tiny cards. KivyPi is also a relatively svelte distro and I'm guessing a fully functional Maslow touchscreen front-end would fit on a 2GB card.



Bar if you didn't mind re-doing the work on a smaller card (maybe a 2GB card if you can find one) and make an image of that, it would solve all the issues above.

---

Posted on **2017-03-06 18:08:17** by **davidlang**:

It's far better to support a general OS (or several) than have an OS image only for the maslow. it gets ugly when you need one OS image to run your CAD program, one to run your conversion program, and one to run the machine, there's no reason to require a dedicated OS image for a purpose (it's useful to provide such an image, but that should be only in addition to the main image)



@bar, if you can find a way to get me the image, I'll do the work.

---

Posted on **2017-03-06 18:19:36** by **Bar**:

Great point. I ordered a small SD card so I should be able to get a small image to you guys soon.



I agree that having a general support is always better. I really struggled to get Kivy to play nice on the main raspberry pi distro, but like I said it was my first time playing with one so I may have struggled even if it was pretty straight forward.

---

Posted on **2017-03-06 23:40:14** by **davidlang**:

As I say, this is the sort of thing I do all the time, I'll be happy to help

---

