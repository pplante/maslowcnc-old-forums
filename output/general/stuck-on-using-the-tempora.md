## Stuck on "Using the Temporary Frame to Cut Parts" step
Posted on **2017-04-25 08:49:48** by **MikeT**:

I watched the "Setup machine dimensions" video, took and entered the measurements in the GC/Settings dialog, and double-checked them. The GC/Actions/Calibrate Chain Length - Automatic step seemed to go OK, ending with the two chain ends dangling a couple inches above the floor. But when I clicked on GC/Actions/Calibrate Motors, the calibration process pulled the temporary sled above the top of the sheet of plywood, almost up to a direct line between the motors. At that point there was so much strain on the chain and motors that I thought something was about to break - clearly this is not how the Calibrate Motors step is supposed to work!



First, any ideas what might be going wrong in the Calibrate Motors step? Second, how do I quickly turn off the motors when some dangerous condition arises and I want to stop them quickly?



Thanks!

---

Posted on **2017-04-25 08:56:54** by **rancher**:

I don't know the answer to your first question, but I have an idea for the second that just came to me and I think I'll test since I have the part.



Everyone, is there any problem with killing the 12v to the motors as an emergency stop?  Amazon has super cheap 12v wireless relays, and I have a couple on hand.  I've almost torn my sled apart on numerous occasions, it would be awesome to have an emergency stop remote.



Will that break anything?

---

Posted on **2017-04-25 09:07:53** by **Bar**:

Cutting the 12v supply to the motors is a great option. It shouldn't effect anything other than the motors, because the 12 volt supply is isolated from the rest of the circut.



Another option is to unplug the USB cord, that will also stop the machine immediately, however it won't remember it's position when you turn it back on, so you will need to do the calibrate chain lengths step again.



As far as the original question, I'm a little stumped. That's not the behavior I would expect from calibrate motors at all. This was the first time you had run the calibrate motors function? Was it one or both motors that turned? Was any text printed in the text window in the bottom right of Ground Control? It might be worth trying to repeat the process without the sled attached, so that we can better figure out what is happening.

---

Posted on **2017-04-25 09:10:14** by **TheRiflesSpiral**:

Is the gearing high enough on the motors that cutting power won't let them spin freely? (Meaning will cutting power cause the router to drop if the bit is retracted?)

---

Posted on **2017-04-25 09:10:51** by **Bar**:

Yes, there is a worm gear in the gear box which can't be back driven so as soon as power is cut the motors are locked

---

Posted on **2017-04-25 09:12:23** by **TheRiflesSpiral**:

Very nice. That explains why there isn't a "park" necessary before shutting the machine off.

---

Posted on **2017-04-25 09:13:40** by **MikeT**:

Bar, when you say "repeat the process without the sled attached", do you mean I should (1) re-run Calibrate Chain Length - Automatic, (2) use a cotter pin to clip the two chain ends together, and then (3) re-run Calibrate Motors? If so, is it OK that the temporary sled measurements that I took are still in the Settings dialog, or should I reset all those values to some defaults?

---

Posted on **2017-04-25 09:18:33** by **Bar**:

Good question.



I would unclip the ends of the chain from the sled and just leave them hanging or even take them off the motors entirely. That way if you see the same behavior where the sled tries to go off the top you can continue to observe what will happen, do the motors stop eventually? I would leave all the settings as is for now, but we might want to set them back to the defaults if we can't find another cause of the problem.

---

Posted on **2017-04-25 09:19:48** by **Bar**:

The calibrate motors function should just rotate each motor back and forth a few times and print some text about what it is doing to Ground Control, so the fact that it's trying to go off the top seems like strange behavior. I'm excited to get to the bottom of it.

---

Posted on **2017-04-25 09:20:42** by **MikeT**:

OK, I'll take a run at it right now and report my results ASAP. Thanks for your help!

---

Posted on **2017-04-25 09:22:52** by **Bar**:

Thank you for tracking down an interesting bug!

---

Posted on **2017-04-25 09:49:07** by **MikeT**:

I just re-ran the Calibrate Chain Length – Automatic process and immediately ran into something fishy. Both motors axes are turning counter-clockwise as they feed out the chain. This means that the left motor (to my left as I face the front of the sheet of plywood) immediately dumps the end of the chain onto the ground, while the right motor completes the Calibrate Chain process normally. Somehow the left motor seems to have gotten confused about which direction it should be turning.

---

Posted on **2017-04-25 09:59:11** by **Bar**:

Woah

---

Posted on **2017-04-25 09:59:18** by **Bar**:

That's a new one

---

Posted on **2017-04-25 10:00:17** by **Bar**:

Let's see if maybe there is a wire crossed in one of the cables. Will you swap the motor cables, but keep everything else the same and see if the problem moves with the cable?

---

Posted on **2017-04-25 10:01:18** by **MikeT**:

Will do.

---

Posted on **2017-04-25 10:19:00** by **MikeT**:

I removed both chains from the motor sprockets, swapped the cables that run between the Arduino shield and the two motors, then re-ran Calibrate Chain - Automatic. Same results as earlier this morning - both motors turn counter-clockwise.

---

Posted on **2017-04-25 10:22:26** by **MikeT**:

I think I've got the cables plugged in correctly. I see that the rows of six pins on both the Arduino shield and the motors are offset slightly to one side of the connectors, and I think I'm matching that alignment with the direction I'm plugging in the female ends of the cables.

---

Posted on **2017-04-25 10:23:22** by **gero**:

For the second part, I have the motor power supply on a separate extension cable with a switch. That is next to the laptop.

---

Posted on **2017-04-25 10:23:44** by **Bar**:

I think that's a good thing, at least it seems like it's probably not a bad cable

---

Posted on **2017-04-25 10:24:51** by **Bar**:

What happens when you click the "test motors" button?

---

Posted on **2017-04-25 10:28:51** by **MikeT**:

Test Motors/Encoders results in the motors first spinning in the direction that would shorten the chain, and then in the direction that would lengthen the chain. The left motor spins counter-clockwise, then clockwise, while the right motor spins clockwise, then counter-clockwise.

---

Posted on **2017-04-25 10:30:56** by **Bar**:

That sounds right!

---

Posted on **2017-04-25 10:31:34** by **Bar**:

Is any text printed on the console in Ground Control when that happens?

---

Posted on **2017-04-25 10:34:54** by **MikeT**:

Testing left-axis motor: Direction 1, Fail; Direction 2; Pass

Testing right-axis motor: Direction 1, Pass; Direction 2; Pass

So direction #1 on the left-axis motor does not appear to be happy!

---

Posted on **2017-04-25 10:37:33** by **Bar**:

That is very strange

---

Posted on **2017-04-25 10:37:49** by **Bar**:

Ohhhh I have a theory

---

Posted on **2017-04-25 10:38:13** by **Bar**:

It could be a bad diode on the motor controller board

---

Posted on **2017-04-25 10:38:16** by **MikeT**:

Shall I swap the motors and then try it again?

---

Posted on **2017-04-25 10:38:29** by **Bar**:

Yes, that's a great idea

---

Posted on **2017-04-25 10:40:10** by **davidlang**:

there should be a way to switch which outputs on the board are used for which motors. Since there are 4 outputs and the maslow only 'needs' three, that would give an ability to easily test for problems like you suspect, or to work around damaging an output.

---

Posted on **2017-04-25 10:42:20** by **Bar**:

Yes! I completely agree.

---

Posted on **2017-04-25 10:42:42** by **Bar**:

Did swapping the motor give you the same result?

---

Posted on **2017-04-25 10:57:32** by **MikeT**:

I swapped the motors, shut down and re-started GC, did a Connect, and did a Test Motors/Encoders. Exactly the same results as earlier - the only reported failure was, "Testing left-axis motor: Direction 1, Fail...". So moving the motors did not move the problem.

---

Posted on **2017-04-25 11:00:14** by **Bar**:

:/ I think the fastest solution is going to be for us to send you a new controller board. We'll send it today with express shipping. Will you email your address to hannah@maslowcnc.com

---

Posted on **2017-04-25 11:01:05** by **Bar**:

I'm sorry for the trouble

---

Posted on **2017-04-25 11:01:08** by **MikeT**:

How fast will it get here? I'd like to get it as soon as possible, but on the other hand I'll be at your booth in Portland on Friday.

---

Posted on **2017-04-25 11:01:28** by **Bar**:

Oh, well then it might be easier to just pick it up here :-)

---

Posted on **2017-04-25 11:01:53** by **Bar**:

We'd send it with the fastest shipping the post office can give us, but it would probably still be thursday

---

Posted on **2017-04-25 11:02:13** by **Bar**:

There is one more thing we can try

---

Posted on **2017-04-25 11:03:39** by **Bar**:

The problem is probably that one of the diodes was installed backwards, the diodes are just there to protect the motor controller chip. If we remove them, the board may work normally but wear out sooner than it would otherwise, but it will probably make it to friday

---

Posted on **2017-04-25 11:06:05** by **MikeT**:

If the only damage would be to the Arduino shield, and it's going to be replaced in a couple days anyway, then it sounds like it's worth a try. So should I cut a pin(s) on one of the diodes?

---

Posted on **2017-04-25 11:10:28** by **Bar**:

Great! This is a big experiment.



Next to each connector there are 4 diodes (the little black squares)



[Diodes](//muut.com/u/maslowcnc/s1/:maslowcnc:Xww5:diodes.jpg.jpg) 



You should be able to just pull off the ones next to the connector which isn't working with needle nose pliers (or unsolder them if you want to do it right)

---

Posted on **2017-04-25 11:10:39** by **Bar**:

Before we do that, will you take a look at something for me?

---

Posted on **2017-04-25 11:11:29** by **Bar**:

Each diode has a white line one the top of it, and each place they go on the PCB has a white line on it also, will you check to see if they all line up?

---

Posted on **2017-04-25 11:14:04** by **MikeT**:

Give me a couple minutes and I'll take a look. Better yet, what if I take a picture and send it to you?

---

Posted on **2017-04-25 11:14:13** by **Bar**:

That sounds perfect

---

Posted on **2017-04-25 11:14:38** by **Bar**:

I really only need to see the 4 next to the connector which isn't working right

---

Posted on **2017-04-25 11:29:25** by **MikeT**:

Here the picture. I pulled off the adjacent heat sink to improve the view.  [IMG_20170425_112322382_HDR](//muut.com/u/maslowcnc/s3/:maslowcnc:UKNa:img_20170425_112322382_hdr.jpg.jpg)

---

Posted on **2017-04-25 11:34:19** by **Bar**:

Even when I download the picture and zoom way in I'm having a hard time seeing the white lines on the tops of the diodes

---

Posted on **2017-04-25 11:34:31** by **Bar**:

They're pretty hard to see even in real life

---

Posted on **2017-04-25 11:34:46** by **Bar**:

Let me see if I can get a picture that shows what I'm looking for

---

Posted on **2017-04-25 11:37:12** by **Bar**:

I got one, but it's tough. The [white lines](//muut.com/u/maslowcnc/s1/:maslowcnc:kapm:whitelines.jpg.jpg)  really don't want to show up

---

Posted on **2017-04-25 11:39:22** by **MikeT**:

They're faint, but I see them.

---

Posted on **2017-04-25 11:40:05** by **MikeT**:

So the point is that the white bars across the diodes match up with the white bars that have been painted on the board?

---

Posted on **2017-04-25 11:41:48** by **Bar**:

yes, exactly

---

Posted on **2017-04-25 11:41:57** by **Bar**:

Is there by any chance one that doesn't line up?

---

Posted on **2017-04-25 11:44:02** by **MikeT**:

I just looked with a magnifying glass, and as best I can tell the white lines on the diodes do correctly line up with the white lines printed on the board.

---

Posted on **2017-04-25 11:44:11** by **Bar**:

Darn

---

Posted on **2017-04-25 11:44:17** by **Bar**:

:-)

---

Posted on **2017-04-25 11:44:27** by **Bar**:

Well thanks for checking!

---

Posted on **2017-04-25 11:44:50** by **MikeT**:

You betcha!

---

Posted on **2017-04-25 11:45:27** by **Bar**:

It might be that the chip itself that you have is bad, but that seems unlikely

---

Posted on **2017-04-25 11:45:44** by **Bar**:

I'd say pull all the diodes off and see if that fixes the problem

---

Posted on **2017-04-25 11:46:22** by **Bar**:

If not, we can express ship you a new board or you can pick one up on Friday (really any time you'd like would actually be OK)

---

Posted on **2017-04-25 11:46:41** by **Bar**:

I'm sorry again for the inconvenience :-(

---

Posted on **2017-04-25 11:47:28** by **MikeT**:

So just yank all four of those diodes off with a needle-nose pliers? Makes me a bit nervous - I've never performed surgery on a circuit board before!

---

Posted on **2017-04-25 11:47:53** by **MikeT**:

What if ones and zeros start pouring out all over the floor?

---

Posted on **2017-04-25 11:48:38** by **Bar**:

Haha what ever you do don't touch them if they do! Especially the ones, they're really sharp!

---

Posted on **2017-04-25 11:48:53** by **Bar**:

But yep, just pull em off

---

Posted on **2017-04-25 11:49:18** by **Bar**:

I don't think we've got much to loose :-) Worst case scenario, it won't work right?

---

Posted on **2017-04-25 11:49:33** by **Bar**:

I recommend a little bit of a twist

---

Posted on **2017-04-25 11:50:30** by **MikeT**:

OK, I'll give it a shot, since the patient's already pretty much toast.

---

Posted on **2017-04-25 11:51:22** by **Bar**:

I'll keep my fingers crossed

---

Posted on **2017-04-25 11:55:33** by **MikeT**:

What if I plug the motor cable into the 4th (right-most) of the white, 6-pin connectors, the one that's to the right of the two diodes that you soldered together a piece of wire?

---

Posted on **2017-04-25 11:56:56** by **Bar**:

That's a great idea

---

Posted on **2017-04-25 11:57:57** by **Bar**:

I'd rather use the z-axis port for the second motor because of the way the chip works. I picked the best pins for the three main motors, but if pulling the diodes off doesn't change anything, lets give that a go!

---

Posted on **2017-04-25 12:00:37** by **MikeT**:

Hmmm, I didn't quite get that. So I should try: (1) the 4th (right-most) connector, and if that doesn't work, (2) the 2nd connector, and if that doesn't work, (3) pull the diodes just to the right of the 3rd connector, and then try the 3rd connector again? Is that the best trial-and-error sequence?

---

Posted on **2017-04-25 12:05:03** by **Bar**:

Sorry, I would say 1) Pull the diodes, they only effect that one port so best case scenario pulling them fixes the port, worst case it's still not working 2) Switch to the middle port 3) Go to the end port (although I think that 4th port is a bit of a long shot)

---

Posted on **2017-04-25 12:06:31** by **Bar**:

I know it seems destructive to take something apart

---

Posted on **2017-04-25 12:07:50** by **MikeT**:

I'm always chicken about tearing into stuff, but you da' man! Give me a little while and I'll let you know how it went.

---

Posted on **2017-04-25 12:10:36** by **Bar**:

:-) If it all falls to pieces, we've got a brand new one with your name on it!

---

Posted on **2017-04-25 12:52:37** by **Bar**:

How did it go?

---

Posted on **2017-04-25 13:11:54** by **MikeT**:

"Falls to pieces"  is where it's at now. I pulled the diodes and tried the 3rd (from the left) connector, then tried the 2nd connector, and finally tried the 4th (right-most) connector. In all cases, Test Motors/Encoders reports:



Testing left-axis motor: Direction 1, Fail; Direction 2 Fail

Testing right-axis motor: Direction 1 Pass; Direction 2, Pass



Then I tried Calibrate Chain Length - Automatic. With all three connectors, the left motor would never move at all, then when I hit the STOP button the right motor would rotate counter-clockwise slowly, feeding out the chain. I'd say communications with the left motor is gone.

---

Posted on **2017-04-25 13:13:07** by **Bar**:

:-(

---

Posted on **2017-04-25 13:14:22** by **Bar**:

When the left motor is plugged into the middle port where the z-axis would normally be, what do you see for the z-axis motor test results?



Testing left-axis motor: Direction 1, Fail; Direction 2 Fail

Testing right-axis motor: Direction 1 Pass; Direction 2, Pass

Testing z-axis motor: Direction 1 ?&quest;

---

Posted on **2017-04-25 13:16:45** by **MikeT**:

I get "Testing Z-Axis motor: Direction 1, Pass; Direction 2, Pass.

---

Posted on **2017-04-25 13:16:56** by **Bar**:

Woo!

---

Posted on **2017-04-25 13:17:40** by **Bar**:

Ok, I'm going to whip up a firmware that just moves the second motor from the bad port to that port. It's not the idea solution, but it should get things going until we can get you a new board Friday

---

Posted on **2017-04-25 13:20:18** by **MikeT**:

That would be nice, if you can spare the time. I'd like to show up on Friday with as many intelligent questions (and as few dumb ones) as possible, to maximize the benefit of the drive down. But if you're swamped and it's going to take up a bunch of your time, I can just wait two more days until you can hand me a new board.

---

Posted on **2017-04-25 13:23:13** by **Bar**:

That makes a lot of sense

---

Posted on **2017-04-25 13:23:49** by **Bar**:

Getting you up and running is a top priority, give me an hour and I'll have something to show :-)

---

Posted on **2017-04-25 13:25:12** by **MikeT**:

It would be appreciated if you can afford to spend another hour on me, given that I've already taken up much of your Tuesday morning.

---

Posted on **2017-04-25 13:26:18** by **Bar**:

Haha, not at all! Getting you guys up and running is my number one goal, and learning about what is going wrong is the key to fixing the problem for the future.

---

Posted on **2017-04-25 13:27:39** by **Bar**:

So far today I've learned that we should never do business with this PCBA company again (the failure rate is way to high for such a simple PCB) and there should absolutely be a setting that lets you move the motors around so that you can just move it to a different port (excellent suggestion).

---

Posted on **2017-04-25 13:33:09** by **MikeT**:

You know how to find the bright side in things, which is a wonderful skill to possess. I'm going to run some errands and will check back in a couple hours. Thanks again!

---

Posted on **2017-04-25 13:38:53** by **Bar**:

Sounds good, hopefully I'll have something ready by the time you get back

---

Posted on **2017-04-25 13:49:55** by **Bar**:

Alright, so it turned out to not take very much time at all :-)



When you get back, give the version of the firmware [here](https://github.com/MaslowCNC/Firmware/tree/move-left-motor-to-z-axis) a try. 



To download it use the green "Clone or Download" button in the upper right corner as shown in  [this picture](//muut.com/u/maslowcnc/s3/:maslowcnc:3fvL:howtodownload.jpg.jpg) 



Let me know how it goes!

---

Posted on **2017-04-26 08:38:00** by **MikeT**:

Actions/Test Motors&Encoders makes both motors move a little in both directions. It reports Pass for both directions for both motors, and reports Fail for both directions for Z-Axis. So far so good! But when I do Actions/Calibrate Chain Length - Automatic, the left motor doesn't move a bit. If I then click STOP, the right motor starts measuring out the chain. Do you suppose there some bit of code in there that's insisting on using the third connector to perform the calibration? Maybe a hard-coded value in there somewhere?

---

Posted on **2017-04-26 09:16:14** by **Bar**:

Sounds like progress. That's a good guess about some hard coded value. Let me see what I can figure out right now. I've got my machine set up in the same configuration so I can test.

---

Posted on **2017-04-26 09:24:29** by **Bar**:

I'm seeing both motors calibrate correctly, but I think I might have an idea of what is going on. There might be some weird junk stored in the Arduino's memory because of all the changes we've made. 



Give clicking *Actions -> Advanced (in the bottom right) -> Wipe EEPROM* then *Actions -> Calibrate Motors* then *Actions -> Calibrate Chain Lengths* again

---

Posted on **2017-04-26 09:24:57** by **Bar**:

What do you see then?

---

Posted on **2017-04-26 09:44:17** by **MikeT**:

Calibrate Motors drove both motors. I ran it with about a foot of slack chain hanging on the motor sprockets. Should I re-run it with no chain on the sprockets?

---

Posted on **2017-04-26 09:47:32** by **MikeT**:

Calibrate Chain Length - Automatic is now driving the left motor. The Wipe EPROM must have fixed the problem!

---

Posted on **2017-04-26 09:50:59** by **Bar**:

Perfect!

---

Posted on **2017-04-26 09:51:57** by **Bar**:

I would re-run "Calibrate Motors" once the whole sled is attached, it compensates for the weight of your router

---

Posted on **2017-04-26 10:10:01** by **MikeT**:

Calibrate Motors is now running fine! Yeehaw!

---

Posted on **2017-04-26 10:10:17** by **Bar**:

Yeehaw!!! :-)

---

