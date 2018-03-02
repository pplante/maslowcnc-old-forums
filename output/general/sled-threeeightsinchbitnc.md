## Sled-ThreeEightsInchBit.nc?
Posted on *2017-04-26 12:10:18* by *MikeT*

Would it be reasonably easy to generate a sled file for a 3/8" diameter router bit? If not, I can go out and buy either a 1/8" or a 1/4" bit. I bought a 3/8" bit because it looked beefy enough to cut all the way through a sheet of 3/4" plywood, but I don't have a lot of experience with routers, so maybe I should have gotten a smaller-diameter bit instead. (I'm doing the "Using The Temporary Frame To Cut Parts" step.)

---

Posted on *2017-04-26 12:12:39* by *Bar*

Yes, absolutely!

---

Posted on *2017-04-26 12:22:24* by *Bar*

I'm generating a 3/8ths version right now, but I also want to plug the new method described [here](https://github.com/MaslowCNC/Mechanics/wiki/Using-the-Temporary-Frame-to-Cut-Parts#step-11-generate-g-code) which guides you through the gcode generation process. 

That way by the time you get the machine built, you already know how to design parts! Let me know what you think.

Also, if you have the instructions open, you can just refresh the page, I rewrote them last night.

---

Posted on *2017-04-26 12:24:38* by *MikeT*

OK, I'll look it over. The sooner I learn about Gcode, the better.

---

Posted on *2017-04-26 12:26:28* by *Bar*

It might be worth starting with a part simpler than the sled, I'm going to change that picture right now

---

Posted on *2017-04-26 12:35:39* by *Bar*

If you refresh the page, the picture of the sled will be updated to match the other pictures :-)

---

Posted on *2017-04-26 13:59:21* by *MikeT*

I'm about to check calibration by cutting the test shape. The test shape file in the All Gcode Files zip file (the one that also contains the two Sled-?&quest;?InchBit.nc files) is named 6 Inch Square Test Shape - Quarter Inch Bit.nc. It's not going to work with my 3/8" diameter bit either, so I'd like to convert it for my router bit size in MakerCAM. But MakeCAM only imports .SVG files, right? So do you have a .SVG version of the test shape?

---

Posted on *2017-04-26 14:19:48* by *Bar*

Great question. There is one. Give me a second to find where it is. I will update the wiki instructions page with the link also.

---

Posted on *2017-04-26 14:29:57* by *Bar*

I'm going to work on integrating those steps into Ground Control next week so there is just a "cut test shape" button, the bit size will be important. Thank you for catching that. 

I've added the .svg file to the folder [here](https://github.com/MaslowCNC/Mechanics/blob/master/SVG%20Files/AllPartsSVG.zip) and updated the wiki page to say that it is an option.

---

