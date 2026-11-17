---
type: simulink-block
title: 'MER Measurement'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Utility Blocks'
documentation_page: 'mermeasurement'
documentation_source_path: 'ref/mermeasurement.html'
language: en
---

# MER Measurement

## Ports
```yaml
ports:
- name: Ref
  summary: Reference signal scalar | vector | matrix | 3-D array
  direction: input
  data_types: single | double | fixed point
- name: Rcv
  summary: Received signal scalar | vector | matrix | 3-D array
  direction: input
  data_types: single | double | fixed point
- name: MS
  summary: Percentage MER of received signal scalar
  direction: output
  data_types: double
- name: min
  summary: Minimum percentage MER scalar
  direction: output
  data_types: double
- name: X%
  summary: Value below which *X*% of MER measurements fall scalar
  direction: output
  data_types: double
- name: nSym
  summary: Number of symbols positive integer
  direction: output
  data_types: double
```

### Input

### **Ref** — Reference signal scalar | vector | matrix | 3-D array

Reference signal, specified as a scalar, vector, matrix, or 3-D array.
If you specify this input, the object measures the MER of the `Rcv` input by using this input as a reference
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

### **Rcv** — Received signal scalar | vector | matrix | 3-D array

Received signal, specified as a scalar, vector, matrix, or 3-D
array.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes
### Output

### **MS** — Percentage MER of received signal scalar

Percentage MER of the received signal over the configured measurement
interval, returned as a scalar in units of decibels.

**Data Types:** `double`

### **min** — Minimum percentage MER scalar

Minimum percentage MER over the configured measurement interval,
returned as a scalar in units of decibels.

#### Dependencies

To enable this port, select the **Output minimum
MER** parameter.

**Data Types:** `double`

### **X%** — Value below which *X*% of MER measurements fall scalar

Value below which *X*% of MER measurements fall since
the last reset, returned as a scalar in units of decibels. Set the value
of *X* in the **X-percentile value
(%)** parameter.

#### Dependencies

To enable this port, select the **Output X-percentile
MER** parameter.

**Data Types:** `double`

### **nSym** — Number of symbols positive integer

Number of symbols that the object uses to measure the output, returned
as a positive integer.

#### Dependencies

To enable this port, select the **Output X-percentile
MER** and **Output the number of symbols
processed** parameters.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Reference signal
  summary: Reference signal source Input port | Estimated from reference constellation
  group: ''
- name: Reference constellation
  summary: Reference constellation constellation(pskmod((0:3)',4,pi/4,"bin")) (default) | vector
  group: ''
- name: Measurement interval
  summary: Measurement interval source Input length (default) | Entire history | Custom | Custom with periodic reset
  group: ''
- name: Custom measurement interval
  summary: Custom measurement interval 100 (default) | positive integer
  group: ''
- name: Averaging dimensions
  summary: Averaging dimensions 1 (default) | vector of integers in the range [1, 3]
  group: ''
- name: Output minimum MER
  summary: Option to add min port to output minimum MER measurements Off (default) | On
  group: ''
- name: Output X-percentile MER
  summary: Option to add X% port to output *X*-percentile MER measurements Off (default) | On
  group: ''
- name: X-Percentile value (%)
  summary: Value below which *X*% of MER measurements fall 95 (default) | scalar in the range [0, 100]
  group: ''
- name: Output the number of symbols processed
  summary: Option to add nSym port to output number of symbols Off (default) | On
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Reference signal** — Reference signal source `Input port` | `Estimated from reference constellation`

Reference signal source, specified as `Input
port` or `Estimated from reference
constellation`.

### **Reference constellation** — Reference constellation `constellation(pskmod((0:3)',4,pi/4,"bin"))` (default) | vector

Reference constellation points, specified as a vector of complex or real
values.

#### Dependencies

To enable this parameter, set the **Reference
signal** parameter to `Estimated from reference
constellation`.

### **Measurement interval** — Measurement interval source `Input length` (default) | `Entire history` | `Custom` | `Custom with periodic reset`

Measurement interval source for MER and minimum MER measurements,
specified as one of these values.

- `Input length` — Measure the MER
  using only the current samples.
- `Entire history` — Measure the MER
  for all samples.
- `Custom` — Measure the MER by
  using a sliding window over an interval that you specify.
- `Custom with periodic reset` —
  Measure the MER over an interval that you specify and reset the
  block after measuring over each interval.

### **Custom measurement interval** — Custom measurement interval `100` (default) | positive integer

Custom measurement interval in samples, specified as a positive
integer.

#### Dependencies

To enable this parameter, set the **Measurement
interval** parameter to `Custom`
or `Custom with periodic reset`.

### **Averaging dimensions** — Averaging dimensions `1` (default) | vector of integers in the range [1, 3]

Dimensions over which the block averages the MER measurements, specified
as an integer or row vector of integers in the range [1, 3]. For example, to
average across the columns, set this parameter to
`2`.

This block supports variable-size inputs of the dimensions across which
the averaging takes place. However, the input size for the nonaveraged
dimensions must remain constant. For example, if the input has size
`[1000 3 2]` and you set this parameter to `[1
3]`, then the output size is `[1 3 1]` and the
number of elements in the second dimension must remain fixed at
`3`.

### **Output minimum MER** — Option to add `min` port to output minimum MER measurements `Off` (default) | `On`

Option to add the `min` port to output minimum MER measurements. To enable
minimum MER measurements, select this parameter.

### **Output X-percentile MER** — Option to add `X%` port to output *X*-percentile MER measurements `Off` (default) | `On`

Option to add the `X%` port to output *X*-percentile MER
measurements. To enable *X*-percentile MER measurements,
select this parameter. When you select this parameter,
*X*-percentile MER measurements persist until you reset the
block. The block performs these measurements by using all of the input
frames since the last reset. You can set the value of *X*
in the **X-percentile value (%)** parameter.

### **X-Percentile value (%)** — Value below which *X*% of MER measurements fall `95` (default) | scalar in the range [0, 100]

Value below which *X*% of MER measurements fall,
specified as a scalar in the range [0, 100].

#### Dependencies

To enable this parameter, select the **Output X-percentile
MER** parameter.

### **Output the number of symbols processed** — Option to add `nSym` port to output number of symbols `Off` (default) | `On`

Option to add the `nSym` port to output the number of symbols used to measure
the *X*-percentile MER. To measure the number of symbols
used for *X*-percentile MER measurements, select this
parameter.

#### Dependencies

To enable this parameter, select the **Output X-percentile
MER** parameter.

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

Measure modulation error ratio in digital modulation applications

The MER Measurement block computes a form of signal-to-noise ratio (SNR) measurement that
you can use to assess the ability of a receiver to accurately demodulate a signal.
Specifically, it returns the modulation error ratio (MER), minimum MER, and percentile
MER for a received signal. You use the MER measurements to determine system performance
in communications applications. For example, to determine compliance with applicable
DVB-T system radio transmission standards conformance testing requires accurate MER
measurements.

This icon shows the block with all ports enabled.MER Measurement block with all ports enabled
