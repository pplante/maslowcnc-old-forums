## GC Crashing
Posted on *2017-05-01 10:02:45* by *mexicomillionaire*

Just downloaded and ran 0_69. It booted the first time without issues. Without connecting to the machine, I tried to load the test shape file. It crashed and now it loads (with the file) and then immediately closes. 

Has anyone else seen this? Re downloading and running has the same issue.

Is there a error log file or a temp file that can be looked at?

---

Posted on *2017-05-01 10:04:06* by *mattnelson*

Is this running in python or a precompiled build?  What OS?  Have you restarted the computer?

---

Posted on *2017-05-01 10:09:00* by *mexicomillionaire*

Restarted- Yes
Running windows 7
It is the windows portable version

I have been able to get 0_64 to run without issues

---

Posted on *2017-05-01 10:14:25* by *Bar*

:-(

I'm testing it right now to see if I can figure out what is going on

---

Posted on *2017-05-01 10:18:03* by *blsteinhauer88*

I had that happen, but it was a file size issue (too big).  The test pattern should not be doing that.

---

Posted on *2017-05-01 10:20:59* by *mexicomillionaire*

I was using the 6 inch . nc file that was on the github page.

Is there a log file that I can send you?

---

Posted on *2017-05-01 10:23:32* by *Bar*

Yes, there isn't a log, but there is an error message which will tell us what's wrong. Unfortunately it closes too fast to see by eye, but we can make it pause. 

Would you be willing to open the *Launch Ground Control.bat* file in notepad and add the word "pause" to the second line like [this](//muut.com/u/maslowcnc/s2/:maslowcnc:umxX:this.jpg.jpg) ?

---

Posted on *2017-05-01 10:34:28* by *mexicomillionaire*

Added the pause. Attached is the command window.

Here is the NC file I tried to load... maybe I got the wrong thing...

https://github.com/MaslowCNC/Mechanics/blob/master/Testing%20and%20Calibration/6%20Inch%20Square%20Test%20Shape%20-%20Quarter%20Inch%20Bit.nc

[0_69 error](//muut.com/u/maslowcnc/s2/:maslowcnc:baq6:0_69error.png.jpg)

---

Posted on *2017-05-01 10:37:59* by *Bar*

Perfect!

I'll figure out what is going on and fix it right now.

---

Posted on *2017-05-01 11:42:27* by *Bar*

I think I've got it tracked down.

Will you give this version of Ground Control a test?

https://www.dropbox.com/s/1nqbla5xmu2l3ci/GroundControl-Windows%20Portable.zip?dl=0

---

Posted on *2017-05-01 11:49:22* by *mexicomillionaire*

That has the same result. I copied the whole command window. Maybe there is some else in here. 

https://drive.google.com/file/d/0B6-vxtJzNE5BRVR6X3F4bkFDTkE/view?usp=sharing

---

Posted on *2017-05-01 11:51:44* by *Bar*

Hmmm :-(

---

Posted on *2017-05-01 11:52:16* by *Bar*

Can you send me the file (bar@maslowcnc.com) which is causing the issue? I couldn't get it to happen with my copy of that file

---

Posted on *2017-05-01 11:53:03* by *mexicomillionaire*

It seems that even the new version (or if I download and run from a different location) trys to open the same file. 

I deleted the file that I initially loaded. I now get an error saying it can't find the file but, it doesn't close now...

---

Posted on *2017-05-01 11:53:16* by *mexicomillionaire*

I am going to try a different file...

---

Posted on *2017-05-01 11:54:33* by *mexicomillionaire*

Is there another known good .nc file I should try?

---

Posted on *2017-05-01 11:56:11* by *Bar*

The settings are stored outside the Ground Control folder now so you don't have to re-enter your machine dimensions every time you upgrade

---

Posted on *2017-05-01 11:58:05* by *mexicomillionaire*

Ahh. Ok. That seemed to be the issue. Still curious what I have the issue?

---

Posted on *2017-05-01 11:58:31* by *Bar*

I would try the gCode in the "Gcode For Testing folder in Ground Control. The best way to get that folder is to download the whole source code by clicking the green download button in the upper right corner  [like this](//muut.com/u/maslowcnc/s3/:maslowcnc:YlOM:likethis.jpg.jpg)

---

Posted on *2017-05-01 11:59:07* by *Bar*

I'm not sure why that file wouldn't open. Do you still have the bad file in the trash can by any chance?

I'd love to take a look at it and make sure nobody else has the problem again in the future.

---

Posted on *2017-05-01 12:02:59* by *mexicomillionaire*

Here is the file from the trash. 

https://drive.google.com/file/d/0B6-vxtJzNE5BRDA4Z2l2OGhKcnc/view?usp=sharing

It was set to open with a G-code software from work (HSMworks). Not sure if this would have an effect. Only thing I noticed.

---

Posted on *2017-05-01 12:03:20* by *mexicomillionaire*

Do I need the new firmware to run this version?

---

Posted on *2017-05-01 12:05:29* by *Bar*

Thanks! I'll take a look at it and see what I can figure out.

You shouldn't need to change the firmware, but it wouldn't hurt. There's some pretty awesome new features since last week like the machine loads it's position on power up :-)

---

Posted on *2017-05-01 12:22:10* by *Bar*

I took a look at what's inside that file and somehow it's the HTML from the website :-)

I don't think we'll get g-code out of it, but that doesn't mean it's OK for it to crash Ground Control. I'll fix the crash for next week's release.

---

Posted on *2017-05-01 12:22:53* by *Bar*

We've got to find a better way to download individual files from GitHub because there seem to be lots of issues with the files it gives everyone.

---

Posted on *2017-05-01 12:31:28* by *Bar*

I fixed it so it won't crash anymore and it will try to load the file to the best of it's ability. I did my best to make Ground Control load gcode no-matter what it looks like, but this is wild

This file
---
G1 X3.9988 Y4.6809 
---

Becomes:

---
<td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">G1 X3<span class="pl-c1">.9988</span> Y4<span class="pl-c1">.6809</span> F15</td>
      </tr>
---

And it still renders  [kinda](//muut.com/u/maslowcnc/s3/:maslowcnc:Rxjn:kinda.jpg.jpg) . The circle becomes a line.

At least it doesn't crash anymore, hopefully no matter what we throw at it.

---

Posted on *2017-05-01 13:01:42* by *mexicomillionaire*

Ok. Yeah the G-code didn't look like anything I had seen before... I used to use EMC on my last machine before upgrading to MACH3. Good to know.

---

Posted on *2017-05-01 13:13:56* by *mexicomillionaire*

If it helps, I opened the test file in Github and copied the text into a new file. This is running without issue.

---

Posted on *2017-05-01 13:16:44* by *Bar*

Yeah, github seems to give really strange files sometimes. I'm not really sure what to do about it.

I'm glad we made it so Ground Control doesn't crash at least.

I wish the forums had more emoji. If this was on github I would do the thumps up emoji a couple times with maybe the 100% emoji and the fireworks emoji. Oh well :)

---

Posted on *2017-05-01 13:50:40* by *blsteinhauer88*

What if you opened a dropbox for Maslow, and there was a pointer to the files in Github to Dropbox?

---

Posted on *2017-05-01 14:08:56* by *Bar*

I really like that GitHub gives everyone the ability to propose changes to any file. Maybe you are right that we should give up on github for some files that people want to download often

---

Posted on *2017-05-01 14:16:33* by *blsteinhauer88*

I like it too, it seem that it is easier for others to get files  when they 'point' at a drop or google box.

---

Posted on *2017-05-01 14:24:51* by *davidlang*

I dislike how dropbox nags you to create an account or sign in when you are just retrieving a public file.

git (and therefor github) are really not designed to hold files that will be downloaded independently.

---

