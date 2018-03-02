## Router Requirements - esp. z-axis
Posted on *2017-05-17 01:23:42* by *julian7*

I have ordered a Maslow for the UK, so I need to find a suitable router. The AEG branded Ridgid router would cost over twice what the Ridgid costs in the US, which is silly. Is anyone able to say exactly what requirements the router has to meet?

For example, this (http://www.screwfix.com/p/triton-mof001-1400w-dual-mode-precision-plunge-router-240v/6768K) is the router I use in my router table. How can I tell if this will work with the z-axis kit?

---

Posted on *2017-05-17 01:33:19* by *gero*

If the knob on the top can move the router up and down full length and can be taken off, exposing a shaft to mount the cuppler, then it will work. 
Perhaps the Bosch can give a idea what to look for https://github.com/MaslowCNC/Mechanics/wiki/More-Photos

---

Posted on *2017-05-17 01:38:35* by *davidlang*

you would be operating it in 'fixed base mode' with the rack and pinion adjustment for the height. That looks like it's done by the big knob on the side of the router. You would have to figure out how that comes apart to see if there is a reasonable way to hook a motor to it. I suspect that you will end up with some sort of belt drive, and end up needing to attach the motor to the moving part of the router.

It would not be my first choice. I'd probably look at doing a shop built router lift first. Are there no fixed-base routers available in your area?

---

Posted on *2017-05-17 01:51:16* by *carlosizsak*

Hi Guys, I'm based in the UK as well and interested to find out what router will work best with Maslow, any comments most welcome, thanks

---

Posted on *2017-05-17 01:55:01* by *gero*

@ julian7 https://www.youtube.com/watch?v=91RsAjy200Y at 2:40 the Miro adjuster knob looks like it would work. I see a screw , since you have that router, take a look.

---

Posted on *2017-05-17 05:36:51* by *carlosizsak*

Julian, it would be great to know if you think this will work, as will consider getting a Triton if so, I wonder which z axis component we would need though

---

Posted on *2017-05-19 10:09:58* by *pips*

i'm also very interested if this works. I need a UK router with z axis but cant seem to find any confirmation which one works

---

Posted on *2017-05-20 01:05:37* by *carlosizsak*

Hey pips, lets stay in touch and share info please

---

Posted on *2017-05-20 07:19:43* by *gero*

For me this calls for a second list to the existing 'Tested Routers List'.
How would you do a wiki page 'Suggested Routers List' where one could add the pros and cons he sees remotely and/or holding it in his/her hands?

---

Posted on *2017-05-20 07:21:26* by *gero*

Plus the regions it is available.

---

Posted on *2017-05-20 07:33:20* by *gero*

When it comes to the question, “Will this router work with the Maslow?”, I sit down a few minutes with my consultants YouBooze and Giggle.

Regarding the ‘Triton MOF0001 / 1400W’, YouBooze provided me with this video: https://www.youtube.com/watch?v=JU6u9legomk and from 0:29 to 0:58 I was convinced that this router is fit for an automated Z-Axis.
I asked Giggle for ‘Triton MOF0001 Parts’ and was presented with this diagram: http://www.toolsparesonline.com/images/diagrams/330085%20MOF001%20Router%201400w.pdf
The shaft in question is Part # 31.6
I don’t think Giggling the diameter of #31.6 would answer the question what coupler needs to be ordered. Someone has to unscrew #30, take #31 to #31.5 off and measure #31.6.
I also found this page, you can order parts and collets:
http://www.toolsparesonline.com/category/940-plunge-router-1400w-mof001-330085.aspx
Other than that you get collets for 6mm and 1/2’  (1/4’ and 8mm seem to come with the router), this router seems highly repairable, as you are able to order each part separate. (You will find #31.6 but no diameter)
Questio ns remaining are:
- Shaft diameter
- What is the 1400w compared to the 2HP Ridgid R22002? Not Giggling that. If it’s the same or higher, perhaps slightly lower, fine. (2000 W  ~ 2.68 HP)
- Height? Hight might be considered with the Z-Mounts that come with the Z-Motor. Not Giggling the hight either. On a Bosch I solved the hight quick and dirty like this:
https://camo.githubusercontent.com/0c168e7aff0b397b7d37a8cd7affaa41a63631e7/68747470733a2f2f646c2e64726f70626f7875736572636f6e74656e742e636f6d2f732f6b676a643239736f7a7265747370732f5a322e6a7067 Yes, there are more pretty solutions. Just not now.
- Weight? 6.2 kg is in the higher range, but till now I can’t see that as a minus.

Personally, I read quite a few reviews of a tool and I need to hold it in my hand and play with everything, to take the last decision. I have no chance to do that in the near future.
I would love to this router in action on a Maslow-UK or soon though.

---

Posted on *2017-05-24 01:14:14* by *pips*

can anyone confirm a working UK router with z-axis support? I want to order the z-axis upgrade but need to decide on router first

---

Posted on *2017-05-24 23:16:21* by *martinnisted*

What about the cheaper model JOF001? http://www.tritontools.com/en-GB/Product/Power%20Tools/Routers/JOF001

Will this router work with z-axis support?

---

Posted on *2017-05-25 00:09:24* by *davidlang*

that link fails for me with a server error.

---

Posted on *2017-05-25 05:26:46* by *TheRiflesSpiral*

Martin, that router appears to have the same "fine adjustment" knob as the MOF001 so I think it should work fine.

---

Posted on *2017-05-30 10:50:17* by *gero*

On the Triton TRA001 the shaft diameter is 3/8"
http://www.maslowcnc.com/forums/#!/general:shaft-coupler-size 
Thanks to skuba

---

Posted on *2017-05-30 14:13:44* by *TheRiflesSpiral*

@gero @skuba Should we add the Triton TRA001 to the tested routers list? https://github.com/MaslowCNC/Mechanics/wiki/Tested-Routers-List

---

Posted on *2017-05-30 16:18:03* by *gero*

@TheRiflesSpiral I suggested a page with "Routers that could work" before. I hope @skube will be chipping some amazing projects soon.

---

