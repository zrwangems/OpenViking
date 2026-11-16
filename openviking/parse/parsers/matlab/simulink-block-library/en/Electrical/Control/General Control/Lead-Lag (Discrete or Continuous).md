---
type: simulink-block
title: 'Lead-Lag (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'leadlagdiscreteorcontinuous'
documentation_source_path: 'ref/leadlagdiscreteorcontinuous.html'
language: en
---

# Lead-Lag (Discrete or Continuous)

## Ports

### Input

### **u** — Compensator input vector

Lead-lag compensator input signal. The block uses the input initial
value to determine the state initial value.

**Data Types:** `single` | `double`
### Output

### **y** — Compensator output vector

Lead-lag compensator output.

**Data Types:** `single` | `double`

## Parameters

### **Lead time constant, T1** — Lead time constant `0.2` (default) | positive number

Compensator lead time constant. To bypass the dynamics of the compensator.
set this value to `0` or to the value of the **Lag
time constant, T2** parameter.

### **Lag time constant, T2** — Lag time constant `0.1` (default) | positive number

Compensator lag time constant. To bypass the dynamics of the compensator.
set this value to `0` or to the value of the **Lead
time constant, T1** parameter.

### **Upper saturation limit** — State upper limit `inf` (default) | real number

Compensator upper state limit. Set this to `inf` for an
unsaturated upper limit, or to a finite value to prevent upper windup of the
system's integrator.

### **Lower saturation limit** — State lower limit `-inf` (default) | real number

Compensator lower state limit. Set this to `-inf` for an
unsaturated lower limit, or to a finite value to prevent lower windup of the
system's integrator.

### **Initialization** — Initial state specification `Inherited from block input` (default) | `Specify as parameter`

Specify the initial state condition for this block. For more information,
see Initial Conditions.

### **Initial state** — Initial state `0` (default) | real number

Block initial state.

#### Dependencies

To enable this parameter, set **Initialization** to
`Specify as parameter`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time or continuous-time lead-lag compensator

The Lead-Lag (Discrete or Continuous) block implements a lead-lag
compensator in conformance with IEEE 421.5-2016[1].

You can switch between continuous and discrete implementations of the block using the
**Sample time** parameter.

### Equations

**Continuous**

To configure the compensator for continuous time, set the **Sample
time** property to `0`. This representation is
equivalent to the continuous transfer function:

G(s)=T1s+1T2s+1,

where:

- *T1* is the lead time
  constant.
- *T2* is the lag time
  constant.

From the preceding transfer function, the compensator defining
equations are:

{x˙(t)=1T2(u(t)−x(t))y(t)=T1T2u(t)+(1−T1T2)x(t)   y(0)=x(0)=u0,

where:

- *u* is the block input.
- *x* is the block state.
- *y* is the block output.
- *t* is the simulation time.
- *u0* is the initial input to
  the block.

**Discrete**

To configure the compensator for discrete time, set the **Sample
time** property to a positive, nonzero value, or to
`-1` to inherit the sample time from an upstream block. The
discrete representation is equivalent to the transfer function:

T1z+(Ts−T1)T2z+(Ts−T2),

where:

- *T1* is the lead time
  constant.
- *T2* is the lag time
  constant.
- *Ts* is the compensator
  sample time.

From the discrete transfer function, the compensator equations
are defined using the forward Euler method:

{x(n+1)=(1−TsT2)x(n)+(TsT2)u(n)y(n)=(1−T1T2)x(n)+(T1T2)u(n)   y(0)=x(0)=u0,

where:

- *u* is the block input.
- *x* is the state.
- *y* is the block output.
- *n* is the simulation time step.
- *u0* is the initial input to
  the block.

### Initial Conditions

To specify the initial conditions of this block, set
**Initialization** to:

- `Inherited from block input` — The block sets
  the state and output initial conditions to the initial input.
- `Specify as parameter` — The block sets the
  state initial condition to the value of **Initial
  state**.

### Limiting the Integral

Set the **Upper saturation limit** and **Lower saturation
limit** parameters to use the anti-windup saturation method.

The anti-windup method limits the compensator state between the lower saturation
limit *A* and upper saturation limit *B*:

A<=x<=B .

Because the state is limited, the output can respond immediately
to a reversal of the input sign when the integral is saturated.

This block does not provide a windup saturation method. To use the windup
saturation method, set the **Upper saturation limit** parameter to
`inf`, the **Lower saturation limit**
parameter to `-inf`, and attach a Saturation block
to the output.

### Bypass Compensator Dynamics

Set the lag time constant to zero or to a value equal to that of the lead time
constant to ignore the dynamics of the compensator. When bypassed, the block feeds
the input directly to the output:

T1=0T2=0T1=T2}  y=u .

In the continuous case, both the sample time and at least one
time constant must be zero.
