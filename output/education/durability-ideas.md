## Durability Ideas
Posted on **2017-03-23 07:06:01** by **mattnelson**:

Being that this will be used in a school I need to make the maslow as durable as possible.  One concern I have is the stretchy string.  Summer temps easily get to 110 degrees F and I'm wondering it the stretchy string will last.  I'm considering replacing those with metal springs or weights.  I've also been trying to figure out the best places to mount the Arduino where it won't get hit or banged but would still be easy to access.  Ideas?  What else could be done to make the maslow as kidproof as possible?

---

Posted on **2017-03-23 07:23:34** by **TheRiflesSpiral**:

Tensioning with a weight may be tough since the chain path is not parallel to the force of gravity... I've actually given this some thought, though.



What I plan to do is to attach a pulley where the hook is and run a fabric cord up to the motor mounts where another pulley would be. A weight can then hang parallel to gravity.

---

Posted on **2017-03-23 09:47:00** by **hannahteagle**:

@mattnelson in terms of the Arduino, I might suggest putting some easily-openable cover over it? Just something that snaps open and close to hopefully block some of those flailing kid arms :) I'm imagining something similar to those clear plastic thermostat covers

---

Posted on **2017-03-23 09:52:48** by **rollandelliott**:

clear acrylic or polycarbonate guards over the left and right sides will keep hands off and still allow a view of machine in operation.

---

Posted on **2017-03-23 12:38:17** by **jbarchuk**:

> @mattnelson

> What else could be done to make the maslow as kidproof as possible?

Don't let them near it? :) This machine has a number of minor to major hazard points. OSHA would have a field day with this one. :)

The router is the obvious hazard, but it makes a lot of noise which is always a red flag even to the less-than-seriously-safety-conscious.

The motor plus gear and chain way up in the air is not a major issue because it's not easy to reach.

My concern is the 'floating gear' because it lowers down to be in easy reach. It moves pretty slowly so it 'seems' less than dangerous. It's easy for someone standing but not facing the machine to back into it and get their hair wound up. It doesn't look dangerous. but touch it in a way that causes it to push a finger into the chain and there -will- be a bloody mess. The bungee plus rollers is a similar issue but not being metal on metal would cause slightly less damage to a finger.

I can't think of a way to put a guard over that whole portion of the machine. Well, it could be covered with a box of some sort but part of the  purpose of education is to let the kids see how the machine works and learn a bit about physics and machinery. To cover it with clear plastic is a -large- piece of plastic, which is expensive.

Regardless of guards I'd put yellow tape on the floor with verbal instructions and a couple of signs to -not- cross that line without direct adult supervision.

---

Posted on **2017-03-23 12:50:04** by **gero**:

Replacing the rubber bands is an idea I also have in mind. I need to see my Maslow in action to take that further. I was thinking of bricks on drawer slides, or something like that.

---

Posted on **2017-03-23 13:54:59** by **spyker**:

Let's be serious about the shock cord. 1/4" shock cord had a strength of 120 lbs, much more than the nema motors will ever put on it. Mil-spec varieties usually have a UV cover on them, and it's less than $20 for 50ft. So, for no change in design and $20, you can have lots of backup ready to go.  As far  ar protection for the Andrino and shield, use the Maslow to cut a lexan box (with ventilation), assemble it with Weld-On 16 polycarbonate glue, and screw it to the frame or wherever. Look into the Box-o-matic program for a tool that will actually create the g-code for a box for you. For only a few dollars, Pokano can cut it for you as well out of acrylic if you are worried about using the router.

---

Posted on **2017-03-23 18:16:16** by **davidlang**:

@spyker, remember that these are not nema steppers, they are dc motors with 200:1 gearing and ~30Kg-cm torque

---

Posted on **2017-03-24 06:45:26** by **spyker**:

@davidlang, even so, the machine has been tested and proven to work with it properly, so why add more cost and development time to the machine when the replacement cost for the part far outweighs the value add?

---

Posted on **2017-03-24 06:47:58** by **mattnelson**:

I'm not worried about the force of the motors or UV, the heat just destroys everything rubbery.   A metal spring seems to do the same function but will not have issues at 110-130 degrees F.

---

Posted on **2017-03-24 06:55:16** by **spyker**:

@mattnelson, I understand as I will be using mine in a San Antonio, TX garage in the middle of summer. I still feel that since Mil-spec bungie cord (MIL-C-5651 Spec) is tested at 158 degrees Fahrenheit ( within 2 degrees), it will be fine.

---

