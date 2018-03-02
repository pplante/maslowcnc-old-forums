## Arduino Code Style
Posted on **2017-01-22 18:11:07** by **jbnimble**:

Was thinking on doing some code style formatting (non-functional changes) and possibly adding more comments to the [Firmware](https://github.com/MaslowCNC/Firmware) code base. What sort of coding style is preferred? For example, tabs vs spaces, etc. Is there interest in adding support for  [Doxygen](http://www.stack.nl/~dimitri/doxygen/) comments for generating documentation? Thoughts? Opinions?



Found these Arduino [Style Guide](https://www.arduino.cc/en/Reference/StyleGuide) and [API Style Guides](https://www.arduino.cc/en/Reference/APIStyleGuide) but they are intentionally vague.



Less vague, but an example of a [code style guide](https://sites.google.com/a/cabrillo.edu/cs-11m/howtos/cppdoc).



My main interest is to better understand the code, and making it have a consistent style while examining the code could be a useful exercise.

---

Posted on **2017-01-23 09:06:48** by **Bar**:

Yes yes yes! Please please please!



I tried to add doxygen compatible block comments to the start of each function, but I've been doing a bad job of keeping up with them recently. 



The other rules I've been following are. 



4 spaces to indent

#defines are ALLCAPS

variables and functions are camelCase 

libraries are CapitalizedFirstLetterToo



All of which seems pretty much consistent with the code style guide you linked. https://sites.google.com/a/cabrillo.edu/cs-11m/howtos/cppdoc



In a small world coincidence, I used to live down the street from the college that wrote that guide, so maybe it's a local dialect to use those rules



I tried to add code climate to automatically monitor style guidelines last week, but apparently it doesn't support C++ 



If you are working your way through the code and have any questions, I am more than happy to answer them.

---

Posted on **2017-01-23 13:42:46** by **jbnimble**:

Should the header with the license statement be "Copyright 2017 Bar Smith" instead of 2014?

---

Posted on **2017-01-23 15:30:59** by **Bar**:

I think it's supposed to be 2014-2017. Going through all the GPL stuff and updating it is on my todo list. There's a bunch of "Makesmith" in there that needs to be "Maslow" too. If you see any that you want to change while you are in there, go for it.

---

