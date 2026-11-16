---
type: simulink-block
title: 'Memoryless Nonlinearity'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Other'
documentation_page: 'legacymemorylessnonlinearity'
documentation_source_path: 'ref/legacymemorylessnonlinearity.html'
language: en
---

# Memoryless Nonlinearity

## Ports

### Input

### **In1** — Input RF baseband signal scalar | column vector

Input RF baseband signal, specified as a scalar or column vector.
Values in this input must be complex.

**Data Types:** `double`
**Complex Number Support:** Yes
### Output

### **Out1** — Output RF baseband signal scalar | column vector

Output RF baseband signal, returned as a scalar or column vector. The
output is of the same data type as the input.

## Parameters

### **Method** — Nonlinearity modeling method `Cubic polynomial` (default) | `Hyperbolic tangent` | `Saleh model` | `Ghorbani model` | `Rapp model`

Nonlinearity modeling method, specified as `Cubic
polynomial`, `Hyperbolic tangent`,
`Saleh model`, `Ghorbani model`,
`Rapp model`, or `Lookup table`. For
more information, see Memoryless Nonlinear Impairments.

### **Linear gain (dB)** — Linear gain `0` (default) | scalar

Linear gain in decibels, specified as a scalar. This parameter scales the
power gain of the output signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Cubic polynomial`,
`Hyperbolic tangent`, or `Rapp
model`.

### **IIP3 (dBm)** — Third-order input intercept point `30` (default) | scalar

Third-order input intercept point in dBm, specified as a scalar.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Cubic polynomial` or
`Hyperbolic tangent`.

### **AM/PM conversion (degrees per dB)** — AM/PM conversion factor `10` (default) | scalar

AM/PM conversion factor in degrees per decibel, specified as a scalar. For
more information, see Cubic Polynomial and Hyperbolic Tangent Model Methods.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Cubic polynomial` or
`Hyperbolic tangent`.

### **Lower input power limit for AM/PM conversion (dBm)** — Input power lower limit `10` (default) | scalar

Input power lower limit in dBm, specified as a scalar less than the **Upper input
power limit for AM/PM conversion (dBm)** parameter value. The
AM/PM conversion scales linearly for input power values in the range
[**Lower input power limit for AM/PM conversion
(dBm)**, **Upper input power limit for AM/PM conversion
(dBm)**]. If the input signal power is below the input power
lower limit, the phase shift resulting from AM/PM conversion is zero. For
more information, see Cubic Polynomial and Hyperbolic Tangent Model Methods.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Cubic polynomial` or
`Hyperbolic tangent`.

### **Upper input power limit for AM/PM conversion (dBm)** — Input power upper limit `inf` (default) | scalar

Input power upper limit in dBm, specified as a scalar greater than the **Lower
input power limit for AM/PM conversion (dBm)** parameter value.
The AM/PM conversion scales linearly for input power values in the range
[**Lower input power limit for AM/PM conversion
(dBm)**, **Upper input power limit for AM/PM conversion
(dBm)**]. If the input signal power is below the input power
lower limit, the phase shift resulting from AM/PM conversion is zero. For
more information, see Cubic Polynomial and Hyperbolic Tangent Model Methods.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Cubic polynomial` or
`Hyperbolic tangent`.

### **Input scaling (dB)** — Input signal scaling factor `0` (default) | scalar

Input signal scaling factor in decibels, specified as a scalar. This
parameter scales the power gain of the input signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Saleh model` or
`Ghorbani model`.

### **AM/AM parameters [alpha beta]** — AM/AM parameters for Saleh model `[2.1587 1.1517]` (default) | two-element vector

AM/AM parameters for Saleh model, used to compute the amplitude gain for an input signal,
specified as a two-element vector. For more information, see Saleh Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Saleh model`.

### **AM/PM parameters [alpha beta]** — AM/PM parameters for Saleh model `[4.0033 9.1040]` (default) | two-element vector

AM/PM parameters for Saleh model, used to compute the phase change for an input signal,
specified as a two-element vector. For more information, see Saleh Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Saleh model`.

### **AM/AM parameters [x1 x2 x3 x4]** — AM/AM parameters for Ghorbani model `[8.1081 1.5413 6.5202 -0.0718]` (default) | four-element vector

AM/AM parameters for Ghorbani model, used to compute the amplitude gain for an input
signal, specified as a four-element vector. For more information, see Ghorbani Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Ghorbani model`.

### **AM/PM parameters [y1 y2 y3 y4]** — AM/PM parameters for Ghorbani model `[4.6645 2.0965 10.88 -0.003]` (default) | four-element vector

AM/PM parameters for Ghorbani model, used to compute the phase change for an input
signal, specified as a four-element vector. For more information, see Ghorbani Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Ghorbani model`.

### **Output scaling (dB)** — Output signal scaling factor `0` (default) | scalar

Output signal scaling factor in decibels, specified as a scalar. This
parameter scales the power gain of the output signal.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Saleh model` or
`Ghorbani model`.

### **Smoothness factor** — Smoothness factor `0.5` (default) | scalar

Smoothness factor, specified as a scalar. For more information, see Rapp Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Rapp model`.

### **Output saturation level** — Output saturation level `1` (default) | scalar

Output saturation level, specified as a scalar. For more information, see
Rapp Model Method.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the **Method** to `Rapp model`.

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

### R2025a: This legacy interface has been removed

The (Legacy) Memoryless Nonlinearity
block has been removed. To apply memoryless nonlinearity to a complex baseband
signal, use the Memoryless Nonlinearity block.

### R2024a: This legacy interface will not be supported

In R2023a, the Memoryless Nonlinearity block updates the
methods for applying memoryless nonlinearity impairments in amplifier models. To
load the updated version of the block, run **Update Model** on
pre-R2023a simulations that use the (Legacy) Memoryless Nonlinearity block.

### R2023a: This legacy interface will not be supported

In R2023a, the Memoryless Nonlinearity block updates the
methods for applying memoryless nonlinearity impairments in amplifier models. The
block with the legacy interface runs without warning but you are encouraged use the
updated block. To load the updated version of the block, run **Update
Model** on pre-R2023a simulations that use the
(Legacy) Memoryless Nonlinearity block.

The updated block removes the Hyperbolic tangent and Ghorbani methods, replaces
the Rapp method with the modified Rapp method, modifies the parameters to apply the
cubic polynomial method, and adds an AM/AM-AM/PM method that uses a lookup table to
define the impairment settings. For the new interface, see the Memoryless Nonlinearity reference page.

## Description

(Removed) Apply memoryless nonlinearity to complex baseband signal

The (Legacy) Memoryless Nonlinearity block applies memoryless nonlinear impairments to a complex baseband
signal. Use this block to model memoryless nonlinear impairments caused by signal
amplification in the radio frequency (RF) transmitter or receiver. For more information,
see Memoryless Nonlinear Impairments.

**Note**

All values of power assume a nominal impedance of 1 ohm.
