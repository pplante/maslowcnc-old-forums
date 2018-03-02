## Kivvy install for Mac OS 10.12.2
Posted on *2017-03-20 06:49:58* by *Jennifer D*

I have to run out the door to an appointment but wanted to post a quick note. 

Back in January I had Ubuntu loaded and running just fine on a partition on my Mac, installed Python, Kivvy, Pyserial, and GroundControl would load, but couldn't get further, obviously, as I didn't have the hardware yet. Now my mac has decided Ubuntu is no longer there to boot to(though the partition is) and all of my attempts to quickly(I know, therein lies my problem) get Ground Control running on my Mac OS side of things have failed. 

Python 2.7.3 is installed. Pip installed, but things are falling apart when it comes to Kivvy. I just realized as I copied the error that the Kivvy command is looking for a Windows file - anyone know what I should be pointing it at? 

Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/19/plqlj__x6j19_zlh9f8lmjv00000gn/T/pip-build-_4S it7/pypiwin32/

---

Posted on *2017-03-20 07:33:46* by *Bar*

Hmmm that is strange. What do you see if you run the pre-compiled version of Ground Control groundcontrol.dmg from https://github.com/MaslowCNC/GroundControl/releases ?

---

Posted on *2017-03-20 09:17:00* by *scottsm*

@Jennifer, I'm on a Mac like you, and I've been able to use the pre-compiled version that Bar linked to. I ran the MakeSymLinks first, then drag - copied the GroundControl app onto the Applications folder link. 
I've also installed in a Linux VM, but a while ago. I remember that I had to install each of the packages one at a time, and that several failed, windows requirements perhaps.

---

Posted on *2017-03-21 12:45:34* by *Jennifer D*

Hi guys - So I've been able to get GroundControl up and running on both Mac and Linux - part of my problem on Linux was forgetting that the steps I thought I'd done were on the Mac side of things. 

Trying to get going(on the Mac side) I have GroundControl installed and running no problem - somehow I didn't see the link to the precompiled version when I tried that yesterday. 

But, I can't seem to mantain a connection, either with the USB extension or without and regardless of which USB port on my laptop I use. On the main GC screen it switches back and forth between "Connected" "Connection Lost" 

Any ideas?

---

Posted on *2017-03-21 12:58:27* by *carlosrivers*

Hey Jennifer just to clarify with you on a similar subject, the newer ground control program only requires a download and install? I saw steps for python and something about Kivvy.

---

Posted on *2017-03-21 13:00:13* by *scottsm*

That sounds like and older version of GroundControl, a behaviour I hoped we had gotten past. The download link for the precompiled package is on [this page](https://github.com/MaslowCNC/GroundControl/releases). Bar updates it as things advance. Is the version you're running from there?

---

Posted on *2017-03-21 13:10:05* by *Bar*

The connecting and disconnecting behavior could be something you would see if the Arduino wasn't running any firmware. If Ground Control doesn't see any data from the machine for two seconds, the connection times out, but if the board is still plugged in it will find it again and reconnect. Do you feel good about the firmware setup part of the process?

---

Posted on *2017-03-21 13:37:27* by *Jennifer D*

Well, I was feeling good about it but let me go through and double check it all!

---

Posted on *2017-03-21 13:44:42* by *Jennifer D*

Ok...the firmware was the problem - seems I forgot to unload it after compiling...oops! 

So now that it's connected is it supposed to say "Unable to resolve Kinematics"?

---

Posted on *2017-03-21 13:51:34* by *scottsm*

There's a newer version (yesterday) of the firmware that eliminates that message. It's spurious as the kinematic routine it refers to isn't 'ready for prime time' yet.

---

Posted on *2017-03-21 13:56:20* by *Jennifer D*

ah, alright...the downside of starting early EST! 
updated the firmware, and looks like we're ready for chain length and so on...hopefully I'll be back saying all's good!

---

Posted on *2017-03-21 14:02:46* by *Jennifer D*

Darn. Nothing doing. Motors aren't turning, chains aren't moving.

---

Posted on *2017-03-21 14:03:32* by *scottsm*

Good news! 
Bar, maybe we should rethink the messages here. 'Connected' really means 'serial port connected', and 'Connection lost' might give a hint about the firmware reply?

---

Posted on *2017-03-21 14:08:38* by *scottsm*

Do the motors give a little whine when you plug in the USB to the computer? If no, check the connections to the Arduino.

---

Posted on *2017-03-21 14:13:02* by *Jennifer D*

Nada. Just unplugged and replugged the motor wiring harnesses at both ends, also checked with and without the USB extension(just to be safe) and nothing doing. I'm not even getting a response in GC when I click the "calibrate chain length". It turns into a color wheel when I click "Actions" but no response in the program when I do any of the calibrating options.

---

Posted on *2017-03-21 14:13:42* by *Jennifer D*

then again...something just started...hang on!

---

Posted on *2017-03-21 14:20:52* by *Jennifer D*

OK - waiting on things to think, but before I forget to ask - which side of the motor controller is left and which is right? I couldn't find anything in the documentation about it - should the power and usb ports face right and the motor wiring go left and right from the Ports 1 and 3(i.e. not crossing each other to reach the motors?) 

Also is there an expected delay before commands execute? It's been a good 45 seconds since I clicked the chain calibration and nothing has happened as yet.

---

Posted on *2017-03-21 14:28:00* by *scottsm*

The 'test motors' begins right away. Too, both motors give a little whine when the Arduino resets, as when the USB cable is connected. You could check connections against this [picture](https://github.com/MaslowCNC/Electronics/raw/master/Documentation/Attach%20Power%20Supply.jpg), and check the power supply is live by the led on it.

---

Posted on *2017-03-21 14:30:42* by *Jennifer D*

Now I'm seriously confused.

Connections verified, power supply led is lit. I unplugged and replugged the usb and upon reset the right motor started turning clockwise and is still going. Had the chain on it to calibrate length and it dropped off because it's turning the opposite way. 

(also...motor still going...)

---

Posted on *2017-03-21 14:32:43* by *Bar*

What happens if you run the "Test Motors" option under the "Actions" button?

---

Posted on *2017-03-21 14:38:58* by *Jennifer D*

Ok - this is very very strange. 

So I swapped the motor wiring harnesses - the left motor is now plugged into the port between the heat sinks and the right is on the outside - figured this out because GC told me it was moving the left motor but the right was the one going. 

When I click test motors nothing happens. 

Going to try measuring the chains again...

---

Posted on *2017-03-21 14:40:52* by *Bar*

I think you are right that swapping the motors will fix the issue with the left motor spinning instead of the right one and and will make the chain go the correct direction.

It seems like you might be seeing some kind of serial connection issue where your commands aren't getting sent to the machine.

---

Posted on *2017-03-21 14:42:52* by *Jennifer D*

I'll agree with that - I clicked calibrate and nothing happened, but when I unplugged the usb and replugged it in, the calibration started upon GC connecting to the chip. 

Not sure how to fix that issue though..

However, I am letting it go through chainlength calibration.

---

Posted on *2017-03-21 14:45:10* by *Bar*

That's a good plan.

When the calibration finishes, try clicking the arrow keys to move the machine around. Do you see commands being sent and the machine responding like this:  [Command responses](//muut.com/u/maslowcnc/s1/:maslowcnc:AQhW:commandresponses.jpg.jpg)

---

Posted on *2017-03-21 14:51:12* by *Jennifer D*

Ok - calibration done. It does move and will return to "home" also. Think it's safe to try go forward with letting it cut parts?

---

Posted on *2017-03-21 14:56:38* by *Bar*

Fantastic! 

You should be good to go!

 I recommend building a "starter sled" as described in this forum post: http://www.maslowcnc.com/forums/#!/general:starter-sled 

You are pretty much as far as I am at this point. I'm working on writing up the directions to build a starter sled right now :-)

---

Posted on *2017-03-21 14:57:41* by *Bar*

Let us know if you have repeatable issues with the serial connection, if that's an ongoing thing we want to figure out how to solve it permanently.

---

Posted on *2017-03-21 15:02:27* by *Jennifer D*

Will do! 

I also plan to write up the challenges I've come across being somewhat a newbie with all of this. I'm far from technically challenged - I've done everything from swap out a transmission and do a top end rebuild on a V8, built a boat, furniture, and so on, but I've definitely had moments when I felt incredibly out of my league over the last two days!

---

Posted on *2017-03-21 15:17:55* by *Bar*

We want to do everything we can to make Maslow accessible to everyone.  Your feedback about what we can make more clear is the key! You only get one first time, it will all look easy the second time so any advice you have right we would love to hear!

---

Posted on *2017-03-21 16:26:03* by *Jennifer D*

I had to call it a day as it looks like rain is rolling in, requiring me to move all various equipment back into the shop, not to mention it's past dinner time!

I was able to get a temporary sled rigged up(used a handy scrap) and calibrated the system. Also got the file downloaded and loaded into GC hopefully tomorrow I'll start cutting!

Bar, I did have a repeatable serial connection issue where GC stopped communicating at all and I had to unplug the USB and replug before it would do anything. If I can tomorrow I'll try to do things a bit more systematically so I can tell you when things stop working. 

 [IMG_0421](//muut.com/u/maslowcnc/s3/:maslowcnc:m6HG:img_0421.jpg.jpg) [IMG_0422](//muut.com/u/maslowcnc/s3/:maslowcnc:J11F:img_0422.jpg.jpg)

---

Posted on *2017-03-21 16:32:44* by *Bar*

That looks beautiful! 

Sounds good, let me know when it's acting up and we'll work it out.
 The more systamatically we can make it happen, the easier it's going to be to track down what's going wrong.

Technically the 'L' brackets should mount the other way :-) but I don't think it matters :-). All of the different holes are to allow you to anchor your chains at different heights to balance the different center of gravity of different routers

---

Posted on *2017-03-21 16:46:21* by *jbarchuk*

> @Jennifer D
> Bar, I did have a repeatable serial connection issue where GC stopped communicating at all and I had to unplug the USB and replug before it would do anything.
The first two typical troubleshooting techniques are to try different USB ports, and change cables. Next is to disable and remove USB drivers and reinstall them. (Windows will do that automatically, other OSes vary.) In any case always very annoying never knowing when it's going to crash.

---

