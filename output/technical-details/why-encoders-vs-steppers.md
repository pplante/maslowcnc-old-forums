## Why encoders vs steppers?
Posted on *2016-10-31 16:46:42* by *electronrancher*

I'm wondering why you went through the trouble of setting up DC motors with encoders instead of just using geared-down steppers - would you mind giving us a bit of insight on your design here?  Thanks!

---

Posted on *2016-11-01 16:37:06* by *Bar*

Sure thing, and great question. It's really about performance vs cost. To get a stepper/gearbox combo which had the same torque and speed as the DC motors would end up being quite a bit more expensive. 

I also just like closed loop control systems. Having feedback about what exactly is happening is cool. The system can actively respond to it's environment. I'd like to add some cool features like adaptive cutting where the machine can sense the load on the bit and set the federate and step-down automatically. I think we're about to see closed loop systems move from being something that only super high end machines use, to something much more common.

---

Posted on *2016-11-01 18:15:02* by *electronrancher*

Agreed, closed loop FTW - and bringing it to the masses is an awesome accomplishment.  Can't wait to get cutting!

One more quick one - is the github code current?  I wanted to use it as a cheat sheet to understand your kinematics derivation on stack, but it looks like it is computing ideal triangles?  Or perhaps it's just super efficient - mathing is not my strong suit.  :)

Thanks again for your reply and for your work - It's a game changer!

---

Posted on *2016-11-02 13:24:43* by *Bar*

Spot on! You are looking for this branch: https://github.com/MaslowCNC/Firmware/tree/kinematics-for-y-axis-compenstion. That branch is very much a work in progress. If you are looking for a cheat sheet, check out this link here. http://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter.

I've gotten a little sidetracked on the z-axis stuff because it seemed like that was what people wanted to see first, but I'm hoping to get back to kinematics in the next day or two. If you have suggestions, feel free to comment on the stack exchange post or even submit a pull request to the firmware branch.

---

Posted on *2016-11-02 14:43:25* by *electronrancher*

Awesome - thanks for the link, I didn't even see the branch.  I am considering building up a test jig to try some of the stuff out, so maybe I'll be able to contribute to firmware sometime soon.

But yeah - keep going with the Z-axis, that will be an amazing addition!  There's plenty of time to tune code later!

---

