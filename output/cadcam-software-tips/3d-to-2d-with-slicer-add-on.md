## 3d to 2d with slicer add-on
Posted on *2017-03-31 23:06:55* by *mikeberg*

i have a good solution for using fusion 360 for making 3d parts first you will be need slicer its an add on that you  can simply downloaded on fusion 360 store . you need one model you did . when you have opened slicer app just one click on your model and slicer make a huge job to calculate each layers you needed for making your model it entirely parametric!
okay lets say you having a sheet of plywood of half an inchs for making  your project entirely....no problem it think about respecting all dimension if you want! many feature of assembling . ok lets say you want to make it with stacking option it calculate each sheet to shape an object in 3d to 2d . nope its not finish ! all that layers is drawed on each sheet of plywood, it can be export in  dxf file or 
svg i know some people have talked of this earlier but i want to show how its powerful like  software        [123Dmake_2](//muut.com/u/maslowcnc/s3/:maslowcnc:ynpy:123dmake_2.png.jpg)

---

Posted on *2017-04-01 02:19:23* by *davidlang*

when 3d printing something you talk about a slicer, because the model needs to be sliced into layers that are printed one at a time. Each layer is completed before the next layer is started.

in the CAD world you talk about the toolpath generator, not a slicer. You want to do as much work as possible with one tool before you change to a different tool. It is working to optimize time (and tool changes take a long time). This may involve doing a lot of work at different depths in one area before moving on to another area.

I've seen videos for fusion360, and it has lots of neat tools for taking a 3d model and approximating it for manufacture. slicing it into layers and then carving each layer is one approach, another one will create a grid of interlocking pieces to approximate the shape, etc.

---

