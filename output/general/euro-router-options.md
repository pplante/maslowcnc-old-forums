## Euro router options
Posted on **2017-02-10 01:20:32** by **jamesbil**:

Believe it or not, If you were to swim east from the US (or fly), once you hit the shores of Ireland and headed deeper into Europe you would find it very difficult to find a fixed base router with an adjustment system suitable to Maslow's z axis motor. 
Also they are all very expensive. Ideally I would like to use a smaller 1/4" router.

This is intended to be a list of routers available in IRL, UK and EU suitable for Maslow's z axis. Some have been mentioned here already.
I am in no way afilliated with any router company or shop.

AEG €335 http://www.rotopino.de/oberfraesmaschine-aeg-mf-1400-ke,34018
5.7kg, 
Bosch €400 https://www.dm-tools.co.uk/product.php/section/4748/sn/BSHGMF1600CE#.WJ2Ag9SLTGh
4.3kg
Triton €270 https://www.iedepot.ie/woodworkers-router-best-ireland/
I have the bigger on of these which is identical, I''l take a video of it later.

Other options are to diy it, something like this https://www.iedepot.ie/gmc-plunge-trimmer-router-quarter-inch/ with the threadded adjuster bar bolted in to the base plate. Probably have to remove the spring too.
Here is s omething that might help, https://woodworkersworkshop.co.uk/products/router-technologies-router-raizer-rz100 again, alot of money.

@davidlang came up with some good options, I like this motor and add a homemade lift https://www.aliexpress.com/item/New-Arrive-0-8kw-Air-Cooled-Spindle-Motor-Cnc-Square-Milling-Machine/32767045510.html?spm=2114.01010208.3.17.kfW9rc&ws_ab_test=searchweb0_0,searchweb201602_4_10065_10068_10000074_10000032_119_10000025_10000029_430_10000028_10060_10000067_10 is it powerful enough?
Also beware of buying from some sites. Over here all products need to be certified with a CE mark. Some unscrupulous companies will fake this.

---

Posted on **2017-02-10 09:30:46** by **jamesbil**:

Here is a video of the Triton, what do you think, will it work with the z axis?https://m.youtube.com/watch?v=zKC9Dpo31AQ

---

Posted on **2017-02-10 09:42:29** by **thomasgkristensen**:

I wonder if the Bosch 1400 would work? https://www.bosch-do-it.com/gb/en/diy/tools/pof-1400-ace-3165140451697-199905.jsp

---

Posted on **2017-02-10 09:43:05** by **Bar**:

That Triton a really really cool router. I've never seen anything quite like it. I would expect it to work well with the z-axis. I couldn't tell quite how the adjustment handle attaches to the shaft, but if you think it would be possible to connect that to a motor shaft I expect it will work really well. 

This thread is a great resource. Thank you for compiling this information for everyone.

---

Posted on **2017-02-10 10:01:31** by **thomasgkristensen**:

After seeing your video I'm really hooked on the Triton. Could you provide the measurement for the shaft? I think you have the 2400 watt model? 

If I order a Triton router now it won't be here until the end of the month and I'd like to add the z-axis option as soon as possible in time for the early beta shipment. Therefore it would be great if you could provide the shaft size.

And thanks for a great video!

---

Posted on **2017-02-10 11:15:26** by **jamesbil**:

A few pics of the shaft adjustment setup. @bar would you mount the z axis above or is there space below the shaft?
 [IMG_20170210_180020](//muut.com/u/maslowcnc/s3/:maslowcnc:JM5n:img_20170210_180020.jpg.jpg) 
 [IMG_20170210_180028](//muut.com/u/maslowcnc/s3/:maslowcnc:EYeR:img_20170210_180028.jpg.jpg) 
 [IMG_20170210_180035](//muut.com/u/maslowcnc/s3/:maslowcnc:0ER2:img_20170210_180035.jpg.jpg) 
 [IMG_20170210_180054](//muut.com/u/maslowcnc/s3/:maslowcnc:YmOk:img_20170210_180054.jpg.jpg) 
Last pic is it fully lowered.

---

Posted on **2017-02-10 13:06:12** by **Bar**:

Is the top knob removable? On my router there was a screw on the top of the knob and when I took it off I got a nice shaft that was easy to couple to. 

I think that the top is going to be easier. The total length of the motor/gearbox/encoder is 105mm which looks too long to fit with the router fully lowered. You could CNC some wood gears which would let you mount the motor next to the shaft maybe and drive it from the bottom? You've got a little bit of a tricky situation where the motor needs to be able to move with the router. I think that there is probably an elegant solution, I'll keep thinking on it.

What a cool looking router.

---

Posted on **2017-02-10 13:18:07** by **jamesbil**:

Thats right, the knob comes off, I think the video shows it. I hadn't thought about the fact that the z motor needs to be attached to the router motor somehow.. methinks some clever fabrication is in order.
Do you know how much weight the z motor will lift? Whatever router is used, it is turning a shaft that has the weight of the router on it.

---

Posted on **2017-02-10 15:21:05** by **Bar**:

The z-axis motor has a good amount of torque. It's quite a bit stronger than what I can turn by hand, so that's probably a good indicator. If you really need a lot of torque, the motors which control the chains are a drop in substitute and those have an incredible amount of torque.

---

Posted on **2017-02-10 19:19:52** by **davidlang**:

does the ball of the adjustment shaft latch into the base somehow? (so that it can pull the router down to the base) That isn't clear from the pictures

---

Posted on **2017-02-11 01:02:26** by **jamesbil**:

No, the shaft doesn't move up or down, it just turns. You can see the teeth on the plunge post. There is some kind of worm gear inside the housing that works on this post to raise or lower it.

---

Posted on **2017-02-11 07:51:57** by **jamesbil**:

@thomasgkristensen the top of the shaft fits a 10mm spanner and has a 4mm threadded hole in the centre. Here are a few more pics, what do you think about mounting the z motor on a 300mm slider which is fixed to the ply base plate. This will allow the z motor to slide up and down with the router motor without having to fix into the body of the router.
 [IMG_20170211_151641](//muut.com/u/maslowcnc/s3/:maslowcnc:H7Oo:img_20170211_151641.jpg.jpg) 
 [IMG_20170211_151727](//muut.com/u/maslowcnc/s3/:maslowcnc:60VN:img_20170211_151727.jpg.jpg) 
 [IMG_20170211_151751](//muut.com/u/maslowcnc/s3/:maslowcnc:8IUI:img_20170211_151751.jpg.jpg) 
 [IMG_20170211_151759](//muut.com/u/maslowcnc/s3/:maslowcnc:nTnx:img_20170211_151759.jpg.jpg)

---

Posted on **2017-02-12 10:20:07** by **thomasgkristensen**:

Thanks for the measurements! I thought the motor wouldn't need to move but if the router motor moves I guess it does. A slider sounds like a plan in that case. 

Once again thanks for the measurement!

---

Posted on **2017-02-13 08:55:24** by **TheRiflesSpiral**:

That's a fairly unique arrangement I've not seen before. It looks like the adjustment shaft has a worm gear on it that rides in the teeth on another shaft. In that case, the adjustment shaft is going to move up and down with the router. Odd...

I think your drawer slide idea is brilliant... They're surprisingly resistant to twist when collapsed like that.

---

Posted on **2017-02-17 14:29:03** by **neilmunro**:

Noticed these (1400w) model are only
 £165 in Argos...

---

Posted on **2017-02-26 00:13:06** by **edou**:

What would be the Z-axis shaft coupler size for the Triton 1400 router? I ordered the router, how to measure the required size correctly?

---

Posted on **2017-02-26 00:28:28** by **jamesbil**:

There are schematic drawings for it on the Triton website. If it is the same as the 2400 watt model the top of the shaft fits a 10mm spanner.

---

Posted on **2017-02-26 06:08:38** by **neilmunro**:

I should get mine end of next week as Argos is out of stock just now. Will post measurements when it arrives....

---

Posted on **2017-02-28 12:38:42** by **neilmunro**:

Hi everyone, just received my Triton model no. MOF001 (1400w model).
I've had a look at the height adjustment shaft and without stripping the whole machine, it looks like we need to attach onto the hex head. The internal hole is 1/4" so rather small to cross drill a shaft inside it...
The hex dimensions are as follows:
Across the flats: 9.33mm
Across the corners: 10.64mm
length of flats: 5.5mm
For completeness, the hole is a few thou shy of 1/4" (sorry 6.22mm ) and the length of the hex is 14mm.
I shall be asking for an 8mm coupler and drilling out 9.3mm then slotting some flats on it in my lathe...
BR   Neil

---

Posted on **2017-02-28 12:49:07** by **neilmunro**:

PS
If you have someone in the family who works at Sainsburys, they get at least a 10% discount at Argos!

---

Posted on **2017-02-28 12:52:52** by **neilmunro**:

PPS
The range of movement is just over 100mm...

---

Posted on **2017-02-28 13:30:04** by **jamesbil**:

I was wondering how to attach that. Could something be done with a 10mm socket from a socket set?

---

Posted on **2017-02-28 13:44:01** by **neilmunro**:

Hi James, I intend to make a female hex in the adapter / connector. This will then fit snugly onto the hex on the machine. In the cnc world to maintain accuracy as much backlash / slop needs to be removed as possible. The connector is only aluminium, so will be easy to machine. It will also having multiple parts involved ...
A 10mm socket would be slack, so each time the stepper motor changes direction, it will take a number of steps to take up the slack..

Bar, can you confirm the encoder is on the motor please?
Thanks
Neil

---

Posted on **2017-02-28 15:05:35** by **Bar**:

I can confirm that the encoder is on the motor :-)

---

Posted on **2017-03-01 00:19:47** by **jamesbil**:

Thanks for the explanation Neil, this makes things a little difficult for those of us without access to a machine shop. We could do with a simple universal solution if one exists. Could something be done with the threaded hole? Bolt the coupler to this, would locktite help prevent it from unscrewing?

---

Posted on **2017-03-01 14:05:28** by **ptrick**:

Triton reviews suggest some quality issues
https://www.amazon.co.uk/Triton-MOF001-Precision-Plunge-Router/dp/B002QS1LPM/ref=pd_sbs_60_7?_encoding=UTF8&psc=1&refRID=WB93SMPWJCVW130BF9P7

Found an out of production ryobi
https://www.amazon.co.uk/d/Power-Routers/Ryobi-ERT1400RV-1-4-inch-1400-W/B004EK231Q

Thinking about trying to rig a plunge router i have.. using the guide rods connected to a motor that will when rotated  pull down the handles with some connected webbing or wire ..

---

Posted on **2017-03-02 14:59:41** by **neilmunro**:

Jamesbil, 
I appreciate not having a shop makes this go difficult. 
When we communicate by such messages we need to remind ourselves that everyone has different requirements, resources, expectations, knowledge and budgets 😕.. These are the things which tend to cause upset and frustration! 
1st, the hole in the centre is not tapped. It could be drilled out to 1/4 inch and a rod glued in. However I want to be able to use my router as it was intended as well as on the Marlow. 
Another solution could be to make a 3d printed nut to fit over the hex and into the supplied adapter. This will need to be a hard plastic such as nylon. I am talking g to a mate about it, but he can be a bit flaky!

---

Posted on **2017-03-02 15:04:11** by **neilmunro**:

Ptrick, 
Yes, saw a few negatives, but also it has a 3 yr guarantee with positives about returns. Mine looks and feels good so far! 
It definitely is much better than Chinese quality😊

---

Posted on **2017-03-03 00:13:44** by **jamesbil**:

@neilmunro I didn't realise it is not threadded on the smaller version, I have the bigger router which is threadded to accept a screw that holds the adjuster knob in place.

---

Posted on **2017-03-03 13:15:18** by **neilmunro**:

Hi Jamesbil, 
As you have a threaded hole, it makes things so much easier....
Suggest you get a large diameter coupler. 
Get a rod with a hole drilled right through as a clearance size for the thread of a cap screw (allen key bolt) which fits the threaded hole in the machine.
Drill through a clearance size for the head of the screw leaving about 6mm of material so you can screw the rod to threaded hole using the capscrew. (some loctite wouldnt go amiss here).
Finally fit the coupler to the rod... job done!

---

Posted on **2017-03-16 00:44:38** by **edou**:

[IMG_20170316_080607](//muut.com/u/maslowcnc/s3/:maslowcnc:7sDf:img_20170316_080607.jpg.jpg) 
Am I correct that the Z-coupler should connect to the hexagonal top of part 34 “Metal Worm Shaft” on the Triton MOF001 1400W router?

Technical diagram http://www.tritontools.com/Helpers/GetImage.ashx?type=ExplodedDiagram&size=&name=MOF001.pdf

Am I measuring it correctly between the two flat sides? @neilmunro, it is 3/8inch right? Anyone can validate this?

---

Posted on **2017-03-16 01:30:58** by **davidlang**:

that would be my guess as to the right part, but you need to measure across the points, not the flats (the points need to be able to fit in the hole of the coupler shaft)

---

Posted on **2017-03-16 01:47:55** by **edou**:

@Bar Could you change my Z-axis shaft coupler to 10mm in light of this new info?

---

Posted on **2017-03-16 10:07:36** by **Bar**:

Yes, absolutely. Can you email Hannah@maslowcnc.com and let her know? She's the organized one :-)

---

Posted on **2017-07-14 14:51:20** by **metrowave**:

Well I've got a Triton tra001, most likely I've ordered the wrong coupler. Is it possible to buy the Maslow coupler separately? I live in UK.

---

Posted on **2017-07-14 16:35:04** by **mrfugu**:

Please be sure to report your successes and failures here: https://github.com/MaslowCNC/Mechanics/wiki/Tested-Routers-List

---

