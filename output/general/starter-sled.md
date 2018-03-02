## starter sled
Posted on **2017-03-19 14:11:59** by **aalbinger**:

I've been hard at work testing the initial "pull yourself up by the bootstraps" version of the machine.  One thing that was becoming tedious while testing was the router with no sled needing to be held by hand.  It is a general rule in woodworking that the worst accidents happen when you aren't paying full attention to the power tool.  As Bar has indicated elsewhere running groundcontrol while hand steadying the very basic machine can be a challenge.



To that end I think a starter sled would be a great idea.  I made a template by taking a standard sheet of 8.5x11 or A4 paper and folding it three times.  Once corner to corner in each direction and once in half along the long side.  This will give you a centerline to place the router on and two reasonable angles for the sled brackets to bolt to.  Cut out a chunk of wood the same size as the paper.  Place your router on it up near the top and trace around your router.  Place the sled angle brackets on the folded lines and mark out where you want a bolt to go in each side.  Be mindful of where the bolt with end up so that yo u don't have it smooshing into your handles.



Here is a photo of my template: http://i.imgur.com/Uffjh5O.jpg?1



Now either use a drill to make the necessairy holes or use your new router to carefully trace out the marks you have made with your template.  Bolt on the bits and try it out.  The measured distance between mounting points on my version was 343mm.  I put that into GroundControl and ran motor calibration.



Here is a video of the machine calibrating: https://www.youtube.com/watch?v=WAKDB-9Kkfc

---

Posted on **2017-03-19 14:17:55** by **aalbinger**:

Note that I ended up using only one bolt per bracket even tho my template shows two.  Space is a bit tight and likely you'll be cutting out the "real sled" as one of your first parts so this doesn't need to be much stronger than one tight bolt can deal with.

---

Posted on **2017-03-19 14:54:02** by **Bar**:

I think this is a FANTASTIC idea and may become the official method very soon. I just went through the process of trying to cut a sled to write the next step in the instructions and it's not a great system. I'm learning how to build the machine at the same time everyone else is because I've only built the one, and that was over the course of several months. Your ideas about how to best put the kit together are tremendously helpful.

---

Posted on **2017-03-19 17:42:19** by **blsteinhauer88**:

Nice job!

---

Posted on **2017-03-19 20:32:25** by **aalbinger**:

I suspect there might be a few other geometry things to enter for this sled to work just right.  I cut out the real sled using the gcode from the wiki and got a pretty good version but it is a bit of an oval instead of a perfect circle.



http://i.imgur.com/DKYjDuY.jpg

---

Posted on **2017-03-19 20:38:41** by **Bar**:

That looks fantastic! I did the same thing and mine was very oval so you're not alone.

---

Posted on **2017-03-19 20:40:05** by **aalbinger**:

also, the backlash on the manual depth adjust on my Rigid router is quite frustrating. :)

---

Posted on **2017-03-20 08:37:28** by **rancher**:

Can you guys give the measurements of chain bracket mount holes to router center hole triangle, please?  I'd like to cut a temp sled that is close if I can.

---

Posted on **2017-03-20 08:57:04** by **Bar**:

Yes! The spacing between where the chains mount is 310mm and they mount 140mm above the bit. So if you had a 'T' shape where the chains we're at the top left and right corners and the bit was at the bottom the dimensions would be 310mm wide, 140mm high.

---

Posted on **2017-03-20 09:02:20** by **rancher**:

Thank you!  There must be twenty of you Bar.  Good work dude.

---

Posted on **2017-03-20 11:09:01** by **Bar**:

Thanks! We do our best.

---

Posted on **2017-03-20 11:57:02** by **carlosrivers**:

GOT MINE! WOOT

---

Posted on **2017-03-20 17:17:50** by **Bar**:

I've been working out how to build the starter sled in a way which is simple and clear, and here's where we are so far. I made a [PDF](https://github.com/MaslowCNC/Mechanics/blob/add-temp-sled/tempSled.pdf) of a version of the sled which is the size of a standard sheet of paper. I then printed the sheet and attached it to a sheet of plywood using a [glue stick](http://www.officedepot.com/a/products/698325/Elmers-Glue-Stick-Classroom-Pack-All/) and cut along the lines using my router by hand which worked well. 



The problems are 1) Does everyone have access to glue sticks? I feel bad suggesting you need to use something which isn't included in the box. 

2) The gluestick leaves a sticky residue on the wood when the paper is removed



What are everyone's thoughts on this idea? Does this seem like a promising avenue?

---

Posted on **2017-03-20 19:09:52** by **scottsm**:

Glue sticks are very available. The sticky residue doesn't seem a problem on a temporary thing like a starter sled. Adding crosshairs to indicate the centers of the various holes would be a nice refinement.

---

Posted on **2017-03-20 20:56:03** by **aalbinger**:

I like it.  Did you counter sink the hole at all for the bolts?

---

Posted on **2017-03-20 21:06:38** by **Bar**:

I did, but I'm thinking we could get a similar effect by setting the router depth to about 1/4 inch to provide a space for the bolt heads to hide

---

Posted on **2017-03-21 07:59:56** by **tmaker**:

If people are going to print that, I'm assuming that everyone's printer software will be slightly different and it might inset the image with default margins and as a result scale the image down.  Would that be an issue?  How important is it to keep the original dimensions?  On my Brother laser printer, I have to uncheck a box that says "Fit to Page" in order to make it use the full page.

---

Posted on **2017-03-21 08:47:33** by **Bar**:

I was thinking about that too. Ideally, from now on the paper will come in the box. 



I think you are spot on that the question to ask is "How important is it to keep the original dimensions".



I will look into how much having the page distorted by adding default margins will cause problems. Fortunately, I think we can tolerate a fair amount of distortion and still end up with a sled which is at least good enough to cut out a better one.

---

Posted on **2017-03-21 08:48:46** by **blsteinhauer88**:

Did you have trouble without the bricks installed with the unit wanting to tip backwards when traveling down the wood, I did.  I used the 310 x 140 mm measurements

---

Posted on **2017-03-21 08:49:12** by **scottsm**:

Putting dimensions on the .pdf would be good.

---

Posted on **2017-03-21 08:52:39** by **Bar**:

Dimensions on the PDF are a great idea. 



As for the bricks wanting to tip everything over, yes. Are you using the steel 'L' brackets to attach the frame? There are a number of holes to allow for adjustment. I can send a picture in a few minutes, but the basic idea is that with the two holes side mounted down you can move the chain attachment point in or out to adjust for your routers center of gravity

---

Posted on **2017-03-21 08:53:17** by **Bar**:

The third hole from the top is right for me

---

Posted on **2017-03-21 08:54:07** by **blsteinhauer88**:

I will try that.  I have video but can figure how to post.

---

Posted on **2017-03-21 14:31:17** by **hannahteagle**:

@aalbinger can we possibly use your sled photo as well as your calibration video in our update this week/post the stuff to our website? we want to try to keep a running log of the progress that we make!

---

Posted on **2017-03-21 17:29:31** by **aalbinger**:

absolutely.

---

Posted on **2017-03-21 18:36:03** by **MakerMark**:

Thanks aabinger! My attempt to cut the sled with the router connected directly to the chains was sketchy at best. Using your temp sled idea made it much safer. 



I used a little wood glue to adhere the template to the wood. It didn't snag or bind when using it, but I'm sure glue stick would be better.  [Image](/images/Ku/Hj/KuHj_image.jpeg.jpg)

---

Posted on **2017-03-22 10:11:30** by **hannahteagle**:

Thanks @aalbinger!

---

Posted on **2017-03-22 15:39:35** by **rexklein**:

ok I cheated I was concerned about the safety and basic extra work of making a temp router mount. I looked around and found a lp gas holder from lowes I am sure a lot of people have these.  [IMG_20170322_153354](/images/uf/80/uf80_img_20170322_153354.jpg.jpg)

---

Posted on **2017-03-22 15:47:05** by **Bar**:

Very slick!

---

Posted on **2017-03-23 13:31:25** by **gero**:

I will cheat as well by building this to cut a starter sled http://www.redneckdiy.com/wp-content/uploads/2015/04/Circle-Jig.jpg

---

Posted on **2017-03-23 15:58:22** by **mikeberg**:

it possible to make the outside circle with a nail in the center of the template attached to a rope and cut the sled with router itself

---

Posted on **2017-03-23 16:10:38** by **aalbinger**:

I'm chuckling at calling a nice round sled cheating :)  The thought was to make a quick and dirty 1 or 2 square cuts and some holes.  If you are going to the work of making a nice round sled by all means make it full size and specs and consider the sled done.  :)

---

Posted on **2017-03-23 18:44:21** by **rexklein**:

here is how my cheat ended up I have a experiment I am going to try for the brick alignment.

[2017-03-23_18-41-34](/images/8D/V9/8DV9_20170323_184134.jpeg.jpg)

---

Posted on **2017-03-23 18:50:46** by **carlosrivers**:

@Rexklein, how did you tighten the bolts for the chain bracket?

---

Posted on **2017-03-23 18:54:30** by **rexklein**:

I am not sure what you mean? on the sled I counter sank them

---

Posted on **2017-03-25 09:07:38** by **blsteinhauer88**:

I redesigned the sled to have the counter sinks for the bolt holes cut.  It came out pretty circular too, just a funny tilt to the left motor which cut down the top of the circle, and some carved out areas I am testing to reduce friction.  But here is how it came out. If anyone interested, I took the sled .svg and added a 1 inch circle over the drill holes, and made it a pocket function of .25 inch.  That carved out a nice counter sink hole you could add a washer too if you wanted.

---

Posted on **2017-03-25 09:08:18** by **blsteinhauer88**:

[IMG_0476](/images/yE/xu/yExu_img_0476.jpg.jpg) [IMG_0477](/images/kS/3I/kS3I_img_0477.jpg.jpg)

---

Posted on **2017-03-25 09:10:36** by **blsteinhauer88**:

And for Bar, the sled is pictured upside down from from the way it cuts, the top of the circle and of the 4 squares are all slanted in the same direction.   I wonder if the left chain slipped on link, the sled was tilting down the to left when cutting.

---

Posted on **2017-03-25 09:14:09** by **davidlang**:

The nice thing is that the shape of the sled doesn't really matter, what matters is just that it's "large enough" for the work you are doing to not fall into a cut you have already made, as low friction against the workpiece as possible, and that your fasteners (chain attachments, router position) are precisely known,, and you can measure where the center of gravity is on the sled (the wider apart the chain attachments are, the more important the center of gravity measurement is)

---

Posted on **2017-03-25 09:16:09** by **davidlang**:

The sled will tilt as it moves around the workspace. If it's on the left side of the workspace, it will tilt to the right (because there is less tension on the right chain), and if it's on the right side of the workspace, it will tilt to the left (because there is less tension on the left chain)



the maslow firmware takes this into account.

---

Posted on **2017-03-25 09:19:32** by **blsteinhauer88**:

Thanks for all that, what is the best way to measure center of gravity, I think I have everything else done, but just getting that funny slant.

---

Posted on **2017-03-25 09:26:18** by **davidlang**:

balance it on a round rod that goes side to side and then move it up and down to find where it balances (without any chains attached)

---

Posted on **2017-03-25 09:30:02** by **blsteinhauer88**:

Measure from there to the bit?

---

Posted on **2017-03-25 09:30:26** by **davidlang**:

note that the round bar doesn't need to be exactly horizontal. mark the edges where it balances, flip it over and draw a line between those points.



draw a line between the chain attachment points, find it's center, and then draw a line perpendicular to the chain attachment line, and measure the distance along this line until you hit the balance line

---

Posted on **2017-03-25 09:31:13** by **davidlang**:

you do also need the distance from the center of the chain attachment line to the center of the bit.

---

Posted on **2017-03-25 09:32:23** by **blsteinhauer88**:

Perfect thanks!

---

Posted on **2017-03-25 13:34:34** by **scottsm**:

Here's what I understood for the center gravity.

 [Maslow Center of Gravity](/images/o7/o0/o7o0_maslowcenterofgravity.jpeg.jpg) The round rod winds up under the bricks, parallel to the chain attachment line.

---

Posted on **2017-03-25 14:55:29** by **davidlang**:

that sounds fairly reasonable, can you show it from the top.



The bricks are heavier than the router, so I am not surprised to see them under the edge of the bricks

---

Posted on **2017-03-25 15:47:05** by **scottsm**:

There's not much to see from the top, just a round sled with the bricks in their 'normal place'. I measured 65mm from the center of the dowel to the center of the router bit.

---

