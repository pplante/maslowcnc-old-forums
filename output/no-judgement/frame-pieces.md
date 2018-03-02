## Frame pieces
Posted on **2017-04-08 14:20:30** by **rexklein**:

so I am ready to try cutting pieces. When I load the anglebrace1.svg there is nothing shown in groundcontrol. what am I doing wrong?

---

Posted on **2017-04-08 15:47:59** by **gero**:

GroundContol would expect a .nc file. (gcode.) Load the .svg in makercam.com and create a toolpath to save as gcode. In the updates the is a link to a video as far I remember.

---

Posted on **2017-04-08 17:00:19** by **rexklein**:

thank you

---

Posted on **2017-04-08 17:04:06** by **rexklein**:

That might be something bar could do to help users make GC open *.nc right now you can choose any filetype.

---

Posted on **2017-04-08 18:09:13** by **Bar**:

Good suggestion. I've made an issue for it [here](https://github.com/MaslowCNC/GroundControl/issues/180) . I will make it so trying to open a file which is not of type .nc pops up an information message.

---

Posted on **2017-04-14 09:51:25** by **boandersen**:

For reference, here are the the videos talking about gcode/makercam/design

Makercam generate gcode:

https://www.youtube.com/watch?v=ocmYJlFGjXY



design idea to completion:

https://www.youtube.com/watch?v=W0mW_mm1iBI&t=174s

---

