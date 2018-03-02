## Firmware update tutorial?
Posted on **2017-03-28 11:43:59** by **rancher**:

Help.

---

Posted on **2017-03-28 12:04:49** by **Bar**:

The process to update is exactly the same as when you first installed the firmware, so the instructions are [here](https://github.com/MaslowCNC/Firmware/wiki/Firmware-Setup)

---

Posted on **2017-03-28 12:05:16** by **rancher**:

That way isn't working for me.  Oh lord how I've tried.

---

Posted on **2017-03-28 12:05:55** by **rancher**:

I realize I may be one of the only ones who started with .60, and am thinking my solution is maybe to delete Arduino entirely and start from scratch?

---

Posted on **2017-03-28 12:08:02** by **Bar**:

I believe you

---

Posted on **2017-03-28 12:08:02** by **rancher**:

Okay, wait....I was not trying that.  I was on the other Arduino firmware page and following the other instructoons, the wrong ones.

---

Posted on **2017-03-28 12:08:11** by **rancher**:

I'm wrong.

---

Posted on **2017-03-28 12:08:16** by **Bar**:

wait, what other page

---

Posted on **2017-03-28 12:08:27** by **rancher**:

I was doing the verify/compile thing.

---

Posted on **2017-03-28 12:08:35** by **Bar**:

Ohhhhj

---

Posted on **2017-03-28 12:08:41** by **Bar**:

That is confusing

---

Posted on **2017-03-28 12:08:47** by **Bar**:

I have done that too

---

Posted on **2017-03-28 12:08:58** by **rancher**:

https://github.com/MaslowCNC/Firmware

---

Posted on **2017-03-28 12:09:14** by **rancher**:

I see the difference now.....I've been doing that all week!

---

Posted on **2017-03-28 12:10:02** by **Bar**:

AHHHH. I'm so sorry! This is what the firmware version number should  [look like](//muut.com/u/maslowcnc/s3/:maslowcnc:fUsz:firmwareversion.jpg.jpg) when you connect to the machine.

---

Posted on **2017-03-28 12:10:43** by **rancher**:

Right, today was the first time I saw that, thus....here I am!!



I brought the board up here with me.  I bet it will be all solved in moments.  Thank you.

---

Posted on **2017-03-28 12:13:06** by **Bar**:

Fingers crossed! I've updated that readme page to be correct so it won't catch anyone else. Thank you for pointing that out!

---

Posted on **2017-03-28 12:18:47** by **rancher**:

Bar, do I need to power the motor relays to update firmware?

---

Posted on **2017-03-28 12:19:11** by **Bar**:

No, you should be able to update the firmware without anything except a USB cable plugged in

---

Posted on **2017-03-28 12:19:23** by **rancher**:

It doesn't seem to be working for me.

---

Posted on **2017-03-28 12:19:43** by **rancher**:

I had some strange behavior when trying to sort out the different firmware versions.

---

Posted on **2017-03-28 12:19:53** by **Bar**:

What do you see?

---

Posted on **2017-03-28 12:20:08** by **rancher**:

One .ino would open in a new instance of IDE, and the newest one does not.

---

Posted on **2017-03-28 12:20:43** by **rancher**:

Currently what I see is .60 in GC after following the update routine.

---

Posted on **2017-03-28 12:21:19** by **Bar**:

Hmmm

---

Posted on **2017-03-28 12:22:18** by **Bar**:

What happens if you delete the old .zip file then open Arduino (It should come up without a file open), then click File->Open so we are sure its opening the latest version

---

Posted on **2017-03-28 12:23:00** by **rancher**:

I deleted all old versions, but I'll double check and try again.

---

Posted on **2017-03-28 12:25:22** by **rancher**:

Yeah, "Firmware-0.61" is the only firmware folder on the machine.....hold on.  Deleted it.

---

Posted on **2017-03-28 12:25:36** by **rancher**:

Okay, blank Arduino.....

---

Posted on **2017-03-28 12:25:39** by **Bar**:

Wait! I know what's going on

---

Posted on **2017-03-28 12:26:10** by **rancher**:

I'm so glad!

---

Posted on **2017-03-28 12:26:20** by **Bar**:

You want to download the very latest version which is in between releases like  [this](//muut.com/u/maslowcnc/s3/:maslowcnc:OxTT:download.jpg.jpg) !

---

Posted on **2017-03-28 12:27:03** by **rancher**:

Heading there now.

---

Posted on **2017-03-28 12:27:32** by **Bar**:

It's part of that same instructions to do it that way, you are grabbing the latest release version (which makes sense), right now because so things are changing so quickly it's worth grabbing the up to the minute one

---

Posted on **2017-03-28 12:28:58** by **Bar**:

We're coming out with a new "version" every Wednesday, but even one week is too long. You might want to update again tonight because I'm working on getting the GRBL-generic code to run correctly right  now

---

Posted on **2017-03-28 12:29:59** by **rancher**:

I was going to the "releases" tab and getting the latest release.  I didn't know they were not the same.  Thank you.

---

Posted on **2017-03-28 12:30:56** by **Bar**:

It's really not clear. You did what makes sense, and in two weeks there won't be any difference really because things will have settled down (I sure hope)

---

Posted on **2017-03-28 12:32:17** by **rancher**:

Success Bar!  V 0.61 in GC.  I might be able to get to the machine again this afternoon if I don't get swamped.  I bet that was most of my issues right there.  Thank you again.

---

Posted on **2017-03-28 12:34:17** by **Bar**:

Absolutely! The rest of our backers will never truly know how much work you guys did to make the system work. Thank you.

---

