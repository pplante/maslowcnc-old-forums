## Where to get Motor/Gearbox/Encoder?
Posted on **2017-06-04 22:58:17** by **msj121**:

I was trying to find a suitable replacement that works the same if not identical to the one in the project.

---

Posted on **2017-06-04 23:40:56** by **davidlang**:

the unit provided in the kit is custom built

it rotates at about 10 rpm, produces 30kg-cm of force and has 8148 pulses/rev on the encoder. This is a gear reduction motor with a 28 pulse/rev encoder on the motor and a 291:1 worm gear final drive.

This is a bit of overkill, higher speeds may be usable, testers have had their sled ripped apart from the force of the two motors pulling on it, and you could probably go down to 2k or so pulses/rev

---

Posted on **2017-06-05 10:35:35** by **taimooryousaf**:

Could I use these motors?
(link)https://www.aliexpress.com/item/Geared-Motor-High-Torque-Reduction-Motor-with-Encoder-Srong-Self-locking-30RPM/32785000612.html?spm=2114.13010308.0.0.CPxnBq(link)

---

Posted on **2017-06-05 11:08:22** by **TheRiflesSpiral**:

It doesn't look like they specify torque on that unit? I'd be wary of plastic gearing...

---

Posted on **2017-06-05 11:13:59** by **davidlang**:

I've seen at least one other person say that they intend to try using something that looks very close to that.

If the torque is too low, then you will have trouble cutting in the top center (where the tension is highest) and may have to slow down your cut speeds. raising the motors higher above the workpiece (and possibly out a bit) will help if you run into grief like this.

---

Posted on **2017-06-07 16:45:51** by **taimooryousaf**:

Is it possible to get the encoder module and attach it to a geared motors with the specs mentioned above?

---

Posted on **2017-06-07 17:02:05** by **davidlang**:

the encoder is built in to the motor, it's not a separate component. There are a lot of encoders available that you can use, either connected to the motor or connected to the output shaft.

---

Posted on **2017-06-08 01:52:56** by **dennisbingham**:

@taimooryousaf I found these motors on AliExpress after your question. The torque is still a bit low, but the specs are clear on this page at least: https://m.aliexpress.com/item/32361264555.html

---

Posted on **2017-06-08 14:24:32** by **willishf**:

Posted links for motors that we are using in the Post titled 

Calibration for different motor/gearbox

---

Posted on **2017-06-21 21:41:05** by **peer89**:

Hi
I'm new to the Maslow Community and thinking about to Build my own Maslow here in Germany.
Im looking for Motors and find these 
https://www.ebay.de/itm/201837824564 
Do you think they should work ?
Greetings from Germany 😉

---

Posted on **2017-06-21 21:55:25** by **davidlang**:

I can't read german, but other than the fact that it's 24v not 12v and I don't know if the arduino shields can handle 24v it looks plausible

---

Posted on **2017-06-21 21:56:57** by **davidlang**:

see the topic 'open source parts' where the exact motor/gearbox that maslow uses has been identified.

---

Posted on **2017-06-21 22:07:55** by **peer89**:

The specifications are 
5Nm
120rpm
24v
I would use 24v Motor driver for those.

---

Posted on **2017-06-21 23:24:21** by **davidlang**:

those motors are faster and more powerful than the stock maslow motors, so they should work. You just need to get an encoder hooked to them somehow (either a low-res encoder on the motor, or a high res encoder on the output shaft)

---

Posted on **2017-06-21 23:54:54** by **peer89**:

thats the Pro of this motor ... they have allready an encoder on the motor ;)
nice!

---

Posted on **2017-06-22 00:33:15** by **davidlang**:

how many pulses/rev on the output?

---

Posted on **2017-06-22 00:55:48** by **peer89**:

i waiting for an answer from the seller. 
i keep updating.

---

Posted on **2017-06-22 02:00:03** by **davidlang**:

one interesting thing about that motor is going to be that it doesn't have an output shaft, it has a hex socket that it rotates. So you will have to have a bearing and shaft to hold the sprocket and have the back of it be a hex shape to connect to the motor.

---

