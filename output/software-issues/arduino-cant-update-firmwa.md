## Arduino can't update firmware to .76
Posted on **2017-06-21 09:06:45** by **Jennifer D**:

Hi all,

After a few months of life keeping me from working on my maslow I'm determined to finally get my frame done and get it up and running! 



I'm running Sierra 10.12.4 on a MacBook Pro and was able to get things running well enough back in March to cut out an oblong sled. Knowing I was months out of date the first thing I did was update ground control and am now attempting to update the firmware. 



When I try to upload I get the following errors:



Sketch uses 37918 bytes (14%) of program storage space. Maximum is 253952 bytes.

Global variables use 2987 bytes (36%) of dynamic memory, leaving 5205 bytes for local variables. Maximum is 8192 bytes.

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_ReceiveMessage(): timeout

avrdude: stk500v2_getsync(): timeout communicating with programmer

An error occurred while uploading the sketch



I am showing a connection to the board - Arduino will  retrieve the board specs. I am concerned there's something more serious wrong as the motors don't hum at all when I plug in the power supply. All cords are plugged in, no damaged cords. 



Any ideas?



Thanks! 



~Jennifer

---

Posted on **2017-06-21 09:23:01** by **Bar**:

Welcome back! We've missed you!



I've seen that issue when ground control is open at the same time as the Arduino program. Is there any chance that Ground Control could be holding onto the port?

---

Posted on **2017-06-21 10:16:59** by **Jennifer D**:

Hi Bar, thanks! It's nice to be able to dive back into the fray :) 



Looks like it might be my usb extension cable - I unplugged everything and connected it to my laptop via the short cable and was able to upload the firmware. Very weird considering the cable worked just fine two months ago! Digging around for a spare now to see if I can get ground control to talk to it - right now it will connect, but I get "fail" on testing the motors.

---

Posted on **2017-06-21 10:27:00** by **Jennifer D**:

Apparently I took a hint from some discussion about usb extension cords being unreliable and bought a long printer cable before I had to shelve the Maslow setup back in March.



Ground Control is recognizing the board now but I'm still getting fail errors when I try to test the motors - all three are failing. I did a power cycle on the board and motors, nothing doing though.

---

Posted on **2017-06-21 10:27:36** by **Bar**:

Also, 0.76 turned out to be a bit of a dog, it might be worth just installing 0.77 available on GitHub now, to be 'released' officially in a couple hours once I know what is causing the issue @rancher is seeing and it's been fixed

---

Posted on **2017-06-21 10:30:59** by **Jennifer D**:

Will try that right now.

---

Posted on **2017-06-21 10:31:04** by **Bar**:

Those long USB extenders can be dodgy if there is a lot of RF around, maybe it's a new environment thing?



Do all three motors fail, or just one? If it's all three, I would check the 12 volt supply first and see that they are getting power

---

Posted on **2017-06-21 10:51:35** by **davidlang**:

seethe comments under 'calibration issues' about the version of pyserial

---

Posted on **2017-06-21 11:35:37** by **Jennifer D**:

*facepalm* I'm going to put a piece of tape over the second power socket on the arduino board - this is not the first time I plugged in the wrong one! 



Ok, so I have firmware updated to .77, but not Ground Control, as I'm installing on a mac and am not yet savvy enough to be able to install GC without the disk image.  Will update that later! 



Let's see how far I make it now!

---

Posted on **2017-06-21 11:38:41** by **mfpiechowski**:

"avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2ReceiveMessage(): timeout

avrdude: stk500v2_getsync(): timeout communicating with programmer

An error occurred while uploading the sketch"



I've experienced this timeout error last night (not with my Maslow, that hasn't shipped yet). In my case, I am trying to flash a MegaPi Hat from Protoneer using a Raspberry Pi 3. If I can get GroundControl and the MegaPi Hat to play nicely together on the Pi3, this is how I will run my Maslow. I'm not quite there yet, but getting closer. 

 

Anyhow, it seems that pressing and releasing the reset button on the Arduino can sometimes get the board to accept a flash if you're seeing the timeout error. Timing is everything, but it really does work. I learned this from a really bad youtube video the other  night. Didn't believe it, but tried it and it worked. I don;t know the reason why, but I can vouch for the fact that it works.

---

Posted on **2017-06-21 11:46:08** by **Bar**:

@Jennifer it's not just you, I've been there too :-)



We've added a 12 volt power indicator LED to the new boards (if they ever actually get them to us) so hopefully soon you'll have a board that will tell you if it's plugged in or not

---

Posted on **2017-06-21 12:08:26** by **Jennifer D**:

I'm holding on for the .77 GC but wanted to see if things would move and so forth so I tried to run through the calibration sequence(even knowing it's broken at the moment). 



Odd z-axis behavior - the z axis is reversing the motions - it's lower the bit into the wood when it should be raising it and vice versa. Have you had reports of that sort of behavior, Bar?

---

Posted on **2017-06-21 12:47:54** by **Bar**:

I have not seen that behavior, very strange. There is an option to reverse the direction in the settings if you make the zaxis pitch negative, but I know you are using the same router as me so I wouldn't expect that to be the issue. 



When you run the "test motors" function do all motors pass?

---

Posted on **2017-06-21 13:04:42** by **Jennifer D**:

Yep. all motors pass, and when I adjusted the z-axis to zero it moved up and down as expected. Very odd behavior! If it continues to do that when I install GC .77 I'll try adjusting the pitch. Just doesn't make sense that it would be backwards during the test cut but not during the zeroing process. Leave it to me to find weird things going on!

---

Posted on **2017-06-21 13:34:33** by **Bar**:

Yeah, that's real strange let's keep an eye on it!

---

Posted on **2017-06-21 16:02:00** by **Bar**:

@rancher reported similar strange z-axis behavior this week so it's not just you! I'm looking into it

---

Posted on **2017-06-23 05:55:00** by **Jennifer D**:

@bar Morning Bar, just wanted to let you know I'm seeing the same reversed z axis behavior in .77 as in .76. I've disabled z-axis for the calibration part of things.

---

Posted on **2017-06-23 10:48:57** by **Bar**:

Very strange! Thanks for the heads up!

---

