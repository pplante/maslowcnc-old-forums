## Accuracy over the entire workable area?
Posted on **2017-05-11 02:02:29** by **asleborgen**:

Hi,

Long time, no forum visit...
I am deeply impressed by all the work you guys put into this project!

Sorry for asking, but I haven't been able to find any info (yes, I have looked)  regarding positional accuracy in the center VS out near the edges of the plate. Can someone please point me in the  right direction?

Best regards
Asle , Norway

---

Posted on **2017-05-11 02:39:26** by **gero**:

Hi asleborgen, my last test over the entire sheet is 2 weeks old and a lot has happened since then. We have been testing a fantastic new calibration that lets the Maslow measure its own demensions.
I hope on Saturday I can do a new test.
This information is outdated http://muut.com/u/maslowcnc/s3/:maslowcnc:S5ed:imag0675.jpg.jpg 
15 squares at targeted 100mm x 100mm.

---

Posted on **2017-05-11 02:45:39** by **gero**:

'Dialing in Critical Measurements' is a almost 400 coments long topic :-)  that is continued in 'New Calibration Procedure'

---

Posted on **2017-05-11 04:28:20** by **davidlang**:

we don't really know the accuracy because we are still working on fixing the software. The hardware is able to be very accurate, but we have seen some problems that could be in the underlying math, and we have some other issues that seem to be related to the software control loops.

Bar just committed the first patches to fix the control loop yesterday, so that should help things, and we are looking closely to try and figure out where the rest of the inaccuracy is 

The stated goal is to get it to 1/64" accuracy. We aren't there yet, but it should get there with software updates (the hardware is able to get down to ~1/1000" in theory)

---

Posted on **2017-05-11 04:39:27** by **asleborgen**:

Thank you both, this is great news! :-) 
I was planning to build a "normal" 3-axis router, but with these improvements I'm really starting to lean towards your design!

1/64" should be roundabout 0,39mm and that must be more than sufficient for plywood and MDF :-)

---

Posted on **2017-05-11 13:44:24** by **davidlang**:

a 'normal' three axis router can do some things that the maslow cannot do, but the maslow is simpler for cutting large sheetstock.

---

