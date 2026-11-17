---
type: simulink-block
title: 'PS Transfer Function'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Linear Operators'
documentation_page: 'pstransferfunction'
documentation_source_path: 'ref/pstransferfunction.html'
language: en
---

# PS Transfer Function

## Ports
```yaml
ports:
- name: U
  summary: Input physical signal, untyped physical signal
  direction: input
- name: R
  summary: Reset physical signal, *R*, untyped physical signal
  direction: input
- name: Y0
  summary: Initial output physical signal, *YO*, untyped physical signal
  direction: input
- name: Y
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **U** — Input physical signal, untyped physical signal

Input physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **R** — Reset physical signal, *R*, untyped physical signal

Reset physical signal. Depending on the **External reset**
parameter value, the block resets the output to initial condition on the rising edge,
falling edge, or both the rising and the falling edge of the reset signal.

#### Dependencies

To enable this port, set the **External reset** parameter to
`Rising`, `Falling`, or
`Either`.

### **Y0** — Initial output physical signal, *YO*, untyped physical signal

Physical signal input port for specifying the block's initial output, which is
also the output value after reset.

#### Dependencies

To enable this port, set the **Initial output source**
parameter to `External`.
### Output

### **Y** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Transfer function type
  summary: Specify type of low-pass filter Lag (default) | Lead-lag
  group: ''
- name: Lag time constant, T
  summary: Lag time constant for first-order low-pass filter 1 s (default) | positive scalar
  group: ''
- name: Lead time constant, T1
  summary: Lead time constant for lead-lag filter 2 s (default) | positive scalar
  group: ''
- name: Lag time constant, T2
  summary: Lag time constant for lead-lag filter 1 s (default) | positive scalar
  group: ''
- name: External reset
  summary: Specify whether block resets its state to initial output based on external reset signal None (default) | Rising
    | Falling | Either
  group: ''
- name: Initial output source
  summary: Select whether to specify the initial output value as a block parameter or an additional input signal Internal
    (default) | External
  group: ''
- name: Initial output
  summary: Output signal value and unit at the start of simulation and after reset 0 1 (default) | scalar, vector, or matrix
  group: ''
```

### **Transfer function type** — Specify type of low-pass filter `Lag` (default) | `Lead-lag`

Select the type of the low-pass filter:

- `Lag` — Model a first-order low-pass filter.
- `Lead-lag` — Model a lead-lag filter.

### **Lag time constant, T** — Lag time constant for first-order low-pass filter `1 s` (default) | positive scalar

The lag time constant for first-order low-pass filter.

#### Dependencies

Enabled when the **Transfer function type** parameter is set to
`Lag`.

### **Lead time constant, T1** — Lead time constant for lead-lag filter `2 s` (default) | positive scalar

The lead time constant for lead-lag filter.

#### Dependencies

Enabled when the **Transfer function type** parameter is set to
`Lead-lag`.

### **Lag time constant, T2** — Lag time constant for lead-lag filter `1 s` (default) | positive scalar

The lag time constant for lead-lag filter.

#### Dependencies

Enabled when the **Transfer function type** parameter is set to
`Lead-lag`.

### **External reset** — Specify whether block resets its state to initial output based on external reset signal `None` (default) | `Rising` | `Falling` | `Either`

By default, the block does not reset its state to the initial output. Setting this
parameter to an option other than `None` exposes the input port
**R**. Depending on the parameter value, the block resets its state
on the rising edge, falling edge, or both the rising and the falling edge of the reset
signal.

### **Initial output source** — Select whether to specify the initial output value as a block parameter or an additional input signal `Internal` (default) | `External`

You can specify the block's initial output as either a block parameter or an
additional input signal:

- `Internal` — Define the initial output using the
  **Initial output** parameter.
- `External` — Define the initial output using the
  external physical signal at port **Y0**.

### **Initial output** — Output signal value and unit at the start of simulation and after reset `0 1` (default) | scalar, vector, or matrix

The output signal value and unit at the beginning of a simulation run and after a
reset. The first edit box represents the signal value. This value can be a scalar,
vector, or matrix, matching the size of the output signal at port
**Y**.

The second combo box represents the signal unit, which must be commensurate with the
unit of the output signal at port **Y**. By default, the unit is
`1` (unitless). You can select a unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid expression, such as
`rad/s`. For more information and a list of unit abbreviations, see
How to Specify Units in Block Dialogs
and Unit Definitions.

#### Dependencies

To enable this parameter, set **Initial output source** to
`Internal`.
## Libraries

Simscape / Foundation Library / Physical Signals / Linear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2022b: Reset block output at events

The block includes an additional parameter, **External reset**, for
resetting the output signal at events. You can specify that the block output resets to the
initial output when the physical signal at port **R** triggers a reset.
Also, the initial output source can now be either a physical signal or a block parameter. If
you set the **Initial output source** parameter to
`External`, the physical signal at port **Y0**
supplies the initial output value, which is also the output signal value after a reset.

### R2019a: Unit propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Model low-pass and lead-lag filters

The PS Transfer Function block lets you model first-order
low-pass filters or lead-lag filters. Modeling both the plant and controller in a Simscape™ network improves simulation efficiency. The PS Transfer
Function block lets you easily parameterize a filter in the desired
configuration:

- `Lag` — Model a first-order low-pass filter. You have to
  provide the lag time constant and the initial output as block parameters.
- `Lead-lag` — Model a lead-lag filter. You have to provide the
  lead time constant, the lag time constant, and the initial output as block
  parameters.

The block icon changes depending on the value of the **Transfer function
type** parameter.

| Restriction Type | Block Icon |
| --- | --- |
| `Lag` |  |
| `Lead-lag` |  |

Untyped physical ports facilitate unit propagation. The output signal has the same
physical unit as the input signal.

You can specify the initial block output as either a block parameter or an additional
input signal:

- To define the initial condition as a block parameter, specify the **Initial
  output source** parameter as `Internal` and enter the
  value and unit in the **Initial output** fields.
- To provide the initial output value from an external source, specify the
  **Initial output source** parameter as
  `External`. An additional physical signal input port,
  **Y0**, appears at the top of the block icon. Connect the external
  physical signal to port **Y0**.

### Resetting the State

The block can reset its state to the specified initial output based on an external
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

When you select either of these options, a trigger port **R** appears
at the top of the block icon. Connect the reset physical signal to port
**R**.

### Assumptions and Limitations

- The block assumes unity low-frequency gain. To model non-unity gain, connect a
  PS Gain block in series with the PS
  Transfer Function block.
