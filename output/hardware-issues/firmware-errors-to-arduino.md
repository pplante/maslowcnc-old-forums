## Firmware errors to Arduino
Posted on **2017-03-17 21:24:52** by **blsteinhauer88**:

Below is the message I got when I tried to reload the firmware.  Bar, During the set up I get to "Chain Setup" where it measures a length.  Only the left motor does start after about 2 minutes of waiting while a circle starts growing from the center point on the Groundcontrol screen, But turns to the left and the chain set at 12:00 as you have it set up in the photo falls off.  The right never moves.  I tried this several times and switched the motors in case there was a "left and right", but it did not work again.  

The same thing happened 3 times so I tried to reload the Firmware "in case", but now I get errors on the reload.  I copied the message for you programmers to take a look at.

 Another note:  I played with the directional pallet on the GroundConrol screen.  Any direction I pushed, or the Home button only turned the left motor and to the left.  It would not turn in two directions.  

I did press the Calibrate Motors, and it turned them both starting with the right one, it different directions at different  speeds.

Here is the error message:

Arduino: 1.8.1 ( Windows 8.1), Board: "Arduino/Genuino Mega or Mega 2560, ATmega2560 (Mega 2560)"

In file included from C:\Users\Lon\Downloads\Firmware-master\Firmware-master\cnc_ctrl_v1\cnc _ctrl_v1.ino:16:0:

C:\Users\Lon\Downloads\Firmware-master\Firmware-master\cnc_ctrl_v1\cnc _ctrl_v1.ino: In function 'interpretCommandString(String)':

sketch\CNC_Functions.h:558:22: warning: iteration 22 invokes undefined behavior [-Waggressive-loop-optimizations]

         sect[i] = ' ';

                      ^

sketch\CNC_Functions.h:557:5: note: containing loop

     while (i < 23){

     ^

Sketch uses 35658 bytes (14%) of program storage space. Maximum is 253952 bytes.
Global variables use 1461 bytes (17%) of dynamic memory, leaving 6731 bytes for local variables. Maximum is 8192 bytes.
avrdude: stk500v2_recv(): checksum error
avrdude: stk500v2_recv(): checksum error
avrdude: stk500v2_recv(): checksum error
avrdude: stk500v2_recv(): checksum error
avrdude: stk500v2_recv(): checksum error
avrdude: stk500v2_recv(): checksum error
avrdude: verification error, first mismatch at byte 0x1014
         0xfc != 0x08
avrdude: verification error; content mismatch
avrdude: verification error; content mismatch

This report would have more information with
"Show verbose output during compilation"
option enabled in File -> Preferences.

---

Posted on **2017-03-17 21:52:44** by **scottsm**:

Is GroundControl still open/active while you are reloading the firmware? I have had errors like that when other programs than Arduino were holding the serial port open...

---

Posted on **2017-03-17 21:58:52** by **scottsm**:

I can remember one time when unplugging/replugging the USB cable was what finally re-loaded the serial drivers and got Arduino to reload the firmware successfully :(

---

Posted on **2017-03-17 22:12:04** by **blsteinhauer88**:

No It was closed, but ...Update:  I deleted all files of the firmware and directories created by the unzipping....and got a new copy and started from scratch, and it up loaded clean.   Thank gosh hate the think I broke it already.  Anyway, I tried the "Calibrate chain length", again and only the left motor runs, and runs to the left.  The right again did not run.  In the control panel this time the left motor would only run, but now in both directions, but the right motor is still silent.

---

Posted on **2017-03-18 08:04:17** by **scottsm**:

I think that 'left motor only' situation is correct, but we don't have all the instructions yet. Look at Bar's answer to a similar question [here](http://www.maslowcnc.com/forums/#!/general:calibrate-chain-length/scottsm-is-correct-the-ma).

---

Posted on **2017-03-18 10:00:09** by **blsteinhauer88**:

Thanks, that makes it more understandable.

---

Posted on **2017-03-18 11:43:06** by **Bar**:

Is there a way I can make the directions more clear about how to program the Arduino?

The left motor only is correct. I will add some language to the directions to make that more clear. I had them measure out the chain one at a time so it's easier to keep an eye on them and make sure the chain doesn't get tangled. That's also why the measure out the chain so slowly.

---

Posted on **2017-03-18 12:11:57** by **blsteinhauer88**:

No, Programing instruction are great. I created the problem with that. Which is what is supposed to happen in beta, so, I went back to your instructions and re- loaded the firmware like it was new and fixed the issue. 

I was playing with the setup late and tried the chain calibration, this is still confusing, but I know you are not finished.  All else is great so far. Lon

---

Posted on **2017-03-18 12:19:16** by **blsteinhauer88**:

One thing still, your photo of the chain on the sprocket shows it staged from the left at the 12 o'clock. When I press the calibrate chain function, my chain drops because the heat turn counter clock wise. I had to stage the chain from the right to have it measure the length of chain.

---

Posted on **2017-03-18 13:38:12** by **Bar**:

:-)

You might need to swap which motor is on which side if they are rotating the wrong direction, or probably just swap the wires.

---

