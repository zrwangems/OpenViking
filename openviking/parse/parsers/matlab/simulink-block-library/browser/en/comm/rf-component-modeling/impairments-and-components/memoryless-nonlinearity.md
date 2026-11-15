---
type: simulink-block
title: 'Memoryless Nonlinearity'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'memorylessnonlinearity'
documentation_source_path: 'ref/memorylessnonlinearity.html'
language: en
---

# Memoryless Nonlinearity

## Ports

### Input

### **In1** — Input RF baseband signal scalar | column vector

Input RF baseband signal, specified as a scalar or column
vector.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out1** — Output RF baseband signal scalar | column vector

Output RF baseband signal, returned as a scalar or column vector. The
output is of the same data type as the input.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main Tab

### **Model** — Amplifier nonlinearity model `cubic` (default) | `ampm` | `modified-rapp` | `saleh`

Specify the amplifier nonlinearity model as one of the following
methods:

- `cubic`
- `ampm`
- `modified-rapp`
- `saleh`

For more information, see Amplifier Model Methods.

### **Linear power gain (dB)** — Linear gain of amplifier `0` (default) | real scalar

Linear gain, specified as a scalar in dB.

#### Dependencies

To enable this parameter, set **Model** to `cubic` or
`modified-rapp`.

### **Type of Non-linearity** — Type of nonlinearity `OIP3` (default) | `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

Third-order nonlinearity type in dBm, specified as one of these options:

- `IIP3` — Input third-order intercept
  point
- `OIP3` — Output third-order intercept
  point
- `IP1dB` — Input 1 dB compression
  point
- `OP1dB` — Output 1 dB compression
  point
- `IPsat` — Input saturation point
- `OPsat` — Output saturation point

#### Dependencies

To enable this parameter, set **Model** to `cubic`.

### **IIP3 (dBm)** — Input third-order intercept point `Inf` (default) | real positive number

Input third-order intercept point, specified as a real positive number
in dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`IIP3`.

### **OIP3 (dBm)** — Output third-order intercept point `Inf` (default) | real positive number

Output third-order intercept point, specified as a real positive
number in dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`OIP3`.

### **IP1dB (dBm)** — Input 1 dB compression point `Inf` (default) | real positive number

Input 1 dB compression point, specified as a real positive number in
dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`IP1dB`.

### **OP1dB (dBm)** — Output 1 dB compression point `Inf` (default) | real positive number

Output 1 dB compression point, specified as a real positive number in
dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`OP1dB`.

### **IPsat (dBm)** — Input saturation point `Inf` (default) | real positive number

Input saturation point, specified as a real positive number in
dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`IPsat`.

### **OPsat (dBm)** — Output saturation point `Inf` (default) | real positive number

Output saturation point, specified as a positive real number in
dBm.

#### Dependencies

To enable this parameter, set **Model** to `cubic` and
**Type of Non-linearity** to
`OPsat`.

### **Lookup table (Pin(dBm), Pout(dBm), deg)** — Lookup table `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]` (default) | *M*-by-3 real matrix

Table lookup entries specified as a real *M*-by-3 matrix. The table
expresses the model output power dBm level in matrix column 2 and the
model phase change in degrees in matrix column 3 as related to the
absolute value of the input signal power of matrix column 1 for the
AM/AM-AM/PM model method. The column 1 input power must increase
monotonically.

#### Dependencies

To enable this parameter, set **Model** to `ampm`.

### **Output saturation level (V)** — Output saturation level `1` (default) | real positive number

Voltage output saturation level, specified as a real positive number
in dBm.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Magnitude smoothness factor** — Magnitude smoothness factor `2` (default) | real positive number

Magnitude smoothness factor for the AM/AM calculations of the modified
Rapp model method, specified as a positive real number.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase gain (rad)** — Phase gain `-0.45` (default) | real scalar

Phase gain for the AM/PM calculations of the modified Rapp model
method, specified as a real scalar in radians.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase saturation** — Phase saturation `0.88` (default) | real positive number

Phase saturation for the AM/PM calculations of the modified Rapp model
method, specified as a positive real number.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Phase smoothness factor** — Phase smoothness factor `3.43` (default) | positive scalar | positive two-element vector

Phase smoothness factor for the AM/PM calculations of the modified Rapp model method,
specified as a positive scalar or a positive two-element vector.

#### Dependencies

To enable this parameter, set **Model** to
`modified-rapp`.

### **Input scaling (dB)** — Scaling factor for input signal level `0` (default) | nonnegative real number

Scaling factor for input signal level for the Saleh model method,
specified as a nonnegative real number in dB.

#### Dependencies

To enable this parameter, set **Model** to `Saleh`.

### **AM / AM parameters [alpha beta]** — AM/AM conversion parameters `[ 2.1587, 1.1517 ]` (default) | two-element vector

AM/AM two-tuple conversion parameters for the Saleh model method,
specified as a two-element vector of nonnegative real numbers.

#### Dependencies

To enable this parameter, set **Model** to `saleh`.

### **AM / PM parameters [alpha beta]** — AM/PM conversion parameters `[ 4.0033, 9.1040 ]` (default) | two-element vector

AM/PM two-tuple conversion parameters for the Saleh model method, specified as a
two-element vector of real numbers.

#### Dependencies

To enable this parameter, set **Model** to `saleh`.

### **Output scaling (dB)** — Scaling factor for output signal level `0` (default) | nonnegative real number

Scaling factor for output signal level for the Saleh model method,
specified as nonnegative real number in dB.

#### Dependencies

To enable this parameter, set **Model** to `saleh`.

### **Reference load (ohm)** — Reference load `1` (default) | positive scalar

Reference load value in ohms, specified as a positive scalar. Use this
value to convert between the voltage levels and the signal and noise
power levels.

**Tunable:** Yes

### **Plot power characteristics** — Plot power characteristics button

This button plots the power characteristics based on the parameters
specified on the **Model** tab.

For more information, see Tips.

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

### R2024b: Memory Less Nonlinearity Block Updates

The block now permit a 2-element phase smoothness factor with independent
*q*1 and
*q*2 values for the modified Rapp model
method, as expressed in this equation.

FAM/PM(u)=Α|u|q11+(|u|B)q2

The block now permits negative values in the 2-element AM / PM conversion
parameter for the Saleh model method. This update enables you to express negative
phase rotation in the AM / PM impairment.

The values in the **Model**
parameter for Memoryless Nonlinearity block have been
renamed:

| Parameter | Values before R2024b | Values since R2024b |
| --- | --- | --- |
| **Model** | `Cubic polynomial` | `cubic` |
| `AM/AM - AM/PM` | `ampm` |
| `Modified Rapp` | `modified-rapp` |
| `Saleh` | `saleh` |

The default value for the **Type of
Non-linearity** parameter have been changed:

| Parameter | Default Values Before R2024b | Default Values Since R2024b |
| --- | --- | --- |
| **Type of Non-linearity** | `IIP3` | `OIP3` |

### R2023a: Modernize memoryless nonlinearity for amplifier modeling

The Memoryless Nonlinearity block updates the methods to apply memoryless nonlinearity
impairments when modeling an amplifier.

The block adds an AM/AM-AM/PM model that uses a lookup table to define the impairment
settings, modifies the parameters to apply the cubic polynomial model, and replaces
the Rapp model with the modified Rapp model. For amplifier model method details, see
Amplifier Model Methods.

These modeling methods are removed:

- Hyperbolic tangent model method
- Ghorbani model method
- AM/PM conversion settings of the cubic polynomial model method

To review the previous block interface, see (Legacy) Memoryless Nonlinearity
reference page.

## Description

Apply amplifier models to complex baseband signal

The Memoryless Nonlinearity block applies amplifier models to a complex baseband
signal. Use this block to model memoryless nonlinear impairments caused by signal
amplification in the radio frequency (RF) transmitter or receiver. For more information,
see Amplifier Model Methods.
