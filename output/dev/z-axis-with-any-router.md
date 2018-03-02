## Z axis with any router
Posted on *2016-10-30 18:57:41* by *brandonmc*

I've been wondering about the z axis and how it will work. Will the Z only work on a particular router or will it work on any router?

---

Posted on *2016-11-03 20:13:17* by *electronrancher*

+1 for this question. And I''d like to add to it

Bar,
Saw the z-axis, very slick.  Am I correct in thinking that you are driving the built-in adjustment screw in the Ridgid?  Or are you actually raising and lowering a plate that the router is mounted to?

You solicited questions in yesterday's update, so I'd like to ask about a makita router that uses the common "gear and latch" style adjustment.  See it here.
https://www.hmres.com/site/images/productimages/64363909-00f0-438d-8431-2ba7.jpg

For this more generic mechanism, I don't think it can be adjusted on the fly - the sleeve would be too loose if the clip were unfastened.  We'd have to hard-mount to a plate and raise the whole plate.  Unless there's a better way - any suggestions?

---

Posted on *2016-11-05 10:25:29* by *Bar*

Thanks! I'd like to make the z-axis adaptable for as many routers as possible, but I haven't got a design which will work for every router. That's a bit part of why we didn't make it a part of the kit by default. I would love to have a design that would work across the board, but I haven't come up with one yet.

I think routers generally fall into two categories, those which can be setup to work as is, and those which would need some type of router lift mechanism. There's just so many different designs of routers in the world, I don't know how to make a design which will accommodate all of them well.

---

Posted on *2016-11-05 10:29:34* by *Bar*

I played around with one of those Makita routers in the store the other day, and my impression was that if you set the latch tension with the nut on the back side just right you MIGHT be able to get it to work, but it's pretty big stretch. Another issue with those small routers is that the base-plate which slides along the work has a very small area compared to a full size router, which is going to make it more susceptible to issues when cutting on a rough surface. They are beautiful machines, it felt like a very well built router.

---

Posted on *2016-11-08 21:05:01* by *thedirtfighter*

Based on what I have seen of your design there are many "shop built" router lift designs that would more than likely be an easy solution to automate the z axis. Just search Youtube. Shop Built, Jay Bates, Izzy Swan, Steve Ramsey, Matthias Wandel, Stumpy Nubs are just a few off the top of my head that I know have made shop built router lifts...all great designs that I am sure could be automated relatively easy.

---

Posted on *2016-11-12 08:57:20* by *laird*

It looks to me like the cheapest "lift" would only work on models with a vertical lift worm gear that you can simply attach a motor to, like the model you recommend. The 'general' solution would be to have a mechanism between the router and the sled to move the router up and down relative to the sled, which would be more complicated/expensive. My vote would be to start by supporting the simpler/cheaper worm-gear approach, because your selected router is only $169, and it could well cost that kind of money to make a general router lift mechanism.

And given the high value of automating Z-axis, it's hard to imagine anyone NOT adding that upgrade. The idea of having to manually adjust a CNC mill to lower and raise the router for every single cut would make it unusable except for the very simplest designs.

---

