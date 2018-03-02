## Temp frame guide question
Posted on **2017-04-30 10:04:54** by **boandersen**:

In the guide to building temp frame, it says:"Attach the temporary sled to the chains using the large cotter pins. Clicking the 'Home' repeatedly in Ground Control will return the sled to the center of the plywood sheet."

Why repeatedly?

---

Posted on **2017-04-30 10:22:34** by **Bar**:

Great question. 

I actually fixed the issue that was causing this last night, so after today it shouldn't be a thing anymore. Basically when the machine first powered on, it used to know it's chain lengths but it didn't have the math to turn those lengths into a position. Clicking the home button several times gave it time to catch up with where it should be (large error circle shrinking).

Now when the machine powers on it can determine it's position, so clicking home once will make the machine move there in a stately manner.

---

