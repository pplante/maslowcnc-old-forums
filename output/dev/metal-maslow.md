## Metal Maslow
Posted on *2017-04-13 08:19:24* by *mexicomillionaire*

First Post, really excited to start dedicating a lot more time to this forum and the wiki. 

I have been working with my kit for the past 2 weeks and I finally have some time to share my progress.

As the title suggest, I chose to build a steel frame for the machine. 

Here is my album for my build pictures. Be kind, my welding is amateur... 

https://goo.gl/photos/B7pDkbsW3Yrk9vYK9

The main reason for steel is that I live in Mexico and getting steel is much easier. I also wanted to explore how accurate I can make this machine. I understand that I could never expect the accuracy of my other, smaller machine but, I want to see how close I can get. 

I think that getting a rigid frame is the first step. 

Currently, it is very rigid and this weekend should be the first cut tests. 

This will hopefully provide a baseline for the machine with the frame stiffness error reduced.  

If more technical details are needed, I can provide them.
 
Open to suggestions and will be back to update after the first real trials. 

  [Metal Maslow Frame](//muut.com/u/maslowcnc/s3/:maslowcnc:LtY4:metalmaslowframe.jpg.jpg)

---

Posted on *2017-04-13 08:42:12* by *davidlang*

I suspect that you want to get it up off the ground a bit (clearance for the sled and easier to position material), and I would suggest making the lower ledge out of wood so you don't damage your bit if you run into it

beyond that, let's see how it works. The maslow has the theoretical potential to be pretty accurate, it will be good to have people pushing it to it's limits :-)

The maslow has a theoretical accuracy of about half a thousandth of an inch in the length of each chain, the inaccuracy comes from droop in the chain, how accurate the machine dimenstions are measured, how much the sled sticks vs slides (and sways like a pendulum)

---

Posted on *2017-04-13 10:00:47* by *Bar*

That looks amazing! Very cool design. I really like how you mounted the motors parallel to the arms. I think it's aesthetically pleasing and keeps things simple. I'm embarrassed to say this but it hadn't occurred to me that you can rotate the motors any way you want. 

I'm very interested to see what kind of accuracy you can hit. Keep in mind that at least for the next few weeks the accuracy limits will probably come from the software. Like @davidlang said the theoretical positioning accuracy is less than a thousandth of an inch. I added test to the latest version of Ground Control which measures how close to perfect the tracking system is working because as I'm starting to improve it I want to be able to track my progress. I'm seeing an average of about 1mm of error right now which is massive. I'd like to see that error go away in the next few weeks.

What a beautiful solid frame! Thank you for sharing. Keep us posted as you progress.

---

Posted on *2017-04-13 10:06:58* by *davidlang*

@bar, I'm really looking forward to finding out how the new double pid loop controller setup changes things. I think you are correct in thinking that it will make a big difference.

---

Posted on *2017-04-13 10:52:47* by *mexicomillionaire*

@davidlang 
I am planning on adding legs on the bottom to get it off the floor. The wooden lip on the bottom is a good idea.

However, I am trying to figure out how to make the table angle adjustable. I am deciding between two options. 

From the information I have found, 15 degrees is the current design. Interested to see how the angle can effect the cutting accuracy. 

Currently, I am leaning to the towards the second option. I do not think I am going to need more then +/-5 degrees.

However, the first option allows for the legs to fold and store the machine more easily.

 [Frame Legs option 1](//muut.com/u/maslowcnc/s2/:maslowcnc:1eHZ:framelegsoption1.png.jpg)  [Frame Legs option 2](//muut.com/u/maslowcnc/s1/:maslowcnc:viS9:framelegsoption2.png.jpg)

---

Posted on *2017-04-13 10:57:01* by *Bar*

Those booth look like great options.

---

Posted on *2017-04-13 11:01:05* by *rexklein*

That is just cool. I also never considered the motors could be at any angle.. And uhhmm so I have a couple of things needing some weldin...:)

---

Posted on *2017-04-13 11:11:34* by *scottsm*

In order to cut to the edge of a sheet, the sled needs to be supported beyond the edge of the sheet for at least the distance measured as 'center of gravity'. I plan to use a piece of scrap that matches the thickness of the sheet to support the sheet. This makes the frame legs stick out in front a bit, but makes a larger flat area for the sled to work on.

---

Posted on *2017-04-13 13:16:54* by *rollandelliott*

LOVE it , I might make my frame out of aluminum. Originally thought Aluminum would make it light enough to move around, but with how heavy mdf is, will need wheels no matter what. and lets face it. I'll probably never move it, lol.

---

Posted on *2017-04-13 18:06:08* by *davidlang*

I would go with option 2, but bolt the back legs on instead of welding them. That way if you find that you want to go steeper, it's easy to drill another hold and change them (and just put a clamp on the joint at the bottom when experimenting), the slot for adjustment on option 1 is overkill. It's a lot of work to make and you aren't going to be adjusting it all the time, just during the initial experimentation period.

---

Posted on *2017-04-23 18:09:38* by *mexicomillionaire*

Got some more time to work on the frame. 

I was able to get the legs/stand completed. I went with option 2 and I will be adding the adjustable feet soon.

Still no cuts but, that should change this weekend.

I have added the pictures to the album. 

goo.gl/photos/B7pDkbsW3Yrk9vYK9

Here is the frame standing on its own. 

 [Metal Maslow Frame standing](//muut.com/u/maslowcnc/s3/:maslowcnc:UA6n:metalmaslowframestanding.jpg.jpg)

---

Posted on *2017-04-23 21:34:30* by *rollandelliott*

Awesome!

---

Posted on *2017-04-23 22:08:01* by *gero*

Nice!

---

Posted on *2017-05-01 19:05:47* by *mexicomillionaire*

Update: The Metal maslow is making dust!

I created the sled on my other desktop CNC machine (10x10 inch work area).  I inset the router plate into the 3/4 plywood. I was only able to place the countersunk holes and router plate. The goal will be to cut the real sled with the maslow and finish it in my smaller CNC.

I attached the video timelapse for those interested.

https://youtu.be/m4XUZWieuM8

I also installed the Z-axis to the sled and got that working. Pictures have been added to the album.

goo.gl/photos/B7pDkbsW3Yrk9vYK9

After stomping on some gremlins with the new GC update (Thanks @Bar), I was able to start testing. 

I couldn't wait to try it out so, just verifying my motor spacing (130.75 in), I set about to cut the test shape. The test square was 5.9 wide and 6.1 tall. So I am seeing come distortion but, I am attributing this to not measuring the CG and hanging point distance.

Super happy with the result. 

Now onto fine tuning and cutting out some projects. I think it would be great to create a "tuning guide" based on the most recent discussions. 
 
 [Hangingsled](//muut.com/u/maslowcnc/s1/:maslowcnc:q23G:hangingsled.png.jpg)  [Testshape](//muut.com/u/maslowcnc/s1/:maslowcnc:jLoP:testshape.png.jpg)  [Router plate](//muut.com/u/maslowcnc/s1/:maslowcnc:Oc8Z:routerplate.png.jpg)

---

Posted on *2017-05-01 21:43:01* by *Bar*

Beautiful! Thanks for the update. I'm working on automating the tuning process based on all the techniques laid out in the forums so that we can all follow the same process to get things dialed in. Fingers crossed I'll have something to show by the Wednesday update.

That looks like a beautiful build. The recessed router plate is slick. <-groan

Keep us posted!

---

Posted on *2017-05-02 09:20:24* by *gero*

What a great idea to sink the router in the plate. Sorry, I need to copy that :-). Will give me some extra mm of Z depth. Thanks for sharing!

---

Posted on *2017-05-02 10:43:15* by *davidlang*

you may not need to use the router plate at all. Initially the design was to use it as it is a slick surface, but it's small compared to the sled, and if it sticks out at all it becomes the surfact things ride on rather than the sled.

---

Posted on *2017-05-02 10:44:09* by *Bar*

@davidlang is right, I don't use the router plate at all. Having it recessed does give a nice slick surface to slide on.

---

