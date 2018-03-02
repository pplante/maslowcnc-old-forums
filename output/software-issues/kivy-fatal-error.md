## kivy fatal error
Posted on **2017-03-24 09:47:13** by **mikeberg**:

my old laptop cannot run ground control.bat (error with opengl due to version 1.1 they say i need 2.0 minimum......what can i do

---

Posted on **2017-03-24 10:06:30** by **davidlang**:

upgrade or get something like a raspberry pi or android device to use instead of the laptop?

---

Posted on **2017-03-24 10:18:41** by **Bar**:

What are the laptop specs?

---

Posted on **2017-03-24 10:20:02** by **mikeberg**:

i have raspberry pi +b edition i spent 2 day to make use main.py  in graphical screen so much issues...i have followed some of the instruction in forum but now i'm waiting until .img for my pi can be downloadable with no issues

---

Posted on **2017-03-24 10:21:27** by **Bar**:

Good to know, I will make creating a .img a priority

---

Posted on **2017-03-24 10:23:15** by **mikeberg**:

thank you so much with all these code its new to me

---

Posted on **2017-03-24 10:29:57** by **mikeberg**:

i run on windows 7 32 bits intel centrino duo processor 1.8 ghz 1 gig ram

---

Posted on **2017-03-24 11:37:12** by **Bar**:

That seems like a reasonably modern system. I will look into it more.

---

Posted on **2017-03-24 11:42:25** by **Bar**:

Can you try to upgrade your graphics driver like they describe here: https://buffered.com/support/solve-opengl-error/ ?

---

Posted on **2017-03-24 12:11:24** by **mikeberg**:

Same problem  [DSC_0299](//muut.com/u/maslowcnc/s3/:maslowcnc:KUOh:dsc_0299.jpg.jpg)

---

Posted on **2017-03-24 12:17:05** by **mikeberg**:

Here when I do dxdiag  [Sketch-1490382990849](//muut.com/u/maslowcnc/s3/:maslowcnc:staT:sketch1490382990849.png.jpg)

---

Posted on **2017-03-24 12:34:12** by **Bar**:

hmmmm :-(

I'll keep looking into it. Thanks for trying that!

---

Posted on **2017-03-26 08:59:16** by **mikeberg**:

I made the same test to run. Exe on an other pc Intel athlon 1.1 ghz 1 gig ram with  nvidia tnt2 graphic card... Same error all driver up to date!?  Kivy need a better pc that I thinked

---

Posted on **2017-03-26 09:32:03** by **Bar**:

That might be so. I bet it is possible to make it run because Kivy has been around for many years so it is likely that an older version of Kivy will work.

Would you be willing to try the "run from the source" method? It might be that when you install python and Kivy directly it will recognize the older version of opengl.

---

Posted on **2017-03-26 21:12:59** by **mikeberg**:

i made some research and i will  maybe try this,the problem here  i does not know how to modify .ky file
http://stackoverflow.com/questions/34969990/kivy-does-not-detect-opengl-2-0?rq=1

---

Posted on **2017-03-26 21:16:32** by **mikeberg**:

like if i has some problem with glew extension

---

Posted on **2017-03-26 21:25:12** by **Bar**:

Awesome find! I can add that to the code first thing tomorrow.

---

Posted on **2017-03-27 08:48:02** by **mikeberg**:

do you will change it for new version release wednesday with the codes i suggested?

---

Posted on **2017-03-27 09:30:06** by **Bar**:

I can do it for today and send you a link, if it fixes the problem it will be part of the Wednesday release too

---

Posted on **2017-03-27 09:38:46** by **mikeberg**:

thank you so much for your time I will try it today

---

Posted on **2017-03-27 09:52:45** by **Bar**:

Thank you so much for tracking down what to try!

The updated version is compiling and uploading right now

---

Posted on **2017-03-27 10:13:01** by **Bar**:

It's [here](https://github.com/MaslowCNC/GroundControl/blob/open-gl-issue-take-three/GroundControl-Windows%20Portable-openGL.zip), let me know if it works!

---

Posted on **2017-03-27 10:29:53** by **mikeberg**:

it improve now! i can see the real version i have in open gl so the bad news its my laptop it with it final version of update it will not function on kivy

---

Posted on **2017-03-27 10:30:48** by **mikeberg**:

[DSC_0303](//muut.com/u/maslowcnc/s3/:maslowcnc:dJYn:dsc_0303.jpg.jpg)

---

Posted on **2017-03-27 11:01:38** by **Bar**:

That's better I guess!

---

Posted on **2017-03-27 11:02:34** by **Bar**:

Have you tried the "run from source" method? I know I used to run Kivy on Windows Vista a long time ago so I think it's possible.

---

Posted on **2017-03-27 12:24:24** by **mikeberg**:

I open. Bat file from the uncompressed file, what do you mean by run from source?

---

Posted on **2017-03-27 12:26:58** by **Bar**:

There are two ways to run Ground Control. You can open bat file from uncompressed file, or you can install python directly and run the program from the source code. There are instructions [here](https://github.com/MaslowCNC/GroundControl/wiki/Windows). 

This way is more complicated, but may work on older computers.

---

Posted on **2017-03-27 19:05:57** by **mikeberg**:

Nice! I will try this tonight and I will give a comeback

---

Posted on **2017-03-28 00:02:22** by **mikeberg**:

I have installed everything with no problems has by Python -m pip kivy. Deps.sd12

---

Posted on **2017-03-28 00:09:45** by **mikeberg**:

I run from source code main.py on cmd and a warning appear maybe it tell you something

---

Posted on **2017-03-28 00:10:21** by **mikeberg**:

[DSC_0304](//muut.com/u/maslowcnc/s3/:maslowcnc:CX2w:dsc_0304.jpg.jpg)  [DSC_0305](//muut.com/u/maslowcnc/s3/:maslowcnc:nIs5:dsc_0305.jpg.jpg)

---

Posted on **2017-03-28 09:36:32** by **allensparks**:

you could try installing kivy manually via pip: https://kivy.org/docs/installation/installation-windows.html#installation-windows is a decent guide. although it assumes your already running powershell, python, and know that pip is part of the python package.

---

Posted on **2017-03-28 09:42:19** by **Bar**:

In the line
---
python -m pip install kivy.deps.sdl2
---

is that the letter 'L' or the number '1' before the two? It should be the letter. That's the only reason I can think that pip might not be able to find the download.

---

Posted on **2017-03-28 09:43:09** by **mikeberg**:

Haha yes its OK now for sdl12

---

Posted on **2017-03-28 09:47:59** by **mikeberg**:

I open main.py by the cmd with source code i got the same problem with open gl...

---

Posted on **2017-03-28 09:48:16** by **mikeberg**:

[DSC_0306](//muut.com/u/maslowcnc/s3/:maslowcnc:IY8x:dsc_0306.jpg.jpg)

---

Posted on **2017-03-28 09:53:19** by **mikeberg**:

in this page open gl tell me they have an extension  named gl_win_swap__hint that it sould help me?its true

---

