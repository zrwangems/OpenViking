---
type: simulink-block
title: 'Total Harmonic Distortion'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'totalharmonicdistortion'
documentation_source_path: 'ref/totalharmonicdistortion.html'
language: en
---

# Total Harmonic Distortion

## Ports

### Input

### **u** — Harmonic magnitude scalar | vector

Harmonic magnitude.

**Data Types:** `single` | `double`
### Output

### **THD (%)** — Total harmonic distortion scalar | vector

Total harmonic distortion as a percentage.

**Data Types:** `single` | `double`

## Parameters

### **Fundamental frequency** — Fundamental frequency in Hz `60` `Hz` (default)

Fundamental frequency, in Hz.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | nonnegative scalar

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify `-1`. For
discrete-time operation, specify a positive integer. For continuous-time
operation, specify `0`.

To improve accuracy, set this value at least 10 times smaller than the **Time
constant** parameter.

**Note**

If this block is in a masked subsystem, or another variant subsystem
that allows either continuous or discrete operation, promote the sample
time parameter to ensure correct switching between the continuous and
discrete implementations of the block. For more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / Measurements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Total harmonic distortion measurement

The Total Harmonic Distortion block calculates the total harmonic
distortion (THD) percentage using these equations:

M=harmonic magnitude2,

and

%THD=100∑i=2nMi2M1,

where:

- *Mi* is the root mean squared
  (RMS) value of the harmonic magnitude that corresponds to the
  ith harmonic order.
- *M* is *VRMS* or
  *IRMS*.
- ∑i=2nMi2 is the sum of all harmonic components.
