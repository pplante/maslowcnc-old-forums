## Ground control inaccurately positions Z-axis motor
Posted on *2017-07-04 15:45:59* by *braedenfoster*

Hey all, 

I have been having issues with getting the Z-axis motor to move the correct distance along the thread. The thread pitch on the router I have is 1.25 mm which I have set in Ground Control, along with having the latest version of Ground Control installed. When I try to move the Z-axis in either direction by 10 mm, it actually moves around about 8mm inwards and moves even less outwards with 10mm set. The Z-axis will also go in first by about 2mm and then go outwards when Z-Out is set. I cannot figure out what the issue is, and why I can't find any solutions online.

Cheers,
B.

---

Posted on *2017-07-04 16:16:39* by *TheRiflesSpiral*

The difference between in/out may be due to lash. Do you have any tension applied to the mechanism to remove lash? At least one user here has bungee cords wrapped around the handles and over the top of the router to keep downward pressure on.

---

Posted on *2017-07-04 16:53:19* by *braedenfoster*

Yeah, I thought there could be a bit of lash, I did however cut off the springs on the router so there shouldn't be much force being applied outwards. I will give bungee cords a go and see if that makes a difference. There is still the problem of the z-axis going the wrong direction and then going back the right way.

---

Posted on *2017-07-04 17:36:54* by *gero*

1) I have seen similar behavior of the z-axis going the wrong direction before with older firmware and Ground Control. I believe also a few comments here. To investigate, I think that the versions of both should be put at the top of the topic to make it easier to replicate and investigate. I assume you are on the latest. So you are on FW and GC on 0.78?
2) Giving the cut file that causes the issue helps others to check. Even if it is only the part that causes the problem. 
3) At the very beginning I and others had strange behavior of Z because of the connector on the motor. We strapped the cord somewhere to avoid movements on the connection while the sled moves.   [IMAG0702](//muut.com/u/maslowcnc/s3/:maslowcnc:1Ocp:imag0702.jpg.jpg)

---

Posted on *2017-07-04 17:42:51* by *gero*

Also please do not feel shy to open an issue at Github https://github.com/MaslowCNC/GroundControl/issues if you can replicate that problem more than twice and provide details on how and when it happens.

---

Posted on *2017-07-04 17:56:06* by *gero*

Kindly forget the part 'provide details on how and when it happens'
You can open an issue without that.
I was just trying to say that the more details provided, the faster it will be resolved.

---

Posted on *2017-07-05 22:33:32* by *davidlang*

you say you cut he springs on the router, what router are you using that has springs on it? the r2200 fixed base kit has not springs.

---

