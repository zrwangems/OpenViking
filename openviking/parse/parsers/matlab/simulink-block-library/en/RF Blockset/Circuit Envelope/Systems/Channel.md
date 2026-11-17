---
type: simulink-block
title: 'Channel'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Systems'
documentation_page: 'channel'
documentation_source_path: 'ref/channel.html'
language: en
---

# Channel

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Source of channel model
  summary: Channel source Isotropic free-space (default) | Ray-tracing
  group: Main
- name: Antenna gain
  summary: Gain of transmitter antenna 0 dBi (default) | real scalar or vector | positive scalar or vector
  group: Main
- name: Impedance (Ohm)
  summary: Input impedance of transmitter antenna 50 (default) | complex scalar or vector
  group: Main
- name: Antenna gain
  summary: Gain of receiver antenna 0 dBi (default) | real scalar or vector | positive scalar or vector
  group: Main
- name: Impedance (Ohm)
  summary: Input impedance of receiver antenna 50 (default) | complex scalar or vector
  group: Main
- name: Path loss
  summary: Free-space path loss 10 dB (default) | real scalar or vector | positive scalar or vector
  group: Main
- name: Path delay
  summary: Free-space path delay 0 s (default) | nonnegative scalar
  group: Main
- name: Map
  summary: Map for visualization or surface data "none" (default) | siteviewer object | triangulation object | string scalar
    | character vector
  group: Main
- name: Propagation model
  summary: Propagation model 'raytracing' (default) | RayTracing object
  group: Main
- name: Tx site
  summary: Transmitter site txsite object | array of txsite objects
  group: Main
- name: Rx site
  summary: Receiver site rxsite object
  group: Main
- name: View Site
  summary: Display RF propagation scenarios button
  group: Main
- name: Carrier frequencies
  summary: Carrier frequencies of channel 2.1 GHz (default) | nonnegative scalar or row vector
  group: Main
- name: Simulate noise
  summary: Simulate thermal noise 'on' (default) | 'off'
  group: Main
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals 'on' (default) | 'off'
  group: Main
- name: Edit System
  summary: Edit or expand channel block button
  group: Main
- name: Modeling options
  summary: Technique to model frequency-dependent channel parameters Time domain (default) | Frequency domain
  group: TX Modeling
- name: Relative error desired (dB)
  summary: Relative error for the rational fit -40 (default) | scalar
  group: TX Modeling
- name: Automatically estimate impulse response duration
  summary: Automatically calculate impulse response duration 'on' (default) | 'off'
  group: TX Modeling
- name: Impulse response duration
  summary: Impulse response duration 0s (default) | scalar
  group: TX Modeling
- name: Modeling options
  summary: Technique to model frequency-dependent channel parameters Frequency domain (default) | Time domain
  group: Medium Modeling
- name: Relative error desired (dB)
  summary: Relative error for rational fit -40 (default) | scalar
  group: Medium Modeling
- name: Automatically estimate impulse response duration
  summary: Automatically calculate impulse response duration 'off' (default) | 'on'
  group: Medium Modeling
- name: Impulse response duration
  summary: Impulse response duration 0s (default) | scalar
  group: Medium Modeling
- name: Modeling options
  summary: Technique to model frequency-dependent channel parameters Time domain (default) | Frequency domain
  group: RX Modeling
- name: Relative error desired (dB)
  summary: Relative error for the rational fit -40 (default) | scalar
  group: RX Modeling
- name: Automatically estimate impulse response duration
  summary: Automatically calculate impulse response duration 'on' | 'off'
  group: RX Modeling
- name: Impulse response duration
  summary: Impulse response duration 0s (default) | scalar
  group: RX Modeling
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Source of channel model** — Channel source `Isotropic free-space` (default) | `Ray-tracing`

Channel source, specified as one of these:

- `Isotropic free-space` — The block models the
  behavior of electromagnetic radiation from a point of transmission as it travels
  through free space. Free-space propagation models have no enforced frequency
  range, assume line-of-sight (LOS) conditions, and disregard terrain, the
  curvature of the Earth, and other obstacles. For more information, see `FreeSpace` (Antenna Toolbox).
- `Ray-tracing` — The block models propagation paths
  using 3-D environment geometry. For more information, see `RayTracing` (Antenna Toolbox).

  **Note**

  To specify the `Ray-tracing` option, you must
  have a license for Antenna Toolbox™.

#### TX Antenna

### **Antenna gain** — Gain of transmitter antenna `0 dBi` (default) | real scalar or vector | positive scalar or vector

Gain of the transmitter antenna, specified as a real scalar or vector, or as a
positive scalar or vector.

- If you specify a real scalar or vector, then set the **Antenna
  gain** parameter unit as `dBi`.
- If you specify a positive scalar or vector, then set the **Antenna
  gain** parameter unit as `None`.
- If you are specify a vector, the vector must be of the same length as the
  vector in the **Carrier frequencies** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

### **Impedance (Ohm)** — Input impedance of transmitter antenna `50` (default) | complex scalar or vector

Input impedance of the transmitter antenna, specified as a complex scalar or
vector in ohms. The vector must be of the same length as the vector that you specify
in the **Carrier frequencies** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

**Data Types:** `double`
**Complex Number Support:** Yes

#### RX Antenna

### **Antenna gain** — Gain of receiver antenna `0 dBi` (default) | real scalar or vector | positive scalar or vector

Gain of the receiver antenna, specified as a real scalar or vector, or as a
positive scalar or vector.

- If you specify a real scalar or vector, then set the **Antenna
  gain** parameter unit as `dBi`.
- If you specify a positive scalar or vector, then set the **Antenna
  gain** parameter unit as `None`.
- If you are specify a vector, the vector must be of the same length as the
  vector in the **Carrier frequencies** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

### **Impedance (Ohm)** — Input impedance of receiver antenna `50` (default) | complex scalar or vector

Input impedance of the receiver antenna, specified as a complex scalar or vector
in ohms. The vector must be of the same length as the vector that you specify in the
**Carrier frequencies** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

**Data Types:** `double`
**Complex Number Support:** Yes

#### Medium

### **Path loss** — Free-space path loss `10 dB` (default) | real scalar or vector | positive scalar or vector

Free-space path loss, specified as a real scalar or vector, or as a positive
scalar or vector.

- If you specify a real scalar or vector, then set the **Antenna
  gain** parameter unit as `dB`.
- If you specify a positive scalar or vector, then set the **Antenna
  gain** parameter unit as `None`.
- If you are specify a vector, the vector must be of the same length as the
  vector in the **Carrier frequencies** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

### **Path delay** — Free-space path delay `0 s` (default) | nonnegative scalar

Free-space path delay, specified as a nonnegative scalar in seconds, milliseconds,
microseconds, or nanoseconds.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Isotropic free-space`.

#### Ray-tracing

### **Map** — Map for visualization or surface data `"none"` (default) | `siteviewer` object | `triangulation` object | string scalar | character vector

Map for visualization or surface data, specified as a `siteviewer`
object, a `triangulation` object, a string scalar, or a character
vector. Valid and default map values depend on the coordinate system, as specified in
the propagation model.

| Coordinate System | Valid map values |
| --- | --- |
| `"geographic"` | - A `siteviewer` (Antenna Toolbox) objecta. - A terrain name, if the function is called with an output argument.   Valid terrain names are `"none"`,   `"gmted2010"`, or the name of the custom terrain   that you create using `addCustomTerrain` (Antenna Toolbox). |
| `"cartesian"` | - `"none"`. - A `siteviewer` object. - The name of an STL file. - A `triangulation` object. |
| a Alignment of boundaries and region labels are a presentation of the feature provided by the data vendors and do not imply endorsement by MathWorks®. | |

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

**Data Types:** `char` | `string`

### **Propagation model** — Propagation model `'raytracing'` (default) | `RayTracing` object

Propagation model, specified as `'raytracing'` or as a `RayTracing` (Antenna Toolbox)
object. The default value is `'raytracing'`, which uses the SBR
method, finds paths with up to two reflections and zero diffractions, and discards
paths that are more than 40 dB weaker than the strongest path.

You can create a `RayTracing` (Antenna Toolbox)
object by using the `propagationModel` (Antenna Toolbox) function. `RayTracing` objects enable
you to specify properties such as the ray tracing method, the maximum number of
reflections and diffractions, path loss thresholds, and building and terrain
materials.

For information about the differences between ray tracing methods, see Choose a Propagation Model (Antenna Toolbox).

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

**Data Types:** `char` | `string`

### **Tx site** — Transmitter site `txsite` object | array of `txsite` objects

Transmitter site, specified as a `txsite` (Antenna Toolbox)
object or an array of `txsite` objects. If you specify an array, the
`txsite` objects comprising the array must be identical except for
the `TransmitterFrequency` property.

**Note**

- Analyze the antenna, array, or PCB stack objects that you are specifying
  in the **Tx site** for at least one frequency before using
  them in the block.
- Specify the `Antenna` property of the
  `txsite` object as either an antenna element from the
  Antenna Catalog (Antenna Toolbox) or an array element from the
  Array Catalog (Antenna Toolbox).
  For more information, see `txsite` (Antenna Toolbox).

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

### **Rx site** — Receiver site `rxsite` object

Receiver site, specified as an `rxsite` (Antenna Toolbox) object.

**Note**

- Analyze the antenna, array, or PCB stack objects that you are specifying
  in the **Rx site** for at least one frequency before using
  them in the block.
- Specify the `Antenna` property of the
  `rxsite` object as either an antenna element from the
  Antenna Catalog (Antenna Toolbox) or an array element from the
  Array Catalog (Antenna Toolbox).
  For more information, see `rxsite` (Antenna Toolbox).

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

### **View Site** — Display RF propagation scenarios button

Click this button to display the transmitter sites, receiver sites, and RF
propagation rays. For more information, see `siteviewer` (Antenna Toolbox). Before clicking this button, specify the `siteviewer` (Antenna Toolbox)
object in the **Map** parameter.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

#### Channel Configuration

### **Carrier frequencies** — Carrier frequencies of channel `2.1 GHz` (default) | nonnegative scalar or row vector

Carrier frequencies of the channel, specified as a nonnegative scalar or row
vector in Hz, kHz, MHz, or GHz.

### **Simulate noise** — Simulate thermal noise `'on'` (default) | `'off'`

Select this parameter to simulate thermal noise in the channel. You must select
**Simulate noise** in the Configuration block before you enable the parameter in this block. Note
that the noise is only added in TX and RX antennas and not in the medium surrounding
them.

### **Ground and hide negative terminals** — Ground RF circuit terminals `'on'` (default) | `'off'`

Select this option to ground and hide the negative terminals. Clear this parameter
to expose the negative terminals. By exposing these terminals, you can connect them to
other parts of your model.

### **Edit System** — Edit or expand channel block button

Click this button to break the Channel block's links to the library
and replace the variables with values that the block estimates using the block
parameters. When clicking this button, the Channel block is either made a simple
unmasked subsystem, or gets expanded. For more information, see Edit Channel Block.

Clicking this button brings up a dialog box with the following options:

- **Edit System** — Edit the internal variables without
  expanding the subsystem.
- **Expand System** — Edit the subsystem and Expand the
  subsystem in the Simulink canvas.
- **Cancel** — Cancel the operation.

**Note**

Once you click the **Edit System** or **Expand
System** button, the operation cannot be undone.

### TX Modeling

### **Modeling options** — Technique to model frequency-dependent channel parameters `Time domain` (default) | `Frequency domain`

Technique to model frequency-dependent channel parameters, specified as one of
these values:

- `Time domain` — This technique creates an
  analytical rational model that approximates all the data in the range.
- `Frequency domain` — This technique computes the
  baseband impulse response for each carrier frequency independently. This
  technique is based on convolution. You can also specify the duration of the
  impulse response when you select this option. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.

The two analysis techniques use these frequency-dependent parameters.

- Antenna impedance — This parameter relates to the input impedance at the
  transmitter antenna terminals and is used in RF system simulation.
- Normalized vector effective length — This parameter establishes a
  relationship between the current flowing at the transmitter antenna terminals
  and the radiated far-field region in a specific direction. Due to reciprocity,
  this parameter also establishes a relationship between the incident field and
  the induced open-circuit voltage on the antenna terminals.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

### **Relative error desired (dB)** — Relative error for the rational fit `-40` (default) | scalar

Relative error for the rational fit, specified as a scalar. The block applies this
value in time-domain modeling of transmitter antenna impedance and normalized vector
effective length and displays the corresponding rational fitting results in the block
mask.

#### Dependencies

To enable this property, set **Modeling options** to
`Time domain`.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response duration `'on'` (default) | `'off'`

Select this parameter to automatically calculate the impulse response duration or
clear this parameter to manually specify the impulse response duration using the
**Impulse response duration** parameter. The block applies the
duration value in frequency-domain modeling of transmitter antenna impedance and
normalized vector effective length.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain`.

### **Impulse response duration** — Impulse response duration `0``s` (default) | scalar

Impulse response duration, specified as a scalar in seconds. The block applies the
duration value in frequency-domain modeling of transmitter antenna impedance and
normalized vector effective length.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain` and clear **Automatically
estimate impulse response duration**.

### Medium Modeling

### **Modeling options** — Technique to model frequency-dependent channel parameters `Frequency domain` (default) | `Time domain`

*Since R2024a*

Technique to model frequency-dependent channel parameters, specified as one of
these values:

- `Frequency domain` — This technique computes the
  baseband impulse response for each carrier frequency independently. This
  technique is based on convolution. You can also specify the duration of the
  impulse response when you select this option. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.
- `Time domain` — This technique creates an
  analytical rational model that approximates all the data in the range.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

### **Relative error desired (dB)** — Relative error for rational fit `-40` (default) | scalar

*Since R2024a*

Relative error for the rational fit, specified as a scalar in dB. The block
applies this value in time-domain modeling of the medium and displays the
corresponding rational fitting results in the block mask.

#### Dependencies

To enable this property, set **Modeling options** to
`Time domain`.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response duration `'off'` (default) | `'on'`

*Since R2024a*

Select this parameter to automatically calculate the impulse response duration or
clear this parameter to manually specify the impulse response duration using the
**Impulse response duration** parameter. The block applies the
duration value in frequency-domain modeling of the medium.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain`.

### **Impulse response duration** — Impulse response duration `0``s` (default) | scalar

*Since R2024a*

Impulse response duration, specified as a scalar in seconds. The block applies the
duration value in frequency-domain modeling of the medium.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain` and clear **Automatically
estimate impulse response duration**.

### RX Modeling

### **Modeling options** — Technique to model frequency-dependent channel parameters `Time domain` (default) | `Frequency domain`

Technique to model frequency-dependent channel parameters, specified as one of
these values:

- `Time domain` — This technique creates an
  analytical rational model that approximates all the data in the range.
- `Frequency domain` — This technique computes the
  baseband impulse response for each carrier frequency independently. This
  technique is based on convolution. You can also specify the duration of the
  impulse response when you select this option. For more information, see Compare Time and Frequency Domain Simulation Options for S-parameters.

The two analysis techniques use these frequency-dependent parameters.

- Antenna impedance — This parameter relates to the input impedance at the
  receiver antenna terminals and is used in RF system simulation.
- Normalized vector effective length — This parameter establishes a
  relationship between the current flowing at the transmitter antenna terminals
  and the radiated far-field region in a specific direction. Due to reciprocity,
  this parameter also establishes a relationship between the incident field and
  the induced open-circuit voltage on the antenna terminals.

#### Dependencies

To enable this parameter, set **Source of channel model** to
`Ray-tracing`.

### **Relative error desired (dB)** — Relative error for the rational fit `-40` (default) | scalar

Relative error for the rational fit, specified as a scalar. The block applies this
value in time-domain modeling of receiver antenna impedance and normalized vector
effective length and displays the corresponding rational fitting results in the block
mask.

#### Dependencies

To enable this property, set **Modeling options** to
`Time domain`.

### **Automatically estimate impulse response duration** — Automatically calculate impulse response duration `'on'` | `'off'`

Select this parameter to automatically calculate the impulse response duration or
clear this parameter to manually specify the impulse response duration using the
**Impulse response duration** parameter. The block applies the
duration value in frequency-domain modeling of receiver antenna impedance and
normalized vector effective length.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain`.

### **Impulse response duration** — Impulse response duration `0``s` (default) | scalar

Impulse response duration, specified as a scalar. The block applies the duration
value in frequency-domain modeling of receiver antenna impedance and normalized vector
effective length.

#### Dependencies

To set this parameter, set **Modeling options** to
`Frequency domain` and clear **Automatically
estimate impulse response duration**.
## Libraries

RF Blockset / Circuit Envelope / Systems

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

### R2024b: `Time domain (rationalfit)` parameter renamed

The `Time domain (rationalfit)` parameter value in the
**Modeling options** parameter has been renamed to `Time
domain` in the Channel block.

When you open a model created before R2024b containing an Channel block,
the parameter name displays as `Time domain`.

### R2024a: Model frequency-dependent propagation scenario using Channel block

You can now use the Channel block to model a frequency-dependent
Ray-trace propagation scenario between two RF systems using options in the **Medium
Modeling** tab.

### R2024a: Modeling TX and Modeling RX tabs are renamed

The **Modeling TX** and **Modeling RX** tabs in the
Channel block have been renamed to **TX Modeling** and
**RX Modeling**, respectively.

When you open a model created before R2024a containing the Channel block,
the software displays the names of the **Modeling TX** and
**Modeling RX** tabs as **TX Modeling** and **RX
Modeling** tabs, respectively.

## Description

Model isotropic free-space or ray-tracing based channel

Use the Channel block from the Circuit Envelope library to model an isotropic free-space
or ray-tracing based channel to account for the effect of antennas and RF propagation in a
medium.
