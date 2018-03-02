## Anyway to run via Mobile instead of a laptop/PC
Posted on *2017-06-14 16:31:51* by *tntahan*

So I just read the update and saw that OnShape was mentioned. I have been using SketchUp And Fusion 360, but thought I would check out OnShape. I noticed that you can use it on your phone/ipad/whatever to not only view, but to edit as well. That is the only CAD software I have found that lets you do that so I thought that was pretty cool! So with that said, it made me think, is there any way to run ground control from your phone/ipad so everything from design to cutting on the Maslow can be done like this? Anyone have any idea of what that would take to make it work?

---

Posted on *2017-06-14 16:46:29* by *TheRiflesSpiral*

I think there's an Android implementation of Python so Kivy should be okay too... I think the biggest challenge will be serial communications.

Also, check out my.sketchup.com it's a slightly less capable Sketchup in an HTML 5 browser.

---

Posted on *2017-06-14 17:05:52* by *Bar*

Someone in the community compiled Ground Control for Android a while back and it ran great. We never tested the serial connection which would be the tough part like @TheRiflesSpiral said. It's on the to-do list, but after we fix all the bugs :-)

---

Posted on *2017-06-14 17:14:10* by *TheRiflesSpiral*

Oh sweet! I missed that. You've probably already seen [this](https://www.allaboutcircuits.com/projects/communicate-with-your-arduino-through-android/)...

---

Posted on *2017-06-14 19:53:22* by *Bar*

I hadn't seen that. Very cool. It's reassuring to know that someone else has done the serial side of things successfully so we know we're not starting from scratch.

---

Posted on *2017-06-18 15:22:34* by *davidthomasgross*

http://www.techworld.com/picture-gallery/apps-wearables/great-programming-apps-for-your-ipad-3497769/

---

Posted on *2017-06-18 15:32:43* by *davidthomasgross*

Maybe if you access the camera connection kit we use it for midi data so it is assiible I think

---

Posted on *2017-06-18 17:54:07* by *scottsm*

Pythonista3 brings python, but beyond that we would need to get someone to bring pyserial and kivy to IOS. The camera connection kit might require some hacking to get it to talk to the Maslow.

---

Posted on *2017-06-18 18:07:27* by *davidlang*

search the iphone store for grbl and the controllers that finds should work with the maslow (once it's setup anyway)

---

