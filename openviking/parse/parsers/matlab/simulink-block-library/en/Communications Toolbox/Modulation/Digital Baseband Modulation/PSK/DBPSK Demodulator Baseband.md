---
type: simulink-block
title: 'DBPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'dbpskdemodulatorbaseband'
documentation_source_path: 'ref/dbpskdemodulatorbaseband.html'
language: en
---

# DBPSK Demodulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: DBPSK-modulated baseband signal scalar | column vector
  direction: input
  data_types: double | single
- name: Var
  summary: Noise variance positive scalar | vector of positive values
  direction: input
  data_types: double | single
- name: Out
  summary: Output signal scalar | column vector
  direction: output
  data_types: double | single | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### Input

### **In** — DBPSK-modulated baseband signal scalar | column vector

DBPSK-modulated baseband signal, specified as a complex-valued scalar
or vector. For more information, see Supported Data Types.

This port is unnamed on the block.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Var** — Noise variance positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive
values.

#### Dependencies

To enable this input, set `Noise variance source`
to `Input port`.

**Data Types:** `double` | `single`
### Output

### **Out** — Output signal scalar | column vector

Output signal, returned as a scalar or column vector with element
values of `0` or `1`.

This port is unnamed on the block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## Parameters
```yaml
parameters:
- name: Phase rotation (rad)
  summary: Additional phase shift 0 (default) | scalar
  group: Main
- name: Decision type
  summary: Decision method for demodulation Hard decision (default) | Approximate log-likelihood ratio
  group: Main
- name: Noise variance source
  summary: Source of noise variance Property (default) | Input port
  group: Main
- name: Noise variance
  summary: Variance of noise 1 (default) | nonnegative scalar
  group: Main
- name: Output data type
  summary: Output data type Inherit via internal (default) | Smallest unsigned integer | double | single | int8 | uint8 |
    int16 | uint16 | int32 | uint32 | boolean
  group: Main
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Phase rotation (rad)** — Additional phase shift `0` (default) | scalar

Additional phase shift in radians between previous and current
modulated symbols, specified as a scalar. This value corresponds to the
phase difference between previous and current modulated symbols when the
input is zero.

**Example:** `pi/4`

### **Decision type** — Decision method for demodulation `Hard decision` (default) | `Approximate log-likelihood ratio`

*Since R2024b*

Decision method for the demodulation, specified as `Hard
decision` or `Approximate log-likelihood
ratio`. When set to `Hard decision`, the
demodulator outputs a column vector of bit values. When set to
`Approximate log-likelihood ratio`, the demodulator
generates positive values for 0s and negative values for 1s.

### **Noise variance source** — Source of noise variance `Property` (default) | `Input port`

*Since R2024b*

Source of the noise variance, specified as `Property`
or `Input port`.

#### Dependencies

To enable this parameter, set the `Decision type`
parameter to `Approximate log-likelihood ratio`.

### **Noise variance** — Variance of noise `1` (default) | nonnegative scalar

*Since R2024b*

Variance of the noise, specified as a nonnegative scalar.

#### Dependencies

To enable this parameter, set the `Noise variance
source` parameter to
`Property`.

### **Output data type** — Output data type `Inherit via internal` (default) | `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Output data type, specified as `Inherit via
internal`, `Smallest unsigned
integer`, `double`,
`single`, `int8`,
`uint8`, `int16`,
`uint16`, `int32`,
`uint32`, or
`boolean`.

Setting this parameter to `Inherit via internal
rule` sets the output data type from the input port.
The output data type is the same as the input data type if the input is
of type `single` or `double`.

When you set the `Decision type` parameter to
`Approximate log-likelihood ratio`, the output data
type matches the input data type. The input data type must be either
double or single.

For more information, see Supported Data Types.
## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024b: Includes support for soft decision demodulation

The DBPSK Demodulator Baseband block now supports these functionalities.

- Specify the decision type for the demodulation as `Approximate
  log-likelihood ratio` by using the `Decision
  type` parameter.
- Specify the source of noise variance and its value by using the
  `Noise variance source` and `Noise
  variance` parameters, respectively.

## Description

Demodulate DBPSK-modulated data

The DBPSK Demodulator Baseband block demodulates a signal that was modulated using the
differential binary phase shift keying (DBPSK) method. The input is a baseband
representation of the modulated signal. For more information, see Algorithms.
