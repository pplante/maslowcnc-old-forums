## New GC release .72
Posted on *2017-05-19 11:46:32* by *blsteinhauer88*

Wow, Maslow on roids! 
1. When changing the Z in and out it pulses. http://www.youtube.com/watch?v=V4TEEBwdQE0

2. Motors twitch when movement paused to change Z http://www.youtube.com/watch?v=eWxVx1UXTm0

3. Cutting much faster! 60 inch per min. http://www.youtube.com/watch?v=LU5Hukqu3Lw 
Video not sped up🙂👍🏻

---

Posted on *2017-05-19 11:55:19* by *blsteinhauer88*

Sled moves around during Z retract due to jerking. Cuts into pattern a bit. Also it's not waiting for full Z retract before it moves again and drags bit while still retracting,  [Image](//muut.com/u/maslowcnc/s3/:maslowcnc:Gfcg:image.jpg.jpg)

---

Posted on *2017-05-19 12:00:07* by *blsteinhauer88*

Video of bit jerking due to sled motor jerk during stationary Z adjustments http://www.youtube.com/watch?v=S1SqzIEkT9w

---

Posted on *2017-05-19 12:16:47* by *blsteinhauer88*

60 inch per min! Nice on longer lines. http://www.youtube.com/watch?v=IvskCh_cFzg

---

Posted on *2017-05-19 12:37:43* by *scottsm*

I noticed the jerky motion and disconnected my z-axis. GC.72 seems to have broken the manual z operation, ignoring all z prompts after the first one (issue opened for that).

---

Posted on *2017-05-19 12:57:00* by *blsteinhauer88*

Mine is adjusting. It only ramped a few cuts. I will post a photo of the completed cut project.

---

Posted on *2017-05-19 15:14:13* by *blsteinhauer88*

[IMG_0824](//muut.com/u/maslowcnc/s3/:maslowcnc:YDdk:img_0824.jpg.jpg)

---

Posted on *2017-05-19 17:13:27* by *blsteinhauer88*

Well cutting in the week spot, high and centerish, the motors chatter instead of a steady  turn. Zoom in on video of this to see, it causes chatter cuts in the piece. http://www.youtube.com/watch?v=Y2TjKvaJA1k
 [IMG_0827](//muut.com/u/maslowcnc/s3/:maslowcnc:2g9h:img_0827.jpg.jpg) [IMG_0828](//muut.com/u/maslowcnc/s3/:maslowcnc:bKfJ:img_0828.jpg.jpg)

---

Posted on *2017-05-19 22:26:09* by *davidlang*

This sort of chattering is a classic example of PID loops not being tuned correctly.

my (semi informed) guess would be that the P value of the position loop (like 69 per the weekly update) is probably too high, making it too aggressive in trying to correct position errors. But tuning PID loops is a black art, so I could be very wrong.

Play with the PID tuning values until the jitter goes away when stationary.

---

Posted on *2017-05-19 22:27:35* by *davidlang*

once we get the pid loops tuned so that it stays stationary when it's supposed to, then we will have to re-tune them for motion

---

Posted on *2017-05-20 17:12:16* by *blsteinhauer88*

It actually calmed down for a different sign i made.  Smooth Z control, but cut lower on the board.  May have been something in the first Gcode.

---

Posted on *2017-05-20 19:23:58* by *scottsm*

Your picture of the chattering on the scroll cut looked interesting to me. I noticed that the chattering happened on the part of the cut where the router was lowering. You mentioned that the problem occurred towards the top of the sheet. I created a similar shape, and tested it at 4 inch increments above the center. I found that once I got above 8 inches, I got a similar chattering pattern in the same portion of the cut, where the router was lowering. The higher the cut position, the more chattering on that lower side. Cuts below the center of the sheet weren't affected in this way. 
I'm not sure there's any connection, but in the test programs that demonstrate the PID operation, the negative example does poorly at trying to reach its goal. There might be something for one who is better with PID programming to look at.

---

Posted on *2017-05-20 22:36:54* by *blsteinhauer88*

I had the same happen today at Y -6 area. I pushed the inch per min to 100. Don't know if that made a difference?

---

Posted on *2017-05-20 22:53:55* by *davidlang*

was it chattering when it was stopped? the ipm setting won't make any difference there. In any case, the current firmware is still capped at 25 ipm (line 431 of CNC_Functions.h

One limitation to the current firmware is that it doesn't try to do any acceleration, it tries to go from stopped to full speed instantly, the lmits of the PID loop will smooth out the start of the cut, but not the end of the cut. this will show up in overshooting the corners a bit

---

Posted on *2017-05-20 23:00:04* by *blsteinhauer88*

Yes during Z retraction. Thats interesting that it is still capped. Seemed much faster.

---

Posted on *2017-05-21 01:33:56* by *davidlang*

There were other changes in the computation this week, instead of planning where to move next every 0.5mm, it looks at the speed it's told to travel and plans out about 3K times/sec, at 48 ipm that works out to about every 3mm.

so if this planning was the limiting factor in the speed, this could result in a very significant speed increase.

try commenting out that line in the firmware and see what you can push the speed to.

---

Posted on *2017-05-21 01:40:56* by *davidlang*

re: chattering when stopped.

does it chatter when no movement is happening (if there is a pause in running) or only when the Z axis is running?

---

Posted on *2017-05-21 03:11:06* by *davidlang*

If the chattering is happening under higher tension, but without Z axis movement, I would guess that the problem is that the speed PID loop is overly aggressive. It needs to apply more power before things move at higher tension loads, and if that causes it's output to ramp up too high before movement starts, that seems like it would match the symptoms that we are seeing.

I also wonder if there needs to be a guard band on the location PID, The resolution that we have there is far higher than needed (almost 51 steps per 1/64" of chain, we only need about 3 pulses per 1/64" to maintain our accuracy, so a dead zone of +-7 pulses would probably work well.

---

Posted on *2017-05-21 03:12:38* by *davidlang*

wait, you said it was bad at z-6, that's lower on the sheet, there is less tension there.

---

Posted on *2017-05-21 20:38:58* by *blsteinhauer88*

Yes it was chattering low too! It was paused with Z movement and motors twitching as in videos posted.

---

Posted on *2017-05-22 08:17:30* by *blsteinhauer88*

[IMG_0833](//muut.com/u/maslowcnc/s3/:maslowcnc:fWpo:img_0833.jpg.jpg) [IMG_0834](//muut.com/u/maslowcnc/s3/:maslowcnc:xKzO:img_0834.jpg.jpg) [IMG_0835](//muut.com/u/maslowcnc/s3/:maslowcnc:hwUK:img_0835.jpg.jpg)
First photo is at about y=+6 second is y= -6 next one is perspective photo. Chatter on both upper and lower curve lines.

---

Posted on *2017-05-22 09:05:34* by *scottsm*

That's pretty clear. How deep was the cut, what speed?

---

Posted on *2017-05-22 12:45:10* by *blsteinhauer88*

Well program was 100 ipm, but i heard firmware is still capped at 23

---

