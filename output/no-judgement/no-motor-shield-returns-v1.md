## No motor shield returns V1.1
Posted on *2017-07-15 12:37:33* by *gero*

I have a Mega connected in the office with no motor shield, just for fun and help while in the forum. It tells me I have PCB v1.1. Not a big issue, but it could confuse and delay trouble shooting on damaged shields. Is there a way to catch no shield?

---

Posted on *2017-07-15 13:18:01* by *mrfugu*

file an issue report? https://github.com/MaslowCNC/Firmware

---

Posted on *2017-07-15 14:57:16* by *gero*

@mrfugu It's not really an issue, as it has no negative effects if you run your Mega without the motor shield. Think the Github should be for issues that effect more than one. Wanted some feedback here first if this is a feature request, or something that needs to be addressed. It will be at the bottom of the priority list. I have a damaged shield around and will try that. If it gives me a wrong version there might be a point.

---

Posted on *2017-07-15 15:26:55* by *mrfugu*

the issue is only in the context of error reporting. if the audrino can detect the presence (or not) of the shield, it should, and report its current state to Ground Control, which should display it to the user in some manner.

---

