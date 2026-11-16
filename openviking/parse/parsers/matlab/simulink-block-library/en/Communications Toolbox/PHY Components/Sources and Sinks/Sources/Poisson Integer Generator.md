---
type: simulink-block
title: 'Poisson Integer Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Sources and Sinks / Sources'
documentation_page: 'poissonintegergenerator'
documentation_source_path: 'ref/poissonintegergenerator.html'
language: en
---

# Poisson Integer Generator

## Ports

### Output

### **Out** — Random integer output scalar | vector | matrix

Random integer output, returned as a scalar,
vector, or matrix. This port is unnamed on the
block. Set the data type by using the **Output data type** parameter.

- The number of rows in the output data
  corresponds to the number of samples in one frame
  and equals the value of the **Samples per frame** parameter.
- The number of columns in the output signal
  corresponds to the number of channels and equals
  the number of elements in the **Poisson parameter(Lambda)**
  parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Poisson parameter(Lambda)** — Poisson parameter λ `0.1` (default) | positive scalar | vector of positive scalars

The Poisson parameter λ, specified as a positive
scalar or row vector of positive scalar values.

- If you set this parameter to a scalar value,
  then every element in the output vector shares the
  same Poisson parameter.
- If you set this parameter to a row vector,
  then the number of elements correspond to the
  number of independent channels output from the
  block.

### **Source of initial seed** — Source of initial seed for random number generator `Auto` (default) | `Parameter`

Source of the initial seed for the random number
generator, specified as either:

- `Auto` –– The block
  uses the global random number stream. If you use
  the `parsim` (Simulink) function, see Tips.
- `Parameter` –– The
  block sets the random number generator seed to
  **Initial seed**.

For more information, see Managing the Global Stream Using RandStream and Random Number Generators.

### **Initial seed** — Initial seed for random number generator nonnegative integer

Initial seed value for the random number generator,
specified as a nonnegative integer. If this
parameter is a constant, then the resulting sequence
is repeatable.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Source of initial seed** to
`Parameter`.

### **Sample time** — Sample time of output signal `1` (default) | -1 | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

### **Samples per frame** — Samples per frame of output signal `1` (default) | positive scalar

Samples per frame in one channel of the output signal,
specified as a positive integer. For information on
the relationship between **Sample
time** and **Samples per
frame**, see Sample Timing.

### **Output data type** — Data type of output signal `double` (default) | `uint8` | `uint16` | `uint32` | `boolean`

Output data type, specified as
`double`,
`uint8`,
`uint16`,
`uint32`, or
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
| **Data Types** | `double` | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: Random number stream processing updates

Updates to the random number stream processing for the
Poisson Integer Generator block remove some limitations.
Before this update, certain operating modes resulted in the block
generating the same numbers every time the simulation ran. This
change removes the limitations noted for those operating
modes.

### R2024a: Seed value must be integer

The Poisson Integer Generator block requires a nonnegative integer
value for the **Seed** parameter.

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink no longer allows you to use the Poisson Integer Generator block
version available before R2015b.

- Existing models automatically update to load the
  Poisson Integer Generator block version announced in R2015b. For
  more information on block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).
- Behavior of the random number generator is changed.
  The statistics are improved. For more information,
  see Source blocks output frames of contiguous time samples but do not use frame attribute.

## Description

Generate Poisson-distributed random integers

The Poisson Integer Generator block generates random integers using a Poisson
distribution. The probability of generating a nonnegative integer
*k* is λkexp(−λ)/(k!), where λ is a positive number known as the
*Poisson parameter*.

When you use this block to generate noise in a binary transmission channel,
typical values for the **Poisson parameter(Lambda)** parameter are much less than
1.
