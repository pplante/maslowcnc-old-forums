## Stepper motor with gearbox
Posted on **2017-06-16 05:43:11** by **kentthoresen**:



---

Posted on **2017-06-16 05:45:52** by **kentthoresen**:

I have hired a programmer to change the code so it can run stepper motors.  It wil be realesed as a fork on git.  I plan to use a nema 34 and a gearbox. If anyone can help me bug test as we release i would apreciate that. let me know.

---

Posted on **2017-06-16 06:48:54** by **scottsm**:

Can you give links for the motor and gearbox you’ve chosen?

---

Posted on **2017-06-16 07:41:42** by **kentthoresen**:

Of course the motors and gears i selected are over dimensioned you can also use a nema 24 stepper motor with a similar gearbox. Gearbox 24:1 : http://www.ebay.com/itm/112200189215?_trksid=p2057872.m2749.l2649&var=412406181485&ssPageName=STRK%3AMEBIDX%3AIT 

Motor: http://www.ebay.com/itm/New-sale-2Axis-wantai-Nema34step-motor-with-1232oz-in-for-cnc-router-plasma-/322320015870?hash=item4b0bc521fe:g:y5QAAOSwnbZYH~Fk

---

Posted on **2017-06-16 07:47:12** by **davidlang**:

it will be interesting to see if that gearbox has enough resistance to being backdriven that the motors don't rotate when power is off.



otherwise, you need to re-calibrate the chains each time you power up.

---

Posted on **2017-06-16 08:26:30** by **scottsm**:

It wouldn’t be hard to develop the habit of hanging or propping the sled up before shutting down. Another approach, if the top links of the zero position are marked, is to re-hang the chains and be close to center. By turning the sprockets to have a point up before re-hanging, one can be very close.

---

Posted on **2017-06-16 09:35:19** by **TheRiflesSpiral**:

What's the motivation for going with steppers instead of motors with encoders? Just curious... I'm having trouble finding an advantage.

---

Posted on **2017-06-16 12:01:55** by **TomTheWhittler**:

If the application is for moving a much lighter sled ,like with a laser engraver, you could use geared steppers. You could then use a raspberry PI CncHat to drive the steppers.

---

Posted on **2017-06-16 12:18:40** by **kentthoresen**:

I have thought a bit about calibration i will try to find a way to auto calibrate when its starts up.  I will have to see how far i get in this first round.  The reason i go with steppers is that i can run it off standard stepper motor drivers i only need the arduino and stepper drivers, i can also runn it on Pi or other maker kit. I dont need any spesialised electronics, only shelfware. i can also use seperate powersupplies so its reliable. Steppers also have very good position control at low rpm with great torque.  With the gearbox i get over 300 kg of torque on the sprocket and very fine position controle with 50 000 pulses per revolution. The accurasy will be superbe.

---

Posted on **2017-06-16 20:31:32** by **davidlang**:

a stepper with a 24:1 gearbox is only 4800 pulses/rev. When you start microstepping you loose a lot of your torque (at about 10 microsteps you are down to ~10% of your rated torque)



I'd love to see a method to automatically measure the chains at startup, that is one of the issues right now.

---

Posted on **2017-06-17 01:06:30** by **kentthoresen**:

The torque loss on micro switching is why i will use large nema 34 motors they are 650W each. Its probably overkill but for a test i dont want to be short on power.. The resolution actually goes the other way with the gearbox it increases. 120 000 pulses per revolution at 24:1.  I have some ideas about the auto calibration with 3 end switches. basically one on each top end and one at the bottom on one side, then i can triangulate. If anyone has any other ideas on auto calibration i would love to hear them.

---

Posted on **2017-06-17 04:01:14** by **davidlang**:

you have to have a pretty good idea of where you are to be able to get the sled to hit the switches.



if you happen to be near the top left corner, you don't want to pull the sled towards you, and if you are near the bottom right corner you don't want to let the chain out.



so you don't even know which way you can safely move the motors.

---

Posted on **2017-06-18 01:41:40** by **kentthoresen**:

Yes its challenging with calibration, i was thinking to have the chain itself trigger the switch.  If i make some adjustments to a chain lock i can have it trigger a opto switch  by having a few such chail locks i can get very accurate measurements of the chain.  I dont know yet i need to experiement a bit.

---

Posted on **2017-06-20 08:37:45** by **kentthoresen**:

Version 1 ready is there any way i could get this pushed to git?

---

Posted on **2017-06-20 09:07:44** by **TheRiflesSpiral**:

You'll need to fork the project and post a new project. I'm fairly certain Bar isn't going to want to mix the code bases.

---

Posted on **2017-06-20 09:26:07** by **Bar**:

Great work! That's fantastic that it is done so quickly.



Yes, TheRiflesSpiral is right, you would want to maintain a separate fork for the stepper version. That way it will be easy to update one version from the other.

---

Posted on **2017-06-20 09:41:39** by **kentthoresen**:

Ok i will make a fork.

---

Posted on **2017-06-20 11:00:11** by **kentthoresen**:

I havent used github for forking before hopefully i did it right the stepper motor support version schould be ready for testing.

---

Posted on **2017-06-20 11:04:26** by **kentthoresen**:

Could you guys help me out bug testing? By the way feel free to do as you pleace with the modifications

---

Posted on **2017-06-20 12:12:18** by **scottsm**:

Could you post a link to the fork?

---

Posted on **2017-06-20 14:07:10** by **kentthoresen**:

My bad. 



https://github.com/kentthoresen/Firmware

---

Posted on **2017-06-22 03:40:44** by **kentthoresen**:

How long are the chains?  gearboxes has arived.



 [20170622_121321](//muut.com/u/maslowcnc/s3/:maslowcnc:ysyo:20170622_121321.jpeg.jpg)

---

Posted on **2017-06-22 04:20:53** by **davidlang**:

the chains are 11' long

---

Posted on **2017-06-22 04:35:46** by **kentthoresen**:

Thanks

---

Posted on **2017-06-22 13:27:41** by **eserv**:

I get error class'axis' does not have any field called "stepper'

 What am I missing?

---

Posted on **2017-06-22 22:49:05** by **kentthoresen**:

The stepper library isnt included for some reason?  Are you using an old version of arduino? or maybe sjekk your library folder see if you have al relevant libraries.

---

Posted on **2017-06-22 23:36:04** by **kentthoresen**:

i see somre errors in my fork please use this one https://github.com/algobasket/MaslowCNC-Stepper-Motor-Firmware

---

Posted on **2017-06-23 14:06:58** by **eserv**:

If you will bear with me and excuse my lack of knowledge, where do you put the software when you "clone or download it?

---

Posted on **2017-06-24 01:38:52** by **kentthoresen**:

Wherever you want i guess ?  i usually put it in my arduino folder under documents

---

Posted on **2017-06-25 23:45:27** by **kentthoresen**:

Changing to  worm gearbox. After testing the initial gearbox i have desided to move to a worm gearbox To avoid the router moving when powered off. http://www.ebay.com/itm/NEMA24-NEMA34-NMRV040-Worm-Gear-Reducer-Ratio-10-15-20-25-30-40-50-60-80-100-1/112192290866?ssPageName=STRK%3AMEBIDX%3AIT&var=412367175525&_trksid=p2057872.m2749.l2649

---

Posted on **2017-06-26 11:29:56** by **mooselake**:

Sorry about the lateness, been tied up.



About nine days back @kentthoresen made a comment about torque loss due to microstepping.  That's actually a complicated subject, but there's a lot of myths surrounding it.   The short answer is you won't actually diminish the ability to move the motors, just the fractional step positional accuracy that's suspect anyway.  Microstepping drivers are quite inaccurate to start with (+/- 10 or higher percent numbers are regularly mentioned, best case), and stepper step positioning isn't always that great either.   Microstepping was intended to give smoother motion - rather than jerking from step (often 1.8 or 0.9 degrees) to step microstepping lets you move in smaller and smoother increments.  To continue with the short answer, assume you're probably ending up with full steps anyway but you were jerking around a lot less on the way.  The long answer involves some serious search-fu (it's been discussed a lot) and study.  Add going to open loop (steppers with no positional feedback) from closed loop (dc motors with encoders) and it's tak ing another potentional positional accuracy hit that won't include any hardware feedback.



Since you've already put the cost way above that of a maslow (those gearboxes are already a big chunk of the total cost),  I'm guessing that this is being done for the joy of development rather than trying to save money (nothing wrong with that, lots of users would rather improve the machine than just cut out parts, I lean that way).  Have you given any thought to using servos instead of big steppers?  Home switches would solve the turn on problem, although you still have to figure out how to not pull the chain that's not being tightened off the sproket.  A third switch to detect the impending end of chain, as you only need it on the first homing, perhaps?  Or using servos with built-in brakes?



Since you're making such a large departure from the original firmware intent perhaps you could investigate modifying smoothieware, LinuxCNC (BBB perhaps?  Plug-in kinematics is designed in already iirc), or one of the higher powered processor firmwares?

---

Posted on **2017-06-26 12:14:43** by **kentthoresen**:

You are right its purely for the joy of developing, i just love machines.



As far as stepping and power goes i am using nema 34 80V 7,8 amp motors now with a 20:1 wormgear. It easily lifts my body weight



Anyway servos could work, good idea, i might try that later. Smoothie etc are also probably worth looking at. Thats far down the line ill see how far i go.



For the chain i think i have a solution if i modify chain locks i can make  the trigger switches, im testing it out now.  ill see if it works like i want it to, i will need to park the machine i think to make the calibration work.

---

Posted on **2017-06-28 09:35:12** by **mooselake**:

Whoops.  Called into work early and never hit the send button.



Sounds like a lot of fun!  You might be able to lift a small car with those motors and gearboxes.  Keep the router stationary and just move the garage around :)



Calibrating/zeroing a Maslow is a lot more complicated than the usual Cartesian machine since it's a lot more than just steps/mm (inch, furlong, whatever) and the usual terminology doesn't work.  Not sure what "parking" means in this context.  My mental concept of homing is to bring the chains to their shortest position on each side (if lower left is 0,0 then 0,max and max,max) with the trickiest part being what to do with the right chain when homing the left one.   Embarrassing to break the right chain if it starts too tight (well, it'd probably just stop the moving chain), also embarrassing to run it off the pulley if it's too loose. Bar's probably explained all this somewhere I've missed.

---

Posted on **2017-06-29 00:44:50** by **kentthoresen**:

Moving the garage! that is definately the next project! 



For homing my current thinking is to use chain locks and exstend the locking plate on one side, By putting the lock plate on oposite sides i can trip 2 switches iwill call them A and B for Left C and D for right. One set on the left side of the chain and one on the right. by alternating the sequence at the start and at end of the chain i get the following switch sequence at minimum A.B and B.A at maksimum for left and C.D etc for right. So homing the left chain could be as easy as run right hand chain until D.C then home left to A.B Then left to B.A and right to C.D  Im pretty sure i can calibrate accurately this way.

---

Posted on **2017-06-29 02:48:14** by **davidlang**:

can you do a diagram? I don't understand exactly what you are suggesting.

---

Posted on **2017-06-29 02:54:57** by **kentthoresen**:

Basically i would add a standard chain lock and change the lock plate so it exstended beyond the chain. If you look at the picture you would get to spikes above the chain. By adding a switch that is triggered by the spike i could get a signal in a spesific sequence. this would tell the system if its the end or the beginning of the chain. [85249](//muut.com/u/maslowcnc/s1/:maslowcnc:qNLT:85249.jpg.jpg)

---

Posted on **2017-06-29 03:05:10** by **davidlang**:

where would you put the switches?



I guess if you put them on the slack side of things you could just run the chain out until you hit them. But this may end up with the sled sitting on the ground if the other chain is also out far enough.



you can't retract the chain unless you know that the other chain has enough slack, and if you run out the other chain as you would need to in the top center, it would drop the sled to the floor if you are at a bottom corner.



but, as always, I could be wrong. try it and let us know how it works.

---

Posted on **2017-06-29 03:12:50** by **kentthoresen**:

i think the best place to put the switches is on top of the sprocket, that way i have a presise location the chain has to move through.  By putting the switches on the chain at a point where its far enough out to calibrate the left side i think i dont need to drop the router to far. Remember i dint need the entire chain out. I only need to let the machine know where it is in relation to the chain. so if i always park the machine so it can begin with the correct position of the right hand chain then calibrating the left schould be easily done.

---

Posted on **2017-06-29 04:44:50** by **davidlang**:

well, if you start with the presumption that you know where the router is (it's "parked"), things are easy. with worm gears you have almost zero backdriving of the gear, so if you just remember where you were when you shutdown, you don't need to do any detection/measuring (this is how the maslow software operates now)



Problems come when you have an emergency shutdown or disconnect so that you aren't parked and didn't get a chance to save your position.

---

Posted on **2017-06-29 07:55:30** by **kentthoresen**:

Well as long as i have both ends, i can find out where the printer is, For example if both chains are run out the first to read "the end" and calibrate from there.

---

Posted on **2017-06-29 09:20:26** by **davidlang**:

yes, as long as there isn't any damage done (including kinking chains) from the router sitting on the floor.

---

Posted on **2017-06-29 14:29:26** by **mooselake**:

Just some wild ideas from looking at the assembly pictures, since the real thing hasn't made it to Mooseland...



I'm a bit leery of the bungee cords and s hook, but a roller switch that would actuate mid-travel in the slack loop (pushed sideways by the chain? optical?) would give you a mid-span position.   This assumes that the middle of the chain won't hit the floor, and allows enough slack so the other side can be fully retracted, or that there's a position where that's true.  "Home" to that, using the slack (already actuated) side first if there is one, to prevent the dreaded floor bump.  Then home to minimum tightness at Xmin, then Xmax,   On Xmax you know how much chain you can let out.  The downside is 4 switches, two per axis.



Can you intercept an unexpected power drop while there's still time to save the current position in the EEPROM?  Never attempted that with an Arduino, and a quick search shows Atmel recommend external brown out detection circuitry.  Constantly updating the EEPROM probably isn't a good idea.



http://www.atmel.com/Images/doc1051.pdf

---

Posted on **2017-06-29 14:40:53** by **scottsm**:

On my ‘mostly’ standard version of the frame, the take-up side of the chain varies too much to accommodate an accurate ‘home’ switch. I’ve painted the links that sit atop the sprockets when the chain cal. finishes, so when I want a quick re-cal I hang the sled with those atop the sprockets and use ‘Advanced/manual calibrate’. This stores the cal. chain lengths as the current location. I’ve also put a peg above the work area so I can hang the sled up to take tension off the chains. These two things seem like they would be useful with a stepper setup.

---

Posted on **2017-06-30 02:02:25** by **kentthoresen**:

My main reason for moving to a worm gear is to make sure it doesnt drop on power off.  @scottsm sounds interestin do you have a picture or something, this could be a quick fix option until we find some permananet solution.  BTW i got the new worm gears today and its so ridicilously overkill, force testing it my scale maxed out at 400kg and snapped off with a loud bang. It seamed like it still had loads of torque to go on. If you make a stepper version nema 24 is more than enough as long as you have a worm gear.  A high power nema 34 like i use is way way way over the top.  I will scale down once the testing is done.

 [20170630_105658](//muut.com/u/maslowcnc/s3/:maslowcnc:CMmd:20170630_105658.jpg.jpg)

---

Posted on **2017-06-30 09:10:10** by **mooselake**:

For many years my mental project list has included adapting a DIY panel saw (like the now out of production http://a2equipment.com/ ) to CNC by moving the panel; Maslow's a more practical solution - although with those motors you use an endless chain loop to move the sheet.

---

Posted on **2017-07-08 01:44:00** by **kentthoresen**:

Here is the wire diagram for using exsternal drivers. [Wirediagram](//muut.com/u/maslowcnc/s1/:maslowcnc:oXQm:wirediagram.jpg.jpg)

---

Posted on **2017-07-08 14:15:30** by **mooselake**:

Cohesion3D sells an inexpensive adapter to go from a pololu socket to external drivers.  Handy if you're using a RAMPS, or C3D's mini

---

Posted on **2017-07-09 00:38:12** by **kentthoresen**:

thanks i have another project where i need this.

---

