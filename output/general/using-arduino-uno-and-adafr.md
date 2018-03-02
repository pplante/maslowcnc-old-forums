## Using Arduino Uno and Adafruit Motor shield instead
Posted on **2017-06-02 01:57:29** by **dennisgislum**:

Does anyone know if it is possible to use a Arduino Uno and a Adafruit Motor shield instead of the Arduino Mega and Maslow motorshield?

---

Posted on **2017-06-02 05:32:09** by **gero**:

Hello @dennisgislum

From my novice opinion, the general answer would be “Yes”.

It’s open source and you are free to modify anything to make it work.

So it is possible.

The downside is quite huge however, compared to the savings.

You might need to skip the automated Z-Axis due to reduced number of pinouts.

You also might need to strip down the firmware code, due to reduced memory.

The machine settings stored in the eeprom of the Mega and the processing speed are 2 more things that would need to be considered.

So out of the box, “No”, I don’t think this will work.

---

Posted on **2017-06-02 05:47:56** by **dennisgislum**:

Hi gero



Thanks for your reply.



Everything you write makes sense.

---

Posted on **2017-06-02 06:04:58** by **gero**:

Adding features and improvements weekly could bring us to the limits of the Mega soon. I have read discussions to port to 'bigger/faster' boards but nothing seems to be decided yet. I would keep some 'space' for all the good things that are still to come :-)

---

Posted on **2017-06-02 06:27:46** by **dennisgislum**:

Ok I have a spare Raspberry Pi, could that be the next bord to use?

---

Posted on **2017-06-02 07:25:28** by **gero**:

The Pi is not compatible with the Arduino Firmware, it can make a nice controller for GrounControl though. I think the boards discussed where Teense and something ESP32, but don't know enough about this stuff.

---

Posted on **2017-06-04 10:14:50** by **bryanpollock**:

I would suggest the Teensy, much faster.

---

Posted on **2017-06-04 10:43:08** by **davidlang**:

we've had the discussion of what possible chips to use when/if we need more speed several times now :-) we probably shouldn't re-hash it here.

---

