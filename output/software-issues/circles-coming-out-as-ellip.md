## Circles coming out as ellipsis
Posted on **2017-03-24 12:43:08** by **Bar**:

I've run the same gcode on my full size machine and on the scaled down version and I can confirm that there is something funky about the way the internal  math is compensating for the machine size. 



On the big machine I get a perfect circle, on the little machine I get an ellipse elongated vertically. So the good news is I can replicate the issue and solve it, and if you are getting elliptical circles, you aren't doing anything wrong. The bad news is that I need to fix it.



If you need round circles right away, I can say that the 

 [default settings](/images/k7/k7km_defaultsettings.jpg.jpg) will give you the right results, but you've got to find a way to position your motors the default distances from the corners of the plywood and construct a sled with the correct dimensions. 



I will have this tracked down ASAP!

---

Posted on **2017-03-24 15:29:39** by **Bar**:

I think I've got this one tracked down (fingers crossed). I moved the discussion into the GitHub issue [here](https://github.com/MaslowCNC/Firmware/issues/140)

---

Posted on **2017-03-24 17:20:08** by **mindeye**:

In the meantime, I've had good success this afternoon with fiddling with the horizontal motor offset. My initial measured 285 produced a 3.5" output vertical movement for an input of 4". Bumping to default 270 got me 3 5/8", Jumping down to 170 produced 4.25" and moving to 220 got the ideal 4" movement. I suppose this makes some sort of sense in theory but empirically it works so it's good enough for me.

---

Posted on **2017-03-24 17:28:45** by **mindeye**:

Nearly there, vertically a 12" diameter circle came out perfect. Horizontally it was still off by an extra 1/4" so this approach doesn't fully solve the issue but it's a lot better than my initial -2.75" vertical and +1" horizontal.

---

Posted on **2017-03-24 18:43:55** by **jbarchuk**:

> @mindeye

> My initial measured 285 produced a 3.5“ output vertical movement for an input of 4”. Bumping to default 270 got me 3 5/8“, Jumping down to 170 produced 4.25” and moving to 220 got the ideal 4" movement.

This is similar to what I meant in another post, automating a 'reverse calibration' process...

Screen says 'manually move the sled to somewhere in the upper-left corner, and tape a pencil to the sled'.

User does that and pushes the Okie-Dokie button.

GC draws a long horizontal line to the right, goes back to the start, and draws a long vertical line down.

GC says 'remove the pencil, and manually move the sled to the lower-right corner.'

User does that and pushes the Okie-Dokie button.

GC draws a long horizontal line to the left, goes back to the start, and draws a long vertical line up.

GC says 'please measure all four of those lines, and tell me what length they are'.

User does that.

GC knows what the line lengths should have been, what they are in reality, and calculates the error factor.

Done.

This would be much faster, easier, and more accurate.

BTW as so meone mentioned losing data when the GC is updated... Any data like that that you enter on a screen, either write it down or take a screencap to make a record of things. If you don't I guarantee you'll make that mistake only once. ;)

All this measuring going on, I STILL don't trust any of these chinese tape measures. Nothing is accurate unless it's gauged against an independent known-accurate scale. Then there's the uncertainty caused by measuring on the left side of the tic mark on the tape, the right side, or the center. Right there is a whole mm of error. Whichever way you go, left, right center, at least do it the -same- -way- every time.

---

Posted on **2017-03-24 18:49:20** by **blsteinhauer88**:

I  put a screw dead center of the sheet and drew a crosshair. I  measured and got close and adjusted the measurements after to zero in on the target.  [IMG_0473](/images/ny/nydq_img_0473.jpg.jpg)

---

Posted on **2017-03-25 08:14:43** by **Bar**:

I totally agree that a calibration process to dial things by moving to known points (like blsteinhauer88 did) is the way to go.



I think ultimately we want to move to a number of known points and work back to find the true dimensions of the machine.

---

