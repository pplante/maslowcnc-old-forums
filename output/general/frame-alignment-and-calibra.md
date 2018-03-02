## Frame alignment and calibration.
Posted on **2017-03-15 09:03:12** by **jbarchuk**:

I took a quote from the double sided cutting thread because it's a different topic.
>TheRiflesSpiral2h!
>The only risk you run with just one hole is that the plane against which your workpiece rests (the board at the bottom) may not be aligned with the same plane in the drive system of Maslow.
The support board / kickplate NEEDS to be PARALLEL to a horizontal line drawn between the centers of the motor axles!! Without that there will be yucky variables that the GC could take into account, but an accurate build should make that unnecessary.
There's been mention of an assembly doc that includes calibration, but nothing specific. Maybe that will take all this into account.
I would gauge everything off the bottom edge of the support board that's fastened to the main structure plywood sheet. That in itself should be as level-level as possible to avoid further inaccuracies.
After assembly of all the wood for -one- rabbit ear, but not the motors themselves, measure the distance from the bottom edge of the kickplate to the top of the motor mounting plate. attach the other rabbit  ear with clamps, and fudge that mount around till the top of that other motor mount plate is exactly-exactly the same dimension as the first one. Lastly drill the holes that fasten the second rabbit ear to the main plywood.
That should achieve a level and parallel workspace.
If there later turns out to be slight inaccuracies, that can be adjusted by adding a shim between the motor bracket and the motor mount plate. (Model aircraft plywood is available at hobby shops down to 1/64", or very thin sheet metal works too.)

---

Posted on **2017-03-15 09:18:00** by **TheRiflesSpiral**:

> @jbarchuk
> I would gauge everything off the bottom edge of the support board that's fastened to the main structure plywood sheet.

That alignment is in the real world. The work Maslow does is in the software realm.

It's common for CNC machines to cut their own scales and alignment marks for this reason. No matter how well, mechanically, your device is set up, there's always the variable of how commands in software get translated to the real world.

---

Posted on **2017-03-15 10:43:30** by **jbarchuk**:

> @TheRiflesSpiral
> No matter how well, mechanically, your device is set up, there's always the variable of how commands in software get translated to the real world.
Mmmm... not in the sense of repeatability.  Meaning for the same input makercam or whatever should always produce the same output. Makercam and another g-code generator might not (will almost never) produce the same g-code. -That's- a factor one should keep in mind when trying different software.
There are physical variables such as backlash and wood expansion/contraction, but on the digital side, for software (data/program,) a 1 is always a 1 and a 0 always a 0. (Yeah there are software updates/upgrades that might cause g-code variations that might have obscure unforeseen accuracy consequences but that's a different issue.)

---

Posted on **2017-03-15 10:51:13** by **davidlang**:

@jbarchuk, remember that the motors are analog, not digital

as for the bottom being aligned, it should be possible to have the maslow trim that edge to make it square as far as it's concerned.

---

Posted on **2017-03-15 10:51:19** by **TheRiflesSpiral**:

The digital asset may not change from cut to cut but in that case (milling both sides of a sheet) the workpiece is changing. That makes the relationship of the workpiece to the workspace (in digital space) relevant.

---

Posted on **2017-03-15 10:52:10** by **TheRiflesSpiral**:

I like that Idea, David. A nice tall bit that could mill the 2x4 flat and also maybe a couple of registration "bumps"?

---

Posted on **2017-03-15 10:53:20** by **davidlang**:

you just may have to attach a board a little higher to give the sled enough stability.

---

Posted on **2017-03-15 11:28:17** by **jbarchuk**:

> @davidlang
> @jbarchuk, remember that the motors are analog, not digital

Of course. I'm talking about the time the object to be cut exists in purely digital format. But even after that the encoder sends a digital representation of the analog position back to the GC. The motor/encoder has an accuracy rating. The GC has to operate at a higher resolution (sampling theorem) than the encoder to assure that that inaccuracy doesn't creep back to the digital side. After that all the real world inaccuracies add up to the total inaccuracy. Holding the frame and force-transmission design as -tight- as possible at -every- point

> as for the bottom being aligned, it should be possible to have the maslow trim that edge to make it square as far as it's concerned.

That's doable but being in the real world there will still be -future- inaccuracies. Temperature and humidity will stretch and shrink the wood. Dropping 60# weights on it will compress the milled edge, or even stretch bolt holes or deform screw thread holes, and it shifts a fraction. Again I'm not talking about one-off pi eces, but repeatability over time.
Milling would be great for initial setup but I think a good stabilisation and strength point would be to fasten that bottom board at least every foot and 8" or 6" would be better. It's not hard to find points where highest accuracies and strongest attachments yield the longest term stability.

---

Posted on **2017-03-15 11:39:13** by **davidlang**:

I'm not sure what you are fastening the bottom board to in your efforts to make it so stable. My understanding it that it attaches to the legs, and possibly the back.

remember, this is made out of wood, and wood expands and contracts with humidity changes. If you try to make things too ridged you will just result in the wood breaking.

the plywood panels that you are going to be buying are not that precise/consistent in their dimensions. They will vary by up to 1/4" on a routine basis and the edges are not going to be square.

The best plan is to try not to go all the way to the edge of the panel, and then the exact angle/dimension/etc of the panel doesn't matter nearly as much.

---

Posted on **2017-03-15 12:46:44** by **scottsm**:

I've been wondering about a pattern of registration marks like those used for pick-and-place pc-board manufacturing. Something I could add to the beginning of a design that would take the router to enough known locations (2? 3? 4?) that I'll feel confident enough to let it go on with the cutting. If it pierced the sheet, it would confirm alignment when the sheet is flipped. Or perhaps a cut 3/5 of the way through - when cut from the other side any offset would show up.

---

Posted on **2017-03-15 13:00:08** by **davidlang**:

cutting all the way through and lining the router bit up with the hole is a pretty practical option, but it's not going to be accurate to 1/64", cutting 3/5 of the way through from both sides is a good way to see if you can notice any difference. A difference that you can only see with a micrometer isn't going to matter.

---

Posted on **2017-03-15 15:25:23** by **jbarchuk**:

> @davidlang
> I'm not sure what you are fastening the bottom board to in your efforts to make it so stable. My understanding it that it attaches to the legs, and possibly the back.

I misremembered. I had it in my head that the frame ply sheet was -between- the bottom horizontal 2x4 and the a-frames behind the plywood. Of course that's wrong. There is no direct connection between the plywood sheet and the 2x4.

The exact distance between the material support and the motors is less important than that they be parallel. A misaligned car front end makes itself known very quickly.

> The best plan is to try not to go all the way to the edge of the panel, and then the exact angle/dimension/etc of the panel doesn't matter nearly as much.

That was a topic early on in the KS chats. Many -will- go to the edge and past it. To the edge is speced. Beyond that is on the craftsman's/experimenter's mental and emotional dime. ;) It's up to the user to make sure that the raw material is accurate enough, and not 1/4" short that they need. :(
As you said, the easy answer to accuracy past  the edge to that is to make the rabbit ears a little taller and wider. Only a few inches (% points) should make a big difference in accuracy near and past the edge.

---

Posted on **2017-03-15 15:54:19** by **jbarchuk**:

> @scottsm
> I've been wondering about a pattern of registration marks like those used for pick-and-place pc-board manufacturing. Something I could add to the beginning of a design that would take the router to enough known locations (2? 3? 4?) that I'll feel confident enough to let it go on with the cutting. If it pierced the sheet, it would confirm alignment when the sheet is flipped. Or perhaps a cut 3/5 of the way through – when cut from the other side any offset would show up.
The best pick-n-place machines use vision systems because they're accurate down to 0.00x". Expense and a bunch of software but doable.
The 3/5 thing is nice but a major PITA if the only available space for test holes require climbing a ladder and leaning over to inspect the inside wall of a hole. I know I'm exaggerating, just put the test holes in a more accessible area and be done with it, but given enough time the extremely unlikely becomes absolutely guaranteed to happen to someone.
But those two thoughts, vision and test holes, clicked an idea for me.
The vision system uses a flow of move,  'look,' verify, adjust, and repeat till the error is below an acceptable level.
This could be done manually with a -few- test holes, and eye/ear calibration.
On the first cut side add a row or array of holes. Larger holes such as 1/4" or 3/8" would be easiest, but it should be doable at 1/8".
Flip the board, and manually locate and align the router over the first test hole, tell the GC that 'this is 0, 0,' and do a hole straight in and out. The sound of the cut and sight of sawdust will tell that it obviously didn't drill on enter, because it's cutting new wood.
The trick is to decide WHICH WAY to move the router to find the center. Never having seen this done I'd -guess- that the sawdust should pop up from the hole on the side that's being cut, and that is the direction that the router is off. So, the router must be moved a few ticks in the opposite direction.
The next trick is to decide how far to move it. That'll be based on experience and practice. One could learn a lot by doing practice drills. First, drill a hole, then don't flip the board, but move the router a few ticks and drill again. Then twice as many ticks as the first move. That second cut will remove a lot more material, and look and sound different. On a real workpiece, after the flip, and first test hole 'redrill,' the user will get used to how it behaves and have a good idea whether to move it 0.01" or 0.05*, and in which direction.
Set that new adjusted point as the origin, and tell the machine to redrill the next hole. The material from that redrill -should- be less, because it should be more accurate. If the dust comes out the same side then further adjustment in the same direction is required. If material comes out the other side then the first adjustment overcorrected. Lather, rinse, and repeat till with each redrill very minimal material comes out evenly all around. (No redrill will ever not remove any new material because even as the drill exits the hole the wood fibers are already moving around and relaxing after the assault by the drill/router.)

---

Posted on **2017-03-15 16:16:23** by **scottsm**:

I think I remember someone in the forum had a link to a pen that would chuck up into a router. Haven't found the link, but I want to get one of those and play around that way before chewing up too very much 'good wood'.
Much food for thought, a lot to look forward to.

---

Posted on **2017-03-15 16:20:34** by **scottsm**:

I just found Bar's link about the pen:
http://www.maslowcnc.com/forums/#!/modifications:pen-plotter/you-might-be-interested-in

---

