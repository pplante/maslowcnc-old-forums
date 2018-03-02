## Can you use All_Parts_Laid_Out.svg to generate a gcode file?
Posted on **2017-05-02 22:48:29** by **mcginniwa**:

I'm a little under the gun time wise and wondering if I can use the combined parts file rather than individual svg files for each frame part.



Bad idea?



Is this file even something that is ready to be tuned into a gcode file?



I'll probably do a test run on a gcode for an individual part before digging into this, but just wanted to know if this is workable.

---

Posted on **2017-05-02 23:14:41** by **scottsm**:

I'd hesitate to lump all the parts into one file since one file becomes one cut session. Lumping the angles and braces where accuracy isn't as important, maybe.

---

Posted on **2017-05-02 23:34:25** by **mcginniwa**:

The downside of cutting the final sled then using it to cut remaining parts is that it adds another round of measuring and calibration on the temp frame.

---

Posted on **2017-05-03 07:42:56** by **Bar**:

I agree with @scottsm you can do it, but it's nice to have different parts as different files so if something goes wrong with one you can easily restart.



If you really need to get things done fast I would say just cut the sled and arms on the temporary frame and fake the legs. The angle is not critical and cutting out all those braces takes a while. Maybe cut one of each and then copy it by hand.

---

Posted on **2017-05-03 13:52:21** by **mcginniwa**:

Thanks. I'll run with that plan.

---

