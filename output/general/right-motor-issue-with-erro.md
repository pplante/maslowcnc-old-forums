## Right motor issue with error
Posted on **2017-07-16 12:47:37** by **mribble**:

I'm trying to setup my machine for the first time.  I got to "Calibrate Chain Length - Automatic" test and I'm having issues with the right motor.



During the first step where I need to get the sprocket tooth to 12:00 position I can turn both motors so both motors movement works.  However, during this calibration step only the left motor turns.



In the command line I'm seeing this error: "One Machine Position Report Command Misread".  Is that a normal error?  I'm not exactly sure how the encoding works with the motors, but I wonder if positional movement works, but the encoder that determines position is not working?



I tried swapping the left and right motor plugs on the PCB and then the right motor moves during the calibration, but the left one then fails.  This seems to indicate an issue with the software or a PCB issue.



Does anyone have an idea of what this could be?



Bar, when asking these kinds of troubleshooting questions do you prefer them on the forums or should I contact you via email?

---

Posted on **2017-07-16 13:26:53** by **gero**:

http://www.maslowcnc.com/forums/#!/general:right-motor-issue

http://www.maslowcnc.com/forums/#!/general:calibrating



Since this is number 3 a issue should be opened on Github. General narrowing in and discussions i think should be here in the forum. But tracking 3 is kind of challenging. On Github they can be marked as duplicates.

---

Posted on **2017-07-16 13:27:08** by **Bar**:

Lets' figure out what's going on. The first thing to try is to run Actions -> Test Motors/Encoders. That will let us know if we have an issue with the electronics.



The "One Machine Position Report Command Misread" is pretty normal especially when the machine first connects. Unless you are seeing it all the time I don't think that's our issue.



It's possible that the issue is just that the instructions aren't clear enough. The normal behavior is for the left motor to fully measure out the chain, then for the right motor to do the same so I wouldn't expect any moment from the right motor until the left motor is finished. Do you see the left motor finish moving, then the right motor go?

---

Posted on **2017-07-16 13:28:22** by **scottbramall**:

On mine the Test motors seems fine.

---

Posted on **2017-07-16 14:35:04** by **mribble**:

The test motors also passes for me.



Here is my log file which shows the test passing (I haven't hooked up my z axis yet so that is expected to pass: http://glacialwanderer.com/files/2017/maslow_log.txt



Here is the command line output which shows the odd error: http://glacialwanderer.com/files/2017/maslow_command_line.txt



I'm using a microsoft surface book running win10 which has been pretty reliable.  I also have a workstation used for development I could try, but haven't yet because I'd need to unscrew the motors.



I just used the python binaries, but I can build from source if there is something you want me to try there.



I have an active github account so moving  this there is fine with me.  Just let me know where you want this discussion to happen.

---

Posted on **2017-07-16 14:42:45** by **scottsm**:

During ‘Calibrate Chain Lenght - Automatic’ the left motor runs for several minutes before the right motor runs. The chains are measured one at a time.

---

Posted on **2017-07-16 14:50:19** by **Bar**:

Thank you for sharing those log files, that's a great thing to be able to reference.



It seems like this right motor issue is wide spread enough that we should make a github issue for it and discuss it there so we can make sure all the discussion happens in one place. I'll make one right now.

---

Posted on **2017-07-16 14:57:20** by **Bar**:

I've made an issue here: https://github.com/MaslowCNC/Firmware/issues/262

---

Posted on **2017-07-16 17:14:09** by **Bar**:

I've made some progress on tracking this one down, so if anyone who is seeing the issue would be willing to check out that github issue and let me know if the tests there fix the issue for you, I would be much obliged

---

