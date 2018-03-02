## Feed rate
Posted on **2017-01-17 07:38:22** by **garyw17**:

Hello,
Awesome project!  I think I saw somewhere in here that your maximum feed rate was around 50 ips?  Do you try to maintain that feed rate at the router regardless of position and direction of travel?  It seems for example that as you get towards the bottom corners of the work area that the feed motor speed would have to be significantly faster to keep the cutter feed rate the same.

---

Posted on **2017-01-17 07:48:24** by **davidlang**:

The system should maintain the feed rate regardless of position on the workpiece. Yes, this will mean that the motors are running at different speeds for different parts of the workpiece. But it needs to vary the speed all over the place anyway just to control the positions.

---

Posted on **2017-01-18 14:29:15** by **TheRiflesSpiral**:

If you want to see the code, it starts at line 206 in CNC_Functions.h.

It doesn't appear to me that the speed is affected by the length of the chains. calculateDelay() pauses the loop for a period of time after each move to control feed rate and it takes step size and feed rate as inputs... I can't see any place where the length of the chains (or calculated position) alters that calculation.

---

