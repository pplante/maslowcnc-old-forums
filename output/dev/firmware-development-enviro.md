## Firmware Development Environment
Posted on **2017-01-19 22:52:24** by **jbnimble**:

Pulled down the [Firmware](https://github.com/MaslowCNC/Firmware) repository, and installed Arduino IDE (v2:1.0.5+dfsg2-4), because I saw the cnc_ctrl_v1.ino file, opened that file in the IDE, and tried to "Verify/Compile" and it failed with this error:

--
In file included from CNC_Functions.h:20:0,
                 from cnc_ctrl_v1.ino:16:
Axis.h:24:24: fatal error: EEPROM.h: No such file or directory
     #include <EEPROM.h>
                        ^
compilation terminated.
--
I tried searching for how to fix this error, and no answer so far other than possibly "[including the dependencies in the sketch rather than the library](http://forum.arduino.cc/index.php/topic,46552.0.html)"

It has been a while since I messed with the Arduino IDE, and I forgot how much I loathed it. Might try one of the many alternatives, but would like to know what is currently being used to develop the firmware.

What are you using to develop the Firmware code, and how do I get it setup so that I can compile?

---

Posted on **2017-01-20 05:44:54** by **scottsm**:

I just confirmed that it will compile using the current version (1.8.1) of the IDE. There have been many changes/improvements to the IDE since v2:1.0.5. One change was to roll EEPROM.h and other common libraries into the core. They seem to release new versions almost monthly. Their policy of making older versions is admirable, but sometimes confusing.

---

Posted on **2017-01-20 06:51:48** by **jbnimble**:

@scottsm, thanks I installed 1.8.1 and got past the EEPROM error, now it complains about "Error compiling for board Arduino/Genuino Uno.", which board should I be targeting?

I was previously using the version that was part of "apt install" for my distribution, I guess they are not up to date.

---

Posted on **2017-01-20 07:35:49** by **scottsm**:

I think Maslow uses the Mega; I had success using Arduino/Genuino Mega.

---

Posted on **2017-01-20 07:38:19** by **jbnimble**:

Yep, just figured that out, I changed the Arduino IDE to use board "Arduino/Genuino Mega or Mega 2560" and the Firmware compiled, thanks for your help!

---

Posted on **2017-01-20 09:22:00** by **jbnimble**:

I created a [Wiki page](https://github.com/jbnimble/Firmware/wiki/Development-Environment) to describe the steps for setting up the Arduino IDE for the Firmware repository, but it appears that pull requests on Wiki pages is not a thing.

@Bar, if you want to add the wiki page I created to the main repository, then please do. I wish it was part of the pull request system so it can be tracked. Maybe it might be better to forego the Wiki pages and add a "Documentation" directory in the repository with mark down pages, so that related documentation can be tracked, thoughts?

I have also seen repositories that just have a huge readme.md with all the repositories documentation, which could also be tracked, and an alternative to GitHub wiki pages.

Essentially I am looking for a place where I can create missing documentation that is tracked in the repository, if someone could make a decision on how that works I would be happy to contribute.

---

Posted on **2017-01-20 09:59:30** by **Bar**:

That's a real bummer that GitHub doesn't support pull requests against the wiki pages. From doing a bit of reading, it looks possible to treat the wiki pages as a separate repository and target them that way, but it looks complicated and I'm afraid that if we set it up like that it will be too difficult to contribute. 

My vote is to put the documentation front and center in the README. I don't imagine the program ever becoming so complex that it can't be accurately summarized there. 

If you make a PR to add that information to the README, I will merge it right away. Beautiful work.

---

Posted on **2017-01-20 12:09:51** by **davidlang**:

There are a number of projects that make the docs a separate repo from the code. This helps in that people are less intimidated by making a change/pull request for docs than for 'code'

---

Posted on **2017-01-20 13:29:38** by **jbnimble**:

@Bar, added a new pull request, also figured out how to setup PlatformIO for the Firmware repository, pretty simple, and Atom is a nice editor, lots of plugins, and things just seem to work out of the box. 

Unlike Eclipse and the Sloeber plugin, things were not working very well for existing projects that were not created inside Eclipse.

---

