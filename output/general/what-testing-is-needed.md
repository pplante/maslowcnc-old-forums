## What testing is needed.
Posted on **2017-06-15 13:03:54** by **blsteinhauer88**:

Programmers! What kind of cuts and where on the board is needed to test cut,  to give more info for your programming?  Or is there any procedure for calibration that is needed to be tested?  I'm not working tomorrow so I can put Maslow through some testing.   Mine is standard Maslow with 10 degree pitch and two bricks.

---

Posted on **2017-06-15 13:53:33** by **Bar**:

For me the most helpful thing is to let me know when you find something which doesn't work, especially if the problem is repeatable. I know what I've been doing is focusing on making as many things as I can to test the machine

---

Posted on **2017-06-15 14:13:35** by **blsteinhauer88**:

I have a code for Mason Bee trays.  I use a 1/4 bit and make long straight lines down the wood 1/4 in deep.  I will cut some vertically and some horizontally.  To make the trays I just push them through a table saw after the shallow cuts.  I will see if they are straight in both directions.

---

Posted on **2017-06-15 14:20:13** by **Bar**:

That's a great test. I love the idea of using the table saw as a way to test for straightness. I've been looking for a good way to measure if my cuts are straight over long distances

---

Posted on **2017-06-15 15:08:55** by **davidlang**:

we need an accuracy test run, with all the recent changes to the code we don't know how accurate the machine is over it's range.



the file http://lang.hm/maslow/testpattern.nc makes a bunch of squares around a 4x8 worksheet. It would be useful for someone to run this and measure the exact dimensions of each square (a caliper will be needed for this)



We also need to know how straight (or not straight) a long horizontal cut is.



@bar, did you ever get the simulator code built to see what sorts of errors show up from incorrect machine dimensions?

---

Posted on **2017-06-15 16:01:08** by **blsteinhauer88**:

@davidlang, I will run that in the morning.  Thanks, and I can report on the horizontal lines too. Thanks!

---

Posted on **2017-06-15 17:22:35** by **Bar**:

@davidlang, great suggestion! I haven't finished the simulation but it's still on the todo list.

---

Posted on **2017-06-16 12:31:41** by **gero**:

[IMAG0851](../../images/YQ/4j/YQ4j_imag0851.jpg.jpg)  5 sheets of 4mm 'whatever' are waiting in the garage just for the testpattern and lines across the sheet. Will try to come up with a solution tonight, to mount my lever that has a laser with a straight line, to a camera tripod. Just give me a GC/FW that I can get through calibration ;-) by morning (12 hours from now) and there will be a lot of dust :-)

---

Posted on **2017-06-16 12:56:17** by **TheRiflesSpiral**:

An accurate way to measure straightness of cuts over long distances is to cut two parts identically then flip them end-for-end and measure any gaps. Any error is exaggerated x2 so it's easier to detect. Something like the picture below...



 [Asset 1](../../images/kY/ki/kYki_asset1.png.jpg)

---

Posted on **2017-06-16 13:08:29** by **TheRiflesSpiral**:

That's how we would tune the panel saw, anyway...

---

Posted on **2017-06-16 14:55:58** by **Bar**:

Great suggestion @TheRiflesSpiral that's a way we could tune Maslow as well. I hadn't considered cutting out parts entirely, I was just thinking of making marks. Thanks for the idea.



@Gero, I'll do my best!

---

Posted on **2017-06-16 20:33:45** by **davidlang**:

The one issue with flipping end to end is that you now depend on how parallel the edges are.



but in our case, the problem we have been fighting is the cut being curved up in the center, so we are less worried about one end being thicker than the other than we are of the center being thicker than either end.

---

Posted on **2017-06-17 08:50:21** by **gero**:

The laser is set up and it seems that could work.  [IMAG0858](../../images/qv/od/qvod_imag0858.jpg.jpg)   [IMAG0857](../../images/Iw/2f/Iw2f_imag0857.jpg.jpg) No cutting as calibration is not working for me. 

Have we reached a stage where we should have a 'Stable Release' for cutting and 'Beta Release' for testing?

---

Posted on **2017-06-17 08:52:48** by **blsteinhauer88**:

I went back to FW .73 and Its working again.  GC is not the problem it seems to be in the last FW update.

---

Posted on **2017-06-17 09:22:11** by **gero**:

Thanks @blsteinhauer88, I will try. Just not sure if test cuts and measurements would still contribute.

---

Posted on **2017-06-17 10:22:39** by **blsteinhauer88**:

I was unable to control the sled.

---

Posted on **2017-06-18 16:17:07** by **gero**:

[IMAG0862](../../images/qH/nd/qHnd_imag0862.jpg.jpg)  [IMAG0863](../../images/uA/4N/uA4N_imag0863.jpg.jpg)

---

Posted on **2017-06-18 16:22:53** by **gero**:

https://www.dropbox.com/s/v2ndrdmlglbw31m/pattern-new.xlsx?dl=0

Take out column D and L on sheet 2 and export to .csv without any delemiters, then rename to .nc

https://www.dropbox.com/s/maut89eaix0ocyk/pattern-new.nc?dl=0

---

Posted on **2017-06-18 16:24:11** by **gero**:

I modified the file and inserted blank space to make it show in GC. Plus added three horizontal lines.

---

Posted on **2017-06-18 16:25:58** by **gero**:

I left all the to many FXXX for checking if I could get a buffer overflow, but no success.

---

Posted on **2017-06-18 16:29:34** by **gero**:

G0 and G1 seemed same speed and not the speed I would expect for both.

---

Posted on **2017-06-18 16:33:58** by **gero**:

Calibration went quite well, but some comments I need to share tomorrow. Left and right down squares, the sled hit the screws because home was not at my center of the sheet and the third time I am requesting that I know better where the center is and I should tell GC.

---

Posted on **2017-06-18 16:54:54** by **davidlang**:

how straight is the horizontal line and how accurate are the squares?

---

Posted on **2017-06-18 18:21:50** by **Bar**:

Good recommendation for defining zero better. I hear you and I'm working on it.



I had the same issue.



Is what you are imagining a "mark the center of the plywood with a pen and move the sled there" step?

---

Posted on **2017-06-18 19:02:17** by **blsteinhauer88**:

[Image](../../images/LZ/2A/LZ2A_image.jpg.jpg)

---

Posted on **2017-06-18 19:03:49** by **blsteinhauer88**:

@davidlang, not bad,  [Image-0](../../images/eZ/g2/eZg2_file_0image.jpg.jpg)

---

Posted on **2017-06-18 21:41:12** by **davidlang**:

can you double check the measurements on that bottom right square? it's a bit of an outlier compared to all the others.



Any word on how straight a horizontal cut ends up being?



Was this created by just entering the machine dimensions in? or was this by cutting test cuts and lying about the chain spacing until the test cut came out clean?



One thing that bothers me is the vertical spacing on the bottom row, it varies quite a bit and it's not a consistant type of variation across the board, it goes up down up down by quite a bit from cut to cut.



which file was this? the testpattern.nc that I posted the link to or the pattern-new.nc that gero posted?



in either case, the file says to run the bit in a spacing of 106mm, which with a 1/8" (3.25mm) bit would result in 102.75mm (4.045") blocks being left 



the vertical spacing (ignoring that bottom right block) ranges from 3.970 (-0.075" or -5/64) to 4.044 (close enough to exact), or just a bit over +-1/32 the median (which itself is off by ~1/32), about double what we are aiming for



the vertical spacing ranges from 4.021 (- 0.024, -3/128) to 4.159 (+0.114, +7/64) for a range of a little over +-1/16 from the median (which is off by ~+1/32), about four times the error we are aiming for.

---

Posted on **2017-06-18 22:40:03** by **davidlang**:

fun with numbers http://lang.hm/maslow/testresults.pdf There's also a spreadsheet there.

---

Posted on **2017-06-19 18:37:50** by **blsteinhauer88**:

That bottom right was measured correct.  I did not watch it  on that cut so it may have bumped something like my shop vac.  I did not run any horizontal or verticals yet.  I have had trouble with the new release and just now have maslow realizing his place in the universe.  I did run the testpattern.nc as you posted with no alterations.

---

Posted on **2017-06-20 13:27:38** by **davidlang**:

did you set the dimensions to mach your machine, or did you do the calibration step that cuts test patterns with you lying about the dimensions until the pattern cuts correctly?

---

Posted on **2017-06-20 14:47:19** by **blsteinhauer88**:

I had used the automatic calibration and the dimensions on the test cut were accurate.  then I loaded your test pattern and hit run.

---

Posted on **2017-06-20 14:47:41** by **blsteinhauer88**:

All dimensions matched my machine

---

Posted on **2017-06-20 21:39:27** by **davidlang**:

hmm, I'm a bit puzzled. If the calibration test was accurate, the center square in this test should have been accurate as well.

---

