---
type: simulink-block
title: 'Generic Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechatronic Actuators\u200b'
documentation_page: 'genericrotaryactuator'
documentation_source_path: 'ref/genericrotaryactuator.html'
language: en
---

# Generic Rotary Actuator

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the actuator positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the actuator negative
terminal.

### **C** — Case mechanical

Mechanical rotational conserving port associated with the actuator
case.

### **R** — Rotor mechanical

Mechanical rotational conserving port associated with the
rotor.

### **H** — Thermal port thermal

Thermal port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of losses that convert
power to heat.

### Electrical Torque

### **Speed values** — Vector of speeds `[-1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000]` `rpm` (default)

Specify a vector of speeds, including their units, for your
torque-speed data.

### **Torque values** — Vector of torques `[.04, .035, .03, .025, .02, .015, .01, .005, 0, -.005]` `Nm` (default)

Specify a vector of torques, including their units, for your
torque-speed data.

### **Rated voltage** — Rated voltage `12` `V` (default)

Indicate the voltage for which the device you are modeling is
rated.

### **Motor efficiency (percent)** — Motor efficiency `80` (default)

The efficiency that the block uses to calculate torque-dependent
electrical losses.

### **Speed at which efficiency is measured** — Speed at which efficiency is measured `2000` `rpm` (default)

The speed that the block uses to calculate torque-dependent electrical
losses.

### **Torque-independent electrical losses** — Fixed electrical loss `0.1` `W` (default)

Fixed electrical loss associated with the actuator when the torque is
zero.

### **Simulation mode** — Simulation mode `PWM` (default) | `Averaged`

If you set the **Simulation mode** parameter to
`PWM`, apply a PWM waveform switching
between zero and rated volts to the block electrical terminals. The
current drawn from the electrical supply is equal to the amount required
to deliver the mechanical power and to compensate for electrical losses.
If the applied voltage exceeds the rated voltage, the resultant torque
scales proportionately. However, applying anything other than the rated
voltage can provide unrepresentative results.

If you set the **Simulation mode** parameter to
`Averaged`, the torque generated in
response to an applied voltage Vav is

VavVrated×T(ω)

where T(ω) is the torque value at speed ω. The current drawn from the supply is such that the
product of the current and Vav is equal to the average power that is consumed.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.0001` `kg*m^2` (default)

Rotor resistance to change in motor motion. The value can be
zero.

### **Rotor damping** — Rotor damping `1e-8` `N*m/(rad/s)` (default)

Rotor damping. The value can be zero.

### Temperature Dependence

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Resistance temperature coefficient.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

The temperature for which the actuator parameters are defined.

### Thermal Port

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Thermal mass** — Thermal mass `100` `J/K` (default)

The thermal mass is the energy required to raise the temperature by
one degree.

## Libraries

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

## Description

Generic rotary actuator driven from DC voltage source or PWM driver

The Generic Rotary Actuator block implements a model of
a generic rotary actuator designed to be driven from a DC voltage source or PWM driver.
You define torque-speed characteristics in terms of tabulated values for powering the
motor at the rated voltage. This functionality allows you to model a motor without
referencing an equivalent circuit.

The motor or actuator architecture determines the way in which electrical losses
depend on torque. For example, a DC motor has losses that are proportional to the square
of the current. As torque is proportional to current, losses are also proportional to
mechanical torque. Most motors have an electrical loss term that is proportional to the
square of mechanical torque. The Generic Rotary Actuator
block calculates this loss term using the **Motor efficiency
(percent)** and **Speed at which efficiency is measured**
parameters that you provide.

Some motors also have a loss term that is independent of torque. An example is a shunt
motor where the field winding draws a constant current regardless of load. The
**Torque-independent electrical losses** parameter accounts for
this effect.

The motor efficiency is the mechanical power divided by the sum of the mechanical
power and both electrical loss terms. The block assumes that the speed at which the
motor efficiency is defined is in the motoring quadrant and, therefore, positive.

You can operate the block in the reverse direction by changing the sign of the voltage
that you apply. The H-Bridge block, for example, reverses motor direction
if the voltage at the REV port is greater than the **Reverse threshold
voltage** parameter. However, if you are using the block in reverse,
specify the torque-speed data for forward operation:

- Positive torques and positive speeds in the motoring quadrant.
- Positive torque and negative speeds in the generating counterclockwise
  quadrant.
- Negative torque and positive speed in the generating clockwise
  quadrant.

### Model Thermal Effects

You can expose the thermal port to model the effects of losses that convert power to heat.
To expose the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a
  thermal port.
- `Show thermal port` — The block contains one thermal
  conserving port.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
