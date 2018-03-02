## Connection Timeout
Posted on **2017-07-11 12:58:07** by **charleswiltgen**:

I'm probably missing something simple here but any help would be great.  We have scratch built a Maslow at the maker space I go to and we keep getting "Connection Timeout".  We are using GC.79 and firmware .79 on a Windows 7 computer.  I can flash the Mega just fine and when I fire up GC I get a connection but after when I try to move the head it moves about an inch and then times out.  Has anyone had this problem.  Any input would be great.

---

Posted on **2017-07-11 13:17:29** by **gero**:

Hi, not sure I can help, but will try:
1) After you flashed the Mega, is the Aruino IDE closed?
2) What is the com port used by the IDE to flash? Is that port set in CG?
ok, forget 2). Just read again and saw it moves

---

Posted on **2017-07-11 13:27:49** by **charleswiltgen**:

I get the timeout even if Arduino is closed.  I have also tried two different mega's

---

Posted on **2017-07-11 13:32:48** by **scottsm**:

Are you able to try the ‘Actions/Test motors ‘ button? What does that do?

---

Posted on **2017-07-11 13:42:47** by **gero**:

Perhaps determine if the connection only drops in GC. The is a test .ino that just runs the motors left and right, in the firmware folder under test_electonics_firmware. Alternatively open the serial monitor in the Arduino and monitor that for a while to see if there is a drop of connection as well.

---

Posted on **2017-07-11 13:49:05** by **gero**:

Does it ever reconnect after the timeout in GC?
Is a gcode file loaded?

---

Posted on **2017-07-11 14:06:23** by **charleswiltgen**:

No gcode file loaded.  It alternates between connected and timeout.

---

Posted on **2017-07-11 14:14:53** by **gero**:

That sounds familiar. Where are the windo$ geeks? Was python newly installed on the system or was it already present?

---

Posted on **2017-07-11 14:24:43** by **charleswiltgen**:

The Test Motors starts and timesout

---

Posted on **2017-07-11 14:25:47** by **gero**:

That is the Test Motors in GC, right?

---

Posted on **2017-07-11 14:27:05** by **charleswiltgen**:

Test motors in GC Yes

---

Posted on **2017-07-11 14:30:14** by **gero**:

It is a shot in the dark that you might have the right version of python, but an outdated version of the pyserial modul. Don't be intimidated by this phrases. We had that issue that caused a time out, so I just want to exclude, that it is the same on your side. I have no windows to test how you can get the version of your python and the pyserial, so I'm a bit stuck here.

---

Posted on **2017-07-11 14:42:48** by **gero**:

If you are confident to open a command prompt and type... try
python --version

---

Posted on **2017-07-11 14:44:08** by **gero**:

try also
pip show pyserial

---

Posted on **2017-07-11 15:16:44** by **gero**:

Have a nice day @charleswiltgen. It is Tuesday 3PM in Portland and Wednesday 1AM in Bahrain, so I will have a good sleep. Once the Maslowians come from work, there will be a great support.
Just to make my points clear:
Python needs to be Version 2. It shows as 2.xx.xx. In my case Python 2.7.12. Do not use Python 3, as it will not work.
The module Pyserial 2.6 is proven to cause timeouts. In my case replacing only that module to Pyserial 3.3 solved the issue.
On your side it could be something else, like a defct USB cable. That can be excluded with a stopwatch and measuring the time between the connection drop and the reconnection. If they are consistent, it is not the cable. :-) See you soon.

---

Posted on **2017-07-11 16:45:53** by **scottsm**:

I get this behavior when my Mega doesn't have the firmware. GC posts that error if it can connect to the serial port chosen but does not receive a valid reply to messages sent.
 Here's a test to verify that the firmware is indeed programmed without iusing GC: In Arduino, open the Serial Monitor and set the speed to 57600. You should see many lines flying by like:
[PE:-0.01,-0.01,255]
<Idle,MPos:-37.66,27.16,0.00,WPos:0.000,0.000,0.000>
[PE:-0.01,-0.01,255]
<Idle,MPos:-37.66,27.16,0.00,WPos:0.000,0.000,0.000>

If you send the string B05 - that's B zero 5 - using that tool, within the stream the Mega should respond:
B05
Firmware Version 0.79
ok

If your Mega answers this way, all is correctly programmed and the python/pyserial troubleshooting path would be the one to follow.

---

Posted on **2017-07-12 10:31:16** by **charleswiltgen**:

serial connection in the Arduino IDE is good.  I tried running Ground control from the source following the instruction but i get an error when running main.py

---

Posted on **2017-07-12 10:47:40** by **charleswiltgen**:

so when I try to follow install from source instructions I get this... [Capture](//muut.com/u/maslowcnc/s1/:maslowcnc:SYD4:capture.png.jpg).  Is there something I am doing wrong?

---

Posted on **2017-07-12 11:05:39** by **TheRiflesSpiral**:

Check your UIElements folder and see if FrontPage.py is present... it appears from your screencap that it's either missing or corrupt.

---

Posted on **2017-07-12 12:16:53** by **charleswiltgen**:

I do not see FrontPage.py file anywhere on my computer.  Was this part of the GC download or the Python

---

Posted on **2017-07-12 12:27:01** by **charleswiltgen**:

Ok I was able to final get this to run GC from the source.  I have verified I have Python 2.7.13 and Pyserial 3.3.  I am still get the connection timeout.  Again, I have verified the firmware is loaded using the Arduino Serial Monitor and Sending a B05 command.  Our Board and Mega work on my Windows 10 machine but we cannot get this work on a Windows 7 machine we are trying to dedicate to the Maslow.  Please any suggestions would help.

---

Posted on **2017-07-12 12:41:05** by **Bar**:

Hmm, I remember there being some special issues with the Arduino drivers on windows 7. That's where I would look first. The connection timeout issue means that Ground Control is able to open a connection, but then never gets a response from the machine.

The other thing I would check is to make sure Ground Control is connecting on the correct port. I know on my computer for some reason COM1 is always listed as an available connection, even when nothing is plugged in and when I try to connect to it I see the connected...connection timed out behavior

---

Posted on **2017-07-12 12:57:27** by **charleswiltgen**:

I can flash the mega no problem from the computer.  When i start GC it does read the firmware version and location from the Mega.

---

Posted on **2017-07-12 13:42:56** by **Bar**:

Hmmm, that sounds like the right COM port then

---

