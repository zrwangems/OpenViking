---
type: simulink-block
title: 'Error Rate Calculation'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'errorratecalculation'
documentation_source_path: 'ref/errorratecalculation.html'
language: en
---

# Error Rate Calculation

## Ports

### Input

### **Tx** — Transmitted data scalar | column vector

Transmitted data, specified as a scalar or column vector. Input
signals, **Tx** and **Rx** must have same data
type.

- If you specify the **Tx** or **Rx** input as
  a scalar, the block compares this value with all elements of the
  other input.
- If you specify **Tx** and **Rx** inputs as
  vectors, they must have the same size.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rx** — Received data scalar | column vector

Received data, specified as a scalar or column vector. Input signals,
**Rx** and **Tx** must have same data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Sel** — Sample indices positive integer | column vector of positive integers

Indices of the samples to consider when comparing data, specified as a
positive integer or column vector of positive integers.

#### Dependencies

To enable this input, set the **Computation
mode** parameter to `Select samples from
input port`.

**Data Types:** `double`

### **Rst** — Reset error count scalar

Reset error count, specified as a scalar.

#### Dependencies

To enable this input, set the **Reset port**
parameter to `on`.

**Data Types:** `double` | `Boolean`
### Output

### **Out** — Difference between transmitted and received data column vector

Difference between transmitted and received data, returned as a column
vector of the form `[R; N;
S]`, where:

- *R* is the error rate.
- *N* is the number of errors.
- *S* is the number of samples
  compared.

#### Dependencies

To enable this port, set the **Output data**
parameter to `Port`.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Receive delay** — Received signal delay `0` (default) | nonnegative integer

Number of samples by which the received data lags behind the transmitted
data, specified as a nonnegative integer. Use this parameter to align the
samples for comparison in the transmitted and received input data
vectors.

### **Computation delay** — Computation delay `0` (default) | nonnegative scalar

Number of data samples that the object ignores at the beginning of the
comparison, specified as a nonnegative integer. Use this parameter to ignore
the transient behavior of both input signals.

### **Computation mode** — Samples to consider `Entire frame` (default) | `Select samples from mask` | `Select samples from port`

Samples to consider, specified as one of these values.

- `Entire frame` — Compare all
  the samples of the received data to those of the transmitted
  frame.
- `Select samples from mask` —
  Set the indices of the samples to consider when making
  comparisons in the **Selected samples from
  frame** parameter.
- `Select samples from port` — Set the
  indices of the samples to consider when making comparisons in
  the **Sel** input port.

### **Selected samples from frame** — Sample indices `[]` (default) | positive integer | column vector of positive integers

Indices of the samples to consider when comparing data, specified as a
positive integer or column vector of positive integers. The default value,
an empty vector, specifies that the block uses all samples from the received
frame.

#### Dependencies

To enable this parameter, set the **Computation
mode** parameter to `Select samples from
mask`.

### **Output data** — Output data location `Workspace` (default) | `Port`

Output data location, specified as one of these options.

- `Workspace` — Send the output
  data to the workspace variable defined by the
  **Variable name** parameter.
- `Port` — Add an output data
  port to the block and send the output data to that port.

### **Variable name** — Output data variable name `ErrorVec` (default) | character vector | string scalar

Output data variable name in the MATLAB® workspace.

#### Dependencies

To enable this parameter, set the **Output data**
variable to `Workspace`.

### **Reset port** — Option to add `Rst` input port `off` (default) | `on`

Enable the `Rst` input port.

### **Stop simulation** — Option to stop simulation after specified number of errors or comparisons `off` (default) | `on`

Option to stop the simulation after the block detects the number of errors
specified in the **Target number of errors** parameter or
performs the number of comparisons specified in the **Maximum
number of symbols** parameter.

### **Target number of errors** — Option to stop simulation after specified number of errors `100` (default) | positive integer

Option to stop the simulation after detecting this number of errors,
specified as a positive integer.

#### Dependencies

To enable this parameter, set the **Stop
simulation** parameter to `on`.

### **Maximum number of symbols** — Option to stop simulation after comparing specified number of symbols `1e6` (default) | positive integer

Option to stop the simulation after comparing this number of symbols,
specified as a positive integer.

**Note**

If you use the Simulink
Coder™ rapid simulation (RSim) target to build an RSim
executable, then you can tune the **Target number of
errors** and **Maximum number of
symbols** parameters without recompiling the model. This
is useful for Monte Carlo simulations in which you run the simulation
multiple times (perhaps on multiple computers) with different amounts of
noise.

#### Dependencies

To enable this parameter, set the **Stop
simulation** parameter to `on`.

## Libraries

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When you set the **Output data** parameter to
`Workspace`, the block generates no code. Similarly, no
data is saved to the workspace if you set the **Simulation mode**
parameter to `Accelerator` or `Rapid
Accelerator`. If you need error rate information in these cases,
set the **Output data** parameter to
`Port`.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced before R2006a**

## Description

Compute bit error rate or symbol error rate of input data

The Error Rate Calculation block compares input data from a transmitter
with input data from a receiver. The block calculates the error rate as a running
statistic by dividing the total number of unequal pairs of data elements by the total
number of input data elements from one source.

You can use this block to compute the symbol or bit error rate because it does not
consider the magnitude of the difference between input data elements. If the inputs are
bits, then the block computes the bit error rate. If the inputs are symbols, then the
block computes the symbol error rate.

This figure shows the block with all ports enabled.Error Rate Calculation block with all ports enabled.
