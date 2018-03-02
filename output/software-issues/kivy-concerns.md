## Kivy Concerns
Posted on *2017-06-04 11:22:10* by *matthewrr*

Hey folks,

Getting some issues trying to get Ground Control updated and humming happily with Kivy.  Here's the terminal output from Linux Mint.

 sudo /home/makerstation/Downloads/GroundControl-master/main.py
/home/makerstation/Downloads/GroundControl-master/main.py: 5: /home/makerstation/Downloads/GroundControl-master/main.py: 

Kivy Imports

: not found
from: can't read /var/mail/kivy.config
/home/makerstation/Downloads/GroundControl-master/main.py: 7: /home/makerstation/Downloads/GroundControl-master/main.py: Syntax error: word unexpected (expecting ")")

Any suggestions?

Also, I'd kill for an auto-update on Ground Control. 

Thanks,
Matthew

---

Posted on *2017-06-04 12:40:44* by *matthewrr*

I've tried several things and one of them got me an open GroundControl. So good there.

---

Posted on *2017-06-04 13:00:57* by *matthewrr*

Now it'll show connected but I can't get anything to move at all. No calibrate, no arrow buttons, nothing.

---

Posted on *2017-06-04 13:11:18* by *matthewrr*

So, the issue is that the test for motors/encoders and the automatic chain length calibration don't have anything popping up. Any suggestions on why I get no response on those two features.

---

Posted on *2017-06-04 14:12:49* by *scottsm*

Have you made the serial connection?

---

Posted on *2017-06-04 16:09:51* by *matthewrr*

Says connected. For some reason, the COM port doesn't change name depending on the individual usb port. Still reads connected. Doesn't change name in arduino software either.

---

Posted on *2017-06-04 17:31:07* by *scottsm*

On my setup, the Arduino shows up as /dev/ttyACM0   that's a zero...b Is that the port you're using?

---

Posted on *2017-06-05 04:59:26* by *matthewrr*

Sure is.

---

Posted on *2017-06-05 07:05:49* by *scottsm*

I recently set up a Ubuntu Linux machine for this, and I remember that after installing Arduino there was a further installation step that didn't trigger until I ran the Arduino program. Adding my user account to the 'dial out' group, I think. Also had to reboot to make it complete. I then uploaded the Blink sketch to see that I had a proper connection, and finally uploaded the Maslow firmware.

---

Posted on *2017-06-05 08:24:44* by *matthewrr*

Well, my firmware seems to have updated successfully.  I think the issue is relating to kivy and the config files it needs.  I think I'll just have to wipe everything and try the full install all over again.

---

Posted on *2017-06-05 08:34:04* by *gero*

Hi @matthewrr, I have GC running on 2 linux, I have uploaded the output of terminal command from both here: https://www.dropbox.com/s/17l4ev7sev618ci/maslow-linux-specs.xls?dl=0

---

Posted on *2017-06-05 08:34:31* by *gero*

perhaps if you share the output on your system it could help

---

Posted on *2017-06-05 08:45:00* by *matthewrr*

Hey, all of that you posted shows in terminal when I fire up GC. Unfortunately, I get no feedback in terminal for any of the GC buttons pressed. I'll try to get it to speak to me later today.

---

Posted on *2017-06-05 08:54:24* by *gero*

GC should display this:
Connected on port /dev/ttyACM0
Sending: B03 A2444 C1222 Q3005.8 E480.61 F304.8 R155 H52 I1 J8148.0 K10 M6.35 N2.3 P7560.0   
Sending: B05
Changing the port in >>Actions>>Port should display:
update ports
/dev/ttyACM0

---

Posted on *2017-06-05 09:07:11* by *gero*

Please forgive for this shot in the dark, but it happened to a few including myself. The power is connected to the motor shield and NOT to the Mega?

---

