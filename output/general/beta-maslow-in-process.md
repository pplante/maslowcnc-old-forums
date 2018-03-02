## Beta Maslow in process
Posted on *2017-03-22 07:42:00* by *Jennifer D*

I have the sled cut! Yay! It's slight elliptical, but I'm hoping that's ok. The offset elliptical hole is from my first attempt this morning - the measurement between chain attachment points is definitely important, and from the looks of my finished sled I need to measure still more carefully. 

I'm going to move my router to the new sled and see if I can get it mounted and calibrated. 

@Bar, definitely repeatable issues with ground control and my serial connection this morning - attempted to remeasure chains and there was no response until I unplugged and replugged the USB cable. Still doesn't respond to the test motor function either. 

I'm taking more detailed notes on my computer through this morning's process and will post those once I can get my wifi to work again(storm took out our power last night and everything's not quite back to normal yet).  [Image](//muut.com/u/maslowcnc/s3/:maslowcnc:UUu7:image.jpg.jpg) 

 [IMG_0423](//muut.com/u/maslowcnc/s3/:maslowcnc:DQpZ:img_0423.jpg.jpg)

---

Posted on *2017-03-22 08:08:09* by *Bar*

Looks fantastic!

I think the issue with Test Motors not responding may be a firmware version issue. We'll come out with a new version today so we can check that.

When the serial connection isn't working, does ground control still say it is 'connected'?

---

Posted on *2017-03-22 08:15:55* by *Jennifer D*

Yes, the last firmware update has allowed it to stay connected without any drops, and haven't gotten any errors either.

---

Posted on *2017-03-22 08:19:45* by *Bar*

If it's saying it's connected that means that the serial connection is truly open at least in one direction. The machine sends back it's position every 200ms and if Ground Control starts missing those it closes the connection says "Not Connected"

---

Posted on *2017-03-22 08:20:17* by *Bar*

You could be seeing an issue with the machine not telling Ground Control that it is ready for a new command

---

Posted on *2017-03-22 08:21:15* by *Bar*

When it's stuck is the last text line on the terminal "ready"?

---

Posted on *2017-03-22 08:56:04* by *Jennifer D*

I believe it did, however, it finished the motor calibration on the new sled and this is what I see  [Image](//muut.com/u/maslowcnc/s3/:maslowcnc:UPJ3:image.jpg.jpg) 

 [Image-0](//muut.com/u/maslowcnc/s3/:maslowcnc:XRil:file_0image.jpg.jpg)

And when I unplug and plug it back in it then says ready

---

Posted on *2017-03-22 09:00:12* by *Jennifer D*

I just tried to calibrate again, making sure the status was "ready" and it didn't start calibrating until I unplugged and replugged the USB. However, any commands from the main GC screen(versus the actions screen) work so far as I can tell. 

I have to close up the shop for the rest of the day, won't be able to play around with settings and such again until Friday. Will keep an eye on the forums and such though!

---

Posted on *2017-03-22 09:40:24* by *Bar*

Very strange. I will investigate and see if I can get you a conclusive answer before then.

---

