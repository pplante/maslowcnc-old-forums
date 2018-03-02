## Bluetooth to Audrino?
Posted on **2017-07-13 09:02:33** by **mrfugu**:

I've been investigating porting Ground Control to iOS and the single largest stumbling block so far seems to be serial i/o from iOS devices via USB, and powering the MaslowCNC Audrino board (and/or iOS device).



Apple's (strict) guidelines mandate that any device connected via USB be MFI (made for iphone) certified. While it still might be possible via the Camera Connection Kit to allow serial communications, it seems Apple recommends primarily Bluetooth for similar situations. Charging an iOS device and powering the Audrino make USB a little more problematic as well, although the new camera connection kit alleviates this i think, but  Bluetooth seems most compelling in the long run.



As I understand it, this would require an additional board to be added to the stock Audrino Mega, or using a different Audrino board?



Long Story short, what is the possibility of adding bluetooth to the Maslow's Audrino? Could this be done by finding an Audrino board with BT built i n? Adding a board? 



It's early days for my iOS attempts, but there is a Kivy-ios port, I can get GC to compile etc, and I think it's entirely possible to create a working build if Bluetooth is used.

---

Posted on **2017-07-13 12:45:54** by **Bar**:

I agree that Bluetooth sounds like the way to go. I'd look at something like this: http://makezine.com/projects/connect-an-arduino-to-a-7-bluetooth-serial-module/



You would have to solder directly to the right pins, but I think it should work.

---

Posted on **2017-07-13 13:50:30** by **TheRiflesSpiral**:

Good grief... that seems too simple to possibly work correctly! :D

---

Posted on **2017-07-13 13:56:55** by **mrfugu**:

in defense of simplicity: it is just a serial connection...

---

Posted on **2017-07-13 14:03:17** by **TheRiflesSpiral**:

No, it's a wireless, ad-hoc encrypted network that carries a serial connection. :)

---

Posted on **2017-07-13 14:04:53** by **TheRiflesSpiral**:

It's just impressive to me that the connection piece is basically transparent... the fact that a developer doesn't really have much to consider in the way of connection type is especially cool.

---

Posted on **2017-07-13 15:18:05** by **scottsm**:

To connect to an IOS device, you might need a BLE-flavored device. [Here](https://tronixlabs.com.au/arduino/boards/mega/bluno-mega-2560-bluetooth-le-with-arduino-mega-australia/) is a Mega with BluetoothLowEnergy built in. I haven’t used these, just saw them mentioned [here](http://www.instructables.com/id/Tutorial-Using-HC06-Bluetooth-to-Serial-Wireless-U/).

---

Posted on **2017-07-13 15:48:28** by **mrfugu**:

you're correct that a BLE (and bluetooth 4.0) will be currently 'most favored' by iOS.

---

Posted on **2017-07-13 16:11:23** by **larry357**:

There was already a bit of discussion on using another board that was a bit faster a while ago, I suggested using an ESP32 as they are getting very cheap :) https://www.aliexpress.com/item/Official-DOIT-ESP32-Development-Board-WiFi-Bluetooth-Ultra-Low-Power-Consumption-Dual-Core-ESP-32-ESP/32799954012.html

---

Posted on **2017-07-13 17:34:26** by **scottsm**:

The ESP32 is interesting, but will require significant work to make it work -a  different interrupt structure, a different approach to non-volatile on-board storage and a change to the number of gpio pins used to drive the three motors. A BLE Mega should run right out of the box, if the BLE serial connection is stable.

---

Posted on **2017-07-13 20:30:21** by **davidlang**:

The BLE mega is going to be the same speed as a plain mega (16 mhz) and rather expensive in comparison. If I was going to spend that sort of money, I'd want to see a performance improvement.

---

