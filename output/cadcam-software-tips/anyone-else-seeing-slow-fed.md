## Anyone else seeing slow federates when using metric?
Posted on **2017-05-06 16:18:23** by **mcginniwa**:

I've run the provided calibration shape gcode file a number of times and it runs fairly fast. It's in imperial rather than metric.

To tweak the bit size, etc. in the `CAM -> profile operation`, I've created a gcode from the source svg file. I used 635mm/minute for feedrate (read in forums that 25"/minute was max rate).

When I run this from GC, it's wicked slow! Anyone ideas why this might be?

---

Posted on **2017-05-06 16:37:07** by **scottsm**:

There was a problem with metric feed rate in the Firmware noted a while back. Line 416 of CNC_Functions.h was changed to address it, on about April 29. You're seeing this slowdown when cutting from a file using a recent copy of Firmware, right?

---

Posted on **2017-05-06 16:39:01** by **mcginniwa**:

Sounds like the issue. That was right around the time I installed the firmware. Don't think I've updated it since. Will update and report back.

Thanks @scottsm

---

Posted on **2017-05-06 16:41:45** by **scottsm**:

If that's the case, I can hope that this fixes it :) . Gero noted the issue and tested the fix. There are other good things in the most recent Firmware and GroundControl, with respect to calibrating the machine. Bar's been putting a lot of work into them.

---

Posted on **2017-05-06 19:00:17** by **Bar**:

@scottsm is being modest here and not mentioning that HE was the one who fixed the issue :-)

I have been putting in a lot of work, but so has the whole community. It's amazing how much things improve each week, so it's always worth grabbing the weekly version of both the firmware and software. That being said, there's still ways we can make it all better so let us know when ever you have an issue.

---

Posted on **2017-05-06 19:57:01** by **mcginniwa**:

Did the trick. Thanks @scottsm!

---

