---
type: simulink-block
title: 'PS Integrator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Linear Operators'
documentation_page: 'psintegrator'
documentation_source_path: 'ref/psintegrator.html'
language: en
---

# PS Integrator

## Ports

### Input

### **I** — Input physical signal, *u*, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **R** — Reset physical signal, *R*, untyped physical signal

Reset physical signal. Depending on the **External reset**
parameter value, the block resets the output to the initial condition on the rising
edge, falling edge, or both the rising and the falling edge of the reset
signal.

#### Dependencies

To enable this port, set the **External reset** parameter to
`Rising`, `Falling`, or
`Either`.

### **X0** — Initial condition physical signal, *XO*, untyped physical signal

Physical signal input port that specifies the initial condition of the block. The
unit of this signal must be commensurate with the unit of the output signal,
*y*.

#### Dependencies

To enable this port, set the **Initial condition source**
parameter to `External`.

### **U** — Upper saturation bound physical signal, *U*, untyped physical signal

Physical signal input port that specifies the upper saturation bound for the block
output. The unit of this signal must be commensurate with the unit of the output
signal, *y*.

#### Dependencies

To enable this port, set the **Limit output** parameter to
`Upper` or `Both` and the
**Limit output source** parameter to
`External`.

### **L** — Lower saturation bound physical signal, *L*, untyped physical signal

Physical signal input port that specifies the lower saturation bound for the block
output. The unit of this signal must be commensurate with the unit of the output
signal, *y*.

#### Dependencies

To enable this port, set the **Limit output** parameter to
`Lower` or `Both` and the
**Limit output source** parameter to
`External`.
### Output

### **O** — Output physical signal, *y*, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **External reset** — Whether block resets to initial condition based on external reset signal `None` (default) | `Rising` | `Falling` | `Either`

You can specify that the block resets its state to the specified initial condition
based on an external signal. By default, the block does not reset its state. Setting
this parameter to an option other than `None` exposes the input
port **R**. Depending on the parameter value, the block resets its
state on the rising edge, falling edge, or both the rising and the falling edge of the
reset signal.

### **Initial condition source** — Whether to specify initial condition as block parameter or additional input signal `Internal` (default) | `External`

You can specify the initial condition of the block as either a block parameter or an
input signal:

- `Internal` — Define the initial condition for
  integration using the **Initial condition** parameter.
- `External` — Define the initial condition for
  integration using the external physical signal at port **X0**.

### **Limit output** — Whether to limit integrator output `None` (default) | `Upper` | `Lower` | `Both`

You can specify upper and lower bounds for the output signal and cause the block to
function as a limited integrator:

- `None` — Do not limit the output.
- `Upper` — Limit the output at the upper bound.
- `Lower` — Limit the output at the lower bound.
- `Upper` — Limit the output both at the upper and the
  lower bound.

For more information, see Limiting the Output.

### **Limit output source** — Whether to specify saturation bounds as block parameters or input signals `Internal` (default) | `External`

Select the way to specify the upper and lower bounds when limiting output:

- `Internal` — Define the saturation bounds using the
  **Upper limit** and **Lower limit**
  parameters.
- `External` — Define the saturation bounds using the
  external physical signals at ports **U** and
  **L**.

#### Dependencies

To enable this parameter, set the **Limit output** parameter to a
value other than `None`.

### **Initial condition** — Initial state for the integration `0 s` (default) | scalar

Initial condition to use in computing the initial state of the block at the
beginning of a simulation run.

The unit specified for the **Initial condition** parameter must
match the unit of the output signal. By default, the input signal is unitless. Then the
output signal is in `s`, and the **Initial condition**
parameter unit is also `s`. If your input signal has a physical unit,
multiply this unit by a unit of time to set the correct unit for the **Initial
condition** parameter. For example, if the input signal is in
`m/s`, then specify the **Initial condition**
parameter unit as `m`.

#### Dependencies

To enable this parameter, set **Initial condition source** to
`Internal`.

### **Upper limit** — Upper saturation limit for block output `inf s` (default) | scalar

Upper saturation limit for the block output. The unit specified for the
**Upper limit** parameter must match the unit of the output signal.

#### Dependencies

To enable this parameter, set the **Limit output** parameter to
`Upper` or `Both` and the
**Limit output source** parameter to
`Internal`.

### **Lower limit** — Lower saturation limit for block output `-inf s` (default) | scalar

Lower saturation limit for the block output. The unit specified for the
**Lower limit** parameter must match the unit of the output signal.

#### Dependencies

To enable this parameter, set the **Limit output** parameter to
`Lower` or `Both` and the
**Limit output source** parameter to
`Internal`.

## Libraries

Simscape / Foundation Library / Physical Signals / Linear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2022b: Use saturation bounds to limit block output

The block includes the **Limit output**, **Limit output
source**, **Upper limit** and **Lower limit**
parameters. Use these parameters to limit the output signal. For more information, see Limiting the Output.

### R2021a: Reset block state at events

The block includes an additional parameter, **External reset**, which
lets can specify that the block output resets to the initial condition when the physical
signal at port **R** triggers a reset. The initial condition source can now
be either a physical signal or a block parameter. If you set the **Initial condition
source** parameter to `External`, the physical signal at
port **X0** supplies the initial condition value for integration and
reset.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Integrate physical signal

The PS Integrator block outputs the integral of its input
at the current time step. The following equation represents the output of the block:

y(t)=∫t0tu(t)dt+y0

where:

- *u* is the physical signal at input port
  **I**.
- *y*0 is the initial condition.
- *y* is the physical signal at output port
  **O**.
- *t* is time.

The PS Integrator block is a dynamic system with one state,
its output. The input of the PS Integrator block is the time
derivative of the state:

x=y(t)

x0=y0

x˙=u(t)

The solver computes the output of the PS Integrator block
at the current time step by using the current input value and the value of the state at the
previous time step. The PS Integrator block saves its output at
the current time step for the solver to use to compute the output at the next time step. The
block also provides the solver with an initial condition to use to compute the initial state
of the block at the beginning of a simulation run. The default value of the initial condition
is 0 s. You can specify another value for the initial condition as either a block parameter or
an input signal:

- To define the initial condition as a block parameter, specify the **Initial
  condition source** parameter as `Internal` and enter
  the value and unit for the **Initial condition** parameter.
- To provide the initial condition from an external source, specify the
  **Initial condition source** parameter as
  `External`. Selecting this option exposes port
  **X0**. Connect the external initial condition signal to this
  port.

Because the block performs integration of the input signal over time, the unit of the
output signal equals the unit of the input signal multiplied by the unit of time, s. For
example, if the input signal is in `m/s`, then the output signal is in
`m`. The unit specified for the **Initial condition**
parameter or the unit of the external initial condition signal at port **X0**
must be commensurate with the unit of the output signal.

### Resetting the State

The block can reset its state to the specified initial condition based on an external
signal. By default, the **External reset** parameter is set to
`None`. To cause the block to reset its state, select one of the
other **External reset** choices:

- Select `Rising` to reset the state when the reset signal
  rises from a negative or zero value to a positive value.
- Select `Falling` to reset the state when the reset signal
  falls from a positive value to a zero or negative value.
- Select `Either` to reset the state when the reset signal
  changes from zero to a nonzero value, from a nonzero value to zero, or changes
  sign.

Selecting any of these options exposes a trigger port, **R**. Connect
the reset physical signal to this port.

### Limiting the Output

The block can function as a limited integrator, holding its output within the specified
saturation bounds:

- When the integral is less than or equal to the lower saturation limit, the block
  holds the output at the lower saturation limit.
- When the integral is between the lower saturation limit and the upper saturation
  limit, the output is the integral.
- When the integral is greater than or equal to the upper saturation limit, the block
  holds the output at the upper saturation limit.

Use the **Limit output** parameter to specify whether to limit the
output at the lower bound, upper bound, or both. The **Limit output
source** parameter provides two ways of specifying the upper and lower
bounds:

- `Internal` — Define the saturation bounds using the
  **Upper limit** and **Lower limit**
  parameters.
- `External` — Define the saturation bounds using the
  external physical signals at ports **U** and **L**.
