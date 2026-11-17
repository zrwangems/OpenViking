---
type: simulink-block
title: 'PS Constant Delay'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Delays'
documentation_page: 'psconstantdelay'
documentation_source_path: 'ref/psconstantdelay.html'
language: en
---

# PS Constant Delay

## Ports
```yaml
ports:
- name: U
  summary: Input physical signal, untyped physical signal
  direction: input
- name: Y
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **U** — Input physical signal, untyped physical signal

Input physical signal.
### Output

### **Y** — Output physical signal, untyped physical signal

Output physical signal.
## Parameters
```yaml
parameters:
- name: Input history
  summary: Signal value and unit during the initial time interval 0.0 1 (default)
  group: ''
- name: Delay time
  summary: Delay time for the signal 1 s (default)
  group: ''
```

### **Input history** — Signal value and unit during the initial time interval `0.0 1` (default)

The output signal value and unit during the initial time interval, until the
specified delay time elapses after the start of simulation. The first edit box
represents the signal value.

The second combo box represents the signal unit, which must be commensurate with the
unit of the output signal at port **Y**. By default, the unit is
`1` (unitless). You can select a unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid expression, such as
`rad/s`. For more information and a list of unit abbreviations, see
How to Specify Units in Block Dialogs
and Unit Definitions.

### **Delay time** — Delay time for the signal `1 s` (default)

The delay for the signal, in units of time. The parameter value must be positive.
## Libraries

Simscape / Foundation Library / Physical Signals / Delays

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Delay input physical signal by specified time

The PS Constant Delay block generates the output physical
signal, **Y**, by delaying the input physical signal,
**U**:

*Y* = *U* ( *t* –
*τ* )

where *τ* is the delay time.

The delay time is constant throughout the simulation. You specify the value of the delay
time as the **Delay time** parameter.

For the initial time interval, when *t* <= StartTime +
*τ*, the block outputs the **Input history** parameter
value. The unit specified for the **Input history** parameter must be
commensurate with the unit of the output signal.

**Note**

- When simulating a model that contains blocks with delays, memory allocation for
  storing the data history is controlled by the **Delay memory budget
  [kB]** parameter in the Solver Configuration block. If this budget is exceeded, simulation
  errors out. You can adjust this parameter value based on your available memory
  resources.
- For recommendation on how to linearize a model that contains blocks with delays, see
  Linearizing with Simulink Linearization Blocks.

Untyped physical ports facilitate unit propagation. The output signal has the same
physical unit as the input signal.
