## Motors did work, but now they dont?
Posted on **2017-03-23 14:31:53** by **carlosrivers**:

I took these screen shots... [Screen Shot 2017-03-23 at 2](/images/9b/c0/9bc0_screenshot20170323at2.33.16pm.png.jpg) [Screen Shot 2017-03-23 at 2](/images/zs/v6/zsv6_screenshot20170323at2.33.34pm.png.jpg)

---

Posted on **2017-03-23 15:00:43** by **carlosrivers**:

So I did a calibrate motors, and they started turning. I was trying my mac laptop, so I was hitting test motors only.

---

Posted on **2017-03-23 15:54:29** by **scottsm**:

All good then, yes? 'Test Motors' seems mysterious to me, too.

---

Posted on **2017-03-23 17:48:41** by **blsteinhauer88**:

Check to make sure your wires have continuity in all the pins.  I had a broken orange wire in one and the calibrate would turn them both but the test would not and it would show a fail on the side with the broken wire.

---

Posted on **2017-03-23 18:26:32** by **rexklein**:

I have the same problem. I have covered every base. all equipment is good every config I could think of will run the right motor. I swapped cables various ways. motors and cables are fine. so its either a board issue or a software issue. 

like Carlos I was able to get it going although I had to reset a few times. but now the left motor just will not respond. The left motor stopped working several times during setup. But now it just will not come back.

---

Posted on **2017-03-23 18:37:52** by **rexklein**:

Here is how far I got till the left side just stopped altogether.  [2017-03-23_18-35-55](/images/YX/Sg/YXSg_20170323_183555.jpeg.jpg)

---

Posted on **2017-03-23 18:44:00** by **blsteinhauer88**:

I am not an engineer, that said, I am coming at this from the "user" standpoint.  Once all the cables had continuity, the next thing I tried was to go back to his set up directions, and start over with the calibrate motors, test motors, chain calibration, and it started working, but again, I did have a bad wire that was replaced.  If it is  turning the motors during the calibration, then not during the test.  That may be a "Bar" issue.  Sorry that is all I got.

---

Posted on **2017-03-23 18:50:44** by **rexklein**:

I spent about 7 hours I tested every possible combo I even went and bought a cheap windows tablet to avoid usb cord issues. when the left side dies it is just plain dead. I am testing one last hypothesis I powered down everything to see if a cold start works it may be something on the board that after heating up fails. In the morning I will start fresh and see if a very cold board works if it does then I will buy myself a beer.

---

Posted on **2017-03-23 20:11:10** by **carlosrivers**:

@Rexklein, It can be very frustrating. I am not sure what exactly I did. I just kept trying to updated the firmware on Arduino, switched the motor cables, I too used a different computer, and then I hit calibrate motors and they came to life. I am currently working on my sled, which has me thinking too hard lol.



Once I have this entire thing figured out I am going to Go-Pro a youtube video of the entire process, from software to building the machine. I know someone else is going to appreciate that.

---

Posted on **2017-03-23 20:15:36** by **rexklein**:

@carlosrivers, It's funny yes I got stuck today but when its all said and done it was still fun, like trying to solve a puzzle.

---

Posted on **2017-03-24 07:46:33** by **Bar**:

That sounds frustrating and I want to make sure we can figure out what's going on so nobody else has to struggle with it. 



Do you have suggestions about how I can try to replicate the issue so I can figure out what's happening?

---

Posted on **2017-03-24 10:55:07** by **rexklein**:

Actually do you know what the data rate etc should be for the com1 port

get this vibe that in the firmware there is a bug that if there are any deviant com settings there could be a break in the code. My ability to measure chains worked after I swapped com ports but I was not able to repeat the trick.

---

Posted on **2017-03-24 11:36:42** by **Bar**:

The data rate should be 19200. I think you are right that the serial connection is a little too touchy right now. The mystery to me is what settings are giving us a situation where the software says it is connected so it's still receiving positional information from the machine, but it won't move. 



The issue could have something to do with when the machine indicates that it is ready for the next command. Ground Control won't send a new command until the machine asks for one, so if the machine isn't indicating that it is ready under some circumstances it could lock up.

---

Posted on **2017-03-24 17:50:33** by **rexklein**:

Hate to say Bar I think I the left port is dead. I can hook the left motor to the zaxis port and is passes. I reloaded firmware and ground control. Nothing has any effect.

---

Posted on **2017-03-24 18:52:54** by **jbarchuk**:

Bar, troubleshooting tip. A user doesn't need a scope to do some simple probing. With the GC in a known 'test' state, you can name what voltages should be on each pin,  Obviously a multimeter can't see waveforms but that would prove a basic level of  pin alive/dead status.

---

Posted on **2017-03-25 08:11:10** by **Bar**:

We'll get you a new board in the mail ASAP. Can you email your address (or just name) to bar@maslowcnc.com so I know who to send it to? While it's in the post, let's see what we can learn. 



@Jbarchucj is right, I think the best way to do that is to put the machine in a known state and probe the pins. I'll write a firmware version today which does nothing but command all four motors to spin and write up a guide about what the voltages on each pin of the wire should be. Do you have a volt meter we could use for testing?

---

Posted on **2017-03-25 09:48:40** by **rexklein**:

I have a voltmeter

---

Posted on **2017-03-25 09:50:48** by **rexklein**:

your sending me the z axis anyway I emailed back send a board as well.

---

Posted on **2017-03-25 11:26:04** by **Bar**:

Unfortunately, I mailed your z-axis yesterday :)

---

Posted on **2017-03-25 13:28:29** by **Bar**:

I just added a new firmware version which just commands the motors to run. I don't think we need the voltmeter, because all we would be looking for is 12v which we can detect easily by seeing the motor turn. 



Give this version [here](https://github.com/MaslowCNC/Firmware) a try, but instead of installing the normal firmware, install  [test_electronics_firmware](/images/JJ/em/JJem_testfirmware.jpg.jpg) . With the firmware installed, try plugging the same motor into each socket 1 at a time and let me know what happens. The goal is that in three of them it will turn for 1 second, stop for 1 second, and then reverse on and on forever.

---

Posted on **2017-03-25 13:47:36** by **rexklein**:

great super easy test

the port for left motor is indeed dead in this test as well

---

Posted on **2017-03-25 13:50:06** by **rexklein**:

z-axis and right port work perfectly fine. that a super easy test. I would actually put that as a ground control test great way to trouble shoot

---

Posted on **2017-03-25 13:55:08** by **rexklein**:

I tested with both cables and both motors. That failure is with the left port no question

---

Posted on **2017-03-25 13:55:53** by **rexklein**:

I looked at the solder on the board and it looked very clean and uniform.

---

Posted on **2017-03-25 14:05:21** by **Bar**:

Thanks for doing that. It looks like we've got it confirmed as a bad port. 



What happens with the far right port (the 4th one)?

---

Posted on **2017-03-25 14:23:35** by **rexklein**:

dead

---

Posted on **2017-03-25 14:24:09** by **rexklein**:

well At-least nothing happens

---

Posted on **2017-03-25 14:36:15** by **Bar**:

Gotcha. That's what I would expect. Thanks for checking. 



Will you shoot me a private message with your real world name or address and I'll send you a new board with express shipping!

---

Posted on **2017-03-25 17:02:28** by **jbarchuk**:

> @Bar

> I just added a new firmware version which just commands the motors to run.

Nice. :)

> I don't think we need the voltmeter, because all we would be looking for is 12v which we can detect easily by seeing the motor turn.

I meant measure the signal pins.

If there's no 12v then nothing works anyway.

If there's a wrong voltage on a signal pin, or no voltage, then it's an issue, that still might be either board or motor but at least that has to be fixed -before- looking at software. There's no sense chasing software ghosts when the hardware has no chance of working.

---

Posted on **2017-03-25 17:44:34** by **rexklein**:

The next time anyone does a rebuild I suggest trying out that firmware test. After experiencing it I think it should be part of the process of setting the machine. It would cover a lot bases from uploading firmware for the first time to verifying all cables boards and motors are in good condition. its a perfect equipment bench test. maybe not a required thing but a strongly suggested thing.

---

Posted on **2017-03-25 17:45:39** by **rexklein**:

would make tech support a lot easier if Bar knew everything performed during that phase.

---

