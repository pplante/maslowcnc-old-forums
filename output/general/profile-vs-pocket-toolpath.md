## Profile vs. Pocket Toolpaths
Posted on **2017-03-16 12:16:47** by **tmaker**:

Will Maslow support a "pocket toolpath" as opposed to a profile toolpath as illustrated in this video? https://youtu.be/Wd54ai1Xbnk?t=1m30s If not, what would be the solution to clear out everything within a closed shape to replicate the pocket toolpath?

---

Posted on **2017-03-16 13:17:46** by **Bar**:

Good question!



Yes, Maslow will do both pocket and profile tool paths. You are limited to pockets smaller than the size of the sled so it doesn't fall into the hole, but pockets like the ones shown in the video are possible.

---

Posted on **2017-03-16 13:18:47** by **tmaker**:

Awesome!  Very glad to hear that :)

---

Posted on **2017-03-16 13:20:19** by **jbarchuk**:

The simplest correct answer is 'yes,' but not because it's 'part of Maslow.' Clear as mud? :) I'll explain a bit more...



(Neither hardware nor software cares a whit whether a cut is a pocket or a path.)



Design software creates visual representations of your ideas, with dimensions and maybe textures to look nice on the screen.



-Some- design software also create g-code.



G-code is a list of commands that tell the router where to go.



Maslow accepts a g-code file, and -executes- those commands by sending signals to the motors that pull the router around.



If your design software does not create g-code, then a site like makercam.com can do that for you, given a *.svg file. (Don't know if it supports other file times.

---

