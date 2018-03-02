## Helping a friend to make a sign.
Posted on *2017-06-05 19:17:48* by *carlosrivers*

Hey guys I've got this PDF file, and I'm playing around with the software in Fusion 360 to work with her design. Can anyone help me understand how I get to a point where I can upload this to Fusion 360 and edit things such as thickness, width and height? Needs to be 12 by 48 with a thickness of 1 inch.

PDF version
https://drive.google.com/open?id=0BzFTyJ3YeFIIdG41YjJQXzZabUphUkpUbnZFaEk1VzVXX3lF

DXF version
https://drive.google.com/open?id=0BzFTyJ3YeFIIdEQtcjNSdEpIQ2l2ZjZFSHZrVUpoVzJldDFv

---

Posted on *2017-06-05 19:20:53* by *carlosrivers*

I think I'm onto something, I should go from PDF to JPEG to DXF?

---

Posted on *2017-06-05 19:40:02* by *carlosrivers*

[Screen Shot 2017-06-05 at 7](//muut.com/u/maslowcnc/s3/:maslowcnc:JIYZ:screenshot20170605at7.38.57pm.png.jpg) 

This is what comes up from a PDF to a DXF file.

---

Posted on *2017-06-05 19:41:02* by *mrfugu*

I'd say you'd want to use an .svg file to import to Fusion, I'd use Illustrator to go from .pdf to .svg): http://toglefritz.com/import-an-svg-into-fusion-360/

---

Posted on *2017-06-05 19:51:17* by *larry357*

Use inkscape as it is free

---

Posted on *2017-06-05 19:56:51* by *blsteinhauer88*

PDF to svg my vote is easel at inventibles. It's free and is easy to set up the sign.

---

Posted on *2017-06-05 21:42:59* by *carlosrivers*

@Blsteinhauer88 Wow Easel for the win dude.

---

Posted on *2017-06-06 01:28:09* by *carlosrivers*

Guys I think Im really close to having something useable. Would anyone who familiar with Fusion 360 mind looking at my file and see if it makes sense? If I understand my own file, I could use a one inch thick plywood?

This is so cool to finally be at the stage of "I think Im getting the feel for this..."

http://a360.co/2rw0Vgs

---

Posted on *2017-06-06 01:42:56* by *carlosrivers*

So from Fusion360 I find a way to make g-code, (NC file) and I loaded into GC. Heres what comes up lol.

 [Screen Shot 2017-06-06 at 1](//muut.com/u/maslowcnc/s3/:maslowcnc:xXbM:screenshot20170606at1.45.08am.png.jpg)

---

Posted on *2017-06-06 01:44:05* by *carlosrivers*

[Screen Shot 2017-06-06 at 1](//muut.com/u/maslowcnc/s3/:maslowcnc:ApI1:screenshot20170606at1.46.44am.png.jpg)

---

Posted on *2017-06-06 09:06:26* by *blsteinhauer88*

I am still struggling with fusion myself.  I have watched a lot of youtube for tutorials,  Look for Lars with F360 and watch his videos.

---

Posted on *2017-06-06 09:33:52* by *Bar*

That actually might not be your issue. That could be an issue with the way Ground Control is rendering the file. Any chance you would be willing to share the file so I can take a look and see if the problem is on my end?

---

Posted on *2017-06-06 10:10:27* by *davidlang*

try running it on this simulator https://nraynaud.github.io/webgcode/

---

Posted on *2017-06-06 10:39:17* by *carlosrivers*

Hey Bar heres the link for the NC file

https://drive.google.com/open?id=0By4wTqIjhYwnTFBoMGFQd1VLckk

---

Posted on *2017-06-06 12:00:41* by *TheRiflesSpiral*

It appears in the simulator that David posted similar to how it appears in GC. I think F360 exported your NC oddly.

---

Posted on *2017-06-06 12:06:26* by *davidlang*

yes, that file is very odd. It doesn't send a bunch of g1 commands, instead it issues a g1 and then sends a bunch of different coordinates. The maslow will not work with this.
what option did you use for the export?

---

Posted on *2017-06-06 12:18:55* by *carlosrivers*

In Fusion is their a specific post processor I should be using?

---

Posted on *2017-06-06 12:38:35* by *davidlang*

I don't know what ones are there, but if there is a grbl one, try that (they said that they were going to add a maslow one, but it sounds like they didn't do so)

---

Posted on *2017-06-20 12:59:51* by *carlosrivers*

Quick question, for this project. Am I going to do a 2-D contour cut?

---

