## wireless connectivity
Posted on **2017-03-01 14:25:32** by **jbarchuk**:

Several Qs really, all related, trying to understand how the system is intended to operate.

The most basic Q is how 'smart' is the board that operates Maslow?

Can I plug a wireless USB network adapter into it that talks with my main computer? (Via Uverse modem/router)

How much 'operation' of the Maslow can I do right at the machine itself not via the PC?

Best case, can I tell the controller board to 'go get this file and run it'? Obviously the controller board would need permissions, file sharing of some sort that I know 100%-nothing about, but if it's doable I'll figure it out.

IF NOT, THEN....

I'm not too discouraged. I have an Very Old Dog PC given by a friend with limited memory and HD space but probably good enough to work. I have spare wireless routers that I can figure out how to give my main router permission to talk to the net -and- talk to the main 'design' PC.

---

Posted on **2017-03-01 15:39:06** by **scottsm**:

There is an Arduino Mega clone running the motors which is willing to communicate serial either over USB or 5volt I/O for the gcode commands. I've gathered parts to try a serial-over-Ethernet connection with the PC remote, away from the sawdust. I'm pessimistic though, that sort of connection has delays and lapses which could spoil a session. Sounds like Bar and Hannah might have experienced something like that running a music program during a cutting session. 

 Your Very Old Dog PC sounds like a good candidate to talk to the Mega. I know that a Raspberry Pi has the horsepower to work, a PC running a simple Linux seems likely to work as well.

 Bar has talked about using an inexpensive Windows tablet. He described just the remote file transfer you mentioned, sending the gcode file from his desktop where he did the design to the tablet which uses it to control the cuts. Lots of options!

---

