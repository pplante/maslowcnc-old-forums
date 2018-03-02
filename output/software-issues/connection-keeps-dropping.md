## Connection keeps dropping
Posted on **2017-06-09 06:22:32** by **gero**:

With the Firmware and GC from Wednesday GC alters between 'Connected' and 'connection lost' ~ every second. The terminal does not give much info. It's sending commands in between:

Connected on port /dev/ttyACM0



Sending: B03 A2444 C1222 Q2998.08 E481.93 F158.75 R75 H-1 I1 J8148.0 K10 M6.35 N2.3 P7560.0   



Sent Space available: 170

connection lost

Connected on port /dev/ttyACM0

Sending: B05   

Sent Space available: 249

connection lost

Connected on port /dev/ttyACM0

Sending: G21



A older GC (29/04) stayed connected

---

Posted on **2017-06-09 06:30:04** by **gero**:

The Serial Monitor in the Aruino IDE stays connected and prints its lines nicely.

---

Posted on **2017-06-09 07:41:08** by **scottsm**:

I’ve had this happen if I had Arduino open when starting up GC.

---

Posted on **2017-06-09 07:45:01** by **gero**:

Restarted Pc, but still. Confirmed that with last weeks GC and this weeks firmware it stays connected.

---

Posted on **2017-06-09 07:51:26** by **scottsm**:

The baud rate in GC is set in Connections/serialPortThread.py, search for 57600. Is that correct in the new version?

---

Posted on **2017-06-09 08:09:50** by **scottsm**:

I just downloaded the [source for V75](https://github.com/MaslowCNC/GroundControl/archive/v0.75.zip) using the link on the releases page with Ubuntu17.4 and it is running OK. This new version shows the GC version as well as the Firmware version when the connection is stable. Is there anything I can check here to help find the issue?

---

Posted on **2017-06-09 08:28:04** by **gero**:

Downloaded the master the third time. The connection loss is gone :-o

57600 confirmed in serialPortThread.py

Whatever it was, it is gone... If it stays away, OK. Thanks for the support

---

Posted on **2017-06-09 09:27:51** by **scottsm**:

Happy to help, i’ve See now you do as much and more for others :)

---

Posted on **2017-06-09 09:29:56** by **TheRiflesSpiral**:

Hmmm... Does GitHub have any provisions for providing checksums for downloads? It sounds to me like there was some integrity issue on your previous attempts.

---

Posted on **2017-06-09 09:30:36** by **TheRiflesSpiral**:

If so, you could at least verify you got all the 1's and 0's lined up from the start... avoiding the whole garbage in garbage out thing. :)

---

Posted on **2017-06-09 10:31:35** by **gero**:

Its getting more crazy, squares are random art now....

---

Posted on **2017-06-09 10:35:04** by **gero**:

Macro buttons are there, but no text or macro... Screen shows sled following the cut path and the cutter goes different directions :-). This will be fun to sort out, hahaha... perhaps i should try the download from the releases.

---

Posted on **2017-06-09 11:30:25** by **gero**:

Back to square one. Since I had a version of CG with no text on the Macro buttons; after 3 downloads suddenly a stable connection, but crazy moves; I downloaded the master of FW and GC I my office, placed them in my public folder and copied it in the workshop from there.

The Arduino gives warnings:

sketch/number.c: In function 'bc_str2num':

sketch/number.c:1523:7: warning: assignment discards 'const' qualifier from pointer target type

   ptr = str;

       ^

sketch/number.c:1548:7: warning: assignment discards 'const' qualifier from pointer target type

   ptr = str;

       ^

/home/ghadmin/Maslow/test/Firmware-master/cnc_ctrl_v1/cnc_ctrl_v1.ino: 15:0: warning: "SERIAL_RX_BUFFER_SIZE" redefined

 #define SERIAL_RX_BUFFER_SIZE 512

 ^

In file included from /home/ghadmin/arduino-1.8.2/hardware/arduino/avr/cores/arduino/Arduino .h:232:0,

                 from sketch/cnc_ctrl_v1.ino.cpp:1:

/home/ghadmin/arduino-1.8.2/hardware/arduino/avr/cores/arduino/Hardwar eSerial.h:53:0: note: this is the location of the previous definition

 #define SERIAL_RX_BUFFER_SIZE 64

 ^

/home/ghadmin/M aslow/test/Firmware-master/cnc_ctrl_v1/cnc_ctrl_v1.ino: 16:0: warning: "SERIAL_TX_BUFFER_SIZE" redefined

 #define SERIAL_TX_BUFFER_SIZE 512

 ^

In file included from /home/ghadmin/arduino-1.8.2/hardware/arduino/avr/cores/arduino/Arduino .h:232:0,

                 from sketch/cnc_ctrl_v1.ino.cpp:1:

/home/ghadmin/arduino-1.8.2/hardware/arduino/avr/cores/arduino/Hardwar eSerial.h:46:0: note: this is the location of the previous definition

 #define SERIAL_TX_BUFFER_SIZE 64

 ^

Sketch uses 36788 bytes (14%) of program storage space. Maximum is 253952 bytes.

Global variables use 2927 bytes (35%) of dynamic memory, leaving 5265 bytes for local variables. Maximum is 8192 bytes.



In GC I am back to the loop of connecting and loosing the connection.



Next I'll try from the releases.

---

Posted on **2017-06-09 11:37:28** by **gero**:

Same result with Firmware-0.73 GroundControl-0.75

---

Posted on **2017-06-09 11:46:33** by **gero**:

I can confirm again that with an other CG I have a stable connection and can move the sled around.

---

Posted on **2017-06-09 12:42:22** by **Bar**:

Hmmm, I just checked to make sure I'm not seeing the same behavior with the latest firmware/GC. I'm thinking it has something to do with the file being corrupted. I also am not getting the same warnings in Arduino. 



You are using the stock Arduino Mega that came in the kit, right?

---

Posted on **2017-06-09 12:58:20** by **gero**:

Yes nothing changed. And I can switch to an older GC and have connection. So the FW seems ok.

---

Posted on **2017-06-09 13:06:06** by **gero**:

Don't worry to much now. Have a guest for Booze and Billiards, so can't test tonight. Have the complete Saturday to try to narrow it down tomorrow. Any tip or test version welcome.

---

Posted on **2017-06-09 13:51:45** by **Bar**:

I'm going to try to replicate the problem exactly. Which version from the release are you using, the source or one of the precompiled ones?

---

Posted on **2017-06-10 00:35:45** by **gero**:

I tried the master from the the main page and source from the release page. The idea from @TheRiflesSpiral for a checksum for download sounds perfect to rule things out. After my second strong coffee, I will be ready to investigate more.

---

Posted on **2017-06-10 01:49:17** by **davidlang**:

If you clone the repository via git, that does checksums (and more) as part of the download.

---

Posted on **2017-06-10 03:20:01** by **gero**:

Thanks @dave. Will defiantly try that via GitKraken.

---

Posted on **2017-06-10 03:36:18** by **gero**:

Hey Linux buddies, how do achieve a download with a checksum? GitKraken is to complex and via terminal:

git clone https://github.com/MaslowCNC/GroundControl.git

Cloning into 'GroundControl'...

remote: Counting objects: 5066, done.

remote: Compressing objects: 100% (15/15), done.

remote: Total 5066 (delta 7), reused 12 (delta 6), pack-reused 5045

Receiving objects: 100% (5066/5066), 122.56 MiB | 2.82 MiB/s, done.

Resolving deltas: 100% (2715/2715), done.

Checking connectivity... done.

---

Posted on **2017-06-10 07:58:34** by **scottsm**:

Sorry @gero, I'm not sure I can answer. I can say that when I git clone as you show I get the same numbers.

---

Posted on **2017-06-10 10:17:20** by **gero**:

https://youtu.be/b6qG8QQeddo Video 1 showing that I can't run this weeks release. https://youtu.be/zQUpN2iHjSM Video 2 showing that I can start any older GC and move the sled. (and an attempted square :-))

---

Posted on **2017-06-10 11:44:10** by **gero**:

Giving up on this one. After ~30 downloads of .zip and .tar.gz plus cloning in the office and the workshop, sending the files via network and carrying them via usb-drive, I think I can exclude a file corruption. There is another Saturday coming end of next week.

---

Posted on **2017-06-10 12:06:55** by **davidlang**:

after you do the git clone, you have a directory called "Ground Control", go into that and you will see all the source. I believe that you can just run main.py from that directory.



once you have cloned a project once, you can update to the current version by going to the directory it was cloned into and doing 'git pull' (as long as you haven't made any local modifications)

---

Posted on **2017-06-10 12:14:51** by **davidlang**:

probably a silly question, but when you fire up arduino to compile the firmware, are you sure that it was compiling the latest version, not an earlier version? I couldn't tell from the videos which directory it was compiling from.

---

Posted on **2017-06-10 12:47:03** by **scottsm**:

It looks like the version 73, the lines:

#define SERIAL_RX_BUFFER_SIZE 512

#define SERIAL_TX_BUFFER_SIZE 512

are new to that version.

---

Posted on **2017-06-10 22:58:14** by **gero**:

@davidlang yes, in the video I missed the step of opening the firmware, but it was the latest. Done it to many times. :-)

---

Posted on **2017-06-10 23:56:58** by **scottsm**:

@gero, you could try commenting out those two lines that set the serial buffer sizes to 512. That is new to version 73, and maybe they take up too much of the memory. The default buffer size for these is 64.

---

Posted on **2017-06-11 00:16:58** by **scottsm**:

Another troubleshooting thing to try is to open the Arduino serial monitor and send B05 followed by a new line. The firmware should respond ‘Firmware v0.73’

---

Posted on **2017-06-11 11:11:24** by **gero**:

The B05 gave me the correct Firmware. Commenting out the 2 lines uploaded fine but did not solve the dropping connection. The serial monitor of Arduino IDE looks fine and prints out all lines. Again, OLDER GC stayes connected with current firmware. The issue is replicated with an old desktop and same kubuntu.

---

Posted on **2017-06-11 13:18:11** by **scottsm**:

Do you have a TTL-232 USB serial adapter in your toolkit? I’ve troubleshot a different GC-to-firmware comm issue using one to echo whatever the firmware receives on the main serial port out one of the Mega secondary serial ports. It could answer whether the data arrives correctly, allow comparing what the working and non-working versions of GC send.

---

Posted on **2017-06-11 13:42:49** by **gero**:

I don't have that adapter but could use an Aruino Uno for that, right?

---

Posted on **2017-06-11 14:09:22** by **gero**:

I just sacrificed my environmental robot and ripped the Mega out to confirm that its not the board. Same behavior that old GC stays connected and new GC loops in connecting and loosing. Now that i know I can test without motorshield I can try with Ubuntu-Mate in the office to rule out the linux version.

---

Posted on **2017-06-11 14:31:31** by **gero**:

The Linux version was not ruled out, in fact it was confirmed that I don't have a dropping connection on Ubuntu Mate :-O

---

Posted on **2017-06-11 15:01:24** by **gero**:

So what is it? Python, kivy or the handling of USB/serial of the OS itself? What has changed in last GC to stop it from running on kubuntu 14.04?

---

Posted on **2017-06-11 15:09:45** by **scottsm**:

It sounds like you’re making headway on the Linux front. Let me know if the serial sniffer would be useful.

---

Posted on **2017-06-11 15:18:02** by **gero**:

Sure, I'll think I can get the Uno to work as an serial adapter and I beleive I can figure out the connections on the Mega, but what and how to run?

---

Posted on **2017-06-11 16:11:01** by **scottsm**:

Hook up ground and connect the Uno RX (pin0) to the beta Maslow board AUX5, which happens to be Rx0 for the Mega (oops!). Try using a serial terminal or Arduino Serial Monitor on the Uno to see whether you can 'hear' the characters coming to the Maslow. I'm not sure how to use the Uno as a serial adapter :(...

On my unit I get:



G20   

B03 A2438.4 C1219.2 Q2995.65 E369.29 F310.2 R139 H79 I1 J8148.0 K10 M6.35 N3.17 P7560.0   

B03 A2438.4 C1219.2 Q2995.65 E369.29 F310.2 R139 H79 I1 J8148.0 K10 M6.35 N3.17 P7560.0   

B05   

G20   



Note: the B03 lines have wrapped - the M6.35 lines are part of the B03 lines...



A hex dump looks like [this:](/images/x8/x8yl_gctomegastartup.png.jpg) .

---

Posted on **2017-06-11 16:37:12** by **scottsm**:

Just noticed that the hex dump got cut off. [Here's the whole thing](/images/my/myw3_gctomegastartup.png.jpg)

---

Posted on **2017-06-12 16:49:10** by **Bar**:

I just want to jump in to say that I've been trying to figure this out on my end too, with no luck. I can't get the issue to happen. I've tried all the version of GC and they all seem to work. I though maybe the Arduino IDE updated since I downloaded mine, and so I uninstalled and updated that, with no change (still works).



There is something weird going on where the compiler is optimizing away variables as 'unused' but we actually need them. Or at least that's what I think is going on. 



The only other thing I can think to do is give [this](https://www.dropbox.com/sh/y7ml553ns66p58x/AABegurqSkQBiQCeTTfKJ6Vxa?dl=0) precompiled firmware a try. Also, maybe check the terminal in the Arduino IDE to make sure that the machine really is sending back information (when the connection drops it's because GC hasn't heard from the machine in two seconds).



I'll let you guys know when I find out more

---

Posted on **2017-06-13 01:12:42** by **larry357**:

Have you tried clearing the EEPROM before installing new firmware? Or is there a loose wire/connection/broken the other thing to check is if the power supply is faulty. So try a new source for the Arduino.

---

Posted on **2017-06-13 09:45:41** by **gero**:

Warning! This (fix?) is not recommended as it is unclear if it might break more then it fixes. On Kubuntu 14.04LTS pyserial 2.6 was the installed version. On Ubuntu-Mate 16.10 and Kubuntu 16.04LTS the version is pyserial 3.3. The command "sudo pip install pyserial --upgrade" uninstalled 2.6 and installed 3.3. GC is not dropping the connection anymore on Kubuntu 14.04LTS. Great thanks to @scottsm!!!

P.S. Do not try this at home!!! :-o

---

