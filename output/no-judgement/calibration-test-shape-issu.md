## Calibration Test Shape Issues
Posted on *2017-06-03 17:59:11* by *jenmsuth*

Hello! When I go to test my calibration on the temporary frame by routing the circle/square template, the software prompts to adjust the bit height, however, the motors continue moving the router along even though I haven't pressed "continue". Along the circle the motors eventually pause and allow me to adjust the bit height. Once it transitions to the square it refuses to stop the motor at all - I end up with the transition path (where there should be no routing) cut as well as the square. Not sure if this is a code file issue or I haven't calibrated something properly....

---

Posted on *2017-06-03 18:25:18* by *jenmsuth*

additionally: reposition lines do not show up dashed...not sure if that is the problem. Not sure if there is a way to update that?&quest;

---

Posted on *2017-06-04 14:22:52* by *scottsm*

This problem is not your fault. It is due to buffering of commands sent to the firmware. There is an open issue #284 in GroundControl, but the solution has not been found.

---

Posted on *2017-06-04 14:29:50* by *jenmsuth*

hmm. is there a good way to proceed with building the permanent frame? or should I wait for the problem to be resolved? My concern is in properly cutting bolt holes, etc.

---

Posted on *2017-06-04 14:35:44* by *davidlang*

it's probably best to wait a few days for this to be tracked down.

---

Posted on *2017-06-04 14:40:38* by *jenmsuth*

got it. Thanks!

---

Posted on *2017-06-05 09:36:58* by *gero*

Wanted to do some tests with modifications on the sled (brackets, weight,COG). What would be the safest firmware and GC release to go back to?

---

Posted on *2017-06-05 12:25:54* by *Bar*

The issue should now be fixed in the latest version of Ground Control and will be part of this week's release. Thank you again for reminding me that this was an issue which needed to be addressed.

---

Posted on *2017-06-08 19:49:42* by *jenmsuth*

Thanks for your hard work to fix it!!

---

