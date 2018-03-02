## Tool Change - Sorta
Posted on **2017-01-26 15:27:29** by **chauhuh**:

I was thinking about tool changes and how that might look and I was wondering what others thought. Obviously the original wasn't planned with this in mind but here goes.

If a sled was designed to be able to hold two routers/spindles you could have two cutters. The software would need to be able to account for the offset and you would probably lose some cut space on the outside of the cutting piece. I believe the routers would have to be placed vertically aligned...

I just thought that this might be easier to implement than actually swapping tools.

Thoughts?

---

Posted on **2017-01-26 15:38:20** by **davidlang**:

seems like a lot more work than just swapping bits. :-)

---

Posted on **2017-01-26 17:42:51** by **chadzimmerman**:

Already working on this with my z-axis sled design.  I am combining a portion of a typical cnc head design into the Maslow sled.  It will end up making the sled larger though.  I am a little behind on the design work though, dealing with two car accidents.. Not fun.

---

Posted on **2017-01-26 18:59:58** by **Bar**:

Tool changes are supported in software. Basically the machine stops and you get a popup on the computer screen asking for the new tool. Once the tool is in place, you click "OK" and the job continues. If you need to adjust the z-axis height for the new tool, you can do that.

---

Posted on **2017-01-27 09:14:55** by **chauhuh**:

I was actually thinking along the lines of not having to babysit the tool change. Just have two routers on the machine with different bits so I don't have to change it myself (so lazy).

---

