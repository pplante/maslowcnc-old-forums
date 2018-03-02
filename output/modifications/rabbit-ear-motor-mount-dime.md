## rabbit ear motor mount dimensions, per workspace dimensions
Posted on **2017-02-11 19:50:53** by **jbarchuk**:

There's a very interesting page that talks about the math involved in calculating v-plotter line tensions vs workspace dimensions. http://2e5.com/plotter/V/design/

Maslow was obviously designed with some baseline calculations to determine the optimal position for the rabbit ear motor mounts. The design dimensions suit a 8' wide x 4' tall workspace.

Folks have mentioned working in 5x5 and 4x8 'portrait' oriented space, and I intend to build a 4-5' wide by 2-3' tall space.

The Q is what formula do we plug those numbers into to determine the exact dimensions of the rabbit ears?

It's (maybe? should be?) possible to use the -ratios- of the dimensions in the design to scale to other workspace dimensions. However 1) That's a PITA to do by hand. 2) I don't know how -valid-a simple scale ratio would be. 3) It's a maaaajor major PITA. 4) 100 or 200 or however many people who are going to build non-standard dimensions will have to go through the major PITA of figuring ou t the ratios, with the usual number of math errors (faulty dimensions) which worst case results in a machine that loses accuracy at the limits of travel. 5) It's a reeeeally major PITA to do that all by hand.

---

Posted on **2017-02-12 00:21:40** by **davidlang**:

That's a very interesting article, but it has some pretty significant assumptions built into it.

1. it assumes that the minimum useful tension is 0.5 * mass of sled

  the lower these can be, the wider the lower section is.

2. it assumes that the maximum useful tension is 1.5 * mass of sled

  the higher these can be, the higher the center section is

3. it assumes that the max acceptable error is 1.4 * motor step size

  the higher this can be, the narrower the orangecenter section is

it's hard to say if these are valid for the maslow or not.

I would say that with chain instead of string, high tension is unlikly to be a major problem.

Adding weight to the sled increases the tension at all times, so makes lower tension ratios more reliable (the basic design adds bricks for weight, so they are already addressing this, even if it was just empirically)
 
the worst resolution that's acceptable is very subjective, saying that it's only 1.4* chain step size is very questionable, it's very easy to get additional resolution on the motors (at least when you are designing them) and so I would expect that this would be better than expected.

I also would not have guessed that the worst resolution was at the top-center.

This does mean that it's probably more important to have the motors high over the workpiece than having them wide (which surprises me a bit) and leaves a bunch of interesting room for experimentation on the exact dimensions to use. The nice thing is that the 'wings' are not shipped, they are cut on-site, so the design can be easily tweaked.

---

Posted on **2017-02-12 00:22:25** by **davidlang**:

ok, I should have looked at the preview, the asterisk character has special meaning on this form, sorry.

---

Posted on **2017-02-12 01:10:03** by **davidlang**:

Thinking about the problem here.

max tension is when the chain would break or the motors were unable to maintain the tension without moving.

Based on what Bar has said, the motors he is using are significantly more powerful than he thinks they need to be, so the max tension should be able to be quite high.

for the minimum tension, the hard limit should be the point where the force of the blade against the wood is higher than the force of gravity holding things in place. This is going to vary based on the power of the router, the cutter used, and the variations in the wood (hitting a knot in a piece of solid wood is going to be far more of a problem than cutting MDF for example), adding weight to the sled will help this

---

Posted on **2017-02-12 04:27:32** by **davidlang**:

doing some digging and playing around with this program produces some interesting info.

The motors that Maslow uses are 30Kg/cm and 8148 encoding pulses/rev driving 10 pin sprockets (just a hair over 1cm radius)  with type 25 (0.25"/link) roller chain

this roller chain has a minimum strength of 350Kg
the shipping weight of a R2200 router is ~10lb (box and all)
bricks are ~4.5lb each

call the sled weight around 22lb or 10Kg

so the max tension the motors can support is ~3x the total sled weight

The motors have just over 5 encoder steps per 1/64" of chain movement. As such, accuracy limits due to encoding steps are essentially nonexistent (the max in the program can be changed from 1.4 to 50.9)

playing around with the parameters, it looks like a tension of around 2Kg (minimum tension of just over 0.2*sled weight) results in a calculated accurate cut area of 4'x8'

the plot is at http://lang.hm/maslow/maslow.png
the modified python code is at http://lang.hm/maslow/v-plotter.py

you should be able to trivially tweak the image size and the separation of the motors to see  what the resulting good cutting area is.

It look like this spacing will easily handle 5" tall wood, just move them up by a foot.

to do portrait mode (8' tall by 4' wide) it looks like you need a spacing of ~6' (vs the stock 9.8' spacing) although some added weight could let you narrow that (or if it will cut reasonably with less tension)

---

Posted on **2017-02-13 10:37:09** by **Bar**:

+1 for that python! Since the software knows the dimensions of the machine, it would be easy to incorporate that that visualization into the machine's visualization of the work-space making it 1) really easy for everyone to test their ideas for different machine dimensions and 2) if someone has a build which is of a not optimal size (due to room size constraints or something) it would remind them where the best parts of the work-space to cut on are. 

The only change I would make is that there isn't really a cutoff at which things just stop working it's more of  a gradient so in the light blue you can still cut, but probably with reduced resolution. It might be good to show it as a gradient to give everyone a better understanding.

Are you comfortable with me taking your code and incorporating it into Ground Control?

---

Posted on **2017-02-13 18:17:12** by **davidlang**:

It's fine with me, but the majority of the code is from 2e5.com and there is no license provided there.

where in the code are the machine dimensions defined?

I was also thinking of changing the color based on the accuracy rather than just the cutroff, but haven't gotten around to it (and I also didn't know how much the results of this simulation actually match reality of the machine)

I would expect that when the tension isn't enough, the movement is unpredictable in the lower corners, and this will vary depending on the friction of the sled.

I suspect that the honeycomb plan is more likely to catch on things instead of sliding better if cut with a vertical bit, but possibly if cut with a shallow v it would be better.

While I agree that it's a great idea to have the basic design be all-plywood, but it would be interesting to see how much difference it makes if you were to use something like that sams club cutting board.

---

