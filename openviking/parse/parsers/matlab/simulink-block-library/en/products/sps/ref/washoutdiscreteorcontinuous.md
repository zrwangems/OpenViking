---
type: simulink-block
title: 'Washout (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Filters'
documentation_page: 'washoutdiscreteorcontinuous'
documentation_source_path: 'ref/washoutdiscreteorcontinuous.html'
language: en
---

# Washout (Discrete or Continuous)

## Ports

### Input

### **u** — Washout input vector

Washout input signal. The block uses the input initial value to
determine the state initial value.

**Data Types:** `single` | `double`
### Output

### **y** — Washout output vector

Washout output signal.

**Data Types:** `single` | `double`

## Parameters

### **Time constant** — Washout time constant `0.1` (default) | positive number

Washout time constant. Set this value less than the **Sample
time** to bypass the dynamics of the filter.

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

Discrete-time or continuous-time washout or high-pass filter

The Washout (Discrete or Continuous) block implements a washout filter
in conformance with IEEE 421.5-2016[1].
The washout is also known as a high-pass filter.

You can switch between continuous and discrete implementations of the integrator using
the **Sample time** parameter.

### Equations

**Continuous**

To configure the Washout (Discrete or Continuous) block for
continuous time, set the **Sample time** property to
`0`. This representation is equivalent to the continuous
transfer function:

G(s)=TsTs+1,

where *T* is the time constant. From the
preceding transfer function, the washout defining equations are:

{x˙(t)=1T(−x(t)+u(t))y(t)=−x(t)+u(t)  x(0)=u0, y(0)=0,

where:

- *u* is the washout input.
- *x* is the washout state.
- *y* is the washout output.
- *t* is the simulation time.
- *u0* is the initial input to
  the block.

**Discrete**

To configure the washout Washout (Discrete or Continuous) for
discrete time, set the **Sample time** property to a positive,
nonzero value, or to `-1` to inherit the sample time from an
upstream block. The discrete representation is equivalent to the transfer function:

G(z)=z−1z+Ts/T−1,

where *Ts* is the
sample time. From the discrete transfer function, the washout defining equations
are defined using the forward Euler method:

{x(n+1)=(1−TsT)x(n)+(TsT)u(n)y(n)=u(n)−x(n)  x(0)=u0, y(0)=0,

where:

- *u* is the washout input.
- *x* is the washout state.
- *y* is the washout output.
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

### Bypass Filter Dynamics

Set the time constant to a value smaller than or equal to the sample time to
ignore the dynamics of the filter. When bypassed, the block feeds the input directly
to the output:

T≤Ts→y=u .

In the continuous case, the sample time and time constant must
both be zero.
