---
type: simulink-block
title: 'Piezo Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechatronic Actuators\u200b'
documentation_page: 'piezorotaryactuator'
documentation_source_path: 'ref/piezorotaryactuator.html'
language: en
---

# Piezo Rotary Actuator

## Ports

### Input

### **f** — Motor driving frequency physical

Physical signal input port associated with the motor driving
frequency, in Hz.

### **v** — RMS supply voltage and direction of rotation physical

Physical signal input magnitude port specifying the RMS supply
voltage, and sign specifying the direction of rotation. If
`v` is positive, then a positive torque acts from
port **C** to port **R**.
### Output

### **i** — RMS phase current physical

Physical signal output port associated with the RMS phase
current.

### **wm** — Rotor speed physical

Physical signal output port associated with the rotational speed of
the rotor.
### Conserving

### **C** — Case mechanical

Mechanical translational conserving port associated with the motor
case.

### **R** — Rotor mechanical

Mechanical translational conserving port associated with the motor
rotor.

## Parameters

### Electrical Torque

### **Motor natural frequency** — Motor natural frequency `40` `kHz` (default)

Frequency at which the piezoelectric crystal naturally resonates. For
most applications, set the input signal at port **f**
to this frequency. To slow down the motor, for example in a closed-loop
speed control, use a frequency slightly less than the motor natural
frequency. The default value is
`40``kHz`.

### **Rated RMS voltage** — Rated RMS voltage `130` `V` (default)

Voltage at which the motor is designed to operate.

### **Rated torque** — Rated torque `0.5` `N*m` (default)

Torque the motor delivers at the rated RMS voltage.

### **Rated rotational speed** — Rated rotational speed `100` `rpm` (default)

Motor speed when the motor drives a load at the rated torque.

### **No-load maximum rotational speed** — No-load maximum rotational speed `160` `rpm` (default)

Motor rotational speed when driving no load and powered at the rated
voltage and driving frequency.

### **Maximum torque** — Maximum torque `1` `N*m` (default)

Maximum torque that the motor delivers when actively driving a load
and powered at the rated voltage and frequency. The default value is
`1``N*m`.

**Note**

The **Holding torque** parameter value, the load
torque the motor holds when stationary, may be greater than the
**Maximum torque** parameter value.

### **Resonance quality factor** — Resonance quality factor `100` (default)

Quality factor *Q* that specifies how torque varies
as a function of driving frequency. Increasing the quality factor
results in a much more rapid decrease in torque as driving frequency is
moved away from the natural frequency.

### **Capacitance per phase** — Capacitance per phase `5` `nF` (default)

Electrical capacitance associated with each of the two motor
phases.

### Mechanical

### **Rotor inertia** — Rotor inertia `200` `g*cm^2` (default)

Rotor resistance to change in motor motion.

### Motor-Off Friction

### **Holding torque** — Holding torque `1.5` `N*m` (default)

The sum of the Coulomb and the static frictions. It must be greater
than or equal to the **Coulomb friction torque**
parameter value.

### **Coulomb friction torque** — Coulomb friction torque `1.0` `N*m` (default)

The friction that opposes rotation with a constant torque at any
velocity.

### **Viscous friction coefficient** — Viscous friction coefficient `0.001` `N*m/(rad*s)` (default) | nonnegative scalar

Proportionality coefficient between the friction torque and the
relative angular velocity.

### **Transition approximation coefficient** — Transition approximation coefficient `10` `s/rad` (default)

The parameter sets the coefficient value that is used to approximate
the transition between the static and the Coulomb frictions. For
detailed information about the coefficient,
*cv*, see the
Simscape
Rotational
Friction block reference page.

### **Linear region velocity threshold** — Linear region velocity threshold `1e-4` `rad/s` (default)

The parameter sets the small vicinity near zero velocity, within which
friction torque is considered to be linearly proportional to the
relative velocity. MathWorks® recommends that you use values in the range between
`1e-5` and
`1e-3``rad/s`.

## Libraries

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Torque-speed characteristics of rotary piezoelectric traveling wave motor

The Piezo Rotary Actuator block represents the
torque-speed characteristics of a piezoelectric traveling wave motor. The block
represents the torque-speed relationship of the motor at a level that is suitable for
system-level modeling. To simulate the motor, the block uses the following models:

- Inertia and Friction Model for Unpowered Motor
- Resonant Circuit Model for Powered Motor

### Inertia and Friction Model for Unpowered Motor

The motor is unpowered when the physical signal input *v* is
zero. This corresponds to applying zero RMS volts to the motor. In this scenario,
the block models the motor using the following elements:

- An inertia whose value is the **Rotor inertia**
  parameter value.
- A friction whose characteristics are determined by the parameter
  values in the **Motor-Off Friction** tab.

  The block uses a Simscape™
  Rotational Friction
  block to model the friction component. For detailed
  information about the friction model, see the
  Rotational
  Friction block reference
  page.

### Resonant Circuit Model for Powered Motor

When the motor is active, Piezo Rotary Actuator block represents
the motor characteristics using the following equivalent circuit
model.

In the preceding figure:

- The AC voltage source represents the block's physical signal input of
  frequency *f* and magnitude
  *v*.
- The resistor *R* provides the main electrical and
  mechanical damping term.
- The inductor *L* represents the rotor vibration
  inertia.
- The capacitor *C* represents the piezo crystal
  stiffness.
- The capacitor *Cp*
  represents the phase capacitance. This is the electrical capacitance
  associated with each of the two motor phases.
- The torque constant *kt*
  relates the RMS current *i* to the resulting mechanical
  torque.
- The quadratic mechanical damping term,
  *λωm*2,
  shapes the torque-speed curve predominantly at speeds close to maximum
  RPM. *ωm* is the mechanical
  rotational speed.
- The term Jω˙m represents the rotor inertia.

At model initialization, the block calculates the model parameters
*R*, *L*, *C*,
*kt* and *λ* to
ensure that the steady-state torque-speed curve matches the values of the following
user-specified parameter values:

- **Rated torque**
- **Rated rotational speed**
- **No-load maximum rotational speed**
- **Maximum torque**

These parameter values are defined for the **Rated RMS
voltage** and **Motor natural frequency** (or rated
frequency) parameter values.

The quadratic mechanical damping term produces a quadratic torque-speed curve.
Piezoelectric motors torque-speed curves can typically be approximated more
accurately using a quadratic function than a linear one because the torque-speed
gradient becomes steeper as the motor approaches the maximum speed.

If the rotor inertia *J* is not specified on the datasheet, you
can select a value that provides a good match to the quoted response time. The
response time is often defined as the time for the rotor to reach maximum speed when
starting from rest, under no-load conditions.

The quality factor that you specify using the **Resonance quality
factor** parameter relates to the equivalent circuit model parameters
as follows:

Q=1RLC

This term is not usually provided on a datasheet. You can
calculate its value by matching the sensitivity of torque to driving
frequency.

To reverse the motor direction of operation, make the physical signal input
*v* negative.
