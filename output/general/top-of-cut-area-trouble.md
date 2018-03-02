## Top of cut area trouble.
Posted on **2017-05-09 19:37:18** by **blsteinhauer88**:

I used F360 today and cut the chair they had designed in the class. The highest cut was the inverted chair side/leg. When over the +12 Y axis area. It shortened the part. I ran test befor in the upper quad and not much decay in the test pattern. Have a look : at my lips chair. [IMG_0757](../../images/K6/gK/K6gK_img_0757.jpg.jpg) [IMG_0758](../../images/HD/PZ/HDPZ_img_0758.jpg.jpg) [IMG_0759](../../images/cO/A8/cOA8_img_0759.jpg.jpg) [IMG_0760](../../images/8n/OY/8nOY_img_0760.jpg.jpg) [IMG_0761](../../images/MJ/UR/MJUR_img_0761.jpg.jpg) [IMG_0762](../../images/xt/S8/xtS8_img_0762.jpg.jpg) [IMG_0763](../../images/JP/NT/JPNT_img_0763.jpg.jpg)

---

Posted on **2017-05-09 19:37:57** by **blsteinhauer88**:

I did fix it with a quick jigsaw. [Image](../../images/Wr/Al/WrAl_image.jpg.jpg)

---

Posted on **2017-05-09 21:10:26** by **Bar**:

Very cool chair!



Unfortunately this could be caused by either of our two on going problems and it's hard to tell which. Both the feedback control system and the calibration of the machine are most sensitive right at the top of the sheet where small movements of the motors make the most difference.



I will add cutting more things right at the top to my testing list.

---

Posted on **2017-05-09 22:21:58** by **blsteinhauer88**:

Yea I found this from super Gero to explain.  [IMG_0764](../../images/T6/Pn/T6Pn_img_0764.png.jpg)

---

Posted on **2017-05-10 08:58:48** by **blsteinhauer88**:

If the arms taller and chain longer?  Would that relieve the higher tension on the chains at it reaches the top of the sheet?  How much taller is Gero's from the stock Maslow like mine.  Or did he use the about 18 inches?  Mine sits about 12 inches off the floor.  I wonder if I lowered the work area 6 inches or so leaving room so the sled won't hit the floor, if that would make a difference up top?  Has this been done yet I don't recall.  Also I can't find Gero's test pattern that returns to center each time and test all corners of the work area.

---

Posted on **2017-05-10 09:18:10** by **Bar**:

The real issue is a software one which is that the machine is the most sensitive to positioning accuracy at the very top (in a very non-linear way). That means that any errors in are amplified right there, and the real solution is that I need to improve the software.



That being said, moving the motors up could help at the cost of less tension in the chains at the very bottom, especially in the lower left and right corners.

---

Posted on **2017-05-10 09:34:24** by **blsteinhauer88**:

Gotcha,  I have faith in your math.... lol

---

Posted on **2017-05-10 10:19:50** by **gero**:

@blsteinhauer88 There is nothing super about not being able to understand the math or contribute to the programing. It forces me to try to narrow things in by experimental approach. For what it is worth, the xls is here https://www.dropbox.com/s/1sedgnbeljxlyry/pattern.xlsx?dl=0) 

It is for 100mm squares with a 6mm bit. Thats why the center square has coordinates like -53 and 53. For a 8mm bit that would be -54 and 54. A lot o F500 can be deleted, I learned. Exported to .csv without any delimiter and the coments, renamed to .nc it can be run, but i think GC does not show the pattern because there are no blanks in the code.  The .nc is here https://www.dropbox.com/s/5rgxlz6r69h3j5v/testpattern.nc?dl=0)

---

Posted on **2017-05-10 10:27:07** by **Bar**:

@superGero I think it's a great name :-)



The new calibration system is going to be in today's update and it's all based on your testing.

---

Posted on **2017-05-10 10:37:18** by **gero**:

:0 My frame is angled at a far to low 6 degree, my sled is yo heavy with 17 kg, my test sheet is a plex with a mirror like surface and i do metric... hahaha. How is that going to work :-)

---

Posted on **2017-05-10 10:38:59** by **Bar**:

Hahaha, you showed us that it was possible to use the distortion in the test shape to dial in the machines dimensions!  :-p

---

Posted on **2017-05-10 10:45:12** by **gero**:

One of the >100 variables. Still to be tested: Fake motor distance +25 % and - 25%. Hight of motors over the sheet +25 and -25%. Cutter to bracket +25 and -25%. And so on. :-) But I need a pen to fit in the router and cover the sheet with wallpaper to take that on.

---

Posted on **2017-05-10 11:08:53** by **blsteinhauer88**:

Your test sheet I posted above helped me to understand why my legs got shorter as the sled climbed higher.   You are the ultimate Beta Tester , using and documenting as you do.  Bar will fix it, plus you made a new work excuse, there is Sick Time, Comp Time, FMLA (US), Holiday, and now... Maslow Time!

---

Posted on **2017-05-10 16:19:11** by **davidlang**:

height of motors above the sheet is not going to cause any distortions, the most it can cause is a vertical position error of where the center of the board is.



motor distance  is likely to be an interesting one to play with.



the bit offset and cg offset are interesting ones as they are used to calculate the tilt (and the effect of the tilt) of the sled. errors here will cause systematic errors that will vary based on the left to right position

---

