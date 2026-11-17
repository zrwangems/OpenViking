---
type: simulink-block
title: 'Random Integer Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Random Data Sources'
documentation_page: 'randomintegergenerator'
documentation_source_path: 'ref/randomintegergenerator.html'
language: en
---

# Random Integer Generator

## Ports
```yaml
ports:
- name: Out
  summary: Random integer output scalar | vector | matrix
  direction: output
```

### Output

### **Out** — Random integer output scalar | vector | matrix

Random integer output, returned as a scalar, vector, or matrix. This
port is unnamed on the block. The data type is set using the Output data type parameter.

The number of rows in the output data equals the value of the
Samples per frame parameter and corresponds to the number of samples
in one frame. The number of columns in the output data equals the number
of elements in the Set size
parameter and corresponds to the number of channels.
## Parameters
```yaml
parameters:
- name: Set size
  summary: Set size 8 (default) | positive integer | row vector of positive integers
  group: ''
- name: Source of initial seed
  summary: Source of initial seed Auto (default) | Parameter
  group: ''
- name: Initial seed
  summary: Initial seed value 0 (default) | nonnegative integer
  group: ''
- name: Sample time
  summary: Sample time 1 (default) | -1 | positive scalar
  group: ''
- name: Samples per frame
  summary: Samples per frame 1 (default) | positive integer
  group: ''
- name: Output data type
  summary: Output data type double (default) | single | uint8 | uint16 | uint32 | boolean
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Set size** — Set size `8` (default) | positive integer | row vector of positive integers

Set size,*M*, specified as a positive integer or row
vector of positive integers. The block generates integers in the range [0,
(*M* – 1)]. The number of elements in **Set
size** corresponds to the number of independent channels output
from the block.

- If **Set size** is a scalar, then all output
  random variables are independent and identically distributed
  (i.i.d.).
- If **Set size** is a vector, then the length of
  the vector determines the number of output channels. The channels
  can have differing output ranges.

### **Source of initial seed** — Source of initial seed `Auto` (default) | `Parameter`

Source of the initial seed for the random number generator, specified as either:

- `Auto` –– The block uses the global
  random number stream. If you use the `parsim` (Simulink)
  function, see Tips.
- `Parameter` –– The block sets the
  random number generator seed to **Initial
  seed**.

For more information, see Managing the Global Stream Using RandStream and Random Number Generators.

### **Initial seed** — Initial seed value `0` (default) | nonnegative integer

Initial seed value for the random number generator, specified as a
nonnegative integer. If the **Initial seed** parameter is a
constant, then the resulting sequence is repeatable.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of
initial seed** parameter to
`Parameter`.

### **Sample time** — Sample time `1` (default) | -1 | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

Samples per frame, specified as a positive integer indicating the number
of samples per frame in one channel of the output data. For information on
the relationship between **Sample time** and
**Samples per frame**, see Sample Timing.

### **Output data type** — Output data type `double` (default) | `single` | `uint8` | `uint16` | `uint32` | `boolean`

Output data type, specified as `double`,
`single`, `uint8`,
`uint16`, `uint32`, or
`boolean`. If this parameter is set to
`boolean`, you must set the Set size parameter to
`2`.

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

Communications Toolbox / Comm Sources / Random Data Sources

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

### R2024a: Random number stream processing updates

Updates to the random number stream processing for the Random Integer Generator block
remove some limitations. Before this update, certain operating modes resulted in the
block generating the same numbers every time the simulation ran. This change removes
the limitations noted for those operating modes.

### R2024a: Seed value must be integer

The Random Integer Generator block requires a nonnegative integer value for the
**Seed** parameter.

### R2024a: R2015b Random Integer Generator block version no longer updated automatically

Starting in R2024a, models containing a Random Integer Generator block that has
not been updated from the R2015b version, will need to be replaced with the current
Random Integer Generator block version.

### R2020a: Random Integer Generator block update supported in Upgrade Advisor

Starting in R2020a, Random Integer Generator block allows you to use the Upgrade Advisor. You
can update to the block version announced in R2015b or keep the block version
available before R2015b.

- Use the Upgrade Advisor to update existing models that include the
  Random Integer Generator block.
- Behavior of the random number generator is changed. The statistics are
  improved. For more information, see Source blocks output frames of contiguous time samples but do not use frame attribute.

## Description

Generate integers randomly distributed in specified range

The Random Integer Generator block generates uniformly distributed random integers in the
range [0, *M*-1], where *M* is specified by the
**Set size** parameter. Use this
block to generate random binary-valued or integer-valued data.
