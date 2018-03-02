## Engraving without cutting ?
Posted on **2017-02-11 17:44:05** by **excessnet**:

I was just wondering, could the Maslow do engraving, do do thing like this : [IMG_20140522_151401](//muut.com/u/maslowcnc/s3/:maslowcnc:L8VL:img_20140522_151401.jpg.jpg) (Random image on internet)

---

Posted on **2017-02-11 18:36:48** by **jbarchuk**:

I don't think it's been mentioned quite that way but should be 100% doable with the Z-axis controller. The point of the Z-axis is to have computer controlled cut depth. Normally for a router that's a few 0.001" beyond the thickness of the material. Set the Z to 1/2 the material thickness and it will cut halfway through.

---

Posted on **2017-02-11 23:47:58** by **davidlang**:

The key issue for these sorts of things is how much of the original surface is left behind. The maslow rides on the surface, so if you cut too much of it away you have a problem.

The original design for the sled has four feet on plus the plastic from the router, and those are what rides on the surface. Some of us have talked about getting a slippery plastic cutting board to use for the sled instead, which would give a wider surface to ride on.

This will be a matter of experimentation after we get our hands on them.

---

Posted on **2017-02-12 01:24:46** by **jamesbil**:

The ply router base looks like it has little Plastic button feet to increase stability, which is fine when working on a small area. But what will be the effect of these feet moving over a previous cut or groove, especially if it is wider than the plastic feet? I would be concerned it would make the router skip or jump.
Maybe a bigger plastic router base and no feet?
Thoughts?

---

Posted on **2017-02-12 01:47:51** by **davidlang**:

That's exactly why we were talking about no having the feet ad not using the plastic base from the router at all, and instead make the sled out of a slippery plastic, possibly something like: https://www.samsclub.com/sams/bakers-chefs-commercial-cutting-board-15-x-20/126035.ip?xid=plp:product:1:1

---

Posted on **2017-02-12 07:38:50** by **jamesbil**:

@David language the link won't load.
Sorry hadn't picked out on that. Makes a lot of sense. Also maybe a round over or shallow bevel on the under side of the sled so it doesn't snag on anything.

---

Posted on **2017-02-12 08:55:16** by **davidlang**:

hmm works for me when I click on it

---

Posted on **2017-02-12 11:13:05** by **TheRiflesSpiral**:

When we designed parts that needed to be super durable but slide well on a variety of surfaces, we used Nylatron GS. It's impregnated with moly powder and it's coefficient of friction is pretty low at 0.3. I used Tetron S (PTFE) on a project too, it's even more slippy at 0.08 but it's stretchy and not all that durable. (It would be fine on wood. Not steel though)

The only reservation I have with UMHW like those cutting boards is that they're not dimensionally stable... they'll warp/twist especially in thin layers. They're also not receptive to most adhesives so you're left to work out a fastening method. Maybe recessed screw heads would work.

---

Posted on **2017-02-12 14:39:53** by **davidlang**:

in our case, things are held on with screws anyway and we're talking about a 1/2" thick piece, not thin layers.

does that make a difference?

---

Posted on **2017-02-13 08:52:01** by **TheRiflesSpiral**:

Provided that piece is well supported, I don't think you'll see an issue. What you want to avoid is just mounting the router to that piece of plastic (with the usual 3 mounting screws on the router) and leaving it at that. At 1/2" you *might*  be okay... it's hard to say. I would recommend backing it up somehow with MDF or plywood or something more stable.

---

Posted on **2017-02-13 10:04:47** by **Bar**:

I ditched the little feet recently for exactly the reason you said, they gave inconsistent behavior on rough surfaces. Right now I'm using a fairly large plywood disk with a beveled edge and it is really good. The biggest issue is (exactly as you predicted) that the coefficient of friction is pretty high. Next I'd like to try a similar size, but with a honeycomb structure to reduce the amount of material in contact with the surface. I think using something like Nylatron would be ideal, but I want to try to do it with regular plywood because that's something we all have.

To answer the original question. Yes you could do something like that, but as was pointed out, you would need to make sure the sled was supported which you could do by cutting all of those at once right next to each-other.

---

Posted on **2017-02-15 01:11:20** by **jbarchuk**:

> @Bar
> I ditched the little feet recently for exactly the reason you said, they gave inconsistent behavior on rough surfaces.

Exactly.

> Right now I'm using a fairly large plywood disk with a beveled edge and it is really good.

Exactly-exactly. I remember seeing vids with a square edge on the sled and meant to comment but forgot.

Skis, snow sleds, bobsleds, boats all have upcurved leading edges for a reason. :)

> Next I'd like to try a similar size, but with a honeycomb structure to reduce the > amount of material in contact with the surface. 

Reducing the footprint, without significantly reducing the mass that the footprint supports (most of which is the router,) increases the PSI of the footprint. That's more basic friction regardless of footprint.

Reductio ad absurdum, the smallest footprint possible would be a single pinpoint. That point would immediately press itself into the material to cut, and all sled movement stops there.

> I think using something like Nylatron would be ideal,

That stuff looks aaawesome! The only pages I see are manufacturers not dis tributors or retailers. :(

In model airplanes people fly aircraft with no landing gear such as seaplanes off water, grass, sand, and snow. The sliding surface may be painted wood, fiberglass, or foam covered with packing tape. Anything wet is actually quite sticky. People use Pam and RainX to make the surface more slippery. Whether it's a possibility for the sled needs more thought. Those materials applied to raw wood will probably just soak in. A surface would need to be sealed for that to not happen. But even with that it's possible that the Pam or RainX might -not- be a good thing to get on the wood being cut if, for instance, it's going to be further finished with stain.

---

Posted on **2017-02-15 07:10:36** by **TheRiflesSpiral**:

Bar, get some Johnson's Paste Wax and give your sled a few light coats over several hours. It will be slicker than a banana peel. :)

---

Posted on **2017-02-15 08:18:20** by **scottsm**:

I've had good luck with Johnson's Paste Wax as a surface lubricant as well. 
I found Nylatron GS online from these folks:
http://www.onlinemetals.com/merchant.cfm?pid=6767&step=4&showunits=inches&id=212&top_cat=0 
but at $31.14 for a 12" x 12" x 1/4" sheet, I'll keep looking, or wait and try some other approaches first.

---

Posted on **2017-02-15 09:13:34** by **davidlang**:

a cheap, but noticable improvement would be to use melamine coated panels, Home Depot has 4x8x3/4 sheets for $35 http://www.homedepot.com/p/Melamine-White-Panel-Common-3-4-in-x-4-ft-x-8-ft-Actual-750-in-x-49-in-x-97-in-461877/100070209

these are sold as shelf material, so they should be available in smaller/cheaper chunks as well.

but I still think that in the long run, something like the sams club cutting board will be better (even if it has more friction initially, the fact that it's solid instead of a laminate that can wear off is probably better)

---

Posted on **2017-02-15 09:48:06** by **TheRiflesSpiral**:

Yeah, nylatron is pricey. Really, it's not too far off UHMW/HDPE from a raw material standpoint if you're buying in machinable chunks, but the cutting board popularity has driven down the cost of the sheet goods... ah the economies of scale.

---

Posted on **2017-02-15 10:31:30** by **scottsm**:

Dollar Tree has some 11" x 14" 'flexible chopping mats' at 2 for a buck. I think I'll start with one of those and work up.

---

Posted on **2017-02-15 11:15:30** by **davidlang**:

the flexible ones would have to be fastened to a wood sled, if you get one of the solid ones, you can make the entire sled from it.

the sams club one is <$9 for 15"x20" (min order 2 if shipped, so say $25 for a pair including shipping)

---

