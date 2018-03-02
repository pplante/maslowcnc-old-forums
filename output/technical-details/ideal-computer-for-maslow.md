## Ideal computer for Maslow?
Posted on **2016-10-21 13:16:25** by **TheRiflesSpiral**:

We're primarily Chromebook users at home; I have a Macbook Pro as my primary but it's not allowed in the shop...

Are there open source or web-based tools to do what is necessary to make a vector file into a "cutter" file? (I'm a total CNC newbie, can you tell?) And what is the interface between the Maslow controller and the computer? USB? Supported by ChromeOS?

Thanks!

---

Posted on **2016-10-24 08:06:06** by **matthewrr**:

Would a Raspberry Pi 3 handle it?

---

Posted on **2016-10-24 10:14:33** by **Bar**:

Having a dedicated computer in the shop is awesome. I bought the cheapest windows 10 tablet I could find (this one: https://www.amazon.com/Hi8-Windows-Android-Features-19201200/dp/B01AN6BBKI/ref=sr_1_3?s=pc&ie=UTF8&qid=1477328674&sr=1-3&keywords=windows+10+tablet) and used Velcro attach it to my machine. One flaw: that tablet has only one USB port which is both for charging and connecting which is a pretty poor design choice in my opinion. 

I design things on my regular computer and then save them into a dropbox folder, then out in the garage I just turn on the machine and the files are ready to cut. Our software supports multi-touch which is nice, so the tablet basically is a touch interface to the machine. 

The software is written in python specifically to make it easy to run on everything. A raspberry pi will handle it great. I haven't got any experience with ChromeOS, but after a little googling it looks like you can run python code on ChromeOS so it should be possible (but maybe a little bit of a hassle)

---

Posted on **2016-10-24 10:16:13** by **Bar**:

Oh, and web based tools! Yes. 

My favorites are: 

www.makercam.com which is simple and no frills, but works great.

http://jscut.org/ which is a little fancier.

There are probably some other cool ones out there so if anyone else knows of some, let me know!

---

Posted on **2016-10-24 10:17:13** by **Bar**:

Oh, also http://easel.inventables.com/users/sign_in you have to make an account and it's really only intended for users of their machines, but it will work great on any machine

---

Posted on **2016-10-25 16:45:45** by **TheRiflesSpiral**:

I missed the Linux mention... my Chromebook will dual-boot to Ubuntu so I'm good. Thanks for the feedback, Bar!

---

Posted on **2016-11-11 14:29:52** by **lthomas987**:

I use OctoPrint to controll my 3d Printer running on a Raspberry Pi, since once the GCODE is generated all you need is a machine to push it to the arduino.  I'm contemplating trying that for Maslow as well.

---

Posted on **2016-11-11 14:53:01** by **TheRiflesSpiral**:

I've got a couple of older android tablets I've been wanting to do something with... maybe I'll put a Linux distro on one and make a touchscreen controller for Maslow. One is that Polaroid made-for-kids thing; it practically indestructible. Perfect for a shop!

---

Posted on **2016-11-11 14:59:46** by **TomTheWhittler**:

Maybe Bar could team up with Bertus Kruger (maker of the Raspberry Pi CNC hat board , http://wiki.protoneer.co.nz/Raspberry_Pi_CNC) to make a custom Raspberry Pi Maslow hat to control Maslow.

---

Posted on **2016-11-11 19:01:57** by **karlthorp**:

I'm planning on installing a CHIP on my Maslow that I can connect to remotely with my pocketCHIP, this way I can have it closed off except for a filtered vent without risking damage to a computer.

for more information on CHIP and pocketCHIP check out www.getchip.com no I don't work for them, I was just one of their backers on Kickstarter

---

Posted on **2016-11-11 20:26:01** by **Bar**:

That little computer looks fantastic! $9! What a deal.

---

Posted on **2016-11-12 11:53:20** by **laird**:

I am also a Chip backer, and I think that using a PocketCHIP as a controller is a great idea. That's a Chip plus a display, keyboard, WiFi. Battary powered, though of course in this case you'd leave it plugged in (it's in a shop...). Brilliant idea, Karl!

---

Posted on **2016-11-12 20:02:25** by **lthomas987**:

Fantastic idea. I hadn't thought of using a CHIP!  I have one of those too.

---

Posted on **2016-11-13 07:01:18** by **chadzimmerman**:

That Chip does look interesting.  I was thinking of using a Pi setup.  May have to rethink now.

---

Posted on **2016-11-15 05:45:50** by **TheRiflesSpiral**:

That pocket Chip thing is like nerd heaven... I must have one.

---

