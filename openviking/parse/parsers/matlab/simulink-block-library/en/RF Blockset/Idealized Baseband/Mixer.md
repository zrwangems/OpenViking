---
type: simulink-block
title: 'Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'mixeridealizedbaseband'
documentation_source_path: 'ref/mixeridealizedbaseband.html'
language: en
---

# Mixer

## Ports
```yaml
ports:
- name: Port_1
  summary: Time-dependent input signal real scalar | real column | complex scalar | complex column
  direction: input
  data_types: double | single
- name: Port_1
  summary: Time-dependent output signal complex scalar | complex column
  direction: output
  data_types: double | single
```

### Input

### **Port\_1** — Time-dependent input signal real scalar | real column | complex scalar | complex column

Time-dependent input signal, specified as a real scalar, real column, complex
scalar, or complex column. A column represents consecutive time points.

**Data Types:** `double` | `single`
### Output

### **Port\_1** — Time-dependent output signal complex scalar | complex column

Time-dependent output signal , returned as a complex scalar or complex column. The
size of the output time dependent signal is equal in size to the input time dependent
signal.

**Data Types:** `double` | `single`
## Parameters
```yaml
parameters:
- name: Mixer type
  summary: Type of mixer mod (default) | demod | iqmod | iqdemod
  group: Main Tab
- name: Sideband
  summary: Sidebands of mixer upper (default) | lower
  group: Main Tab
- name: RF (Hz)
  summary: RF carrier frequency 1e9 (default) | real number
  group: Main Tab
- name: LO (Hz)
  summary: Local oscillator frequency 1e8 (default) | real number
  group: Main Tab
- name: Gain (dB)
  summary: Conversion gain for mixer 0 (default) | real number
  group: Main Tab
- name: Simulate using
  summary: Specify type of simulation to run Interpreted execution (default) | Code generation
  group: Main Tab
- name: LO phase offset (deg)
  summary: LO phase offset 0 (default) | real number
  group: Impairments Tab
- name: I/Q gain imbalance (dB)
  summary: IQ gain imbalance 0 (default) | nonnegative real numbers
  group: Impairments Tab
- name: I/Q phase imbalance (deg)
  summary: IQ phase imbalance 0 (default) | real numbers
  group: Impairments Tab
- name: Non-Linearity
  summary: Third-order nonlinearity type OIP3 (default) | IIP3 | IP1dB | OP1dB | IPsat | OPsat
  group: Impairments Tab
- name: IIP3 (dBm)
  summary: Input third-order intercept point Inf (default) | real positive number
  group: Impairments Tab
- name: OIP3 (dBm)
  summary: Output third-order intercept point Inf (default) | real positive number
  group: Impairments Tab
- name: IP1dB (dBm)
  summary: Input 1 dB compression point Inf (default) | real positive number
  group: Impairments Tab
- name: OP1dB (dBm)
  summary: Output 1 dB compression point Inf (default) | real positive number
  group: Impairments Tab
- name: IPsat (dBm)
  summary: Input saturation point Inf (default) | real positive number
  group: Impairments Tab
- name: OPsat (dBm)
  summary: Output saturation point Inf (default) | real positive number
  group: Impairments Tab
- name: Plot power characteristics
  summary: Plot power characteristics button
  group: Impairments Tab
- name: Include mixer noise
  summary: Add mixer noise to system off (default) | on
  group: Noise Tab
- name: Mixer noise type
  summary: Noise representation NF (default) | noise-temperature | noise-factor
  group: Noise Tab
- name: Noise temperature (K)
  summary: Noise temperature to model mixer noise 290 (default) | nonnegative real number
  group: Noise Tab
- name: Noise figure (dB)
  summary: Noise figure to model mixer noise 10 * log10( 2 ) (default) | nonnegative real number
  group: Noise Tab
- name: Noise factor
  summary: Noise factor to model mixer noise 2 (default) | positive integer scalar greater than or equal to 1
  group: Noise Tab
- name: Seed source, mixer noise
  summary: Source of initial seed auto (default) | user
  group: Noise Tab
- name: Seed for mixer noise
  summary: Seed for random number generator 67987 (default) | nonnegative integer less than 232
  group: Noise Tab
- name: Include phase noise
  summary: Add LO phase noise to LO signal off (default) | on
  group: Noise Tab
- name: Phase noise level (dBc/Hz)
  summary: Phase noise level relative to carrier [-145 -150] (default) | negative real scalar | negative real vector
  group: Noise Tab
- name: Frequency offset (Hz)
  summary: Phase frequency offset [2000 20000] (default) | positive real scalar | vector of positive increasing real values
  group: Noise Tab
- name: Automatic frequency resolution
  summary: Automatically determine number of frequency bins on (default) | off
  group: Noise Tab
- name: Number of signal samples
  summary: Number of samples in time-domain signal 0 (default) | real nonnegative integer less than or equaled to 65536
  group: Noise Tab
- name: Seed source, phase noise
  summary: Source of initial seed auto (default) | user
  group: Noise Tab
- name: Seed for phase noise
  summary: Seed for random number generator 67987 (default) | nonnegative integer less than 232
  group: Noise Tab
- name: Plot phase characteristics
  summary: Plot phase characteristics button
  group: Noise Tab
```

### Main Tab

### **Mixer type** — Type of mixer `mod` (default) | `demod` | `iqmod` | `iqdemod`

Mixers available in the Mixer block, specified as one of the following:

- `mod` — Modulator
- `demod` — Demodulator
- `iqmod` — IQ Modulator
- `iqdemod` — IQ Demodulator

For more information, see Mixer Architectures and Design Equations.

### **Sideband** — Sidebands of mixer `upper` (default) | `lower`

Sidebands of the mixer, specified as one of the one of the following:

- `lower`
- `upper`

For more information, see Mixer Sidebands.

#### Dependencies

To enable this parameter, set **Mixer
type** to `mod`.

### **RF (Hz)** — RF carrier frequency `1e9` (default) | real number

*Since R2024b*

RF carrier frequency for the mixer model, specified as a real number in Hz.

#### Dependencies

To enable this parameter, set **Mixer
type** to `mod`,
`demod`, `iqdemod`.

### **LO (Hz)** — Local oscillator frequency `1e8` (default) | real number

*Since R2024b*

Local oscillator frequency for the mixer model, specified as a real number in
Hz.

#### Dependencies

To enable this parameter, set **Mixer
type** to `mod`,
`demod`, `iqmod`.

### **Gain (dB)** — Conversion gain for mixer `0` (default) | real number

Conversion gain for the mixer model, specified as a real number in dB.

### **Simulate using** — Specify type of simulation to run `Interpreted execution` (default) | `Code generation`

Type of simulation to run, specified as one of the following:

- `Code generation` — Simulate model using generated
  C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations, as long as the model does not change. This option
  requires additional startup time, but the speed of the subsequent simulations is
  faster than `Interpreted execution`.
- `Interpreted execution` — Simulate model using the
  MATLAB® interpreter. This option shortens startup time speed, but the
  speed of the subsequent simulations is slower than `Code
  generation`. In this mode, you can debug the source code of the
  block.

### Impairments Tab

### **LO phase offset (deg)** — LO phase offset `0` (default) | real number

LO phase offset, specified as a real number in degrees.

#### Dependencies

To enable this parameter, set **Mixer
type** to `mod` or
`demod`.

### **I/Q gain imbalance (dB)** — IQ gain imbalance `0` (default) | nonnegative real numbers

IQ gain imbalance, specified as a nonnegative real numbers in decibels.

#### Dependencies

To enable this parameter, set **Mixer
type** to `iqmod` or
`iqdemod`.

### **I/Q phase imbalance (deg)** — IQ phase imbalance `0` (default) | real numbers

IQ phase imbalance, specified as a real number in degrees.

#### Dependencies

To enable this parameter, set **Mixer
type** to `iqmod` or
`iqdemod`.

### **Non-Linearity** — Third-order nonlinearity type `OIP3` (default) | `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

Type of third-order nonlinearity type in the cubic polynomial model, specified as
`IIP3`, `OIP3`, `IP1dB`,
`OP1dB`, `IPsat`, or
`OPsat`.

For more information, see Nonlinearities in Idealized Baseband Mixer Block.

### **IIP3 (dBm)** — Input third-order intercept point `Inf` (default) | real positive number

Input third-order intercept point, specified as a real positive number in
dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `IIP3`.

### **OIP3 (dBm)** — Output third-order intercept point `Inf` (default) | real positive number

Output third-order intercept point, specified as a real positive number in
dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `OIP3`.

### **IP1dB (dBm)** — Input 1 dB compression point `Inf` (default) | real positive number

Input 1 dB compression point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `IP1dB`.

### **OP1dB (dBm)** — Output 1 dB compression point `Inf` (default) | real positive number

Output 1 dB compression point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `OP1dB`.

### **IPsat (dBm)** — Input saturation point `Inf` (default) | real positive number

Input saturation point, specified as a real positive number in dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `IPsat`.

### **OPsat (dBm)** — Output saturation point `Inf` (default) | real positive number

Output saturation point, specified as a positive real number in dBm.

#### Dependencies

To enable this parameter, set **Type of
Non-Linearity** to `OPsat`.

### **Plot power characteristics** — Plot power characteristics button

This button plots the power characteristics based on the value you specify in the
Gain (dB) parameter in the
**Main** tab and the Non-Linearity in the
**Impairments** tab. When plotting power characteristics, the block
ignores all other impairment values.

For more information, see Plot Power Characteristics.

### Noise Tab

### **Include mixer noise** — Add mixer noise to system `off` (default) | `on`

Select this parameter to add mixer noise to the input signal. Once you select this
parameter, the parameters associated with **Include mixer noise** are
displayed and the mixer components in the block icon are shaded gray.

For more information, see Mixer (System) Noise Simulations.

### **Mixer noise type** — Noise representation `NF` (default) | `noise-temperature` | `noise-factor`

Type of noise, specified as one of the following:

- `noise-temperature` — Noise temperature
- `NF` — Noise figure
- `noise-factor` — Noise factor

For more information, see Mixer (System) Noise Simulations.

#### Dependencies

To enable this parameter, select **Include mixer
noise**.

### **Noise temperature (K)** — Noise temperature to model mixer noise `290` (default) | nonnegative real number

Noise temperature to model the mixer noise, specified as a nonnegative real number
in kelvin.

#### Dependencies

To enable this parameter, select **Include mixer
noise** and set **Mixer noise
type** to `noise-temperature`.

### **Noise figure (dB)** — Noise figure to model mixer noise `10 * log10( 2 )` (default) | nonnegative real number

Noise figure to model the mixer noise, specified as a nonnegative real number in
decibels.

#### Dependencies

To enable this parameter, select **Include mixer
noise** and set **Mixer noise
type** to `NF`.

### **Noise factor** — Noise factor to model mixer noise `2` (default) | positive integer scalar greater than or equal to `1`

Noise factor to model mixer noise, specified as a positive integer scalar greater
than or equal to `1`

#### Dependencies

To enable this parameter, select **Include mixer
noise** and set **Mixer noise
type** to `noise-factor`.

### **Seed source, mixer noise** — Source of initial seed `auto` (default) | `user`

Source of initial seed used to prepare the Gaussian random number noise generator,
specified as one of the following:

- `auto` — When you set **Seed source, mixer
  noise** to `auto`, seeds for each mixer
  instance are generated using a random number generator. The reset method of the
  instance has no effect.
- `user` — When you set **Seed source, mixer
  noise** to `auto`, the value provided in the
  **Seed for mixer
  noise** is used to initialize the random number generator and the
  reset method resets the random number generator using the **Seed for
  mixer noise** property value.

#### Dependencies

To enable this parameter, select **Include mixer
noise**.

### **Seed for mixer noise** — Seed for random number generator `67987` (default) | nonnegative integer less than 232

Seed for the random number generator, specified as a nonnegative integer less than
232. Use this value to initialize the random number
generator.

#### Dependencies

To enable this parameter, select **Include mixer
noise** and set the **Seed source, mixer
noise** parameter to `user`.

### **Include phase noise** — Add LO phase noise to LO signal `off` (default) | `on`

Select this parameter to add frequency-depended LO phase noise to the LO signal.
Once you select this parameter, the parameters associated with the **Include
phase noise** are displayed and the LO source inside the block icon is
shaded gray.

For more information, see Phase Noise in Mixer Block.

### **Phase noise level (dBc/Hz)** — Phase noise level relative to carrier `[-145 -150]` (default) | negative real scalar | negative real vector

Phase noise level relative to carrier, specified as negative real scalar or vector
in dBc/Hz.

**Note**

The number of terms listed in the **Phase noise level
(dBc/Hz)** parameter must equal the number of terms in the Frequency offset (Hz) field.

#### Dependencies

To enable this parameter, select the **Include phase
noise** parameter.

**Data Types:** `double`

### **Frequency offset (Hz)** — Phase frequency offset `[2000 20000]` (default) | positive real scalar | vector of positive increasing real values

Specify the frequency offset as a positive real scalar or vector of positive
increasing real values of type double in Hz.

**Note**

The number of terms listed in the **Frequency offset (Hz)**
must equal the number of terms in the Phase noise level (dBc/Hz) field.

#### Dependencies

To enable this parameter, select the **Include phase
noise** parameter.

### **Automatic frequency resolution** — Automatically determine number of frequency bins `on` (default) | `off`

Select this parameter to automatically determine number of frequency bins used in
a two-sided phase noise spectrum. You can also set the number of frequency bins using
the **Number of signal samples**  and **Sample rate
(Hz)** parameters when you set the **Automatic frequency
resolution** parameter is set to `off`.

#### Dependencies

To enable this parameter, click **Include phase
noise**.

### **Number of signal samples** — Number of samples in time-domain signal `0` (default) | real nonnegative integer less than or equaled to `65536`

Number of samples in the time-domain signal for the blocks sample time or the
number of frequency lines (bins) in the signals two-sided frequency spectrum to
achieve the required frequency resolution for a specified Frequency offset, specified
as a real nonnegative integer less than or equaled to `65536`.
Frequency resolution increases as the value of number of signal samples increases.

**Note**

The value of this parameter must be set to a power of two.

#### Dependencies

To enable this parameter, select the **Include phase
noise** parameter and deselect **Automatic frequency
resolution**.

### **Seed source, phase noise** — Source of initial seed `auto` (default) | `user`

Source of initial seed used to prepare the Gaussian random number LO phase noise
generator, specified as one of the following:

- `auto` — When you set the **Seed source,
  phase noise** to `auto`, seeds for each
  mixer instance are generated using a random number generator. The reset method
  of the instance has no effect.
- `user` — When you set the **Seed source,
  phase noise** to `user`, the value provided
  in the **Seed for phase
  noise** is used to initialize the random number generator and the
  reset method resets the random number generator using the **Seed for
  phase noise** property value.

#### Dependencies

To enable this parameter, select the **Include phase
noise** parameter.

### **Seed for phase noise** — Seed for random number generator `67987` (default) | nonnegative integer less than 232

Seed for the random number generator, specified as a nonnegative integer less than
232. Use this value to initialize the random number
generator.

#### Dependencies

To enable this parameter, select **Include phase
noise** and set the **Seed source, phase
noise** parameter to `user`.

### **Plot phase characteristics** — Plot phase characteristics button

This button plots the phase characteristics based on the parameters specified on
the **Noise** tab and either the block sample time when a simulation
has been performed or estimated from the Frequency offset (Hz) parameter
values.

For more information, see Plot Phase Noise Characteristics.
## Libraries

RF Blockset / Idealized Baseband

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024b: Parameters of Mixer block from idealized baseband library have been renamed

The following parameters in the Mixer block in the idealized baseband
library have been renamed.

| Parameter Name Before R2024b | Parameter Name Since R2024b |
| --- | --- |
| **Mixer sideband** | **Sideband** |
| **Conversion gain (dB)** | **Gain (dB)** |
| **Type of Non-linearity** | **Non-linearity** |

The following parameter values in the Mixer block in the idealized
baseband library have been changed:

| Parameter | Values Before R2024b | Values Since R2024b |
| --- | --- | --- |
| **Mixer type** | `Modulator` | `mod` |
| `Demodulator` | `demod` |
| `IQ Demodulator` | `iqdemod` |
| `IQ Modulator` | `iqmod` |
| **Mixer noise type** | `Noise figure` | `NF` |
| `Noise temperature` | `noise-temperature` |
| `Noise factor` | `noise-factor` |
| **Sideband** | `Upper` | `upper` |
| `Lower` | `lower` |
| **Seed source, phase noise** | `Auto` | `auto` |
| `User specified` | `user` |
| **Seed source, mixer noise** | `Auto` | `auto` |
| `User specified` | `user` |

The following default values in the Mixer block in the idealized baseband
library have been changed:

| Parameter | Default Values Before R2024b | Default Values Since R2024b |
| --- | --- | --- |
| **Non-linearity** | `IIP3` | `OIP3` |
| **Mixer noise type** | `Noise temperature` | `NF` |

When you open a model created before R2024b containing the Mixer block,
the software replaces the parameter names and values as shown in the table.

### R2024b: Input carrier frequency greater than LO frequency parameter is replaced

The **Input carrier frequency greater than LO frequency** parameter has
replaced by **RF (Hz)**and **LO(Hz)** parameters.

When you open a model created before R2024b containing the Mixer block,
the software replaces the**Input carrier frequency greater than LO
frequency** with **RF (Hz)**and **LO(Hz)**
parameters.

### R2023a: Phase noise characteristics of Mixer block changed

Starting in this release, the extrapolated low-frequency phase noise below the first
frequency point that specifies the 1/f^3 in the Mixer block is now 30
dB/decade instead of 3 dB/decade.

When you open a model created before R2023a containing the Mixer block
and click the **Plot Phase Characteristics** button, the software scales
the phase noise level in dBc/Hz on the y-axis in a phase noise magnitude response
plot.

For example, open the Mixer block and select **Include Phase Noise**.
Set the **Number of signal samples** to `2^10` and click
the **Apply** button. Click the **Plot Phase
Characteristics** button to plot the phase noise magnitude response and observe
that the first frequency point that specifies the 1/f^3 in the Mixer block is
scaled to 30 dB/decade.

Phase noise magnitude response where the first frequency point that specifies the 1/f^3 in the Mixer block is scaled to 30 dB/decade

### R2021a: Mixer models and noise supported for Mixer block in Idealized Baseband library changed

Starting in R2021a, the Mixer block supports modulator, demodulator, IQ modulator, and
IQ demodulator mixers with impairments and noise. The new Mixer block enables you to use
pre-R2021a functionality when the **Mixer type**
parameter is set to `Modulator`.

When you open a model from a previous release containing the Mixer block from the
Idealized Baseband library, the pre-R2021a version of this block is automatically replaced
with the R2021a version of this block with impairments and noise.

## Description

Model RF and IQ modulator and RF and IQ demodulator with impairments and noise

The Mixer block models four complex baseband mixers and with impairments
and noise. The four mixer types that the block models are Modulator, Demodulator, IQ
Modulator, and IQ Demodulator. Impairments include IQ gain and phase mismatch where
appropriate, while noise includes both system and LO phase noise.

**Note**

- Idealized Baseband library blocks assume input and output ports are matched. For
  more information on port signal power, see Power Ports and Signal Power Measurement in RF Blockset.
- Idealized Baseband library blocks are single carrier with assumed carrier frequency
  value. Therefore the Ideal Baseband Mixer block can produce only a single sideband
  output.
- Mixer block mask icons are dynamic and indicate the current set of applied noise
  parameters. For more information, see Mixer Block Icons.
