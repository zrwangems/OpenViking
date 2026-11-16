---
type: simulink-block
title: 'Antenna'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'antenna'
documentation_source_path: 'ref/antenna.html'
language: en
---

# Antenna

## Ports

### Input

### **RX** — Received signal scalar | vector | matrix | *m*-by-*n*-by-*k* array

Received signal, specified as a scalar, vector, matrix, or an array of size
*m*-by-*n*-by-*k*. In the
array:

- *m* — Represents the frame size
- *n* — Represents the number of interferers
- *k* — Represents horizontal or vertical polarization. The
  value of the *k* must be 2.

**Data Types:** `double`
### Output

### **TX** — Transmitted signal scalar | vector | matrix | *m*-by-*n*-by-*k* array

Transmitted signal, specified as a scalar, vector, matrix, or an array of size
*m*-by-*n*-by-*k*. IN the
array:

- *m* — Represents the frame size
- *n* — Represents the number of interferers
- *k* — Represents horizontal or vertical polarization. The
  value of the *k* must be 2.

**Data Types:** `double`

## Parameters

### Main

### **Source of antenna model** — Antenna model `Isotropic radiator` (default) | `Antenna Designer` | `Antenna object`

Antenna model, specified as one of the following:

- `Isotropic radiator`
- `Antenna Designer`
- `Antenna object`

**Note**

- To use `Antenna Designer` and
  `Antenna object` options you will need Antenna Toolbox™.

- Antenna block supports model
  protection and accelerator modes. When **Source of antenna
  model** is set to:

  - `Isotropic radiator` — Accelerator mode is
    supported.
  - `Antenna Designer` or `Antenna
    object` — Accelerator mode, rapid accelerator mode, model
    reference accelerator mode, and model protection are supported.

  For more information, see Enable Model Protection and Accelerator Modes in RF Blockset Models.  *(since R2024b)*

### **Create Antenna** — Open Antenna Toolbox Antenna Designer app button

Open the Antenna Designer app from the Antenna Toolbox to create an antenna.

#### Dependencies

To enable this parameter, set the **Source of antenna model**
to `Antenna Designer`.

### **Antenna object** — Antenna or array element input from workspace antenna catalog object | antenna array catalog object | `measuredAntenna` object | `pcbstack` object

Antenna or array element input from the workspace, specified as one of these objects:

- Antenna catalog — Use any one of the antenna objects from the Antenna Catalog (Antenna Toolbox).
- Array catalog — Use any one of the array objects from the Array Catalog (Antenna Toolbox). You
  can specify an array with a maximum of 65 ports.
- Measured antenna — Use
  `measuredAntenna` object to model a measured antenna or array
  characterized by its S-parameters and frequency-dependent far-field radiation
  pattern that includes both the polarization components. You can model an array
  with a maximum of 65 ports. *(since R2023b)*
- PCB stack — Use `pcbStack` (Antenna Toolbox) object to model a
  single-feed or multifeed PCB antenna.

**Note**

Analyze the antenna, array, or PCB stack objects in the workspace for at least
one frequency before using them in the block.

#### Dependencies

To enable this parameter, set **Source of antenna model** to
`Antenna object`.

### **Antenna Gain** — Antenna gain `0` `dBi` (default) | real scalar or vector | positive scalar or vector

Antenna gain, specified as real scalar or vector if you set units to
`dBi` or positive scalar or vector if you set units are
`None`. If the antenna gain is a vector, the vector length must be
equal to the vector length of **Incident carrier frequencies** and
**Radiated carrier frequencies**.

#### Dependencies

To enable this parameter, set **Source of antenna model** to
`Isotropic radiator` and check **Input incident
wave** or **Output radiated wave** or both

### **Impedance (Ohm)** — Input impedance `50` (default) | complex-valued scalar or vector

Input impedance, specified as a complex-valued scalar or vector in ohms. If the
impedance is a vector, the vector length must be equal to the length of
**Incident carrier frequencies** and **Radiated carrier
frequencies**.

#### Dependencies

To enable this parameter, set **Source of antenna model** to
`Isotropic radiator`.

**Data Types:** `double`
**Complex Number Support:** Yes

### **Input incident wave** — Input incident wave for simulating receiving antenna `'off'` (default) | `'on'`

Select this parameter if you want to simulate a receiving antenna.

### **Output radiated wave** — Output radiated wave for transmitting antenna `'on'` (default) | `'off'`

Select this parameter if you want a simulate a transmitting antenna.

### **Incident carrier frequencies** — Carrier frequencies for receiving signal `2.1` `GHz` (default) | nonnegative scalar or row vector

Carrier frequencies for a receiving signal, specified as a nonnegative scalar in
hertz or a row vector with each element unit in hertz. If the value of
**Antenna gain** or **Impedance** is a vector,
then the values of **Incident carrier frequencies** and
**Radiated carrier frequencies** must be identical.

#### Dependencies

To enable this parameter, select **Input incident
wave**.

### **Radiated carrier frequencies** — Carrier frequencies for transmitting signal `2.1` `GHz` (default) | nonnegative scalar or row vector

Carrier frequencies for a transmitting signal, specified as a nonnegative scalar
in hertz or a row vector with each element unit in hertz. If the value of
**Antenna gain** or **Impedance** is a vector,
then the values of **Incident carrier frequencies** and
**Radiated carrier frequencies** must be identical.

#### Dependencies

To enable this parameter, select **Output radiated
wave**.

### **Direction of departure** — Azimuth and elevation angles towards which output signal power wave radiates `[0 0]` `deg` (default) | finite real row vector of length 1-by-2 | finite real matrix of length *m*-by-2

Azimuth and elevation angles towards which the output signal power wave radiates,
specified as a finite real row vector of length 1-by-2 or finite real matrix of length *m*-by-2 *(since R2023a)* with each element
unit in degrees or radians. *m* is an integer between in the range
[2, 100].

#### Dependencies

To enable this parameter, set **Source of antenna model** to
`Antenna Designer` or `Antenna
object` and select **Output radiated
wave**.

### **Direction of arrival** — Azimuth and elevation angles from which input signal power wave arrives `[180 0]` `deg` (default) | finite real row vector of length 1-by-2 | finite real matrix of length *m*-by-2

Azimuth and elevation angles towards which the input signal power wave arrives,
specified as a finite real row vector of length 1-by-2 or finite real matrix of length *m*-by-2 *(since R2023a)* with each element
unit in degrees or radians. *m* is an integer between in the range
[2, 100].

#### Dependencies

To enable this parameter, set **Source of antenna model** to
`Antenna Designer` or `Antenna
object` and select **Input incident wave**.

### **Simulate noise** — Simulate thermal noise `'on'` (default) | `'off'`

Select this parameter to simulate thermal noise in the antenna due to the real
part of the impedance see at the antenna terminals. You must select **Simulate
noise** in the Configuration block also.

### **Ground and hide negative terminals** — Ground RF circuit terminals `'on'` (default) | `'off'`

Select this option to ground and hide the negative terminals. Clear this parameter
to expose the negative terminals. By exposing these terminals, you can connect them to
other parts of your model.

### Modeling

### **Modeling options** — Model frequency-dependent antenna parameters `Time domain` (default) | `Frequency domain`

Model frequency-dependent antenna parameters, specified as:

- `Time domain` — This technique creates an
  analytical rational model that approximates the whole range of the data.
- `Frequency domain` — This technique computes the
  baseband impulse response for each carrier frequency independently. This
  technique is based on convolution. There is an option to specify the duration of
  the impulse response. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.

The frequency-dependent parameters are:

- Antenna impedance — The input impedance at the antenna terminals. This is
  used in RF system simulation.
- Normalized vector effective length — A property used that ties between the
  current flowing at the antenna terminals and the radiated far-field at a given
  direction. Due to reciprocity, the effective length also ties between the
  incident field and the induced open-circuit voltage on the antenna
  terminals.

#### Dependencies

To set source **Source of antenna model** of
`Antenna Designer` or `Antenna
object` to activate the **Modeling** Tab that
contains the **Modeling options** parameters.

### **Relative error desired (dB)** — Relative error acceptable for the rational fit `-40` (default) | scalar

Relative error acceptable for the rational fit, specified as a scalar. Applies to
time domain modeling of both antenna impedance and normalized vector effective length.
The corresponding rational fitting results for each property are displayed on the
block mask.

#### Dependencies

To enable this property, set **Modeling options** to
`Time domain`.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response `'on'` | `'off'`

Select this parameter to automatically calculate the impulse response duration.
Clear this parameter to manually specify the impulse response duration using
**Impulse response duration**. Applies to frequency-domain modeling
of both antenna impedance and normalized vector effective length.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain`.

### **Impulse response duration** — Impulse response duration `1e-10``s` (default) | scalar

Impulse response duration, specified as a scalar. Applies to frequency-domain
modeling of both antenna impedance and normalized vector effective length.

#### Dependencies

To set this parameter, first select `Frequency domain`
in **Modeling options**. Then, clear **Automatically
estimate impulse response duration**.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2024b: `Time domain (rationalfit)` parameter renamed

The `Time domain (rationalfit)` parameter value in the
**Modeling options** parameter has been renamed to `Time
domain` in the Antenna block.

When you open a model created before R2024b containing an Antenna block,
the parameter name displays as `Time domain`.

### R2024b: Enable model protection and accelerator modes in Antenna block

The Antenna block now supports these features:

- Model protection: Conceal the contents of your model by creating a protected model
  in the SLXP file format.
- Rapid accelerator and model reference accelerator simulation modes: These
  accelerator modes enhance simulation speed by generating an executable for your model.
  The degree of speedup varies based on the model.

**Note**

The Antenna block only supports model protection and accelerator modes when the
**Source of antenna model** parameter is set to `Antenna
Designer` or `Antenna object`.

### R2023b: Model antenna using `measuredAntenna` object

The Antenna block in the Circuit Envelope library now supports the
`measuredAntenna` object. Specify this object to model a measured antenna
or array characterized by its S-parameters and frequency-dependent far-field radiation
pattern that includes both the polarization components.

### R2023a: Multiple directions of arrival and departure in Antenna block

You can now use the Antenna block to transmit and receive signals in
multiple directions using the **Direction of arrival** and
**Direction of departure** properties.

### R2022a: Model transmit and receive antenna array

To model a transmit and receive antenna, specify an antenna array from the Array Catalog (Antenna Toolbox) in the
**Antenna
object** parameter.

### R2021b: Antenna block icon updated

The Antenna block icon was updated in R2021b. The block icon is now
dynamic and shows the current state of the noise parameter.

When you open a model created before R2021b containing an Antenna block,
the software replaces the block icon with the R2021b version.

## Description

Model antenna or antenna array accounting for incident power wave (RX) and radiated power wave (TX)

Model an antenna or antenna array using the Antenna block. Use this block to:

- Convert a Simulink® input of an incident power wave vector into RF Blockset™ voltage signal at the antenna or antenna array ports.
- Convert current at RF Blockset antenna or antenna array ports to a Simulink output of a radiated power wave vector.
- Introduce antenna impedance into an RF system.

By default, the antenna block is an isotropic radiator producing a Simulink output signal. For an isotropic radiator, specify the gain and impedance of the
antenna in the block parameters. The **Radiated carrier frequencies**
parameter is a set of carrier frequencies over-which the Antenna block creates
the radiated power wave. For more information, see Radiated Wave and Incident Wave.

The Antenna block mask icons are dynamic: The icons show the current state
of the noise parameter, indicate if you have specified an `antennaarray` object
in the **Antenna object**
parameter, and update the number of ports based on the number of elements in the
`antennaarray` object. This table shows how the block icons vary based on the
state of the **Simulate noise**
and **Antenna object**
parameters.

| Antenna object | Simulate noise: `on` | Simulate noise: `off` |
| --- | --- | --- |
| Antenna Catalog Objects | Antenna block icon with Simulate noise is set to on. | Antenna block icon with Simulate noise is set to off. |
| Antenna Array Catalog Objects | Antenna block icon with four-element antenna array as input and Simulate noise is set to on. | Antenna block icon with four-element antenna array as input and Simulate noise is set to off. |
