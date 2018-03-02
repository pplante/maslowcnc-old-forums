## The Weekly Wednesday Update is Up!
Posted on *2017-03-08 16:47:02* by *Bar*

https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1826692

We're trying something new this week with splitting the update into a technical update for the beta testers and a general progress update for everyone.

We've been getting a lot of feedback that people are feeling overwhelmed by the technical details. We get that a lot of people just want to build awesome stuff and not worry about the way the software works internally.

As always, we don't have any secrets so both updates are available for everyone to read if you are interested.

You can find the general progress update here: https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1826692

And the technical update here: https://www.kickstarter.com/projects/1830738289/maslow-cnc-a-500-open-source-4-by-8-foot-cnc-machi/posts/1825395

What do you guys think of the new structure? 

Is there a better way we can stay completely transparent without overwhelming some of our backers with technical details?

---

Posted on *2017-03-08 16:58:22* by *davidlang*

moving my comment from there to here (so more people see it)

I don't care that much about one update vs two, but I really dislike having most of the update be in a video. You can't skim a video, it doesn't get indexed in search engines to find it later. Please reserve the video for demos and put the important info in text (it's probably a good idea to have the update text be posted here as well rather than people having to go elsewhere to find it)

Also, in the video you say that with the high-friction sled you see the chains getting too little tension on the edges, since you measure the tension, how little is too little?

---

Posted on *2017-03-08 21:24:02* by *Bar*

Thank you, that's good feedback.

I don't actually measure the tension in a real world unit like kelograms or pounds, but we could. I consider the tension to be too little if there is any noticable curve in the chain.

---

Posted on *2017-03-09 04:31:45* by *davidlang*

ok, so the kinematics doesn't take chain curve into account :-)

---

Posted on *2017-03-09 06:51:33* by *TomTheWhittler*

Bar, People are still asking questions in the comment section of Kickstarter that you should answer.

---

Posted on *2017-03-09 07:57:27* by *rancher*

I can't seem to find any news in the update on shipping?

---

Posted on *2017-03-09 08:11:53* by *tmaker*

Personally, I like the video format.  Plus it allows us to actually SEE what you're talking about which seems like the most efficient way to communicate certain things.

---

Posted on *2017-03-09 09:46:32* by *Bar*

@TomTheWhittler thanks for the heads up, I'll check those right now. The KS comment system is hard to keep tabs on because there are just so many places to leave comments.

@rancher We didn't say anything, but nothing has changed. The PCBA factory is till telling us the 10th is their delivery date. We have all of the rest of the parts counted and bagged so we should be able start shipping immediately when the PCBs arrive.

@tmaker Thanks! I think a good system might be to show things in the video, but also make the accessible through the Wiki so that they can be reviewed later too

---

Posted on *2017-03-09 10:38:54* by *jbarchuk*

Tmaker, yes, that makes sense. It's often easier to get information across in a verbal and show-and-tell- format. When (in this case for example) it comes to getting across specific dimension, speeds, angles or whatever, it's better to have it in text format. That's where the wiki comes in. Whatever important facts happen, that need to be looked up quickly instead of watching a vid again to find it, should be recorded in the wiki.
Another advantage of text/web page format is that things can be changed easily. When a narrator makes an error of fact, later when they find out about it the only way to change it is to edit the vid and put a note on the screen with the correct fact.

---

Posted on *2017-03-09 12:20:11* by *Bar*

Thanks for keeping me honest guys. Posting a video about how to use the wiki to store important information for everyone's benefit and then not including information in that video in the wiki is silly!

I've posted the diagrams from the video with explanations on the wiki here: https://github.com/MaslowCNC/Firmware/wiki/Proposed-Changes-to-Firmware-Archetecture

---

Posted on *2017-03-10 00:48:07* by *jamesbil*

Great updates guys, keep up the good work.
I liked the what's in the box page. Tho it did raise a question...
I would have quite a bit of the mounting hardware in my workshop or available to me locally.
Have you considered offering a maslow "lite" as an option?
So all of the essentials; motor, wiring, board etc, but none of the items easily available; screws, bolts, some of the brackets etc. Maybe even the chain. Include a list of parts needed so we can source locally.
This might keep down shipping costs for overseas and also keep down import tax costs for backers in the eu.
Just an idea..

---

Posted on *2017-03-10 10:24:07* by *Bar*

I tried to keep the hardware simple and universally available as possible :-) 

The hard thing to keeping the cost down by reducing the number of parts is that a lot of the cost comes from things that don't end up in the box like liability insurance (It took 2+ months to find someone who would even answer my calls after finding out what we're building, insurance companies don't like weird new types of power tools). We could take out the wood screws and common bolts, but those don't reduce our costs much. Reducing the shipping/VAT costs for the non-US world is a big priority. We're hoping to find a way to ship from within the EU which should help reduce cost and time.

---

Posted on *2017-03-10 12:19:30* by *jamesbil*

Thanks for the reply Bar, I'm deffinately not complaining about the cost of maslow, you have put so much work and resources into it. I was just thinking about the weight for shipping and any way to lower import tax is welcome.

---

Posted on *2017-03-10 14:58:37* by *TomTheWhittler*

Humm. What if you put in in a bigger box and filled the empty space with a couple helium balloons.. ;)

---

Posted on *2017-03-11 03:07:24* by *spatialguy*

Come on Tom, this forum is not for silly comments! Hydrogen is twice as light as Helium!! lol Perhaps add a warning sticker on the box)

---

Posted on *2017-03-11 07:34:02* by *TomTheWhittler*

I know. I should have put it in the "non-judgemental section".  ;)
Although Hydrogen is twice as light as Helium there is that additional shipping cost problem of "potentially hazardous material". I believe the goal here is less cost and not shipping the customer a "surprise".

---

Posted on *2017-03-11 07:35:37* by *spatialguy*

Agreed

---

Posted on *2017-03-11 14:31:36* by *spatialguy*

@bar Re: Friction: There is a product that I have used here for years here in Australia and likely there too called silver-glide. It will reduce the friction and not affect the workpiece. Another easy option would be to laminex the base. An iron and a router and it will be done in 30min.

---

Posted on *2017-03-13 07:58:08* by *mindeye*

In the US and UK, that product appears to be sold as Silbergleit for others looking in similar locales.

---

