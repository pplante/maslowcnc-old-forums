## Change in firmware?
Posted on **2016-10-25 06:01:14** by **asleborgen**:

Hi, Asle from Norway here. 
I`m really impressed with your work, and as a fellow maker, also really keen on building my own Maslow :-)
Enough intruductory mabojambo, over to the question:...

Is there a simple way to change the parameters for motors and encoders in the Arduino program? I`ve found a couple of cheap geared motors with encoders on Ebay, but I highly doubt that they are equal to your motors... As a mechanical engineer i feel up to the task of making the mechanical bits, but my programming skills suck (at best), thus the question...

Anywhoo; keep up the good work, this project is brilliant in its simplicity!

Best regards
Asle

---

Posted on **2016-10-25 09:12:55** by **Bar**:

Yes! It is very easy to set the encoder the resolution of the encoders and the dimensions of the machine in the software. We're an open source project so I wanted to make it as easy as possible for people to build their own. 

If you start building one and have any questions, ask away, we're here

---

Posted on **2016-10-27 03:41:49** by **asleborgen**:

@BAR; would it be possible to sneak a peak of your H-bridge pcb? I`m fully capable of doing all the assembly, but unfortunately, pcbdesign was not a part of my mechanical designer (engineer) training :-)

---

Posted on **2016-10-27 07:56:14** by **Bar**:

Of course! We're open source and open hardware :-). You can find the latest versions of my PCBs at https://github.com/MaslowCNC in the PCBs repository.

---

Posted on **2016-10-27 14:38:55** by **kc8kzn**:

you mentioned PID settings in another comment. are those also easy to change? (getting them right may be another question)

---

Posted on **2016-10-27 19:39:39** by **Bar**:

Haha :-) They are easy to change. At the moment they are #defined in the firmware, but the library I am using actually supports changing them on the fly, so I am going to put them into the software settings along with things the dimensions of the machine. I figure that a lot of people will want to either modify their machine or build one from scratch so keeping all the knobs you want to turn when you do that is a priority

---

