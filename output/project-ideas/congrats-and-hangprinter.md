## Congrats and Hangprinter
Posted on *2016-10-16 13:00:48* by *torbjorn*

Hello MaslowCNC community and congrats with the vertical and simplified frame- CNC design. I love it!

I've made a string-driven RepRap.
video:
https://vimeo.com/147278540
dev blog:
https://vitana.se/opr3d/tbear/

Looking into adding servos to the Hanging RepRap (and also building a MaslowCNC on a hackathon). We should see if we can cross pollinate our projects.

Baz have suggested that I check out the motors that Maslow use with  a 1,000:1 reduction gear box and a 12ppr encoder. Where can I buy them, and how can we synchronize and share research and test results?

---

Posted on *2016-10-17 10:20:17* by *Bar*

I know I said this before in our email, but I want to say it again publicly, this is soooooo cool. I especially love that it's all in one package. 

I hadn't really thought about where to buy the motors. We have our motors custom made to spec, and usually they want MOQs in the 100s, but they will do one-off motors to test an idea. When we put in our order, I can have them make some if you are serous about using them. 

Do you feed the cable onto a spool? I can't quite tell in the video.

Do you use github? 

Our (My) code is intentionally written to be portable so each motor is an object, each axis is an object...etc so you can easily pull the libraries you want and do things like say aAxis.write(100). And it will move 100mm or aAxis.setInches(); aAxis.write(.01); and it will move .01 inches.

---

Posted on *2016-10-19 03:41:56* by *torbjorn*

Thanks!
I'm serious about testing servos. They would make the moving part of Hangprinter ca 1 kg lighter than the current prototype with stepper motor solution. Also, closed loop control is crucual since prints will often be > 20 h long.

As I see it, swapping steppers for servos is a software autocalibration problem because PID values are hard to tune right. Users need all the help they can get with PIDs... I must get an ok motor started and find ok PID values manually before I can start coding since I have so little experience with servos...

Yes, I use as large spools and as thin lines as I can to minimize error from build-up on spools. I do no software correction of spool-build-up-errors since they are very small.

I'm tobbelobb on Github

https://github.com/tobbelobb/hangprinter

What motivated you to write your own firmware instead of using/modifying existing ones?

---

Posted on *2016-10-19 05:27:04* by *torbjorn*

The branch `build_maunal_0` is the most up-to-date one on github. It corresponds to the build instructions found here: http://vitana.se/opr3d/tbear/index.html#Clerck_assembly_manual

---

Posted on *2016-10-19 12:27:18* by *torbjorn*

I live in Sweden, so it might be expensive to send servos. Thanks for offering =)

---

Posted on *2016-10-19 13:09:56* by *Bar*

I bet they'll fit in a small flat rate box so it shouldn't be more than $30. Is size/weight an issue for you. Our main motors are pretty beefy and with a 1,000:1 gear box you are going to have WAY more torque than anyone needs. 

I just spec'd some smaller motors for the z-axis on Maslow, maybe those would be better. I should have factory samples of the z-axis motor in about 2 weeks.

---

Posted on *2016-10-24 11:38:10* by *torbjorn*

Nice =) I'd like weight to be as low as possible, the z-axis motors sounds like the better fit. Emailing my address.

Good luck with the big launch tomorrow!

---

