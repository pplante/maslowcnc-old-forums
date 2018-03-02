## what's the status on the three layer pid project
Posted on *2017-05-11 17:07:29* by *davidlang*

I'm seeing interesting sounding commit comments on the topic, any reports here (or do we have to wait until next Wednesday's status report :-)

---

Posted on *2017-05-11 17:44:32* by *davidlang*

I notice that at 'full speed' (48 ipm), the minimum step size is almost 4mm due to the time needed to do the kinematics computation at that speed. This works out to ~3KHz decision cycle on this processor

This makes me think that we should be looking at options to possibly use something faster than an arduino (I'm assuming a mega @16MHz)

Thinking about the requirements, it looks t me like there is a need to be able to drive 4 motors (2 GPIO each for output, 2 GPIO each for encoder, ideally with pwm on the motor outputs), for around 16 GPIOs. plus the serial interface.

Is the maslow using any analog inputs? (I can't see where they would be used, but I'm asking to be sure).

There are a lot of faster options out there, and a quick check of the #include lines in the firmware doesn't show much in the way of special libraries that are arduino specific.

I don't know about a lot of different options, but the ESP-32 chip which runs at 160/240MHz and has lots of GPIOs a vailable (or the esp8266 chip which is tight on GPIOs and runs at 80/160 MHz). both of these are 32 bit chips vs the 8 bit arduino should make a lot of the complex math go faster.

---

Posted on *2017-05-11 17:45:27* by *davidlang*

once we get the software working well, we can look at various ways to speed things up, getting things working accurately is more important than getting it working fast at this point.

---

Posted on *2017-05-11 19:29:42* by *scottsm*

I'd like to look at the EPS32 for this. It seemed to me that the interrupts and PWM peculiarities of the ESP32 would need to be reviewed by one with deeper insight than I have, though.

---

Posted on *2017-05-11 19:45:17* by *Bar*

The early results on adding the second layer of PID are positive so far. I'm seeing much tighter position holding, and theres still quite a bit of tuning to do.

I agree that we're running of of head room on this processor pretty quickly. I'd advocate for the Arduino Yun as where we go to grow, it's pin comparable with the Mega and at 96mhz (32 bit) so we'd speed things up. The other two advantages are that the USB drivers for their boards are very well tested by that community, and if we can pigyback on their economy of scale it keeps the cost down. We might be able to buy Yun comparable boards for close to the cost of the chip alone if we're rolling our own.

I think the first place to look is to see how we can accelerate the computation of the kinematics, and where else we can shave some fat. There's a lot that could be trimmed to speed things up.

But, before we go there I agree with @davidlang, let's see tight consistent stable software reliability before we push speed

---

Posted on *2017-05-11 20:02:19* by *scottsm*

Do you mean the Arduino Due? It's pinout is similar to the Mega...

---

Posted on *2017-05-11 20:06:41* by *scottsm*

Shouldn't be too hard to adapt the Maslow board to 3V logic :), a relatively easy conversion.

---

Posted on *2017-05-11 20:18:34* by *davidlang*

the arduino cpu on the yun is still only 16MHz

---

Posted on *2017-05-11 20:25:14* by *Bar*

Thanks guys, sorry. I absolutely meant the due. :-)

---

Posted on *2017-05-11 20:36:41* by *davidlang*

does the maslow motor board work with 3.3v or does it require 5v?

---

Posted on *2017-05-11 20:39:16* by *larry357*

https://www.aliexpress.com/item/Official-DOIT-ESP32-Development-Board-WiFi-Bluetooth-Ultra-Low-Power-Consumption-Dual-Core-ESP-32-ESP/32776342162.html at $11.34 is a bit cheaper than the yun :P

---

Posted on *2017-05-11 20:40:30* by *larry357*

o.k still cheaper than the due (by $2) :P

---

Posted on *2017-05-11 20:44:41* by *davidlang*

I'm seeing the due at $50 https://www.sparkfun.com/products/11589

but the esp32 is faster.

neither uses the atmega chip that the rest of the arduino family uses, both can be run through the arduino IDE. both are 3.3v not 5v. so either should be a viable option.

---

Posted on *2017-05-11 20:48:04* by *Bar*

In theory the sheild should be 3.3v compatible, but I haven't tested it. The motor controlers and encoders are good for 3.3 logic, but the motor controlers need a 5v supply. I'm guessing we're close to being ready for 3.3 volts, but a few little things would need to get rearranged. 

I agree that both are good options.

---

Posted on *2017-05-11 20:59:52* by *davidlang*

the due is 84MHz, 512K flash, 96k ra
the esp32 is 2x240MHz, 4M flash, 520K ram and includes bluetooth and wifi. <$10 each for the module, a couple bucks more mounted to a board to be breadboard friendly (see the aliexpress link above)

I don't know where you are on the manufacturing of the motor adapters, but if they haven't been built yet, making them 3.3v compatible would be a very good futureproofing feature.

---

Posted on *2017-05-16 10:39:00* by *scottsm*

The Due and the ESP32 have different approaches to non-volatile store age from the Mega. The Firmware currently arranges for storing 100 floats (linSegs) for each of the three axes, which persists through firmware re-programming. It looks like these are used to record the current position. The Due has nvs that lives within the program space, so is erased when the firmware is upgraded. The Esp32 nvs persists, but in the current Arduino environment has room for only ~210 floats in a Key/Value store.
Is there a need for the values stored to be available after a firmware update, or is it reasonable (maybe preferable?) to clear them when the firmware is updated? If not, the Due might need an I2C eeprom to provide the nvs. 
 Is there actually a need for storing 100 floats for each axis, or would fewer suffice? If the full size is needed, an ESP32 would need a different approach to nvs.

---

Posted on *2017-05-20 21:28:00* by *davidlang*

The hifive1 bord also fails due to the need for eeprom
https://www.sifive.com/products/hifive1/

---

