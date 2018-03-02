## My Maslow is up and running!
Posted on **2017-03-27 23:03:13** by **jessbussert**:

This is a photo of my first g-code run using a sharpie for a router bit.  Hey!  I don't wanna waste wood while I'm tweaking things, right?  https://imagebin.ca/v/3H5RMCHXBJAc



My machine looks a lot different from Bar's and so a little explanation might be in order.  Before Bar sent out the beta test kits I had already started hacking on the design.  I'm like that, ok?  https://imagebin.ca/v/3H5Rnz6K52xC



First off, I wanted my machine to be totally independent from the frame so that I could take the router, sled, electronics, and motors off the frame and pack them away in a reasonably sized package.  I wanted something that I could put in checked luggage or ship via UPS.  The reason for this is that I would like to be able to take the Maslow with me the next time I take a mission trip.  The last time I went somewhere (Haiti, after the earthquake) it would have been wonderful to have a tool like Maslow to help with the relief efforts.  Having everything together on the sled makes this a possibility.



Another reason I redesigned the sled was because I spend about 11 month s of the year traveling around the US in a big 'ol motor home.  I'm working as a traveling emergency room nurse and I take short-term contracts at hospitals around the country.  As such, I don't have a garage or much space to spread out while I'm on the road.  Having the Maslow reduced to a smaller, portable package just makes it easier for me to play with it when I'm away from home.



I also wanted to change the geometry of the machine to bring the math back to a simple trig function.  I was worried that the original design allowed for some unwanted torques since the router descends below the focal point of the chain triangle.  Now, to his credit, Bar has implemented some amazing black magic code to overcome this issue.  I was just hoping that if I went back to a basic triangle I could increase the cut rate without sacrificing precision.  In order to accomplish this I used two 12 inch diameter circular bearing races (http://www.rockler.com/low-profile-lazy-susans) mounted so they were each centered on the router bit.  I mounted the motors to these, each to its own bearing.  This setup allows each motor to swing around the router bit independent of the other motor.  It still remains to be seen it this will work or was just a lot of effort for minimal benefit.  



Finally, I added a heavy cardboard form used for casting concrete pillars.  This sits inside the bearing races and surrounds the router.  The purpose of the tube is to help keep the dust out of my bearing races, to provide an enclosed volume to eventually incorporate a vacuum assisted dust collection system, and to reduce the operating noise.  I'll undoubtedly need to provide additional dust protection for the races but I hope this will be a good start.



The problems I've experienced so far are numerous and pretty frustrating.  I'll highlight a few of the major ones below.



First off, I chose cheap bearings and they are not working as well as I'd like.  They don't turn as smoothly as they should, in part because they were designed for horizontal installation and I'm using them vertically.  Also, they are just stamped and formed sheet metal with a bunch of ball bearing in them.  Not exactly what you would call precision equipment!  I guess you get what you pay for.  My next revision will undoubtedly need to address this.



Next, I'm having issues with too much friction between the sled and the work piece.  I have a few plans to address this issue.  I'm planning on using a different material to face off the bottom of the sled.  I'd like to find something with a lower coefficient of friction than the current wood-on-wood.  I might try an acrylic sheet or maybe a Delran cutting board I pick up from the Dollar Store.  I'm also planning on routing a quarter round fillet on all leading edges on the bottom of the sled.  Finally, I'm going to remove most of the material from the interior of this slippery facing, leaving just a minimal circumference to maintain contact between the sled and the work piece.



Another factor contributing to the friction problem is the way my chain is currently attached.  The chain -should- pull parallel to the plane of the work piece.  Mine currently isn't.  On one end the chain goes around my motors at a height about 5 inches above the work piece.  The other end is only about 1 inch above this plane.  I didn't think this would make much of a difference but it does.  Upward travel tends to pull the top edge of the sled into the work piece, suspending the following edge by as much as a half inch.  Downward travel takes up this suspension adding unwanted backlash.  And of course this would all play hell with my eventual Z axis implementation.



I'm having some distortion of my dimensions as evidenced by the scrunched image I produced from Bar's test g-code file.  Also, the horizontal I drew thru the origin ended up being an arc instead of a line.  I'm sure these are just calibration issues that will be resolved by better measuring of my dimensions and rechecking the associated constants in the code.  Or, at least I hope this will resolve it!



There were a few other less important issues that I stumbled over but I'll stop where I'm at for now.  It's been a long day!  That said, any of you who are interested in modding your Maslow in a similar fashion are welcome to contact me.  Also, if you have any ideas for improvements on this design I'd love to hear them.



Ciao for now,

-Jessica

---

Posted on **2017-03-28 06:19:34** by **jknox**:

This is really, really interesting. Are your motors mounted on the sled!?! It's an awesome idea to make the entire machine self contained and portable! Can you describe or take a picture of how your chains are attached/routed. I'm having a hard time seeing how this works.



Those 'lazy-susan' bearings only work in a horizontal orientation with a vertical load. It may be hard to find something that's not too expensive that's large enough to fit and can take that side load and still roll smoothly, but I'll look around. I've also been thinking about rotating attachment points. I have an idea to keep everything in the same plane but I'm pretty sure friction is going to be a big problem.

---

Posted on **2017-03-28 08:30:02** by **mindeye**:

This is fantastic! Would love to see more images and maybe a video of it in action when you get a chance. I've had good success using a cutting board cut with a nice radius edge attached to my plywood sled with carpet tape.

---

Posted on **2017-03-28 08:58:11** by **rancher**:

Very cool design!

---

Posted on **2017-03-28 09:06:25** by **jknox**:

Jess, you may not want to remove the material from the interior of the sled plate, it would cause problems when cutting near the edges of a sheet (when the sled is hanging over the edge/corner)



FYI, this is the general idea for rotating sled attachment points that I've been thinking about.  The only way this would have a chance of working as currently drawn is if all pieces were HDPE (or similar): [Rotating sled concept](../../images/qT/lG/qTlG_rotatingsledconcept.png.jpg)

---

Posted on **2017-03-28 12:13:48** by **larry357**:

If you can incorporate rollerblade bearings they work well at angles with a load of weight I.e me 😀

---

Posted on **2017-03-28 13:24:31** by **jknox**:

Larry, great idea!  [Rotating sled concept2](../../images/AY/U3/AYU3_rotatingsledconcept2.png.jpg)

---

Posted on **2017-03-28 14:07:53** by **jessbussert**:

So a few of you asked for more photos on my build.



This first image is the basic structure of the sled:

https://imagebin.ca/v/3H9dEpkowJJy

The bottom layer is a tombstone shaped sled, 16" tall and 12" wide, cut from 3/4" ply.

The next layer is a 12" circular bearing.

The middle layer is paddle shaped, 12" OD x 9" ID, also cut from 3/4" ply.

Next is another circular bearing like the previous one.

The top layer, which you can see best, is the same as the middle layer.



The handles of the paddle pieces are for my motors to mount on.

The base of the tombstone is for electronics and my bricks.

And, of course, the router mounts to the center of the circles.



With this design the force vectors should point directly from the router bit to the chain mounting points at the top of my cutting frame.  That is, as long as my bearings turn smoothly.  Also, I made another slight mistake that you don't have to.  I mounted my motors with the shaft centered on the paddle handles but I think I should have mounted them so that the tangent of the sprocket was in the center instead.  Live and  learn.



The next image is my chain and sprocket housing.

https://imagebin.ca/v/3H9jRnZhbXjZ

This piece is laser cut from 1/4" ply and glued together as a unit.  This is the design I am currently using but after spending a lot of time screwing with it I'm going to revise it to something much simpler in the future.  I'll first explain what I've done currently and then discuss my future plans.



So, when you laser cut thin wood the edges get pretty charred up.  My first effort was made only from wood and it didn't work at all.  The chain moves with such force that when it spalled up it just dug into the wood, tearing it to pieces.  My next effort used a thin shim of aluminum cut from a Pepsi can to hopefully keep the chain from spalling.  This also failed miserably.  The shim was mauled up by the chain like wet tissue paper!  Next, I went to an aluminum U channel that I cut and shaped with a Dremel tool.  Here is a picture:

https://imagebin.ca/v/3H9mL0n55dcU

Even this took a lot of tweaking before I got it up and running.  This is what I'm using currently and here is a final photo of the results:

https://imagebin.ca/v/3H9nEH4UaJdv

The black stuff between the aluminum and the wood is JB Weld epoxy.  I used drywall screws to adjust the positioning of the channel before squirting in the epoxy in order to make sure my placement was correct.  Here is a photo of that process complete with the clamps I used and the drywall screws for shims:

https://imagebin.ca/v/3H9oT51MwE0F



As I said above, this is the process I am currently using.  It works, but I'm not fully happy with it for a few reasons.  First, it's overly complicated.  Second, it introduces friction between the chain and the aluminum channel.  This friction will eventually wear the channel away.  Finally, even this design occasionally allows the chain to spall up when first loading the chain in place.  This is a royal pain in the keaster when it happens because I need to disassemble a bunch of stuff to free it up.  Luckily, I don't need to load the chain very often.



The design I will try next will be much simpler.  I'm planning on placing free spinning sprockets on standoffs and positioning them such that they bump tooth-to-tooth with my drive sprocket.  This should keep the chain in place without all the issues that the channel introduced.  Hindsight is 20-20.



That's all I can post for now.  My partner and I have an art fair we are attending this coming weekend and we need to get ready for the opening.  We do photography and one of the first projects I hope to build with my Maslow is a very large format wet plate camera for doing ambrotypes.  Wish me luck!



-Jessica

---

Posted on **2017-03-28 14:49:06** by **davidlang**:

when using chains on traditional CNC machines, it's common to use three sprockets, one for the motot, and then two that are tangential to the straight-line chain position (like an upside down T) this ensures good chain wrap around the sprocket and low drag.



an idler sprocket to ensure a good wrap around the drive sprocket should work well (you should be able to get at least a 50% wrap around the drive sprocket)



This also gets to what my biggest concern with your design is, what happens to the slack chain? dropping to the ground right below the router will quickly accumulate sawdust in the chain.



If you loop the chains around the motor sprockets and then hook them back up to the corners with some sort of mild tension, you will get good wraps around the sprocket and have at least a chance of the chain staying out of the sawdust. Too much tension will be a problem (if it causes slack in the main chain length).

---

Posted on **2017-03-28 15:02:47** by **jknox**:

Nice, this is a really creative design, I like it. I agree that the idler sprockets will be a much more elegant solution, and should be less prone to wear and jambs. David, is this the type of sprocket layout you're talking about: [Chain wrap](../../images/Q6/vW/Q6vW_chainwrap.png.jpg) ?

---

Posted on **2017-03-28 15:15:39** by **davidlang**:

yes, that gives you the most possible wrap. You may be able to eliminate one of the idlers in this case as the arm rotates to stay aligned.

---

Posted on **2017-03-28 16:11:32** by **jessbussert**:

Yeah, the idler is a much better solution.  I'll work on that when I get back from the art fair.



My idea for the slack chain issue was to craft a magazine that would hang off the exit ports to collect the output side of the chain.  If you look at the second photo in the original post I made you will see little pips on the sides of my motor mounts.  I was going to use these to hang the magazines.  I would make the magazines from two pieces of masonite or 1/4" ply separated by a little more than the width of the chain.  This would allow the chain to drop down and stack on itself without overlapping and getting kinked up.



Since I'm dealing with big bearings, dust collection is an important issue that I think I'll have covered with my current setup.  If so, I may not need to worry about this too much.  Perhaps I could just attach little brushes at the output opening to kinda sweep things clean.



One other possibility that I'm toying with is a little out there.  Tell me what you think of this:



When I redesign the bearings I was thinking of ways I could create an air bearin g.  This would give me a self cleaning, near frictionless bearing assembly for my motor mounts.  It would also require a small compressor to make it work.  I could port my exhaust from the air bearing over the chain to help keep it free of dust.  I'm not sure if I want to go to the trouble/cost of adding a small compressor, but an air bearing would sure be cool!

---

Posted on **2017-03-28 16:20:03** by **jessbussert**:

@jknox:  in regard to removing the material from the bottom of the sled:



You bring up a good point about catching on the edge of the work piece.  In my case I have created a frame with a 6" lip around the periphery to hold my work piece.  This gives me an extra lip for my sled to move across.  For others who might have a different frame design, think about still removing material from the bottom of the sled.  Just don't take as much as I originally proposed.  Instead, think about leaving additional material radiating out from the center in a star burst pattern.  Envision an asterisk surrounded by a circle for a better idea of what I'm talking about.

---

Posted on **2017-03-28 18:25:29** by **rollandelliott**:

UMHW plastic has even less friction than HDPE plastic.  you can buy thick sheets of it to make a sled or use .005" tape to coat the underside.

---

Posted on **2017-03-28 18:26:34** by **rollandelliott**:

search ebay for 300mm aluminum lazy susan. People use these bearings to make track saws, I have one in my shop some where I bought but never used. might work better than those stamped bearings you used. not sure, but worth a shot.

---

Posted on **2017-03-28 18:28:15** by **rollandelliott**:

I know very little about the math/programming that lets maslow accurately cut, but won't this design require a whole new program to be written that is designed for these pivoting motor mounts? I kind of like this design better than the original.

---

Posted on **2017-03-28 19:41:43** by **jessbussert**:

I don't believe the math should be an issue. Bar has variables in his code that specify the width of the sled mount points as well as the drop to the router.  By making all these values zero (or 0.00001) it effectively changes the geometry into a triangle.

---

Posted on **2017-03-28 20:35:33** by **davidlang**:

if you are thinking air bearings, you can also think in terms of an air cushion for the sled. In both cases I think you are badly over-engineering things,  but let's see if this triangle approach produces any more accuracy than the stock approach. I suspect that it's not going to matter much, and a tweak of the existing design to move the motors to the sled (without the big circular bearings) would be a very interesting variation to try.

---

Posted on **2017-03-28 20:38:21** by **davidlang**:

by the way, when I say you are probably badly over-engineering this, I have a strong tendency to do the same thing :-)



I'm always fighting the tendency and trying to do a sanity check on the results to see if they are really better in practice.

---

Posted on **2017-03-28 21:30:13** by **jessbussert**:

Me? Over engineer something? No! Never!



*grins*

---

Posted on **2017-03-29 06:05:07** by **TomTheWhittler**:

Spoken like a true Engineer ;)

Why use only one screw when 4 will guarantee it will never come off :)

BTW. I like your "all in one concept" sled. It tidies things up without a lot of wires running around.

---

Posted on **2017-03-29 07:05:08** by **rollandelliott**:

Cutting boards are hdpe plastic not derlin plastic

---

Posted on **2017-03-29 10:11:11** by **jessbussert**:

@TomTheWhittler:  That's why if I were a NASA engineer all my craft would be 300% heavier and require much bigger engines!  Hey!  Bigger engines?  COOL!

---

Posted on **2017-03-29 11:13:27** by **TomTheWhittler**:

I must be an engineer as I am constantly told I over build stuff.

---------------------------------------------------------------------- ----------------

my normal signature line :

Research is the only place in a company where you can continually have failures and still keep your job.

I knew immediately that was where I belonged.

---

Posted on **2017-04-01 12:57:49** by **blsteinhauer88**:

Mine is built and making projects! [IMG_0503](../../images/Dv/Xr/DvXr_img_0503.jpg.jpg)

---

Posted on **2017-04-01 13:42:10** by **Bar**:

Beautiful!

---

Posted on **2017-07-02 07:16:25** by **khandam**:

any updates? this design looks promising and I want to do something similar. hoping to learn from your experience?

---

Posted on **2017-07-05 19:30:57** by **rollandelliott**:

Dang this wAs the only lazy susan build and they have gone MIA?

---

Posted on **2017-07-05 20:01:09** by **iroc999**:

Yes I like this sled mounted motor design! I'm definitely going to run back and start working that idea into my sled concept

---

Posted on **2017-07-05 20:53:59** by **TheRiflesSpiral**:

She's busy saving the world... no time for forums now!

---

