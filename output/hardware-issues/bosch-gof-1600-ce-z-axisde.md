## Bosch GOF 1600 CE Z-axis/depth adjustment
Posted on *2017-05-06 21:41:33* by *mcginniwa*

Moving this from [My Z Struggles](http://www.maslowcnc.com/forums/#!/general:my-z-struggles) to it's own thread since it's evolved to be about Bosch router.

Read the end of that thread for background.

So I'm happy to report back that I've overcome the depth limitation problem I seemed to have with the fixed base. It's a matter of set up of the bit depth, the macro depth adjustment, and the Z-axis/fine depth adjustment position when you place the motor in the fixed base. Thanks @larry357 and @davidlang for the help.

However, I am still seeing some Z-axis issues. I think these can be overcome by adjustments to plunge depth speed in your cutting files and/or router motor speed. Possibly feed direction as well?

Basically I saw two remaining issues:

* torque on the Z-axis assembly during circular cuts where the Z-axis was plunging and meeting resistance. I.e. there was horizontal pressure on the bit while Z-axis was adjusting. The base clamp lever being unlocked may make this work by introducing more play into things. I.e. the bit can move more side-to-side than it would  with things locked down

* the macro depth adjustment lever sometimes moving as if it had been released during Z-axis adjustments - this may have happened during the torquing behavior. Not sure what was going on when it happened.

I do feel like I've made progress though and that the Bosch fixed base should work once the kinks are worked out.

---

Posted on *2017-05-07 01:36:58* by *larry357*

Good that you are making some progress, I did notice that the hole closest to the spindel would make it all wobble a bit more than if it was in the middle one. I ordered some router bits that are 50mm long with 25mm cutting part as the shorter the better I guess... But without a machine to test on I`m not that much help :)

---

