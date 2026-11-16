---
type: simulink-block
title: 'Noise'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Sources'
documentation_page: 'noise'
documentation_source_path: 'ref/noise.html'
language: en
---

# Noise

## Ports

Not documented in R2025b.

## Parameters

### **Source type** — Noise type `Ideal voltage` (default) | `Ideal current`

Noise type, specified as `Ideal voltage` or `Ideal
current`.

### **Noise distribution** — Noise distribution type `White` (default) | `Piece-wise linear` | `Colored`

Noise distribution type, specified as `White`, `Piece-wise
linear`, or `Colored`.

### **Noise power spectral density** — Single-sided noise power spectral distribution `0` (default) | scalar | vector

Single-sided noise power spectral distribution (PSD), specified as a scalar or
vector in V2/Hz or A2/Hz. The
single-sided PSD varies based on the noise distribution type. When you set the
**Noise distribution**
parameter to one of these options:

- `White` — Specify the **Noise power spectral
  density** parameter as a nonnegative scalar. The noise PSD of white noise
  is constant across all frequencies and the noise power depends on the bandwidth of
  the carrier or the time step. This is an uncorrelated noise source.
- `Piece-wise linear` — Specify the **Noise
  power spectral density** parameter as a vector. The vector must be of the
  same length as the vector you specify in the **Frequencies**
  parameter.

  For each carrier, the noise source behaves like a white noise source. The noise
  PSD of the noise source depends on the carrier, and you can calculate it by
  performing the linear interpolation at the carrier frequency on the noise spectral
  density curve.

  The noise spectral density curve represents the variation in noise PSD with
  respect to frequency. The block uses the values that you specify in the
  **Noise power spectral density** and
  **Frequencies** parameters to determine this curve.
- `Colored` — Specify the **Noise power spectral
  density** parameter as a vector. The vector must be of the same length as
  the vector you specify in the **Frequencies** parameter. This is a
  correlated noise source.

  The noise spectral density over the bandwidth at the carrier frequency is
  determined by the noise spectral density curve unless you set the **Impulse response duration** parameter to
  `0`.

The units of the single-sided PSD depend on the **Source type** parameter. When
you set the **Source type** parameter to:

- `Ideal voltage` — The block simulates the PSD in
  V2/Hz.
- `Ideal Current` — The block simulates the PSD in
  A2/Hz.

### **Frequencies** — Frequencies for piece-wise linear noise distribution `0 Hz` (default) | vector of non-negative frequencies | `Hz` | `kHz` | `MHz` | `GHz`

Frequencies for piece-wise linear noise distribution, specified
as vector of non-negative frequencies.

### **Automatically estimate impulse response duration** — Estimate impulse response duration `on` (default) | `off`

Select this parameter for the block to automatically estimate impulse response
duration or clear this parameter to specify the impulse response duration using the
**Impulse response duration** parameter..

#### Dependencies

To enable this parameter, set **Noise Distribution** to
`Colored`.

### **Impulse response duration** — Impulse response duration to simulate colored noise `1e-10 s` (default) | scalar | `s` | `ms` | `us` | `ns`

Impulse response duration to simulate colored noise, specified as a scalar in s, ms,
us, or ns. When you set the **Impulse response duration**
parameter to `0`, the software interpolates linearly as with a
`Piece-wise linear` noise source.

#### Dependencies

To enable this parameter, set **Noise Distribution** to
`Colored` and clear **Automatically estimate
impulse response duration**.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this option to internally ground and hide the negative
terminals. To expose the negative terminals, clear the option. By
exposing these terminals, you can connect them to other parts of your
model.

By default, this option is selected.

## Libraries

RF Blockset / Circuit Envelope / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2021b: Noise block icon updated

Starting in R2021b, the Noise block icon is now updated. When you open a
model created before R2021b containing a Noise block, the software replaces
the block icon with the R2021b version.

## Description

Model noise using current or voltage noise source in RF systems

Use the Noise  block to model noise as an ideal current or voltage source for
blocks. Using this block you can select the noise distribution type as white,
piecewise-linear, or colored. When you use a Noise  block to simulate noise in
an RF model, select the **Simulate noise** check box in the Configuration block. Otherwise, the model simulates without noise. The Noise block
does not depend on the **Temperature** parameter in the Configuration.

Noise block mask icons are dynamic and show the current type of source.
This table shows you how the icons on this block vary based on the type of source you set on
the **Source type** parameter on the block.

| Source type: `Ideal voltage` | Source type: `Ideal current` |
| --- | --- |
| Sinusoid block icon with Source type is set to Ideal voltage. | Sinusoid block icon with Source type is set to Ideal current. |
