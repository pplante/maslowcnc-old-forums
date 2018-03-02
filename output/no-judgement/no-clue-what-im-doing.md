## No clue what I'm doing
Posted on **2017-03-25 18:38:57** by **fsubigturk**:

so I downloaded the python 2.7.13 and when I try to run it and I type the python --version I get some error code and a trace back and that the name python does not exist.  I feel like I'm way over my head and not sure what to do. Am I in the wrong command prompt area?

---

Posted on **2017-03-25 18:49:23** by **boandersen**:

No, you probably just need to add a path to the python file location - its probably c:\python27\



.. or change to that directory first and execute from there

---

Posted on **2017-03-25 18:51:21** by **fsubigturk**:

where do I type the c:\python27\? Also if its not in python where do I go.  I have very little computer knowlegde

---

Posted on **2017-03-25 18:52:03** by **fsubigturk**:

or how to spell apparently

---

Posted on **2017-03-25 18:57:35** by **boandersen**:

Assuming you are on windows,

to check that python is there and works;

right click start and click command Prompt

then type:

cd \python27\

now try the python --version command



if that works, you need to add this to the path environment variable.. (i'll post that as a new reply

---

Posted on **2017-03-25 18:59:20** by **boandersen**:

it's actually all here: https://github.com/MaslowCNC/GroundControl/wiki/Windows#step-1-install-python



If python does not open, it is most likely an issue with needing to add python to you PATH. You can find out more information about that here: http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path

---

Posted on **2017-03-25 19:09:00** by **fsubigturk**:

so then I just add this "C:\Users\User\Desktop\Python27" now is where I get confused do I change all the \ for ; or do I just type that in as one whole thing?

---

Posted on **2017-03-25 19:19:14** by **boandersen**:

type as a whole thing..

---

Posted on **2017-03-25 19:32:52** by **fsubigturk**:

thank you that worker and I made it all the way to the install kivy part but when I type in the python -m install kivy it turns around and tells me

"C:\Users\User\Desktop\Python27\python.exe: No module named install"

---

Posted on **2017-03-25 20:11:26** by **Bar**:

Are you sure you want to run the program from the source code? We do have a pre-compiled version that might be easier to set up [here](https://github.com/MaslowCNC/GroundControl/wiki/Windows)

---

Posted on **2017-03-25 20:33:52** by **fsubigturk**:

Okay now I can truly let you know how much I know about this stuff. I did the first step and have ground control but I thought the other steps were required to make it work. So if all I need is ground control when I'm in ground control I keep getting connected and lost connection messages on the side. The other thing I noticed is that when I go into the open file I can see the kivy files but when I hit load they won't come up in the ground control screen. Is there some ground control for dummies I could look into

---

Posted on **2017-03-25 20:56:00** by **Bar**:

You are good to go!

---

Posted on **2017-03-25 20:56:50** by **Bar**:

The other steps are just there if you want to run it from the source...but I can see how that is not clear. I will update it to make the distinction more obvious.



Thanks you for pointing that out!

---

Posted on **2017-03-25 20:58:42** by **Bar**:

If you keep seeing connected...disconnected happening on the right side, I would recommend trying to upload the firmware again. That is a common thing to see if the machine does not have the firmware installed. There are instructions [here](https://github.com/MaslowCNC/Firmware) for doing that

---

Posted on **2017-03-25 20:59:49** by **Bar**:

Ground control can only open gcode files which are usually files ending in .nc, which files are you wanting to open?

---

Posted on **2017-03-25 21:00:32** by **Bar**:

Sorry, I should have linked to the instructions better, they are [here](https://github.com/MaslowCNC/Firmware/wiki/Firmware-Setup)

---

Posted on **2017-03-25 21:02:08** by **Bar**:

There is a [ground control users guide](https://github.com/MaslowCNC/GroundControl/wiki/Ground-Control-Users-Guide) which might help. If something is unclear in the guide let me know, I can't tell you enough how helpful it is to learn what is not clear (like the software instructions)

---

Posted on **2017-03-25 21:03:38** by **Bar**:

I've already updated the software instructions based on your feedback. Thank you!

---

Posted on **2017-03-26 10:01:30** by **fsubigturk**:

Okay so the programming is done I think, I no longer get the connected and disconnected but now when I hit test motors in ground control I get Left motor direction 1/2 fail and same with the right motor. I have the board hooked up like it shows I the picture. Is there something I'm doing wrong [Image](//muut.com/u/maslowcnc/s3/:maslowcnc:gVrw:image.jpg.jpg) [Image-1](//muut.com/u/maslowcnc/s3/:maslowcnc:539N:file_1image.jpg.jpg)

---

Posted on **2017-03-26 10:02:57** by **Bar**:

That all looks correct to me

---

Posted on **2017-03-26 10:04:05** by **Bar**:

I would double check that the board is getting power. There should be a blue indicator light on the power supply

---

Posted on **2017-03-26 10:06:45** by **Bar**:

After that I would try running the Test Electronics version of the firmware available in the same folder as the regular firmware [here](https://github.com/MaslowCNC/Firmware)

---

Posted on **2017-03-26 10:07:05** by **Bar**:

That will command the motors to turn one way for 1 second, then reverse for one second

---

Posted on **2017-03-26 10:07:17** by **fsubigturk**:

Lol it was power supply

---

Posted on **2017-03-26 10:07:33** by **fsubigturk**:

They passed the test

---

Posted on **2017-03-26 10:07:41** by **Bar**:

Wooooo!

---

Posted on **2017-03-26 10:09:27** by **scottsm**:

An led on the final board to indicate this power connection is correct would help this.

---

Posted on **2017-03-26 10:11:46** by **Bar**:

I couldn't agree more. Top of my todo list.

---

Posted on **2017-03-26 12:18:42** by **fsubigturk**:

[IMG_6129](//muut.com/u/maslowcnc/s3/:maslowcnc:DaVN:img_6129.jpg.jpg) here you go bar

---

Posted on **2017-03-26 12:20:59** by **Bar**:

That's a 3rd grade rendition of the star ship enterprise if I ever saw one!

---

Posted on **2017-03-26 12:21:36** by **Bar**:

So everything seems normal,  like if you click the arrow keys the machine moves in the right direction?

---

Posted on **2017-03-26 12:22:22** by **fsubigturk**:

it does but when the file is loaded it does weird things. dosent even return back to the home spot I had calibrated

---

Posted on **2017-03-26 12:23:52** by **fsubigturk**:

okay just did the checks now and it went home good and functioned perfectly

---

Posted on **2017-03-26 12:24:29** by **Bar**:

The worst problems are the intermittent ones because it behaves nicely sometimes and not other times

---

Posted on **2017-03-26 12:24:59** by **Bar**:

The first thing I would recommend is download the latest firmware and Ground Control

---

Posted on **2017-03-26 12:25:24** by **Bar**:

It's possible (fingers crossed) that this is an issue with an old version

---

