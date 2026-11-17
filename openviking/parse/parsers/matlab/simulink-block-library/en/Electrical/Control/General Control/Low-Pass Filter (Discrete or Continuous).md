---
type: simulink-block
title: 'Low-Pass Filter (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'lowpassfilterdiscreteorcontinuous'
documentation_source_path: 'ref/lowpassfilterdiscreteorcontinuous.html'
language: en
---

# Low-Pass Filter (Discrete or Continuous)

## Ports
```yaml
ports:
- name: u
  summary: Filter input vector
  direction: input
  data_types: single | double
- name: y
  summary: Filter output vector
  direction: output
  data_types: single | double
```

### Input

### **u** — Filter input vector

Low-pass filter input signal. The block uses the input initial value
to determine the state initial value.

**Data Types:** `single` | `double`
### Output

### **y** — Filter output vector

Low-pass filter output.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Gain
  summary: Filter gain 1 (default) | positive number
  group: ''
- name: Time constant
  summary: Filter time constant 1 (default) | positive number
  group: ''
- name: Upper saturation limit
  summary: State upper limit inf (default) | real number
  group: ''
- name: Lower saturation limit
  summary: State lower limit -inf (default) | real number
  group: ''
- name: Initialization
  summary: Initial state specification Inherited from block input (default) | Specify as parameter
  group: ''
- name: Initial state
  summary: Initial state 0 (default) | real number
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | 0 | positive scalar
  group: ''
```

### **Gain** — Filter gain `1` (default) | positive number

Low-pass filter gain.

### **Time constant** — Filter time constant `1` (default) | positive number

Low-pass filter time constant. In the discrete implementation, set this
value to less than the **Sample time** to bypass the
dynamics of the filter.

### **Upper saturation limit** — State upper limit `inf` (default) | real number

Low-pass filter upper state limit. Set this to `inf` for
an unsaturated upper limit, or to a finite value to prevent upper windup of
the filter's integrator.

### **Lower saturation limit** — State lower limit `-inf` (default) | real number

Low-pass filter lower state limit. Set this to `-inf` for
an unsaturated lower limit, or to a finite value to prevent lower windup of
the filter's integrator.

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

Discrete-time or continuous-time low-pass filter

The Low-Pass Filter (Discrete or Continuous) block implements a
low-pass filter in conformance with IEEE 421.5-2016[1]. In
the standard, the filter is referred to as a Simple Time Constant.

You can switch between continuous and discrete implementations of the integrator using
the **Sample time** parameter.

### Equations

**Continuous**

To configure the filter for continuous time, set the **Sample
time** property to `0`. This representation is
equivalent to the continuous transfer function:

G(s)=KTs+1,

where:

- *K* is the filter gain.
- *T* is the filter time constant.

From the preceding transfer function, the filter defining
equations are:

{x˙(t)=1T(Ku(t)−x(t))y(t)=x(t)   y(0)=x(0)=Ku0,

where:

- *u* is filter input.
- *x* is filter state.
- *y* is filter output.
- *t* is simulation time.
- *u0* is the initial input to
  the block.

**Discrete**

To configure the filter for discrete time, set the **Sample
time** property to a positive, nonzero value, or to
`-1` to inherit the sample time from an upstream block. The
discrete representation is equivalent to the transfer function:

G(z)=K(Ts/T)z−11+(Ts/T−1)z−1,

where:

- *K* is the filter gain.
- *T* is the filter time constant.
- *Ts* is the filter sample
  time.

From the discrete transfer function, the filter equations are
defined using the forward Euler method:

{x(n+1)=(1−TsT)x(n)+K(TsT)u(n)y(n)=x(n)   y(0)=x(0)=Ku0,

where:

- *u* is the filter input.
- *x* is the filter state.
- *y* is the filter output.
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

The anti-windup method limits the integrator state between the lower saturation
limit *A* and upper saturation limit *B*:

A<=x<=B .

Because the state is limited, the output can respond immediately
to a reversal of the input sign when the integral is saturated. This block diagram
depicts the implementation of the anti-windup saturation method in the filter.

This block does not provide a windup saturation method. To use the windup
saturation method, set the **Upper saturation limit** parameter to
`inf`, the **Lower saturation limit**
parameter to `-inf`, and attach a saturation block
to the output.

### Bypass Filter Dynamics

Set the time constant to a value smaller than or equal to the sample time to
ignore the dynamics of the filter. When bypassed, the block feeds the gain-scaled
input directly to the output:

T≤Ts→y=Ku

In the continuous case, the sample time and time constant must
both be zero.
