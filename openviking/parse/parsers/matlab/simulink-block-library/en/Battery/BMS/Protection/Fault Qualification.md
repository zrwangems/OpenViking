---
type: simulink-block
title: 'Fault Qualification'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Protection'
documentation_page: 'faultqualification'
documentation_source_path: 'ref/faultqualification.html'
language: en
---

# Fault Qualification

## Ports

### Input

### **Symptom** — Symptom flag `0` | `1` | vector of `0` or `1` values

Indication that the battery has a symptom to qualify. If this input is equal to
`1`, the battery has a symptom.
### Output

### **Error** — Error flag `0` | `1` | vector of `0` or `1` values

Indication that the battery has an error. If this output is equal to
`1`, the battery has an error. The size of this
port is equal to the size of the **Symptom** input port.

## Parameters

### **Qualification time (s)** — Error qualification time `2` (default) | positive scalar

Time required to qualify the error, in seconds.

### **Disqualification time (s)** — Error disqualification time `4` (default) | nonnegative scalar

Time required to disqualify the error, in seconds. If you set this
parameter to `0`, the block does not disqualify the
error.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify this
parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that allows
you to switch between continuous operation and discrete operation, promote
the sample time parameter. Promoting the sample time parameter ensures
correct switching between the continuous and discrete implementations of the
block. For more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Battery / BMS / Protection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Specify vectorized inputs of logical signals

The **Symptom** input port now accepts vectors of logical values
`0` or `1`. The qualification and
disqualification times are the same for all input symptoms.

## Description

Fault qualification algorithm

This block implements a fault qualification algorithm. The input and output ports are logic
signals and you can specify them as scalars or vectors. To prevent error
disqualification, set the **Disqualification time** parameter to
`0`.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
block for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the block for
discrete time, set the **Sample time (-1 for inherited)**
parameter to a positive, nonzero value, or to `-1` to inherit the
sample time from an upstream block.

**Note**

Continuous-time implementation of this block works only in a double-precision
floating-point simulation. If you provide single-precision floating-point parameters and
inputs, this block casts them to double-precision floating-point values to prevent
errors.

This diagram shows the structure of the block:

### Equations

This figure shows how the internal counter and the **Error** output port
of this block work:

The fault qualification takes a symptom as input. The input is `1` when a
symptom is present, such as an overvoltage error, and `0` when the
symptom is not present. When the symptom is present, the block increments an
internal counter. When the counter reaches the maximum value corresponding to the
desired qualification time, the output port is `1`.

You must provide a disqualification time greater than `0` to allow
disqualification. When the disqualification time is not `0` and the
symptom is not present, the block decrements the counter until it reaches
`0`. When the counter is `0`, the output port
is `0`.
