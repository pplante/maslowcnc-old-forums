## Grbl USB to serial transmission errors
Posted on **2017-02-16 01:05:44** by **jbnimble**:

Reading the [known issues](https://github.com/gnea/grbl/wiki/Known-Issues#usb-to-serial-transmission-errors) on the grbl wiki, and saw this usb error and solution. This may be applicable to Maslow as well?



@Bar, which mega board and revision is Maslow using? [Original](https://www.arduino.cc/en/Main/ArduinoBoardMega) or [2560](https://www.arduino.cc/en/Main/arduinoBoardMega2560) with which revision?

---

Posted on **2017-02-16 10:00:39** by **Bar**:

We're using a Mega 2560 R3 compatible board with the the Atmel 16U2 USB chip. The fact that they experience better performance at higher baud rates is interesting. We're running at 19200 right now because I've found it's easier to get the usb serial drivers to play nice across multiple platforms at lower speeds, but I think we probably want to bump that up as soon as we've got all the versions of win/linux/mac playing nice at 19200. 



I haven't seen any dropped data, but that doesn't mean it isn't happening and I'm just not noticing. It's definitely a thing to keep an eye on.

---

Posted on **2017-02-16 10:17:41** by **jbnimble**:

Better to learn from others problems.



Slightly off topic, I doubt it is possible at this point for our arduini api to be grbl api compatible, but if it were in the future then maslow could have a lot more options on control UIs like linuc cnc and others. I especially like the grbl feature of look ahead to adjust speed on cornering, I think I saw a thread here where it was discussed.

---

Posted on **2017-02-17 09:33:21** by **Bar**:

I don't think it should be too hard to make the interface compatible. I want to make sure it's working as is for everyone first, but if you filed a feature request for that on GitHub I don't see any reason we couldn't work towards that. 



As far as look-ahead I think that's a great idea. Also probably worth filing a feature request for it.



(Feature requests are just issues with the tag "enhancement" as far as I can tell, you can file them here: https://github.com/MaslowCNC/Firmware/issues)

---

