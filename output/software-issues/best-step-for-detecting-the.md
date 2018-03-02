## Best step for detecting the maslow port on Linux?
Posted on **2017-05-31 12:18:37** by **mikeberg**:

I have fresh installed Ubuntu Linux and all it components to run ground control now I'm unable to connect my port and make some motor test

---

Posted on **2017-05-31 12:19:49** by **Bar**:

That is great news! 

The port should be the same as in the Arduino IDE. Does that help?

---

Posted on **2017-05-31 12:22:29** by **mikeberg**:

When I plug USB cable these two motor turn half of a turn and stop I supose it's normal

---

Posted on **2017-05-31 12:27:30** by **Bar**:

That used to be normal, but I think in the latest firmware I made is so they wouldn't move when powered up. Are you using the latest firmware?

---

Posted on **2017-05-31 12:27:30** by **gero**:

Are you comfortable with the putting commands in a terminal? A ls /dev before and after plugging in the arduino will show a difference

---

Posted on **2017-05-31 12:46:16** by **gero**:

Took some time to fire mine up. It connects to /dev/ttyACM0 on my kubuntu.

---

Posted on **2017-05-31 17:23:40** by **mikeberg**:

What I made for now to detect which port is open on my computer I opened arduino ide and a list of Port is displayed in real time. I guess my port for maslow is maybe the same of you gero it name is very similar

---

Posted on **2017-05-31 17:25:29** by **mikeberg**:

What was your steps to make it run maslow gero?

---

Posted on **2017-06-01 09:12:04** by **gero**:

Python should be present on your system. You can check the version with 'python -V' in a terminal. It should not be 3, I think, mine is 2.7.something. I needed to install pip. The rest I followed from here: https://github.com/MaslowCNC/GroundControl/wiki/Linux

---

