## makercam circle didn't go well
Posted on **2017-03-18 18:09:17** by **aalbinger**:

I put my temp kit together.  Chucked a pencil for a cutter and used a piece of dollar tree foam board to see the path.



I tried a 10cm circle drawn, profiled and exported as generic gcode from makercam.



The machine would move to the start point but then I could not find an imput that would make it continue on.



So next I tried one of the example gcode files that came with the groundcontrol windows zip file.  Seemed to work great.



Wonder what I/makercam did that groundcontrol didn't like.

 [Pencil-cutter](/images/ED/xo/EDxo_pencilcutter.jpg.jpg) [Test-gcode](/images/WF/Dv/WFDv_testgcode.jpg.jpg)

---

Posted on **2017-03-18 18:27:03** by **Bar**:

Hmm, maybe give using makercam in the "inches" mode, I haven't tested the centimeters setting nearly as thoroughly. Is there any way you can send me the file that didn't run? I can take a look at it and try to run it give you a better answer.



Great work getting everything put together so quickly!

---

Posted on **2017-03-18 21:28:23** by **blsteinhauer88**:

I'm not having any luck.  Bar I had to load the Python 2.7 for window 64 bit to run ground control.  I have rechecked everything and I only get the right motor to turn.  Changed motor sides, cables, etc.  The left will run only if I switch the cable plug on the Maslow board.  I made a circle in MakerCam sent the Gcode to GroundControl, and only the right motor would turn.  The cross hairs following the line also went off the line, then it stalled.  I tried then one of the premade Gcodes in GroundControl and this time the cross hairs followed the line but NO motors turned.  I am at a loss.  I ran so long one time even after I hit stop, the motor kept turning and I had to catch the router as the temporary clip pulled off.  I had to close the program to stop the motor.  Unknown it the board had an issue or what.  Remember mine was runnong backwards when it was the left motor?&quest;?&quest; Not sure what to do now.

---

Posted on **2017-03-18 21:49:11** by **Bar**:

Ok, I will add some code which will test the motors first thing tomorrow. 



What happens when you run the "Calibrate Motors" option?

---

Posted on **2017-03-18 22:12:04** by **blsteinhauer88**:

one motor will do it seems, several tests at different speeds, right one, then the left will start and just run the same direction, but not do the identical tests as the first one.  I know they will both work because of that, just won't work simulating a cut.

---

Posted on **2017-03-18 22:28:35** by **Bar**:

That does seem off. I would expect the same behavior from both motors. When the calibration is running, what text is displayed on the console? 



Can you confirm for me that the motors are plugged in to sockets 1 and 3 like in this  [Picture](/images/4v/K9/4vK9_picture.jpg.jpg)?

---

Posted on **2017-03-18 22:36:38** by **blsteinhauer88**:

Yes 1 and 3 like your photo.  the right starts first and only goes back and turns clockwise about 1/4 turn each time.  Then back counter clockwise.  Then the left goes, and does what I thinks it should, speed changes back and forth several times.  



Panel says for right side, testing (then a number) stall.   The left gave values for the test and finished with a -27

---

Posted on **2017-03-18 22:38:33** by **blsteinhauer88**:

[Image](/images/nb/C9/nbC9_image.jpg.jpg)

---

Posted on **2017-03-18 22:40:01** by **Bar**:

That looks perfect for the wiring

---

Posted on **2017-03-18 22:42:00** by **blsteinhauer88**:

its strange, the chain calibrate will run my right side motor, not the left like the other day.  and the calibrate motors will at least run both motors.  But if i just try and use the arrows to drive the motors, it will not run.  If I run a Gcode they wont run either.

---

Posted on **2017-03-18 22:47:17** by **Bar**:

The calibrate chain lengths should only run one at a time, it should be one motor for quite a while (two minutes?) and then the other for the same length of time. Do you see the right side motor run for good amount of time, then stop? 



I will write a testing module tomorrow which will test each motor in a clear way so we can learn more.



The way the whole motor calibration thing works right now is pretty buggy and it can cause strange behavior which is one of the reasons I want to rewrite it ASAP. It works once it's all happy, but can be finicky.

---

Posted on **2017-03-18 22:47:58** by **davidlang**:

my guess would be a problem with the encoder (or the wires from it)



did you try swapping the wiring between the motors and see if it's the wiring or the motor?

---

Posted on **2017-03-18 22:49:55** by **Bar**:

I feel a lot better about the hardware than I do about the software at this point. My bet is on a software issue.

---

Posted on **2017-03-18 22:50:04** by **blsteinhauer88**:

Yes, tried swapping wires to motors. 

The chain calibrate only runs on one motor, after about 2 minutes of a circle in the console from the zero point and getting larger on the screen.  It never runs the other motor

---

Posted on **2017-03-18 22:51:06** by **blsteinhauer88**:

Sorry guys I know its late.

---

Posted on **2017-03-18 22:53:54** by **Bar**:

That's alright, thanks for bearing with us while we get all the kinks figured out.



I don't have hardware at home to test, but I think the thing to do is that first thing tomorrow I'll write a test script that will tell us something conclusive.

---

Posted on **2017-03-18 22:54:46** by **blsteinhauer88**:

Ok cool

---

Posted on **2017-03-18 22:58:17** by **aalbinger**:

Interesting.  I compiled and ran https://www.arduino.cc/en/Tutorial/EEPROMClear?action=sourceblock&num=1



Then compiled and ran the firmware from github.  Calibrate chain length. Calibrate motors.



Then ran the gear looking example gcode without issue.  (pencil as a bit in the router)



Immediately following the gcode running my setup goes back to loading and displaying any running gcode but no movement in the machine.

---

Posted on **2017-03-18 22:59:54** by **aalbinger**:

motor calibrate still seems to run the motors fine.  The hardware seems good but the software kind of gives up beyond running the first gcode.

---

Posted on **2017-03-18 23:01:25** by **blsteinhauer88**:

I used the gear looking thing too.  The software was running but not the motors...

---

Posted on **2017-03-18 23:29:11** by **Bar**:

I think the issue you are seeing @aalbinger is different from what @blsteinhauer88 is seeing, but I could be wrong. 



I think the issue of both motors deciding not to move anymore after a while comes from an issue with the kinematics being unable to find a solution for the machine geometry. I just added the ability to change the machine dimensions on the fly a couple days ago and I think I may have broken something in the process. When you are in that state of being stuck, can you look at the Arduino [Serial monitor](/images/tD/RZ/tDRZ_serialmonitor.jpg.jpg)  and see what information the the machine is sending back? You will have to close Ground Control in order to open the serial monitor.

---

Posted on **2017-03-18 23:33:20** by **aalbinger**:

I'll give it a look after some sleep :)



1:30AM here and the garage temp just dropped below freezing so I think I'm going to call it a night.

---

Posted on **2017-03-18 23:48:03** by **blsteinhauer88**:

Just tested and loaded the Gear Gcode again.  Told it to run, and only the left motor ran, and it appears up is down with that also.  Right never ran so it drew a diagonal line. (using soap stone in router)..New to the programming thing, the serial monitor is just scrolling about 6 charactors of gibberish separated by ^.

---

Posted on **2017-03-18 23:53:28** by **blsteinhauer88**:

[Image](/images/AP/gU/APgU_image.jpg.jpg)

---

Posted on **2017-03-19 08:25:39** by **aalbinger**:

you will need to set the serial monitor to 19200 rather than the default 9600

---

Posted on **2017-03-19 09:32:14** by **Bar**:

@aalbinger is right, you want to set the serial monitor to 19200 rather than the default of 9600. 



You can make the change from the drop down in the bottom right corner  [Serial monitor](/images/Ge/1M/Ge1M_serialmonitor.jpg.jpg)  .



Good recommendation.

---

Posted on **2017-03-19 10:08:48** by **blsteinhauer88**:

Do we need to change the baud rate on the computer to 19200 also? Mine is Com5.

---

Posted on **2017-03-19 10:33:55** by **Bar**:

COM5 is the name of the port, and 19200 is the speed of the port. Changing the speed really just lets you read the characters. If it's reading at the wrong speed it will look like gibberish

---

Posted on **2017-03-19 10:39:08** by **Bar**:

Going back to the original question that this post was about of the circle not cutting right, I see exactly the same behavior where it starts and then stalls which is great news because that means I can figure out what's going on and fix it.

---

Posted on **2017-03-19 11:53:04** by **Bar**:

I think I've got it. If you grab the latest firmware from https://github.com/MaslowCNC/Firmware I think it might work :-)

---

Posted on **2017-03-19 11:54:29** by **Bar**:

I'm going to start a new topic for the only one motor turning issue that @blsteinhauer88 is having because I think that is an unrelated problem

---

