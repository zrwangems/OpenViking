---
type: simulink-block
title: 'Lowpass Resampler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'lowpassresampler'
documentation_source_path: 'ref/lowpassresampler.html'
language: en
---

# Lowpass Resampler

## Ports
```yaml
ports:
- name: in
  summary: Discrete time input signal scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: out
  summary: Continuous time output signal scalar
  direction: output
  data_types: single | double
```

### Input

### **in** — Discrete time input signal scalar

Discrete time input signal, specified as fixed-step or variable-step
scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **out** — Continuous time output signal scalar

Continuous time output signal, returned as a fixed-step or variable-step
scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Inherit output rise/fall time
  summary: Inherit output rise/fall time from fixed-step input sample time on (default) | off
  group: ''
- name: Output rise/fall time
  summary: 20%−80% output rise/fall time 1e-10 (default) | positive real scalar
  group: ''
  block_parameter: OutputRiseFall
  type: character vector
  values: positive real scalar
  default: 1e-10
- name: Number of samples of delay
  summary: Number of samples of propagation delay for fixed-step operation 1 (default) | positive real scalar
  group: ''
  block_parameter: NDelay
  type: character vector
  values: positive real scalar
  default: '1'
- name: Output sample time
  summary: Type of output sample time Inherited (default) | Fixed step discrete | Variable step discrete
  group: ''
  block_parameter: OutputTsType
  type: character vector
  values: Fixed step discrete | Variable step discrete
  default: Inherited
- name: Samples out per rise/fall time
  summary: Number of output samples in single output rise/fall time 5 (default) | positive real scalar
  group: ''
  block_parameter: OutputTsRatio
  type: character vector
  values: positive real scalar
  default: '5'
- name: Enable large buffer
  summary: Enable extra buffer samples on (default) | off
  group: ''
- name: Number of extra buffer samples
  summary: Number of extra buffer samples to support sample delays 10 (default) | positive real scalar
  group: ''
  block_parameter: NBuffer
  type: character vector
  values: positive real scalar
  default: '10'
```

### **Inherit output rise/fall time** — Inherit output rise/fall time from fixed-step input sample time on (default) | off

Select to inherit the output rise/fall time from the fixed-step input sample
time.

**Note**

In case of variable step input, there is no rise/fall time to inherit.

### **Output rise/fall time** — 20%−80% output rise/fall time `1e-10` (default) | positive real scalar

20%−80% output rise/fall time, specified as a positive real scalar.

#### Dependencies

To enable this parameter, deselect the **Inherit output rise/fall
time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputRiseFall` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1e-10` |

### **Number of samples of delay** — Number of samples of propagation delay for fixed-step operation `1` (default) | positive real scalar

Number of samples of propagation delay for fixed-step operation, specified as a
positive real scalar.

If the Lowpass Resampler block inherits **Output rise/fall
time** in fixed-step mode, the resampler conversion delay is given by *NDelay*·*τ*, where *NDelay* is the **Number of samples of
delay** parameter and *τ* is the inherited input sample
interval.

In the variable-step input mode, the resampler conversion delay is given by
0.6*τv* when *NDelay*
equals to one, and is (*NDelay*-0.5)·*τv* when *NDelay* is greater than one.
*τv* is 5/3 times the **Output
rise/fall time** parameter.

There is a tradeoff between the delay of the conversion and the suppression of
out-of-band numerical artifacts, with greater delay producing better fidelity in band
and greater suppression out-of-band.

**Note**

If you need anti-aliasing filter rejection, set **Number of samples of
delay** to 5 or higher.

#### Dependencies

To enable this parameter, deselect the **Inherit output rise/fall
time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NDelay` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `1` |

### **Output sample time** — Type of output sample time `Inherited` (default) | `Fixed step discrete` | `Variable step discrete`

Type of the output sample time to be used by downstream blocks, specified as either
fixed step discrete or variable step discrete. The output sampling rate must be higher
than the input sampling rate. For more information, see Variable Step Sampling Scheme.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputTsType` |
| **Type:** character vector |
| **Values:** `Fixed step discrete` | `Variable step discrete` |
| **Default:** `Inherited` |

### **Samples out per rise/fall time** — Number of output samples in single output rise/fall time `5` (default) | positive real scalar

Number of output samples in a single output rise/fall time, specified as a positive
real scalar.

#### Dependencies

To enable this parameter, select the option `Fixed step
discrete` or `Variable step discrete` in the
**Output sample time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutputTsRatio` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `5` |

### **Enable large buffer** — Enable extra buffer samples on (default) | off

Select to enable extra buffer samples. This option is enabled by default.

### **Number of extra buffer samples** — Number of extra buffer samples to support sample delays `10` (default) | positive real scalar

Number of extra buffer samples needed to support the number of samples of delay,
specified as a positive real scalar.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `NBuffer` |
| **Type:** character vector |
| **Values:** positive real scalar |
| **Default:** `10` |
## Libraries

Mixed-Signal Blockset / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

### R2022a: Updated in R2022a

Lowpass Resampler can define its own output sample times.

### R2021a: Introduced in R2021a

Use to change the sampling time of a signal.

## Description

Convert signal from one sample time to another

The Lowpass Resampler block converts either a fixed-step discrete or a
variable-step discrete sample time at its input to a different sample time at its output. To
calculate the output sample values, the block uses a lowpass filtering interpolation
algorithm. The algorithm minimizes frequency aliasing at the output with respect to an output
rise/fall time.

If the output rise/fall time is inherited from a fixed-step discrete input, the cutoff
frequency is the Nyquist rate of the input. Otherwise, the cutoff frequency is the Nyquist
rate associated with a sample interval obtained by scaling the specified 20%−80% output
rise/fall time to a value for 0%−100% rise/fall time.
