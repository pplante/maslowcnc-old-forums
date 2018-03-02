## Software Compatability
Posted on **2017-03-30 17:51:53** by **tntahan**:

So I looked at the post for the Assembly Guide and looked at some of the software listed that we need (ground control, Arduino, Firmware for it) But I didn't see anywhere that said anything about minimum system requirements for a computer. I am wanting to use an old laptop I have for this, anyone know the system requirements?

---

Posted on **2017-03-30 17:55:46** by **Bar**:

That's a great question. I really don't know the exact requirements. As far as processor speed/ram the requirements are not large. We have found that you need to have a graphics card with least an Open-GL 2.0 compatible driver to be able to open Ground Control

---

Posted on **2017-03-30 19:17:39** by **mikeberg**:

i make a test tonight for the compatibility between my old desktop pc and linux os i want to make possible run GroundControl on old pc in the past I tried to make it run on Windows with some issue... I can run ground control on my raspberry pi so I cannot see why it will be not possible

---

Posted on **2017-03-30 19:18:31** by **Bar**:

I think that is a very good plan. Please let us know how it goes

---

Posted on **2017-03-31 14:49:25** by **mikeberg**:

I make a test with debian os and the same issue encounter :( kivy isn't compatible with old processor  [DSC_0307](/images/MN/XH/MNXH_dsc_0307.jpg.jpg)

---

Posted on **2017-03-31 17:42:04** by **Bar**:

Hmmm that is very unfortunate. I think one thing we can do to help is to use the same interface as grbl (a common CNC firmware) which will mean that there will be many programs available to control Maslow

---

Posted on **2017-03-31 19:18:24** by **davidlang**:

That would be a good move, that way you can concentrate on the firmware and hardware (which is unique to maslow) and then think hard about the value-add of maintaining Ground Control instead of just using one of the exiting grbl compatible tools.



GUI/Front-end programming is a different skill set than firmware programming and hardware design is even more different. How many different projects do you need to keep up on?

---

Posted on **2017-03-31 20:27:37** by **rancher**:

> @davidlang

> exiting grbl compatible tools



Wow, some of those tools look pretty interesting. 



https://github.com/grbl/grbl/wiki/Using-Grbl

---

Posted on **2017-03-31 21:45:36** by **mikeberg**:

I approve!! that look fantastic for us

---

Posted on **2017-04-01 07:44:49** by **gero**:

@mikeberg Not that wold know anything about this, but i post it anyway just in case it could be a starting point. I remembered some issues with LinuxCNC and OpenGL on older hardware and their documentation is so outdated that I could still find it after years. From the docu: "By installing the package 'libgl1-mesa-swx11' you can get software OpenGL? rendering even if your video card has buggy direct rendering." https://packages.debian.org/sid/libgl1-mesa-swx11

---

Posted on **2017-04-01 21:17:07** by **mikeberg**:

i have tryed your code and its seem to help but my screen wont open [DSC_0309](/images/mJ/Gn/mJGn_dsc_0309.jpg.jpg)

---

Posted on **2017-04-01 21:21:24** by **mikeberg**:

seriously i want to make a test with grbl it not seem to be to much complicate i will come back if my .nc file runn good

---

Posted on **2017-04-01 21:27:19** by **mikeberg**:

im sure about  not everyone dont want to buy a new pc just because kivy its not compatible on olds pc :p

---

Posted on **2017-04-01 21:52:33** by **Bar**:

I completely agree. We need to find a way to use old PCs. Running Maslow is a great job for an old computer and I think many people will want that.

---

Posted on **2017-04-01 22:14:53** by **Bar**:

Do you have a grbl control program that works for you that you want me to test with? In theory they all should be the same, but I'd still rather make it work for the one you want first.

---

Posted on **2017-04-01 23:14:29** by **mikeberg**:

yep i finded one gcode sender it can be execute on all three platform named universal gcode sender it seem to be great only java is required

---

Posted on **2017-04-01 23:19:32** by **mikeberg**:

My first. NC file test work very nicely on it, I'm offline with my arduino uno for now but im very confiant  [DSC_0310](/images/7B/ns/7Bns_dsc_0310.jpg.jpg)

---

Posted on **2017-04-01 23:23:08** by **mikeberg**:

link for universal gcode sender 

 http://winder.github.io/ugs_website/

---

Posted on **2017-04-01 23:40:05** by **mikeberg**:

test done with the old computer it was never  worked also much good

---

Posted on **2017-04-02 08:53:00** by **scottsm**:

That 'universal gcode sender' works OK on OSX. It seems to be actively supported.

---

Posted on **2017-04-02 09:30:33** by **Bar**:

Fantastic! That looks like the one.

---

Posted on **2017-04-02 10:36:59** by **mikeberg**:

i found another one  that look a bit complicated no more support since 2015 its called grbl controller  http://zapmaker.org/projects/grbl-controller-3-0/

---

Posted on **2017-04-02 10:41:49** by **mikeberg**:

Nice tutorial about how to flash uno and make it run https://youtu.be/rX8nLEuN2nE

---

Posted on **2017-04-02 12:43:39** by **Bar**:

I've started digging into how the grbl protocol works and it's very similar to how our protocol works so we should be able to adopt it without too much trouble.



There are a couple key differences like they use G91 (switch to relative coordinate system) to jog the machine so it will take me a couple hours to get everything playing nice, but it is very doable.

---

Posted on **2017-04-02 15:40:42** by **scottsm**:

Making the MaslowCNC 'speak grbl' will open up lots of options for front ends and free you up to work on the machine itself. An exciting development!

---

Posted on **2017-04-02 18:49:34** by **mikeberg**:

hey @bar how you will set it to make all calibration run on home start (g28)with maslow

---

Posted on **2017-04-02 19:01:22** by **mikeberg**:

i think you should put  position x0y0 in the center of the plywood sheet its easy to measure with a mesuring tape on diagonal

---

Posted on **2017-04-02 19:56:10** by **Bar**:

X0y0 is the center of the plywood, so we should be good on that one, I will look into G28, but it should be easy. Will you mention it in the GitHub thread on grbl support? That way I will be sure to see it while I'm working on it. Seems like a good suggestion.

---

Posted on **2017-04-03 08:53:16** by **scottsm**:

I put a link in Firmware issue #122 to a discussion of G28 that clarified the grbl coordinate systems and their interactions for me.

---

Posted on **2017-04-03 09:17:24** by **rancher**:

That was super helpful to me Scott, thank you.  Now I know what my Z-axis is doing at the start of the jobs, and what to do about it.

---

