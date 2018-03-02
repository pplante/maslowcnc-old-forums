## v-plotter.py
Posted on *2017-02-13 19:17:41* by *davidlang*

I copied the code from http://2e5.com/plotter/V/design/ which lays out the math for a plotter designed like the maslow. I tweaked the constants and added a grid display.

the resulting code is at http://lang.hm/maslow/v-plotter.py I don't consider anything I've done to it creating enough to be worth copyright, so my modifications are public domain. 2e5.com puts no license on the code, but is encouraging people to use it, so I assume that it's also public domain as well. I would consider it curious to leave comments in it  

with the default parameters, this seems to match the maslow design and therefor can be used as a basis for modifying the dimenstions of the maslow and deciding how large a board could be cut as a result

for example, if you change the spacing to 6.0 and the width,height to 1000,1500 you get a version that shows you could cut a 4' wide by 8' tall sheet of plywood

changing the height to 1400 will show you how mounting the motors higher would affect the cutting area (for people who want to look at cutting 5' x 5' wood)

note, the current setting of .2 f or the low tension is a guess that makes things look right for the maslow. When you get near the lower edges, the problem is that one of the chains will be under low tension, this can cause inaccuracies as the weight of the chain can cause it to bow, and the sled can have trouble sliding. If the sled is made slipperier, you can probably cut with lower tension, if it's made heavier, the tension will be higher everywere, and you can cut to the lower corners better

todo: change the colors from just light blue 'out of spec for tension' to a red for tension too high, and a gradient for when the tension gets too low.

David Lang

---

Posted on *2017-02-13 20:40:05* by *lsimonetto*

hi there - what language is that coded in? would love to get the optimal coordinates for  4'x8' or 5'x10' sizing, but really only know excel coding... happy to learn something else though! If much longer distances are suggested, would happily also post the design of the resulting arms, and how to rigidly integrate them into the machine (rigid structures is far more my thing than coding!)

---

Posted on *2017-02-13 21:14:12* by *davidlang*

it's written in python.

once you get python installed in windows, you should be able to do 

python v-plotter.py

from the command line (probably easier ways to do it, but I haven't used windows in a couple of decades)

once you have the ability to run it, you should be able to just change the image dimensions and spacing variable to play around and see what sizes will work.

P.S. spellchecker got me on my prior post, I meant to say I would consider it courteous t leave the comments on the origins of the code in place. :-)

I've e-mailed the original author to check on his license preference. I suspect GPL given his membership in the EFF, but we'll see.

---

Posted on *2017-02-14 20:43:48* by *lsimonetto*

Thanks again for the info :)

---

Posted on *2017-03-23 23:35:57* by *jbarchuk*

Hey @davidlang I have a Q for you please! It took me a WEEK at a few hours a day to get silly python running right -with- -graphics-. I've used it only occasionally before, never with graphics. That was 3 PCs and 4 OSes. I finally decoded the clues at stackexchange so the imports work.
The only thing I changed in your version of the v-plotter script was screen resolution.
I need your opinion whether this output looks right.
I -think- it does. It would be clearer if the output included numbers about dimensions and such, but the 4'x8' built into the script make sense by what it outputs. I'm not complaining at all. It's a free script with no commercial value LOL! and I don't expect any bells or whistles. If it's right then I'll scale it down to 30"x20" that I will be using, which is why this script interested me in the first place.
TYVM!
[Maslow-v-plotter-screencap-01](//muut.com/u/maslowcnc/s2/:maslowcnc:1pOP:maslowvplotterscreencap01.png.jpg)

---

Posted on *2017-03-24 00:42:36* by *davidlang*

yep, that looks right. I run linux on everything, so pyton is 'just there'

the heavy grids are 1' squares, the light subgrids are 1" squares.

Note that this is not a full representation of the Maslow, it assumes the chains go directly to the center point (where on the maslow, they go to the corners of the sled), it's just to give you a rough approximation of where you are likely to run into grief.

Once we get someone building these things, they can tell us how accurate it is. :-)

---

