---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'amplifieridealizedbaseband'
documentation_source_path: 'ref/amplifieridealizedbaseband.html'
language: en
---

# Amplifier

## Ports
```yaml
ports:
- name: Port_1
  summary: Input baseband signal real scalar | real column | complex scalar | complex column
  direction: input
  data_types: double | single
- name: Port_1
  summary: Output baseband signal real scalar | real column | complex scalar | complex column
  direction: output
  data_types: double | single
```

### Input

### **Port\_1** — Input baseband signal real scalar | real column | complex scalar | complex column

Input baseband signal, specified as a real scalar, real column, complex scalar, or
complex column.

**Data Types:** `double` | `single`
### Output

### **Port\_1** — Output baseband signal real scalar | real column | complex scalar | complex column

Output baseband signal, specified as a real scalar, real column, complex scalar, or
complex column. The output port mimics the properties of the input port. For example, if the
input baseband signal is specified as a real scalar with a data type double, then the output
baseband signal is also specified as a real signal with the data type double.

**Data Types:** `double` | `single`
## Parameters
```yaml
parameters:
- name: Model
  summary: Amplifier nonlinearity model cubic (default) | ampm | modified-rapp | saleh
  group: Main Tab
- name: Linear power gain (dB)
  summary: Linear gain of amplifier 0 (default) | real scalar
  group: Main Tab
- name: Type of Non-Linearity
  summary: Third - order nonlinearity type OIP3 (default) | IIP3 | IP1dB | OP1dB | IPsat | OPsat
  group: Main Tab
- name: IIP3 (dBm)
  summary: Input third-order intercept point Inf (default) | real positive number
  group: Main Tab
- name: OIP3 (dBm)
  summary: Output third-order intercept point Inf (default) | real positive number
  group: Main Tab
- name: IP1dB (dBm)
  summary: Input 1 dB compression point Inf (default) | real positive number
  group: Main Tab
- name: OP1dB (dBm)
  summary: Output 1 dB compression point Inf (default) | real positive number
  group: Main Tab
- name: IPsat (dBm)
  summary: Input saturation point Inf (default) | real positive number
  group: Main Tab
- name: OPsat (dBm)
  summary: Output saturation point Inf (default) | real positive number
  group: Main Tab
- name: Simulate using
  summary: Specify type of simulation to run Code generation (default) | Interpreted execution
  group: Main Tab
- name: Plot power characteristics
  summary: Plot power characteristics button (default)
  group: Main Tab
- name: Lookup table (Pin(dBm), Pout(dBm), deg)
  summary: Lookup table [ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ] (default) | *M*-by-3 real matrix
  group: Main Tab
- name: Output saturation level (V)
  summary: Output saturation level 1 (default) | real positive number
  group: Main Tab
- name: Magnitude smoothness factor
  summary: Magnitude smoothness factor 2 (default) | real positive number
  group: Main Tab
- name: Phase gain (rad)
  summary: Phase gain -0.45 (default) | real scalar
  group: Main Tab
- name: Phase saturation
  summary: Phase saturation 0.88 (default) | real positive number
  group: Main Tab
- name: Phase smoothness factor
  summary: Phase smoothness factor [3.43, 3.43] (default) | real positive number | two-tuple vector
  group: Main Tab
- name: Input scaling (dB)
  summary: Scaling factor for input signal level 0 (default) | nonnegative real number
  group: Main Tab
- name: AM / AM parameters [alpha beta]
  summary: AM/AM conversion parameters [ 2.1587, 1.1517 ] (default) | two-element vector
  group: Main Tab
- name: AM / PM parameters [alpha beta]
  summary: AM/PM conversion parameters [ 4.0033, 9.1040 ] (default) | two-element vector
  group: Main Tab
- name: Output scaling (dB)
  summary: Scaling factor for output signal level 0 (default) | nonnegative real number
  group: Main Tab
- name: Include Noise
  summary: Add noise to system off (default) | on
  group: Noise Tab
- name: Specify noise type
  summary: Noise representation NF (default) | noise-temperature | noise-factor
  group: Noise Tab
- name: Noise temperature (K)
  summary: Noise temperature to model noises in amplifier 290 (default) | nonnegative real number
  group: Noise Tab
- name: Noise figure (dB)
  summary: Noise figure to model noise in amplifier 10 * log10( 2 ) (default) | nonnegative real number
  group: Noise Tab
- name: Noise factor
  summary: Noise factor to model noise in amplifier 2 (default) | positive integer scalar greater than or equal to 1
  group: Noise Tab
- name: Seed source
  summary: Source of initial seed auto (default) | user
  group: Noise Tab
- name: Seed
  summary: Seed for random number generator 67987 (default) | nonnegative integer
  group: Noise Tab
```

### Main Tab

### **Model** — Amplifier nonlinearity model `cubic` (default) | `ampm` | `modified-rapp` | `saleh`

Specify the amplifier nonlinearity model as one of the following:

- `cubic` — The cubic polynomial model uses linear power gain
  to determine the linear coefficient of a third-order polynomial and either IP3, P1dB, or
  Psat to determine the third - order coefficient of the polynomial.
- `ampm` — The AM/AM-AM/PM model uses a lookup table to
  calculate the amplifier power characteristics.
- `modified-rapp` — The modified Rapp uses a normalized
  transfer function to calculate the amplifier power characteristics.
- `saleh` — The Saleh model also uses a normalized transfer
  function to calculate the amplifier power characteristics.

For more information, see Nonlinearity Models in Idealized Amplifier Block.

### **Linear power gain (dB)** — Linear gain of amplifier `0` (default) | real scalar

Linear gain, specified as a scalar in dB.

### **Type of Non-Linearity** — Third - order nonlinearity type `OIP3` (default) | `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

Third order nonlinearity type, specified as `IIP3`,
`OIP3`, `IP1dB`, `OP1dB`,
`IPsat`, or `OPsat`.

### **IIP3 (dBm)** — Input third-order intercept point `Inf` (default) | real positive number

Input third-order intercept point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `IIP3`.

### **OIP3 (dBm)** — Output third-order intercept point `Inf` (default) | real positive number

Output third-order intercept point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `OIP3`.

### **IP1dB (dBm)** — Input 1 dB compression point `Inf` (default) | real positive number

Input 1 dB compression point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `IP1dB`.

### **OP1dB (dBm)** — Output 1 dB compression point `Inf` (default) | real positive number

Output 1 dB compression point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `OP1dB`.

### **IPsat (dBm)** — Input saturation point `Inf` (default) | real positive number

Input saturation point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `IPsat`.

### **OPsat (dBm)** — Output saturation point `Inf` (default) | real positive number

Output saturation point, specified as a positive real number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`cubic` and **Type of Non-Linearity**
to `OPsat`.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` – Simulate model using generated C code.
  The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional startup
  time, but the speed of the subsequent simulations is faster than `Interpreted
  execution`.
- `Interpreted execution` – Simulate model using the
  MATLAB® interpreter. This option shortens startup time speed, but the speed of the
  subsequent simulations is slower than `Code generation`. In this
  mode, you can debug the source code of the block.

### **Plot power characteristics** — Plot power characteristics button (default)

This button plots the power characteristics based on the parameters specified on the
**Main** tab.

For more information, see Plot Power Characteristics.

### **Lookup table (Pin(dBm), Pout(dBm), deg)** — Lookup table `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]` (default) | *M*-by-3 real matrix

Table lookup entries specified as a real *M*-by-3 matrix. This table
expresses the model output power dBm level in matrix column 2 and the model phase change in
degrees in matrix column 3 as related to the absolute value of the input signal power of
matrix column 1 for the AM/AM - AM/PM model. The column 1 input power must increase
monotonically.

The `interp1` function with the `linear` method is
employed to extrapolate and interpolate the data points specified in the lookup table.
Furthermore, for extrapolating input data points that are less than the smallest specified
input power value in the lookup table, the AM/AM extrapolation uses a slope of 1 and constant
phase value equal to the phase of the smallest input power.

#### Dependencies

To enable this parameter, set **Model** to
`ampm`.

### **Output saturation level (V)** — Output saturation level `1` (default) | real positive number

Voltage output saturation level, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Magnitude smoothness factor** — Magnitude smoothness factor `2` (default) | real positive number

Magnitude smoothness factor for the `modified-rapp` amplifier
model AM/AM calculations, specified as a positive real number.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase gain (rad)** — Phase gain `-0.45` (default) | real scalar

Phase gain for the `modified-rapp` amplifier model AM/PM
calculations, specified as a real scalar in radians.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase saturation** — Phase saturation `0.88` (default) | real positive number

Phase saturation for the `modified-rapp` amplifier model AM/PM
calculations, specified as a positive real number.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase smoothness factor** — Phase smoothness factor `[3.43, 3.43]` (default) | real positive number | two-tuple vector

Phase smoothness factor for the `modified-rapp` amplifier model
AM/PM calculations, specified as a positive real number or two-tuple vector.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Input scaling (dB)** — Scaling factor for input signal level `0` (default) | nonnegative real number

Scaling factor for input signal level for the `saleh` amplifier
model, specified as a nonnegative real number in dB.

#### Dependencies

To enable this parameter, set **Model** to
`saleh`.

### **AM / AM parameters [alpha beta]** — `AM/AM` conversion parameters `[ 2.1587, 1.1517 ]` (default) | two-element vector

AM/AM two-tuple conversion parameters for `saleh` amplifier
model, specified as a two-element vector of nonnegative real numbers.

#### Dependencies

To enable this parameter, set **Model** to
`saleh`.

### **AM / PM parameters [alpha beta]** — `AM/PM` conversion parameters `[ 4.0033, 9.1040 ]` (default) | two-element vector

`AM/PM` two-tuple conversion parameters for
`saleh` amplifier model, specified as a two-element vector of
nonnegative real numbers.

#### Dependencies

To enable this parameter, set **Model** to
`saleh`.

### **Output scaling (dB)** — Scaling factor for output signal level `0` (default) | nonnegative real number

Scaling factor for output signal level for `saleh` amplifier
model, specified as nonnegative real number in dB.

#### Dependencies

To enable this parameter, set **Model** to
`saleh`.

### Noise Tab

### **Include Noise** — Add noise to system `off` (default) | `on`

Select this parameter to add system noise to the input signal. Once you select this
parameter, the parameters associated with the **Noise** tab are
displayed.

### **Specify noise type** — Noise representation `NF` (default) | `noise-temperature` | `noise-factor`

Type of noise, specified as one of the following:

- `noise-temperature` — Noise temperature
- `NF` — Noise figure
- `noise-factor` — Noise factor

For more information, see Thermal Noise Simulations in Idealized Amplifier Block.

#### Dependencies

To enable this parameter, select **Include Noise**.

### **Noise temperature (K)** — Noise temperature to model noises in amplifier `290` (default) | nonnegative real number

Noise temperature to model noise in the amplifier, specified as a nonnegative real
number in degrees (K).

#### Dependencies

To enable this parameter, select **Include Noise** and set
**Specify noise type** to
`noise-temperature`.

### **Noise figure (dB)** — Noise figure to model noise in amplifier `10 * log10( 2 )` (default) | nonnegative real number

Noise figure to model noise in the amplifier, specified as a nonnegative real number in
dB.

#### Dependencies

To enable this parameter, select **Include Noise** and set
**Specify noise type** to
`NF`.

### **Noise factor** — Noise factor to model noise in amplifier `2` (default) | positive integer scalar greater than or equal to 1

Noise factor to model noise in the amplifier, specified as a positive integer scalar
greater than or equal to 1.

#### Dependencies

To enable this parameter, select **Include Noise** and set
**Specify noise type** to
`noise-factor`.

### **Seed source** — Source of initial seed `auto` (default) | `user`

Source of initial seed used to prepare the Gaussian random number noise generator,
specified as one of the following:

- `auto` - When **Seed source** is set to
  `auto`, seeds for each amplifier instance are generated using a
  random number generator. The reset method of the instance has no effect.
- `user` - When **Seed source** is set to
  `user`, the value provided in the **Seed** is used to
  initialize the random number generator and the reset method resets the random number
  generator using the **Seed** property value.

### **Seed** — Seed for random number generator `67987` (default) | nonnegative integer

Seed for the random number generator, specified as a nonnegative integer less than
232. Use this value to initialize the random number
generator.

#### Dependencies

To enable this parameter, click **Include Noise** check box
and choose `user` in the **Seed source**
parameter.
## Libraries

RF Blockset / Idealized Baseband

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024b: Parameters of Amplifier block from idealized baseband library have been renamed

The following parameter values in the Amplifier block in the idealized
baseband library have been renamed:

| Parameter | Values before R2024b | Values since R2024b |
| --- | --- | --- |
| **Model** | `Cubic polynomial` | `cubic` |
| `AM/AM - AM/PM` | `ampm` |
| `Modified Rapp` | `modified-rapp` |
| `Saleh` | `saleh` |
| **Specify noise type** | `Noise figure` | `NF` |
| `Noise temperature` | `noise-temperature` |
| `Noise factor` | `noise-factor` |
| **Seed source** | `Auto` | `auto` |
| `User specified` | `user` |

The following default values in the Amplifier block in the idealized
baseband library have been changed:

| Parameter | Default Values Before R2024b | Default Values Since R2024b |
| --- | --- | --- |
| **Type of Non-linearity** | `IIP3` | `OIP3` |
| **Specify noise type** | `Noise temperature` | `NF` |

When you open a model created before R2024b containing the Amplifier block,
the software replaces the parameter names and values as shown in the table.

## Description

Complex baseband model of amplifier with noise and nonlinearities

The Amplifier block generates a complex baseband model of an amplifier with thermal noise.
This block provides four nonlinearity models and three options to specify noise
representation.
