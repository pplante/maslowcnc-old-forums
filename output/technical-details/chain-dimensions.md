## Chain dimensions
Posted on **2017-06-20 13:07:30** by **gilbertjm**:

Hello,

since the original #25 chain is hard to get in Europe, I'm currently looking for alternatives. Is there a good reason to use a chain with such a small pitch of 1/4'' = 6,35mm. Here we have a norm called DIN 8187. The 04B-1 with a pitch of 6mm is quite close to the original specifications, but the 06B-1 with 3/8''=9,525mm is more common. At the moment I would like to give the 06B-1 a try... Thanks for your opinions

---

Posted on **2017-06-20 13:14:10** by **TheRiflesSpiral**:

Just keep in mind the variables that would need to change along with chain pitch. (Number of sprocket teeth, sprocket diameter... maybe that's it?)

---

Posted on **2017-06-20 13:26:18** by **davidlang**:

the small chain is lighter than heavier chain. give it a try and I'd suggest that you look and see if there are any hidden assumptions in the code about chain pitch (I don't think so, but...) and send in a patch if you find any.

---

Posted on **2017-07-17 13:28:20** by **netzbasteln**:

Hi gilbertjm, thanks for your research. Have you already found out something new? I also believe 06B-1 is worth a try, easier to source, especially the tensioning chainwheels with bearings. Already got the motors from china, their axle is 8mm and their flat part is 7mm.

---

Posted on **2017-07-17 13:48:52** by **netzbasteln**:

Addition: original Maslow does not use tensioning chainweels with bearings though.

---

Posted on **2017-07-17 14:15:41** by **netzbasteln**:

Another addition: CNC_Functions.h makes the dimensions of the chain and the number of teeth totally definable:



#define DISTPERROT     10*6.35 //#teeth*pitch of chain

#define ENCODERSTEPS   8148.0 //7*291*4 --- 7ppr, 291:1 gear ratio, quadrature encoding



https://github.com/MaslowCNC/Firmware/blob/master/cnc_ctrl_v1/CNC_Functions.h

---

