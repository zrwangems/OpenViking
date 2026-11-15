---
type: simulink-block
title: 'Inductive Rotor Position Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'inductiverotorpositionsensor'
documentation_source_path: 'ref/inductiverotorpositionsensor.html'
language: en
---

# Inductive Rotor Position Sensor

## Ports

### Conserving

### **R** — Rotational velocity for sensor positive probe mechanical rotational

Mechanical rotational conserving port associated with the sensor
positive probe.

### **C** — Rotational velocity for the sensor negative probe mechanical rotational

Mechanical rotational conserving port associated with the sensor
negative (reference) probe.

### **yp** — `y`-axis positive terminal electrical

Electrical conserving port associated with the
`y`-axis positive terminal.

#### Dependencies

To enable this port, set **Output interface** to
`Electrical connections`.

### **yn** — `y`-axis negative terminal electrical

Electrical conserving port associated with the
`y`-axis negative terminal.

#### Dependencies

To enable this port, set **Output interface** to
`Electrical connections`.

### **xp** — x-axis positive terminal electrical

Electrical conserving port associated with the `x`-axis positive
terminal.

#### Dependencies

To enable this port, set **Output interface** to
`Electrical connections`.

### **xn** — x-axis negative terminal electrical

Electrical conserving port associated with the `x`-axis negative
terminal.

#### Dependencies

To enable this port, set **Output interface** to
`Electrical connections`.
### Output

### **Angle** — Rotational angle physical signal

Rotational angle of the magnetic field in the *x*-*y*
plane, returned as a physical signal.

#### Dependencies

To enable this port, set **Output interface** to
`Decoded angular position`.

## Parameters

### **Number of pole pairs** — Number of pole pairs `2` (default) | scalar

Number of pole pairs.

### **X-axis voltage amplitude** — `x`-axis voltage `2.5` `V` (default) | scalar

`x`-axis voltage amplitude.

### **Y-axis voltage amplitude** — `y`-axis voltage `2.5` `V` (default) | scalar

`y`-axis voltage amplitude.

### **X-axis voltage offset** — `x`-axis voltage offset `0` `V` (default) | scalar

Potential difference in the electric current flow through the electric
conductor in the absence of external magnetic field on the
`x`-axis.

### **Y-axis voltage offset** — `y`-axis voltage offset `0` `V` (default) | scalar

Potential difference in the electric current flow through the electric
conductor in the absence of external magnetic field on the
`y`-axis.

### **Quadrature error** — Quadrature error `0` `deg` (default) | scalar

Amount of quadrature error. Quadrature switching can decrease offset
errors.

### **Tumbling coefficient** — Tumbling coefficient `0` (default) | scalar

Tumbling coefficient, in degrees.

### **Output interface** — Interface for decoded information `Electrical connections` (default) | `Decoded angular position`

Port interface for the decoded information, specified as either `Electrical
connections` or `Decoded angular
position`.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Inductive rotor position sensor with four inductive coils

The Inductive Rotor Position Sensor block uses the theory of
eddy current losses to obtain the rotor position. It consists of four planar coils and a
target trace that detect the rotor position. The target trace is shaped in a sinusoidal
way and made from conductive material. The distance between the four planar coils is
equivalent to 90 degrees of one cycle.

### Equations

The voltages between the elements of the sensor are described by the
equations:

vx=Vx0+Axcos(Nθ)+Ksin(θ)

vy=Vy0+Aycos(Nθ−π2+β)+Ksin(θ)

where:

- *vx* is the cosine
  voltage.
- *vy* is the sine
  voltage.
- *Ax* and
  *Ay* are the voltage
  amplitudes for the *x* and *y* axes
  that reflect the sensitivity mismatch.
- *Vx0* and
  *Vy0* are the voltage
  offsets for the *x* and *y*
  axes.
- *N* is the number of pole pairs.
- *θ* is the mechanical position.
- *β* is the quadrature error.
- *K* is the tumbling factor.

The block uses this equation to decode the angle:

θout=arctan(vyvx).

This figure shows the effects of the tumbling factor:

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
