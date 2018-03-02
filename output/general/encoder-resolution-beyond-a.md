## Encoder resolution beyond Arduno sample rate
Posted on *2017-06-04 13:31:29* by *umindedstrikesagain*

Reading the motor specs, 20RPM with 8148 effective CPR and doing the calculation for the current firmware feed rate of 25in/min. #25 chain is 0.25"/link so 25in/min is 100links/min, 10 tooth sprockets so 10RPM. That's effectively 82,000CPR that the atmega micro needs to pickup accurately. 

The current firmware uses the Arduino libraries and interrupt driven encoder inputs. The Arduino ISR routines max out around 72,000/s so any faster feedrate will drop positional accuracy.

8148CPR with 2.5" of feed/rotation @ 10teeth is 0.0003" per encoder tic. Given it usually takes 2 ticks to determine rotational direction, add in wiggle room of 4 ticks your at a reliability of 1000CPR. That is STILL 0.0025" which is like 1/512".

Wouldn't an effective shaft CPR of ~700 which would yield around 1/64th accuracy  be much more useable and take a huge processing burden off of the microprocessor?

---

Posted on *2017-06-04 13:49:53* by *davidlang*

The actual encoder is a 7-line encoder (28 pulses/rev) on the motor, with a 291:1 gear ratio.

With a encoder of this type, it only takes one pulse to detect movement, and you know immediatly which direction you have moved.

As to the speed, as I understand it, the encoder library has assembly routines to be able to handle higher speeds.

---

Posted on *2017-06-04 13:57:47* by *umindedstrikesagain*

My point is still valid though. If we push more motion calculations to firmware (like acceleration curves for corners) the crazy high encoder rate will hog a massive amount of processor time. 

I am going to experiment with a spare 1000CPR encoder from my telescope on the sprocket itself and see if there are any issues. I think having the encoder on the output shaft will also increase accuracy (no gearbox backlash).

An alternative would be to re-spin the board. Since the cost of a PCB is already present you could afford an STM32F103 at 73MHZ with hardware encoder inputs just by removing the pinheaders.

---

Posted on *2017-06-04 14:10:47* by *davidlang*

backlash is not an issue in this design as there is always a load on one side of the gear (towards the center)

one thing to remember, the system needs several pulses to be able to measure speed, so you may run into problems when you get too few pulses (and when your pulse distance is near your desired accuracy, you don't have any wiggle room)

please do experiment, but I suspect that you would be better off with one of the 2400 cpr encoders instead of a 1000 cpr encoder

---

Posted on *2017-06-04 14:22:20* by *davidlang*

going back to your first post.

8148 pulses/rev x (10 r/m) /(60 sec/m) is only 1358 interrupts/sec x 2 (two motors) = 2716 interrupts/sec

If an arduino can do 70k interrupts/sec, we are nowhere close to the limits (around 5%)

one of us messed up our math, please double-check and see which of us it is. :-)

---

