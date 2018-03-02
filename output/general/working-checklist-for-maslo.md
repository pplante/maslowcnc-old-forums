## Working Checklist for Maslow Setup
Posted on **2017-07-13 08:30:52** by **nathanmiller**:

In preparation of my Maslow I've been scrubbing the wiki for all items I might need to get it up and running. So far I have this list put together: 

https://docs.google.com/document/d/1O9q6mmUd9QyshDdgfv8O5HRPfRO7hF-rQ1jPLTVJpTQ/edit?usp=sharing

Could you have a look and let me know what needs to be added, modified or removed? Once it's solid I'd like to add it to the wiki:

---

Posted on **2017-07-13 08:46:58** by **mrfugu**:

The standard Rigid router has a 1 1/2" OD dust collection attachment included, I'd recommend adding a 8-12' x 1 1/2" hose (to keep weight as low as possible) and then couplers to whatever size Shop Vac/dust collector you might have.  You'll probably want a nice long USB Cable as well, in order to keep your computer as far away from the machine as you'd like.

---

Posted on **2017-07-13 11:24:03** by **nathanmiller**:

all excellent additions. Thanks.

---

Posted on **2017-07-13 11:43:58** by **mrfugu**:

In an ideal world, there would be pins on the motor shield that auto start  the router and dust collection system, with a big safety paddle interrupt switch, that also told GC that it's been tripped, allowing the machine to re-home and re-start exactly in place from the interrupt point. I don't think we're quite there yet.

---

Posted on **2017-07-13 12:28:12** by **scottsm**:

There are six gpio pins on the board that could be used for that. The Maslow folks have chosen not to control power for their own very good reasons, but it shouldn’t be too hard to set up for one’s self.

---

Posted on **2017-07-13 13:17:29** by **nathanmiller**:

As to the checklist, if there is some sort of kill switch one could put inline with the router power. I could list it as an optional item on my list. 
Maybe there is some sort of extension cord that would have an emergency stop toggle inline?&quest; I've searched Amazon but can't find anything set up like that.

---

Posted on **2017-07-13 13:25:45** by **nathanmiller**:

In light of previous comments I have added "extension cords" to the list. Thanks for the input. :)

---

Posted on **2017-07-13 14:30:45** by **davidlang**:

I like this emergancy off switch, given the size of this machine you may want one on each side

http://www.rockler.com/safety-power-tool-switch

---

Posted on **2017-07-13 19:17:24** by **rollandelliott**:

that switch looks pretty cool, but for $5, one can just mount a electrical box and switch inside of it.

---

Posted on **2017-07-13 19:18:01** by **rollandelliott**:

add a 18' circle of UMHW plastic for the bottom of the sled to reduce friction.

---

Posted on **2017-07-13 19:23:50** by **mrfugu**:

this issue is still unresolved, see friction discussion here: https://github.com/MaslowCNC/Mechanics/issues/20

---

Posted on **2017-07-13 19:39:29** by **nathanmiller**:

I like the ideas being listed, the emergency switch and the alternative bottom sled material, but I think we might want to hold off for a bit. The checklist is all about getting started with Maslow, not about perfecting it.

---

Posted on **2017-07-13 19:41:02** by **nathanmiller**:

Also, what's the best approach for adding this checklist to the wiki? Or is there a better place (and format) to use?

---

Posted on **2017-07-13 19:45:02** by **mrfugu**:

the wiki appears to be the ideal place, specifically the https://github.com/MaslowCNC/Mechanics/wiki

---

Posted on **2017-07-13 20:01:25** by **mrfugu**:

see this discussion thread for related guidance from Bar: https://github.com/MaslowCNC/Mechanics/pull/68

---

Posted on **2017-07-13 20:33:34** by **davidlang**:

@rollandelliott, it's a lot harder to hit a regular switch than that big red paddle, and when things go wrong you want the switch to be as easy to hit as possible (I like to have it where it can be hit with a knee as well as by hand)

---

Posted on **2017-07-14 06:16:39** by **nathanmiller**:

All the information gathered so far is on github in the wiki. You can see, and edit it here: https://github.com/MaslowCNC/Mechanics/wiki/Initial-Setup-Checklist
Thanks again for the help in identifying needed components. Feel free to add/edit the wiki as needed.

---

Posted on **2017-07-14 06:29:24** by **mrfugu**:

awesome! thanks!

---

Posted on **2017-07-14 07:44:29** by **TheRiflesSpiral**:

I updated the assembly instructions link to start at the frame assembly, rather than the sled assembly.

---

Posted on **2017-07-14 08:57:28** by **nathanmiller**:

perfect. Thank you TheRiflesSpiral!

---

