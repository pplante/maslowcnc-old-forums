## Calibration for different motor/gearbox
Posted on **2017-06-07 18:22:30** by **willishf**:



---

Posted on **2017-06-07 18:31:14** by **willishf**:

We have  built and began testing of maslow cnc where because we do robotics for middle/high school we already had a collection of motors with encoders. Using neverrest motor that you can purchase from andymark or servocity with 256:1 planetary gear box(banebot). We went through the dimension calibration but didn't see anything in user interface to adjust for different motors. For the z-axis it had adjustment for distance traveled to accommodate different routers. 

When we tested in the Y direction(going up) the distance was fairly close to the distance asked to move. When going the same distance in the X direction it was off by 3X. The repeatability of going in the opposite direction and returning to the same spot was very good. 

Looking for guidance on how to calibrate for a motor with different gear ratio and potential different ticks per revolution for motor encoder. Have no problem editing arduino code if that is the place to make the adjustments. Didn't hav e time to look at code before it was time to go home. 

Short video of the first movement test. 

https://goo.gl/photos/LKn1ZRJ4zYXYiTgF7

---

Posted on **2017-06-07 19:15:54** by **scottsm**:

I think what you’re looking for is in the firmware file CNC_functions.h:

#define ENCODERSTEPS   8148.0 //7*291*4 --- 7ppr, 291:1 gear ratio, quadrature encoding

Not sure, but I think that’s worth a try :)

It looks like you’re very close to having a working unit, keep us informed on how it goes. Do you have model numbers or links for those motors?

---

Posted on **2017-06-07 19:17:25** by **davidlang**:

the settings you are looking for are in Kinematics.h and CNC_Functions.h

specifically for the encoder, look for ENCODERSTEPS in CNC_Functions.h but you should look through both for the various definitions for machine dimensions.

---

Posted on **2017-06-08 08:31:36** by **Bar**:

Both @scottsm and @davidlang are right (they usually are), but there is an easier way too. In the ground control settings window click the "Maslow Settings" tab at the top and you will see an option for "advanced settings" which should have the options you need. Good luck and post pictures!

---

Posted on **2017-06-08 14:20:02** by **willishf**:

Yes the student working on this just informed me he found what was needed in advance settings.

For the motors and they have built in encoders so you need the custom cable. You would order it without the gearbox or could use the 60 gear box and setup a 1:4 chain drive for a gear box. 

http://www.andymark.com/NeveRest-s/550.htm

http://www.andymark.com/product-p/am-2992.htm

The 256-1 planetary gear box can be found at this link where you may need a different press on gear to make it work plus grease. If you call andymark they will know the details. Videos on youtube how to put it together. Not hard if you know what you are doing. 

http://www.andymark.com/Banebots-P60-256-1-Planetary-Gearbox-p/am-2878.htm

Any consideration for using stepper motors for precise control?  100:1 gearbox on stepper motor is $53 at amazon. http://a.co/j0Ql6wq Changes the motor controller requirements but plenty of those options in CNC space. 

The larger value of this project is an ar duino hat that can handle more than 1 amp motor load with built in support for encoders. I think you could get that board on adafruit and sell a few of them.

---

Posted on **2017-06-08 14:23:55** by **willishf**:

Just saw the reply for the following post about stepper motors. Software should be able to abstract out which shouldn't be that difficult. Loss of power I guess is a concern. With a 100:1 gear box you get incredible resolution that you can reliably control plus won't drop if you loose power.

---

Posted on **2017-06-08 15:44:04** by **davidlang**:

a planetary gear box can be back-driven, which means that when the motor is not being driven, the weight of the sled can cause the output shaft to move. This can be a problem.

a worm gear setup cannot be back driven, so it's much better for this use.

Yes, software can handle the change from brushed DC motors to steppers, someone just needs to write it  (patches welcomd :-) )

---

Posted on **2017-06-09 06:32:58** by **willishf**:

With the setup we have and planetary gearbox 256:1 it holds no problem.

---

Posted on **2017-06-09 14:28:30** by **davidlang**:

at 256:1 it is not going to backdrive easily, but there is a good chance that it will move a little bit (especially if the gearbox is under tension and is hit by vibration when powered off)

---

Posted on **2017-06-09 14:42:34** by **jwolter0**:

@willshf, are you a FRC team?  If so, what's your team number?  I'm with 1248.

---

Posted on **2017-06-09 15:35:41** by **willishf**:

Yes we are very active in FTC and support 35+ teams. We also do FRC where we try hard to not let mentors touch robot in the first four weeks..

---

Posted on **2017-06-09 15:36:38** by **willishf**:

Now that the gearboxes are starting to get some use we are getting drift. We are going to test with this wormgear from servocity https://www.servocity.com/wdg30p

---

Posted on **2017-06-09 15:38:02** by **willishf**:

jwolter the URL for our program www.tech-garage.org

---

Posted on **2017-06-09 20:37:57** by **jwolter0**:

Wow, that looks like a great program!  Thanks for the pointer.

---

Posted on **2017-06-10 16:11:02** by **aj-ji**:

Interesting to see other robotics teams here! I'm from 3452, although my team didn't purchase one, I did myself with intentions of letting my team use it during season for prototyping.

---

Posted on **2017-06-13 09:28:21** by **willishf**:

The servo city gearbox has a delrin gear that strips under the load.

---

Posted on **2017-06-13 09:32:43** by **Bar**:

:-(

---

Posted on **2017-06-13 10:01:16** by **TheRiflesSpiral**:

Oh bummer... is it a common diameter/pitch that could be replaced with a metal part?

---

