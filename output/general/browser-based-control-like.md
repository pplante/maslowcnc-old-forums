## Browser based control like Octoprint?
Posted on **2017-03-23 12:07:48** by **noexit**:

On my home built 3D printer, I quickly abandoned connecting it directly to my PC, and started using a Raspberry Pi with Octoprint to control my printer. Are there any plans for something like this?

---

Posted on **2017-03-23 12:55:17** by **davidlang**:

well, you can already control it from a pi or android device, and with a pi you can remote the display to another computer with the X11 protocol (aka XWindows)

it seems that all the control software does is to do a little setup and then feed the g-code to the arduino, so it would be pretty easy to make a web enabled version of it.

That said, I'd be a bit surprised if bar had this directly, it's a fair amount of work and his time is probably better spent improving the machine and it's firmware.

---

Posted on **2017-03-23 14:57:30** by **TomTheWhittler**:

Bar already has ground control working on a Raspberry PI 3 complete with keyboard and mouse.
I just can not find the discussion thread where he wrote that.
As Davidlang pointed out it should be pretty easy to make a web enabled version of it since the Raspberry Pi 3 has wifi built in.

---

Posted on **2017-03-23 15:01:37** by **TomTheWhittler**:

Is was in the thread "Raspberry Pi 3 setup for Ground Control"

---

