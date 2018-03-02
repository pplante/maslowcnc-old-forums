## Maslow in demo video vs. state of Github repos
Posted on **2017-02-28 11:56:33** by **jtzemp**:

Hey, Maslow peeps!



So, I'm a hacker/maker and I just found out about the Maslow a day or two ago. If I would have come across this project during the Kickstarter campaign, I would have backed it _so hard_. And to say I'm super stoked about it is about the understatement of the year. I "reserved my spot" with a $1USD payment, but I'm kinda anxious to play with stuff and hack on stuff sooner.



Since I've got a little bit of experience with stuff like this (PCBs, firmware, Python, 3D printing/gcode, etc.) and I was considering building myself a prototype version before you're ready to start selling retail (which is where I am in the queue, I'm sure). Given that you're opened the source and looking at the Hardware, Firmware and GroundControl repos, I feel like I could get started making my own Maslow to tinker with until you're selling "retail" versions.



So given that, I was wondering if the Maslow CNC in the demo videos was running off of the same stuff that's in the Github repos. 



I.e. if I start building a Maslow based on what's out there now, is there even some sembla nce of a chance I'll have a unit that can work? As I run into and hopefully fix some bugs, I'd absolutely be contributing back. I love open source!



I'm thinking mostly about the Firmware and GroundControl.



This might be too ambitious, but I was gonna see if the Firmware will compile for the Particle.io platform and if it does, or I can make it w/o too much work, I was gonna design and fab a motor controller PCB with a socket for a Particle Photon/Electron (Electrons have more pins, but Photons should have just enough if I don't use the AUX pins).



Anyway, to make a short story long, where are y'all in the process? Are thinks in the repos "working" enough for an intrepid hacker to cobble something together, even if I'll be fighting an uphill battle both ways in the snow?

---

Posted on **2017-02-28 12:10:22** by **TomTheWhittler**:

Welcome. There are a few post in this forum of other members trying to get a jump on building their own. Bar has been updating the Github but only he knows how recent it is compared to what is shipping in the next couple of weeks to the Beta supporters. One of the failings seems to the the geared motors that others have tried to use. I think if you can wait a couple of weeks then a lot of this will be sorted out as people will get their Beta's and be reporting back.

 If you are really good at software then maybe getting Groundcontrol to work on a Raspberry Pi 3 would be helpful to a lot of folks. The last post about this that I had read indicated it was working but with no mouse support. Of course I am biased as I have a Raspberry Pi 3 waiting to run mine when it ships after the Beta's. I would also like to use the mouse but I'm not that great on the software side so until someone figures that out the people that want to use a Raspberry Pi are stuck.

---

Posted on **2017-02-28 12:13:00** by **TheRiflesSpiral**:

Tom's right regarding the RPi3. Kivy on Raspbian (Jessie) does not display the cursor during mouse movement. If you're using a touch screen, you probably don't care, but if you're using a keyboard/mouse, it's cumbersome.



I left that project at the point where I was going to write a custom touchring.py module for Kivy that forced mouse events to the screen but I haven't got back to it.

---

Posted on **2017-02-28 12:18:23** by **TomTheWhittler**:

sections that might help you.

In General section : Topic : Motor specifications

---

Posted on **2017-02-28 12:19:29** by **TomTheWhittler**:

In technical Details section : Questions About Ground Control

---

Posted on **2017-02-28 12:19:55** by **TomTheWhittler**:

in technical Details section : Motor Direction and sign convention

---

Posted on **2017-02-28 12:21:50** by **TomTheWhittler**:

In Dev section : Raspberry Pi 3 setup for Ground Control

---

Posted on **2017-02-28 15:19:24** by **Bar**:

Hey jtzemp, welcome!



The repos are 100% up to date. We're totally open so there's no secret version of anything we have hidden away. 



Pull requests are welcome for any bugs you find or features you want to add. Things are evolving pretty quickly so expect to have to update off of the master branch regularly. 



We branched the conversation a little to talk about the raspberry pi, but there's some good news on that front. I got mine working with both multi touch and mouse input late last night. I will post a copy of my disk image as soon as I can figure out how to make a copy of it. I believe there are still issues with mouse events over SSH so if you aren't planning to connect a real monitor we've still got some work to do, but progress is being made. Onward!

---

Posted on **2017-02-28 16:20:31** by **jbnimble**:

WRT your question about Atom.io, the answer is yes using the Platform.io plugin, instructions on setting up the Firware project in the readme here: https://github.com/MaslowCNC/Firmware

---

Posted on **2017-02-28 20:25:44** by **scottsm**:

Interesting, jtzemp! FWIW I have a couple Particle.io Photons on hand, and I'm in line for one of the beta packages. I'm willing to prototype up a connection from a Photon to the H-bridge board and run some tests if you are interested and have some code to test. I think the code dealing with motor location is interrupt-driven, and I wonder if the network service routines of the Photon would interfere. Interesting to try, though.

 I also wonder about the ESP32 for this. Interrupts are available in the Espressif IDE, and is think they're close to ready in the Arduino IDE, so that might be something to look into as well.

---

Posted on **2017-03-01 10:20:17** by **jtzemp**:

Yeah, I started work porting the firmware last night, but the Encoder library from PJRC uses a lot of stuff from Arduino libraries, which are AVR-specific that don't really translate very well in ARM. I think it's certainly doable, but not a quick fix. I'll keep plugging away as I have time. 



Thanks for getting back to me, everyone!

---

Posted on **2017-03-01 12:41:55** by **scottsm**:

@Bar, how tightly coupled is the firmware to the encoder library? It looks like the interrupt portion and the assembly language inline parts are used. Do you have a feeling about how sensitive to speed this is? Do you know how fast the interrupts come while the motor runs?

---

Posted on **2017-03-01 17:04:22** by **Bar**:

The pulses don't come that fast. The library is pretty heavily optimized and hard to port, but we really don't need that much optimization. I would expect less than 10k pulses/second at full speed. Even that is a safe guess, I bet its quite a bit less. It might be faster to duplicate the behavior of the encoder library rather than try to port it.

---

Posted on **2017-03-01 18:30:01** by **scottsm**:

If what you say is true, it should be possible to duplicate the functions. The Photon runs at 120Mhz compared to the Mega at 16Mhz (I think). The Esp32 goes up to 240Mhz. Unless some serious processing gets done with each pulse it seems possible. We'll have to see how the network processing affects things, though.

 I'll hook up a scope and have a look when I get set up.

---

Posted on **2017-03-01 20:45:39** by **davidlang**:

note that there is support to use the arduino IDE to compile code for the ESP8266/ESP32 chips, so start off by just loading up the code and trying it :-)



I expect the biggest change is going to be around the configuration for more advanced protocols (i2c etc) where the arduino has a fixed name but the ESP* can use any port, so they have forked libraries that take additional parameters to specify what pins are used for what function.

---

Posted on **2017-03-01 21:38:24** by **jtzemp**:

Yeah, @scottsm good thoughts and questions! So, IMHO the Photon doesn't always need to connect to the cloud. The first iteration probably wouldn't. Future iterations might try to allow you to do GroundControl from an Internet connected device (web page?) vs. a computer/Rpi/tablet. But yeah... for me, it's just enough to get it working at a basic level.

---

Posted on **2017-03-01 21:52:21** by **scottsm**:

That will make it all easier!

---

