## The Jan 25 Weekly Wednesday Update is UP!
Posted on **2017-01-25 16:48:50** by **Bar**:

This week I downloaded and built a chair from OpenDesk. You can check it out here: https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1792072



Any questions about this weeks update or suggestions for a future update? What do you want to see more of?

---

Posted on **2017-01-25 17:25:55** by **chauhuh**:

It might be nice to see how the machine performs on different materials.

---

Posted on **2017-01-25 17:34:17** by **Bar**:

I think that is a fantastic idea. That could really be a whole update right there. What would be some good materials to test? The ones that come to mind are OSB, Sheetrock, Foam, Cardboard?, some kind of hardwood in plank form...what else am I missing?

---

Posted on **2017-01-25 18:10:57** by **chauhuh**:

Possibly acrylic. Really thin plywood (like a veneer). Sheet metal?

---

Posted on **2017-01-25 18:12:59** by **chauhuh**:

BTW I really enjoyed the last update to see working/usable products coming out of this great machine. It got me thinking about chairs and I found this.



http://www.sketchchair.cc/

---

Posted on **2017-01-25 18:40:10** by **TheRiflesSpiral**:

Coroplast! (Corrugated plastic) You can probably get a sheet from your local sign shop.

---

Posted on **2017-01-25 18:54:31** by **danield**:

How long did it take to cut out the chairs once you had worked out the issues? How long would it take if you wanted to cut out two more?

---

Posted on **2017-01-25 20:18:20** by **jbarchuk**:

Dollar Tree foam board. Other any other dollar store foam board. There isn't much difference except for the adhesion of the paper to the foam.



Thick 1/2" and 1" blue insulation foam is great for the 3D people. It's very straight and flat.



Fan fold insulation foam is also very common but not naturally flat, and smooth(er) on only one side. The smooth side still had lots of small imperfections but should be doable, and the rough side is wavy and textured.

---

Posted on **2017-01-25 21:57:42** by **davidlang**:

you are doing very shallow cuts at very slow speeds (especially for a 2HP motor). Sorry for the long post, but I want to be sure I document the reasons behind my numbers.



This website has info on the preferred cutting settings for different types of wood.: https://www.onsrud.com/xdoc/feedspeeds



cutting hard plywood the chiploads can be pulled from this table https://www.onsrud.com/files/pdf/2012LMTOnsrudProductionCuttingToolsHardPlywood.pdf



feed rage (ipm) = RPM * # of cutting edges * chip load



for a good quality single pass with a 1/4 bit, the chipload should be ~0.015 with a cut depth of .25" 



so feed rate = 15000 * 2 *0.015 = 450 ipm



to cut 3x tool diameter (3/4" in one pass) you would cut the chip load by 50%, or want to cut ~200 ipm



if you cut too far below that, you will overheat the cutter and burn the wood



cutting only .1 deep @25 ipm is 1/20 or less of what the recommended feed rate would be. I would be expecting to see a lot olf burning of the edges of the wood at that speed.



by comparison, I see people talking about using the 2.5HP shopbot cutting 3/4 " plywood in a single pass at 20k rpm and ~4-6 ips (240-360 ipm), which seems inline with the chipload compression.



Is the maslow really limited to such slow feed rates? I would expect it to be slower than the really solid shopbot, but we are talking about a factor of ~150x difference here (between the ipm difference and the number of passes needed due to the depth difference)



If you are cutting so slow, you may want to consider slowing down the router to it's minimum speeds (which would set the 'suggested' feed rate to ~1/2 the values listed above.



Could you show some cutting tests at higher speeds, greater depths, and with larger bits (per the tables, there are a lot of cases where it's better to use a 3/8 or 1/2 bit than a 1/4 bit)



For these sorts of tests, circles or squares would be good (so that we can see easily how accurate they are), or possibly the something from the makerbench series would be useful in your shop https://obrary.com/collections/designs-for-the-cnc-router/products/makerbench-series-5

---

Posted on **2017-01-25 23:13:17** by **larry357**:

An outtake video, would love to see the miniture chair :)

---

Posted on **2017-01-26 00:30:48** by **jamesbil**:

Hi Bar, As a carpenter, it does look like your cuts are very shallow as noted by another comment. As a rule I would set the depth to half the diameter in all but the hardest woods. So for a 10mm cutter it would be 5mm deep each pass. Looks like you were cutting 1 or 2mm? You could probably also speed up the feed rate slightly. 

This is looking at it from an "on the bench" point of view, obviously you know best regarding the maslow setup.

How long did the chair take in real time? 

Be good to see the dreaded MDF cut too.

---

Posted on **2017-01-26 19:12:11** by **Bar**:

You guys are absolutely right that I was way too conservative on the feed-rate and step down. I played it really safe. To better answer your question I played around a little bit more to see how far I could have pushed things and I filmed some of the results: https://www.youtube.com/watch?v=GGSYVikWs3g



The chair in the video took about four hours to cut, but I think it could be done in under an hour with the proper tool and once we've got all the kinks worked out of the firmware.

---

Posted on **2017-01-26 21:35:52** by **davidlang**:

That looked really good. the chips cut looked much better as well.



On the shopbot forums, I was seeing comments that the people doing this sort of thing full time are moving from 1/4 bits to 3/8 or 1/2. Part of this is that the bits are just stronger, but also they have a larger percentage of their volume cut away for the chips to move.



based on what you showed in the video, I think it would be very happy cutting at full speed with the larger bit.



I'll bet that after firmware fixes you could cut the chair in under 30 min,

---

