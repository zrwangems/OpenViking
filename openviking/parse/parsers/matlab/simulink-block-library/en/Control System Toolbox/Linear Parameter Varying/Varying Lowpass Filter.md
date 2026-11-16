---
type: simulink-block
title: 'Varying Lowpass Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyinglowpassfilter'
documentation_source_path: 'ref/varyinglowpassfilter.html'
language: en
---

# Varying Lowpass Filter

## Ports

### Input

### **u** — Filter input scalar

Lowpass filter input signal.

### **freq** — Cutoff frequency scalar

Filter cutoff frequency, specified in rad/s.
### Output

### **y** — Filter output scalar

Lowpass filter output signal.

## Parameters

### **Filter order** — Lowpass filter order 1 (default) | positive integer

Lowpass filter order, specified as a positive integer.

## Libraries

Control System Toolbox / Linear Parameter Varying

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Butterworth filter with varying coefficients

The block implements an analog Nth-order Butterworth
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
