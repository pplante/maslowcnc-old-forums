## Seattle
Posted on **2017-01-26 21:54:01** by **chauhuh**:

Anyone else in the Seattle area get one of these?

---

Posted on **2017-01-27 08:03:07** by **mindeye**:

Soon after betas arrive I'll be putting mine together. I'm in the Northgate area. Pretty sure there's a solid handful of folks in this area getting one sooner or later.

---

Posted on **2017-01-27 09:13:28** by **chauhuh**:

Oh serious! I'm a Northgate guy myself.

---

Posted on **2017-01-27 09:16:36** by **chauhuh**:

I'd love to be able to come by and see your machine since I won't be getting mine until May.

---

Posted on **2017-01-27 09:41:17** by **sparhawk2k**:

Woah! I'm in Pinehurst, just north of Northgate! Getting mine in May.

---

Posted on **2017-01-27 09:49:25** by **mindeye**:

Very nice! I said Northgate to keep it more recognizable but truly I'm Pinehurst as well. I'm definitely up for demo-ing once I'm up and running.

---

Posted on **2017-01-27 09:49:46** by **chauhuh**:

Awesome! I'm technically in Shoreline, just north of Pinehurst but I work in Northgate.

---

Posted on **2017-01-27 09:54:50** by **sparhawk2k**:

I'd love to see a demo! I was wondering how I was going to manage to wait for mine to arrive...

---

Posted on **2017-01-27 10:14:30** by **sparhawk2k**:

I help run the Pinehurst blog and Facebook group. And I was the Pinehurst Community Council president for like 7 years. I'm psychologically incapable of calling it Northgate now even if nobody knows what I'm talking about. :)

---

Posted on **2017-01-27 11:40:10** by **TheRiflesSpiral**:

Today I learned that everyone in the Seattle area is actually from a slightly different area than they say they are... :D

---

Posted on **2017-01-27 11:47:34** by **sparhawk2k**:

Except me. :-D



Though really, it's kinda hilarious when you really start getting into the weeds of the communities and neighborhoods in Seattle. Some of them are tiny (a few blocks across) and many of them overlap so you can be in different neighborhoods depending on the context or who you're talking to. There are umbrella neighborhoods that cover large areas with smaller neighborhoods contained within. And they're constantly shifting and changing, driven by changing demographics, construction, or realtors using different names to try to trick people into thinking an area is trendy.



And we still try to draw them on a map...

---

Posted on **2017-01-27 12:54:22** by **TheRiflesSpiral**:

That's such a stark contrast when compared to the St. Louis area. Those lines are drawn with permanent ink and guarded jealously. It probably has something to do with the City/County nature of the area.

---

Posted on **2017-01-27 12:57:46** by **sparhawk2k**:

I mean, they're guarded jealously here too. I have had conversations with people telling me my neighborhood doesn't exist and isn't real because they remember the neighborhoods when they grew up and it wasn't there then. Who cares about the fact that since then "we" put a freeway (I-5) through the middle of the city and divided the neighborhoods in two in many cases.

---

Posted on **2017-04-13 15:22:46** by **sparhawk2k**:

So @Mindeye... Thoughts on a Pinehurst/Northgate/Shoreline demo in the near future? :)

---

Posted on **2017-04-13 15:49:04** by **chauhuh**:

I'd get in on this!

---

Posted on **2017-04-13 18:00:42** by **mindeye**:

Hmmmm... Perhaps next Tuesday evening would work, 7 maybe? Unfortunately out of town this weekend.

---

Posted on **2017-04-14 11:39:47** by **sparhawk2k**:

Tuesday evening at 7pm should work for me! It might be easier to organize the details by email? Mine is Sparhawk2k@gmail.com and if people who were interested emailed me I can start a thread with everybody included. Just in case others are hesitant to post their email on a public forum.

---

Posted on **2017-04-14 11:52:04** by **sparhawk2k**:

This is obviously dependent on Mindeye emailing me as well. But I figured I'd get the ball rolling in case he didn't want to post his info here. But we could also just organize it here if that's easier.

---

Posted on **2017-04-15 08:00:41** by **mindeye**:

I'm at mind.eye@gmail.com, I think the only thing I'd rather do via email is hand out my address. Is there anything in particular folks are wanting to see? I'll try to come up with some good demo cuts but a little prep will make for a better demo for all.

---

Posted on **2017-04-16 22:52:05** by **sparhawk2k**:

I'm mostly interested in the setup and seeing some basic things end to end from the drawing to the cuts. I am curious to see the z-axis in person too. In terms of a demo cut, anything kinda complicated would be great, especially parts fitting together.

---

Posted on **2017-04-16 22:53:07** by **sparhawk2k**:

I saw a post on here ages ago about joints cut by CNC which I found very intriguing and will probably be trying myself. But it's probably a bit much for a demo unless you had any interest in it yourself. http://mkmra2.blogspot.com/2014/08/cnc-cut-wood-joinery.html

---

Posted on **2017-04-18 08:47:30** by **mindeye**:

Basic things end to end is totally doable. Parts fitting together is questionable currently (at least with my current calibration). My Maslow gets them close enough for minor adjustments to make them work but it's far from ideal currently. I'm hoping the coming improvements to make it a double closed-loop with auto-calibration will get it to a place where we can get really good CNC joinery out of it. Definitely something I'm excited to work with.



For part of the demo I think we'll draw a box joint in sketchup, use makercam to generate the gcode, and then cut it out and see where we land.

---

Posted on **2017-04-18 21:11:05** by **mindeye**:

Demo success! CNC box joint using two tool paths, first tool falsely large by .05" and then second path true tool size, .25" [IMG_20170418_210249723](/images/yu/yuzz_img_20170418_210249723.jpg.jpg)

---

Posted on **2017-04-18 22:22:14** by **scottsm**:

That's very very cool. Are the reliefs at the base of the fingers .25" or .3"? I'm wondering how you handled those. Did you put both toolpaths into one file, or two?

---

Posted on **2017-04-19 08:11:36** by **mindeye**:

So... that's actually a case of user error on my part - they're only .25" so the first pass didn't actually cut them hardly at all... which means the second pass cut the whole .75" depth of plywood at once. I think because it only had to go an eighth of an inch it was ok but I bet that would snap a bit pretty quick if you kept doing it. By far the best cut I've gotten out of the Maslow. Turns out changing direction on the last cut causes more harm then good because it tends to skitter around not really cutting properly. This is the first one where I left both passes counter-clockwise and it came out much better than where I ran it counter, then clock.

---

Posted on **2017-04-19 08:40:26** by **scottsm**:

That's a valuable insight, that using clockwise causes issues. Who would have thought that 0.05" was enough meat to cause trouble? Also that cutting the reliefs on the last pass worked so well - that simplifies the process a lot.

---

Posted on **2017-04-20 22:39:35** by **kaboomfox**:

+1 for northgate! get mine in may.

---

Posted on **2017-04-20 22:49:15** by **sparhawk2k**:

We certainly need a local user group of some sort... :)



And thanks again to Mindeye. It was really helpful getting to see it.

---

Posted on **2017-04-26 12:43:02** by **Bar**:

@mindseye, can I put a picture of your box joint in the weekly update and encourage others to meet up and share ideas?

---

Posted on **2017-04-26 12:45:41** by **TheRiflesSpiral**:

How did I miss this?! Joinery with Maslow! That's impressive stuff. The box joint is totally underrated in my opinion. Dovetails seem to dominate box/drawer joinery discussions but I'll take a simple over/under any day! Way cool.

---

Posted on **2017-04-26 13:09:52** by **mindeye**:

@Bar, you have my approval to use anything I post here. If it helps encourage people to do neat things how can I argue?

---

Posted on **2017-04-26 13:34:33** by **Bar**:

Thanks! Thanks for doing neat things that encourage other people to do neat things!

---

