## My Z Struggles
Posted on **2017-04-19 16:47:18** by **rancher**:

I thought I'd write this up a bit so others can maybe avoid these pitfalls.  I have been struggling with Z heights since day one.  I've been using Fusion360, and am new to every aspect of this process so I had a lot to learn there with regards to settings.  I'm not 100% sure I've got that completely sorted, but that's another topic.  For now I wanted to go over the things that have been tripping me up with any file.



First and foremost, the lack of down force on the router and resulting backlash.  Since adding the compression strap, things are so much better.  I could not figure out why I was never cutting all the way through, and the cuts seemed shallow and uneven in depth.



[DownZ1](//muut.com/u/maslowcnc/s2/:maslowcnc:KMkF:downz1.jpg.jpg)



 [DownZ2](//muut.com/u/maslowcnc/s2/:maslowcnc:4jyS:downz2.jpg.jpg) 



[DownZ3](//muut.com/u/maslowcnc/s2/:maslowcnc:PXbD:downz3.jpg.jpg) 



Secondly, and hopefully this is only me...the Z motor cap, the black plastic housing, is poorly attached if at all, and it has been continually working my connector out.  The attachment is opposite the router from me, so I often have been unaware that the z isn't working.  I have been wiggling it to make sure it's making contact, b ut now the cap is totally wonky and the connector won't stay clipped.  I've got it zip tied down and next comes the duct tape.  I'll tame it, for sure, but I'm telling you guys this to say, watch that connection.  Right when you build it, set up some strain relief and chafe protection and make sure that connector stays in.  Mine has been intermittent for a while now, and I only just figured it out. 



Lastly is operation.  Setting zero-z, then retracting the tool, then run the program.  I was not retracting and it would take off to the start point with the tool lightly in the material.  Then I'd panic and back it out, and usually get myself out of whack with regards to zero, due to the backlash.  So I was never in the wood on the first cut.  Geez that took a while to crack for such a simple problem!



Hope that helps you guys get right to it.

---

Posted on **2017-04-19 16:56:33** by **blsteinhauer88**:

I like the down pressure idea, have you notice the router heating with the vents covered?  Also that must be a Fusion thing.  I have been using Makercam and Easel, which both set a safety height for movement, even to the start point.  Can your design be made and saved as a .dmg or svg and open in these programs and the paths created?

---

Posted on **2017-04-19 17:05:41** by **rancher**:

I'm pretty sure Fusion has a safety height.  I'm just not quite all the way there yet and there are a lot of settings.  As I learn more though, I'm of the mind that may all have been due to the intermittent connection.



  No, I haven't noticed it running hot, but I haven't run the machine for any significant length of time.  I'll keep an eye on it, and maybe put some standoffs there if need be.  It makes an enormous difference on the cut.  Mine did, anyway.

---

Posted on **2017-04-19 17:15:00** by **blsteinhauer88**:

Yea! cut and arch that lifts it off and is held in place by the band.

---

Posted on **2017-04-19 18:02:47** by **scottsm**:

I really like your down-pressure idea, [here's my version](//muut.com/u/maslowcnc/s1/:maslowcnc:0rsY:fullsizerender.jpg.jpg). A piece of bungee cord folded and pulled through a ball fitting and held with a couple hog rings.

 I'm with you on the z-motor cap. If you look at my z-motor you'll see a strip of velcro cable-tie holding the cable to the motor body. This has kept the connector from coming loose, and when the cap gets popped off :( while fussing with the depth screw, at least it stays 'in the neighborhood'. I may tape the cap in place but haven't gotten around to that. I notice the velcro has climbed up to cover the motor's air hole, probably not good.

 Learning z-motor hygiene comes hard for me, I've got traverse gouges across most of the things I've done. Easel is good for taking care of this, it raises the cutter before traversing home at the end of a file:

G1 Z0.15000 F9.0

G0 X0.00000 Y0.00000

 I'm using inches there, so the cutter should be 0.15" above the surface, and thanks to your down-pressure idea, that's become reliable.

---

Posted on **2017-04-19 18:31:16** by **MakerMark**:

I like the z strap idea and will give it a try tomorrow. What are you all doing to keep tension on the outer ring to prevent x/y slop? I've got a rubberband on the clamp handle to the right router handle. It's held up to ~8hrs of cut time, but it's building up a lot of metal dust and has polished some areas close to a mirror reflection.

---

Posted on **2017-04-19 18:40:15** by **rancher**:

Mark, you can tighten the nut on the handle bolt and adjust how tight it is.  With the compression strap driving it downwards, I've got it pretty tight.  Enough that there isn't much appreciable xy slop.  



Scott, that bungee looks like a good solution.  I was looking for one of those but found the innertube first.  I'm also quite relieved to hear I'm not the only one fighting the connector.  I spent a lifetime wiring boats and I know how to wire stuff to stay put, so it bugged me that a loose connection was one of my issues.  Thank you for all of the validation that my issues aren't all me!

---

Posted on **2017-04-19 19:07:58** by **scottsm**:

@rancher, I've done a bit of wiring on boats, in a previous lifetime. This is neither yacht-grade nor mil-spec, but we gotta keep the connectors from coming adrift! I've got an inner-tube strap as well, but it didn't hold tight enough at the deepest plunge (I cut the holes too far apart :( )

---

Posted on **2017-04-20 04:38:03** by **MakerMark**:

@rancher - thanks! I'll try tightening the nut when I put the z bungee in place.

---

Posted on **2017-04-20 09:04:18** by **gero**:

@rancher, the Z motor cap is not only you. I had some strange Z issues, a combination of to shallow and to deep cuts and after putting the base on the table and moving Z in and out a hundred times I am convinced that it not my Z-spindle. Perhaps some 'Z-Position information' gets lost or messed up due to vibration and the connector. Can not confirm that, but trying to strap that thing down is a good tip. Thanks

---

Posted on **2017-04-20 09:57:44** by **Bar**:

That is important to know and sounds like an issue we should look into. Will you make an issue for it on GitHub and put in any information about when it happens and how you did the tests so I can try to track it down?

---

Posted on **2017-04-20 12:22:30** by **rancher**:

I've got two more causes of Z problems, after this morning's tests.



Check your coupler every now and then.  The set screws on mine had backed out, and this morning I was stymied again.  Again!



....and then once more!  If you run the Z all the way in the body of the router will decouple from the red worm gear button.  You will Z out and nothing happens.  Geez!  Hopefully that's the last one!



Bar, which issue are you referring to?  Most of mine were mechanical, with the biggest offender the poor connection at the motor and failing motor cap.

---

Posted on **2017-04-20 12:57:27** by **Bar**:

Really I'd say make an issue for anything anything you see that could be better.



The issue with the black cap coming off is something I'm working with the factory to improve, but having an issue for it would make sure it stays on the top of the todo list, and could be a place I could keep everyone informed about how that is going.



Running into the z all the way out in the body of the router and having it decouple seems like a purely mechanical issue, but I bet we could find a way to solve it. I'm thinking that when the z-axis is run all the way out to the end, the motor will have to work harder and slow down. Because we can monitor the speed of the motor we can probably detect that and pause it. Maybe show a message on the screen? 



What do you think?



I'd say whenever you have trouble with anything file an issue for it, if something annoys you, we should fix it.

---

Posted on **2017-04-20 13:06:26** by **rancher**:

Detecting an over value on the load would be useful at both ends of the worm gear, since I assume the gear is the red plastic button and it won't take much of that.  The router body coming off the transport is more user learning curve, I suspect.  I had a short bit and a deep cut.  Now I know, I would use a longer bit next time.  



The cap and connector are a problem for sure.  You will want to solve it somehow before you ship out 600 of them.  I know you want to do it for the users, but I am thinking as much for your sake.  It will be a giant headache if they all fall off and cause intermittent problems.  Maybe pre-connected at the motor with a tie wrap to the body and a dab of hot glue at the connector or cap, or...something.

---

Posted on **2017-04-20 13:15:38** by **scottsm**:

I've run my z-motor into the stops and chewed up the red plastic button. It really is a matter of learning to set up the router, a user education issue. Keeping the connector from coming off the motor seems like a Maslow issue, though. A cable tie to the motor mount?

---

Posted on **2017-04-20 13:19:42** by **blsteinhauer88**:

Just in case:



http://www.ereplacementparts.com/ridgid-r2200-heavy-duty-2hp-router-combo-kit-parts-c-7929_8182_167782.html

---

Posted on **2017-04-20 16:05:37** by **blsteinhauer88**:

This is what I've set up for Z pressure and the loose cap. [IMG_0668](//muut.com/u/maslowcnc/s3/:maslowcnc:pOlu:img_0668.jpg.jpg) [IMG_0669](//muut.com/u/maslowcnc/s3/:maslowcnc:rwO3:img_0669.jpg.jpg) [IMG_0670](//muut.com/u/maslowcnc/s3/:maslowcnc:NSVf:img_0670.jpg.jpg)

---

Posted on **2017-04-20 16:47:54** by **rancher**:

Those are both awesome solutions!  Thank you for those, my cap is in a bad way at this point.

---

Posted on **2017-04-21 00:46:29** by **davidlang**:

once you have the setscrews in place, put a drop of nail polish on them to keep them from vibrating loose (or use a weak threadlocker)

---

Posted on **2017-04-21 05:32:35** by **jwolter0**:

A few quick thoughts:

1. That replacement parts site should be on the wiki somewhere, if it's not already.  I might do it sometime if I remember, but I need to head to work now.

2. It took me looking at the pictures (thanks blsteinhauer88) to figure out that the "loose cap" really was a loose cap and not a loose capacitor.  Feeling a little sheepish...

---

Posted on **2017-04-21 07:45:39** by **scottsm**:

There are other sources for these parts, but it seems few keep them in stock. I ordered from two sources, received one order after a week, the other two weeks. At $0.90 each I figured I could afford to keep a few of these on hand especially since I was shut down without it and the lead time is _days_ (spoiled by modern times)...

---

Posted on **2017-04-21 07:47:02** by **scottsm**:

I had another z-runaway, loose z connector again. I was trying the approach of cable-tying the cable to the motor mount and didn't snug it down tight so the cable must have wiggled when the sled traversed. An up-spiral bit buried beyond the flukes and trying to cut at 20ips makes some impressive smoke and charred chips! The 'Stop' is my friend - should we make it red?

---

Posted on **2017-05-02 15:54:18** by **mcginniwa**:

After running the test shape on the temporary frame with the temporary sled successfully, I decided to go ahead and try setting up the Z-axis on the temporary sled (hopefully making cutting frame parts less work):



 [IMG_0370](//muut.com/u/maslowcnc/s3/:maslowcnc:PJCI:img_0370.jpg.jpg) 



Certainly a fiddly process with the small screws and bolts, but seemingly worked ok.



I tried re-running the test shape with the Z-axis kit installed and got unexpected results (only the initial diagonal was cut, i.e. the reverse of intent). I then figured that I need to "define zero" for the Z-axis.



I went through that process, but got the same result. The Z-axis mechanism works, but is doing adjustments in the opposite direction than I think the file dictates.



I'm using the `6 inch Square Test Shape - Quarter Inch Bit.nc` from the [zip download](https://github.com/MaslowCNC/Mechanics/blob/master/Gcode/All%20Gcode%20Files.zip).



I don't think the problem is mechanical. I think I'm missing a step or misunderstanding how to set up the Z-axis.



Any ideas?

---

Posted on **2017-05-02 16:15:06** by **rancher**:

I think you are the first non-Rigid router with Z.  Maybe it's threaded the opposite way?  That sounds like opposite behavior.

---

Posted on **2017-05-02 16:22:56** by **Bar**:

It sounds like maybe it needs to spin the opposite direction. That's something I can add to the software right away. 



If you want to lower the router does the knob turn clockwise or counter clockwise when viewed from the top?

---

Posted on **2017-05-02 16:26:14** by **davidlang**:

we do need a way to drive the motor either way for Z+



there are just too many different ways to hook a motor to a router to not have this as an option.



This could either be a software config option (probably the best option), or it could be a way to reverse wiring

---

Posted on **2017-05-02 16:32:36** by **Bar**:

I'm happy to make a software option for it. It is important. Would someone be willing to make a request for it on GitHub so I don't forget?

---

Posted on **2017-05-02 16:43:27** by **mcginniwa**:

> If you want to lower the router does the knob turn clockwise or counter clockwise when viewed from the top?



Lowering the router bit towards the material turns clockwise (right now, that's happening with "Z-Out" in Z-axis controls).



Raising it (right now, that's happening with "Z-in" in Z-axis controls), is counter clockwise.



So maybe I'm not going crazy!

---

Posted on **2017-05-02 16:50:33** by **Bar**:

Perfect! 



Thanks for the tip that we need a reverse direction. I'll hop on it.

---

Posted on **2017-05-02 16:52:07** by **davidlang**:

I added an issue for the motor direction and one for allowing motors to be plugged into any port

---

Posted on **2017-05-02 16:52:35** by **Bar**:

Perfect! Thank you.

---

Posted on **2017-05-02 16:55:52** by **mcginniwa**:

Actually I am also seeing something mechanical. There's a "macro adjustment lever" on the Bosch GOF 1600 CE fixed base that looks like it can slip when lowering the bit if there is too much resistance.



It's probably just an issue when the router isn't cutting. At least that is my hope ;)

---

Posted on **2017-05-02 18:02:29** by **davidlang**:

it looked like you have the base unlatched in the picture you posted. you should adjust the tension in the latch so that you can close the latch and move the router freely, but without noticeable play.

---

Posted on **2017-05-02 18:28:53** by **mcginniwa**:

I knew someone was going to catch that ;)



From the manual:



> Fixed Base Depth Adjustments

> To Adjust Depth

> Note: All depth adjustments must be made with base clamp lever released.

---

Posted on **2017-05-02 18:32:22** by **Bar**:

*Catch* that was that a pun? :-)

---

Posted on **2017-05-02 18:32:42** by **mcginniwa**:

So I take that to mean is that even fine depth adjustments (i.e. Z-axis shaft turning) require the base clamp lever to be released.

---

Posted on **2017-05-02 18:33:48** by **mcginniwa**:

> Catch that was that a pun?



Not intentional!

---

Posted on **2017-05-02 18:54:44** by **davidlang**:

@mcginniwa

Yes, the manual says that, but we are doing something unusual here. They say that because they need the clamp adjusted enough to keep it from moving at all (they can't count on the adjusting knob not turning). Since we have another mechanism to keep it from moving (the motor on the knob), we don't need the clamp that tight for safety reasons.



and with the clamp released, the router moves way too much, it will cause problems with what you are cutting (and may even damage things)



I'll bet that the manual also warns never to turn it on with the clamp open. :-)

---

Posted on **2017-05-02 20:12:25** by **mcginniwa**:

Ok, I'll give it a try and report back.

---

Posted on **2017-05-02 20:12:31** by **larry357**:

@mcginniwa Great work, I'm just glad that you could fit the z-axis o.k and great that this work is done before I get my non beta one. I turned the knob, and it did move it o.k up and down with the catch closed (not one to read to many manuals) but it did scratch the router motor a bit and seemed tight...

---

Posted on **2017-05-02 20:15:22** by **larry357**:

maybe an option is for a bungee tie down to keep it tight without the lock https://www.mitre10.co.nz/shop/number-8-3-piece-bungee-cord-set-220-x-185-x-15mm-assorted-colours/p/268001

---

Posted on **2017-05-02 20:26:10** by **davidlang**:

they all have an adjusting screw under the latch (you need to be able to adjust exactly how tight it is to hold the router tight under normal conditions), so you can just adjust it to be just the right tension. no need for a bungee cord or similar.

---

Posted on **2017-05-02 20:27:35** by **mcginniwa**:

@davidlang with base lever clamp locked, the motor will not move even if the Z-axis shaft turns. I tried with and without and measured the depth of the bit, etc. With base clamped locked, it's Z-axis is inoperable.



It's pretty sturdy with it open and there is a failsafe to keep motor from coming out of the base.

---

Posted on **2017-05-02 20:28:49** by **mcginniwa**:

> they all have an adjusting screw under the latch (you need to be able to adjust exactly how tight it is to hold the router tight under normal conditions), 



Ah, that's probably the trick. The lock is super tight right now, but I'll see if I can loosen it to allow Z-axis fine movement.

---

Posted on **2017-05-02 20:57:39** by **mcginniwa**:

@davidlang did another round of experiments. I loosened the set screw all the way out on the latch.



 [IMG_5594](//muut.com/u/maslowcnc/s3/:maslowcnc:ApGv:img_5594.jpg.jpg) 



Assuming that I'm adjusting the right thing (it's just to the right of the  upside down "Bosch" in the pic), even with it completely loose, the motor wouldn't move in the base although the Z-axis shaft then spun freely consistently.



I took the motor out to check the locking mechanism. The metal band that is pressed against the motor does push in more when that screw is tightened. I'm wondering if it's a matter of letting it wear in.

---

Posted on **2017-05-02 21:03:39** by **davidlang**:

there's usually a screw inside the latch itself, but you may be finding the right one. If you remove that screw entirely, does it still get too tight.



If the motor is too tight to move, the z screw should not be able to turn (as it would be trying to move the motor against the base), check that it hasn't popped out of position or something.

---

Posted on **2017-05-02 21:30:25** by **mcginniwa**:

With the screw all the way out it managed to raise the bit, but not lower it. Whereas with it unlatched it worked in both directions freely.



Right now I'm inclined to circle back to the mechanical problem after the software configuration stuff is in place so it will work with the Bosch. I still need to get on cutting the parts for the final frame. I'm supposed to demo this thing at Arduino day on Saturday!

---

Posted on **2017-05-02 21:42:31** by **larry357**:

I'll have a play this evening, with the base. But from reading it does look like you need it loose... Also do note "A small disadvantage with this is that it does Imperial measurements better than metric - a full turn is 3/16" or around 4.5 mm but only *close to* but not quite 4.5 mm."

---

Posted on **2017-05-02 21:47:44** by **mcginniwa**:

Cool @larry357. Appreciate another set of eyes.



By the way, where are you located in NZ?

---

Posted on **2017-05-03 13:58:50** by **mcginniwa**:

Just reporting back here that the software change boils down to [configuration change only](https://github.com/MaslowCNC/Firmware/issues/204#issuecomment-298963382).



Make the setting for Z-axis pitch a negative number.



Thanks @bar!



I'll experiment with this shortly and report back if there are any more issues.

---

Posted on **2017-05-03 15:59:13** by **mcginniwa**:

Changing `Z-axis Pitch` to negative value worked a treat.



I also experimented with pitch value and think that `-2` gives more accurate adjustments for the Bosch GOF 1600 CE fixed base.



In regards to the mechanical issue... I'm continuing with the base clamp lever unlocked for now. Keeping an eye on it.

---

Posted on **2017-05-03 16:24:02** by **mcginniwa**:

Another note. I've had some issues with run-away Z-axis adjustments using the Z-axis control box and with the Home button every now and then. Have to hit "Done" and then "Stop" and monkey with things to reset zero, etc.

---

Posted on **2017-05-03 16:32:50** by **Bar**:

Interesting and good to know.



Are there conditions which make that happen?



Do you want to see a "Stop" button in that window?

---

Posted on **2017-05-03 17:20:23** by **mcginniwa**:

> Do you want to see a “Stop” button in that window?



Maybe just that "Done" would stop current Z-axis operation.

---

Posted on **2017-05-03 17:21:54** by **mcginniwa**:

> Are there conditions which make that happen?



I'll take note next time it happens. The only thing that may recreate it is if the previous run was stopped early before I hit "Home".

---

Posted on **2017-05-04 04:25:53** by **larry357**:

@mcginniwa I'm in Hamilton. I had a further look, didn't have a fitting Alan key for the fixed base lock. But the movement is minimal so be interested to see how it cuts. Can always add a few pieces of electrical tape☺

---

Posted on **2017-05-04 14:17:54** by **mcginniwa**:

@larry357 cool, good to know another North Island Maslow person.



Sadly I got mixed results yesterday when cutting in regards to the Z-axis with the Bosch GOF 1600 CE fixed base with the base clamp lever open.



I'm a little worried that the design of Bosch fixed base has fundamental issues due to repeated slippage when trying to cut a depth more than 12mm (multiple 2mm or 3mm passes).



Essentially I see slippage when the Z-axis adjustment is moving on either far side of the depth macro adjustment position range. At least I think that is the deal.



@davidlang's point that the clamp needs to be locked in order to prevent this seems correct, except that then the motor doesn't move in the base at all in that case. Ugh.



I'm pretty bummed out at the moment. I was unable to make any forward progress on building the final frame yesterday. Had to pull out of doing at demo at local Arduino Day.



May not be able to get back to things for a few weeks.

---

Posted on **2017-05-04 16:32:28** by **mcginniwa**:

I also have the plunge base for the Bosch router and actually think its "Afterlock Microfine Depth Control" may make it a better option as a Z-axis compatible base for the GOF 1600 CE. The motor would stay fully secured in the base motor housing while the hosing is moved up and down relative to sled on the plunge arms.



The downside is that it looks to only have 15mm of possible depth range. Effectively that means only 10mm of depth since 5mm above the material would need to be reserved for "safe travel".



To get around the depth limitation for greater depths work, you would have to re-run cutting jobs where you adjust where 0 for the Z-axis is relative to the router and the material. Essentially you adjust the router so the last cut's depth becomes the new 0 point on the router plunge base.



I'm kind of hoping that I can eek out some more range once the knob is off the depth control shaft.



Anyway, worth experimenting with as I'm unhappy with what's going on with the fixed base.

---

Posted on **2017-05-04 16:49:36** by **larry357**:

What do you mean it slips? As it is locked in one of the 3 holes on the router motor. Maybe do what someone else did and put a inner bike tube over the top of it to pull it towards the work...

---

Posted on **2017-05-04 16:50:38** by **larry357**:

picture in the first post of this thread...

---

Posted on **2017-05-04 16:50:50** by **mcginniwa**:

@larry357 it seems to want to slip out of whichever 1 of those holes it's been set it when it gets to the far side of its range.

---

Posted on **2017-05-04 16:59:13** by **davidlang**:

I don't understand what hole it is popping out of, can you post a new picture and identify what hole you are talking obout

---

Posted on **2017-05-04 16:59:19** by **mcginniwa**:

It's possible that 15mm is also the Z-axis range variance between the 3 macro settings on the fixed base and that by pushing beyond that, I've triggered the slipping.



Very hard to explain in text and I'm not up for running through and video things over and over right now.

---

Posted on **2017-05-04 17:03:05** by **mcginniwa**:

@davidlang the "macro lever" clicks into 1 or 3 holes on the motor.



 [IMG_5595](//muut.com/u/maslowcnc/s3/:maslowcnc:hYRu:img_5595.jpg.jpg) [IMG_5596](//muut.com/u/maslowcnc/s3/:maslowcnc:he9x:img_5596.jpg.jpg)

---

Posted on **2017-05-04 17:08:32** by **larry357**:

No not 15mm, it has a large adjustment... maybe tie it back/ or prop something underneath some how, so it cant come loose @davidlang here is a vid of the outside of it https://youtu.be/1QeRpzKfnTo?t=154

---

Posted on **2017-05-04 17:14:08** by **larry357**:

40mm adjustment should be possible https://youtu.be/EPyka70p96E?t=152

---

Posted on **2017-05-04 17:39:15** by **davidlang**:

with the router out, how much movement does that latch have?

---

Posted on **2017-05-04 17:47:39** by **mcginniwa**:

I'm going to have to come back to this later. Sorry guys. Maybe we can set up vid call sometime to work together on it. Hard going for me as someone not familiar with routers generally.

---

Posted on **2017-05-04 17:48:34** by **davidlang**:

that second video does say that the fixed base should have 1 5/8 of adjustment available (in the documentation, look for router table adjustments)

---

Posted on **2017-05-05 02:43:55** by **larry357**:

@mcginniwa I saw what happens, but only when the base comes close to the router motor edge where it tappers out. So the hole closest to the spindle, works best. Then you have about 35mm up and down.

---

Posted on **2017-05-06 16:33:18** by **mcginniwa**:

@larry357 - yeah, looking better. Still in process of trying deeper cuts, will let you know how it goes.



Two key things on top of using the first macro setting (hole closest to the spindle) from what I'm seeing so far:



1. set up the fine depth adjustment mark on the "macro depth adjustment lever" about 10-15mm from the top of the threads when setting motor position in the base

2. your bit shaft length and its placement in the collet need to be set with the cutting depth in mind relative to 0 point of Z-axis (duh) - so when fine depth adjustment mark is 10-15mm from top, your bit should be flush with bottom of sled



Another tweak, judging by the manual, the correct Z-axis pitch is `-1.5` rather than `-2`.

---

Posted on **2017-05-06 21:43:14** by **mcginniwa**:

Moved to [Bosch GOF 1600 CE specific discussion](http://www.maslowcnc.com/forums/#!/hardware-issues:bosch-gof-1600-ce-z-axisde).

---

