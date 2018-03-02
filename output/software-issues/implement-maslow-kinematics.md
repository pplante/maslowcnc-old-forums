## implement maslow kinematics in grbl?
Posted on *2017-04-28 22:49:13* by *davidlang*

I went looking to see what is implemented in the grbl firmware https://github.com/gnea/grbl and found that it implements a LOT more gcode features than we do, including some pretty sophisticated velocity planning (taking into account the angle between two line segments to figure out what speed you can have as you approach the turn for example)

It has a very complete engine to decode the g-code and convert it to a series of straight moves with various acceleration profiles ( cruise-only, cruise-deceleration, acceleration-cruise, acceleration-only, deceleration-only, full-trapezoid, and triangle(no cruise)). 

in grbl, it looks like stepper.c has the fucntions that move the steppers based on a series of micro-moves

we would let the rest of the firmware think that it's running stepper motors, but instead of using the steps to move motors directly, they would move the target position (and it already has a target speed). At that point, a couple PIR loops to implement  the maslow mechanics would let us function. It looks like most of the work would end up being in the st_prep_buffer() function (and the exact interfaces that has to the stepper interrupt functions)

---

Posted on *2017-04-28 23:22:51* by *davidlang*

layers of indirection, movement blocks are then broken down to segment blocks for the motor to actually execute. They are executing the motor functions via an ISR(TIMER1_COMPA_vect) call
a segment block is:

---
// Segment preparation data struct. Contains all the necessary information to compute new segments
// based on the current executing planner block.
typedef struct {
  uint8_t st_block_index;  // Index of stepper common data block being prepped
  uint8_t recalculate_flag;

  float dt_remainder;
  float steps_remaining;
  float step_per_mm;
  float req_mm_increment;

  #ifdef PARKING_ENABLE
    uint8_t last_st_block_index;
    float last_steps_remaining;
    float last_step_per_mm;
    float last_dt_remainder;
  #endif 

  uint8_t ramp_type;      // Current segment ramp state
  float mm_complete;      // End of velocity profile from end of current planner block in (mm).
                          // NOTE: This value must coincide with a step(no mantissa) when converted.
  float current_speed;    // Current speed at the end of the segment buffer (mm/min)
  float maximum_speed;    // Maximum speed of executing block. Not always nominal speed. (mm/min)
  float exit_speed;       // Exit speed of executing block (mm/min)
  float accelerate_until; // Acceleration ramp end measured from end of block (mm)
  float decelerate_after; // Deceleration ramp start measured from end of block (mm)

  #ifdef VARIABLE_SPINDLE
    float inv_rate;    // Used by PWM laser mode to speed up segment calculations.
    uint8_t current_spindle_pwm;
  #endif
} st_prep_t;
---

---

