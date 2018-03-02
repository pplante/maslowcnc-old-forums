## Speed/Feed charts
Posted on **2017-06-05 13:48:04** by **nathanmiller**:

I'm getting excited to take order of my Maslow but one thing I had hoped would be worked out before I got mine set up is the speed & feed calculations. 

Do you know if any beta testers have worked on this? If not I will put it on my to-do list for when mine is set up. 

I'm thinking a database would work well, and maybe some way to quickly visualize the tests (see my ugly attached image) [Untitled](/images/Um/kB/UmkB_untitled.png.jpg)

---

Posted on **2017-06-05 13:50:30** by **nathanmiller**:

actually, I think the graph would be more like this:  [Untitled-0](/images/Ok/gZ/OkgZ_file_0untitled.png.jpg) 

At any rate, it would be nice to see what the typical successful speed/feed combo is like for various material and bit types.

---

Posted on **2017-06-05 13:56:50** by **TheRiflesSpiral**:

This is an example of where having a wiki really pays off. I can see this being added at a page at github that way it's a collective effort.

---

Posted on **2017-06-05 14:30:45** by **davidlang**:

see the topic "bit lifespan" under no judgement. I linked several things in that topic.



part of the fun in determining the best speeds/feeds to use with the maslow is that the sled can swing due to it's momentum when it hits the end of a cut. We don't currently implement any look-ahead or acceleration planning, and that will change the limits significantly.



We still have people experimenting with different angles and weights which can also affect this.



right now development is more focused on trying to improve the accuracy and the code efficiency (which allows for more accuracy as well)

---

Posted on **2017-06-05 14:31:27** by **davidlang**:

http://www.maslowcnc.com/forums/#!/no-judgement:bit-lifespan

---

Posted on **2017-06-05 16:43:40** by **gero**:

From my to-do list :-): feed of Z-Axis into the material (I have sled twists there); feed and depth for clean cut (RPM of the router seems to be higher than recommended for horizontal machines, but not confirmed by me yet, depths seem to be to shallow, also not confirmed in my setup yet). Much to try out.

---

