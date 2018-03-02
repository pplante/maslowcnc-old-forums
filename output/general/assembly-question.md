## assembly question
Posted on *2017-05-08 14:49:19* by *jeffhunt*

Hi, I am considering purchase and scanned through the assembly. Does anyone have a CNC already that they used to fabricate any of the parts used to build the maslow? I have a cnc with 70 x 30 in bed and was wondering is the files exist to cut the sled or any other parts. What is the learning curve of the software, and last, has anyone cut an opendesk project and how long did it take?  Does anyone know how the feedrate compares to an xcarve?

---

Posted on *2017-05-08 15:01:24* by *davidlang*

Keep in mind that we are still in the beta-tester phase and are working through various problems and design ideas

The maslow should be able to do 48 ipm as the software gets worked out, right now it is limited to half that. I have no idea what the xcarve is able to do.

The files for the various parts are posted in the github repos, people have also built machines that only used straight cuts that could be done with a circular saw.

all CNC machines can use basically the same software to design the parts and convert them to g-code, that is where the vast majority of the learning curve is. The software to take the g-code and run it is always pretty simple.

does this answer your questions

---

Posted on *2017-05-08 16:38:07* by *gero*

The Maslow can cut its base itself by attaching the parts as described here: https://github.com/MaslowCNC/Mechanics/wiki/How-To-Assemble-The-Temporary-Frame
You are free to make your own frame and get inspiration here: https://github.com/MaslowCNC/Mechanics/wiki/Alternative-Frame-design-from-Beta-Testers
The learning curve of Ground Control is nicely documented and improved daily and fun to follow. There are other programs that you can use but the names just come not to my mind right now.
Turning a design into art or a usable piece is related to what Cam / Cad software you use and how good you can get at that.
A list of what is used here is found:  https://github.com/MaslowCNC/GroundControl/wiki/CAD-(Computer-Aided-Design)-software-packages
and here: https://github.com/MaslowCNC/GroundControl/wiki/CAM-(G-code-generation)-programs
Hope to see you soon.

---

