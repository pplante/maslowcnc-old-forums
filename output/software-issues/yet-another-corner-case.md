## Yet another corner case
Posted on **2017-05-27 11:29:14** by **gero**:

FreeCad v.17 daily build might be responsible for this interesting find. FreeCad is under development, so bugs are expected. I am not sure though, so I thought I will share this. I wanted to cut a shelf with cutouts for LED lamps. The circles go down in 3 steps and the last round has 4 holding tabs. MaslowBH decided that music notes would look much better.  [IMAG0801](/images/v6/v6ka_imag0801.jpg.jpg) 

It was interesting to see how it lost position, found itself and continued as if nothing had happened. Interesting also that after each position loss it assumed itself higher in GC, showing the error circle and displaying a downward move, while the sled was going up to meet the position GC showed. https://youtu.be/JTxUoL5ntzU It takes off at 1:12. The .nc is here (at own risk) https://www.dropbox.com/s/qc07z9749kxre45/light2.nc?dl=0

---

Posted on **2017-05-27 11:33:06** by **davidlang**:

any time you get buffer overflow, it's really hard to recover from it.

---

Posted on **2017-05-27 11:34:46** by **gero**:

The finding itself feature work really nice

---

Posted on **2017-05-27 11:34:54** by **davidlang**:

hmm, gcodesimulator has trouble with it

https://nraynaud.github.io/webgcode/

---

Posted on **2017-05-27 11:35:49** by **davidlang**:

interesting, this not only uses X Y Z axis, but also I J K

---

Posted on **2017-05-27 11:36:38** by **gero**:

I only tried CAMoptics and it ran well there. Thanks for the generator tip.

---

Posted on **2017-05-27 11:38:10** by **gero**:

I did not choose any post processor, because other than linuxCNC, I did not know the rest

---

Posted on **2017-05-27 11:39:14** by **davidlang**:

it also has lines like:

G0 G0 F800 X348.500000 Y292.500000 Z5.000000



(the double g0 isn't right)

and calls for a tool change as T1.000000 instead of T1  (it's outputting float, not int there), it's also dumping everything in far too high a precision.



was this using FreeCAD to convert to the .nc file?

---

Posted on **2017-05-27 11:40:30** by **gero**:

Yes, the FreeCad path

---

Posted on **2017-05-27 11:41:07** by **davidlang**:

never mind the IJK, that's part of the G3 command

---

Posted on **2017-05-27 11:42:11** by **gero**:

I might try the different post processor to see if that changes the things you found.

---

Posted on **2017-05-27 11:50:17** by **gero**:

The G0 G0 was human error. It went back to x0,y0 after each circle so I deleted those lines. Must have missed 1 G0

---

Posted on **2017-05-27 12:01:56** by **davidlang**:

Ok, I cleaned up the file a bit, it's at http://lang.hm/maslow/light2.simplified.nc



other than the double G0, I don't see anything that I would expect to cause grief on the maslow (I expect the T1.00000 would confuse machines that actually looked at the Tool change command, but maslow is too simple to do so)



see if this works any better (and see if you still get the buffer overflow errors popping up)

---

Posted on **2017-05-27 12:09:03** by **davidlang**:

I probably misread what was happening the first time I looked at the gcode simulator.



looking at things in more detail, I'm pretty sure it's the G0 G0 that messed up the maslow, but check



I also created lang.hm/maslow/light2.single.nc that just cuts a single circle

---

Posted on **2017-05-27 12:13:54** by **davidlang**:

P.S. could you re-run the accuracy test with all the squares around the sheet now that we have the new double-PID firmware

---

Posted on **2017-05-27 12:25:10** by **gero**:

The buffer overflows are still there, on the first circle it did not throw the position off, on the second it did. Will try to get rid of those digits.

PS, will do my best to find a slot to rerun the squares the next days.

---

Posted on **2017-05-27 12:40:20** by **gero**:

light2.single.nc: The position is not thrown off. Buffer overflow happens at the last round at the second tab. But it seems as if it runs though, (have Z up now).

---

Posted on **2017-05-27 12:40:52** by **davidlang**:

remember that Bar bumped up the allowed speed, so you can now do about 900 mm/m, so that should make the tests go a bit faster

---

Posted on **2017-05-27 12:43:06** by **gero**:

I have the brackets outside now (like all) and have a lot of wiggling on the sled since. To compare with the previous cut I should but them back more to the inside.

---

Posted on **2017-05-27 12:43:58** by **gero**:

900mm/m is nice :-)

---

Posted on **2017-05-27 12:45:52** by **davidlang**:

I think on this error, we are going to need to have Bar take a look at it. I suspect the buffer overflow errors are the root cause of the problem. I don't see anything wrong with the tabs.

---

Posted on **2017-05-27 12:48:57** by **davidlang**:

on general testing, I think it would be very interesting to run a test with the brackets in the 9oclock/3oclock position, with one brick mounted above the sled (so that the CG is at the bit and both are in line between the brackets), this would require changing the h3 and s values in Kinematics.h to 0. If this works well, I think the math will be simplified enough to make a noticeable speedup

---

Posted on **2017-05-27 12:55:18** by **gero**:

Great idea, like the guy walking the rope... has a looong stick to balance. I am designing a new sled and will put that option into it. Also the holes on the brackets are far bigger then the screws and the turning points of the chains on the brackets have to much play. Still searching to mount the chain on a bearing.

---

Posted on **2017-05-27 12:55:59** by **gero**:

Oh, just read again, the brackets, not the bricks... still a good test

---

Posted on **2017-05-27 13:11:38** by **davidlang**:

brackets to the outside edges, bricks to top/bottom to make the sled balanced

---

Posted on **2017-05-27 13:12:30** by **gero**:

Tried with post processor LinuxCNC and less digits and K is gone.

G3 X92.0937 Y218.6482 Z-5.5000 I-15.9063 J-23.6482 F6000.00

---

Posted on **2017-05-27 13:15:07** by **davidlang**:

on another CNC machine I built, I used type 25 chain and milled the ends off a couple bolts, drilled a hole in them, and used a master link to attach the chain to the bolt. Doing something like this would give us as accurate a pivot point as we could get (limited by flex of the brackets)

 [Cnc_chain](/images/yg/ygmy_cnc_chain.jpg.jpg)

---

Posted on **2017-05-27 13:19:05** by **gero**:

I have seen that picture. I have turned off screws like that by hand. they were not drilled and flattened. In the picture the force is linear to the screw. On the Maslow, cutting at the top the forces are pretty sideways.

---

Posted on **2017-05-27 13:37:00** by **davidlang**:

You are correct about the direction of forces



But if the bolt is flattened to the correct thickness, and drilled for the master link, the chain can pivot on the pin from the master link (just as it would on a normal chain link at that point)



In the picture the bolt was mounted so the chain could flex up and down, rotate the bolt 90 degrees and the chain can flex in the direction we need to for the maslow. With a nut on each side of the mounting bracket (ideally a nylock nut long-term), the pivot points are going to be as solid as we can get them.



another approach (more suited to mass production) would be to change the mounting bracket. Instead of punching large holes in the bracket, punch a small hole (for the pin) and a U shape around it, then fold the tab out 90 degrees and hook the chain to it.

---

Posted on **2017-05-27 14:05:10** by **gero**:

Still the buffer overflow with a rather cleaned up file. Not at the same positions each time, seems more random then before. https://www.dropbox.com/s/z021gf27upstgcg/light3.nc?dl=0

---

Posted on **2017-05-27 15:26:30** by **gero**:

And in light4.nc (just changed the angeled tabs to 90 degree, just in case) the same. Running the file further it stopped with the sled not moving in real and not on the screen, but X and Y counting downwards and Z up and down by 0.1mm. Frozen at that stage.

---

Posted on **2017-05-27 15:35:45** by **Bar**:

I've got to rush off because my ride to he hardware store is here, but give the latest version a go. I think I've got the issue fixed.

---

Posted on **2017-05-27 15:47:32** by **davidlang**:

it looks like he created a new branch (buffer-over-flow-bug) bit didn't finish merging it into master

---

Posted on **2017-05-27 16:25:30** by **gero**:

It looks like the buffer overflow is gone, all circles went smooth. I had one more issue on the outer cut, but this seems to be related to something else. Perhaps a loose screw on the right motor sprocket. Strange noises there and ending to low suggests that.

Far beyond bed time and hard working day tomorrow leaves no time for investigation.

---

Posted on **2017-05-27 19:04:57** by **scottsm**:

The chain attachment to the sled need two degrees of freedom because the chain is not perfectly parallel to the work surface.

---

Posted on **2017-05-27 19:11:04** by **Bar**:

Great point. I think we should really work on making it perfectly parallel to the work surface, because ideally it would be.

---

Posted on **2017-05-27 19:39:56** by **scottsm**:

I think 'perfectly parallel' will need adjustable motor mounts and stiffeners to keep the work surface from bowing between the legs...

---

Posted on **2017-05-27 19:43:16** by **scottsm**:

@Bar, does the fix you mention above need both GC and the firmware updated? Which branch of firmware?

---

Posted on **2017-05-27 23:06:57** by **Bar**:

I believe it was just a GC issue, but it wouldn't hurt to update both

---

Posted on **2017-05-28 00:11:34** by **davidlang**:

@scottsm, there is some sideways flex to the chain, it should be enough for the +- 1 inch over a couple of feet. We should build it to be parallel when you have about 1.5" of material on the frame (3/4 backer board + 3/4 workpiece), with ~+-1 inch of play, you can handle down to 1/2" total or up to 2.5" total



and also remember, this is less important the further you are from the motors, so if you are pushing the the thickness,just avoid cutting in the upper corners.

---

Posted on **2017-05-28 00:12:39** by **davidlang**:

remember that the chain going over the sprockets doesn't have the second degree of freedom, so whatever you do is going to be flexing the chain from there. if it's 'hard mounted' to the sled, the sled is going to see the same amount of flex

---

Posted on **2017-05-28 08:44:32** by **scottsm**:

Good point about the sprocket end if the chain. It's because of skipping trouble I've had that I commented about the sled connection. The sprocket tooth shape gives a small amount of side play forgiveness, I wasn't sure whether the chain pinned to a fixed point would be as forgiving. I guess that might be a matter of looser tolerances when machining it. The fixed point does seem like a desirable thing, as small changes in that dimension make appreciable difference in the calibration process.

---

Posted on **2017-05-28 10:18:01** by **davidlang**:

I don't know if it will make a big difference, but it would be good to have someone test it , just in case it does. Even if we don't change everyone's kit, we can probably correct for this in other ways.

---

Posted on **2017-05-28 14:56:43** by **gero**:

[Lights](/images/6w/6wnm_lights.jpg.jpg) The workflow in FreeCad, designing and generating the G-Code seems to be my current choice. The final cut went well and the result is near to perfect. A little sanding and painting and my LED will shine nicly in my shelf. Thanks for the always incredibly fast support!

---

Posted on **2017-05-28 21:31:10** by **Bar**:

Thank you for giving me clearly defined problems to solve, and for taking our growing pains in stride!



I'm starting to accumulate a collection of other people's things as I do these test cuts. Just this weekend I got a copy of blsteinhauer88s sun moon sculpture and a copy of your shelf! :)

---

