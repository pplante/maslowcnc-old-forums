## Z axis control
Posted on **2017-03-21 17:09:25** by **thatoneguydavid**:

I have been working on a unique solution for Z axis control with a couple of my friends.  here is what we have come up with at this point. 



we started from a DeWalt trim router. (DWP611)  its a bit less powerful than the original router suggested (1.25HP vs 2.25HP) but it spins a bit faster (max of 27Krpm vs 23Krpm)



https://www.amazon.com/gp/product/B0048EFUV8/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1



the interesting thing about this router is its depth control mechanism.  when the black collar on the top of the base is rotated the motor moves up and down.  The idea was to add a belt drive sprocket to this collar, and drive this from a servo.

we chose to use the following motor: Pololu item #: 2827



https://www.pololu.com/product/2827



this motor has a gear head and an encoder.



the gear head added to this is from stock drive parts:  A 6H25M016DF0906



https://shop.sdp-si.com/catalog/Product.aspx?id=A_6H25M016DF0906



the orange gear was modeled by a friend starting from a SDP model that turned out to not be a good model.  the teeth are pretty much non existent. (this  is being updated)



the motor mount i built using parts from  MicroRax:

http://www.microrax.com/MicroRAX-Home-10.html



the ultimate goal is to bring AC power to and enclosure on the sled.  in that enclosure there would be a small microprocessor with Bluetooth connectivity. 



the processor would:

* drive a relay to turn on the router

* control the z height servo

* control the router speed (by modifying the router with a digital pot instead of the thumb wheel pot on the stock router)

*monitor the encoder for stall condition if the height adjustment is for some reason bound up.



eventually a z-height calibration would also be added to the system for after a tool change.  the idea would be that somewhere on the frame of the cutter there would be a calibration location where the z-height would be lowered until a sensor (tac switch, pressure sensor, gap sensor, etc.) is tripped.  this would be a fixed location so from that index the z-height can be adjusted to the surface of the material.



as i complete these pieces i will post my progress as well as files for the community to use.



 [IMG_4299](/images/m2/m2ip_img_4299.jpg.jpg) [IMG_4300](/images/nl/nldp_img_4300.jpg.jpg) [IMG_4298](/images/zy/zyde_img_4298.jpg.jpg)

---

Posted on **2017-03-21 17:13:03** by **Bar**:

Gorgeous!

---

Posted on **2017-03-21 17:13:54** by **thatoneguydavid**:

thanks, is there a way to upload vid to this forum?  i could post that little clip i sent you.  or i guess you could (smile)

---

Posted on **2017-03-21 17:15:01** by **Bar**:

If you link to a youtube video it embeds pretty nicely automatically, that's the only way I've found :-)

---

Posted on **2017-03-21 17:33:05** by **thatoneguydavid**:

here is a quick video i just shot.

https://youtu.be/qfpYpDCoaiw

---

Posted on **2017-03-21 18:17:12** by **Bar**:

Beautiful!

---

Posted on **2017-03-23 09:53:53** by **rexklein**:

I am unbelievably humbled by that. errr..... Uhmm..... how much to you want for that piece of art. I am happy to pay I already have that router. Man that is so cool

---

Posted on **2017-03-23 09:59:26** by **thatoneguydavid**:

thank you for the kind words.  

when the next version of the gear is tested i will be posting a file for print.   I am also working on a sheet metal version of the motor mount bracket.  i will keep this thread up to date with progress.

---

Posted on **2017-05-18 10:11:20** by **thatoneguydavid**:

video is a bit choppy, but here is V2 of the printed gear.

https://youtu.be/IjgobAI4znk

---

Posted on **2017-05-18 10:52:31** by **Bar**:

That's awesome! So smooth.

---

Posted on **2017-05-18 10:54:34** by **thatoneguydavid**:

thanks!  

im really getting excited about it.  should have a print file to upload in the next week.  there is a bit of tweaking to do on the I.D.  i will be interested to see if the maslow can cut it.....

---

Posted on **2017-05-18 14:34:35** by **rollandelliott**:

I'd buy that too. or if you dont' want to get into making them maybe upload stl to thingverse? That is a TON of nuts and bolts to make the 90 degree support though! bent sheet metal or even two pieces of plywood with L brackets or angle iron would be much less work.

---

Posted on **2017-06-05 11:09:14** by **thatoneguydavid**:

Yes, i agree that there is a lot of hardware to make the bracket.  if you look a little further back you will see that a sheet-metal version is in the works.

---

Posted on **2017-06-05 11:14:49** by **thatoneguydavid**:

as promised, i am now uploading the link to the custom gear for Z-axis system i have been working on.



https://grabcad.com/library/64-tooth-htd-pulley-1



there are two parts that must be glued together as most home 3D printers have limited overhang capabilities.



this is designed to work with this router:

https://www.amazon.com/gp/product/B0048EFUV8/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1



the rest of the parts i have used are listed in previous posts in this thread.

---

Posted on **2017-06-05 11:18:18** by **davidlang**:

I will point out that you aren't saving much money with that router, it's only $30 cheaper than the suggested one and has 1/2 the HP and only a 1/4" collet

---

Posted on **2017-06-05 11:18:51** by **davidlang**:

but I guess if you already have it ...

---

Posted on **2017-06-05 11:56:19** by **thatoneguydavid**:

i was not trying to save money, i already had it and it seemed like a great mechanism for adding z-axis control.  if i do end up needing more power i will switch to this version:

https://www.amazon.com/DEWALT-DW618-Electronic-Variable-Speed-Fixed-Base/dp/B00006JKXB/ref=sr_1_1?ie=UTF8&qid=1496688933&sr=8-1&keywords=DEWALT+DW618

and design a new collar gear.

---

