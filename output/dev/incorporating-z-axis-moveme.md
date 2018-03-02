## Incorporating Z axis movement
Posted on **2016-11-17 07:55:07** by **Jeremy Wright**:

Found this project from 

http://www.popularwoodworking.com/woodworking-blogs/editors-blog/checking-maslow-cnc and find this to be an intriguing project, that I hope is successful, as the concept is compelling.



I'm curious if a third "tri-pod" cable has been considered as an expansion from XY plane control into a full on Parallel Kinematics machine (http://articles.sae.org/9787/). I have seen these PK machines used, and while they have some quirky access limitations, it seems a natural extension to your aims with this project. I'm sure this would make for some wacky coding, but for say carving on wooden components it could be quite powerful (e.g. acanthus leafed knee, ball and claw leg)

---

Posted on **2016-11-17 10:30:46** by **Bar**:

Thanks for posting a link to the article, those guys were a ton of fun to hang out with!



I played around with a 4 cable system early on, but ended deciding to keep it simple to keep the cost down. A big part of the reason I really like the idea of keeping it open source is so that we can all explore these cool alternative designs. If someone plays around with the hardware and it looks promising, I'm happy to do the coding side of it.



Could you by any chance post the link to the sae article again? It looks really interesting, but that link seems to be funky

---

Posted on **2016-11-17 12:01:29** by **Jeremy Wright**:

Hrmmm... it looks like SAE does some sort of dynamic linking that doesn't allow long term linking... weird. Probably a better example would be in video anyway, as the SAE article "Parallel kinematic machines for large wing and fuselage assembly

16-May-2011" is for assembly and I had seen the technology related to machining.

https://youtu.be/4xSkt9Fa8iQ

https://youtu.be/SSSvKt92tnA

In my concept, I imagine a non-rotating router placed on the tripod head.



I imagine a 4 cable system would be a lot more challenging than a 3 cable system given the problem of overconstraint. You have a really interesting concept here and I am intrigued as my professional background is with exact constrained designs & 3D tolerance analysis, though in my woodworking hobby its mostly in traditional hand tools, rather than tech. Perhaps in the future I will have some time to participate in the open source nature of this project, for which you are definitely to be commended.

---

Posted on **2016-11-17 17:55:01** by **Bar**:

Awesome!



I tried to get around the over constrained issue by using counter weights instead of motors on the lower two cables to give a constant tension. The controller board for the z-axis will actually support a fourth independent axis, so if you wanted to play around with a 3 chain system, the hardware is in place.



Thanks for passing those videos along. Very cool.

---

Posted on **2016-11-18 05:45:21** by **ihabfahmy**:

For z-axis control, it may be simpler to move the workpiece than to move the router with all the chains attached (or even easier than moving the router bit, on models that are not have a depth-of-cut screw).

---

Posted on **2016-11-18 08:15:02** by **Jeremy Wright**:

One last reference that may help your future endeavors for getting low cost precision with fewer iterations, is an excellent book on exact constraint principles (ISBN: 0791800857) it's small and digestible (though a bit pricey if you can't find a library to lend it) It pieces together things you probably already know to become things you may not have connected all the dots to yet. No connection here, just a really good book.

---

Posted on **2016-11-18 13:04:27** by **davidlang**:

@ihabfahmy, the current Z-axis plan is to leave the router solidy mounted and put a motor on the router's existing depth knob.



This is FAR simpler than moving the entire router mount, let alone the workpiece.

---

Posted on **2016-11-20 12:34:31** by **jambo**:

so when the z axis plan is applied, does this mean for 3/4 inch ply, you could leave the machine running itself and it would automatically repeat passes until the depth reaches a point where the wood is cut right through?

---

Posted on **2016-11-20 14:47:39** by **Bar**:

Yes. The z-axis will also retract itself between cuts so you could cut a pieces from the 3/4 plywood without touching the machine. For an example, check out the crutch in our week 2 update that one of our backers sent in. That was cut from 3/4 plywood without touching the machine.

---

Posted on **2017-01-15 12:28:07** by **glenboudreaux**:

Is there a video showing the z-axis in action?

---

Posted on **2017-01-16 06:00:47** by **TomTheWhittler**:

The kickstarter Z-axis update had a picture of the proposed z-axis setup with a small embedded video click of it working.



https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1726891

---

Posted on **2017-01-16 07:52:32** by **glenboudreaux**:

Thanks! I had not seen that post.

---

