## what actually talks to the router?
Posted on **2017-01-07 05:59:08** by **nathanmiller**:

I feel dumb asking this but I have never run a CNC router in my entire life... but sure can't wait to get started!! Can you tell me exactly what speaks to the controller/router? I know I can create designs in Sketchup or similar software, and I think I understand how to prepare and export the design as G-code in a .dxf file. But what happens next? What software do I load the .dxf file into that speaks directly to the Maslow controller, and makes the CNC magic happen?

---

Posted on **2017-01-07 06:26:09** by **TheRiflesSpiral**:

You'll need a computer running the GroundControl software. Over in Dev there are a couple of discussions around getting it to function on a Raspberry Pi which would be a sub-$100 solution. But any ol' windows computer with a USB port is going to work fine. I'm also working on getting it going on an El Capitan install of MacOS and lastly, I'm going to try to get it going on an older Mac Mini running Snow Leopard.

---

Posted on **2017-01-07 11:45:58** by **Bar**:

That's a great question! TheRiflesSpiral pretty much nailed it.

The big old school machines usually have either a dedicated computer that controls them or a control panel which accepts USB drives with g-code files. 

The controls are really just there to move the machine to the position where you want to start the cut, and keep an eye on it while it's running. To do those two things we use Ground Control which in it's current infant state looks like this:  [GroundControl](//muut.com/u/maslowcnc/s3/:maslowcnc:pmfl:groundcontrol.jpg.jpg) 

Basically you get a digital position readout, a preview of the part(s) being cut and their positioning on the piece of plywood, and arrow keys to jog the machine around and start and stop the run.

You can run it on any computer really, but it can be nice to either leave an old computer hooked up to the machine or have a standalone solution like the Raspberry Pi because then you don't have to take your computer into your work space. 

I'm hoping to do a end to end walk through for the update not this week, but the week after to show every step of the process to go from sketchup to  holding a part. 

Getting more people involved in CNC routing is literally the entire point of the project and your feedback and questions are the key to doing that. I think the two big hurdles to getting people on board are getting the cost down as low as possible, and making the software approachable so if at any point you think something is unclear or could be simpler, please let me know.

---

Posted on **2017-01-07 13:15:08** by **jbarchuk**:

I'm trying to think up how to describe this based on what you know.

The g-code is a plain text file that is a list of position and action commands. You know that.

The behavior (motion and speed) of the head (that holds the router or inkjet or plasma or whatever) is know in a controllable and repeatable manner down to the 0.4mm. That info is know to the CAD software that visually creates your object, -and- the controller board that will tell the motors what to do.

The control board mounted on the machine converts those text commands to the electrical signals that control the motors.

G-code is also in a sense an interpreted language in that the controller is interpreting the commands created by the CAD software, and g-code commands can be sent directly via a PC or another tiny control panel connected to the control board. No the system doesn't have that 'local control' thing right now but let's all lobby for the option. :)

---

