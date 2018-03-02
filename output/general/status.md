## Status?
Posted on **2017-06-19 12:55:39** by **rancher**:

Okay gang, where are we at?  I've been waiting for someone to report success with calibration and cutting, but I'm getting mixed messages.  A pretty good test run yesterday, but I'm seeing some sled danger on github, calibration fails, etc.  I can't tell if I should go try to calibrate and cut, or keep waiting.  I know you software dudes are seeing dropped characters.  Is that still a problem?  Will it affect my simple files?  Is calibration working?  I really don't want to spend another two hours in my shop for a failed calibration routine, I've done that quite a few times this month already.  Can we please get an update on current version, and last known good config. if it isn't there yet.  It worked well for me back in April, but since then I've been unable to make it through the calibration without an error, let alone cutting.

---

Posted on **2017-06-19 16:03:29** by **rancher**:

Well, I turned on my PC and the motors made their happy buzz greeting.  Uploaded new firmware, new GC, and that's the last I heard from the motors.  GC looked to be working, connected, but....no go.

---

Posted on **2017-06-19 17:20:56** by **davidlang**:

go back to the prior firmware (v0.73)

---

Posted on **2017-06-19 17:42:56** by **Bar**:

Hmmm....I was waiting for someone else to answer because I always think everything is working. Just tested my machine with the latest and it seems to be happy.

Is everyone else seeing the issue too?  Anyone have specifics on what seems to be going wrong?

---

Posted on **2017-06-19 17:55:07** by **Bar**:

Actually, I think I figured it out. I believe the issue should be fixed

---

Posted on **2017-06-19 18:19:47** by **rancher**:

> @davidlang
> go back to the prior firmware (v0.73)
The problem with going back and forth is somewhere there is a calibration problem and somewhere else a dropped char. problem.  I can't tell what's what.  I propose we are mature enough for a stable version and betas.  I was happy back in April, it doesn't need to cut fast, or PID, or whatever all the things are that you guys are working on that I'm thankful for.  But, nonetheless, I'd be giving you way, way, way more feedback if I could go switch back and forth between known good and beta.  Just sayin'.  I'm okay with whatever and I know it's beta, but.....we are kinda stalling out it seems.

---

Posted on **2017-06-19 18:22:43** by **rancher**:

What I'm trying to say is, Maslow works great already for me.  Instead though I sound like I'm bummed and people watching are getting the wrong idea.  This thing works beyond my expectations.  Let's get back to cutting so you can get back to coding.  My email train from github shows how hard you are all working.  It's appreciated.

---

Posted on **2017-06-19 18:30:39** by **davidlang**:

what is considered "known good"? Every version released has had bugs that are fixed in the next version, and every release has "not worked" (or some definition of "worked") for someone.

Unfortunantly, there have also been new bugs introduced as well.

If there is a version that works for you, you don't have to upgrade from it. The problem is that the 'working version' is going to be different for different people.

now, we are a far cry from the early days (only a month ago) when the software was evolving hour by hour and if o, on Sunday, you were running software released Saturday morning, you were hopelessly out of date. Releases are only made once a week, and there are no known bugs at the time of release.

The problem with shifting to stable/beta releases is how do you define what's stable and what's not?

---

Posted on **2017-06-19 18:57:36** by **rancher**:

Stable was cutting with a bit of distortion that we could tune with settings.  No sled tearing action, motors working, 25ipm.  We were there, and we are all interested in pushing forward, but I can't help you if it's broken every time I have a chance to go to my shop.

---

Posted on **2017-06-19 19:06:43** by **rancher**:

How about the version Bar cut swords with?  That didn't cut off any legs mysteriously.

---

Posted on **2017-06-19 19:46:03** by **Bar**:

I would say that every update was better than the one before except for the release last Wednesday, I try to make the Wednesday version which is the "release" the best that I possibly can. 

This last week a bug slipped through. Grabbing the "latest" off GitHub is a little more of a grab bag because that code is what I'm working on minute by minute. 

I will make sure that this Wednesday's version is more thoroughly tested than usual and can serve as a good stable place for us to rely on.

---

Posted on **2017-06-20 04:47:43** by **rancher**:

Well, I'm confused.  I thought we should always use the green button, but I found releases last night.  So, which ones work?  David, what are you having success cutting and calibrating with, GC and Firmware?  Anyone else who has successfully calibrated and cut recently, what versions work for you?  I'd really like to get back on the boat, but I can't seem to figure out how to get there.

---

Posted on **2017-06-20 12:17:53** by **rancher**:

Does anyone have any input on good versions for calibration?  I have time to try to get back up these next couple days, but I have no idea what to try.

---

Posted on **2017-06-20 12:55:47** by **carlosrivers**:

So to clarify we should be using the firmware that is the one before this latest version?

---

Posted on **2017-06-20 13:01:27** by **Bar**:

I've been trying not to answer this because I think having someone else's opinion about what works and what doesn't is valuable.

I just want to add that my goal is by the end of tonight (possibly late) to have a version of both the firmware and Ground Control which I have thoroughly tested for you guys so we have a solid place to work from.

---

Posted on **2017-06-20 13:24:35** by **davidlang**:

Downloading releases gets the 'wednesday release' version (the numbered versions)

downloading with the green button gets you the up-to-the-second version, with all the work done since the last release

the releases are tested more, but if there is a feature you want to test, or if you are having problems with the prior release (or if you are just willing to test the latest-and-greatest to help find bugs before the release), running the versions downloaded with the green button can be useful.

If you are going to be running the non-release versions, I would suggest that you get it via git clone, not just downloading a zip file. It is faster to update to new versions (via the git pull command) than downloading another zip file, and it gives you the ability to do git bisect which is a very powerful tool for finding when a bug was introduced, which makes it much easier to fix the bug in many cases.

a few posts down there is a topic on testing, and in that case the person cutting used firmware .73 with GC .76

I do not have a machine yet, so I can't test things myself.

---

Posted on **2017-06-20 13:29:37** by **gero**:

Tried not to answer, because I like to repeat and see it at least twice, before I comment or file an issue. Sadly no time, so I will share the unconfirmed observations.
Calibration:
a) lowering Z 0.1 raised sled a little, raising Z 0.1 lowered sled.
Both only the first time I pressed the buttons.
b) If the first testpattern cut is not visible, you can't repeat without entering some numbers. Going back also does not help. You need to enter some imaginary numbers. 1st cut can not be repeated.
The top left cut was not visable, so no measurement,
trying to go back and set zerro did not help.
Recut testpattern stayes grayed out. Add a start over button?
c) cuts lower Z into the moving cut. Moves do not wait until Z has reached the final depth.
d) 604mm is accepted to finish the calibration? That is 4mm off the target.
e) calibrating right chain length, the left motor wiggles and ends not exactly at 12:00, after the right chain is measured.

---

Posted on **2017-06-20 13:37:30** by **gero**:

Left motor while right chain is measured https://youtu.be/Z5MZliyXsV0

---

Posted on **2017-06-20 14:17:37** by **rancher**:

Thank you all very very much!  It is as I suspected by following the github threads.  It looks like the latest few iterations are throwing up various barriers to calibration, which is just fine with me.  I can wait for tomorrow's official for sure, and the boys are painting the boat I'm wiring at the moment, so I am off this afternoon and tomorrow.  Bar, if I can help test a new version that *might* work, I'm in.  Like I said, I just want to jump back on, and it's been hard to track with all the various conversations.

I'll sit tight and keep checking in.  I would like to help if I can.

---

Posted on **2017-06-21 11:55:26** by **gero**:

Was anything changed on the issue that 604mm is accepted to finish the calibration?

---

Posted on **2017-06-21 12:07:37** by **Bar**:

604 seems really over size to me. Do you get 604 every time if you repeat the process?

---

Posted on **2017-06-21 12:09:57** by **gero**:

I have the brackets very close to the router now and start at 609mm. The problem for me it finishes when I enter 604mm. That is not 0.5mm near. That is 4mm off.

---

Posted on **2017-06-21 12:38:54** by **Bar**:

It's looking for a less than .5 mm difference between the horizontal and vertical measurement. I'm going to update the text to be more clear right now.

I've been trying to avoid working with the absolute measurement, because then things like bit size and where you measure from and to start to matter. When measuring the distance we can get away with any bit size and measuring from anywhere to anywhere else as long as we're consistent.

---

Posted on **2017-06-21 12:40:01** by **gero**:

Oh, I assumed it was going for a fixed distance :-)

---

Posted on **2017-06-21 12:41:47** by **gero**:

So we are calibrating synchronization X/Y and not accuracy?

---

Posted on **2017-06-21 13:37:29** by **Bar**:

We're really refining the measurement of the distance between the sled mounting points. The theory is that using the chain to measure the distance between the motors gives us a very accurate measurement for that spacing, then counting the links gives us a guess for the distance between the sled points. Cutting the test pattern refines the measurement. Keep in mind that where the chains attaching to the sled actually flex is 1/2 a link past the edge of the bracket so it's a rough distance to measure accurately by hand

---

Posted on **2017-06-21 13:42:43** by **davidlang**:

is the resulting distance figure plausable? or is it obviously incorrect, but producing the right result in the center of the wood?

---

Posted on **2017-06-21 13:44:14** by **Bar**:

:-(

---

Posted on **2017-06-21 13:47:44** by **gero**:

24th April -> 2017 I cut near the center within a 10th of a mm. https://muut.com/u/maslowcnc/s1/:maslowcnc:0WgM:perfect.jpg.jpg
27th April -> Over the sheet the worst was 4.8mm off https://muut.com/u/maslowcnc/s3/:maslowcnc:S5MO:end.jpg.jpg
19th June  -> https://muut.com/u/maslowcnc/s3/:maslowcnc:uA4N:imag0863.jpg.jpg
21th June  -> I measured the center and a few more squares, but can't be bothered to measure more due to measurements 4-6 mm off already.
However, I modified the sled. I have three mounting points. I was planing to test the entire sheet with the three mounting point of the brackets. Sadly I also reduced the weight. To many variables have changed. Will try first to mount the brackets back to the the outside.

---

Posted on **2017-06-21 13:48:13** by **Bar**:

@Gero How did you do the calibration that first time that was spot on? Was the bad one recently when you saw the 606mm calibration?

@davidlang I end up with a value that seems to be pretty much correct for my sled. It's a tough distance to measure by hand, but it looks right. Certainly plausable, but I'd be interested to hear what everyone gets

---

Posted on **2017-06-21 13:51:59** by **gero**:

The 10th of a mm, we entered all measurements manually and I slowly increased the distance of of the brackets.

---

Posted on **2017-06-21 13:54:46** by **gero**:

Will do a few tests on Saturday, so god will that my job does not ruin the weekend. Will dig out the manual entered numbers, put the brackets where you have them and see what difference that makes.

---

Posted on **2017-06-21 14:01:44** by **Bar**:

Weird, because the automatic calibration process should be based on the same technique. When you pull out the old numbers which were spot on, I'd be curious to know how they compare to the numbers in your settings after the automatic calibration process. @davidlang is right, let's keep an eye on the automatic process and make sure it's not giving us numbers which we don't think are plausible

---

Posted on **2017-06-21 14:09:46** by **gero**:

Getting late here. Need to log out. See you soon here. Always fun.

---

Posted on **2017-06-21 14:11:23** by **Bar**:

Night Gero!

---

Posted on **2017-06-21 15:58:35** by **rancher**:

Bar, I counted out 48 holes and calibration cut was dead on first try.  I originally built my sled with your 130mm (I think iirc) measurements as accurately as I could.

---

