---
type: simulink-block
title: 'RC Servo'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'rcservo'
documentation_source_path: 'ref/rcservo.html'
language: en
---

# RC Servo

## Ports

### Conserving

### **s** — Shaft control electrical

Electrical conserving port associated with the PWM control signal. The
output shaft angle demand is set by the pulse width of the voltage
applied to this port.

### **+** — Positive terminal electrical

Electrical conserving port associated with the motor positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the motor negative
terminal.

### **R** — Rotor mechanical rotational

Mechanical rotational conserving port associated with the
rotor.

### **C** — Casing mechanical rotational

Mechanical rotational conserving port associated with the stator
(casing).

## Parameters

### Electrical Torque

### **Stall torque** — Maximum load torque `2.4` `kg*cm` (default)

Maximum load torque that the RC servo can move without stalling
(stopping).

### **Time to travel 60 degrees (no load)** — Output shaft 60 degrees turn time `0.28` `s` (default)

Time for the output shaft to turn 60 degrees when the motor is driving
no load.

### **Corresponding nominal voltage** — DC supply voltage `4.8` `V` (default)

DC supply voltage used when measuring stall torque and time to travel
60 degrees.

### **Rotational range** — Output shaft angular range `[0 180]` `deg` (default)

Output shaft angular range of the RC servo.

### **Corresponding pulse widths** — Input pulse widths range `[550 2330]` `us` (default)

Input pulse widths corresponding to the minimum and maximum output
angles, as defined by the **Rotational range**
parameter. Pulse widths outside of this range are clipped by the block
to stay within this range.

### Control

### **Pulse threshold** — Threshold voltage for pulse control `3` `V` (default)

Threshold voltage for pulse control. The input pulse is detected as
high when the voltage between the s and - ports is above this
level.

### **Signal input resistance** — Impedance `18` `kOhm` (default)

Electrical impedance measured between the s and - ports.

### **Angle resolution** — Minimum error allowed between the demanded and measured output shaft angle `0.1` `deg` (default)

Minimum error allowed between the demanded and measured output shaft
angle. When the error between the demanded output shaft angle and
measured output shaft angle drops below the angle resolution, the motor
is powered off. This parameter models the hysteresis usually
incorporated into an RC servo controller to prevent chatter around a set
point.

### **Angle measurement error** — Model error in angle measurement `0` `deg` (default)

Model error in angle measurement. This parameter allows you to model
an angle measurement error, such as can happen due to a failing
potentiometer angle sensor. For example, if you want to model the motor
being powered against one of the hard stops, you can set a suitable
angle measurement error to achieve this.

### Mechanical

### **Backdrive torque (unpowered)** — Load torque required to backdrive unpowered motor `0.5` `kg*cm` (default)

Load torque required to backdrive the motor when it is unpowered. The
block uses this value to determine the gear friction parameters.

### **Gear reduction ratio** — Approximate reduction ratio from motor shaft to RC servo output shaft `320` (default)

Reduction ratio from the DC motor shaft to the RC servo output shaft.
This parameter affects only the impact of rotor inertia on equivalent
inertia value at the output shaft. It has no impact on no-load speed.
Therefore, the value does not have to be precise.

### **Rotor inertia** — Inertia of DC motor and rotor gearing `10` `g*cm^2` (default)

Inertia of the DC motor, plus inertia of the gearing reflected to the
rotor (typically small if the gears are plastic).

### **End-stop angles** — Mechanical angle range `[-5 185]` `deg` (default)

Mechanical end stops prevent rotation of the output shaft beyond the
specified range. The range specified by the end stop angles must be
larger than that specified by the **Rotational range**
parameter.

### **End-stop stiffness** — Stiffness of mechanical end stops `1e6` `N*m/rad` (default)

Stiffness of mechanical end stops.

### **End-stop damping** — Damping of mechanical end stops `0.01` `N*m/(rad/s)` (default)

Damping of mechanical end stops.

### Faults

### **Servo fault** — Option to add fault to RC servo `Add fault` (default)

Option to add a fault to the RC servo.

To add a fault, click the **Add fault**
hyperlink.

### **Failure mode** — Select the type of fault `Fail off` (default) | `Fail forward` | `Fail reverse` | `Failed winding`

Type of fault to model:

- `Fail off` — No electrical
  torque.
- `Fail forward` — Rotates in a
  positive direction to hit the upper end stop.
- `Fail reverse` — Rotates in a
  negative direction to hit the lower end stop.
- `Failed winding` — Torque is
  applied only if the motor rotor lines up with one of the two
  remaining functioning windings.

#### Dependencies

To enable this parameter, add a fault to the RC Servo block by
clicking the **Add fault** hyperlink in the
**Servo fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible current** — Current threshold to fault transition `1` `A` (default) | positive scalar

Current threshold to a fault transition. If the current exceeds this
value for longer than the **Time to fail when exceeding maximum
permissible current** parameter value, then the block
enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding maximum permissible current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Maximum length of time that the current can exceed the maximum
permissible value without triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

## Libraries

Simscape / Electrical / Electromechanical / Brushed Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2023a: Implement temporal or behavioral triggers for faults using a single parameter

The **Enable temporal trigger** and **Enable behavioral trigger** parameters have been removed and are replaced with the **Fault
trigger** parameter. You can set the **Fault trigger**
parameter to `Temporal` or `Behavioral`.
You can enable only one trigger.

If you created a model in an earlier release and enabled both temporal and behavioral
triggers, now only the temporal trigger is enabled. Therefore, the simulation results are
different if the behavioral trigger causes the fault in your model.

If you want to trigger a fault at a specific time, set the **Fault trigger**
parameter to `Temporal`. If you want to determine whether a system
fails and, if so, when it fails, set the **Fault Trigger** parameter to
`Behavioral`.

## Description

Radio control servomotor with PWM-based angular position tracking and fault modeling

The RC Servo block represents a small DC motor with a
gearbox and control circuitry, commonly used in quadcopters, radio-controlled planes and
helicopters, and other mechatronic devices. RC servos provide angular position control
of the output shaft over a limited angle range. The angle demand is set by the pulse
width of a PWM signal applied to port s.

The RC Servo block models the following effects:

- Torque-speed behavior based on DC motor equations
- Position tracking based on the input PWM signal pulse width
- Internal gear reduction ratio, including associated friction losses
- Mechanical end stops, to prevent the output shaft being driven out of range by
  the load
- Position measurement error
- Fault modeling

The motor equations are the same as those used by the DC
Motor block, except that the inductance is not modeled. The
RC Servo block determines the equation parameters
using the stall torque and no-load speeds, and makes a correction to take account of the
backdrive torque.

### Faults

To model a fault in the RC Servo block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The RC Servo block allows you to model several
types of fault:

- Fail off — No electrical torque.
- Fail forward — Rotates in a positive direction to hit the upper end
  stop.
- Fail reverse — Rotates in a negative direction to hit the lower end
  stop.
- Failed winding — Torque is applied only if the motor rotor lines up
  with one of the two remaining functioning windings.

The block can trigger fault events:

- At a specific time.
- When a current limit is exceeded for longer than a specific time
  interval.

If you want to trigger a fault at a specific time, in the
**Fault Inspector** window, set **Trigger type** to
`Timed`. If you want to determine whether a system fails and, if
so, when it fails, in the **Fault Inspector** window, set **Trigger
type** to `Behavioral`.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

### Assumptions and Limitations

- This block has no optional thermal port.
- If you simulate the model with a fixed-step solver, for example, using a
  local solver, the step size must be small enough to get the required
  resolution of the input pulse width. For fast desktop simulation, use this
  block with variable step solvers.
