## Calibrate Chain Length
Posted on **2017-02-18 13:55:39** by **garyw17**:

Can anyone please explain exactly what the calibrate chain length button does in the ground control software?

Thanks.

---

Posted on **2017-02-19 10:01:12** by **scottsm**:

I think @Bar is investigating a way for the machine to 'measure itself', the distance between the motors. Not something one would do often, I guess, but if one had a full sized base for full sheets and a smaller base for odd sizes and everyday use it could be useful. Also useful when trying various geometries of 'motor-mount/bunny-ears' as discussed elsewhere here.

 In the firmware repository in cnc_functions.h, it looks like there are some stubs for the codes 'B01, B02' sent by 'calibrate motors' and 'calibrate chains length' buttons. Interesting to see how the software ties the pieces together 😀

---

Posted on **2017-02-20 10:43:24** by **Bar**:

@scottsm is correct. The machine needs to know the lengths of its chains when it first powers on, after that the length is stored in the nonvolitle memory so disconnecting power or flashing the firmware won't make it forget. 



The obvious way to get the initial chain lengths is to ask you to measure them and enter the number, but there's going to be some error there. Instead I would like to have the machine feed out a set amount of chain when you first set it up. You can read about the plan here: https://github.com/MaslowCNC/GroundControl/issues/73



Feel free to add any suggestions for improving the process.

---

