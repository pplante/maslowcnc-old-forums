## Interesting article about OpenDesk
Posted on *2017-04-11 09:19:35* by *scottsm*

I haven't had time to read it yet, but Make: has an article about [using OpenDesk for CNC projects](http://makezine.com/2017/04/04/opendesk-cnc-furniture/). There might be some good info there.

---

Posted on *2017-04-11 09:57:46* by *mindeye*

Contains this gem: """Also, use VCarve’s “Last Pass” feature when creating profile toolpaths.Your router’s passes around the perimeter will be offset by .1mm until the last/lowest cut. Then your router will cut to the precise line in reverse direction. The result is a much cleaner cut.""" 

Looks like a great way to merge the 2 toolpath approach with the first being a false, larger-than-reality bit. I imagine you could emulate this behavior in makercam by splitting your last cut at full depth and true bit size from all-but-your-last cut at varying depth passes and larger-than-life bit size.

---

Posted on *2017-04-11 10:01:39* by *scottsm*

If the "last pass" is in the reverse direction, that can be accomplished as well.

---

