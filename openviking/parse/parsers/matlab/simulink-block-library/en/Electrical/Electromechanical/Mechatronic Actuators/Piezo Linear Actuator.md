---
type: simulink-block
title: 'Piezo Linear Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'piezolinearactuator'
documentation_source_path: 'ref/piezolinearactuator.html'
language: en
---

# Piezo Linear Actuator

## Ports

### Input

### **f** — Motor driving frequency physical

Physical signal input port associated with the motor driving
frequency, in Hz.

### **v** — RMS supply voltage and direction of rotation physical

Physical signal input magnitude port specifying the RMS supply
voltage, and sign specifying the direction of rotation. If
`v` is positive, then a positive force acts from
port **C** to port **R**.
### Output

### **i** — RMS phase current physical

Physical signal output port associated with the RMS phase
current.

### **vel** — Rotor speed physical

Physical signal output port associated with the linear speed of the
rotor.
### Conserving

### **C** — Case mechanical

Mechanical translational conserving port associated with the motor
case.

### **R** — Rotor mechanical

Mechanical translational conserving port associated with the motor
rotor.

## Parameters

### Electrical Force

### **Motor natural frequency** — Motor natural frequency `92` `kHz` (default)

Frequency at which the piezoelectric crystal naturally resonates. For
most applications, set the input signal at port `f` to
this frequency. To slow down the motor, for example in a closed-loop
speed control, use a frequency slightly less than the motor natural
frequency.

### **Rated RMS voltage** — Rated RMS voltage `5.7` `V` (default)

Voltage at which the motor is designed to operate.

### **Rated force** — Rated force `0.1` `N` (default)

Force the motor delivers at the rated RMS voltage.

### **Rated speed** — Rated speed `50` `mm/s` (default)

Motor speed when the motor drives a load at the rated force.

### **No-load maximum speed** — No-load maximum speed `150` `mm/s` (default)

Motor speed when driving no load and powered at the rated voltage and
driving frequency.

### **Maximum (stall) force** — Maximum force `0.15` `N` (default)

Maximum force the motor delivers when actively driving a load and
powered at the rated voltage and frequency.

**Note**

The **Holding force** parameter value, the load
force the motor holds when stationary, may be greater than the
**Maximum (stall) force** parameter
value.

### **Resonance quality factor** — Resonance quality factor `100` (default)

Quality factor *Q* that specifies how force varies as
a function of driving frequency. Increasing the quality factor results
in a much more rapid decrease in force as driving frequency is moved
away from the natural frequency.

### **Capacitance per phase** — Capacitance per phase `5` `nF` (default)

Electrical capacitance associated with each of the two motor
phases.

### Mechanical

### **Plunger mass** — Plunger mass `0.3` `g` (default)

Mass of the moving part of the motor.

### Motor-Off Friction

### **Holding force** — Holding force `0.3` `N` (default)

The sum of the Coulomb and the static frictions. It must be greater
than or equal to the **Coulomb friction force**
parameter value.

### **Coulomb friction force** — Coulomb friction force `0.15` `N` (default)

The friction that opposes rotation with a constant force at any
velocity.

### **Viscous friction coefficient** — Viscous friction coefficient `1e-5` `s*N/mm` (default) | nonnegative scalar

Proportionality coefficient between the friction force and the
relative velocity.

### **Transition approximation coefficient** — Transition approximation coefficient `0.1` `s/mm` (default)

The parameter sets the coefficient value that is
used to approximate the transition between the
static and the Coulomb frictions. For detailed
information about the coefficient,
*cv*,
see the Simscape
Translational Friction block reference
page.

### **Linear region velocity threshold** — Linear region velocity threshold `0.1` `mm/s` (default)

The parameter sets the small vicinity near zero velocity, within which
friction force is considered to be linearly proportional to the relative
velocity. MathWorks recommends that you use values between
`1e-6` and `1e-4` mm/s.

## Libraries

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Force-speed characteristics of linear piezoelectric traveling wave motor

The Piezo Linear Actuator block represents the
force-speed characteristics of a linear piezoelectric traveling wave motor. The block
represents the force-speed relationship of the motor at a level that is suitable for
system-level modeling. To simulate the motor, the block uses the following models:

- Mass and Friction Model for Unpowered Motor
- Resonant Circuit Model for Powered Motor

### Mass and Friction Model for Unpowered Motor

The motor is unpowered when the physical signal input *v* is
zero. This corresponds to applying zero RMS volts to the motor. In this scenario,
the block models the motor using the following elements:

- A mass whose value is the **Plunger mass** parameter
  value.
- A friction whose characteristics you specify using the parameter
  values in the **Motor-Off Friction** tab.

  The block uses a Simscape™
  Translational Friction block to model the
  friction component. For detailed information about the friction model,
  see the Translational
  Friction block reference page.

### Resonant Circuit Model for Powered Motor

When the motor is active, Piezo Linear Actuator
block represents the motor characteristics using the following equivalent circuit
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
- The force constant *kf*
  relates the RMS current *i* to the resulting mechanical
  force.
- The quadratic mechanical damping term, λx˙2, shapes the force-speed curve predominantly at speeds
  close to maximum RPM. x˙ is the linear speed.
- The term Mx˙ represents the plunger inertia.

At model initialization, the block calculates the model parameters
*R*, *L*, *C*,
*kt* and *λ* to
ensure that the steady-state force-speed curve matches the values for the following
user-specified parameters:

- **Rated force**
- **Rated speed**
- **No-load maximum speed**
- **Maximum (stall) force**

These parameter values are defined for the **Rated RMS
voltage** and **Motor natural frequency** (or rated
frequency) parameter values.

The quadratic mechanical damping term produces a quadratic force-speed curve.
Piezoelectric motors force-speed curves can typically be approximated more
accurately using a quadratic function than a linear one because the force-speed
gradient becomes steeper as the motor approaches the maximum speed.

If the plunger mass *M* is not specified on the datasheet, you
can select a value that provides a good match to the quoted response time. The
response time is often defined as the time for the rotor to reach maximum speed when
starting from rest, under no-load conditions.

The quality factor that you specify using the **Resonance quality
factor** parameter relates to the equivalent circuit model parameters
as follows:

Q=1RLC

This term is not usually provided on a datasheet. You can
calculate its value by matching the sensitivity of force to driving
frequency.

To reverse the motor direction of operation, make the physical signal input
*v* negative.
