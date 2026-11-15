---
type: simulink-block
title: 'Current Limiter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'currentlimiter'
documentation_source_path: 'ref/currentlimiter.html'
language: en
---

# Current Limiter

## Ports

### Input

### **Lim** — Variable current limit, A physical signal

*Since R2024a*

Input physical signal that defines the current limit, in amps.

#### Dependencies

To enable this port, set **Limiter type** to
`Variable limit`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative
terminal.

### **H** — Thermal port thermal

Thermal conserving port associated with the thermal mass.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal port `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal port of the block and model thermal parameters.

### Parameters

### **Limiter type** — Limiter type `Constant symmetric limits` (default) | `Constant asymmetric limits` | `Variable limit`

*Since R2024a*

Limiter type. Choose one of these options:

- `Constant symmetric limits` —
  Set a constant magnitude for the current limit.
- `Constant asymmetric limits` —
  Set one limit for positive currents and one limit for
  negative currents.
- `Variable limit` — Specify the
  magnitude of the current limit using an input physical
  signal. Use this option to define a current limit that
  changes over time.

### **Current limit** — Positive current limit `1` `A` (default) | positive scalar

Current limit in the direction of forward current.

If you set the **Limiter type** to
`Constant asymmetric limits`, the block
assumes that the current limit for negative currents is equal to the
limit for positive currents.

#### Dependencies

To enable this parameter, set **Limiter type** to
`Constant symmetric limits` or
`Constant asymmetric limits`.

### **Reverse direction current limit** — Negative current limit `1` `A` (default) | positive scalar

*Since R2024a*

Current limit in the direction of reverse current.

#### Dependencies

To enable this parameter, set **Limiter type** to
or `Constant asymmetric limits`.

### **Voltage drop when current starts to limit** — Voltage drop when current starts to limit `0.1` `V` (default) | positive scalar

Approximate voltage drop across the component when the current limit
is active. When the voltage drop is equal to this value, the block
limits the current to 0.9993 times the current limit value.

### **Limit-state conductance** — Limit-state conductance `1e-3` `1/Ohm` (default) | positive scalar

Rate of change of current with respect to the voltage drop for large
current magnitudes.

### Thermal Port

### **Thermal mass** — Thermal mass `100` `J/K` (default) | positive scalar

Heat energy required to raise the temperature by one K.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

### R2024a: **Initial Temperature** parameter replaced with **Temperature** variable

The **Initial temperature** parameter has been replaced with the
**Temperature** variable inside the **Initial
Targets** section in the block dialog box or Property Inspector.

If a model you created in an earlier release contains this block, the software
automatically sets the value of the **Temperature** variable inside
the **Initial Targets** section to the value you specified for the
**Initial temperature** parameter.

### R2024a: Specify constant asymmetric and variable symmetric current limits

You can now specify different current limits in the direction of forward and
reverse current. To enable this option, set the **Limiter
type** parameter to `Constant asymmetric
limits`.

You can also define the magnitude of the current limit as a function of time by
using an input physical signal. To enable this option, set the **Limiter
type** parameter to `Variable
limit`.

## Description

Behavioral model of current limiter

The Current Limiter block provides a behavioral model
of a current limiter. Use this block to model current limiting in power supplies and
motor drives or in components that limit inrush current.

The block limits the current using a hyperbolic tangent function,

i=iLIMtanh(4vvLIM)+gLIMv,

where:

- *i* is the current through the component.
- *v* is the voltage drop across the component.
- *i*LIM is the current limit.
- *v*LIM is the approximate voltage drop
  across the component when the current limit is active.
- *g*LIM is the rate of change of
  current with respect to the voltage drop at large current magnitudes. This
  variable is also called the *limit-state
  conductance*.

The *g*LIM*v* term represents
how you cannot limit the current to a fixed value for arbitrarily high voltages. This
term also improves numerical properties during simulation.

Choose a value for *g*LIM such that *g*LIM*v* is small compared to *i*LIM
when *v* is equal to the maximum voltage drop that you expect.

This figure shows a typical *i*-*v* characteristic
for the Current Limiter block. When *i*
is lower than *i*LIM, the device behaves like a
resistor. The conductance is approximately equal to 4*v*LIM/*v*LIM. As *i* approaches
*i*LIM, the rate of change of current with
voltage falls rapidly to the limit-state conductance
*g*LIM.

Graph showing a typical I-V characteristic

To choose a suitable value for *v*LIM, compare
your *i*-*v* characteristic to a plot from a
datasheet. Smaller values give you a steeper gradient at low currents, but the solver
needs tight tolerances and smaller step sizes.

When *v* =
*v*LIM,

i=iLIMtanh(4)+gLIMvLIM=0.9993iLIM+gLIMvLIM.

The current through the component is therefore approximately equal to the current
limit.

The Current Limiter block limits positive and negative
currents. To limit the current to *i*LIM in one
direction only, connect the Current Limiter block to a
Diode block. To prevent any
current limiting in the reverse-biased direction, connect the two blocks in series. To
block any current in the reverse-biased direction, connect the two blocks in parallel.

To use the same current limit *i*LIM for
positive and negative currents, set the **Limiter type** parameter to
`Constant symmetric limits`. The **Current
limit** parameter defines the magnitude of the current limit.

To use a different current limit for positive and negative currents, set the
**Limiter type** parameter to `Constant asymmetric
limits`. The **Current limit** parameter defines the
current limit for positive currents and the **Reverse direction current
limit** parameter defines the limit for negative currents.

To use a current limit that is a function of time, set the **Limiter
type** parameter to `Variable limit`. The input
physical signal to the **Lim** port defines the magnitude of the
current limit.

### Thermal Port

This block has one optional thermal port. To control the
visibility of the thermal port, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain a thermal
  port.
- `Show thermal port` — The block contains one thermal
  conserving port.

The thermal port model contains a thermal mass. The power dissipated by the
current limiter, plus the heat flow into the thermal port, drives the thermal mass
differential equation,

mdTdt=Ploss+QH,

where:

- *m* is the thermal mass.
- *T* is the thermal port temperature.
- *P*loss is the electrical loss,
  *v*·*i*.
- *Q*H is the heat flow from the
  external network into the thermal port.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
