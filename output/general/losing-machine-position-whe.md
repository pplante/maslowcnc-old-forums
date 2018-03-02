## Losing machine position when Motor Control Board Powered off but Jogging in GC
Posted on **2017-06-05 12:10:26** by **ledsled71**:

When the motors are powred off, but you accidentally jog in Ground Control, does the machine lose its' position?

I ask because GC shows the machine moving even though the board is powered off, yet when I power the board up, the machine doesn't then move to match the position shown in GC.  I'm guessing that I've now lost position?

---

Posted on **2017-06-05 12:15:52** by **Bar**:

Yes and no.

First, that's a corner case we should take care of. What are your thoughts on the right behavior?

What's happened is that the machine's target position will have moved, so once the board is powered back up both motors will adjust to move the machine directly to the indicated position. You do not need to re-calibrate the chain lengths.

---

Posted on **2017-06-05 12:19:39** by **ledsled71**:

Not sure I'm understanding.

I would expect the machine to move once powered up to where GC is showing it to be, but no movement happens when it powers up.

---

Posted on **2017-06-05 12:27:30** by **Bar**:

For safety, the machine powers up in a dormant state. It won't move until you click a button (to prevent if from moving when you aren't expecting it). Clicking any of the arrow buttons will cause the machine to move to the location indicated in Ground Control once power has been restored.

---

Posted on **2017-06-05 12:31:43** by **ledsled71**:

Aha!  Thanks, enjoying all of this learnin'

---

