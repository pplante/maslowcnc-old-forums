## GroundControl preflight
Posted on **2017-01-30 11:31:28** by **scottsm**:

@Bar, I'm not sure of the purpose for the [10<< 1< || 1>  10>>] section of the controls, but I've been using it to preflight .nc files.
 The controls don't seem to affect anything but the positionIndicator on the screen, so perhaps this is what they are for. That said, I have a couple of tweaks or suggestions to offer:
 One can step beyond the end of the source file and crash Kivy. Using exception handling would prevent the crash.
 G code statements which move only in the Z axis jump the positionIndicator momentarily to (0,0). I suggest preserving the location and changing the color of the positionIndicator to visually flag the operation. Maybe white for a step that includes a change of Z?
 As I said, I'm not sure I'm using these for their intended purpose. If the changes seem useful though, I'll put in PR's for them.

---

Posted on **2017-01-30 17:13:56** by **Bar**:

You are pretty close to the intended purpose ;)

Those are there to fast forward through a cut. I found that somewhat regularly I either wanted to skip over part of a file or less commonly go back to something that was run earlier. You can pause and then fast forward or jump back at any point in the file. 

If you wanted to make a PR to fix the fact that you can fast forward past the end of the file and crash the program, that would be fantastic. That's a bug for sure. If not I can fix it too.

I'm also open to any new features that you think would be useful.

---

Posted on **2017-01-30 19:14:40** by **scottsm**:

I see how that could be very useful. I'll do the PRs and let you decide on them.

---

