## Ground control won't run
Posted on **2017-03-17 14:55:57** by **blsteinhauer88**:

Got my kit today, installing ground control  and installed per the instructions. Ran the batchfile and briefly saw an error message flashed on my screen. Had to use my iPhone to film it so I could slow it down and grab the frame to see what it says .  I have no idea what it means, if anyone can help me out? I would appreciate it thanks.  [IMG_0430](//muut.com/u/maslowcnc/s3/:maslowcnc:90jt:img_0430.png.jpg)

---

Posted on **2017-03-17 15:56:27** by **jbarchuk**:

I have the same issue. A little googling reveals that it affects various software, and different fixes worked for different people. Thirty years later and Windows is still not much more that a stinky bucket of wormy ones and zeros.

---

Posted on **2017-03-17 16:20:17** by **scottsm**:

I had this issue, misty memories about a security setting dealing with dlls... 

 I could cd into the GroundControl directory and run GroundControl.exe directly from there, though :)

---

Posted on **2017-03-17 16:29:25** by **Bar**:

Good recommendation @scottsm! The batch script is really just a shortcut to the GroundControl.exe file in the GroundControl folder. If you try to run that file directly do you see the same issue? What version of windows are you using?

---

Posted on **2017-03-17 16:35:47** by **blsteinhauer88**:

Yes, it did the same thing, Windows 8.1.  Success though!!  I got in and up and running with the "source code" way through Python.  It was easy.  Just had to get the paths correct, and then in the instructions there are a couple ">" left on the string of text.  Once i took that off it took the commands fine.

---

Posted on **2017-03-17 16:38:07** by **scottsm**:

I think Windows is protecting us from an unregistered app or developer; Win10 puts up a SmartScreen alert (which one can opt around via the 'more info' link) for the .bat file and for the .exe as well. Protection is a good thing, not sure how to clean this up.

---

Posted on **2017-03-17 16:47:44** by **Bar**:

Great news! I'm glad you got it to work :-). The 'source code' option is a good one, but it can be a little technical so I want to have an easy option for everyone. From doing some reading that issue can be caused by a security thing like @scottsm is saying or by the way I'm packaging the app. I'm going to keep investigating and find a solution which will work for everyone.

---

Posted on **2017-03-17 17:43:08** by **Bar**:

I removed the ">" from the instructions. Thank you for pointing out that those were confusing.

---

Posted on **2017-03-17 18:10:09** by **blsteinhauer88**:

Thanks, It must be a windows thing for the "easy" way to run it.  I did re install from the Zip file and this time got window warning with the "user account control" that it was going to make changes to the hard drive.  It did not start even thought I accepted the risk.  If that helps any.

---

Posted on **2017-03-19 16:20:47** by **Bar**:

Would anyone who had trouble running Ground Control give the GroundControl.exe file in this folder a try: https://www.dropbox.com/s/7arudbbzqmephyh/GroundControl.zip?dl=0 



Running the file file as administrator by right clicking on it may help.



:fingers crossed:

---

Posted on **2017-03-19 17:16:39** by **scottsm**:

The exe file runs as expected, all looks well on Win10. FWIW, I saved the .bat file from the previous install, it works too.

---

Posted on **2017-03-19 17:19:37** by **Bar**:

Woo! That's fantastic news. Thank you so much for testing it.



Did you need to run it in admin mode?

---

Posted on **2017-03-19 17:20:55** by **scottsm**:

No, I just selected 'Open'.

---

Posted on **2017-03-19 17:24:42** by **scottsm**:

Is it time for a new 'Release'? Does Build-OSX need to be updated? 

Too, GroundControl is using the Release system, Firmware not. Is there a danger of a mismatch between the two?

---

Posted on **2017-03-19 17:40:23** by **Bar**:

Great!



I was planning to do a weekly "Releases" with the update, but it seems like so much has changed/improved/been fixed in the last two days that it might be time already. I just brought Build-OSX up to date, if you would be so kind as to run the build again, let's do it!

---

Posted on **2017-03-19 17:42:05** by **scottsm**:

Got it, thanks. I'll send a link as before.

---

Posted on **2017-03-19 17:58:43** by **Bar**:

Awesome!



I agree that the firmware should really be on a release system too, and I'm going to do releases weekly with the update so we have older versions to go back to if we need.  I think having the directions point to the latest possible version is good for now because things are getting better so quickly that having the five o'clock version is better than the two o'clock version is way better than the eight am version

---

Posted on **2017-03-19 18:39:20** by **Bar**:

For anyone reading this late, there is a new version up here: https://github.com/MaslowCNC/GroundControl/releases which in theory solves the problem. If anyone has issues with it, let me know and we'll keep at it.

---

