## Multiple passes for thicker ply
Posted on *2016-11-20 14:23:25* by *jambo*

Hi, hoping someone can help with this question; if I'm cutting 3/4 inch material and it's advised to only cut around 1/8 inch per pass, will Maslow automatically repeat passes until the 3/4 inch material is cut right through or would I have to manually intervene at the end of each pass to increase the depth?

---

Posted on *2016-11-20 14:57:51* by *TheRiflesSpiral*

Maslow will pause and ask you to set the depth after each pass. The concept of the Z-axis is to eliminate this manual step and automatically increase the depth between passes.

---

Posted on *2016-11-22 01:51:09* by *jambo*

Thanks Riflesspiral, What about if you had a workpiece with multiple holes in it?, will the z-axis solution allow you to move from one 'cut out' to the next automatically or is that a step too far?

---

Posted on *2016-11-22 04:03:08* by *TheRiflesSpiral*

I've only just started playing with the makercam.com site, but it appears that you can select multiple objects and generate multiple tool paths. I can't say for sure how Ground Control handles that, but I'm sure Bar will chime in.

---

Posted on *2016-11-22 11:00:12* by *Bar*

For multiple holes or multiple parts cut from the same sheet, the z-axis will automatically retract the bit, move to the new location and then begin cutting :-)

---

