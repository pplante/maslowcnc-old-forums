## Scratch Built Machine
Posted on *2017-03-09 11:10:06* by *garyw17*

Hello,
Just thought I'd give an update for anyone not on the kickstarter buy list who may be thinking about trying to scratch build their own machine.   I posted earlier about trying a small Pololu motor with built in encoder, and that the gearbox failed.  I realize now that motor was woefully under powered compared to the Maslow motors.  I was not able to find any thing comparable to Maslow motor with a  worm drive and built in encoders, so ended up buying separate motor (Ebay Item ID: 162355094908 )and encoders (Item ID: 171947459869).  The encoders are 600 ppr (so much lower than standard Maslow but hopefully still good enough), and the motor has roughly twice the torque as the standard Maslow motor mentioned by Bar  But of course has a much higher current draw, so I don't think the L298 motor controllers will work.  I ended up buying a 10 amp dual motor controller for about $26 (Ebay Item ID: 171947459869).  In early testing I accidentally had a wood screw in the way of the motion of the sled and was looking the other way.  I did not notice any change in the motor so und when the sled hit the screw..... just a loud snap as it broke the screw off cleanly.  Clearly there is plenty of power here.  

I am driving the whole thing using an old 12 volt deep cycle battery from my camper.  I do not yet have a router (or Z axis drive).

For mounting the motors and encoders, I bought a 3x3 x 0.25 thick aluminum angle piece, and a 1.5x1.5 x .125 thick aluminum square U piece from www.online metals.com.  The angle piece holds the motor, and the U piece mounts to the face of the angle piece and holds the encoder, which connects to the motor via a small aluminum coupler.  A few pictures are attached showing the parts, and the final assembly.  I did not have access to a lathe or milling machine, so all parts were made with hand tools and a small drill press, but you do have to be pretty careful laying things out to make it all fit.

Unfortunately last night I broke the power adapter for my Lenovo tablet, so testing is done for a couple days while I wait for a new one.  I was successful at moving the motors around and reading the encoder outputs by writing a small Arduino script, but did not get the actual Maslow software to control it yet.  There are a couple of challenges to resolve.  Since my encoders are mounted facing the motors, they actually turn in the opposite direction (CW versus CCW).  I think.  Depends on which side you look from I guess.  So my pulse count may (or may not) go in the wrong direction when the motors turn.  Maybe flipping the encoder A/B channels fixes this... or maybe not.  Also the L298 motor controllers have two pins which control direction of the motor with the H bridge.  This new motor controller only uses one pin.  High for one direction.... low for the opposite direction.  I tested that with my simple script and it works, but I still need to figure out which one of the pins coming off the Arduino to connect to each motor.  Sorting out these connection issues is not so easy (at least for me as a non-software type guy).

That all for now.  If anyone has any advice I appreciate it.  Otherwise, I will update when I (hopefully) get things sorted.

 [Front_view](//muut.com/u/maslowcnc/s1/:maslowcnc:4Glz:front_view.jpg.jpg) [Parts](//muut.com/u/maslowcnc/s1/:maslowcnc:chmL:parts.jpg.jpg) [View1](//muut.com/u/maslowcnc/s1/:maslowcnc:COR6:view1.jpg.jpg) [View2](//muut.com/u/maslowcnc/s1/:maslowcnc:nI0K:view2.jpg.jpg)

---

Posted on *2017-03-09 11:37:18* by *nloding*

Excellent, I *just* asked this in another thread. Do you have specs for the motors that Maslow uses (model, torque, etc.)? I've searched but can't find anything. I'm most concerned about those and the chains. Curious if created your own Arduino shield or used an existing one?

---

Posted on *2017-03-09 11:42:07* by *garyw17*

Bar mentioned that the motors were (I think) about 30 kg-cm of torque at 30 rpm.  The ones I picked are about double that.  I did not use a shield.  I just connected the motor controller directly to the Arduino.  Idon't think I shield is needed.    I bought the #25 chain off ebay (need about 11 to 12 ft I think).  Bar uses a 10 tooth sprocket, but I went with 12 since that fit my 3/8 drive shaft (bought that from McMaster-Carr)

---

Posted on *2017-03-09 11:53:17* by *Bar*

This is AWESOME! Amazing work!

I think you are in some good luck with the encoder/H-bridge differences. Swapping the A/B channels will work to reverse the direction (good guess), and while our H-bridge has two control pins and yours only has one, the way we are using them the two pins are always opposite so forward is High-Low and reverse is Low-High so you should be able to get the right behavior using only one pin.

Using both pins would allow us to do active breaking (I believe), but I don't see a need for that.

Again, great great work. Keep us posted!

---

Posted on *2017-03-09 13:32:27* by *garyw17*

Thanks Bar.  One other thing related to the shield question from nloding.    I am new to Arduino (I never even heard of it until after I saw the Maslow), but I believe the shield in this case is the motor controller.  So if you had a shield designed for the Maslow, you simply plug it in and go.  It also makes for nice packaging.  In my case though I bought an external motor controller that is not an Arduino shield as I mentioned.  I don't think that causes any problems, other than the fact that it has to be connected back to the Arduino mega.  If you look at the firmware code, you can see which pins on the Arduino are used to control the motors and read the encoders.  You then just need to mount your controller board near the Arduino, and make up some connecting wires.  This was also new to me, but I found that www.pololu.com sells the little connectors that work with 0.1 pin spacing (I have no association with Pololu, and there are probably other sources as well).  You need both male and female crimp pins (they come in packs of 100).  They sell plastic housings that the n allow you to make up connectors with as many pins as you want.  These are very inexpensive, so I bought 1,2,3,4,5, and 6 pin housings.  I also bought their crimper tool which was a little expensive ($35 or so I think), but it works well.  This also let's you make up the wires and connectors that have to run out to encoders to provide power and signal.  If anyone is interested, I will post the wiring/pin connections I used.  After I get it sorted out that is.

---

Posted on *2017-03-09 15:31:28* by *jbarchuk*

> @garyw17
> the shield in this case is the motor controller.
This one-board solution is the best decision on several counts related to -efficiency-. The first and most important is that Bar et al. don't have to deal with supporting multiple different Arduino manufacturers, maaany more different kinds of motor boards, and random scavenged cables. I remember one comment Bar wrote that when looking at some sample chains one chain was clearly better than the other and that's the one he went with. That takes a variable out of the equation.
Next is efficiency for the user. There are a LOT of people here who don't solder or know how to figure out how to use a crimper, or how to route and protect cables in a machine environment. The fewer wires flapping in the breeze the better EXCEPT for those supplied for the machine that fit as designed.
Related to that, this is designed to be as plug-n-play as possible. The -intent- of the design is that the user should be able to build the machine and operate it, without having to 'figure out' the operations part of it other than learning  the UI and getting the g-code from the design software to the controller.
The more control the designer has over things, the fewer variables introduced by users. That will happen anyway once in a while. Fewer variables are better when you're dealing with 1000 users.

---

Posted on *2017-03-09 16:51:44* by *garyw17*

Yes, I absolutely agree.    If I could have just bought the kit for $350, that  is the smart move.  But, I missed the kickstart, and didn't want to wait.   So I'm just sharing in case someone else is in a similar position and wants to tinker.

---

Posted on *2017-03-12 16:41:44* by *garyw17*

I have run into a problem, and can't figure out what is going wrong.  Hopefully someone with a better understanding of the software can offer a suggestion.  I believe I have things connected up correctly.  But when I try to move the router using the arrows in ground control, I see the white circle with cross hatches move in the software in the commanded direction and distance, but the router itself does not move.  I even read in some simple gcode for a square, and when I press "run" the white circle follows a path around it as expected, but again no actual router motion.  The position output in the gui tracks the white circle.  I don't see a red circle (thought I remembered that from an earlier version?)

However, if I run the motor calibration I get what I expect.  First the left motor lets chain in and out for a few minutes, then the right.  Looking at the gui afterwards, I see the calibration was successful and it lists the results.  So I think the software must be reading the encoders OK, and can certainly command the router to move.

I also wrote a separate simple A rduino script that allows me to set the motor speed and direction and writes the encoder output to the serial monitor. as a check  When I look it shows that both encoders are behaving as expected.

I m using the firmware and ground control downloaded from the pinned directories this morning.  Running on a windows 10 laptop.  The only mod I made was to change the encoder to 600 ppr and the sprocket from 10 teeth to 12.

I think the fact that the router moves during motor calibration but not via the arrows is a clue.  I suspect the calibration uses a direct command to move, while the arrows instead move the desired position target, and teh PID control is supposed to take over and move there.  But I m not sure if my problem is hardware or software.

---

Posted on *2017-03-13 10:01:36* by *Bar*

I've seen that issue too. It's not a hardware thing, it has to do with the calibration not being correct. 

If you aren't using the most recent version of GC and the firmware, I recommend grabbing them because I've been messing with that stuff in the last week.

You are spot on that the calibration routine commands the motors directly while the regular motion uses the stored calibration. You can make the firmware ignore the calibration entirely by deleting lines 75-76 in the file GearMotor.h which are:

"
//linearize the motor
  speed = _convolve(speed);
"

When you run the calibration, what numbers do you see? My guess is that one motor or encoder is hooked up backwards.

---

Posted on *2017-03-13 10:05:44* by *garyw17*

I am running the most recent code (as of yesterday morning). I think it puts out two numbers.... one for the left and then one for the right?  I got +50, and -29.  Should the second number be negative?

---

Posted on *2017-03-13 10:11:35* by *Bar*

Those actually sound spot on. The second one should be negative. If something was reversed you would get something like +255/-255.

If you remove those two lines of code, what happens? Are you using an Arduino Mega2560?

---

Posted on *2017-03-13 10:18:09* by *garyw17*

Thanks.  Yes, mega 2560.  I had a couple other reasons to think  I was connected right at the moment.  I noticed back in my days with the pololu motors that when connected correctly, both motors would "come alive" when I upload the firmware.  By that I mean they would move back and forth a bit.  If they were connected wrong, there would either be no motion, or one of them would take off.  And when I run the motor calibration, if connected wrong the motion tends to just run off the table.  I find that when I change the wiring/pin connections I have now, I run into those same issues.  Connected as is, those issues are OK.  I'll try deleting those 2 lines and post again shortly.

---

Posted on *2017-03-13 10:42:40* by *garyw17*

I do not see any change after deleting the 2 lines.  I also re-ran the motor calibration, and got about the same values as before.  I do notice that the first time (only the first time) I push the up arrow button the motors make a short "hum", like they are starting.  But then nothing.

---

Posted on *2017-03-13 10:53:03* by *TheRiflesSpiral*

Outside looking in here... is it possible that the calibration routine and the normal movement routine use different pulse width? That would explain the hum without a movement.

---

Posted on *2017-03-13 11:33:30* by *garyw17*

The "hum" lasts only a fraction of a second the first time I push  the up arrow.  After that, nothing.  As you probably know, the pulse width modulation (pwm) controls the speed, so yes, for sure the calibration and normal movement use different values.  The pwm value from normal operation comes from the PID routine, which looks at the error between target position and current position.  To get current position it has to read the encoders, just like it does in calibration.  Since the target position obviously moves when I push the arrow buttons (I see that that white circle with cross hairs moves), it would seem maybe it isn't actually reading the encoders to get current position.  But then how was it able to run calibration?

---

Posted on *2017-03-13 12:42:45* by *TheRiflesSpiral*

Right... what I was suggesting (poorly :D ) is that it's waiting for an encoder pulse but it never comes. That might be because PW isn't long enough to cause a move, or maybe the pin on which the pulse comes in is defined in two places? (And is wrong in one)

Also, a little bit of learning on my part... Am I correct in saying the encoders don't indicate a position, only a change in position? The position is actually held in software as a result of the increment/decrement of a count due to pulses from the encoders. (which is used to calculate position) Have I got that right?

If that's the case is it possible the variable holding current position is being overwritten with the target position so the net pulse expectation is 0?

Sorry, I know these are stupid, basic things to check but I always go back to KISS when these kinds of things trip me up.

---

Posted on *2017-03-13 13:04:18* by *garyw17*

When it reads the encoder, the command looks something like
_encoder.read()/NUMBER_OF_ENCODER_STEPS)
The encoder.read function returns a count of number of pulses, which obviously gets divided by the encoder NUMBER_OF_ENCODER_STEPS (600 in my case) to get a number of revolutions.  So it is not waiting for an encoder pulse.  It just reads the encoder when that info is needed.

So I think what happens is that the encoder count gets zero'ed out at the beginning.  There is a variable (something like ORIGIN_CHAIN_LENGTH) which I think comes in here.  Even though we are at zero encoder count, the software knows what the chain length is.  And then it can calculate the new chain length at any time by just reading the present value of the encoder.

For debugging purposes, when I wrote a simple Arduino script to move the motors around, I wrote the encoder count out to the serial monitor using this.  But unfortunately I can not seem to use the serial monitor in Arduino at the same time that ground control is running, since ground control is the serial connection.  If I could find s ome way to monitor the outputs, it might help me debug.  Maybe I can modify the firmware sketch to export the values it is using in some fashion, but I'm not sure how to do that at the moment.

---

Posted on *2017-03-13 13:34:00* by *Bar*

I have a new theory about what's going on.

Have you run the "Calibrate Chain Lengths" option? The way it works is that you hook the first link of each chain onto the top (12:00 o'clock) tooth on each gear and then click "Calibrate Chain Lengths". The motors will then measure out the correct length of chain to setup the machine the first time. I was experiencing the behavior you described with a fresh Arduino before running the chain length calibration.

Sorry for the confusion, you are a week ahead of schedule so we're missing a lot of necessary documentation.

@TheRiflesSpiral is right that the encoders don't indicate a position, but only a change in position. Because of that, they need to have a known starting ie first link at 12:00 o'clock. After that the length is stored in the Arduino's EEPROM which is preserved when power is disconnected or even if the firmware is upgraded so you shouldn't have to do the calibration very often.

Huge props to @TheRiflesSpiral for guessing what was up without even ever touching hardware!

Let us know if that changes anything.

Also , keep an eye on the chains as they are starting, because they can get caught on the sprocket and wind themselves into a ball especially right at the beginning. Once there are a good number of links hanging down they tend to take care of themselves. The calibration will do the left chain first.

---

Posted on *2017-03-13 13:38:51* by *garyw17*

Ahhh.   No, I did not do that.  Just so I am clear, I should first disconnect my sled, and then place the first link of each chain on the sprockets, and it feeds the chain out towards the sled.  Should I try to get a tooth pointed straight up when I start?

---

Posted on *2017-03-13 13:45:49* by *TheRiflesSpiral*

Aw, shucks... yer makin' me blush. :D

---

Posted on *2017-03-13 15:40:28* by *Bar*

Yup, disconnect your sled and place the first link of each chain at 12:00 and it will feed towards the sled. Having a tooth pointed straight up would be ideal. There's an issue filed to add that behavior.

You can run the process without the chains on at all if you want just to see how it goes.

---

Posted on *2017-03-13 17:14:49* by *garyw17*

OK.  The tip about checking it without a chain was good. Saves a lot of time.  So it looks like maybe I was not connected up right after all.   Depending on encoder and motor connections, sometimes the chain feeds out smoothly, and sometimes the sprocket oscillates back and forth, letting out a small amount of chain at a time.  Would I be correct in assuming it should be a smooth operation, and the oscillation indicates something is backwards?  The other issue is it seems to let out way too much chain.  I think your original chain length was 1650 mm, so at about 75 mm per rev I should get about 22 revs of the sprocket?

---

Posted on *2017-03-13 17:28:33* by *Bar*

The oscillation is probably caused by the PID controller not being tuned right. Because your motors are different they may behave differently, but I would expect the calibration process to take care of that. Line 45 of the file CNC_functions.py will let you set the size of your sprockets which should at least fix the correct length of chain being measured out and could help with the PID tuning.

---

Posted on *2017-03-13 17:58:48* by *davidlang*

given the difference between 8k pulses/rev and 600 pulses/rev, it is very possible that some timeout/time-constant in the pid controller will need to be adjusted as it takes >10 as long to get a pulse

---

Posted on *2017-03-13 21:19:15* by *garyw17*

You may well be right about the encoder pulse count, but after a couple hours of reading thru the sketch files I haven't found anything yet.  I found a function in axis.cpp called  speedSinceLastCall that only depends on reading the encoder without correcting for the number of steps, but I think it is only checking to see if the motor stalled.  I scaled it up anyway based on the ratio of encoder steps, but it didn't seem to matter.  Cetainly if the PID proportional gain is too high it could make things unstable and cause oscillation.  But I haven't figured out yet if/how my system may be getting into trouble with that.  I did set my sprocket teeth (12 instead of default 10).

---

Posted on *2017-03-14 09:52:53* by *Bar*

I tried to do all the internal calculations in the units of MM to keep things clear, but @davidlang is right that I is an important thing to change. The number of pulses per rotation is defined at the top of axis.cpp in line 29:

#define NUMBER_OF_ENCODER_STEPS 8148.0 

We should make a wiki page to talk about all the things that need to be changed. I bet we can save the next guy who does this a lot of time :-)

---

Posted on *2017-03-14 13:18:08* by *jbarchuk*

> @Bar
> We should make a wiki page to talk about all the things that need to be changed.
Anything you think needs adjustment, open an issue to make it obvious to others. Then that topic gets talked about right there.

---

Posted on *2017-03-14 14:33:57* by *garyw17*

Just had a thought that might address the possibility of my pulse count being so different causing an issue.  What if I left the numberofencoderseteps at 8144, which is the default value.  Then every time the encoder gets read, I multiply the pulse count that is read by the ratio of 8144/600.  So, if the motor turns one rev, the encoder.read would return 600, but multiplied by the scale factor we get 8144, which is what the code expects for one rev.  

I think I just need to search and replace for all instances of   encoder.read

---

Posted on *2017-03-14 15:31:36* by *jbarchuk*

> @garyw17
> I think I just need to search and replace for all instances of encoder.read
Yes but don't go editing all those instances when only a couple of lines of defines is necessary.
Change #define NUMBER_OF_ENCODER_STEPS to NUMBER_OF_ENCODER_STEPS_BY_DESIGN. (With the 8148.0 left in place.)
Add a new #define ENCODER_RATIO_FACTOR 1 or whatever appropriate name.
Then add #define NUMBER_OF_ENCODER_STEPS (NUMBER_OF_ENCODER_STEPS_BY_DESIGN / ENCODER_RATIO_FACTOR)
For your machine change the ~_FACTOR from 1 to 600, and all the other instances are automatically adjusted.
I think I hit all of that right. If not let me know and I'll get someone to edit it.

---

Posted on *2017-03-14 15:34:00* by *jbarchuk*

Kewl, m00t, stomp all my finely crafted underscores. ;)

---

Posted on *2017-03-14 17:18:40* by *garyw17*

OK.  Never mind all that.  I found the problem, and it was not the Kewl software at all.  Or my wiring.  I thought the encoders I bought (see part numbers above) were 600 ppr.  But I just checked, and they are giving me 2400 ppr.  Maybe the 600 ppr was if you only read 1 channel?  I'm not really sure of that, but regardless, I changed the number of encoder step parameter to 2400, and like magic it works!

Amazing how many hours I stood there and stared at it doing the unexpected all because of that one detail.

Anyway, thanks for all of you who read this and pitched in ideas.  Maybe it will save someone else in the future.

---

Posted on *2017-03-14 19:24:42* by *Bar*

If it makes you feel any better, you aren't wrong. Each encoder channel produces 600 pulses per rotation, and each channel is 90 degrees out of phase so the total encoded information is the same as one 2400 pulse encoder with direction information. The software is smart enough extract the extra steps even if you wouldn't see them with an oscilloscope. Congratulations!

---

