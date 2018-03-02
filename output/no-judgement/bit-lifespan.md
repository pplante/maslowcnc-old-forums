## bit lifespan
Posted on **2017-05-27 14:42:45** by **boandersen**:

How long should a good bit last before needing to be sharpened or replaced? Iam seeing fraying after < 25 ft cutting with a bosch 1/4" (85911MC). Do you sharpen your bits yourselves?

---

Posted on **2017-05-27 15:06:07** by **davidlang**:

you should not see the bit wearing after < 25 ft.

how long the bit last depends on a lot of things, including how much and why type of glue is used in the plywood you are cutting

A lot of it depends on how hot the bit gets, if the router rpms are too high, and you are cutting too slowly, the bit gets hotter rubbing against the uncut wood and doesn't get much heat carried away by the chips it's cutting 

there was an article posted a few weeks ago about a company who has a very expensive CNC cutting marine grade plywood (the vacuum to hold the wood down cost over $10K), they go through multiple $30 carbide bits per day, but they are cutting really aggressively (since the machine costs well into 6 figures, they need to get their money from it)

unfortunately I don't really have a good answer for you. doing a quick google search found one discussion where they were talking about ~1000 ft of cutting and if one or two bits were needed. I also found this that talks about 200-400 ft http://patwarner.com/routerbits.html

---

Posted on **2017-05-27 15:28:24** by **davidlang**:

a few resources to look at

https://www.shopbottools.com/ShopBotDocs/files/FeedsandSpeeds.pdf
http://www.cnccookbook.com/CCCNCFeedsSpeedsWood.htm
http://www.cnccookbook.com/CCCNCMillFeedsSpeedsBasics2.htm

based on these, I really think you are running too slow and too shallow at too high a speed and overheating the bit.

we are limited to 35 ipm on the maslow, or about 0.5 ips, these guides talk about cutting at much higher speeds. For example, the shopbot manual includes an example

single flute 1/4" bit, cutting 0.5" deep per pass @18000 rpm should be moving at ~1.125 inches per second

now, our router runs about half that speed, (8-12k rpm IIRC), so if we have a 2-flute cutter and cut at our fastest speed, (we should move 2x as fast with twice as many flutes, and a bit under half as fast due to rpms), we are still cutting at about half the recommended rate.

---

Posted on **2017-05-27 15:39:54** by **davidlang**:

another post, this one with a perfect example for us
http://makezine.com/2014/03/21/cnc-routing-basics-toolpaths-and-feeds-n-speeds/

they show a 1/4" bit with 2 flutes cutting at 90 ipm @18K rpm. since our machine maxes out at about 1/3 that speed, ideally we would want to be running the router at about 6k rpm, but I believe that it only goes down to ~8k rpm.

now, these are the 'production' feeds, the best possible throughput, it's good to cut a little slower than this, but if you cut too slowly you are really rubbing. The make article talks about cutting 0.01" per flute per rev and the second cnccookbook article talks about 0.0008" per flute being in the rubbing category, that's a range of ~10x

without calculations, the thing to do is to watch the result of the cut. If you are just getting powder or dust, you are cutting way too slow, you need to be getting larger chips of wood being cut off.

---

Posted on **2017-05-27 15:45:01** by **davidlang**:

another good guide
http://www.onsrud.com/files/pdf/LMT-Onsrud-CNC-Prod-Routing-Guide.pdf

---

Posted on **2017-05-27 16:00:17** by **boandersen**:

Thank you so very much for that in depth answer. I've been running at 23K and limiting myself to 25ipm to be good to the machine.. I was so wrong it seems.. I'll slow down my rpms and speed up my cut - very nice.. Thanks again

---

Posted on **2017-05-27 16:31:33** by **rollandelliott**:

Buy bits in ten packs when they are only $4 each it doesnt matter if they wear out a little early

---

