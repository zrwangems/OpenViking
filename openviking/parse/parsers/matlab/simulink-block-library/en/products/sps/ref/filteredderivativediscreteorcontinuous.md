---
type: simulink-block
title: 'Filtered Derivative (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'filteredderivativediscreteorcontinuous'
documentation_source_path: 'ref/filteredderivativediscreteorcontinuous.html'
language: en
---

# Filtered Derivative (Discrete or Continuous)

## Ports

### Input

### **u** — Derivative input vector

Filtered derivative input signal. The block uses the input initial
value to determine the state initial value.

**Data Types:** `single` | `double`
### Output

### **y** — Derivative output vector

Filtered derivative output signal.

**Data Types:** `single` | `double`

## Parameters

### **Gain** — Derivative gain `1` (default) | positive number

Filtered derivative gain.

### **Time constant** — Derivative time constant `0.1` (default) | positive number

Filtered derivative time constant. For acceptable accuracy, set this value
at least 10 times greater than the **Sample time**.

### **Upper saturation limit** — Output upper limit `inf` (default) | real number

Filtered derivative upper output limit. Set this to `inf`
for an unsaturated upper limit.

### **Lower saturation limit** — Output lower limit `-inf` (default) | real number

Filtered derivative lower output limit. Set this to
`-inf` for an unsaturated lower limit.

### **Minimum sample time to time constant ratio** — Discrete ratio `10` (default) | real number

Minimum acceptable sample time to time constant ratio. As the sample time
approaches the time constant, the accuracy of the block decreases. Use this
parameter to set the tolerance of this ratio.

### **Initialization** — Initial state specification `Inherited from block input` (default) | `Specify as parameter`

Specify the initial state condition for this block. For more information,
see Initial Conditions.

### **Initial state** — Initial state `0` (default) | real number

Block initial state.

#### Dependencies

To enable this parameter, set **Initialization** to
`Specify as parameter`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive number

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify `-1`. For
discrete-time operation, specify a positive integer. For continuous-time
operation, specify `0`.

For acceptable accuracy, set this value at least 10 times smaller than the
**Time constant** parameter.

If this block is in a masked subsystem, or other variant subsystem that
allows either continuous and discrete operation, promote the sample time
parameter. Promoting the sample time parameter ensures correct switching
between the continuous and discrete implementations of the block. For more
information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Discrete-time or continuous-time filtered derivative

The Filtered Derivative (Discrete or Continuous) block implements a
filtered derivative in conformance with IEEE 421.5-2016[1].

You can switch between continuous and discrete implementations of the derivative using
the **Sample time** parameter.

### Equations

**Continuous**

To configure the filtered derivative for continuous time, set the
**Sample time** property to `0`. This
representation is equivalent to the continuous transfer function:

G(s)=KsTs+1,

where:

- *K* is the gain.
- *T* is the time constant.

From the preceding transfer function, the derivative defining
equations are:

{x˙(t)=1T(Ku(t)−x(t))y(t)=1T(Ku(t)−x(t))   x(0)=u0, y(0)=0,

where:

- *u* is the block input.
- *x* is the state.
- *y* is the block output.
- *t* is the simulation time.
- *u0* is the initial input to
  the block.

**Discrete**

To configure the filtered derivative for discrete time, set the
**Sample time** property to a positive, nonzero value, or
to `-1` to inherit the sample time from an upstream block. The
discrete representation is equivalent to the transfer function:

(KT)z−1z+Ts/T−1,

where:

- *K* is the gain.
- *T* is the time constant.
- *Ts* is the sample
  time.

From the discrete transfer function, the derivative equations are
defined using the forward Euler method:

{x(n+1)=(1−TsT)x(n)+(TsT)u(n)y(n)=KT(u(n)−x(n))   x(0)=u0, y(0)=0,

where:

- *u* is the block input.
- *x* is the block state.
- *y* is the block output.
- *n* is the simulation time step.
- *u0* is the initial input to
  the block.

### Initial Conditions

To specify the initial conditions of this block, set
**Initialization** to:

- `Inherited from block input` — The block sets
  the state initial condition to the initial input, making the initial
  output zero.
- `Specify as parameter` — The block sets the
  state initial condition to the value of **Initial
  state**.

### Limiting the Output

Limit the filtered derivative output by setting the **Upper saturation
limit** and **Lower saturation limit** parameters to
finite values.

Unlike other common blocks given in IEEE 421.5-2016, there is no difference
between the windup and anti-windup saturation methods for the filtered derivative.
The output can respond immediately to a reversal of the input sign when the output
is saturated.
