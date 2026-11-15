---
type: simulink-block
title: 'Variable Pulse Generator'
family: discontinuities
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'variablepulsegenerator'
---

# Variable Pulse Generator

Generate ideal, time varying pulse signal

## Libraries

Simulink / Discontinuities

## Description

Use the Variable Pulse Generator block to create ideal modulated pulse
signals.

Generally speaking, the output pulse of the block is described by

y(t)={1tk<t<tk+pw0tk+pw<t<tk+1

where *pw* is the output pulse width.

For an implementation of Pulse Width Modulation, see PWM.

## Ports

### Input

### **D** — Duty Cycle scalar

Desired duty cycle of the pulse *P*, specified as scalar within the range [0,1].

**Data Types:** `double`

### **P** — Period scalar

Time between rising edges of consecutive pulses of the output signal.
A smaller value represents a higher frequency pulse.

**Data Types:** `double`
### Output

### **Port 1** — Modulated pulse signal scalar

Modulated output pulse signal corresponding to input duty
cycle.

**Data Types:** `double`

## Parameters

### **Allow zero pulse width** — Allow zero magnitude of output signal off (default) | on

Enable this parameter to allow the output pulse signal to support pulses
of width 0.

**Note**

Enabling this parameter causes the block to have direct feedthrough.
This can cause algebraic loops in your model.

### **Run at fixed time intervals** — Choose continuous or discrete-time behavior `continuous` (default) | `discrete`

Select whether the block should operate in continuous or discrete sampling modes.

By default, the block uses `continuous` sampling mode as it
improves simulation performance with variable step solvers.

Select `discrete` sampling mode if you need to:

- use a fixed-step solver
- generate code
- sample the block output

### **Sampling rate** — Set pulse resolution 0.1 (default) | scalar

Specify the rate at which the block samples input duty cycle signal. This sampling
rate becomes the resolution of the output pulse signal.

#### Dependencies

This parameter requires that **Sampling mode** is set to
`discrete`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into discrete equivalents that support production code generation. To start the Model Discretizer, in the Simulink® Editor, on the **Apps** tab, under **Apps**, under **Control Systems**, click **Model Discretizer**. One exception is the Second-Order Integrator block because, for this block, the Model Discretizer produces an approximate discretization.

## Version History

**Introduced in R2020b**
