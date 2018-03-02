## Feasibility of a ground control managed "Master power switch"
Posted on **2017-03-27 14:42:33** by **Jennifer D**:

Not sure if this question has been posed yet. 



I'm wondering if there's any possibility of adding a switch that would control power to the router. I ask, because even while I was trying to be extra careful and safe, I found myself tempted every so often to adjust my router depth without turning it off.  I resisted, but I can see it happening at some point! 



On my wishlist for my shop is one of these to manage my shopvac dust collection - https://www.amazon.com/BCTINT-10031-010-Automated-Vacuum-Switch/dp/B0035YGLZG 



Which made me think that having something similar that the router plugged into would be fantastic. When GC asks you to adjust something, or even with the panic switch/limit switch ideas, that GC could turn that switch off. For people who don't add the z-axis control if would be a great safety measure, as the program would turn the router off, and wouldn't turn it back on until the operator hit ok. 



I'm new to this sort of DIY, so I'm not sure what's entailed, but thought it worth posing the question!

---

Posted on **2017-03-27 14:52:54** by **aalbinger**:

So far the consensus seems to be something like http://a.co/5dC5cBE controlling power to the router and the motor control board on the arduino.  The arduino firmware will see that it hasn't gotten updates from the encoders and ground control will wait for the arduino to tell it what is going on but the router won't be spinning and the positional motors will be off.



In theory turning the power back on will let it start up where it left off.  In practice you might have to figure out a way to power up the router before the positional motors so it can build some momentum before being asked to cut.  I'm also not familiar with the motor tuning code and don't know what a loss of power to the positional motors/encoders would cause the firmware to actually do.

---

Posted on **2017-03-27 15:50:29** by **Bar**:

Those automatic vacuum turn on things are pretty slick, I've been eyeing one myself.



I'm hesitant to add a relay which turns on the router automatically for safety reasons. It's very dangerous to have the router turn on while changing a bit for example. I agree that it would be very convenient, but as a safety concern I probably won't add that feature. There are 6 AUX ports available, and I'm sure a number of people will use them to turn on and off the router.



I know shopbot solves this problem by chaining the wrench for changing the router bit to the starting key making it so you can't turn the machine on while changing bits.

---

