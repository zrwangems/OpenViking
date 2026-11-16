---
type: simulink-block
title: 'Receiver Thermal Noise'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'receiverthermalnoise'
documentation_source_path: 'ref/receiverthermalnoise.html'
language: en
---

# Receiver Thermal Noise

## Ports

### Input

### **In1** — Baseband signal scalar | column vector | matrix

Baseband signal, specified as a complex-valued scalar,
*N*S-element column vector,
or
*N*S-by-*N*C
matrix. *N*S is the number of
samples and *N*C is the number
of channels.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out1** — Output signal scalar | column vector | matrix

Output signal, returned as a scalar, column vector, or matrix of
complex values with the same length and data type as the input
signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Specification method** — Thermal noise specification method `Noise temperature` (default) | `Noise figure` | `Noise factor`

Thermal noise specification method, specified as one of these options.

- `Noise temperature` specifies the
  noise in kelvins.
- `Noise figure` specifies the added
  receiver noise in dB relative to an input noise temperature of
  290 K. The noise figure is the decibel equivalent of the noise
  factor.
- `Noise factor` specifies the added
  receiver noise relative to an input noise temperature of 290 K.
  The noise factor is the linear equivalent of the noise
  figure.

### **Noise temperature (K)** — Noise temperature `290` (default) | scalar

Noise temperature in kelvins, specified as a scalar.

**Tunable:** Yes

#### Dependencies

This parameter applies when you set **Specification method** to `Noise
temperature`.

**Data Types:** `double` | `single`

### **Noise figure (dB)** — Receiver noise figure `3.0103` (default) | scalar

Receiver noise figure in dB relative to a noise temperature of 290 K, specified as a
scalar.

**Note**

This parameter specifies the noise contribution of the receiver
circuitry only. To add the effects of antenna noise, select
**Add 290K antenna noise**.

**Tunable:** Yes

#### Dependencies

This parameter applies when you set **Specification method** to `Noise
figure`.

**Data Types:** `double` | `single`

### **Noise factor** — Receiver noise factor `2` (default) | scalar

Receiver noise factor relative to a noise temperature of 290 K, specified
as a scalar.

**Note**

This parameter specifies the noise contribution of the receiver
circuitry only. To add the effects of antenna noise, select
**Add 290K antenna noise**.

**Tunable:** Yes

#### Dependencies

This parameter applies when you set **Specification method** to `Noise
factor`.

**Data Types:** `double` | `single`

### **Add 290K antenna noise** — Option to add 290 K antenna noise `off` (default) | `on`

Select this parameter to add 290 K antenna noise to the signal.

#### Dependencies

This parameter applies when you set **Specification method** to `Noise
factor` or `Noise
figure`.

### **Reference load (ohm)** — Reference load `1` (default) | scalar

Reference load value in ohms, specified as a scalar. This value is used to
compute the voltage levels based on the signal and noise power
levels.

**Tunable:** Yes

**Data Types:** `double` | `single`

### **Random number source** — Source for random number stream `Global stream` (default) | `mt19937ar with seed`

Source for random number stream, specified as `Global
stream` or `mt19937ar with
seed`.

### **Initial seed** — Initial seed value `67987` (default) | scalar

Initial seed value for the random number generator, specified as a
scalar.

#### Dependencies

This parameter applies when you set **Random
number source** to `mt19937ar with
seed`.

**Data Types:** `double` | `single`

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

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2023b: Multichannel input support

The `Receiver Thermal Noise`
System object™ accepts a matrix input baseband signal. Each column of the matrix
represents a baseband signal from one channel of a multi-antenna system.

### R2023b: Variable-size support

This support enables you to vary the length of input signal each time the block
executes in your simulation.

### R2023b: Random number generator update

The Receiver Thermal Noise block updates the random number generator (RNG)
source. You can now use the **Random number
source** parameter to select `Global stream` or
`mt19937ar with seed` as the RNG source. To use this block in a
For Each Subsystem (Simulink) you must set
**Random number source** to `Global
Stream`. This ensures that each run will generate independent noise
samples.

For simulations created before R2023b, the block defaults to legacy mode. In
legacy mode, the block uses the Random Source block to generate noise and random numbers are generated
using the Ziggurat method (V5 RANDN algorithm). The block reuses the same initial
seeds every time you rerun the simulation, so that this block outputs the same
signal each time you run a simulation.

To improve statistics when running simulations with pre-R2023b models that use the
Receiver Thermal Noise block, run **Update Model** and
convert the pre-R2023b model to use new the Receiver Thermal Noise block
capability.

### R2023b: Code Generation

Code generation is enabled by default. For more information, see **Simulate
using**.

### R2023b: Single data type support

If the input signal is of type single, then the block natively computes in single
precision, and the returned output is also of type single.

## Description

Apply receiver thermal noise to complex signal

The Receiver Thermal Noise block applies receiver thermal noise to a complex signal. The block
simulates the effects of thermal noise on a complex signal. The **Specification
method** parameter enables specification of the thermal noise based on the
noise temperature, noise figure, or noise factor.
