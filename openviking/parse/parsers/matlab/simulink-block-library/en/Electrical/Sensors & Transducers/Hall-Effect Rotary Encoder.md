---
type: simulink-block
title: 'Hall-Effect Rotary Encoder'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'halleffectrotaryencoder'
documentation_source_path: 'ref/halleffectrotaryencoder.html'
language: en
---

# Hall-Effect Rotary Encoder

## Ports

### Output

### **Angle** — Rotational angle physical signal

Physical signal output port for the decoded position in terms of the
rotational angle of the magnetic field in the x-y plane.

#### Dependencies

To enable this port, set the **Output interface**
parameter to `Decoded angular
position`.
### Conserving

### **R** — Rotational velocity for the sensor positive probe mechanical rotational

Mechanical rotational conserving port associated with the sensor
positive probe.

### **C** — Rotational velocity for the sensor negative probe mechanical rotational

Mechanical rotational conserving port associated with the sensor
negative (reference) probe.

### **yp** — y-axis positive Hall field electrical

Electrical conserving port associated with the y-axis positive Hall
field.

#### Dependencies

To enable this port, set the **Output interface** parameter to
`Electrical connections`.

### **yn** — y-axis negative Hall field electrical

Electrical conserving port associated with the y-axis negative Hall
field.

#### Dependencies

To enable this port, set the **Output interface**
parameter to `Electrical
connections`.

### **xp** — x-axis positive Hall field electrical

Electrical conserving port associated with the x-axis positive Hall
field.

#### Dependencies

To enable this port, set the **Output interface**
parameter to `Electrical
connections`.

### **xn** — x-axis negative Hall field electrical

Electrical conserving port associated with the x-axis negative Hall
field.

#### Dependencies

To enable this port, set the **Output interface**
parameter to `Electrical
connections`.

## Parameters

### **X-axis voltage amplitude** — x-axis voltage `2.5` `V` (default)

X-axis voltage amplitude, in volts.

### **Y-axis voltage amplitude** — y-axis voltage `2.5` `V` (default)

Y-axis voltage amplitude, in volts.

### **X-axis voltage offset** — x-axis voltage offset `0` `V` (default)

Potential difference in the electric current flow through the electric conductor in the
absence of external magnetic field on the x-axis, in volts.

### **Y-axis voltage offset** — Y-axis voltage offset `0` `V` (default)

Potential difference in the electric current flow through the electric conductor in the
absence of external magnetic field on the y-axis, in volts.

### **Quadrature error** — Quadrature error `0` `deg` (default)

Amount of quadrature error. Quadrature switching can decrease offset
errors.

### **Output interface** — Interface for decoded information `Electrical connections` (default) | `Decoded angular position`

Port interface for decoded information.

Set this parameter to `Electrical connections` to
output the Hall voltages at each sensor. Choosing this option enables the
**yp**, **yn**,
**xp**, and **xn** conserving
ports.

Set this parameter to `Decoded angular position`
to output the rotational angle of the magnetic field in the x-y plane.
Choosing this option enables the **Angle** physical signal
port.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Four-element Hall-effect rotary encoder

The Hall-Effect Rotary Encoder block models a 360° rotary
position sensor using four equally spaced Hall elements under a magnetized, rotating
magnet. The elements generate four sinusoidal waveforms.

This figure shows a schematic of the encoder. The hall elements,
*y*p,
*y*n,
*x*p, and
*x*n, remain in a fixed position while the
north and south poles of the magnet rotate at the angle *θ*.

### Equations

These equations describe the voltages between the elements of the rotary encoder:

vx=Vx0+Axcos(θ)

vy=Vy0+Aycos(θ−π2+β),

where:

- *vx* is the voltage between
  elements *xp* and
  *xn*;
- *vy* is the voltage between
  elements *yp* and
  *yn*;
- *Ax* and
  *Ay* are the voltage
  amplitudes for the *x* and *y* axes
  that reflect the sensitivity mismatch;
- *Vx0* and
  *Vy0* are the voltage
  offsets for the *x* and *y*
  axes;
- *β* is the quadrature error.

The block uses this equation to decode the angle:

θout=arctan(vyvx).

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
