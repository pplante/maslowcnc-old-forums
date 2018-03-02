## Calibrating
Posted on *2017-07-15 06:29:17* by *scottbramall*

Having a couple of issues calibrating the machine, the right motor doesnt seem to move. Anyone else had this issue?

---

Posted on *2017-07-15 07:55:14* by *gero*

Hi, does is move with the >test motors/encoders< from the actions menu?

---

Posted on *2017-07-15 08:33:09* by *Bar*

There is absolutely something going on with the right motor, but I'm having trouble tracking it down because every time I try to make it happen may machine starts acting normal. It is on the top of my to-do list.

Were you a beta tester or a regular backer?

---

Posted on *2017-07-15 09:21:41* by *Bar*

In either case, @gero is spot on that the first thing to do is test the Actions -> Test Motors/Encoders

---

Posted on *2017-07-16 00:26:56* by *scottbramall*

Under the test motors both motors work fine. When calibrating everything's ok up until setting the chain length when the left motor releases enough chain to get to the home position but the right motor doesn't spin. Just makes a faint sound.

---

Posted on *2017-07-16 00:27:46* by *scottbramall*

Sorry. I'm a regular backer

---

Posted on *2017-07-16 01:12:37* by *gero*

So that looks like you confirmed a bug in FW0.80 that blsteinhauer88 reported 8 days ago. He could do the calibration with FW0.78. You can get it from the releases https://github.com/MaslowCNC/Firmware/releases

---

Posted on *2017-07-16 01:19:26* by *gero*

He also has problems with moving the sled. Better stick with FW0.78 for the moment. The thread http://www.maslowcnc.com/forums/#!/general:right-motor-issue
UPS! You have the new motor shied, right? The new shield was introduced in 0.79 where the right motor bug started. So I guess the new shield will not work with 0.78 :-(

---

Posted on *2017-07-16 01:22:02* by *scottbramall*

Yes. I have the new shield. If bar wants to Skype or anything or send and beta codes I'm happy to help

---

Posted on *2017-07-16 01:50:34* by *gero*

It's 1:48 in Portland, so I guess they are fast asleep. In 5 or 6 hours there should be some support.

---

Posted on *2017-07-16 05:36:27* by *scottbramall*

Just tried firmware .78 and when calibrating it turns the motors the wrong way and by too much.

---

Posted on *2017-07-16 12:01:07* by *gero*

Pretty sure the new shield will not work with FW prior to 0.79. I guess that is why Bar put the detection of the shield version in.

---

Posted on *2017-07-16 13:29:47* by *Bar*

@Gero is right that anything prior to 0.79 won't work with the newer shields.

It's good to hear that Actions -> Test Motors works, because that means all of the electronics are good. It seems like we've got an issue with the right motor behaving very strangely. I'm in the process of tracking it down, but it's a tough one to crack because it seems to only affect some people some times which is weird to say the least.

---

Posted on *2017-07-16 13:34:18* by *scottbramall*

At the moment I'm trying to calibrate the machine and get as far as the point where it releases the chain to get to the centre position, the left motors fine but the right motor doest move at all, however, it does make a slight high pitched sound. I also tried v0.79 and got to the same point each time.

---

Posted on *2017-07-16 13:36:24* by *Bar*

Hmm, OK. let me think about what we should try next for a second

---

Posted on *2017-07-16 13:37:16* by *Bar*

What happens when you click the arrow buttons to make the machine move around?

---

Posted on *2017-07-16 13:46:19* by *scottbramall*

Give me 2min, just on way to work to check

---

Posted on *2017-07-16 13:53:12* by *scottbramall*

Left motor moves but right doesn't

---

Posted on *2017-07-16 13:53:57* by *scottbramall*

The left only moves in a CW motion tho regardless of what arrow you press on ground control

---

Posted on *2017-07-16 13:54:39* by *Bar*

When you have a chance, give this firmware here: https://github.com/MaslowCNC/Firmware/tree/explore-optimization-issues a try. You can download it by using the green "clone or download" button on the right hand side

---

Posted on *2017-07-16 14:00:01* by *scottbramall*

Same as before, nothing on right motor, only moves left motor CW

---

Posted on *2017-07-16 14:02:29* by *Bar*

:-(

---

Posted on *2017-07-16 14:05:03* by *scottbramall*

I seem to think over the weekend, I half calibrated it and at the point it should have released enough chain on the right motor to centre the sledge i skipped the calibration so it thought it was calibrated. After that I seem to think the left motor did turn in both directions, I'm just trying it now to see

---

Posted on *2017-07-16 14:05:04* by *Bar*

Oh, I have a new idea! Try clicking Actions -> Advanced -> Calibrate Chain Lengths Manual

---

Posted on *2017-07-16 14:05:29* by *Bar*

Maybe try closing ground control and re-opening it after that also just to make sure we're starting fresh

---

Posted on *2017-07-16 14:06:19* by *scottbramall*

Yes,The left motor is now moving in both directions, the right motor is making a hum but not moving.

---

Posted on *2017-07-16 14:09:22* by *scottbramall*

OK, so after clicking the calibrate manual and then restarting ground control both motors seem to be spinning (although when it comes to the end of the movement both are making some noise and not moving)

---

Posted on *2017-07-16 14:10:48* by *Bar*

Perfect! That sounds like exactly what you want to see :-)

---

Posted on *2017-07-16 14:11:40* by *Bar*

Sorry that took me so long to diagnose, I just assumed that because we were talking about the right motor you were seeing the same issue some of the Beta testers are seeing with the right motor and the newest firmware

---

Posted on *2017-07-16 14:13:01* by *Bar*

What happened was that the machine was trying to compute it's position for an impossible geometry (negative chain lengths or something like that). Was there a warning message that popped up when the machine would first connect saying something like that?

---

Posted on *2017-07-16 14:13:05* by *scottbramall*

So when I click manual calibration should it give me an option to input anything?

---

Posted on *2017-07-16 14:13:39* by *scottbramall*

I think it just said it needed calibrating.

---

Posted on *2017-07-16 14:26:50* by *Bar*

Perfect! When you see that error message it really just means you need to run the chain calibration by clicking Actions -> Calibrate Chain Lengths Automatic. The manual one isn't really recommended

---

Posted on *2017-07-16 14:28:58* by *scottbramall*

But it won't move the right motor when calibrating chain lengths?

---

Posted on *2017-07-16 14:30:51* by *Bar*

Oh darn, so maybe we're looking at two issues. I'm sorry I misunderstood

---

Posted on *2017-07-16 14:31:38* by *Bar*

So now the situation is that both motors will move when using the arrow buttons, but during the automatic chain length calibration process the left motor measures out the chain, but then the right one doesn't start to move after the left one finishes?

---

Posted on *2017-07-16 14:32:47* by *scottbramall*

Well I've been getting to that point of calibrating the chain lengths from the  setup machine dimensions - so maybe if i can setup the machine dimensions, skip the chain and then open it separately it may work?

---

Posted on *2017-07-16 14:34:50* by *Bar*

That's a great idea. You can manually enter the machine dimensions in the settings (even just rough guesses for now so we can figure out what's going on), then do Actions -> Calibrate Chain Lengths Automatic to test if the problem is going through the calibration process

---

Posted on *2017-07-16 14:37:54* by *Bar*

Here are my  [Settings](//muut.com/u/maslowcnc/s3/:maslowcnc:vTlM:settings.jpg.jpg) if you want to get some reasonable values without measuring anything

---

Posted on *2017-07-16 14:46:41* by *scottbramall*

It turned slightly and is now making a high pitched hum.

---

Posted on *2017-07-16 14:49:47* by *scottbramall*

Then after a while..."unable to find valid machine position. Please calibrate chain length.

---

Posted on *2017-07-16 14:50:33* by *scottbramall*

Now if i press one of the arrows on ground control it only moves the left motor.

---

Posted on *2017-07-16 14:50:40* by *Bar*

Hmmmm...darn

---

Posted on *2017-07-16 14:52:21* by *Bar*

I just tried again to get the same issue on my end and I can't so I'm going to have to rely on you guys to test things. The issue seems to be pretty wide spread, so I'm going to make a GitHub issue to focus the discussion in one place.

---

Posted on *2017-07-16 14:55:40* by *Bar*

I've made an issue here: https://github.com/MaslowCNC/Firmware/issues/262

---

Posted on *2017-07-16 16:18:09* by *davidlang*

@bar, the text of that message (calibrate chain lengths) is very misleading. Can you change it to something like "unable to calculate position, possible machine dimension problem" or something that doesn't point at a specific step as the solution. It may be useful to have the firmware output the machine dimensions as it thinks they are (along with the position it was trying to calculate)

In playing with the simulation, I found I could get that error to happen regularly, not because of chain length problems, but because the forward loop to find it's position would get into a bad state.

I was most able to replicate this when I tried setting the S and H3 values small as it would miscaclulate the chain lengths and at the center think one chain needed to be longer than the other, then as it was hunting for optimum, as it passed center, the chain lengths would flip and it would start hunting again and be in an endless loop.

---

Posted on *2017-07-16 17:04:35* by *Bar*

I agree that it is unclear, and we should re-write it, but I like that it gives the user specific feedback about what to do about the problem. 9/10 times someone sees that issue all they need to do is Actions -> Calibrate Chain Lengths, but I agree we should make it clear that isn't the only solution. 

Can anyone think of better text that makes it more clear why the error is popping up, and better recommends what to do about it?

---

