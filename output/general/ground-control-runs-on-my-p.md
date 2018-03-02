## Ground Control runs on my Pinebook!
Posted on **2017-06-24 12:18:59** by **mattnelson**:

I just received my new $99 ($150 shipped with accessories) Pinebook laptop.  https://www.pine64.org/?page_id=3707  After some effort I now have Ground Control running on it!

---

Posted on **2017-06-24 13:36:35** by **scottsm**:

What things did you need to do to get it to run?

---

Posted on **2017-06-24 16:58:17** by **mattnelson**:

I had to play with it some.  I started off by following the linux install wiki but ran in to trouble on step 2 when it said to run the pip command.  I got the command not found error.  I googled until I found the commands to get pip installed.  I then found and ran the "pip install -r requirements_linux.txt command in the ground control folder.  This mostly worked.  The only error I received at this point was it couldn't find truefont or something like that.  I googled the command to install that then reran the pip install command above and everything worked.

---

Posted on **2017-06-24 17:52:09** by **scottsm**:

That’s good to hear. The Pinebook could be an economical controller for the Maslow.

---

Posted on **2017-06-24 23:52:42** by **gero**:

Great option. What Linux does it ship with?

---

Posted on **2017-06-25 01:45:39** by **mattnelson**:

Umbunto Mate

---

Posted on **2017-06-25 05:59:26** by **TheRiflesSpiral**:

Ubuntu has apt for a package manager. You can use apt-get install... from now on. Although pip is fine too.

---

Posted on **2017-06-25 16:29:06** by **gero**:

I had to add my self to the 'Dialout' group. Perhaps the installation the Arduino IDE does that already,

---

