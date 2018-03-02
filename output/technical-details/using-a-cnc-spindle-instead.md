## Using a cnc spindle instead of a router
Posted on *2016-10-15 18:47:05* by *neon22*

In my country the Ridgid routers are not available and a 2kW router by (say) makita is >$900. I wonder if a Chinese 2-5kW spindle with controller would do as good a job.
Of course need to build a support for it to float on the surface. But not as tricky a base as that required for a 'real' router because most of the features of such a base are not required. Just to sit flat on the surface. Might even be better with a bigger more stable flat base ?&quest;
Any ideas ?

---

Posted on *2016-10-15 19:37:06* by *Bar*

I would expect a 2-5kW spindle to do a great job. If you have any in particular that you are considering I'm happy to take a look. My only concern would be how would you set the depth of the cut? Using a router gives you a platform which has built in depth adjustment, but most stand alone spindles don't have that.

---

Posted on *2016-10-15 21:32:26* by *neon22*

yes. good point. I was thinking something like this mount:
https://www.aliexpress.com/item/Diameter-80mm-Adjustable-1-5-2-2KW-Water-Air-Cooled-Spindle-Motor-Mount-Holder-Clamp-for/32418491862.html

Its an 80mm diameter adjustable circular mount but some of the spindles are square too. Like this one:
https://www.aliexpress.com/item/Square-4kw-ER20-Air-cooled-spindle-motor-4-Ceramic-bearing-4kw-VFD-Engraving-milling-for-CNC/32740722752.html

Need a clamp mount for that probably and comes with ER20 collet.
I'm in a 230VAC country so 220 is OK.

Here are a number of aircooled ones of differing ratings:
https://rattmmotor.aliexpress.com/store/group/Air-cooled-spindle-motor/907217_256261020.html

---

Posted on *2016-10-17 15:35:12* by *neon22*

Can you guys see the servo'd steppers they sell. Any use for your driver motors ? The driver board is available in may places HSS57closed loop stepper driver.
E.g. https://www.aliexpress.com/item/EU-Ship-Free-VAT-Nema23-2N-m-Closed-Loop-Easy-Servo-motor-4-2A-L-76mm/32672465235.html

---

Posted on *2017-01-26 14:43:56* by *lthomas987*

That mount you posted with the threaded screw adjustment would probably take the planned Z control great.  I had just been contemplating my old terrible router, and then what to replace it with when it dies.  And if a Chinese spindle would be a better choice than a router.  So if anybody tries it I'd like to hear about it.

---

Posted on *2017-01-26 14:54:31* by *davidlang*

The advantages of a spindle are:

more precise
more flexibility in tool size
more flexibility in RPM (depending on control interface)
lighter
smaller
quieter
power (depending on the spindle and router)

With the maslow, reduced weight isn't an advantage (you already add bricks to add weight, so if you reduce weight with the spindle, you have to add it back)

The cutting rate and depth shown so far are shallow enough that additional power and rpm control probably won't help (and the recommended router is pretty powerful)

precision isn't going to help much, the difference in precision between a router and a spindle is far less than the positioning error being claimed.

smaller and quieter may be an advantage.

The Maslow is not a high precision device, so I would be surprised if the additional flexibility in tool size was used much.
 
Possible, and if you can get one cheap enough, it may be cheaper than the router and therefor worthwhile, but I doubt it would make a big difference.

---

