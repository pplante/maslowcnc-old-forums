## 'Nother Calibrate Motors problem
Posted on **2017-05-03 23:06:11** by **MikeT**:

Early last week the sled was running off the top of the sheet of plywood when I ran Calibrate Motors. Then we spent the end of the week tracking down the problem. Strangely, the problem seems to have come back.



I installed the new Arduino shield, downloaded the latest version of the Firmware, did Actions/Advanced/Wipe EEPROM, ran the Arduino IDE, and uploaded V 0.67. I got the z-axis kit assembled and calibrated. Then I went back to restart the Using the Temporary Frame to Cut Parts step.



I checked all the Settings values and set Z-Axis Installed to Yes. Then I ran Test Motors/Encoders and got Fail for Testing left-axis motor: Direction 1, but got Pass for Directions 2, and for both directions on the right motor and the z-axis. That didn't seem to make sense, because the left motor turned both directions (clockwise and counter-clockwise) during the test. So I kept going and did Calibrate Chain Length - Automatic, which seemed to work fine. When I did Calibrate Motors things seemed to start off OK, but then the sled migrated up toward the top of the sheet of plywood, an d then started going up over the top. At that point I yanked the USB out of my laptop and both motors stopped.



Logging during Calibrate Motors was as follows. 



Testing 127

-good

Testing 63

-good

Testing 31

-stall

Testing 47

-stall

...

Testing 62

-stall

decided on a final value of: 63

Testing -127

Connection Lost



I presume the "Connection Lost" happened when I yanked out the USB.



Thanks,

Mike

---

Posted on **2017-05-03 23:10:45** by **davidlang**:

failing a test doesn't mean that the motor doesn't move, it means that the arduino doesn't get the response it expect when the motor is told to move. (it can't tell how far or how fast the motor is moving)



try re-seating the connections to the left motor.



until it passes the motor/encoder test, it's not going to work

---

Posted on **2017-05-04 07:47:49** by **Bar**:

@davidlangis right, if the test isn't passing in one direction but the motor is turning that means the signal from the encoder isn't making it to the Arduino.



There are no components along that path so a lose connection is the most likely culprit.



I would try swapping the motor wires to see if the problem moves or stays with the motor. Then I would try plugging the motor into the z-axis port to see if it passes the test there

---

Posted on **2017-05-04 09:07:40** by **MikeT**:

In what follows, I'm numbering the white connectors on the Arduino shield as #1 through #4 from left to right, as I look at the shield from the top with the black power port in the lower-right hand corner. Please see attached photo of my numbering scheme.



Below is  my standard configuration. Note that the left motor (the one on the left as I stand facing the plywood while watching the router making its cuts) is plugged into Connector #3, and the right motor is plugged into Connector #1 (the left-most connector on the shield). This might be backwards from how you're set up.



Connector #1 - Right motor

Connector #2 - Z-Axis

Connector #3 - Left motor

Connector #4 - N/A



The results I get from Test Motors/Encoders are shown below.



Left motor, Dir #1:    FAIL

Left motor, Dir #2:   Pass

Right motor, Dir #1:  Pass

Right motor, Dir #2: Pass

Z-Axis, Dir #1:           Pass

Z-Axis, Dir #2:          Pass



If I swap the left and right motor cables at the Arduino, which is to say I use the following configuration, I get exactly the same results as shown above from Test Motors/Encode rs.



Connector #1 - Left motor

Connector #2 - Z-Axis

Connector #3 - Right motor

Connector #4 - N/A



If I swap the cables at the Arduino again, to the following configuration, I get exactly the same results as shown above from Test Motors/Encoders.



Connector #1 - Z-Axis

Connector #2 - Left motor

Connector #3 - Right motor

Connector #4 - N/A



Does all this say that Connector #1, which the systems always believes is connected to the left motor, is bad? That's hard to believe, because Bar was using this very Arduino shield successfully himself in Portland six days ago.



 [ArduinoShield](/images/2u/46/2u46_arduinoshield.jpg.jpg)

---

Posted on **2017-05-04 09:28:14** by **Bar**:

Hmmm....that is strange. I agree with your deduction that since the problem doesn't move with motor it's got to be the board. 



The strange thing is that between that connector and the Arduino there is nothing but a wire trace on the PCB. I would say maybe take the shield off the Arduino and put it back on? It might be a bad connection between the shield and the Arduino.

---

Posted on **2017-05-04 09:36:15** by **MikeT**:

I just took the shield off the Arduino and then put it back on. No change - Test Motors/Encoders still reports Fail for Left-axis motor, Direction #1.

---

Posted on **2017-05-04 09:37:46** by **Bar**:

Do you by any chance have a volt meter?

---

Posted on **2017-05-04 09:39:39** by **MikeT**:

I don't have a volt meter, but I do have an old, blue Arduino Mega 2560 that you gave me back in November, when I came over to see you in Port Townsend. Should I swap it in and see if that will work?

---

Posted on **2017-05-04 09:40:14** by **Bar**:

YES!!!

---

Posted on **2017-05-04 09:40:44** by **MikeT**:

I'll try it and then get back to you.

---

Posted on **2017-05-04 09:40:58** by **Bar**:

Brilliant. Great idea.

---

Posted on **2017-05-04 09:48:49** by **MikeT**:

I don't know if I'd go with "brilliant". Maybe "desperate" would be more accurate?

---

Posted on **2017-05-04 09:52:36** by **scottsm**:

And 'fortunate' - being able to swap out the Arduino is the best next test.

---

Posted on **2017-05-04 09:59:24** by **MikeT**:

"Fortunate" is working as well as "brilliant" today. (It's good to be Irish!) I just got "Pass" across the board from Test Motors/Encoders, including against the pesky left motor/direction #1 combo.



One thing that changed when I swapped in the old, blue Arduino board, is that the Arduino IDE connected to it via COM4 rather than COM3, which is what I had been using to connect to the Arduino board that came with the Beta package. Ground Control reported "No connection" when I tried Connect via COM3, so I changed that setting to COM4. Now things seem happy. Whatever works, right?!

---

Posted on **2017-05-04 10:02:05** by **Bar**:

Fantastic! We got really lucky there that you already had a spare. Good thinking.



The COM3 COM4 thing is normal, every time you connect a new one it's going to get a new number.

---

Posted on **2017-05-04 10:03:03** by **MikeT**:

Remember that we got lucky because you got generous, and handed me a spare board back in November!

---

Posted on **2017-05-04 10:07:53** by **MikeT**:

It's an absolutely glorious morning up here - a little fog early, which has now burned off, and the warm sunshine is streaming down. I'm going to email you about some of my favorite spots to see on the Oregon coast between Seaside and Manzanita. I hope that one of these sunny days you and Hannah will drive over there early and spend a day exploring. That stretch of coastline is so beautiful that you won't believe it!

---

Posted on **2017-05-04 10:16:08** by **Bar**:

It's an amazing day here too. Summer is just around the corner. I would love to hear your recommendations for where to go on the coast. I'm sure we'll get out there soon :)

---

Posted on **2017-05-04 12:17:48** by **MikeT**:

I was able to cut the test pattern (3 1/2" diameter circle inside a 6" diameter square), including using z-axis to do three separate passes to reach the full depth. I think all systems are "go"!

---

Posted on **2017-05-04 12:23:48** by **Bar**:

:-) :-) :-) :-)

---

