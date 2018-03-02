## Stuck with the new calibration
Posted on *2017-05-03 12:13:40* by *gero*

Right motor wont turn to 12:00. Test test_electonics_firmware is OK. Test motor and encoders is also OK. On the screen in GC I have Kinematics: Unable to resolve x/y. No chance to bring the right sprocket to 12:00

---

Posted on *2017-05-03 12:25:05* by *gero*

Got rid of the Kinematics: Unable to resolve by running the .nc and clicking stop. That was not the problem with the right motor. Now i can see a B09 R.5 and B09 R-.5

---

Posted on *2017-05-03 12:27:40* by *gero*

The Konsole is interesting... trying to load .jpgs
right CCW
Sending: G91   

Sending: B06 L0 R0   

Sending: B09 R.5   

Sending: G90   

[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Measure Motor Height.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Sled Attached.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Ready To Calibrate Right Sprocket.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Measure Motor Height.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Chain Between Sled Mounts.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Chain On Right Sprocket.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Chain Between Sprockets.JPG
[ERROR  ] [Image       ]  Error reading file ./Documentation/Calibrate Machine Dimensions/Chain On Left Sprocket.JPG
[ERROR  ] [Image       ] Error reading file ./Documentation/Calibrate Machine Dimensions/Sprocket at 12-00.JPG

---

Posted on *2017-05-03 12:32:56* by *Bar*

Hmmm

It seems to me like these are two issues

I had a lot of trouble with the sprocket not turning issue. I thought I had a fix for it, but I guess not.

If you run a file do both motors move?

For the pictures issue do you see pictures on the slides as you go through the steps?

I just merged in a new bunch of changes many of which were your ideas :)

---

Posted on *2017-05-03 12:34:35* by *gero*

the motortest was fine, the pictures seems a linux thing, will test a new download

---

Posted on *2017-05-03 12:37:03* by *Bar*

What happens if you click one of the arrow buttons, do the motors move then?

I think what is going on is that the kinematics are getting locked up somehow so that the motor test will pass (because electronics are good) but it won't take any real commands. At least that's the behavior I was seeing yesterday.

For the pictures I'm a little lost as to the right solution. My guess is that it has to do with the way the paths are specified. That seems like it might be platform dependent. 

Let me know if you can figure out how to make the pictures show up

---

Posted on *2017-05-03 12:48:37* by *gero*

the pictures could be .JPG vs .jpg

---

Posted on *2017-05-03 12:51:39* by *gero*

confirmed, renamed one picture to JPG and that one shows.

---

Posted on *2017-05-03 12:52:52* by *gero*

The right motor still refuses CW and CCW

---

Posted on *2017-05-03 12:54:02* by *gero*

And on the arrows the same, only left turns

---

Posted on *2017-05-03 12:59:30* by *gero*

Where does GC store the settings, deleting those could be a quick fix

---

Posted on *2017-05-03 13:07:47* by *gero*

ok, renaming groundcontrol.ini to groundcontrol.oldini, created a new one and made now both motors refusing to turn to 12:00 :-)

---

Posted on *2017-05-03 13:21:58* by *Bar*

Hmm at least we got the pictures thing. What happens if you do the automatic chain length re-calibration?

---

Posted on *2017-05-03 13:24:13* by *gero*

Now it refuses to do about anything. The kinematics message is back. Uploading the firmware again shows in serial monitor:
[PosError:-1375.45,-1375.45]
[PosError:-1375.45,-1375.45]
unable to find position
ready
ok
Grbl v1.00
<Idle,MPos:-0.00,55364.24,0.00,WPos:0.000,0.000,0.000>
[PosError:0.00,0.00]
<Idle,MPos:-0.00,55364.24,0.00,WPos:0.000,0.000,0.000>
[PosError:0.00,0.00]
ok
<Idle,MPos:-0.00,55364.24,0.00,WPos:0.000,0.000,0.000>
[PosError:0.00,0.00]
<Idle,MPos:-0.00,55364.24,0.00,WPos:0.000,0.000,0.000>
[PosError:0.00,0.00]

---

Posted on *2017-05-03 13:29:04* by *Bar*

:-( That's what I was seeing yesterday

It's confused about the lengths of the chains which are stored in the EEPROM so they won't get erased by new firmware

---

Posted on *2017-05-03 13:30:33* by *gero*

calibrate chainlenth only did left motor

---

Posted on *2017-05-03 13:31:09* by *Bar*

That's very strange

---

Posted on *2017-05-03 13:32:00* by *Bar*

I've updated all of the picture names so at least those should show up now

---

Posted on *2017-05-03 13:32:45* by *Bar*

Ohhhh I've got an idea of what it could be!

---

Posted on *2017-05-03 13:33:01* by *Bar*

Give me a second, I'll make a test for it

---

Posted on *2017-05-03 13:53:10* by *Bar*

Give this firmware here: https://github.com/MaslowCNC/Firmware/tree/Gero-test

I'd recommend running it without the sled attached because it might do something weird.

First try clicking the arrow buttons to see if it moves, then try calibrate chain lengths - automatic and let me know what it does/prints

---

Posted on *2017-05-03 14:08:25* by *gero*

arrow buttons, only left motor, calibrate chain lengths – automatic, only left motor  [High-y](//muut.com/u/maslowcnc/s1/:maslowcnc:KtrK:highy.jpg.jpg)

---

Posted on *2017-05-03 14:08:59* by *Bar*

Did it say "Starting pos:  something" when running the chain length calibration?

---

Posted on *2017-05-03 14:10:56* by *gero*

No, only  [Chain-l](//muut.com/u/maslowcnc/s1/:maslowcnc:AGjT:chainl.jpg.jpg)

---

Posted on *2017-05-03 14:11:53* by *Bar*

Woah...interesting

Thank you. Let me keep digging

---

Posted on *2017-05-03 14:14:19* by *gero*

with Y at 25258 it has taken off to moon ;-)

---

Posted on *2017-05-03 14:16:06* by *Bar*

That's a notable accomplishment in itself! First Maslow in space :-)

I've gotten mine all wonked out too, so hopefully I'll be able to find out what's going on

---

Posted on *2017-05-03 14:18:52* by *gero*

As this could be a result of the buffer overflow, your time is better kept elsewhere. Could I not just wipe the arduino and pretend I am new?

---

Posted on *2017-05-03 14:27:04* by *Bar*

I think this is something new and important, I was seeing it yesterday but I thought I had it tracked down. 

Will you give it one more go to download the latest firmware from MaslowCNC/Firmware/tree/Gero-test and run the calibrate lengths test?

I think I got mine back to normal now, so hopefully it will do the same for yours. 

There should be a [message](//muut.com/u/maslowcnc/s1/:maslowcnc:8JZe:message.jpg.jpg) right at the top when it connects to make sure it's working right :)

---

Posted on *2017-05-03 14:49:27* by *gero*

Thanks for the greeting :-). Only left chain :-(  [Chain1](//muut.com/u/maslowcnc/s1/:maslowcnc:zIwl:chain1.jpg.jpg)  [Chain2](//muut.com/u/maslowcnc/s1/:maslowcnc:EVTW:chain2.jpg.jpg)  [Chain3](//muut.com/u/maslowcnc/s1/:maslowcnc:qCm9:chain3.jpg.jpg)  [Chain4](//muut.com/u/maslowcnc/s1/:maslowcnc:c5n1:chain4.jpg.jpg)

---

Posted on *2017-05-03 14:52:22* by *Bar*

:-(

---

Posted on *2017-05-03 14:53:23* by *Bar*

Give *Action -> Advanced -> Wipe EEPROM* a go and lets see if that makes it happy

---

Posted on *2017-05-03 15:01:43* by *gero*

Sadly no. It's 1 am now and work tomorrow. Need to postpone. Sorry, thanks for the support, Bar

---

Posted on *2017-05-03 15:05:15* by *gero*

Although the test.ino turned both synchron and test motors and encoders also passed all, I will still try the second motor shield tomorrow. Just to rule that out.

---

Posted on *2017-05-03 15:07:27* by *Bar*

Ok, sorry I couldn't figure it out tonight. I'll keep thinking and see if I can have something for you tomorrow.

---

Posted on *2017-05-03 17:46:15* by *Bar*

When you have a chance, take a look at this branch here: https://github.com/MaslowCNC/Firmware/tree/Gero-2

It should print out some values for the right axis pretty much all the time like  [this](//muut.com/u/maslowcnc/s1/:maslowcnc:8OoU:printvalues.jpg.jpg) 

I would be curious to know what those values look like when you would be expecting the right axis to be moving.

---

Posted on *2017-05-04 01:18:02* by *gero*

In 5 to 6 hours from now I should be ready to try that 8)

---

Posted on *2017-05-04 09:08:50* by *gero*

Right-axis:
0.00
-255.00

The first 2 always stay same, the 3rd increases with left move and decreases with right move. With chain calibration it counts upwards from 0 till 26.58 and then shows 0.00 mm  [Test2-1](//muut.com/u/maslowcnc/s1/:maslowcnc:fM4U:test21.jpg.jpg)  [Test2-2](//muut.com/u/maslowcnc/s1/:maslowcnc:oTXb:test22.jpg.jpg)  [Test2-3](//muut.com/u/maslowcnc/s1/:maslowcnc:TwqK:test23.jpg.jpg)  [Test2-4](//muut.com/u/maslowcnc/s1/:maslowcnc:BzwW:test24.jpg.jpg)

---

Posted on *2017-05-04 09:20:29* by *gero*

addition: test motor-encoders turns both and adds 0.10 to the first number each time

---

Posted on *2017-05-04 09:21:07* by *Bar*

Ok, those numbers look great which is good, but also means the problem is something else.

What happens if you run "Calibrate Motors"?

---

Posted on *2017-05-04 09:26:10* by *gero*

that runs both, without sled: L 32 -27 R 28 -31

---

Posted on *2017-05-04 09:26:44* by *Bar*

But the right one still doesn't turn if you say click one of the arrow buttons?

---

Posted on *2017-05-04 09:27:58* by *gero*

Now it does, left and right turn motor CCW

---

Posted on *2017-05-04 09:28:26* by *Bar*

WOOOOOOOOO

---

Posted on *2017-05-04 09:28:47* by *Bar*

:-) :-) :-)

---

Posted on *2017-05-04 09:32:44* by *Bar*

Ok, so here's what was wrong. Because you had a bad board the calibration process couldn't move your motor so the stored motor calibration was something bogus and so the motor wouldn't move. By re-running the calibration we overwrote it.

I need to add some sort of check in there so if the calibration is off it lets us know. It should send a message that says something like "Motor Calibration Error" because then you would know what to do right away.

Sorry for the trouble in tracking it down, but know that because you helped me figure out what was going on, we can solve it forever for everyone!

---

Posted on *2017-05-04 09:35:21* by *gero*

Always at your service. Thanks! So were do I start now? Calibrate motors first with sled and chain length without and measurements without?

---

Posted on *2017-05-04 09:37:22* by *Bar*

That sounds like exactly the right thing to do :-)

---

Posted on *2017-05-05 02:08:41* by *gero*

Not quite done :-(
It did solve that the right motor refused to turn, but:
After putting back the current firmware, the machine still does not know its position. Calibrate Motors and Calibrate Chain Length work well, but do not help. The error circle tries all sizes form xxl to xs and then 'Unable to find valid machine position. Please calibrate chain lengths.' Hold and continue is confusing. The picture shows that after another chain calibration, the message comes back.  [Pos-error](//muut.com/u/maslowcnc/s1/:maslowcnc:a8XN:poserror.jpg.jpg)

---

Posted on *2017-05-05 02:12:58* by *gero*

All arrows move the picture and XY coordinates but the sled is not moving.

---

Posted on *2017-05-05 02:20:05* by *davidlang*

unable to find machine position is actually a badly worded error message. What it really means is that it was unable to compute the correct chain lengths to use for the desired X/Y coordinates. In the firmware code, there is a guesscount variable that is tested to see if it has made too many guesses (this was 200, but a recent patch changes it to 100 and changes the error text to an even more misleading string) you can try changing it to a larger value to let the firmware try longer (
Kinematics.cpp ~line 217). There is also MaxTries in Kinematics.h that is set at 10.

Try setting these to higher numbers and see if that helps

---

Posted on *2017-05-05 02:21:51* by *gero*

Just noticed a 15hour new firmware. Testing that and if its the same I will try the higher value. Thanks!

---

Posted on *2017-05-05 02:24:16* by *gero*

motoroffsety = -1.09
sledwidth = 241.3
bedwidth = 2444
comport = /dev/ttyACM0
zaxis = 1
sledcg = 52
zdistperrot = 2.3
bedheight = 1222
sledheight = 119
motorspacingx = -1.04

Do the motoroffsety and motorspacingx look right?

---

Posted on *2017-05-05 02:27:06* by *davidlang*

no, motoroffsety is the distance between the motors and the top of the workspace, it should be about a foot, not negative

motorspacingx is supposed to be just shy of 10'

with those negative numbers, it will never compute things properly

---

Posted on *2017-05-05 02:28:16* by *davidlang*

default is 
            float motorOffsetY  = 463.0;                               //vertical distance from the corner of the work area to the sprocket center

            float D             = 2978.4;                              //distance between sprocket centers

---

Posted on *2017-05-05 02:37:24* by *gero*

Kinematics.cpp line 217, changed to 150, no difference. Kinematics.h max try set to 30. The error circle became much more viable and the attempts, but ends with same message. Or should I try the calibration again after the changes?

---

Posted on *2017-05-05 02:39:07* by *gero*

Ok, i'll do the full calibration set and check those number again.

---

Posted on *2017-05-05 04:45:22* by *gero*

So the machine is moving again :-). Strange findings on the way.
a) At 5 of 8, it showed a negative number for Vertical offset  [Meas1](//muut.com/u/maslowcnc/s1/:maslowcnc:BT7r:meas1.jpg.jpg)   , going back to set the sprocket to 12:00 for the chain length calibration and forward again this number had changed.  [Meas2](//muut.com/u/maslowcnc/s1/:maslowcnc:HWyD:meas2.jpg.jpg)
b) After the chain length the hated popup was back  [Pos-err](//muut.com/u/maslowcnc/s1/:maslowcnc:E9Zb:poserr.jpg.jpg)
c) All arrows work, the left-up creates a with distance growing error circle, clicking repeatedly makes it grow bigger then the sled  [Err-cir](//muut.com/u/maslowcnc/s1/:maslowcnc:MVkx:errcir.jpg.jpg) 
d) I am not in the center of the sheet on X (10mm left), this is new. Y is off since tweaking the bracket distance (now 20mm below)

---

Posted on *2017-05-05 05:42:03* by *gero*

Kindly ignore the X part of d). Tape-measuring the sheet again I am 4mm to the right of X0. There is a good chance that when turning the testsheet around, this tolerance was created by me.

---

Posted on *2017-05-05 05:45:30* by *gero*

Correction for d) GC Y0 is 26mm blow actual sheet Y0.

---

Posted on *2017-05-05 10:43:55* by *Bar*

Hmmm. Getting a negative value in step 5 of 8 is something I've seen too. That one should be fixed with the latest version. 

The positioning error in X0Y0 is interesting. I haven't measured exactly where the center of my sheet is so I don't have anything to compare to.. Using the newest version, how close to even square sides can you get on the test pattern?

---

