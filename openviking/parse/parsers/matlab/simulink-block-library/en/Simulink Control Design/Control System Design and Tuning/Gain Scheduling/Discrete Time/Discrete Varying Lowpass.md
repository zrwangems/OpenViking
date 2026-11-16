---
type: simulink-block
title: 'Discrete Varying Lowpass'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Discrete Time'
documentation_page: 'discretevaryinglowpass'
documentation_source_path: '../control/ref/discretevaryinglowpass.html'
language: en
---

# Discrete Varying Lowpass

## Ports

### Input

### **u** — Filter input scalar

Lowpass filter input signal.

### **freq** — Cutoff frequency scalar

Continuous-time value of the cutoff frequency, specified in
rad/s.
### Output

### **y** — Filter output scalar

Lowpass filter output signal.

## Parameters

### **Filter order** — Lowpass filter order 1 (default) | positive integer

Lowpass filter order, specified as a positive integer.

### **Pre-warping frequency w0 (rad/s)** — Pre-warping frequency 0 (default) | positive scalar

Pre-warping frequency, specified as a positive scalar. Discretization of
the continuous-time Butterworth filter can shift the cutoff frequency when
it is close to the Nyquist frequency. To ensure that the analog and digital
filters have matching frequency response near a particular frequency
`w0`, set this parameter to `w0`. The
default value `w0 = 0` corresponds to the bilinear (Tustin)
transformation without pre-warp:

s=2Ts(z−1z+1),

where *Ts* is the block sample
time, specified with the **Sample time Ts**
parameter.

### **Sample time Ts** — Sample time 1 (default) | positive scalar

Block sample time, specified as a positive scalar. This block does not
support inherited sample time, because it requires a specified sample time
to compute the discretization of the Butterworth filter.

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

Discrete Butterworth filter with varying coefficients

The block implements the Tustin discretization of a continuous-time
Nth-order Butterworth filter. The result is a digital
filter with unit DC gain and varying cutoff frequency that you provide as an input to
the block.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the cutoff frequency depend on the block output
**y**. If you have such dependence, the resulting filter causes
an algebraic loop, because computing the block output value requires knowing the
block output value. This algebraic loop is prone to instability and
divergence.
