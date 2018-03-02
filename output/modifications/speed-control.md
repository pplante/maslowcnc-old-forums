## speed control?
Posted on **2016-11-14 01:33:59** by **davidlang**:

have you thought about modifying the router so that it's speed can be controlled as well?

the obvious way is to mount a servo with a wheel against the existing speed control, but anything external like that is going to be less reliable than modifying the router and providing a direct control.

---

Posted on **2016-11-14 10:46:30** by **TheRiflesSpiral**:

A universal speed control for AC motors is probably the right solution. That can be standardized and work for any router.

---

Posted on **2016-11-14 17:31:22** by **Bar**:

I hadn't thought about it in depth, but it shouldn't be too hard to do. I think that TheRiflesSpiral is right that the easiest way to do that might be with an external universal speed control. 

I'm hearing so many good suggestions for ideas of things to add that I'm putting 4 auxiliary ports onto the controller to make it easy to do those kinds of additions. They will use the standard servo connector so if you did decide to attach a servo it could plug right into on of the aux ports.

---

Posted on **2016-11-15 15:54:29** by **davidlang**:

The problem with using an external speed control is that all it can do is reduce the power of the motor, it doesn't know how fast it's spinning.

the internal speed controller can (should) have feedback so that as the router slows, it feeds more power to to motor to maintain the speed.

This isn't possible with an external controller add-on.

---

Posted on **2016-11-16 19:47:08** by **karlthorp**:

@Bar

Would it be possible to add a PWM circuit rated for a router combined with an amp meter to receive feedback from the router to the controller board and add speed control to the software?

---

Posted on **2016-11-17 10:57:25** by **Bar**:

Yes. The controller has four aux input/outputs so you could use one output to control the PWM and one input to read the speed back from your router. It would take a bit of engineering, but it's entirely possible.

I probably won't sell the whole circuit because of the liability around circuits which control 110/220v, but I'm happy to help.

I actually built one of these at one point for a job a while back, and the part to look at is called a thyristor. It's like a transistor, but cheaper and rated for higher power.

---

Posted on **2016-11-18 13:01:17** by **davidlang**:

I was thinking more in terms of opening up the router and replacing the pot for the existing variable speed control with a connection to the computer.

---

Posted on **2016-11-20 15:10:53** by **TheRiflesSpiral**:

There are a few IC's that vary resistance in accordance with an input voltage... You can even pull this off with a JFET or MOSFET if you're using them in their linear range.

---

