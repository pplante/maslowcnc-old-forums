## How to set the speed of cut
Posted on *2017-04-09 13:15:00* by *nickandj*

We have set up the frame, calibrated the motors and the chains, and on our first cut, the speed was WAY too fast.  How do we change the speed?

---

Posted on *2017-04-09 13:54:23* by *carlosrivers*

Could you upload a video?

---

Posted on *2017-04-09 14:16:32* by *mattnelson*

This is done in the software you use to generate the .nc file.  Some are using makercam for this purpose.  The speed is called the feedrate.

---

Posted on *2017-04-09 14:24:52* by *scottsm*

I found the default federate in Makercam way too fast, too. I've been using 15ipm, but I don't have a lot of experience. If you don't want to go through the Makercam step again, you can edit the .nc file in a text editor, look for F60 (or F45 or whatever the speed was) and change it to F15 for 15 ipm (or choose your own feed rate). In GroundControl, I usually load some other file, then load the one I've edited, just to make sure that my changes are recognized.

---

Posted on *2017-04-09 14:58:24* by *Bar*

The latest (officially released next Wednesday) firmware also automatically limits the feedrate to a reasonable 25ipm to prevent this issue in the future.

---

Posted on *2017-04-09 17:24:53* by *justinbane*

We figured it out Bar, Nick and I are def the idiot  beta testers, but you need those too!

---

Posted on *2017-04-09 17:47:33* by *Bar*

Our goal is to make CNC accessible to everyone which means keeping it cheap and making it easy to use. If you are confused by something, it means it's confusing and we need to make it simpler. If you are every confused for any reason, please please please let us know. If you're confused that means 10 other people were confused, but didn't say anything.

---

Posted on *2017-04-09 18:14:14* by *justinbane*

Thank you bar, I will start by simplifying your comment, "Yes you are an idiot, but at least you are a loud idiot" :D Nick and I are working on our own Idiots guide to post, including classics such as.... " No idiot, in fact you do not attach your router base to the sled" as well as the always popular "Yes Virginia, some of those dots on the screen mean you have to turn your router off or bad things happen"....ever forward!

---

