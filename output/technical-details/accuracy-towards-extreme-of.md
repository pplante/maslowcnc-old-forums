## Accuracy towards extreme of working surface
Posted on **2016-10-27 10:18:12** by **olly_oneill**:

Firstly, I'd like to say I'm massive fan of your kickstarter idea and intend on supporting. I'm an architect in London but I also code and run a V plotter drawing machine at home to create artwork (https://www.instagram.com/olly_oneill_art/ if your interested) I'm also involved with some maker spaces and work for an architects collaborating with wikihouse currently. I have used 'trad' CNC milling machines for more than 10-12 years in different capacities

Does your machine stay accurate towards the edges of the working plane? I have some trouble personally with a slight 'warping' on the extremities of my large format machine v plotter. My machine is under a great degree of tension towards the top corners.

How do you accurately calibrate the size of the cuts using the v-plotter system? Does it need very accurate 'centring' on its home to get within 1mm accuracy towards the edge of the plane? My reason for asking is that I would like to use it to build an extension  my house and the biggest draw for this method of prefabrication is absolute accuracy.

I look forward to hearing from you and hopefully realising some projects with this device

---

Posted on **2016-10-27 10:38:02** by **sparhawk2k**:

There was a question below where this was answered in quite a bit of detail. http://www.maslowcnc.com/forums/#!/technical-details:question-about-accuracy-r

---

Posted on **2016-10-27 19:48:58** by **Bar**:

Those are GORGEOUS man! Hands down the most wonderful V-plotter work I've seen. Check out my other answer and let me know if you have any follow up questions. You clearly have a lot of relevant experience. Your question about centering is on point (<---Boo bad pun). The better job you do of telling the machine about it's dimensions and where home is, the more accurate the math will be. That being said, I don't do any crazy super hard core calibration stuff, I use a ruler and I'm moderately attentive to getting it right.

Can you share anymore about what you are planning to build? If you are waiting to surprise the world, I totally understand, and I can't wait to see it :-)

---

Posted on **2016-10-28 02:42:25** by **olly_oneill**:

Bar, 

I'd recommend the Stipplegen02 program if you want to try cutting some perforated images into a panel for practice/ calibration http://www.evilmadscientist.com/2012/stipplegen2/. The SVG output is perfect for vector based machines

Thanks for sending that link through. It certainly answers most my questions at the moment. Yeah can certainly share what I'm/we are planning on doing. 

Currently in discussions and planning with friends for a collaborative art piece for a UK festival next Summer. We want to build a giant mandala 3D slot together head made out of ply, paint it some crazy colours and project moving fractal images onto it. Its inspired partly by the Shaman @ Boom festival in Portugal we saw last Summer (https://www.youtube.com/watch?v=_zqbX2ORgZs). The proof of concept for this project is due to be laser cut very shortly.

Also, as previously mentioned will probably use it to extend my house if can get it working accurately. This will prob be quite a simple box layout as although aspiration is high, funds are low and I'm a die hard modernist at heart. Pr oposing to construct it using similar principles to the WikiHouse (slot together box sections filled with insulation). As you guess I will be cutting sections almost as big as large ply sheet. I'm always trying to get my V plotter more accurate and faster. Although its pretty good (uses pre-tensioned beaded cord onto a custom made 3D printed gear with a weighted pulley) the torque on the stepper motors always cause a little slippage. Its the pin point accuracy on the corners I'm looking for. I now run my machine at a very high steps per minute to get pieces done more quickly as some take over 30 hours, Consequently a right angle change of direction on mine sometimes causes a small curving 'kick' just after the turn. I think its momentum issue. Have you encountered this with the added weight of a router and two bricks?

Do you think your machine is capable of achieving similar accuracies to 'rack and pinion' (not sure what to call it) machine? What is your method of centering it on home currently?(assuming its on the sheet of material you have set up) (I currently set mine to the top of whatever size canvas/page I'm using but I can run the pen on and off the paper easily)

---

Posted on **2016-10-28 10:52:34** by **Bar**:

That projection mapping project looks amazing. That's exactly the kind of art/engineering project that I was hoping to see people building. 

The 'kick' that you are experiencing after turns is a thing that we have to deal with too. I think that is what will really put an upper limit on how fast the machine can move.  Fortunately for us, the cutting process is a lot slower than the drawing process so it's less of an issue. I'd like to add some dynamic acceleration ramping with look-ahead in the future so if that the machine is coming up to a right angle, it can calculate ahead to slow down and not overshoot. I think that would let us move a bit faster.

Comparing to a 'rack and pinion' machine is a little tricky because there are some really beautiful ones out there and some not so great ones. I'd say we can beat any rack an pinion machine in the same price range hands down (because I don't think there are any :-) ). But seriously, the really good ones with heavy frames are great. The really low end ones that use pretty cheesy aluminum extrusion and low quality gears are n't something I would want to work with. To make that kind of design work well, it really needs to be done right. Because Maslow is based around keeping all the parts under constant tension all the time, we can get away with more. I guess I'd say that if both designs had an unlimited budget, the rack and pinion machine would win which is why you see all the professional shops with $20,000+ machines built that way, if you are constrained in budget, I'd say the hanging design would win for accuracy (which is why nobody makes a $350 rack an pinion system)

---

