## Python on El Capitan
Posted on **2016-12-27 19:56:38** by **TheRiflesSpiral**:

Howdy. I decided to give Python a try on the MacBook Pro this evening. The Python install went fine, as did Pyserial. Pip was up-to-date and the wheel and setuptools installs were fine as well.



Docutils and pygments also installed properly but the dependencies install went wrong at pypiwin32. Obviously the win32 API's aren't present on an OSX machine, or any *nix variant for that matter. I decided to skip over that one but the remaining kivy dependencies wouldn't install either.



Collecting kivy.deps.sdl2

  Could not find a version that satisfies the requirement kivy.deps.sdl2 (from versions: )

No matching distribution found for kivy.deps.sdl2

Brians-MacBook-Pro-2:~ bdieckma$ python -m pip install kivy.deps.glew

Collecting kivy.deps.glew

  Could not find a version that satisfies the requirement kivy.deps.glew (from versions: )

No matching distribution found for kivy.deps.glew



The Kivy install failed as well though I presume it has to do with the dependencies above.



Collecting kivy

  Downloading kivy-1.9.1.tar.gz (16.4MB)

    100% |████████████████████████████████| 16. 4MB 50kB/s 

    Complete output from command python setup.py egg_info:

    Using distutils

    

    Cython is missing, its required for compiling kivy !

    

    

    Traceback (most recent call last):

      File "<string>", line 1, in <module>

      File "/private/var/folders/6g/fqb9sxlj0xq4xlwwqhhp7qmr0000gn/T/pip-build-c4 Uk_F/kivy/setup.py", line 184, in <module>

        from Cython.Distutils import build_ext

    ImportError: No module named Cython.Distutils

    

    ----------------------------------------

Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/6g/fqb9sxlj0xq4xlwwqhhp7qmr0000gn/T/pip-build-c4U k_F/kivy/

---

Posted on **2016-12-28 08:29:59** by **scottsm**:

I found that pypiwin32 wasn't needed on my OS X setup. I downloaded the binary <https://kivy.org/downloads/1.9.1/Kivy-1.9.1-osx-python2.7z> and followed the installation instructions <https://kivy.org/docs/installation/installation-osx.html>. After completing the steps including "Start from the Command Line" I could run 'kivy cncgc.py' from within GroundControl-master and see the GUI. I loaded an .nc file and can see the tool path. I wish there was a way to simulate a cutting session.

 I did open the simulation.py and played with the 2D sled controls. That might be interesting for the folks designing an alternative sled, or altering the bed size.

---

Posted on **2016-12-28 10:02:03** by **Bar**:

Thanks scottsm!

---

Posted on **2016-12-29 04:37:22** by **TheRiflesSpiral**:

Great! I'll try this out later today.

---

