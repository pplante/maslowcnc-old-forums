## Invalid  syntax
Posted on *2017-07-10 14:45:30* by *taylor47*

I am trying to configure python for the first time - when I try any of the commands listed I get an Invalid syntax error, see below

 python -m pip install pyserial
                ^
SyntaxError: invalid syntax

Any ideas?

---

Posted on *2017-07-10 14:51:05* by *scottsm*

What platform are you using?

---

Posted on *2017-07-11 06:03:43* by *TheRiflesSpiral*

Can you try:
---
man pip
---
And see what the return is? I'm wondering if maybe pip wasn't installed during your python install.

Also, it's always a good idea to:
---
sudo apt-get update
---
before doing any package work.

---

Posted on *2017-07-17 12:12:54* by *taylor47*

I am getting the below for man pip

  File "<stdin>", line 1
    man pip
          ^
SyntaxError: invalid syntax

and for the sudo script 

>>> sudo apt -get update
  File "<stdin>", line 1
    sudo apt -get update
           ^
SyntaxError: invalid syntax

---

Posted on *2017-07-17 12:13:17* by *taylor47*

I am using a windows 10 machine

---

Posted on *2017-07-17 12:33:05* by *mrfugu*

not a windows guy myself, but  it sounds like python isn't installed yet. 

https://github.com/MaslowCNC/GroundControl/wiki/Windows  

also, theRiflesSpiral's instructions were for linux. 

good luck!

---

Posted on *2017-07-17 12:37:24* by *TheRiflesSpiral*

Oh, shoot. Sorry about that Taylor. I recognized the syntax of Python but I forgot it's the same across platforms and assumed you were on a linux system. My bad.

---

Posted on *2017-07-17 12:39:46* by *taylor47*

after further reading it dosnt look like i need python unless I am going to run ground control from the source code, thats way to involved for me. thanks for your help

---

Posted on *2017-07-17 23:51:11* by *cameronswartzell*

The issue here is python was not added to "the path" in windows, so it's not recognized as a command. Bar's guide mentions this, and there is a link showing the quick fix for adding it, if anyone else is having this problem.

---

