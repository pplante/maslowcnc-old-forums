## [CRITICAL          ] GL: Minimum required OpenGL version (2.0) NOT found!
Posted on **2017-05-18 14:21:16** by **digital_janitor**:

Ground control errors out with [CRITICAL          ] GL: Minimum required OpenGL version (2.0) NOT found!
I saw a couple posts regarding opengl 2 and older hardware.   I don't think this pertains precisely to the previous thread, so I am starting a new one.  Windows 10 fresh install, i5-2430, intel 3000.  Installed drivers directly from MS.  Ran GLview, verified opengl 3.1 support is being provided by driver.  I also ran across this 
https://github.com/kivy/kivy/issues/3576
added Config.set('graphics', 'multisamples', '0') to main.py, didn't seem to make a difference, though I may not understand where that should be placed.

Any help would be appreciated.  Full log below

[INFO              ] Logger: Record log in C:\Users\gateway\.kivy\logs\kivy_17-05-18_6.txt
[INFO              ] Kivy: v1.9.1
[INFO              ] Python: v2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)]
[INFO              ] Factory: 179 symbols loaded
[INFO              ] Image: Providers: img_tex, img_dds, img_gif, img_sdl2 (img_pil, img_ffpyplayer ignored)
[INFO               ] OSC: using <thread> for socket
[INFO              ] Window: Provider: sdl2
[INFO              ] GL: GLEW initialization succeeded
[INFO              ] GL: OpenGL version <1.1.0>
[INFO              ] GL: OpenGL vendor <Microsoft Corporation>
[INFO              ] GL: OpenGL renderer <GDI Generic>
[INFO              ] GL: OpenGL parsed version: 1, 1
[CRITICAL          ] GL: Minimum required OpenGL version (2.0) NOT found!

OpenGL version detected: 1.1

Version: 1.1.0
Vendor: Microsoft Corporation
Renderer: GDI Generic

Try upgrading your graphics drivers and/or your graphics hardware in case of problems.

The application will leave now.

---

Posted on **2017-05-18 14:55:50** by **digital_janitor**:

As an aside, I was able to run it successfully from the source code, just the prepackaged that didn't work.

---

Posted on **2017-05-29 17:37:18** by **mikeberg**:

I bought one pc( Intel duo core 2) just for my maslow and I have the same problem with open gl compatibility and I run it from source code nothing change in my screen and it close

---

Posted on **2017-05-29 23:13:02** by **gero**:

Did you try installing the driver from the manufacturer and adding the lines in config.set https://stackoverflow.com/questions/34969990/kivy-does-not-detect-opengl-2-0

---

Posted on **2017-05-30 15:07:29** by **mikeberg**:

I make a try tonight

---

Posted on **2017-06-06 12:18:48** by **aktroy**:

Could you possibly describe in more details how to insert these couple of lines of code? I have zero programming experience and have no idea of how to edit the code.

---

Posted on **2017-06-06 17:15:38** by **mikeberg**:

I have all my answers to my problem! 😁 in the past I thinked Intel driver manager have searched in my pc for all because I have no other graphic card it simply onboard the mother board . after updating with this program I'm still getting the same problem with open gl 2.0 not found....now all I have do is right click on the desktop and advance option to know more about my chipset on my graphic card.I searched for drivers on Intel website and the Intel driver utility did not install graphic driver all my problem come there. I install it manually, now I'm happy to say to you, maslow will cutting wood

---

Posted on **2017-06-06 17:20:05** by **scottsm**:

That's great news! We all learned more about making this run. Thanks for sharing the solution :)

---

Posted on **2017-06-06 17:28:38** by **mikeberg**:

I read I many forum that windows updater update opengl driver but in my case it doesn't do anything to help open gl... Intel graphic acceleration is necessary to get 2.1 gl

---

