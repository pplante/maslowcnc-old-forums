## What part of the 4x8' sheet is most accurately cut with current firmware?
Posted on *2017-07-15 06:44:44* by *rollandelliott*

I know from reading the forum that the two lower corners suffer from inaccuracies due to long chain lengths.
A lot of my projects dont' need a full 4x8 sheet. Would it be a safe bet that using a 4x4 sheet is more accurate? How about if one only needs a 2x4' sheet of plywood. Where would one put the 2x4 sheet for best accuracy? dead center or top center?

---

Posted on *2017-07-15 06:57:49* by *mrfugu*

Take a look at the simulation thread. 
the outer edges, yes, the extreme top an bottom, a little less so. (obviously ensure the sled cannot interact with bottom of the stand)  
I note that in the simulation thread, Bar mentions that it is approaching the outer edge of tolerances what can be easily measured (+/-3-4mm) and aiming for tolerances that are difficult to measure (+/- 0.6mm).

---

Posted on *2017-07-15 07:52:28* by *gero*

I would say dead center, or slightly lower should give the best accuracy at the moment.

---

Posted on *2017-07-15 14:59:00* by *davidlang*

it depends on which dimensions of the machine are incorrect. Playing around with the simulation, some cause more errors at the outer edges, some cause more errors near the top with the bottom center being the best, some cause more errors the further you get from the center

the edges suffer more than the center, beyond that it depends which parameters are off.

---

