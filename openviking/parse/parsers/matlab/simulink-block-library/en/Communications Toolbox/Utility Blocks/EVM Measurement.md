---
type: simulink-block
title: 'EVM Measurement'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'evmmeasurement'
documentation_source_path: 'ref/evmmeasurement.html'
language: en
---

# EVM Measurement

## Ports

### Input

### **Ref** — Reference signal array

Reference signal, specified as an array of up to three dimensions. If
you specify this input, the object measures the EVM of the `Rcv` input by using this input as a reference
constellation.

The dimensions of this input must match those of the
`Rcv` input. The object uses each element of this
input as the reference symbol for the corresponding element of the
`Rcv` input.

#### Dependencies

To enable this port, set the **Reference signal**
parameter to `Input port`.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **Rcv** — Received signal array

Received signal, specified as an array of up to three
dimensions.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes
### Output

### **RMS** — Percentage RMS EVM scalar

Percentage RMS EVM over the configured measurement interval, returned
as a scalar.

**Data Types:** `double`

### **max** — Maximum percentage EVM scalar

Maximum percentage EVM over the configured measurement interval,
returned as a scalar.

#### Dependencies

To enable this port, set the **Output maximum
EVM** parameter to `On`.

**Data Types:** `double`

### **X%** — Value below which *X*% of EVM measurements fall scalar in the range [0, 100]

Value below which *X*% of EVM measurements fall since
the last reset, returned as a scalar in the range [0, 100]. Set the
value of *X* in the **X-percentile value
(%)** parameter.

#### Dependencies

To enable this port, set the **Output X-percentile
EVM** parameter to `On`.

**Data Types:** `double`

### **nSym** — Number of symbols positive integer

Number of symbols used to measure the *X*-percentile
EVM, returned as a positive integer.

#### Dependencies

To enable this port, set the **Output X-percentile
EVM** and **Output the number of symbols
processed** parameters to `On`.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Normalize RMS error vector by** — Normalization method `Average reference signal power` (default) | `Average constellation power` | `Peak constellation power`

Normalization method used in EVM calculation, specified as
`Average reference signal power`,
`Average constellation power`, or
`Peak constellation power`. For more
information, see Algorithms.

### **Average constellation power** — Average constellation power `1` (default) | positive scalar

Average constellation power in watts, specified as a positive
scalar.

#### Dependencies

To enable this parameter, set the **Normalize RMS error
vector** parameter to `Average constellation
power`.

### **Peak constellation power** — Peak constellation power `1` (default) | positive scalar

Peak constellation power in watts, specified as a positive scalar.

#### Dependencies

To enable this parameter, set the **Normalize RMS error
vector** parameter to `Peak constellation
power`.

### **Reference signal** — Reference signal source `Input port` | `Estimated from reference constellation`

Reference signal source. To provide an explicit reference signal against
which to measure received signal, set this parameter to `Input
port`. To measure the EVM of the received signal against a
reference constellation, set this parameter to `Estimated from
reference constellation`.

### **Reference constellation** — Reference constellation `constellation(pskmod((0:3)',4,pi/4,"bin"))` (default) | vector

Reference constellation points, specified as a vector of complex or real
values.

#### Dependencies

To enable this parameter, set the **Reference
signal** parameter to `Estimated from reference
constellation`.

### **Measurement interval** — Measurement interval source `Input length` (default) | `Entire history` | `Custom` | `Custom with periodic reset`

Measurement interval source for RMS and maximum EVM measurements,
specified as one of these values.

- `Input length` — Measure the EVM
  using only the current samples.
- `Entire history` — Measure the EVM
  for all samples.
- `Custom` — Measure the EVM over an
  interval you specify and use a sliding window.
- `Custom with periodic reset` —
  Measure the EVM over an interval you specify and reset the block
  after measuring over each interval.

### **Custom measurement interval** — Custom measurement interval `100` (default) | positive integer

Custom measurement interval in samples, specified as a positive
integer.

#### Dependencies

To enable this parameter, set the **Measurement
interval** parameter to `Custom`
or `Custom with periodic reset`.

### **Averaging dimensions** — Averaging dimensions `1` (default) | vector of integers in the range [1, 3]

Dimensions over which the block averages the EVM measurements, specified
as an integer or row vector of integers in the range [1, 3]. For example, to
average across the rows, set this parameter to `2`.

This block supports variable-size inputs of the dimensions across which
the averaging takes place. However, the input size for the non-averaged
dimensions must remain constant. For example, if the input has size
`[1000 3 2]` and you set this parameter to `[1
3]`, then the output size is `[1 3 1]` and the
number of elements in the second dimension must remain fixed at
`3`.

### **Output maximum EVM** — Option to add `max` port to output maximum EVM measurements `Off` (default) | `On`

Option to add the `max` port to output maximum EVM measurements.

### **Output X-percentile EVM** — Option to add `X%` port to output *X*-percentile EVM measurements `Off` (default) | `On`

Option to add the `X%` port to output *X*-percentile EVM
measurements. When you set this parameter to `On`,
*X*-percentile EVM measurements persist until you reset
the block. The block performs these measurements by using all of the input
frames since the last reset. You can set the value of *X*
in the **X-percentile value (%)** parameter.

### **X-percentile value (%)** — Value below which *X*% of EVM measurements fall `95` (default) | scalar in the range [0, 100]

Value below which *X*% of EVM measurements fall,
specified as a scalar in the range [0, 100].

#### Dependencies

To enable this parameter, set the **Output X-percentile
EVM** parameter to `On`.

### **Output the number of symbols processed** — Option to add `nSym` port to output number of symbols `Off` (default) | `On`

Option to add the `nSym` port to output number of symbols used to measure the
*X*-percentile EVM.

#### Dependencies

To enable this parameter, set the **Output X-percentile
EVM** parameter to `On`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as `Interpreted
execution` or `Code generation`.

- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option requires less startup time, but the
  speed of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Utility Blocks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To generate code in a model using this block, you must enable **Dynamic
Memory Allocation in MATLAB Functions**. For more information, see
Dynamic memory allocation in MATLAB functions (Simulink).

## Version History

**Introduced in R2009b**

## Description

Measure error vector magnitude (EVM)

The EVM Measurement block measures the root mean squared (RMS) EVM,
maximum EVM, and percentile EVM of a received signal. EVM is an indication of modulator
or demodulator performance.

This icon shows the block with all ports enabled.EVM measurement block with all ports enabled.
