---
type: simulink-block
title: 'Resolver-to-Digital Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Observers\u200b'
documentation_page: 'resolvertodigitalconverter'
documentation_source_path: 'ref/resolvertodigitalconverter.html'
language: en
---

# Resolver-to-Digital Converter

## Ports

### Input

### **Vp** — Voltage phase angle scalar

Simulink signal that corresponds to the voltage phase angle.

**Data Types:** `single` | `double`

### **Vx** — `x`-axis voltage scalar

Simulink signal that corresponds to the `x`-axis
voltage.

**Data Types:** `single` | `double`

### **Vy** — `y`-axis voltage scalar

Simulink signal that corresponds to the `y`-axis
voltage.

**Data Types:** `single` | `double`
### Output

### **Velocity** — Rotational velocity scalar

Simulink signal that corresponds to the rotational velocity.

**Data Types:** `single` | `double`

### **Angle** — Rotational angle scalar

Simulink signal that corresponds to the rotational angle.

**Data Types:** `single` | `double`

## Parameters

### **Number of pole pairs** — Pole pairs in the attached machine `4` (default) | positive scalar integer

Number of pole pairs in the attached machine.

### **Phase-looked loop proportional gain** — PLL proportional gain `15` (default) | positive scalar

Proportional gain for the phase-locked loop filter. This value determines how
aggressively the PLL tracks and locks to the phase angle. Increase this
value to more closely track step changes in the phase angle.

### **Phase-looked loop integral gain** — PLL integral gain `2.5e5` (default) | positive scalar

Integral gain for the phase-locked loop filter. Increase this value to increase the rate
at which steady-state error is eliminated in the phase angle. This value
also determines how aggressively the PLL tracks and locks to the
phase.

### **Initial position (rad)** — Initial phase angle `0` `rad` (default) | scalar

Initial estimate of the phase angle. If the input signal is a vector, use
scalar parameters or use vector parameters that are the same size as the
input signal.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive scalar

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify `-1`. For
discrete-time operation, specify a positive integer. For continuous-time
operation, specify `0`.

**Note**

If this block is in a masked subsystem, or another variant subsystem
that allows you to switch between continuous operation or discrete
operation, promote the sample time parameter to ensure correct switching
between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / Observers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Resolver-to-digital converter

The Resolver-to-Digital Converter block models a transducer
that converts the angular position or velocity of a rotating shaft to an electrical
signal. Resolver-to-digital converters are commonly used in harsh, rugged environments,
such as in fully electric vehicles.

The converted signal is proportional to the sine or cosine of the shaft angle.

A resolver sensor has one rotor winding with the exciter sine wave that is AC-coupled to two
stator windings. The stator windings, a sine coil and a cosine coil, are mechanically
positioned 90-degrees out-of-phase. As the rotor spins, the rotor position angle changes
with respect to the stator windings. The resulting amplitude-modulated signals must then
be gained, demodulated and post processed to extract angle and velocity information
([1] and [2]).

### Equations

The block uses a phase-locked loop (PLL) to extract the angle and the velocity of
the rotating shaft. The error voltage used by the PI controller is obtained as:

Ve=VyVpcos(Nθ)−VxVpsin(Nθ),

where:

- `Vp` is the excitation
  voltage.
- `Vx` is the
  `x` voltage for the secondary winding of the
  resolver.
- `Vy` is the
  `y` voltage for the secondary winding of the
  resolver.
- `N` is the number of pole pairs for the
  resolver.
- `θ` is the angle.

Therefore, the velocity is obtained as:

ω=KpVe+Ki∫Ve,

and the angle is computed from the velocity using:

dθdt=ω.
