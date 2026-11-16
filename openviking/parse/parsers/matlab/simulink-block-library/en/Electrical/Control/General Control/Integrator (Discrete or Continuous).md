---
type: simulink-block
title: 'Integrator (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'integratordiscreteorcontinuous'
documentation_source_path: 'ref/integratordiscreteorcontinuous.html'
language: en
---

# Integrator (Discrete or Continuous)

## Ports

### Input

### **u** — Integrator input vector

Integrator input.

**Data Types:** `single` | `double`

### **Reset** — Revert to initial state scalar

Integrator reset. To reset the integrator state to the value of the
**x0** port, pass a nonzero value to this port.
Alternatively, attach a zero-valued Constant block to
this port to override the external reset.

**Data Types:** `single` | `double`

### **x0** — Initial state vector

Integrator initial state. To specify the value of the state after a
reset, pass a signal to this port.

**Data Types:** `single` | `double`
### Output

### **y** — Integrator output vector

Integrator output.

**Data Types:** `single` | `double`

## Parameters

### **Integrator method** — Option to specify integration or accumulation method `Integration: Forward Euler` (default) | `Integration: Backward Euler` | `Integration: Trapezoidal` | `Accumulation: Forward Euler` | `Accumulation: Backward Euler` | `Accumulation: Trapezoidal`

*Since R2025a*

Option to specify the integration or accumulation method. For more
information, see the Integration and Accumulation Methods section of the
Discrete-Time Integrator block.

#### Dependencies

To enable this parameter, set **Sample time (-1 for
inherited)** to `-1` or a positive real
number.

### **External reset** — Reset strategy `level` (default) | `rising` | `falling` | `either`

Select the external reset strategy for the integrator:

- Select `rising` to reset the state
  when the reset signal rises from a negative or zero value to a
  positive value.
- Select `falling` to reset the state
  when the reset signal falls from a positive value to a zero or
  negative value.
- Select `either` to reset the state
  when the reset signal changes from zero to a nonzero value, from
  a nonzero value to zero, or changes sign.
- Select `level` to reset the state
  when the reset signal is nonzero at the current time step or
  changes from nonzero at the previous time step to zero at the
  current time step.

### **Limit type** — Saturation strategy `Anti-windup` (default) | `Windup`

Select the limit type of the integrator:

- Select `Anti-windup` to limit the
  state of the integrator, preventing windup.
- Select `windup` to limit the output
  of the integrator, allowing windup of the integrator
  state.

### **Upper saturation limit** — State upper limit `inf` (default) | real number

Integrator upper saturation limit. Set this to `inf` for
an unsaturated upper limit, or to a finite value to saturate the integrator
using the strategy set by **Limit type**.

### **Lower saturation limit** — State lower limit `-inf` (default) | real number

Integrator lower saturation limit. Set this to `-inf` for
an unsaturated lower limit, or to a finite value to saturate the integrator
using the strategy set by **Limit type**.

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

### R2025a: Specify integration or accumulation method

You can now specify the integration or accumulation method of the block by using
the **Integrator method** parameter. This block can integrate or
accumulate a signal using a forward Euler, backward Euler, or trapezoidal
method.

## Description

Discrete-time or continuous-time integrator

The Integrator (Discrete or Continuous) block implements a simple
integrator in conformance with IEEE 421.5-2016[1].

You can switch between continuous and discrete implementations of the integrator using
the **Sample time (-1 for inherited)** parameter.

### Equations

**Continuous**

To configure the integrator for continuous time, set the **Sample time
(-1 for inherited)** property to `0`. This
representation is equivalent to the continuous transfer function:

G(s)=1s.

From the preceding transfer function, the integrator defining
equations are:

{x˙(t)=u(t)y(t)=x(t)  x(0)=x0,

where:

- *u* is the integrator input.
- *x* is the integrator state.
- *y* is the integrator output.
- *t* is the simulation time.
- *x0* is the initial state of
  the integrator.

**Discrete**

To configure the integrator for discrete time, set the **Sample time
(-1 for inherited)** property to a positive, nonzero value, or to
`-1` to inherit the sample time from an upstream block. The
discrete representation is equivalent to the transfer function:

G(z)=Tsz−1,

where *Ts* is the
sample time.

This block can integrate or accumulate a signal
using a forward Euler, backward Euler, or trapezoidal method. To specify the
integration or accumulation method of the block, use the
**Integrator method** parameter. *(since R2025a)* If you set
the **Integrator method** parameter to
`Integration: Forward Euler`, the block defines the
integrator equations using the forward Euler method from the discrete transfer function:

{x(n+1)=x(n)+Tsu(n)y(n)=x(n)  x(0)=x0,

where:

- *u* is the integrator input.
- *x* is the integrator state.
- *y* is the integrator output.
- *n* is the simulation time step.
- *x0* is the initial state of
  the integrator.

### Defining Initial Conditions

You can define the state initial conditions using the input port
**x0**. The integrator state reverts to the initial condition
any time it is reset.

### Limiting the Integral

You can limit the integral output using one of two methods:

- Set **Limit type** to
  `Anti-windup` to use the anti-windup
  saturation method.

  The anti-windup method limits the integrator state
  *x* between the lower saturation limit
  *A* and upper saturation limit *B*:

  A<=x<=B .

  Because the state is limited, the output can respond
  immediately to a reversal of the input sign when the integral is
  saturated.
- Set **Limit type** to
  `Windup` to use the windup saturation
  method.

  The windup method limits the integrator output *y*
  between the lower saturation limit *A* and upper
  saturation limit *B*:

  A<=y<=B .

  Because the output is limited, the state can continue
  to grow when the integrator is saturated. As a result, the output cannot
  respond to a reversal of the input sign until the state has reached the
  limiting saturation point.

### Resetting the State

You can reset the state of the integrator by passing a nonzero signal to the
**Reset** port of the block.
