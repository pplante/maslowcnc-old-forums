## Accuracy
Posted on *2017-05-25 01:24:10* by *garry_j*

To improve accuracy away from centre, and indeed everywhere, the chains need to maintain a radius line from the centre of the cutter. A couple of arms pivoting on the router mount is all that's needed.

---

Posted on *2017-05-25 01:27:30* by *davidlang*

There are people trying that. But the math we are using takes into account the tilt of the sled and the fact that the chains do not point directly at the center of the cutter.

an explination of the math used
https://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter/10858#10858?newreg=13734dd331424a0ea0d2ddc79c562910

see the inverse function in the code
https://github.com/MaslowCNC/Firmware/blob/master/cnc_ctrl_v1/Kinematics.cpp

now, I think there's probably a bug in here that's causing our error, but we haven't tracked it down yet.

---

Posted on *2017-05-25 05:46:53* by *garry_j*

A lot of measurements to set up accurately, not to mention centre of mass is critical. Good luck with it.

---

Posted on *2017-05-25 09:24:13* by *Bar*

Pivoting around the bit would be ideal, but there's quite a bit of hardware that goes into making that work. It could work, but probably not at our price point. I'm a pretty firm believer in trying to solve problems in software over hardware, but a big part of why everything is open source is to encourage that kind of exploration. If you build one that pivots, let us know!

---

Posted on *2017-05-25 09:27:58* by *davidlang*

Bar, did you ever test a sled where the router bit and the CG are on the line connecting the chain pivots?

one brick above and one below the router, with the chains connecting at the center of the sides.

This would make figuring out the math for positioning _much_ simpler (and hopefully faster)

---

Posted on *2017-05-25 09:39:33* by *Bar*

I haven't, but that's a really really cool idea. I'll add it to my list and keep thinking about it. Let me know if you try it. What a creative idea.

---

Posted on *2017-05-25 09:51:17* by *davidlang*

unfortunately I'm not a beta tester, so all I can do is make suggestions.

---

Posted on *2017-05-25 09:52:10* by *Bar*

We're trying to get the rest of these kits in the mail change that pretty soon here :)

---

