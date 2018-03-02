## test request
Posted on **2017-05-12 21:30:36** by **davidlang**:

The purpose of this is to detect if the sled is sticking or sliding properly. If it is sliding properly, the cuts should be exactly on top of each other. If the sled is sticking, the cut back can end up rounding the corner.



http://lang.hm/maslow/testpattern4.nc



This goes to the bottom left corner of the work area, cuts a right angled down/right and then covers the same path left/up. This lowers the bit at the beginning of the cut and raises it at the end, so it's doable even without a motorized Z axis.



This is testing one of the worst areas, where one chain is near vertical and the other has the lowest tension on it, with the sled moving away from the low tension test. It first cuts down (gravity helping) and to the right (tension being added to the chain) and then tests as you loosen the already slack chain and then start pulling up. If the sled sticks as the right chain looses tension, it can fail to move until the left chain starts pulling up, at which point it will swing.



I'd like to see someone who has a frame they can easily tilt and a stock sled 

 test this.



 1. with and without dust collection



    a powerful dust collection system can vacuum the sled down to the workpiece. this test is to see if we need to cut slots in the sled to keep this from happening.



2. with different weight on the sled



    do we really need so much weight in bricks? does it make a difference (assuming you have the chains attached far enough out for the sled to be balanced)?



3. at a few different angles.



    The default is ~15 degrees, if we change the angle to 10 degrees or 5 degrees does it make things better? what if we change it to 20 degrees?



If you can film it, you don't need to move the wood to make a fresh cut each time, the video  will let us see if it's going through the same path or not.



my suspicion is that:



1. the amount of weight on the sled will make very little, if any difference

 

    the weight of the sled falls out of all the motion math, and adding weight increases friction linearly along with the downward force on the sled



2. things will be worse with dust collection on



    indicating a need to have some gap on the sled so that air can get in and not suction the sled down to the workpiece



3. things will be better the closer the sled is to vertical.



    indicating that we are better off with an angle less than 15 degrees (for cutting purposes anyway, overall stability may require more of an angle or other weight on the base to keep it from being knocked over easily)

---

Posted on **2017-05-12 22:55:55** by **Bar**:

That's a great idea. I've been looking for a quantitative way to test different angles and this is the best I've seen so far

---

Posted on **2017-05-13 06:21:17** by **davidlang**:

the closer to the corner the cuts are made, the more it will test the low chain tension part of the test, but I kept it back from the edge about 6" so that the "suctioning down" effect could be tested

---

Posted on **2017-05-13 07:03:02** by **jwolter0**:

Excellent test idea!  I'd suggest an additional test of the same pattern near the middle of the working area to separate out the effects of mismatched chain tension from the general repeatability.  If you ran the middle-of-the-board test with changes to the other variables (weights, dust collection on/off, working angles), you'd have a database from which you could tease out all sorts of effects and interactions.

---

Posted on **2017-05-13 14:22:51** by **blsteinhauer88**:

I'm at the beach this weekend. I'll run it when I get back.

---

Posted on **2017-05-13 14:56:24** by **davidlang**:

@jwolter0



I expect that when the sled sticks, it's going to be a very dramatic change to the cut (a quarter circle rather than an angle), not some minor errors in repeatability

---

Posted on **2017-05-15 11:27:20** by **blsteinhauer88**:

@davidlang, i am still planning on running your test pattern, hopefully tonight.  how deep it the cut, i plan to run it on my scrap board and if its only .1 deep that would be great.

---

Posted on **2017-05-15 15:45:51** by **gero**:

@davidlang I love this great idea that would bring a huge step forward and I could do different angles and weights at different speeds. Stuck for a while, as at the end of the money there is so much month left. Also finding companies for affordable bits that ship to here is a nightmare.

---

Posted on **2017-05-15 16:58:20** by **davidlang**:

This is 0.3" deep, but if you change the numbers in the file, or just set the Z zero above the board, you can adjust it.

---

Posted on **2017-05-15 16:58:57** by **davidlang**:

@gero, your local hardware store should have router bits available

---

Posted on **2017-05-15 17:00:14** by **blsteinhauer88**:

Will do

---

Posted on **2017-05-15 17:10:18** by **gero**:

> @davidlang

> your local hardware store should have router bits available

Sadly this does not apply to Bahrain. And 98% of Amazon does not ship to here. I ordered from Germany, but the price is to high for testing. I need to keep those for projects. Spending hours on searching and being hesitant with Ailbaba. I will get them, latest on my next trip abroad. This gives me hope: https://www.toolstoday.com/p-5645-solid-carbide-spiral-flute-plunge-2-flute-up-cut.aspx but still above $25 per piece and no info on how good the brand is.

---

Posted on **2017-05-15 17:14:38** by **gero**:

Sharing information of sellers that ship internationally is a task. I am on it :-).

---

Posted on **2017-05-15 17:27:06** by **Bar**:

We're also working on getting some bits from Alibaba and making them available. I think we can get cheaper bits for everyone by buying them in bulk, plus I want them just for making things. We will absolutely ship to Bahrain :)

---

Posted on **2017-05-16 13:52:08** by **rollandelliott**:

I love the Chinese tungsten bits off aliexpress, very good pricing and quality. in bulk they are dirt cheap.

---

Posted on **2017-05-17 02:19:34** by **gero**:

> @rollandelliott

Bulk and dirt cheap is exactly what I need to make a lot of dust.

Do you by chance have a link to what you bought? I am bit overwhelmed with the choices.

---

Posted on **2017-05-17 05:22:41** by **jwolter0**:

@gero, I added a page on the wiki for sharing sources of parts (https://github.com/MaslowCNC/Mechanics/wiki/Parts-Vendors).  I'm sure many in the community would appreciate knowing if they ship internationally, so feel free to add your discoveries there, too.

---

Posted on **2017-05-17 08:15:11** by **Bar**:

That's a fantastic idea for a wiki page. Thank you for making that.

---

Posted on **2017-05-19 09:11:06** by **blsteinhauer88**:

@davidlang I finally got to my machine, wife and I hit with the sinus and lung junk going around...., anyway I have interesting results.  B patient as I post the photos and videos for ya.  My videos are not great. Lon

---

Posted on **2017-05-19 09:11:46** by **blsteinhauer88**:

https://www.youtube.com/watch?v=_D83y4W--xU&sns=em

---

Posted on **2017-05-19 09:12:27** by **blsteinhauer88**:

This video, if you can play is with two bricks, dust on, and 10 degrees

---

Posted on **2017-05-19 09:13:15** by **blsteinhauer88**:

[IMG_0807](//muut.com/u/maslowcnc/s3/:maslowcnc:H0Jr:img_0807.jpg.jpg) [IMG_0808](//muut.com/u/maslowcnc/s3/:maslowcnc:mZU3:img_0808.jpg.jpg) [IMG_0809](//muut.com/u/maslowcnc/s3/:maslowcnc:iEeg:img_0809.jpg.jpg) [IMG_0810](//muut.com/u/maslowcnc/s3/:maslowcnc:INma:img_0810.jpg.jpg) [IMG_0811](//muut.com/u/maslowcnc/s3/:maslowcnc:uPQx:img_0811.jpg.jpg) [IMG_0812](//muut.com/u/maslowcnc/s3/:maslowcnc:EOxj:img_0812.jpg.jpg) [IMG_0813](//muut.com/u/maslowcnc/s3/:maslowcnc:gNC5:img_0813.jpg.jpg)

---

Posted on **2017-05-19 09:13:40** by **blsteinhauer88**:

The photos have captions.  I think I have one more video.

---

Posted on **2017-05-19 09:18:48** by **blsteinhauer88**:

https://www.youtube.com/watch?v=Yoc9qdhJvKY&sns=em

---

Posted on **2017-05-19 09:19:20** by **blsteinhauer88**:

This photo is at 15° tilt dust collection on and one brick stock sled

---

Posted on **2017-05-19 09:27:15** by **blsteinhauer88**:

My setup now is a 10 degrees stock with a one brick sled.  I may ad one back on.  It appears weight does matter, even in just 5 degrees of tilt.  I wonder what a 5 degree tilt would do?  By the way the test was done with last weeks firmware and GC release, NOT the latest one with the PID upgrade.

---

Posted on **2017-05-19 09:42:06** by **rollandelliott**:

I get error video is not available?

---

Posted on **2017-05-19 09:58:11** by **blsteinhauer88**:

Ok let me check it

---

Posted on **2017-05-19 09:59:27** by **blsteinhauer88**:

Try now they were set to private

---

Posted on **2017-05-19 10:01:20** by **scottsm**:

That did it, thanks :)_

---

Posted on **2017-05-19 22:13:52** by **davidlang**:

Thanks for testing this. One thing I realized a few minutes ago is that we may have a little bit of rounding at full speed, simply due to the fact that gravity gives us so little force at such steep angles.



I think it's interesting that one brick gives us very good results at 10 degrees, but not so good at 15 degrees. That makes me very curious to see what happens at 5 degrees (including with no bricks)



It seems that at 15 degrees, dust collection doesn't make a difference. So don't bother doing with/without dust collection on all of them, just one test at 5 degrees, no bricks with/without to double check the most extreme case.



I suspect that the new firmware will make a bit of a difference here (I don't think a huge difference), but if so, we may need to re-run some of these

---

