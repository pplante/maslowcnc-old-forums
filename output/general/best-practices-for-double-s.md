## Best Practices for Double Sided Cutting?
Posted on *2017-03-14 21:28:26* by *tmaker*

I'm curious if Bar or anyone has attempted to mill both sides of a plywood sheet using Maslow and if there are any best practices for keeping everything aligned precisely?  I have some designs brewing in my head that would require both sides of a plywood sheet to be cut but I'm curious if there is a good way to flip the sheet over while maintaining precise alignment.  Might this require a recalibration or positioning of the router after the sheet is flipped?  

Please tell me if I'm way off, but my first thoughts would be to drill a straight hole (drill press would be difficult so maybe using the Z-axis on the router?) in the extreme lower left corner that the router can reach and tell Maslow that's where home is.  After Maslow finishes cutting the front side, flip the sheet over from right to left so that the hole is now in the lower right corner.  Reposition Maslow so that the bit drops and fits perfectly into the hole on the right, load in the new tool path and tell it to cut.

Potential issues that I can see with this method would be that things still might not line  up correctly if the plywood isn't seated perfectly horizontal from what the Maslow software thinks is horizontal.  I'm not all that familiar with the calibration process so it's possible that this is already taken care of and that it's a non-issue.  If anybody can shed some light in this area it'd be greatly appreciated.  Thanks!

---

Posted on *2017-03-15 00:11:10* by *davidlang*

your idea is about the best that is possible (you may want to put the hole someplace more central, but that doesn't change the basic idea or it's limitations)

---

Posted on *2017-03-15 06:20:13* by *TheRiflesSpiral*

The only risk you run with just one hole is that the plane against which your workpiece rests (the board at the bottom) may not be aligned with the same plane in the drive system of Maslow.

Here's how I personally would handle this:

1) With no workpiece in the Maslow, mill two holes at the far edges of where your workpiece will be. They should be fairly large if your design will accommodate it. Big enough for a 5/8" or 1" dowel. (You've now established Maslow's workspace in the real world, on the backer board)

2) Put your workpiece in Maslow and mill those same two holes.

3) Put dowels in the holes through your workpiece and the backing board and mill your front design.

4) Flip the sheet over, replace the dowels and mill your back design.

---

Posted on *2017-03-15 06:45:38* by *tmaker*

Two big dowels makes sense and should solve the horizontal plane issue.  But I'm curious if there still might be some flexing issues with all the weight of the plywood on the dowels.

Here's a video that shows a similar method used on a Shopbot: https://youtu.be/Wd54ai1Xbnk

---

Posted on *2017-03-15 07:23:42* by *TheRiflesSpiral*

In that case (where the dowels don't support the piece adequately) I'd probably knock some wedges in the corners so they're just alignment, not support)

---

Posted on *2017-03-15 08:04:00* by *davidlang*

dowels can help address the positioning of the work, but you still have to worry about making it symmetrical, which requires setting the right zero point after flipping.

---

Posted on *2017-03-15 08:24:35* by *jbarchuk*

Dangit, long freeking post, but there are a lot of workflow details here. :(
@tmaker very good point. Even large wood pins will twist and wear out over time, by the weight of the workpiece. I think it'd work fine for one or a few pieces, but not production quantities of use.
The pins are not so much of a loss, those are easy to replace, but the holes in the spoilboard will eventually develop an oval shape. However using a vertical orientation system Maslow actually has an advantage using gravity to hold the workpiece in the X dimension, and that'll become apparent in a minute....
EDIT... As I was writing this way of using just one to align the workpiece, I thought of another way that uses no pins that I will add at the bottom. Same theory in general though, using gravity to hold one dimension.
With the horizontal-plane style of Shopbot the workpiece needs to be aligned and fastened in two dimensions, and light weight pins can track and hold the alignment because other than the router there's no serious weight on the pins.
Maslow uses gravity to hold the workpiece against  the kickplate at the bottom of the frame, so that alignment happens automatically!!
The Q is how to align it horizontally.
This is not difficult with a z-axis controller. It could be done by hand with an electric drill, but slightly less accurate.
Load the workpiece.
Pick a point anywhere very near the horizontal-center of the workpiece, that is not where the router will cut, in a scrap area. Preferably at the -=exact=- center, which will save a little adjustment step later. But for many designs finding the right point might be impossible, so there's still another technique.
Route a hole through the workpiece -and- the spoilboard, of the diameter of a small wood dowel. (1/4" dowel is all that's necessary because it won't have any weight on it.)
Press a dowel into the new holethrough the workpiece and into the spoilboard.
IMPORTANT... the top of the dowel must not protrude beyond the top surface of the workpiece, or it will interfere with the motion of the sled.
CLAMP THE WORKPIECE TO THE SPOILBOARD to avoid any horizontal shifting.
These next few steps are correct -IF- the dowel was added at the exact horizontal-center of the workpiece. If not then I added a few lines after these lines.
Flip the workpiece, pull the dowel out of whichever piece it happened to stay attached to, and insert it into the hole in the spoilboard.
Set the workpiece on the bottom kickplate. *THAT'S* what takes care of the vertical alignment. :)
Tilt the workpiece back gradually, eyeballing the line of eventually mating the alignment hole in the workpiece with the pin mounted in the spoilboard. When those two points align and the pin fits in the workpiece hole, horizontal alignment is achieved. Done and done, cut the second side. End.
If the alignment dowel is not at the exact horizontal center, there are two ways to adjust for that, and one way to ignore it and still use the same dowel hole.
First is to route a second alignment hole in the spoilboard, with the hole mirrored on the centerline in the x-dimension. That will automatically line up with the hole in the workpiece after the workpiece is flipped horizontally. That should probably be done when the first spoilboard alignment hole was routed, to avoid more unnecessary handling of the workpiece board and changing bits and such.
Another way is to know the offset dimension, and program that variable into the starting point of the router for the reverse side cut.
Another way, IF the dowel hole isn't too far off the x-centerline, AND the workpiece doesn't slide too far off to the left or right to get out of the 'accurate/useful' range of the router, then flip the workpiece, mount it on the kickplate, align and mate the dowel and hole in workpiece. The workpiece has -shifted- in the x dimension, by exactly the distance the alignment dowel is mounted away from the vertical centerline. Program that number into the starting point of the next cut.
ADDENDA, a way to achieve horizontal alignment with no pins. This technique is very common in all kinds of woodworking. UNFORTUNATELY it's a VERY UNCOMFORTABLE technique for very LARGE weights such as 4x8 sheets of plywood. But it's doable. ALSO UNFORTUNATELY it's only eyeball-accurate, but with practice and a scriber rather than a pencil can be accurate down to 1/32 or 1/64". That's not -precise- but probably adequate for many applications that don't require super-alignment.
The workpiece is resting on the kickplate. Vertical alignment is automatic and accurate.
With a square, mark a vertical line across the kickplate and a bit up into the workpiece.
Next, use the square to transfer the line on the front side of the workpiece to the back. I really can't explain that here in a few words but here's a video that demonstrates a few ways to do it. https://youtu.be/ZVqYBfKl2rk
After cutting the first side, and flipping the workpiece horizontally, use that transferred line to align with the line on the kickplate, and horizontal alignment is achieved. No pins! Yay! :)
I said UNCOMFORTABLE because manhandling a 60# chunk of 4'x8' plywood so you can see and accurately work on the top, -then- the edge, and -then- the back is NOT FUN OR EASY, but doable.
Regardless, it's the accuracy of that line transfer that determines how the overall accuracy will line up. That's why I said scriber not pencil works much better.

---

Posted on *2017-03-15 10:04:11* by *tmaker*

Please correct me if I'm wrong, but it sounds like you're assuming that the kickplate on the bottom will always be in perfect horizontal alignment with Maslow and the software.  If that assumption was true, your process sounds like it would work.  But personally, I would like to come up with a solution that doesn't assume or require that the kickplate will always be in perfect horizontal alignment.  Let's face it, 2x4s can easily bow and change over time, with humidity...etc even if it's not all that noticeable with the naked eye.  

The thing I like about the 2 pin / dowel idea (check the video I sent earlier) is that it would still allow you to perfectly align your work from front to back even if you started with some crazy kickplate angle at lets say 45 degrees.   The work might not be fully resting across the entire kickplate if it wasn't level, but the software wouldn't care because the pins would still be in alignment.  

What I don't like about the pin idea is that 1) the pins can get in the way of the sled if they aren't recessed and 2) the weight of the material  would likely flex the pins enough to throw off the alignment or degrade the dowel holes in the spoil board over time.  Hmm...I still feel like there's a better solution here that just needs some time to marinate in our brains..

---

Posted on *2017-03-15 10:48:02* by *davidlang*

what sort of accuracy are you looking to get? the Maslow only claims 1/64 of an inch to begin with, and realistically, wood swells/shrinks more than that, and any sanding/finishing you will will add/subtract more than that.

---

Posted on *2017-03-15 10:53:21* by *tmaker*

I was hoping to stay within that 1/64 tolerance.

---

Posted on *2017-03-15 11:00:57* by *davidlang*

The clearance for pins (to be able to get the workpiece over the pins), or the measurements of the width of your wood (if you have a stop on the side that you push against) are going to be off by more than 1/64 of an inch.

Even using metal pins you will have trouble positioning anything to that accuracy.

---

Posted on *2017-03-15 11:10:41* by *TheRiflesSpiral*

Ouch. Yeah... 1/64 is going to be tough for that purpose. Given the compressible nature of wood I'm thinking you may need to cut, flip and then do some "spot" checks at the extreme edges of your design to see how the bit is going to land.

Good luck, whatever you decide. I'm sure we'd love to hear about your progress!

---

Posted on *2017-03-15 11:14:22* by *tmaker*

While I was hoping to stay within that tolerance, it's possible that it's unnecessary to be that accurate for the parts I'm designing. I'm sure even 1/32 or maybe 1/16 would be fine.  After I get everything setup I'll have to run some tests and explore some ideas.

---

