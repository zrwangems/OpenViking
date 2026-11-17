---
type: simulink-block
title: 'Bernoulli Binary Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Random Data Sources'
documentation_page: 'bernoullibinarygenerator'
documentation_source_path: 'ref/bernoullibinarygenerator.html'
language: en
---

# Bernoulli Binary Generator

## Ports
```yaml
ports:
- name: Out
  summary: Output data signal scalar | vector | matrix
  direction: output
  data_types: double
```

### Output

### **Out** — Output data signal scalar | vector | matrix

Output data signal, returned as a scalar, vector, or matrix.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Probability of zero
  summary: Probability of generating zero at output 0.5 (default) | scalar in the range [0, 1] | vector of scalars in the
    range [0, 1]
  group: ''
- name: Source of initial seed
  summary: Source of initial seed for random number generator Auto (default) | Parameter
  group: ''
- name: Initial seed
  summary: Initial seed for random number generator nonnegative integer
  group: ''
- name: Sample time
  summary: Sample time of output signal 1 (default) | -1 | positive scalar
  group: ''
- name: Samples per frame
  summary: Samples per frame of output signal 1 (default) | positive scalar
  group: ''
- name: Output data type
  summary: Data type of output signal double (default) | single | uint8 | uint16 | uint32 | boolean
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Probability of zero** — Probability of generating zero at output `0.5` (default) | scalar in the range [0, 1] | vector of scalars in the range [0, 1]

Probability of zero must be in the range of [0, 1]. The number of elements in the
**Probability of zero** parameter corresponds to the number of
independent channels output from the block. The Bernoulli distribution with parameter
*p* produces zero with probability *p* and one with
probability *1-p*.

### **Source of initial seed** — Source of initial seed for random number generator `Auto` (default) | `Parameter`

Source of the initial seed for the random number generator, specified as either:

- `Auto` –– The block uses the global random number
  stream. If you use the `parsim` (Simulink) function, see Tips.
- `Parameter` –– The block sets the random number
  generator seed to **Initial
  seed**.

For more information, see Managing the Global Stream Using RandStream and Random Number Generators.

### **Initial seed** — Initial seed for random number generator nonnegative integer

Initial seed value for the random number generator, specified as a nonnegative
integer. If this parameter is a constant, then the resulting sequence is
repeatable.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of initial
seed** to `Parameter`.

### **Sample time** — Sample time of output signal `1` (default) | -1 | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

### **Samples per frame** — Samples per frame of output signal `1` (default) | positive scalar

Samples per frame in one channel of the output signal, specified as a positive
integer. For information on the relationship between **Sample time**
and **Samples per frame**, see Sample Timing.

### **Output data type** — Data type of output signal `double` (default) | `single` | `uint8` | `uint16` | `uint32` | `boolean`

Output data type, specified as `double`, `single`,
`uint8`, `uint16`, `uint32`, or
`boolean`.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

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

Updates to the random number stream processing for the Bernoulli Binary Generator block
remove some limitations. Before this update, certain operating modes resulted in the block
generating the same numbers every time the simulation ran. This change removes the
limitations noted for those operating modes.

### R2024a: Seed value must be integer

The Bernoulli Binary Generator block requires a nonnegative integer value for the
**Seed** parameter.

### R2024a: R2015b Bernoulli Binary Generator block version no longer updated automatically

Starting in R2024a, models containing a Bernoulli Binary Generator block that has not
been updated from the R2015b version, will need to be replaced with the current
Bernoulli Binary Generator block version.

### R2020a: Bernoulli Binary Generator block update supported in Upgrade Advisor

Starting in R2020a, Bernoulli Binary Generator block allows you to use the Upgrade Advisor. You can
update to the block version announced in R2015b or keep the block version available before
R2015b.

- Use the Upgrade Advisor to update existing models that include the Bernoulli Binary Generator
  block.
- Behavior of the random number generator is changed. The statistics are improved. For
  more information, see Source blocks output frames of contiguous time samples but do not use frame attribute.

## Description

Generate Bernoulli-distributed random binary numbers

The Bernoulli Binary Generator block generates random binary numbers using a Bernoulli
distribution. Use this block to generate random data bits to simulate digital communication
systems and obtain performance metrics such as bit error rate. The Bernoulli distribution with
parameter *p* produces zero with probability *p* and one
with probability *1-p*. The Bernoulli distribution has mean value
*1-p* and variance *p*(*1-p*). The
**Probability of zero** parameter specifies *p* and can
be any real number in range [0, 1].

The output signal can be a column or row vector, two-dimensional matrix, or scalar. The
number of rows in the output signal corresponds to the number of samples in one frame and is
set by the **Samples per frame** parameter. The number of columns in the
output signal corresponds to the number of channels and is set by the number of elements in
the **Probability of zero** parameter. For more details, see Sinks.
