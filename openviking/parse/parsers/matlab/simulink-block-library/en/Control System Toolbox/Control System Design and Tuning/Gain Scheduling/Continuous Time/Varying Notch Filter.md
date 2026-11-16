---
type: simulink-block
title: 'Varying Notch Filter'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Continuous Time'
documentation_page: 'varyingnotchfilter'
documentation_source_path: '../control/ref/varyingnotchfilter.html'
language: en
---

# Varying Notch Filter

## Ports

### Input

### **u** — Filter input scalar

Notch filter input signal

### **freq** — Notch frequency scalar

Value of the notch frequency, specified in rad/s.

### **gmin** — Gain at notch frequency scalar

Value of the gain at notch frequency, in absolute units. This value
controls the notch depth. The notch filter has unit gain at low and high
frequency. The gain is lowest at the notch frequency, the value at the
**freq** port.

### **damp** — Damping ratio of the filter poles scalar

Value of the damping ratio, specified as a positive scalar value. The
damping ratio controls the notch width; the closer to 0, the steeper the
notch.
### Output

### **y** — Filter output scalar

Notch filter output signal.

## Parameters

Not documented in R2025b.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Notch filter with varying coefficients

The block implements a continuous-time notch filter with varying coefficients. The
instantaneous transfer function of the filter is given by:

N(s)=s2+2\*gmin\*damp\*freq\*s+freq2s2+2\*damp\*freq\*s+freq2,

where *gmin*, *damp*, and *freq*
are the values supplied at the corresponding input ports. These parameters control the
notch depth and frequency as shown in the following illustration. The damping ratio
*damp* controls the notch width *Δ*; larger
*damp* means larger *Δ*.

Use this block and the
other blocks in the Linear Parameter Varying library to implement common control elements with
variable parameters or coefficients. For more information, see Model Gain-Scheduled Control Systems in Simulink.

**Caution**

Avoid making the filter coefficients depend on the block output
**y**. If you have such dependence, the resulting filter causes
an algebraic loop, because computing the block output value requires knowing the
block output value. This algebraic loop is prone to instability and
divergence.
