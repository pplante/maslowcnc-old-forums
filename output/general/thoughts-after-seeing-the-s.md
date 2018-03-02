## Thoughts after seeing the system at the maker fair
Posted on **2017-05-23 21:00:26** by **lostpath**:



---

Posted on **2017-05-23 21:23:42** by **lostpath**:

I was very impressed with the system at the Bay Area Maker Faire and placed an order, but I wondered if a few simple changes might make the system better.

My suggestions of things to try are: 

a) Add some counterweight to the non-working ends of the chains (where the elastic pulls), as if the drive was closer to balance (you need some tension for backlash issues). The motors would need to work less hard, and that would be good for heat on the control board.

b) Adding some sorbothane (anti-vibration rubber) between the stands and the panel, and between the router and its sled might reduce vibration in the system which should allow higher cutting speeds or higher accuracy, or better edge quality. Worth a try?

c) Personally I would have used an ARM based board like the Teensy 3.x (runs Arduino out of the box) or the FRDM-K64F (harder to start using but more powerful). Both are MUCH faster which should help with well everything! This could be done latter if necessary.

---

Posted on **2017-05-23 22:11:02** by **davidlang**:

backlash is actually not an issue, there is only load from one direction, towards the center of the machine. Adding counterweights would actually increase the chances of moving the gears in the wrong direction and triggering backlash issues. All that's needed is to keep the chain from getting tangled up.



I agree that a faster processor is needed (currently, at 48 ips it can only figure out what it needs to do every 3mm due to processor limits), but there is also the issue of the motor selection. With the max speed @12v that the motors produce, (after their gearing) and the ~2cm diameter sprockets on the motor, the max that a chain can move is ~48 ips. Currently it is set to a max of 25 ips while cutting until we get all our accuracy issues worked out.



You would have to go to a faster motor, or larger diameter sprocket to get faster speeds.



Bar tends to cut slower, at ~20 ips, and in extremely shallow cuts (0.1"/pass). We know the machine can do much better than  that, but until we get the accuracy figured out, we haven't really tried to push it.



The padding is an interesting idea, we'd have to see where it actually does some good, beta-testers, please experiment :-)

---

Posted on **2017-05-23 23:18:09** by **lostpath**:

I agree backlash is not an issue with the offset weight, but I still think the weight offset maybe more than optimal. Someone with a system can test this its pretty simple to add counter weights although the more weight, the more inertia, so it could actually add to the peak power needed!



If the Teensy 3.5 had the enough of the right type of pins, it would be the simplest to move to as it uses the same language but is 120 MHz and 32 bit. It is also cheap!



I was also wondering about a few other things on the accuracy. Looking at the system, (and code) you deviate from a simple math problem because:

a) the point the chain leaves the sprocket varies with angle

b) the sled tilts as it is moved around the board

c) cutting adds a force that also rotates the sled



I think a) could be reduced if the chain left not from the sprocket, but from a couple of small diameter rollers that pinched it at a defined point after the sproket.

b) could be eliminated with a  sled that had the "virtual" holding point of the chains at the center of the sled's c of g, or maybe the spindle axis a lthough this might make (c) worse and would be more expensive to make. 

All of these mechanical refinements might be no better than simply mapping the distortion field as was commented before. It might seem a dirty solution, but it could be the fastest thing to calculate if the distortion is a simple function. Sometimes simple is better!



Some vibration absorbers are always a good idea although if you want to get fancy you should experimentally measure the resonance frequencies and tune the absorbers. Of course you need a calibrated hammer and accelerometers to do it right.

---

Posted on **2017-05-23 23:35:28** by **davidlang**:

well, this is C, that works on everything :-)



The issue is libraries, many of the 'arduino compatible' devices don't have eeprom for example, which this code depends on, so there will be some porting effort needed.



as for the complexity of the math problem



the cutting force doesn't make a noticeable difference. but the other two issues are real, you missed a few



the amount of chain between the top of the sprocket and where the chain moves off at an angle for example 



take a look at https://robotics.stackexchange.com/questions/10607/forward-and-revers-kinematics-for-modified-hanging-plotter/10858#10858?newreg=13734dd331424a0ea0d2ddc79c562910 for the writeup that the math in Kinematics.cpp is based off of.



moving the chain through pinch rollers doesn't solve the problem, it still departs the pinch rollers at different angles.



look into what's been done, nobody here is saying the math is trivial (only the folks in the youtube comments who haven't done it are dismissing it as trivial or something anyone who took a one week programming class could do trivially)

---

Posted on **2017-05-23 23:36:28** by **davidlang**:

there is a point of diminishing returns.



with known broken software, we think we are at around 1/16", and we think that (not so) simple software fixes will probably be able to get us to 1/64"

---

Posted on **2017-05-23 23:40:51** by **davidlang**:

by the way, there are people experimenting with different sled designs, including ones trying to virtually attach to the center of the sled.

---

Posted on **2017-05-24 00:21:14** by **lostpath**:

Have a look at the Teensy 3.x, it has most of the libraries ported, see https://www.pjrc.com/teensy/td_libs_EEPROM.html for details of the EEPROM.

---

Posted on **2017-05-24 05:02:27** by **davidlang**:

doing a bit of quick digging, I found instructions for windows and mac, but not linux (on installing teensy support for the arduino IDE), can you point me at the correct instructions?

---

Posted on **2017-05-24 07:48:15** by **lostpath**:

https://www.pjrc.com/teensy/td_download.html for all the support.

---

Posted on **2017-05-24 08:12:46** by **davidlang**:

Ok, I installed that and the build fails on the other common problem, interrupt handling. So there are still going to need to be changes to the code to handle other boards.

---

Posted on **2017-05-24 08:47:06** by **scottsm**:

There is some inline assembly code in the source, so there will be changes required for almost any other board :) . The purpose was to speed up I/O, though, so it shouldn't be needed for a significantly faster processor.

---

Posted on **2017-05-24 09:01:02** by **Bar**:

The inline assembly is just in the encoder reading, right? I have a hunch that library will run on the tinsy without being ported because it was written by Paul (the creator of tinsy)

---

Posted on **2017-05-24 09:07:39** by **davidlang**:

In my 'smoke test' compiles for other boards, I haven't ever gotten far enough to trip over the inline assembly, everything has tripped over either the interrupt or the eeprom issue (arduino due, esp-32, esp-8266, HiFive1)

---

Posted on **2017-05-24 11:06:19** by **scottsm**:

The eeprom issue would be fairly straightforward to tackle, there are really only two places that actually address the EPROM library so nadapting to another form of storage is pretty focussed.

 The interrupts are where the snakes are; the timer and encoder libraries use them. The encoder library is where the inline assembly code is found as well. Interesting places to explore...

---

Posted on **2017-05-24 11:51:39** by **davidlang**:

it could be as simple as the ISR call needing a extra parameter or having a different name.

---

Posted on **2017-05-24 12:31:25** by **davidlang**:

ok, looking at bit at the logs, some of it is missing includes, some of it is different names for interrups

---

Posted on **2017-05-24 13:32:49** by **mooselake**:

If you're looking at the ARM route, try the Re-ARM board rather than the ARM Teensy.  It should take the driver board without retracking it.

---

Posted on **2017-05-24 14:10:32** by **davidlang**:

There are two approaches we (mostly the community) are looking at.



1. is there anything that's a plug-in replacement that will work (the driver board was not designed to be 3.3v, most of it should be able to run on 3.3v but there was one item that needs 5v)



at the moment, I think the only possible option for this is the HiFive1, which is very fast (much faster than the Teensy), but also $59. I ordered one to play around with.



2. if we can't do a plugin replacement, then anything is on the table, and we can just go price/performance.



we need 5 GPIO pins per motor (2 encoder, 2 direction, 1 PWM), the motor controller supports 4 motors, so this would be 20+ GPIOs.



At 4 ipm, the current software (as of changes today) can figure it's position about every 1.5mm, which is ~1/16", we really should have 4x the speed, and it would be good to have headroom beyond that. going to 32 bit should significantly speed things up



It would be nice to have something that's got some wireless capabilities and is cheap.



In part because it's something I know a little about (and it's the ne w hot chip), I've been leaning towards the ESP32 in this case, it's <$10 and dual core (32 bit @240MHz), wifi and bluetooth and would be very easy to solder to a motor controller board (no need for expensive headers to connect the two)

---

Posted on **2017-05-24 15:05:40** by **jtzemp**:

So, I'm coming to this thread (all threads really) late, but I'd started on a Particle Photon port (it's ARM 32 based with WiFi). I got hung up on the AVR-specific code in the PJRC Encoder library. A coworker of mine recently ported the PJRC Encoder library over to Particle's platform, and I was gonna pick up where I left off on the port. (I was slammed for the last few weeks).



Since I'm a relative noob here, can you tell me about having/needing 4 motors? I thought there were just 3 (the two "pen plotter" motors on the arms and one for the Z-axis). What am I missing?



The reason I ask is that the Particle Photon only has 18 GPIO. On the port I was working on, I also wanted to include an SD card to store files.



The idea was that the control software would push the instruction set over wifi and store them on the SD card for the MCU to run w/o being connected to a "real" computer. Then over the Internet I'd be able to check on progress. 



If I add an SD card, that uses up pins for the 4th motor (unless I make an adapter to make motors/encoders run over SPI).



I've been us ing KiCad (not Eagle) to do the PCB so far, in case anyone wants to collaborate. I'm not a PCB expert, I've only done a small handful of boards before, so I welcome feedback. I haven't pushed my changes to Github yet.



If the Photon isn't viable with it's 18 pins, Particle makes a different board with a SMD form factor that exposes 25 pins. It's called the P1, and it'd need a more complicated board design (power regulation, RGB LED, buttons, USB port, etc.), but it's certainly possible.



They both still run at 3.3v, but the Photon can take 5v it just steps it down via an onboard regulator. The Photon is $19 and the P1 is $12 (but you have to buy in multiples of 10).

---

Posted on **2017-05-24 15:13:10** by **davidlang**:

well, the standard design 'needs' 3 motors, but the board has 4 channels on it, so if we are looking to pick something new, we should pick something that can support all 4 :-)



It would also have been good if the motor controller design only had one direction pin per motor, having two scares me. I haven't looked at the circuit board, but having two strongly indicates that it's possible to turn on both sides of the h-bridge at the same time, and if the pwm is still active at the time this happens, it can burn out the chip, especially if the system crashes/stops at just the wrong time.

---

Posted on **2017-05-24 16:18:30** by **dougl**:

As for the Z-Axis, and router motor for that matter, I want to get that all on wireless so only a 110V power cord is dragging around.  That would be the first thing I'd shoot for once I got a working system. So, in reality we'd only need 2 motor controller circuits.

---

Posted on **2017-05-24 16:43:44** by **scottsm**:

The present design uses separate I/O pins for the two direction control inputs of each motor, but they are always driven in complement with the present software. One I/O pin and an inverter would do the job for each motor, and this would reduce the number of pins needed. That would rule out the possibility of things like dynamic braking, but with the gear arrangement on the Maslow dynamic braking doesn't seem as useful as opening up more controller board options would be.

---

Posted on **2017-05-24 20:28:50** by **scottsm**:

Digging into the EEPROM usage in the firmware, it looks like there are fewer than 100 floats stored there. On the Arduino platform of the ESP32 the Preferences library will store a few more than 200 floats, so this looks promising. All the pins can do interrupts and most of them PWM. This look like a interesting path to explore.

---

Posted on **2017-05-24 22:29:20** by **lostpath**:

Are the current updates, the time for one loop of the PID loop? If so I would think you need to go much faster than one update every 1/64 inch. If it is just changing the PID's target, the chain length loop, I would guess you would want to be at least 3x the intended resolution. What I am getting to is I suspect you need not a 4x speed up but a 12x speed up. The current processor is 8 bit 16 MHz, the ARM/RISC solutions are 32 bit and at least 120 MHz so that should be enough ESPECIALLY if it is one with a FPU which should significantly speed up the maths. Thinking about it maybe its the lack of a FPU that makes solving the chain length take time on the ARV platform. For the board options I think a FPU should be a requirement. As pointed out there are lots of options. The ESP32 has great potential, but it is in development, using it might be a time constraint issue. I would suggest going for the board with the most support already existing. You do not want the project to turn in to a micro-controller development tool project! (this is the reason I suggested the Teensy 3 f ast, cheap and good library support although poor footprint compatibility) There are a lot of options I see a Make magazine here with an advert from DigiKey with 53 MCU's listed, and I think you have named a few NOT listed!

---

Posted on **2017-05-25 00:07:41** by **davidlang**:

well, at this point I suspect tht they have already ordered all the arduinos for the kickstarter backers, so it will be arduinos that we get. I'm looking at a 2nd generation or individual upgrade.



what do you mean about the esp32 still being in development? it's shipping and there are a good number of librarires supported (I can't tell if it's enough yet, I'm watching it for home automation uses, replacing the esp8266

---

Posted on **2017-05-25 09:34:23** by **Bar**:

They are ordered and more importantly have arrived, but more than that I have reservations about solving things by adding more processing power. We do always have that option, but I have no doubt that the processor we have is fast enough if we take the time to optimize the code. The kinematics math (the thing which uses the most processing power) computes twice as fast in this week's version (v0.71) as last week's version (v0.70) and we've seen a general improvement of 4x-5x in how often we can recompute the position over the last month. There's still quite a bit of optimization and clean up we can do.



I'd like to see us really nail down the math and optimize the math so that when we go to a faster processor, we can use that extra computation power to do add new features like bluetooth or wifi.

---

Posted on **2017-05-25 10:20:29** by **dougl**:

What would be helpful here would be edge testing so we know how fast the system can operate and be within specs.  Using COTS L298 drivers should be an easy hardware test if the software is portable to something like and Odroid, rPi3, BBB, etc( ie standard Linux ARM ). I run Delta 3D printers and 8bit AVR works but the kinematics math limits quality and speed so most have moved to 32bit controllers. From the ATMega2560.

---

Posted on **2017-05-25 10:22:20** by **dougl**:

Might I add, many still build with ATMega2560 but those who have been doing it for a year or two often start migrating. So there's nothing wrong with it for the initial system since it's been proven to work.

---

Posted on **2017-05-25 10:38:45** by **davidlang**:

right now, we have some problems that aren't related to speed, even when going slow, we have something wrong (either in the math or it's far too sensitive to small measurement errors in defining the machine)



The last I heard, a 7' long horizontal cut has a bow of ~1/16" or so towards the center.



We need to do some accuracy tests since the new double-PID loop firmware was put in place.

---

Posted on **2017-05-25 10:40:58** by **scottsm**:

With the motors running flat out, the left and right encoders each measure around 670Hz on each channel, the z encoder channels 560Hz. With the .71 firmware, a G0 command seems to generate around 280Hz from each encoder channel (software limit looks like 1000mmps, CNC_Functions.h line 492), with a 50% duty cycle.

 The PWM signal is 490Hz and rarely reaches 80% when executing G0 moves around the work area. 

Those are some of the factors that we're working with.

---

Posted on **2017-05-25 10:47:15** by **davidlang**:

interesting, try raising that speed limit and see what you can push it to. (although, as I said, speed isn't causing the bigger accuracy problems we're fighting)

---

Posted on **2017-05-25 13:04:31** by **scottsm**:

Raising the speed limit does reach 99.8%.

---

Posted on **2017-05-25 16:27:18** by **davidlang**:

what speed did you end up getting to?

---

Posted on **2017-05-25 16:29:10** by **mattnelson**:

@scottsm I'm a little slow, reach 99.8% of what?

---

Posted on **2017-05-25 16:39:00** by **scottsm**:

The motor speed is controlled with pulse-width modulation. The result isn't strictly linear, but a 99.8% pulse width means that the voltage is at the maximum available for all but 0.2% of each time slot. That's as fast as the motor can run :).

---

Posted on **2017-05-25 16:43:24** by **scottsm**:

David, I changed the speed limit to 2000mmpm and ran from the bottom center toward the top center. It was as I approached the upper end that the PWM maxed. Horizontal traverses and motion over near the edge didn't run the PWM up as much; not as much torque needed I'd guess.

---

Posted on **2017-05-26 01:11:15** by **davidlang**:

I wonder how close to that speed you actually got.

---

Posted on **2017-05-26 07:01:29** by **scottsm**:

670Hz observed on one channel, 8148 steps per rotation, 10*6.35mm per rotation, the maximum chain speed is calculable. Motors 2995mm apart, work area 1219mm by 2438mm spaced 369mm below the motors. Two chains pulling the sled between them, what's the theoretical maximum? :)

---

