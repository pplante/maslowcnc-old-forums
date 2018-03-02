## Motor life expectancy  and feed rate
Posted on **2016-11-17 00:09:45** by **jamesbil**:

The moors are really nice and compact but due to the fact that they are lifting a few kg of a router, a few kg of bricks plus cutting resistance, what kind of life should we get out of the motors?



Does the software adjust the feed rate according to rpm, bit size and depth of cut?

---

Posted on **2016-11-17 10:38:11** by **Bar**:

I've been running  my motors every day for about 4 months now with no issues, so I would expect them to last quite awhile. Because of the 300:1 reduction gearbox with a worm gear, the motors aren't really working that hard and stay cool even after hours of running. We will make them available as a replacement part so when they do wear out, they will be available.



The software lets you set the federate, bit-size and depth of cut. It doesn't do it automatically, but I've been playing around with the idea of adding that feature. Because of the machine's unique closed loop design, the machine can actually sense how much force is being applied to the motors and could use that to calculate the right cutting speed.

---

