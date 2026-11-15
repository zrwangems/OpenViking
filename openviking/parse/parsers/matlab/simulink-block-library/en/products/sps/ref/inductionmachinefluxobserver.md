---
type: simulink-block
title: 'Induction Machine Flux Observer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Observers\u200b'
documentation_page: 'inductionmachinefluxobserver'
documentation_source_path: 'ref/inductionmachinefluxobserver.html'
language: en
---

# Induction Machine Flux Observer

## Ports

### Input

### **iabc** — Current vector

Measured stator currents in the per-unit system.

**Data Types:** `single` | `double`

### **wr** — Speed scalar

Measured rotational speed.

**Data Types:** `single` | `double`
### Output

### **idqseF** — Current vector

Filtered *d*-axis and *q*-axis
stator currents in the synchronous reference frame.

**Data Types:** `single` | `double`

### **imr** — Current scalar

Magnetizing rotor current.

**Data Types:** `single` | `double`

### **theta** — Electrical angle scalar

Rotor electrical angle.

**Data Types:** `single` | `double`

### **we** — Synchronous speed scalar

Rotor synchronous speed.

**Data Types:** `single` | `double`

## Parameters

### **Rated electrical frequency (Hz)** — Frequency `60` (default) | positive

Machine rated electrical frequency.

### **Rotor resistance, referred to the stator side (pu)** — Resistance `0.01` (default) | positive

Rotor resistance, referred to the stator side, in the per-unit
system.

### **Rotor leakage inductance, referred to the stator side (pu)** — Inductance `0.06` (default) | positive

Rotor leakage inductance, referred to the stator side, in the per-unit
system.

### **Magnetizing inductance (pu)** — Inductance `2.7` (default) | positive

Magnetizing inductance in the per-unit system.

### **Time constant for dq currents filters (s)** — Time constant `1e-4` (default) | `0` or positive

Time constant used to low-pass filter the
*d*-*q* currents.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / Observers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Induction machine flux observer for field-oriented control

The Induction Machine Flux Observer block obtains the synchronous
speed, *ωe*, and electrical angle,
*θe*, that are required for performing
rotor field-oriented control (FOC). The figure shows the equivalent circuit for the observer.

### Equations

To determine the synchronous speed and electrical angle, the Induction
Machine Flux Observer block uses these relationships:

λdr'e=Lr'idr'e+LMidse≜LMimr,

0=Rr'idr'e−(ωe−ωr)λqr'e+dλdr'edt,

and

iqr'e=−LMLr'iqse,

in these combined forms:

idr'e=LMLr'(imr−idse)

dimrdt=Rr'Lr'(idse−imr)

and

ωe=ωr+Rr'Lr'iqseimr

where:

- λdr'e is the *d*-axis rotor flux.
- imr is the magnetizing current.
- idse and iqse are the *d*-axis and
  *q*-axis stator currents.
- idr'e and iqr'e are the *d*-axis and
  *q*-axis rotor currents.
- ωe is the synchronous speed.
- ωr is the mechanical rotational speed.
- Rr' is the rotor resistance, referred to the stator
  side.
- Lr' is the rotor leakage inductance, referred to the
  stator side.
- LM the magnetizing inductance.
