---
type: simulink-block
title: 'Integrator with Wrapped State (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Function Blocks'
documentation_page: 'integratorwithwrappedstatediscreteorcontinuous'
documentation_source_path: 'ref/integratorwithwrappedstatediscreteorcontinuous.html'
language: en
---

# Integrator with Wrapped State (Discrete or Continuous)

## Ports

### Input

### **u** — Integrator input vector

Integrator input.

**Data Types:** `single` | `double`
### Output

### **y** — Integrator output vector

Integrator output.

**Data Types:** `single` | `double`

## Parameters

### **Wrapped state upper limit** — State upper limit `2*pi` (default) | real number

Integrator upper limit.

### **Wrapped state lower limit** — State lower limit `0` (default) | real number

Integrator lower limit.

### **Initial condition** — State initial value `0` (default) | real number

Integrator initial state.

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

Discrete-time or continuous-time integrator with wrapped state

The Integrator with Wrapped State (Discrete or Continuous) block
implements a wrapped state integrator in conformance with IEEE
421.5-2016[1].

Use this block to generate periodic signals such as angles or to represent a
voltage-controlled oscillator. You can switch between continuous and discrete
implementations of the integrator using the **Sample time**
parameter.

### Equations

**Continuous**

To configure the integrator for continuous time, set the **Sample
time** property to `0`. This representation is
equivalent to the continuous transfer function:

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

To configure the integrator for discrete time, set the **Sample
time** property to a positive, nonzero value, or to
`-1` to inherit the sample time from an upstream block. The
discrete representation is equivalent to the transfer function:

G(z)=Tsz−1,

where *Ts* is the
sample time. From the discrete transfer function, the integrator equations are
defined using the forward Euler method:

{x(n+1)=x(n)+Tsu(n)y(n)=x(n)  x(0)=x0,

where:

- *u* is the integrator input.
- *x* is the integrator state.
- *y* is the integrator output.
- *n* is the simulation time step.
- *x0* is the initial state of
  the integrator.

### Defining Initial Conditions

You can define the state initial conditions using **Initial
condition** parameter.

### Wrapping Cyclic States

The integrator wraps its state between the specified lower and upper values. This
diagram shows the outputs of a wrapped and nonwrapped state integrator for a
constant input.

In the diagram, the lower and upper limits are *0*
and *2π*, respectively.
