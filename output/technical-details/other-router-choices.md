## Other Router Choices?
Posted on **2017-04-26 17:03:44** by **sparhawk2k**:

Is EVERYBODY in the US going with the Ridgid R22002? :)

I'm curious about the Bosch 1617EVS.

Though I'm not sure how adventurous I want to be trying something nobody has tested yet. There was a thread on the details (http://www.maslowcnc.com/forums/#!/technical-details:z-axis-question-for-bosch-r) but I don't see anything on actually trying it yet.

I'm curious to see how it works with other options in general though. There's only one other router in the Tested Routers List that's not the EU one. Are there beta testers with other routers that haven't made it to the wiki yet?

https://github.com/MaslowCNC/Mechanics/wiki/Tested-Routers-List

---

Posted on **2017-04-26 17:44:27** by **Bar**:

I think that's a great question. From handling them in the store they seem like really well built routers and the price is right in the ridgid range. The z-axis on them seems to work quite well with very little backlash. Overall I'd bet the bosh is a good choice, but I haven't really gotten to put in many hours using one. If you go that way, let us know. I think it would be valuable information for everyone.

---

Posted on **2017-04-26 17:45:57** by **gero**:

You are the one to add more tested routers!

---

Posted on **2017-04-26 18:16:58** by **rollandelliott**:

Is there a palm router which has a z axis knob? Seems like all the small routers ive seen do not have a very big depth control knob like thd big  1/2" routers do

---

Posted on **2017-04-27 12:26:21** by **sparhawk2k**:

Unfortunately, I'm not a beta tester so I don't have the system yet to test. So I can't add info on tested routers YET. I was hoping to get feedback before mine ships so I can decide which z-axis kit to order.

I figure it's more helpful earlier as it will impact the orders of a lot more people. Though I certainly plan on contributing back once I've got mine up and running.

---

Posted on **2017-04-27 18:14:00** by **ylexot**:

I've also been eyeing that one. I'd like to get the kit with both the fixed and plunge bases.

---

Posted on **2017-04-27 20:22:55** by **mcginniwa**:

I think @jbarchuk is using a similar Bosch rig. Check out the vids mentioned [here](http://www.maslowcnc.com/forums/#!/general:bosch-ra1161-fixed-base-mod).

Here in NZ, a couple of us are trying the Bosch GOF 1600 CE combo router (have to buy fixed base from states) which I think has a US equivalent model. I'll report back once I have my beta kit put together. Should be this week.

---

Posted on **2017-04-28 03:24:06** by **plexer**:

Looks like the GOF 1600 CE might be one for the UK market too

---

Posted on **2017-04-29 11:28:03** by **jonmatcho**:

I bought the Bosch 1617 with an extra two bases, one for a router table and one for the Maslow (so I still always have a free standing base).  I am waiting for the next round to receive my Maslow kit.

I can't imagine how I could go wrong with this router and wouldn't be surprised that this Bosch turns out to be the best balance of cost, precision, and durability.  

We shall see... looking forward!

---

Posted on **2017-06-03 09:32:25** by **plexer**:

Hi all, I'm in Florida at the moment and hoping to pick up a ridgid while I'm here would this one work? http://www.homedepot.com/p/RIDGID-5-5-Amp-Corded-Compact-Router-R24012/100337039 they also have the R22002 as well.

---

Posted on **2017-06-03 09:35:31** by **plexer**:

Although I don't think it will work with where the micro adjuster is located

---

Posted on **2017-06-03 09:42:33** by **davidlang**:

It would be a real pain to motorize that Z axis, I'd just spend the extra $50 on the larger router.

---

Posted on **2017-06-03 09:48:15** by **plexer**:

Just need to find one in stock locally before I leave on Thursday :)

---

Posted on **2017-06-04 06:38:42** by **plexer**:

Hmm finding one is proving difficult what about this ryobi one? Cheap enough to be worth a punt? http://www.homedepot.com/p/Ryobi-8-5-Amp-1-1-2-Peak-HP-Router-R1631K/206757945 fixed base router's are expensive in the UK

---

Posted on **2017-06-04 06:48:59** by **ylexot**:

Looks like it could work, but don't you use 220V in the UK?

---

Posted on **2017-06-04 06:51:05** by **plexer**:

Yes but 110 transformers are common for outside building work so the voltage is fine the frequency of the mains power is slightly different 60hz Vs 50hz bit that's ok

---

Posted on **2017-06-04 06:51:40** by **ylexot**:

Oh, here's a negative for it...It looks like it's a fixed RPM.

---

Posted on **2017-06-04 07:04:30** by **plexer**:

Oh yeah :( damn

---

Posted on **2017-06-04 10:05:35** by **mfpiechowski**:

A little late to the party, but I thought I would chime in regarding the Bosch 1617. I am currently using one in my router table and I like it a lot. The only issue I see with using the 1617 and its fixed-base on a Maslow is the lack of range on the threaded depth adjuster. Mine only has an inch of travel, but it has multiple detents in the motor body. There's no way to get more than an inch of Z-travel without resetting the motor, which may not be enough for some cases. I also have a Ridgid router that is a bit older than the recommended one. I use that for hand use. It has 2 inches of range on the threaded adjuster, which is plenty for the Maslow.

---

Posted on **2017-06-04 10:42:44** by **sparhawk2k**:

So you've got an inch of travel automatically but can then manually move it to get more depth by changing where the motor sits? I looked up detents but don't completely understand.

---

Posted on **2017-06-04 11:00:03** by **ylexot**:

This review might help explain the detents some: http://www.newwoodworker.com/reviews/bsch1165rvu.html

It looks like the fine adjustment (which is what the Z-axis will use) only has 7/8" of travel. That's a bit tight, but it'll still work with 3/4" plywood. For thicker stock, I guess you'll have to have a manual plunge step somewhere in the g-code.

---

Posted on **2017-06-04 11:10:21** by **mfpiechowski**:

Exactly. The router has a series of slots in the motor that the tab on the threaded adjuster engages with, then the adjuster moves through about an inch. My 1617 is a couple years old, the newer ones may be different. Still, it is something worth looking into for use like this on a Maslow. With a "safe height" of a quarter inch, even 3/4-inch material would use up all the available Z-travel.

---

Posted on **2017-06-04 11:15:19** by **davidlang**:

not to mention that you would be required to position the bits at exactly the right depth to put you all the way at one end of the travel at the 'safe height'. It's really easy to eat up that 1/4" with the bit positioned slightly wrong

---

Posted on **2017-06-07 16:16:43** by **sparhawk2k**:

Thanks. I ended up going with the Ridgid R22002. It sounds like it works. Maybe I'll play with trying other routers in the future but for now I figure that's safer/easier.

---

