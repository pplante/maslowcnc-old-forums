## Machine Settings
Posted on **2017-02-15 09:32:04** by **garyw17**:

There seem to be a number of variables in the firmware that need to be adjusted based on machine hardware and size.  I am unclear on exactly what some of them are.  What I have found so far is:



CNC_Functions.h

  #define DIST_PER_ROTATION      .... needs to have sprocket # of teeth entered



Axis.cpp

  #define NUMBER_OF_ENCODER_STEPS  .... needs to have encoder steps entered



Kinematics.h

  #define ORIGINCHAINLEN    .... I am not sure exactly what this variable is 



Then there is a section with this data.  I assume I update with my machine dimensions?

            //geometry

            float l = 310.0;                               //distance between sled attach points

            float s = 139.0;                               //vertical distance between sled ...

            float h = sqrt((l/2)*(l/2) + s * s);           //distance between sled attach.....

            float h3 = 79.0;                               //distance from bit to sled center of mass

            float D = 2978.4;                             //distance between sprocket centers

            float R = 1 0.2;                                //sprocket radius



Kinematics.cpp

I see a section under //#define OLDKINEMATICS

The first 2 are size of the workspace (4x8), but I am not exactly sure what the other 4 are, or if they need to be updated by me..



#define MACHINEHEIGHT    1219.2 //this is 4 feet in mm

#define MACHINEWIDTH     2438.4 //this is 8 feet in mm

#define MOTOROFFSETX     270.0

#define MOTOROFFSETY     463.0

#define SLEDWIDTH        310.0

#define SLEDHEIGHT       139.0



Are there any other parameters I need to be aware of and update?



Thanks for any input.

---

Posted on **2017-02-15 10:11:30** by **Bar**:

Yes! All of those things are important. I'm going to move all of those settings out into the user setting panel in Ground Control to make them easier to edit. 



I've got a feature request filed for that here: https://github.com/MaslowCNC/GroundControl/issues/75



Feel free to add any other machine settings you would like to be able to edit from Ground Control and I'll add them.

---

Posted on **2017-02-15 13:29:20** by **garyw17**:

So what exactly is ORIGINCHAINLEN?  And is MOTOROFFSETX and MOTOROFFSETY the distance from the top corner of teh work space to the sprocket center?

Thanks

---

Posted on **2017-02-15 15:04:34** by **Bar**:

ORIGINCHAINLEN is the length of the chain when the the router is centered. It can be calculated from the machine dimensions but right now it is #defined because of the way I calibrate (I have one link painted white which I use for a reference, a better system is coming soon see this issue: https://github.com/MaslowCNC/GroundControl/issues/73 ).



MOTOROFFSETX and MOTOROFFSETY are exactly what you guessed. They are the distance in x and y from the corner of the work space to the motors.

---

Posted on **2017-02-15 15:32:51** by **davidlang**:

so we have the spacing between the motors and the distance from the motors to the top corners of the work area. Is there also a height parameter for the work area that would let it know how far down from there it can go?

---

Posted on **2017-02-15 15:46:28** by **davidlang**:

As a side note, the numbers listed above give a ~18" vertical spacing. the simulation calls for an 11" spacing, and then the bit is ~5.5" below the chain attachment points, so there should be ~3" of vertical play available (if the math is right) before the motors run out of power

---

