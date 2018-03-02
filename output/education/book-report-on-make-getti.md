## Book report on "Make: Getting Started with CNC"
Posted on **2017-01-31 15:49:03** by **jbnimble**:

I got this book primarily to educate myself as Maslow will be my first CNC, and so decided to do a little write up to have a place to find my notes. This book primarily focuses on CNC using the Shapeoko in addition to coverage of general CNC concepts. The parts I found the most useful were terminology and explanation of the process and tools involved in working with a CNC.

Make: Getting Started with CNC
Personal Digital Fabrication with Shapeoko and other Computer-Controlled Routers
by Edward Ford
2016

The book includes the names and descriptions of the hardware associated with a router/spindle for example: spindle/router, neck/shank, collet, collet nut, and end mill. The author suggests using ficture tape or double sided tape for securing material, not sure if that is completely applicable for the geometry of Maslow, but I had never heard of ficture tape. Other securing solutions included step clamps, t-slots, threaded inserts, screws, tape, vises, and a vacuum table of which I suspect screws, vises and possibly tape would apply to Maslow CNC.

The author has several  suggestions on end mills. For example, using a center cutting end mill because it can cut straight down into material similar to how a drill bit works. A "starter set" of end mills is suggested to include: two flute spiral upcut bit, two flute ball nose end mill, straight flute bit, v-bit 60 or 90 degrees, and conical engraving bit. Other types of end mills that were discussed were table surfacing and square (flat tip). Terminology associated with an end mill include overall length, shank diameter, cutting edge diameter, cutting length, reach, and flutes.

Tool holding methods include jar chuck (like a traditional drill chuck), or fixed diameter collet. The author lists ER collets as ER-8, ER-11, ER-16, and ER-20. The collet is tool specific, so be sure to buy the collets that are meant for the router you plan to use.

A section I found particularly interesting was tool paths. The book discusses the difference between 2D, 2.5D, and 3D tool paths. The kinds of CAM operations like outside profile, inside profile, pocket, engrave, and peck drilling. The kerf, or gap made by cutting from the end mill or saw blade. Tips like pocket, drilling, and engraving must happen first or dog bone and T-bone overcut's for inside corners. The author explains the difference between parallel and contour finishing, and the use  of an edge finder/wiggler for finding the edge of a part that is already made.

CAM software and other websites that are listed include:
http://www.makercam.com/ (free web based, could not find a license)
http://pycam.sourceforge.net/ (GPLv3 Linux, Windows, MacOS)
https://inkscape.org/en/ (GNU GPLv2 Linux, Windows, MacOS)
https://nraynaud.github.io/webgcode/ (MIT License, free web based)
http://camotics.org/ (GNU GPLv2, Linux, Windows, MacOS)
http://librecad.org/cms/home.html
http://qcad.org/en/
http://www.openscad.org/
https://www.blender.org/
http://freecadweb.org/
http://www.sketchup.com/
http://www.thuijzer.nl/image2gcode/
http://www.scorchworks.com/Dmap2gcode/dmap2gcode.html

http://www.vectric.com/ (commercial, product is called VCarve)
http://www.cambam.info/ (commercial)
http://www.autodesk.com/products/fusion-360/overview (commercial)
http://www.grzsoftware.com/ (commercial, product called MeshCAM)
http://dolphin-cadcam.webnode.com/ (commercial, several web sites very confusing)

http://buildlog.net/ (project site)
http://lcamtuf.coredump.cx/gcnc/ (guide to CNC)
https://github.com/gnea/grbl (GPLv3, CNC control software for Arduino)
http://linuxcnc.org/ (GNU GPLv2, CNC control software for Linux)

https://shop.carbide3d.com/ (equipment vendor)

Project Ideas and interesting sites:
http://www.shapeoko.com/forum/viewtopic.php?f=30&t=4603
http://100kgarages.com/
https://www.opendesk.cc/
http://www.evilmadscientist.com/2012/stipplegen-weighted-voronoi-stippling-and-tsp-paths-in-processing/
http://www.shapeoko.com/wiki/index.php/Tsp_sld
http://jasondorie.com/page_cnc.html

---

Posted on **2017-01-31 17:12:45** by **davidlang**:

A lot of what is covered isn't a good fit for the capabilities of the Maslow

The Maslow is a 2.5D machine, it is very limited in what you can do with the Z axis because it rides on the workpiece 

As far as chucks go, you really don't have an option, the router will come with what it comes with, and you are stuck with it. Similarly, for mills, you are limited to things with a 1/4" or 1/2" shaft to fit the router (and they can't be too long (again, due to the limited Z capability)

Similarly contour vs parallel finishing is also not that relevant because of the limited Z capabilities.

As far as workholding is concerned (vices, etc) the Maslow is designed for gravity to hold the piece in place.

thin double-sided tape can work, my favorite is actually composite nails from a nailgun ( https://raptornails.com/ ). they hold nicely against normal  working loads, don't damage anything if you cut through them, and are easy to remove (a sharp sideways rap will snap the nails cleanly along the joint

---

