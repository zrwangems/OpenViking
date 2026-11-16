---
type: simulink-block
title: 'SaturatingAmplifier'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'saturatingamplifier'
documentation_source_path: 'ref/saturatingamplifier.html'
language: en
---

# SaturatingAmplifier

## Ports

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal, can be a sample-by-sample signal specified as a scalar, or
an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Clipped output voltage scalar | vector

Clipped output voltage, as specified by the SaturatingAmplifier
block. If the input signal is a sample-by-sample signal specified as a scalar, the
output is also scalar. If the input signal is an impulse response vector signal, the
output is also a vector.

**Data Types:** `double`

## Parameters

### **Mode** — Amplifier operating mode `On` (default) | `Off`

Amplifier operating mode:

- `Off` — SaturatingAmplifier is bypassed and
  the input waveform remains unchanged.
- `On` — SaturatingAmplifier scales the input
  waveform according to a voltage in vs. voltage out response.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current saturating
  amplifier operating **Mode**.
- Use `set_param(gcb,'Mode',value)` to set amplifier to a
  specific **Mode**.

### **Specification** — Input specification for limiting amplifier output `'Limit and Linear Gain'` (default) | `'VinVout'`

Input specification for limiting amplifier output:

- `'Limit and Linear Gain'` — Creates a soft clipping
  voltage in vs. voltage out response with the values specified in
  **Limit** and **Linear Gain**.
- `'VinVout'` — Generates output voltages corresponding
  to input voltage specified in **VinVout**. The block maps the
  input voltage to the output voltages using a memoryless nonlinearity response. If
  any input voltage point falls outside the specified values, the output for that
  particular input voltage is interpolated.

#### Programmatic Use

- Use `get_param(gcb,'Specification')` to view the current
  **Specification** of saturating amplifier.
- Use `set_param(gcb,'Specification',value)` to set
  saturating amplifier to a specific **Specification**.

**Data Types:** `char`

### **Limit** — Clipping voltage for the limiting amplifier `1.2` (default) | real positive scalar

Clipping voltage for the limiting amplifier, specified as a real positive scalar in
V.

#### Dependencies

This parameter is only available when **Specification** is
selected as `'Limit and Linear Gain'`.

#### Programmatic Use

- Use `get_param(gcb,'Limit')` to view the current value of
  **Limit** of saturating amplifier.
- Use `set_param(gcb,'Limit',value)` to set
  **Limit** to a specific value.

**Data Types:** `double`

### **LinearGain** — Amplifier gain in the linear region `1` (default) | real positive scalar

Amplifier gain in the linear region, specified as a unitless real positive
scalar.

#### Dependencies

This parameter is only available when **Specification** is
selected as `'Limit and Linear Gain'`.

#### Programmatic Use

- Use `get_param(gcb,'LinearGain')` to view the current value
  of **LinearGain** of saturating amplifier.
- Use `set_param(gcb,'LinearGain',value)` to set
  **LinearGain** to a specific value.

**Data Types:** `double`

### **VinVout** — Input and corresponding output voltage responses *N*×2 matrix | *N*×2×*M* matrix

Input and corresponding output voltage responses, specified as an
*N*×2 matrix (2-D) or *N*×2×*M*
matrix (3-D) in volts. *N* is the number of voltage samples and
*M* is the number of slices.

If **VinVout** is a 3-D matrix, you can select which slice of the
**VinVout** is to use. To know more about defining 3-D
**VinVout** matrix, see Define Saturating Amplifier with 3D VinVout Matrix.

#### Dependencies

This parameter is only available when **Specification** is
selected as `'VinVout'`.

#### Programmatic Use

- Use `get_param(gcb,'VinVout')` to view the current
  **VinVout** table value of saturating amplifier.
- Use `set_param(gcb,'VinVout',value)` to set
  **VinVout** to a specific value.

**Data Types:** `double`

### **Slice select** — Select which corner of 3D GPZ matrix to use `0` (default) | nonegative scalar integer

Select which slice, family, or corner of a 3-D `VinVout` matrix to
use during CTLE configuration.

You must set the **Specification** parameter to
`'VinVout'` to effectively use the **Slice
Select** parameter. Depending on how many slices are available in your
`VinVout` matrix, you can then select the slice you are interested in
from a zero-based index available from the dropdown menu.

#### Programmatic Use

- Use `get_param(gcb,'SliceSelect')` to view the current
  value of **Slice select**.
- Use `set_param(gcb,'SliceSelect',value)` to set
  **Slice select** to a specific value.

**Data Types:** `double`

### **Visualize Response** — Plot input vs output voltage response button

Click to plot the input vs. output voltage response of the Saturating
Amplifier block.

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file. If
you deselect **Mode**, it is removed from the AMI files, effectively
hard-coding **Mode** to its current value.

### **Slice select** — Include Slice select parameter in IBIS-AMI model on (default) | off

Select to include **Slice select** as a parameter in the IBIS-AMI
file. If you deselect **Slice select**, it is removed from the AMI
files, effectively hard-coding **Slice select** to its current
value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

### R2023b: Slice Select

you can now select which slice, family, or corner of a 3-D GPZ matrix to use during CTLE
configuration.

## Description

Models a saturation amplifier

The SaturatingAmplifier block scales the input waveform according to a
voltage in vs. voltage out response. The voltage in vs. voltage out response is specified
either by the soft clipping response defined by **Limit** and
**Linear Gain**, or by the **VinVout**  matrix. The
SaturatingAmplifier block applies memoryless nonlinearity to incoming
waveform.
