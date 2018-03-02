## Assembly guide error
Posted on **2017-03-18 10:56:05** by **mattnelson**:

I realize it is in progress, but Step 4 and Step 5 links both point to the same page.

---

Posted on **2017-03-18 11:43:30** by **Bar**:

Thanks for the heads up! I'll fix that.

---

Posted on **2017-03-18 13:47:55** by **Bar**:

The link should go to the right place now. Thanks again for pointing that out

---

Posted on **2017-03-19 04:21:00** by **flyingavatar**:

Bar,



Also, for the "Using the Temporary Frame to Cut Parts" page you can link to the raw GCode content directly using the raw.githubusercontent.com domain.  (These are the links that are generated buy clicking the "Raw" button on a particular file's page in the repository.)



https://raw.githubusercontent.com/MaslowCNC/Mechanics/master/Gcode/Sled-EigthInchBit.nc

https://raw.githubusercontent.com/MaslowCNC/Mechanics/master/Gcode/Sled-QuarterInchBit.nc

---

Posted on **2017-03-19 09:34:03** by **Bar**:

In my browser the raw content gives the text of the file, but I really just want it to give you a download of the whole .nc file. What is the behavior in your browser?

---

Posted on **2017-03-19 10:35:07** by **aalbinger**:

same behavior.  right click on the link and "save as" works great.  .nc is after all just a text file.

---

Posted on **2017-03-19 17:52:14** by **flyingavatar**:

If you're able to control the HTML of the link, you can use:



--- html

<a href="https://raw.githubusercontent.com/MaslowCNC/Mechanics/master/Gcode/Sled-EigthInchBit.nc" download target="_blank">Sled-QuarterInchBit.nc</a>

---



which will force a download in a new window.

---

Posted on **2017-03-19 18:40:24** by **Bar**:

I'll see if I can change the HTML, if not I think right click is a good solution if we're clear about how to do it. Thanks for the suggestions everyone!

---

