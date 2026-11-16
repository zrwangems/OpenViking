---
type: simulink-block
title: 'IMT Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'imtmixer'
documentation_source_path: 'ref/imtmixer.html'
language: en
---

# IMT Mixer

## Ports

Not documented in R2025b.

## Parameters

#### Main

### **Carrier frequency (Hz)** — Carrier frequency `1e9` (default) | scalar

Carrier frequency, specified as a scalar in hertz. When multiple carriers
exist on the input connection, this carrier frequency is selected as the RF
signal input. Distance between adjacent carriers must be greater than (1−1e−8)Fc.

**Data Types:** `double`

### **Local oscillator frequency (Hz)** — Local oscillator (LO) frequency `0.9e9` (default) | scalar

Local oscillator (LO) frequency, specified as a scalar in hertz.

### **Reference input power (dBm)** — Reference input power `-10` (default) | scalar

Reference input power, specified as a scalar in dBm. The expression for
the normalized input signal for the specified reference input power is:

10((−Prf+20log10(1Rin)+30)20)

Intermodulation tables assume that the spur levels are measured for a
reference input and output power. For example, if you increase the input
power by 10 dB, the spurs due to second order non-linearity will increase by
20 dB, the spurs due to third order non-linearity will increase by 30 dB,
and so forth.

### **Nominal output power (dbm)** — Nominal LO power `-20` (default) | scalar

Nominal output power, specified as a scalar in dBm. The expression for the
normalized output signal for the specified reference input power is:

2x10((Pif−20log10(1Rout)−30)20)

### **Use data file** — Specify data file to use `off` (default) | `on`

Select this parameter to specify the data file you want to use to extract
the spur table. Clear to specify your own spur values. The data file may
contain any combination of IMT table, AC data, and colored spot noise in S2D
or P2D format. See [4].

### **Data file** — Data file `samplespur1.s2d` (default)

Data file, specified as IMT data, AC data, and colored spot noise. To
learn about the combination of inputs a data file can have and how this
block extracts and calculates the parameters, see Block Parameters When Using Data File.

#### Dependencies

To set this parameter, first select **Use data
file**.

### **Input impedance (Ohm)** — Input impedance of mixer `50` (default) | real scalar | vector of positive real scalars

Input impedance of mixer, specified as a real scalar or vector of positive
real scalars in ohms.

**Note**

For non-50 ohm input and output impedances, the IMT data is
normalized to 50 ohms.

### **Output impedance (Ohm)** — Output impedance of mixer `50` (default) | real scalar | vector of positive real scalars

Output impedance of mixer, specified as a real scalar or vector of
positive real scalars in ohms.

**Note**

For non-50 ohm input and output impedances, the IMT data is
normalized to 50 ohms.

### **Ground and hide negative terminals** — Ground RF negative circuit terminals `on` (default) | `off`

Select this parameter to internally ground and hide the negative
terminals. To expose the negative terminals, clear this parameter. If the
terminals are exposed, the input signal is not referenced to the
ground.

#### IMT

### **IMT table** — IMT spur visualization `[99 99 99; 99 0 99; 99 99 99]` (default) | square matrix

IMT spur visualization, specified as a square matrix.

### **Output signal power (dBm)** — Signal power of desired output tone `0` (default) | scalar

Signal power of the desired output tone when plotting intermodulation
products, specified as a scalar.

### **Mixer type** — Mixer type `Upconverter` (default) | `Downconverter`

Mixer type, specified as `Upconverter` or
`Downconverter`.

For a single tone carrier *Fcar*
nonlinearly modulated with an LO signal of frequency
*FLO*, the mixer output
intermodulation products occur at frequencies:

Fout(M,N)=|M×Fcar±N×FLO|

where:

- *Fcar* – input RF
  signal carrier frequency
- *FLO* – local
  oscillator frequency
- *M* and *N* are nonnegative
  integers (0,1,…, order of nonlinearity)

For a downconverter, the desired output tone is |Fcar−FLO|, and for an upconverter it is |Fcar+FLO|. All other combinations of *M* and
*N* represent the spurious intermodulation
products.

### **Plot** — Visualize IMT table values using specified signal power and mixer type button

Visualize IMT table values using specified signal power and mixer
type.

#### Noise

### **Simulate noise** — Simulate device or phase noise `on` (default) | `off`

Select this parameter to simulate noise as specified in block parameters
or in file.

If the noise is specified in an `.s2p` file, then it is
used for simulation.

### **Noise type** — Noise type `Noise figure` (default) | `Spot noise data`

Noise type, specified as `Noise figure` or
`Spot noise data`.

#### Dependencies

To set this parameter, first select **Simulate
noise**.

### **Noise distribution** — Noise distribution `White` (default) | `Piece-wise linear` | `Colored`

Noise distribution, specified as:

- `White` – Spectral density is a
  single nonnegative value. The power value of the noise depends
  on the bandwidth of the carrier, and the bandwidth depends on
  the time step. This is an uncorrelated noise source.
- `Piece-wise linear` – Spectral
  density is a vector of values
  [*pi*]. For each
  carrier, the noise source behaves like a white uncorrelated
  noise. The power of the noise source is carrier
  dependent.
- `Colored` – Depends on both carrier
  and bandwidth. This is a correlated noise source.

#### Dependencies

To set this parameter, first select **Simulate
noise**.

### **Noise figure (dB)** — Noise figure `0` (default) | scalar

Noise figure, specified as a scalar in decibels.

#### Dependencies

To set this parameter, first select **Simulate
noise**.

### **Frequencies (Hz)** — Frequency data `0` (default) | scalar | vector

Frequency data, specified as a scalar for white noise or vector for
piece-wise linear or colored noise in hertz.

#### Dependencies

To set this parameter, first select **Select noise**
then select `Piece-wise linear` or
`Colored` in **Noise
distribution**.

### **Minimum noise figure (dB)** — Minimum noise figure `0` (default) | scalar | vector

Minimum noise figure, specified as a scalar or vector in decibels.

#### Dependencies

To set this parameter, first select `Spot noise
data` in **Noise type**.

#### Dependencies

To set this parameter, first select **Select noise**
then select `Spot noise data` in
**Noise Type**.

### **Optimal reflection coefficient** — Optimal reflection coefficient `0` (default) | scalar | vector

Optimal reflection coefficient, specified as a scalar or a vector.

#### Dependencies

To set this parameter, first select **Select noise**
then select `Spot noise data` in
**Noise Type**.

### **Equivalent normalized noise resistance** — Equivalent normalized noise resistance `0` (default) | scalar | vector

Equivalent normalized noise resistance, specified as a scalar or
vector.

#### Dependencies

To set this parameter, first select **Select noise**
then select `Spot noise data` in
**Noise Type**.

### **Add LO phase noise** — Add phase noise `off` (default) | `on`

Select this parameter to add phase noise to your system with a continuous
wave source.

#### Dependencies

To set this parameter, select **Simulate
noise**.

### **Phase noise frequency offset (Hz)** — Phase noise frequency offset `1` (default) | scalar | vector

Phase noise frequency offset with respect to LO signal, specified as a
scalar or vector with each element unit in hertz.

The frequency offset values must be bounded by the envelope bandwidth of
the simulation. For more information see Configuration.

#### Dependencies

To enable this parameter, first select **Simulate
noise** then select **Add phase noise**.

### **Phase noise level (dBc/Hz)** — Phase noise level `-Inf` (default) | scalar | vector | matrix

Phase noise level, specified as a scalar or vector or matrix with elements
in decibel per hertz.

If you specify a matrix, each column should correspond to a non-DC carrier
frequency of the CW source. The frequency offset values must be bounded by
the envelope bandwidth of the simulation. For more information see Configuration.

#### Dependencies

To enable this parameter, first select **Simulate
noise** then select **Add phase noise**.

### **Automatically estimate impulse response duration** — Automatically estimate impulse response duration `on` (default) | `off`

Select this parameter to automatically calculate impulse response for
frequency-dependent noises. Clear this parameter to manually specify the
impulse response duration using **Impulse response
duration**.

#### Dependencies

To enable this parameter, first select **Simulate
noise** then select **Add phase noise**.

### **Impulse response duration** — Impulse response duration `1e-10``s` (default) | scalar

Impulse response duration used to simulate frequency-dependent noise,
specified as a scalar in seconds. The time should be an integer multiple of
the step size in the configuration block,
`Tduration =
NTstep`.

#### Dependencies

To set this parameter, first clear **Automatically estimate
impulse response duration**.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

### R2022a: Extract reference input power and nominal output power from data file

You can now extract reference input power and nominal output power from a data
file. For more information, see Block Parameters When Using Data File.

### R2021b: IMT Mixer block icon updated

Starting in R2021b, the IMT Mixer block icon has updated. The block
icons are now dynamic and show the current state of the noise parameter.

When you open a model created before R2021b containing a IMT Mixer
block, the software replaces the block icon with the R2021b version.

## Description

Model mixer using intermodulation table (IMT)

Use the IMT Mixer to perform frequency translation defined in an
intermodulation table (see [1], [2], [3], and [4]) for a single tone
carrier mixed with a local oscillator (LO) signal. The block includes nonlinear
amplification, device and phase noise, and mixer spur visualization. For a single tone
carrier *Fcar* nonlinearly modulated with an LO
signal of frequency *FLO*, the mixer output
intermodulation products occur at frequencies:

Fout(M,N)=|M×Fcar±N×FLO|

where:

- *Fcar* – input RF signal carrier
  frequency
- *FLO* – local oscillator
  frequency
- *M* and *N* are nonnegative integers
  (0,1,…, order of nonlinearity)

For a downconverter, the desired output tone is |Fcar−FLO|, and for an upconverter it is |Fcar+FLO|. All other combinations of *M* and
*N* represent the spurious intermodulation products.

IMT Mixer block mask icons are dynamic and indicate the current state
of the applied noise parameter. For more information, see IMT Mixer Icons.
