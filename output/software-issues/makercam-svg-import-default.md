## Makercam SVG Import Default Resolution
Posted on *2017-07-10 08:45:10* by *jbnimble*

I've read some [makercam documents](https://www.shapeoko.com/wiki/index.php/MakerCAM) that recommend modifying:
```
Edit > Edit Preferences > SVG Import Default Resolution (px/inch)
```
Depending on which application was used to create the SVG file. For example:
```
Illustrator: 72
Inkscape: 90
```
I'm using [OpenSCAD](http://www.openscad.org/) to create SVG's, does anyone know what px/inch should be used for OpenSCAD?

---

Posted on *2017-07-10 09:30:47* by *Bar*

I've found the right value for inkscape to be 96, so that might be worth a try

---

Posted on *2017-07-10 11:26:05* by *TheRiflesSpiral*

On a Windows PC, generally 96 is a good place to start. (Windows native display resolution is 96ppi) On a mac, 72 would be more appropriate.

Vector graphics software will generally export at the native display resolution of the operating system when no scale is provided since they're unit independent.

Linux varies and is also customizable so all bets are off!

---

Posted on *2017-07-10 11:31:20* by *jbnimble*

Using Linux, so I guess I'll have to figure that out.

---

Posted on *2017-07-10 12:49:26* by *TheRiflesSpiral*

Try:
---
xdpyinfo | grep dots
---

This should return "96 dots" or something like that.

---

Posted on *2017-07-10 12:58:51* by *gero*

whoareyou@dexter:~$ xdpyinfo | grep dots
  resolution:    96x96 dots per inch :-)

---

Posted on *2017-07-10 13:09:59* by *TheRiflesSpiral*

Well there you go. I checked an Ubuntu Mate install, a Raspbian install and an ancient Fedora machine and they were all 96. An old Unix (Sun) system was 120 though... so probably safe to start at 96 and test.

---

Posted on *2017-07-10 14:01:36* by *davidlang*

px is supposed to be 72/inch per standard (but not everyone follows standards)

as noted, what matters is that you match your CAM software to what your drawing software expected.

---

Posted on *2017-07-10 14:03:00* by *davidlang*

the resolution of your screen should not matter, you aren't measuring things on your screen and expecting them to match those measurements on wood.

---

Posted on *2017-07-10 14:52:07* by *TheRiflesSpiral*

Not the display resolution, but the -system- resolution. They are usually the same, but sometimes are not.

In the absence of a unit of measure applied to the values in a vector file, the default system resolution is used. This is pretty common. (For units to not be stored with the file) It's not necessarily the screen resolution (this varies by display and can be taken from the EDID info for a specific display)

I run into this a lot when people want to print literature and send me technical drawings to include for diagrams. The scale is always messed up.

---

Posted on *2017-07-10 15:17:04* by *davidlang*

SVG files do not have a resolution in dots, they may have a resolution defined in points, but points are defined to be 1/72"

svg files should be defined in real-world measurements, not system specific numbers. They get converted into system/display measurements only at display time. They are like pdf and postscript files that way.

you should never convert to display measurements until the last possible chance.

---

Posted on *2017-07-10 21:20:29* by *TheRiflesSpiral*

SVG files (and other formats) often aren't defined in real-world measurements. I agree they should be, I'm saying they often aren't. Also, some software ignores the real-world measurements that are given during import.

Vector format measurements have to be interpreted for display and also during import into another piece of software which is what we're talking about here.

There's no conversion occurring... you just have to tell the software you're importing the file into what the scale is and in the absence of a scale defined in the file, some software uses the system resolution as a default.

Consider this simple bit of code:
---
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
 xmlns:xlink="http://www.w3.org/1999/xlink">
<desc>Output from Flights of Ideas SVG Sketchup Plugin</desc>

  <path id="face0-cut"
 style="fill:none;stroke:#0000FF;stroke-width:1;stroke-miterlimit:4;str oke-dasharray:none;stroke-linejoin:round;stroke-linecap:round"
        d="M 0.0,0.0 L 0.0,25.4 L 25.4,25.4 L 25.4,0.0 L 0.0,0.0 "
  />
---
This is an export using the SVG exporter extension  for Sketchup. The units in this drawing were set to Imperial. You'll notice the document doesn't have any units defined. So in this case, what does 25.4 mean? I know it's a 1" square (I drew it) so I know that It's actually exporting in mm but nothing that can import this file knows that. You have to tell it what the scale is. In this case, if you import the SVG into MakerCam, you get a .3528" square with the upper left corner at 0,0.

Now if I set the Sketchup document units to Metric and export the same drawing, I get this:
---
<svg width="45.4mm" height="45.4mm"
 viewBox="0 0 45.4 45.4"
 xmlns="http://www.w3.org/2000/svg" version="1.1"
 xmlns:xlink="http://www.w3.org/1999/xlink">
<desc>Output from Flights of Ideas SVG Sketchup Plugin</desc>

  <path id="face0-cut"
 style="fill:none;stroke:#0000FF;stroke-width:1;stroke-miterlimit:4;str oke-dasharray:none;stroke-linejoin:round;stroke-linecap:round"
        d="M 0.0,0.0 L 0.0,25.4 L 25.4,25.4 L 25.4,0.0 L 0.0,0.0 "
  />
---
The units are now defined. Anything should be able to import that properly. If you import this SVG into MakerCam, you get a 1" square with the lower left corner at 0,0.

This is just a quirk of this particular export plugin. AutoCad, DraftSight, etc all have these quirks that have to be worked around depending on how a file is set up and exported.

---

Posted on *2017-07-11 04:25:45* by *jbnimble*

@TheRiflesSpiral, thanks! I did some more searching, before reading your post, and found that the internet agrees with you :)

My solution for SVG files is now to modify the OpenSCAD exported file from this:
```
<svg width="890" height="280" viewBox="-445 -140 890 280" xmlns="http://www.w3.org/2000/svg" version="1.1">

```
To this:
```
<svg width="890mm" height="280mm" viewBox="-445 -140 890 280" xmlns="http://www.w3.org/2000/svg" version="1.1">

```
ie. Adding "mm" to 'width' and 'height' attributes, since I'm assuming those units in my OpenSCAD model. 

Apparently in OpenSCAD-land it is important to them to keep unit agnostic, and manually adding the units for an SVG is not onerous.

---

Posted on *2017-07-11 06:00:40* by *TheRiflesSpiral*

Excellent solution. If you're comfortable digging around in XML files, you can solve a lot of problems. For instance, the FlightsOfFancy plugin goes out to 12 decimal places sometimes. 9 of those decimals are zeros... what's the point?!

To be completely honest, I think the scaling and multiple software issue will eventually drive me to an all-in-one CAD/CAM solution like F360. I just have to force myself to learn it properly.

---

