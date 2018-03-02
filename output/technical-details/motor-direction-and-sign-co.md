## Motor Direction and sign convention
Posted on **2017-01-28 20:11:23** by **garyw17**:

Hello all,
Since I didn't make the cutoff for kickstarter kits, I decided to give it a go and see if I could make something work.  After lots of internet searching, I found a motor that looks like it might work.  The Pololu 25D with a 227:1 gearbox puts out 1.7 ft-lbs of torque, has a max speed of 33 rpm, and has a built in encoder with over 10,000 counts per rev.  I bought a couple of them along with an L298 dual H bridge motor controller and an Arduino mega.  I downloaded the latest version of firmware and ground control software, and had no problem getting python, etc, installed and running on my Windows 7 PC.

I connected the motors and encoders up according to the pinout listed in CNC_Function.h    I then wrote a simple sketch to drive either the left or right motor based on a pwm value, and used the encoder library included with the firmware download to look at the encoder output in the serial monitor.  That way I can tell when the pwm value drives the motor CW or CCW, and I can see whether it is accumulating a positive or negative rotation angle from the encoders. 

Could someone please let me know what the required directions and signs are?  I.e., if I apply a pwm signal to the left motor, which way should it turn (facing the shaft), and should that be a positive or negative encoder angle: and same for the right motor.

I have been experimenting today, and part of my trouble is I don't quite know what to expect.  I guessed at some sign conventions.  I find that when I upload the firmware to the Arduino, both motors oscillate a few times back and forth, then stop.  The same happens when I then launch ground control.  Typically at that point the white cross hairs are not on top of the red ones.  I think they are supposed to be?  But I figured that may just be because the PID gains are not set correctly for me, although I'm not clear yet on whether those gains update automatically some how, or I need to manually tune them somehow.  In any case, at that point if I use the manual move command, I see the red circle move, and then the white cross hairs moves off sort of randomly, rather than following it.  The position in ground control updates until the white cross hairs get way off the screen, at which point the position stops updating and the motors just spin continuously.

I think the most likely problem is my sign convention, but if anyone has another idea please let me know.

Thanks!

---

Posted on **2017-01-29 01:17:13** by **davidlang**:

simple engineering would suggest that the chains pass over the top of the sprockets, so that would mean that the direction t shorten the chain would be different for the two motors, with the left one turning counter-clockwise and the right one turning clockwise

---

Posted on **2017-01-29 07:23:49** by **garyw17**:

Vertical motion is a good test case.  Since there is no positive/negative on the output of the motor controller card, I can change direction by just switching the wires, but that does not help with the controller.  The right side motor direction is controlled by the Arduino pins 9 and 8, and the left by 13 and 12.  To get vertical motion of the router (CCW on left motor and CW on right motor), which pins go high and which go low?  Then, while the motors are running in this mode (upward router travel), should the encoder angle for each motor be going positive or negative?  I'

---

Posted on **2017-01-29 08:11:49** by **garyw17**:

Update.   OK.  Got it working now after a bit more trial and error.   Just have to be very careful which pins are encoder A/B, the H bridge init 1 and 2, and which way the motor is connected.  Very cool to see the PID controller track the commanded motion!

---

Posted on **2017-01-30 09:42:41** by **Bar**:

Awesome work! It sounds like you've pretty much got if figured out. One more thing you might be interested in is that  the file Axis.h line 26 "#define NUMBER_OF_ENCODER_STEPS" sets the number of steps per rotation of the output shaft. This will probably be different for your motors so you may want to update it.

---

Posted on **2017-01-30 17:17:50** by **Bar**:

You also might be interested in the "calibrate motors" button under "More Actions" -> "Calibrate Motors". The motor calibration process runs your motors through a series of movements and creates an internal model for the system which it uses to give you more controlled motion. The calibration is saved in the Arduino's nonvolatile memory so it isn't lost even if power is disconnected. To run the calibration first make sure you have the latest firmware because I fixed a bug in there today. It takes about 15 minutes to run right now. I think I can make it run much quicker in the future. It's best to do the calibration again once you have your router all hooked up because it will compensate for the weight of your router.

---

Posted on **2017-02-01 05:12:45** by **garyw17**:

Thanks for the info.  I was wondering if I was going to have to manually tune the PID gains since my system is different, but it sounds like this takes care of that.  Awesome. I am out of town for a week, but will experiment with it when I get home.

---

Posted on **2017-02-02 13:28:24** by **kiwimaker**:

Hi, I'm in the same position as you (Missed the kickstarter so plan to build my own).  Could you confirm thie motor you got?  Based on the torque and gearbox ratio you provided, I'm guessing you got the 12V medium power (https://www.pololu.com/product/3245) unit?

---

Posted on **2017-02-02 16:38:56** by **TomTheWhittler**:

I am not sure that is the best motor to use. Being a direct geared reduction motor and not a worm driven geared motor it might be prone to movement/slippage with a heavy router attached when no power is being applied. You might be able to compensate by putting weights on the opposite chain end to lessen the weight of the router.
I think a worm driven motor might be best like this one
http://www.ebay.com/itm/High-Torque-Turbo-Worm-Gear-Motor-100RPM-DC24V-3-43NM-GW6280-with-Sensor-DIY-New/112043801280?
but I am not recommending that one as I have not gotten one to tear apart to see the construction. The cheap worm drive one I did get :
http://www.ebay.com/itm/262494873809?
has metal gears but a plastic worm drive gear off the motor shaft. It would not last long trying to drag a router around.
Perhaps Bar has more insight as I am sure he experimented with a bunch of motors before deciding on a custom made motor.

---

Posted on **2017-02-02 17:41:04** by **Bar**:

I think either of those motors with encoders could work. I think @TomTheWhittler is right that you might get movement when the machine is powered off on the direct drive version and that the ebay motor looks a little cheesy, but I'd just go for it with either one. You can always upgrade it if you need to and that way you aren't stuck.

---

Posted on **2017-02-02 18:23:00** by **kiwimaker**:

Thanks for the quick reply.  I'm going to go with these: https://www.surplustronics.co.nz/products/4752-maxon-dc-geared-motor-with-encoder-and-gearbox- 

They're available locally for me and seem to be very good quality.  RS components sell the motor, gearbox and encoder for over $1000

---

Posted on **2017-02-02 22:24:09** by **davidlang**:

a good source for cheap geared motors (no built-in encoder, but that's not hard to add)

http://www.allelectronics.com/category/400400/motors/dc-gear-motors/1.html

---

Posted on **2017-02-02 22:25:11** by **davidlang**:

what sort of speed and torque ratings do the 'official' motors have?

---

Posted on **2017-02-03 08:59:00** by **Bar**:

I don't recal exactly of the top of my head, but I believe they are in the 30kg-cm torque range at about 30 rpm.

---

Posted on **2017-02-03 21:30:34** by **garyw17**:

Yes @kiwimaker, I got the 12 V medium power Pololu.  It's a good point about possible movement when I power off though from @TomTheWhittler.  But with a 227:1 gear ratio I think it will be pretty hard to back drive the motor.  I'll post info once I get to that point.  I only bought two motors, so if it is a problem I can always switch to a worm drive, and use the Pololu to drive the Z axis.

---

Posted on **2017-02-23 10:18:12** by **garyw17**:

OK, an update on my experience with the Pololu motors.  The gearbox failed on one of them last night, after I had increased my sled weight to about 20 lb.  Prior to that (with no weight on the sled) it had been working OK.  Basically, it just was not robust enough for this application, even though I had designed a solid bracket to take the load from the chain, and had used a counterweight to take some of the torque load off the motor.  After some internet searching, I just ordered a couple of worm drive gear motors off Ebay (Item ID: 162355094908), along with a more powerful motor controller and a couple of 600 p/r encoders.

---

Posted on **2017-02-23 10:32:11** by **TomTheWhittler**:

Since Bar is getting close to shipping Beta's now perhaps he has the "real" drive motors with encoders in stock now ?

---

Posted on **2017-02-23 11:19:53** by **Bar**:

We rushed just about enough to ship the betas because shipping things via DHL is expensive. We have a couple spares but I want to hold onto them incase someone gets a bad one. The rest are coming on a ship so we should have them in 2-3 weeks.

---

