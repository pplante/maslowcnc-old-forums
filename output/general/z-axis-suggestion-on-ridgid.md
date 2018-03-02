## Z-axis suggestion on Ridgid Routers
Posted on *2017-03-28 16:51:50* by *jessbussert*

All you peeps with the recommended Ridgid routers, here's something to think about when you are messing with your Z-axis.  As you may have already noticed, there is a lot of play in Ridgid's design for the depth setting.  I would suggest that when adjusting depth by hand that you first draw the bit out beyond the depth you need and then reverse inward until you get to your desired setting.  This way you are always setting your depth by turning your screw the same direction.  Doing so will take up any backlash inherent in the Ridgid design.

You can accomplish this same process on an automated Z-axis by always issuing a G0 Z0 command before issuing your depth selection command.  This should work for most Z changes that don't involve a smooth curve across the Z axis.

If this was too confusing, think of it another way.  Always set your depth moving the bit into the material.  Never set it moving out of the material or by using a back-and-forth process of overshooting and then correcting.

---

Posted on *2017-04-04 23:04:41* by *rexklein*

That is awesome, I am not up and running yet. But wow you totally answered my immediate thought (wow there is a lot of play in that router depth). Thanks for doing my thinking for me really great solution one worthy of being directly pasted into the maslow manual!

---

Posted on *2017-04-04 23:52:03* by *scottsm*

That's good advice. Cutting tabs involves raising Z over the tab, I'll make sure to use a tall enough tab to account for the backlash.

---

Posted on *2017-04-05 00:43:54* by *davidlang*

with the ridgid router, you should be loosening the nut under the latch so that when it is latched, the router is still able to move, but tight enough that it doesn't wobble. If it's loose, you have things adjusted incorrectly.

---

Posted on *2017-04-05 03:48:27* by *TheRiflesSpiral*

The backlash is a result of the clearance between the parts that make the adjustment, not the clamping mech. There's clearance between the arm that rides on the threaded rod and between the recess in the router body that receives the arm.

It should be simple enough to add an additional number of turns necessary to take up this lash when changing directions in the Z-axis. I'll add a feature request to Github.

---

