## Raspberry Pi Controller?
Posted on *2016-12-27 13:22:49* by *dom_e_uk*

Hi Guys,

I'm super stoked about getting my hands on Maslow and am currently occupying my mind with other stuff.

Basically, my goal is to have Maslow hanging on the back wall of my garage, with a screen next to it wall mounted.  It'll be touch screen with a Raspberry Pi inside it with a USB out (for PiSerial) and Wifi to connect to my home network.  In essence, I'll be designing my projects in the comfort of my office/lounge and save all the ideas on my Network Storage.  Then when I feel the need I can goto my garage and load my projects from the NAS and send it onto Maslow.

Now, I'm happy with making my design and generating my gcode.  The issue I don't get is getting GroundControl onto the Pi.
I've tried crowbaring it through every way i can think of and install KivyPie etc, but I'm still at a loss.

My forte isn't programming and one of the reasons I got a Pi was to stretch myself, but I'm a bit out of my depth.  If anyone has any ideas then they'd be welcome.

Dom

---

Posted on *2016-12-27 19:17:26* by *TheRiflesSpiral*

You can check out the details of Ground Control here: https://github.com/MaslowCNC/GroundControl

Raspbian installs the python runtime and an IDE by default so I think it would be a great place to start.

---

Posted on *2016-12-28 08:48:42* by *dom_e_uk*

@TheRifleSpiral

I've been following the instructions on the github site, but for some reason it doesn't like Kivy or Pip...... (No idea).....

I've got the Ground Control software on it and unzipped, but whenever I try to run it, it's just there laughing at me!

---

Posted on *2016-12-28 10:07:59* by *Bar*

I'm going to order a Pi so I can jump in, it seems like a lot of people are interested in going the Pi path so I want to make sure it works smoothly. 

Any recommendations for which one is the right one to test on, or are they all pretty similar?

---

Posted on *2016-12-28 11:27:10* by *larry357*

All similar, but the pi3 is faster and has wifi http://core-electronics.com.au/tutorials/compare-raspberry-pi-boards.html

---

Posted on *2016-12-28 11:28:57* by *dom_e_uk*

I think they're all pretty similar...... The Pi Zero is the cheapest (smallest and coolest aswell in my opinion). It only has 1 USB port (but you can connect hubs).  

Personally I'm using the Pi 2, which has built-in Ethernet and 4 USB so it's easier for WiFi dongles and connecting to the Maslow itself.

My thinking is just to have the Pi hidden internally in a monitor and then it's effectively standalone, and almost as if the Maslow has a built in GUI station.  That's just my thinking though.

---

Posted on *2016-12-28 19:34:49* by *chadzimmerman*

I have a P2 running my network server, been running without complaint for over a year now.  I am going to get a P3 for the Maslow control if I go that route.  Will get a P3 anyway to play.. would be nice to have a computer in the workshop anyway.

---

Posted on *2016-12-29 02:21:22* by *dom_e_uk*

Bar (or other programmer types),

One last Idea (clearly I can realise you have a lot on and this is just polish).  Is there any scope to have controls that run from the Ground Control Software to GPIO pins on the Control Board? If that is either on the Pi or your board?  I think it'd be really cool to add 2(maybe more if anyone can think of any) outputs to drive relays.  These could be for the router itself and a hoover.  

Is essence everything could then be controlled from the software and you could almost schedule the router and hoover to start and stop at the beginning/end of the tool path.

Clearly, I would have manual switches in place to isolate both in case of emergency or accessing the router (to change bits etc), Just seems like a more streamlined idea (although I'm open to criticism/moaning) :-)

Dom

---

Posted on *2016-12-29 04:45:15* by *TheRiflesSpiral*

Bar has mentioned that there will be user-configurable outputs on the Maslow control board for exactly this type of thing. (relays for router/dust collector control) 

I don't think Bar plans to actually write that code, as far as I'm aware but I'm sure the community will come through within hours of the first beta unit having been received. :D

Remember that the entire project is open source, including the Ground Control software so if you're interested in using the GPIO on the Pi instead, that's do-able by adding the necessary references to the code and the necessary logic as well.

---

Posted on *2016-12-29 04:48:09* by *TheRiflesSpiral*

Dom, I'm planning to work the Pi stuff out today/tomorrow. I'll start a new thread in dev and we can work it out.

---

Posted on *2016-12-29 05:24:36* by *dom_e_uk*

Mega....... 

More than happy with building/wiring etc!  Programming stumps me a bit though ;-)

---

Posted on *2016-12-29 06:04:21* by *TomTheWhittler*

I have been using a Raspberry Pi 3 (Ethernet & Wifi built in) along with a Protoneer CNCHat (http://wiki.protoneer.co.nz/Raspberry_Pi_CNC) to run a small WhittleCNC machine. The Pi 3 is only around $ 45.00 and would allow us to have a remote control of the Maslowcnc. The combo that I have works great and the developer of the CNChat (Bertus Kruger) has a done a lot of great work both software and hardware for the CNChat. He has a pretty active forum (http://forum.protoneer.co.nz/index.php).  I believe that Bertus has even supported this campaign so Bar may want to chat with him directly.

---

Posted on *2016-12-29 19:01:34* by *Bar*

It sounds like the Pi 3 is the one most people are looking at and the idea of having wifi and bluetooth built in is amazing. I've got one of those on the way. I'm pretty swamped so it might be a little bit before I get a chance to play with it but it'll be sitting on my desk taunting me.

The suggestions for IO pins to be available on the control board is a really good one. Someone suggested that a couple weeks ago, and I've added 6 aux outputs to the main control board. Each output uses a standard .1 spacing connector and provides +5 volts, GND, and a GPIO pin. The newest version of the controller should get a shout out in the update this week, so expect some pictures and details then.

---

