## Z-Axis Calibration and motor engagement
Posted on **2017-07-16 08:22:49** by **jbnimble**:

Using 0.80 Firmware and Ground Control 0.80. Setup and plugged in Z-Axis, and running Step 7 of 9 of calibration. Noticing that when I move the Z-Axis up/down that the Left and Right motor/encoders are also engaging. Why would the Left/Right motors need to engage?



I have also noticed that when manually moving the left/right motors that there is a period after the movement (especially during calibration) where the motors wiggle back and forth and make a lot of noise. Anyone know why the motors appear to stay engaged when they are done moving, or should not be moving at all (calibrating Z-Axis)?

---

Posted on **2017-07-16 13:34:09** by **Bar**:

I know exactly what you are talking about.



You are totally right that there is no need for the left and right motors to power on when moving the z-axis, and there was in fact a period of time where they were set not to power on, but we found that having the left and right motors off during the z-axis motions was leaving a mark on the edges of parts that were cut. I'm not completely sure why that was happening, but the easiest way to fix the issue was to leave all the motors on whenever any of them are moving, and for two seconds after they finish moving. 



This is something we can revisit once everything is more stable, because you are right that it shouldn't be necessary.

---

Posted on **2017-07-16 14:07:52** by **jbnimble**:

Thanks. I can say that once I finally got the calibration working (I must have run it at least 10 times in the last 2 days), that it appears to be cutting as expected. Top left corner had some issues, but I think that is known. Also the Z-Axis makes all the difference, cutting with that temp sled that did not have a Z-Axis was painful. A lot of lessons learned this weekend. Excited that things are mostly working! ... and I need a quieter vacuum, wowsa. [Progress...](/images/q5/q578_20170716_165916.jpg.jpg)

---

Posted on **2017-07-16 14:14:59** by **Bar**:

That's fantastic to hear! Keep us posted as you progress :-)

---

Posted on **2017-07-17 01:51:29** by **cameronswartzell**:

https://www.ridgid.com/us/en/14-gallon-high-performance-wet-dry-vac



The ridged vacs, available at Home Depot, with SNR (scroll noise reduction) are practically stealth vacuums. I mean, they make noise but MUCH less. Absolutely worth it

---

