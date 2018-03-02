## One motor turning the wrong way during chain calibration
Posted on **2017-06-20 03:50:48** by **thomasgkristensen**:

Hi all!



It was finally time for me to run the chain length calibration but alas! When I tried adjusting the sprocket I noticed that the left motor what turning when I pressed the right button and the other way around.



I swapped the cable and got the left motor to calibrate the chain just fine. Success! The right motor however started turning CW instead of CCW, dropping the chain on the floor.



I've checked and double checked that the motors are pointing the same way as on the pictures for the temporary sled and everything seems to look fine. The cables seem to turn the right way as well.



I'm running 0.76 of both firmware and ground control.



Has anyone seen similar issues or have any ideas as to what I might have done wrong?

---

Posted on **2017-06-20 04:15:35** by **gero**:

Hello, do you have the motors connected this way?  [IMAG0875](//muut.com/u/maslowcnc/s1/:maslowcnc:PrmW:imag0875.jpg.jpg)

Are you using the firmware and groudcontrol from the releases or from the green download button?

---

Posted on **2017-06-20 04:32:22** by **thomasgkristensen**:

I've tried that way and swapping L and R. It's really good to have confirmed that the leftmost port on your picture is R. Thanks! I really couldn't figure that out.



I've downloaded the firmware and groundcontrol from the releases page. I don't know of any green buttons?

---

Posted on **2017-06-20 04:32:31** by **thomasgkristensen**:

And thanks! Of course!

---

Posted on **2017-06-20 05:22:31** by **thomasgkristensen**:

I tried downgrading the firmware to 0.73 and the groundcontrol version to 0.75 but now I can't get any life in the motors. Maybe the software is just in a bit of a flux?

---

Posted on **2017-06-20 05:23:05** by **thomasgkristensen**:

I can tell that groundcontrol connects to the machine though as I get the version of the firmware echoed back.

---

Posted on **2017-06-20 05:54:42** by **rancher**:

I'm pretty sure it's broken right now.  I think we need to wait for updates or something.

---

Posted on **2017-06-20 09:27:14** by **Bar**:

What happens when you press the "test motors" button?

---

Posted on **2017-06-20 11:15:27** by **thomasgkristensen**:

The left motor turns correctly back and forth, but the right motor turns the opposite direction on its test run (which I believe is wrong).

---

Posted on **2017-06-22 11:10:54** by **thomasgkristensen**:

I am no longer able to run the test routine. I just get a fail on all three motors now. The port it identifies also seems to have changed from /dev/cu.usbmodem1411 to /dev/tty.usbmodem1411 which is really confusing. I can still see the firmware version and I have successfully updated to 0.77 for both firmware and groundcontrol.



I'm not sure how to troubleshoot from here. I fear I might have damaged a circuit board or the motors but I'm unsure how to figure out where it's failing.

---

Posted on **2017-06-22 11:44:52** by **gero**:

On what Operating System are you running Ground Control?

---

Posted on **2017-06-22 12:14:09** by **gero**:

Looks like Mac.

---

Posted on **2017-06-22 12:22:13** by **gero**:

Tip 1) (forgive me)

Check if the power supply for the motors is in the shield and not in the Mega.

2) Open the Adrduino IDE and check the serial monitor, if it gives hyroglyphs change baud rate to 57000. You should see something like this -->[PE:0.00,-0.01,255]

<Idle,MPos:-0.24,-463.57,3.00,WPos:0.000,0.000,0.000>

<--

3) check what port the IDE conected to and close the IDE

4)Open GC and check the port, if not the same try changing in settings.

---

Posted on **2017-06-22 12:35:49** by **Bar**:

+1 for everything @gero says those are exactly the right steps to try. Let us know how it goes!

---

Posted on **2017-06-22 12:36:42** by **thomasgkristensen**:

Thanks @gero! I'm ashamed to admit that Tip 1 was correct! I'd completely forgotten there was a power port on the arduino :-(



You're right, it is a mac.



Thanks once again! You can't image how silly I feel right now.

---

Posted on **2017-06-22 12:37:17** by **gero**:

We have all been there.... we all admit :-)

---

Posted on **2017-06-22 12:38:53** by **Bar**:

We've all been there. You aren't even the first this week. Bonus points to @gero for diagnosing the issue correctly on his first point!



The new PCBs we're going to be shipping you guys have one LED which indicates that the 12 volt supply is connected, and one to indicate that the USB is connected, so hopefully soon it will be easier to catch that issue :-)

---

Posted on **2017-06-22 12:52:31** by **thomasgkristensen**:

Haha! Good idea! I can confirm that both motors now turn the direction they are supposed to! Happy days :-)



Unfortunately it has now become apparent that the chain measured out is for the full size setup. I'm trying out a smaller version (I can't fit big pieces of plywood in my car) and I just assumed the chain would be measured out to the smaller dimensions I put in the settings.



I don't know if support for smaller versions of the machine is on the schedule or if I need to figure out how to get a bigger piece of plywood and find some place to put it :-D

---

Posted on **2017-06-22 13:48:35** by **Bar**:

Great point! I hadn't thought of that. Are your chains of shorter length or can you measure out the full length, then backtrack?

---

Posted on **2017-06-22 14:06:15** by **davidlang**:

when feeding out the chain, instead of feeding out a fixed amount, do the chain length calculation to find what they should be for '0,0'

---

Posted on **2017-06-22 23:27:24** by **thomasgkristensen**:

@bar I haven't shortened the chains so I could backtrace. Is that possible in the current implementation?



@davidlang so are you suggesting doing the maths to find the center by hand and then measuring out and putting the chains on the spokes correctly? Sounds like that should work as long as the rest of the gcode interpretation doesn't assume anything about the chain lengths.

---

Posted on **2017-06-30 11:27:12** by **thomasgkristensen**:

I have been experimenting with manually unhooking the chain and positioning the sled in the middle of my smaller plywood setup. After putting the sled in the middle of the plywood I then use the manual chain length calibration but I can see it assumes my chains are much longer than they actually are. When I then try to move around the sled is moved much further then the 4 inches I've asked it to move. It also seems to go up even when I press down.



I assume this is all caused by the control software resetting 0, 0 to the wrong chain lengths. Am I not doing this the right way?

---

Posted on **2017-06-30 13:12:33** by **Bar**:

I'm sorry about the slow response on this one. Making the machine work at any size IS on my todo list. I've been pretty much swamped this week with getting the kits out, and the next few weeks will probably be pretty hectic too as I try to help everyone get their machines put together. I haven't forgotten about you.



Yeah, you are going to see a lot of strange behavior when the machine thinks the chains are different lengths.



The first thing I would try would be to run the chain calibration without the chains actually on the motors. The cross hairs will probably then indicate that the sled is somewhere off the bottom of the sheet (where it would be if the chains were attached). 



With the chains still not on the motors use the arrow keys to move the cross hairs until they indicate that the sled is in the center of the sheet. Then put the chains on the motors so that the sled is actually in the center of the sheet. The actual chain lengths will now agree with the real location of the sled.



I haven't actually tested this because I don't have a smaller machine built, so l et me know how it goes. Pictures and screen shots are very helpful if it doesn't work to better understand what's going on.

---

Posted on **2017-07-01 11:00:47** by **thomasgkristensen**:

No problem at all! I understand that supporting the happy path for setting this up is much more important than my very special case :-D



I will try out the detailed suggestion. Thanks!

---

