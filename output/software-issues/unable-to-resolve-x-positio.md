## Unable to resolve x-position error
Posted on **2017-03-20 14:04:19** by **Bar**:

The latest version of the firmware up now should fix the "unable to resolve x position" error. The problem had to do with the way the internal math was calculating the starting position of the router. When the machine first turns on, it knows it's starting chain lengths (which are saved), but not it's (x,y) coordinates. It was calculating it's starting (x,y) using a flawed approximation. 

Rather than keeping the flawed approximation, I just removed it entirely because I would rather not have a section of code which is at least partly broken hanging around. We may see some strange behavior around the machine knowing where it is on startup now. 

Basically, what will happen now is that when the machine turns on, it knows it's real chain lengths, but thinks it should be at position (0,0) so it will show a large error. Clicking the "Home" button several times or any of the positioning arrows will let the machine catch up to the new target.

Not a perfect solution, but better than a cryptic error message.

---

