## Calibration routine malfunction
Posted on **2017-06-16 09:44:41** by **blsteinhauer88**:

With the latest fw/GC my sled is having trouble finding center, I have an error ring and it just climbs the board.  I decided to Wipe the eprom, reload the FW and calibrate like new.  When I get the the first step to align the gear, the left motor will move 1degree, but the right motor turns about a full turn of the gear.   I cannot align the gear to finish the steps.

---

Posted on **2017-06-16 09:51:55** by **blsteinhauer88**:

yes, reloaded and confirmed, it turns the right motor one full turn, not one degree.

---

Posted on **2017-06-16 10:07:58** by **scottsm**:

I see that problem with the error ring as well.

---

Posted on **2017-06-16 10:31:07** by **blsteinhauer88**:

I started an issue report in GC

---

Posted on **2017-06-16 12:13:01** by **Bar**:

Conversation is [here](https://github.com/MaslowCNC/GroundControl/issues/324) for those who want to follow along

---

Posted on **2017-06-17 07:44:32** by **rancher**:

What's the current status here?  I checked the threads in Github, but can't tell if I should spend the time trying to calibrate and cut a project today, or wait a bit longer.  Are we up?

---

Posted on **2017-06-17 07:52:26** by **gero**:

From the Linux side I can tell that I have 2 failed attemts to calibrate today with FW0.76 and GC0.76 with minus values for motor spacing and vertical offset. Would be nice to know if this is only me again :-)

---

Posted on **2017-06-17 08:52:57** by **rollandelliott**:

I'm getting nervous, isn't the final product supposed to ship in a couple of weeks and there are still issues calibrating it? Seems like shipping product that is not 100% ready would result in tons of support requests and wasted time. I know in my business it does. Better to perhaps delay shipments till this is all worked out?

---

Posted on **2017-06-17 10:24:45** by **blsteinhauer88**:

Don't be nervous this was with FW 73 [IMG_0033](//muut.com/u/maslowcnc/s3/:maslowcnc:Z4d3:img_0033.jpg.jpg)

---

Posted on **2017-06-17 10:55:38** by **rancher**:

That's nice!  Wait, so it's working?  I keep reading about legs being cut off and stuff, and dropped code.  I am ready to cut some projects but have been waiting on the current bugs to be resolved.  So....it works?

---

Posted on **2017-06-17 11:07:15** by **blsteinhauer88**:

Use Fw 73 and the latest GC and you will be fine!  He is fixing FW 76 now!

---

Posted on **2017-06-17 13:29:52** by **Bar**:

That sign is beautiful!



I *think* I've got a fix for the calibration issue with FW 76 up, and we're hot on the trail of the missing serial characters (if that's not a Hardy Boys book title, it should be)

---

Posted on **2017-06-17 14:54:54** by **larry357**:

That sign went all wrong! Just look at the spacing on the tractor tires! 😛 Awesome work! can't wait to get my machine!

---

Posted on **2017-06-17 15:21:57** by **rollandelliott**:

blsteinhauer88 What software are u using to make those signs?

---

Posted on **2017-07-06 22:51:48** by **blsteinhauer88**:

@rollandelliott I got the pattern from cnc dfx site, https://cncdxffiles.com/

Then I used illustrator to convert to svg, then I used Easel to clean up the design so that Maslow can cut it with a .062 or 1/16 bit.

---

