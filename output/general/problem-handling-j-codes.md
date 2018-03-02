## Problem handling "J" codes?
Posted on **2017-03-25 10:15:05** by **rancher**:

This is what I've been chasing since I first tried to cut my own part.  I assumed it was a problem with my design or output settings, but I'm getting the same behavior using Bar's example gcode files.  The carriage stops after a J value.  Not all J values.  Low ones or zero, but I'm not 100% sure, or even that it is the J value that is the problem.  Anyway, I can't cut a thing, although the workaround is Pause right before it stops, then run, and it will continue.  

 

I also am unable to FFwd in these files, and wonder if that is part of the reason the shuttle function is so wonky.



All files do this for me, but not the circles, holes, or Bar's "CauseB" example file.



Here's what it looks like when it's broken.

 [IMG_3565](//muut.com/u/maslowcnc/s2/:maslowcnc:4LUN:img_3565.jpg.jpg)

---

Posted on **2017-03-25 11:25:29** by **Bar**:

Great catch!



Would you be willing to make an issue on github and attach a file which isn't working? That will make it real easy for me to start investigating. 



Great job narrowing it down.

---

