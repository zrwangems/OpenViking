---
type: simulink-block
title: 'Binary Symmetric Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'binarysymmetricchannel'
documentation_source_path: 'ref/binarysymmetricchannel.html'
language: en
---

# Binary Symmetric Channel

## Ports
```yaml
ports:
- name: Input
  summary: Input signal column vector | matrix
  direction: input
- name: Output
  summary: Binary output signal column vector | matrix
  direction: output
- name: Err
  summary: Error locations column vector | matrix
  direction: output
```

### Input

### **Input** — Input signal column vector | matrix

Input signal, specified as a column vector or an
*N*S-by-*N*C
matrix of `Boolean` values.
*N*S is the number of
samples per channel. *N*C is the
number of independent data channels. For more information, see Tips.
### Output

### **Output** — Binary output signal column vector | matrix

Binary output signal, returned as a column vector or matrix with the
same dimensions as `Input`. The output signal is a
version of the input signal that has been modified by introducing random
errors based on the specified Error probability. To set the output data type, use Output data type.

### **Err** — Error locations column vector | matrix

Error locations, returned as a column vector or matrix with the same
dimensions as `Input`. Element values in
`Err` are `1` or
`0`, where:

- `1` indicates that the corresponding
  element in `Output` has an error.
- `0` indicates that the corresponding
  element in `Output` does not have an
  error.

The data type of `Err` is the same as
Output, as set
by Output data type.

#### Dependencies

To enable this port, select Output error vector.
## Parameters
```yaml
parameters:
- name: Error probability
  summary: Probability of error occurrence 0.05 (default) | scalar
  group: ''
- name: Output error vector
  summary: Option to output error locations on (default) | off
  group: ''
- name: Output data type
  summary: Output data type double (default) | single | boolean
  group: ''
- name: Initial seed
  summary: Initial seed 71 (default) | integer
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Error probability** — Probability of error occurrence `0.05` (default) | scalar

Probability of error occurrence for the input signal elements, specified
as a scalar in the range [0,1]. The probability of error applies
independently for each element.

### **Output error vector** — Option to output error locations `on` (default) | `off`

To enable the `Err` output port to the block, select
this parameter.

### **Output data type** — Output data type `double` (default) | `single` | `boolean`

Select the output data type as `double`,
`single`, or `boolean`. This parameter
sets the output data type for both the **Output** and
**Err** ports.

### **Initial seed** — Initial seed `71` (default) | integer

Initial seed value for the random number generator used by the block,
specified as an integer. The block uses the `mt19937ar`
algorithm to generate uniformly distributed random numbers. For details
about the `mt19937ar` algorithm, see Creating and Controlling a Random Number Stream.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as:

- `Code generation` –– Simulate the
  model using generated C code. The first time you run a
  simulation, Simulink generates C code for the block. The C code is
  reused for subsequent simulations as long as the model does not
  change. This option requires additional startup time.
- `Interpreted execution` –– Simulate
  the model using the MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you
  can debug the source code of the block.
## Libraries

Communications Toolbox / Channels

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2018b: Random Number Generation

To improve statistical properties, the Binary Symmetric Channel block uses the
`mt19937ar` algorithm with `RandStream`. The Binary Symmetric Channel block accepts a single scalar value for
the Initial seed parameter.

## Description

Introduce binary errors

The Binary Symmetric Channel block introduces errors to the input signal transmitted through a
binary symmetric channel. The errors are introduced based on the specified Error probability. For more information, see Tips.
