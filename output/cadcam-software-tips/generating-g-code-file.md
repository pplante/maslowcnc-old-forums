## Generating G code file
Posted on **2017-06-01 09:35:37** by **cmazzoli**:

may be a silly question but I am new to all this. In the tutorial he puts all the parts to be cut in one image. When i design the parts in makercam can i put all the parts in there and make 1 gcode file then load that into the maslow software? Or do i need to make seperate gcode files for each part then load all those files into the maslow software? thanks!

---

Posted on **2017-06-01 09:37:52** by **davidlang**:

if you put all the parts in one g-code file, the maslow will cut them all at once. If you put them in separate files, you will need to load and cut each one individually.



The normal thing is to do all the layout work and placement before you generate the g-code and export it all as a single file.

---

Posted on **2017-06-01 09:40:37** by **blsteinhauer88**:

@davidlang is correct, (not a surprise!)  I would make a rectangle in Makercam the size of your piece of wood, layout the parts inside that rectangle and make cam operations to the parts, not the rectangle, just use it as a guide and you can have a better visual for layout.

---

Posted on **2017-06-01 09:42:55** by **cmazzoli**:

yeah that was what I was doing. I made the 4X8 space and was adding the parts of a little free library. I will keep doing that then learn how to make the cam operations to the parts then export it as one gcode file. I am glad we can do it this way! 1 file at a time would have been a bummer. thanks!

---

Posted on **2017-06-01 09:47:35** by **blsteinhauer88**:

need help just ask, there is a shark pool of experience out here now to help you.

---

Posted on **2017-06-01 09:59:26** by **cmazzoli**:

you got it. thanks!

---

