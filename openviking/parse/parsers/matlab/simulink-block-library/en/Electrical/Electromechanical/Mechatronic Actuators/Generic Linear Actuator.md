---
type: simulink-block
title: 'Generic Linear Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'genericlinearactuator'
documentation_source_path: 'ref/genericlinearactuator.html'
language: en
---

# Generic Linear Actuator

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: C
  summary: Case mechanical
  direction: conserving
- name: R
  summary: Plunger mechanical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the actuator positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the actuator negative
terminal.

### **C** — Case mechanical

Mechanical translational conserving port associated with the actuator
case.

### **R** — Plunger mechanical

Mechanical translational conserving port associated with the
plunger.

### **H** — Thermal port thermal

Thermal port.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal port No thermal port (default) | Show thermal port
  group: ''
- name: Speed values
  summary: Speed values [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30] m/s (default)
  group: Electrical Force
- name: Force values
  summary: Force values [4, 3.5, 3, 2.5, 2, 1.5, 1, .5, 0, -.5] N (default)
  group: Electrical Force
- name: Rated voltage
  summary: Rated voltage 12 V (default)
  group: Electrical Force
- name: Motor efficiency (percent)
  summary: Motor efficiency 70 (default)
  group: Electrical Force
- name: Speed at which efficiency is measured
  summary: Speed at which efficiency is measured 20 m/s (default)
  group: Electrical Force
- name: Force-independent electrical losses
  summary: Force-independent electrical losses 2 W (default)
  group: Electrical Force
- name: Simulation mode
  summary: Simulation mode PWM (default) | Averaged
  group: Electrical Force
- name: Plunger mass
  summary: Plunger mass 0.1 kg (default)
  group: Mechanical
- name: Linear damping
  summary: Linear damping 1e-5 N/(m/s) (default)
  group: Mechanical
- name: Resistance temperature coefficient
  summary: Resistance temperature coefficient 3.93e-3 1/K (default)
  group: Temperature Dependence
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Temperature Dependence
- name: Thermal mass
  summary: Thermal mass 100 J/K (default)
  group: Thermal Port
```

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model the effects of losses that convert
power to heat.

### Electrical Force

### **Speed values** — Speed values `[-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]` `m/s` (default)

Specify a vector of speeds, including their units, for your
force-speed data.

### **Force values** — Force values `[4, 3.5, 3, 2.5, 2, 1.5, 1, .5, 0, -.5]` `N` (default)

Specify a vector of forces, including their units, for your
force-speed data.

### **Rated voltage** — Rated voltage `12` `V` (default)

Indicate the voltage for which the device you are modeling is
rated.

### **Motor efficiency (percent)** — Motor efficiency `70` (default)

Efficiency that the block uses to calculate force-dependent electrical
losses.

### **Speed at which efficiency is measured** — Speed at which efficiency is measured `20` `m/s` (default)

Speed that the block uses to calculate force-dependent electrical
losses.

### **Force-independent electrical losses** — Force-independent electrical losses `2` `W` (default)

Fixed electrical loss associated with the actuator when the force is
zero.

### **Simulation mode** — Simulation mode `PWM` (default) | `Averaged`

If you set the **Simulation mode** parameter to
`PWM`, apply a PWM waveform switching
between zero and rated volts to the block electrical terminals. The
current drawn from the electrical supply is equal to the amount required
to deliver the mechanical power and to compensate for electrical losses.
If the applied voltage exceeds the rated voltage, the resultant force
scales proportionately. However, applying anything other than the rated
voltage can provide unrepresentative results.

If you set the **Simulation mode** parameter to
`Averaged`, the force generated in response
to an applied voltage Vav is

VavVrated×F(v)

whereF(v) is the force value at speed v. The current drawn from the supply is such that the
product of the current and Vav is equal to the average power that is consumed.

### Mechanical

### **Plunger mass** — Plunger mass `0.1` `kg` (default)

Mass of the moving part of the motor. The value can be zero.

### **Linear damping** — Linear damping `1e-5` `N/(m/s)` (default)

Linear damping. The value can be zero.

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

Generic linear actuator driven from DC voltage source or PWM driver

The Generic Linear Actuator block implements a model of
a generic linear actuator designed to be driven from a DC voltage source or a PWM
driver. Define force-speed characteristics in terms of tabulated values for powering the
motor at the rated voltage. This functionality enables you to model a motor without
referencing an equivalent circuit.

The motor or actuator architecture determines the way in which electrical losses
depend on force. For example, a DC motor has losses that are proportional to the square
of the current. As force is proportional to current, losses are also proportional to
mechanical force. Most motors have an electrical loss term that is proportional to the
square of mechanical force. The Generic Linear Actuator
block calculates this loss term using the **Motor efficiency
(percent)** and **Speed at which efficiency is measured**
parameters that you provide.

Some motors also have a loss term that is independent of force. An example is a shunt
motor where the field winding draws a constant current regardless of load. The
**Force-independent electrical losses** parameter accounts for this
effect.

The motor efficiency is the mechanical power divided by the sum of the mechanical
power and both electrical loss terms. The block assumes that the speed at which the
motor efficiency is defined is in the motoring quadrant and, therefore, positive.

You can operate the block in the reverse direction by changing the sign of the voltage
applied. The H-Bridge block, for example, reverses motor
direction if the voltage at the REV port is greater than the **Reverse threshold
voltage** parameter. However, if you are using the block in reverse,
specify the force-speed data for forward operation:

- Positive forces and positive speeds in the motoring quadrant.
- Positive force and negative speeds in the generating counterclockwise
  quadrant.
- Negative force and positive speed in the generating clockwise quadrant.

### Model Thermal Effects

You can expose the thermal port to model the effects of losses that convert power to heat.
To expose the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a
  thermal port.
- `Show thermal port` — The block contains one thermal
  conserving port.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.
