---
type: simulink-block
title: 'Discrete Varying Notch'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingnotch'
documentation_source_path: 'ref/discretevaryingnotch.html'
language: en
---

# Discrete Varying Notch

## Ports
```yaml
ports:
- name: u
  summary: Filter input scalar
  direction: input
- name: freq
  summary: Notch frequency scalar
  direction: input
- name: gmin
  summary: Gain at notch frequency scalar
  direction: input
- name: damp
  summary: Damping ratio of the filter poles scalar
  direction: input
- name: y
  summary: Filter output scalar
  direction: output
```

### Input

### **u** — Filter input scalar

Notch filter input signal

### **freq** — Notch frequency scalar

Continuous-time value of the notch frequency, specified in
rad/s.

### **gmin** — Gain at notch frequency scalar

Continuous-time value of the gain at notch frequency, in absolute
units. This value controls the notch depth. The notch filter has unit
gain at low and high frequency. The gain is lowest at the notch
frequency.

### **damp** — Damping ratio of the filter poles scalar

Continuous-time value of the damping ratio, specified as a positive
scalar value. The damping ratio controls the notch width; the closer to
0, the steeper the notch.
### Output

### **y** — Filter output scalar

Notch filter output signal.
## Parameters
```yaml
parameters:
- name: Pre-warping frequency w0 (rad/s)
  summary: Pre-warping frequency 0 (default) | positive scalar
  group: ''
- name: Sample time Ts
  summary: Sample time 1 (default) | positive scalar
  group: ''
```

### **Pre-warping frequency w0 (rad/s)** — Pre-warping frequency 0 (default) | positive scalar

Pre-warping frequency, specified as a positive scalar. Discretization of
the continuous-time notch-filter transfer function can shift the notch
frequency when it is close to the Nyquist frequency. To ensure that the
continuous and discrete filters have matching frequency response near a
particular frequency `w0`, set this parameter to
`w0`. The default value `w0 = 0`
corresponds to the bilinear (Tustin) transformation without pre-warp:

s=2Ts(z−1z+1),

where *Ts* is the block sample
time, specified with the **Sample time Ts**
parameter.

### **Sample time Ts** — Sample time 1 (default) | positive scalar

Block sample time, specified as a positive scalar. This block does not
support inherited sample time, because it requires a specified sample time
to compute the discretization of the notch filter.
## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time notch filter with varying coefficients

The block implements the Tustin discretization of a continuous-time notch filter with
varying coefficients. Feed the continuous-time values of the notch frequency, minimum
gain, and damping ratio to the **freq**, **gmin**, and
**damp** input ports, respectively. These parameters control the
notch depth and frequency of the continuous-time notch frequency as shown in the
following illustration. The damping ratio **damp** controls the notch
width *Δ*; larger **damp** means larger
*Δ*.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the filter coefficients depend on the block output
**y**. If you have such dependence, the resulting filter causes
an algebraic loop, because computing the block output value requires knowing the
block output value. This algebraic loop is prone to instability and
divergence.
