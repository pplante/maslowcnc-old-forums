## Problems running Ground Control on Android
Posted on **2017-02-04 11:04:00** by **jbnimble**:

Used the [Kivy Buildozer VM](https://kivy.org/#download) to create an APK from the [Ground Control](https://github.com/MaslowCNC/GroundControl) source, and then installed the APK onto an Android tablet (4.1.2). The app when started has a "Loading..." screen and then dies. 

Anyone have any ideas on what I might be missing? If anyone has successfully run Ground Control on an Android tablet, what steps did you follow?

---

Posted on **2017-02-04 14:49:45** by **Bar**:

I haven't messed with Android yet, but I'm excited that you are looking into it. The goal is to target Windows, Mac and Linux first and then bring in Android. I didn't list Android as a supported platform on the website because I thought it might be a little tricky to get working.  I would bet the issue you are dealing with has to do with the serial port module PySerial. I looked into it briefly a while ago and I believe that there are some attempts to port it to Android, but I don't think Buildozer is able to wrap it up without a little bit of extra love.

---

Posted on **2017-02-08 18:50:08** by **jbnimble**:

Ok, lots of research later, I got Ground Control to work on my Android tablet. As @Bar mentioned there is a little "love" that has to be configured within Buildozer, but not too bad, and a file rename. I wrote down all the steps I followed, it would be nice if someone could validate that this also worked for them. I could not do much more than view the app and press some buttons since I don't have hardware to plug into for testing.

How to create a "Ground Control" APK for Android

Download and extract [Kivy Buildozer VM](https://kivy.org/#download)
Install VirtualBox, and open Kivy Buildozer VM > Start
Install Guest Additions
Add Shared Directory (lets call it "HostSharedDir") to the host machine
Restart VM

Within the VM, open the "Web Browser" and download the [Ground Control master zip](https://github.com/MaslowCNC/GroundControl).

Open "LX Terminal" and change directories to the downloaded zip
$ cd Downloads
Extract the zip
$ unzip GroundControl-master.zip
Change directories into GroundControl
$ cd GroundControl-master
Initialize Buildozer
$ buildozer init 

Modify generated "buildozer.spec" file to the following:
`    requirements = pyserial,kivy`
`    android.p4a_whitelist = lib-dynload/termios.so`

Note: not totally sure if the buildozer.spec changes are "required", but they were things I changed based on my research. The main error was due to the following file name problem.

Due to Kivy needing a "main.py", copy and rename:
`cncgc.py -> main.py`

Build the project
$ buildozer android debug
Mount the previously created shared directory
$ sudo mount HostSharedDir
Copy the APK to Host
$ sudo cp ~/Downloads/GroundControl/bin/MyApplication-0.1-debug.apk /media/sf_HostSharedDir
Copy APK to SD card
Insert SD card into Android tablet, install APK

On my tablet it took a long time to load with a "Loading..." screen, and then the app with all the buttons showed.

For debugging purposes if you ever need it the name of the app is: `org.test.myapp/org.renpy.android.PythonActivity`

I found an app from the Play Store useful called [aLogcat](https://play.google.com/store/apps/details?id=org.jtb.alogcat&hl=en) for viewing logs on the device.

---

Posted on **2017-02-24 10:30:59** by **Bar**:

That's fantastic! I hadn't planned to get Android working for quite a while. Would you be willing to share a copy of your APK so I can play around with it on my phone?

I know apps packaged with Kivy take a lot longer to launch the first time because all the files are being extracted in the background.

Great work!

---

Posted on **2017-02-24 12:17:39** by **jbnimble**:

@Bar, I'll pull the latest code, generate an apk and put a link here. It was not too bad, figured out the kinks in an evening or two. Hopefully I'll get the file up sometime this evening. Probably I should copy these instructions to the wiki...

---

Posted on **2017-02-24 15:03:58** by **Bar**:

That would be fantastic! Thank you.

---

Posted on **2017-02-25 01:25:02** by **jbnimble**:

Created a repository to store the built apk https://github.com/jbnimble/GroundControlAndroid, was able to load and start the application from my Android tablet

---

Posted on **2017-02-27 10:46:21** by **Bar**:

Awesome! I'll give it a go on my phone!

---

Posted on **2017-02-27 13:42:30** by **Bar**:

I'll have to work on how everything renders on very small screens like phones, but other than that it runs great. Good work!

---

Posted on **2017-02-27 13:48:45** by **jbnimble**:

I added a wiki page for building ground control executables and added what I did for Android, and left a place holder for other platforms.

---

