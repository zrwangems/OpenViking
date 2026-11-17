---
type: simulink-block
title: 'Continuous Wave'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Sources'
documentation_page: 'continuouswave'
documentation_source_path: 'ref/continuouswave.html'
language: en
---

# Continuous Wave

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Source type
  summary: Wave type Ideal voltage (default) | Ideal current | Power
  group: ''
- name: Constant in-phase value
  summary: In-phase modulations of carrier frequencies 0 V (default) | vector of real numbers | V | mV | kV
  group: ''
- name: Constant quadrature value
  summary: Quadrature modulations of carrier frequencies 0 V (default) | vector of real numbers | V | mV | kV
  group: ''
- name: Source impedance(Ohm)
  summary: Input impedance of source 50 (default) | positive real number | complex number
  group: ''
- name: Available power
  summary: Available power of carrier frequencies 0 W (default) | vector of real numbers | W | mW | dBW | dBm
  group: ''
- name: Angle(degrees)
  summary: Phase angle of power waves 0 (default) | vector of real numbers
  group: ''
- name: Carrier frequencies
  summary: Carrier frequencies 0 (default) | vector of real positive numbers | Hz | kHz | MHz | GHz
  group: ''
- name: Add phase noise
  summary: Add phase noise off (default) | on
  group: ''
- name: Phase noise frequency offset (Hz)
  summary: Phase noise frequency offset 0 (default) | scalar | vector | matrix
  group: ''
- name: Phase noise level (dBc/Hz)
  summary: Phase noise level 0 (default) | scalar | vector | matrix
  group: ''
- name: Automatically estimate impulse response duration
  summary: Automatically estimate impulse response duration on (default) | off
  group: ''
- name: Impulse response duration
  summary: Impulse response duration 1e-10s (default) | scalar
  group: ''
- name: Plot phase noise characteristics
  summary: Phase noise magnitude response button
  group: ''
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: ''
```

### **Source type** — Wave type `Ideal voltage` (default) | `Ideal current` | `Power`

- `Ideal Voltage` — The block
  simulates a constant voltage envelope
  *v*0 at the specified
  **Carrier frequencies**. The envelope has real
  and imaginary parts specified by the **Constant in-phase
  value** and **Constant quadrature
  value** parameters.
- `Ideal Current` — The block
  simulates a constant current envelope
  *i*0 at the specified
  **Carrier frequencies**. The envelope has real
  and imaginary parts determined by the **Constant in-phase
  value** and **Constant quadrature
  value** parameters.
- `Power` — The block simulates the
  constant voltage envelope

  v0=2P0Re(Zs)ejπ180ϕ

  where:

  - *P*0 is the
    value of the **Available power**
    parameter
  - *Zs* is the
    value of the **Source impedance
    (ohms)** parameter.
  - *ϕ* is the value of the
    **Angle (degrees)**
    parameter.

### **Constant in-phase value** — In-phase modulations of carrier frequencies `0 V` (default) | vector of real numbers | `V` | `mV` | `kV`

In-phase modulations for each of the **Carrier
frequencies**, specified as a vector of real numbers. Specify
the units from the corresponding drop-down list.

#### Dependencies

To enable this parameter, on the **Source type** tab,
choose `Ideal voltage` or `Ideal
current`.

### **Constant quadrature value** — Quadrature modulations of carrier frequencies `0 V` (default) | vector of real numbers | `V` | `mV` | `kV`

Quadrature modulations for each of the RF circuit carrier frequencies,
specified as a vector of real numbers. Specify the units from the
corresponding drop-down list.

#### Dependencies

To enable this parameter, on the **Source type** tab,
choose `Ideal voltage` or `Ideal
current`.

### **Source impedance(Ohm)** — Input impedance of source `50` (default) | positive real number | complex number

Input impedance of source, specified as a positive real number or a
complex number. The complex number must contain real and imaginary parts
greater than or equal to `1e-18` ohms.

#### Dependencies

To enable this parameter, on the **Source type** tab,
choose `Power`.

### **Available power** — Available power of carrier frequencies `0 W` (default) | vector of real numbers | `W` | `mW` | `dBW` | `dBm`

Available power at the specified **Carrier frequencies**,
specified as a vector of real numbers. Specify the units from the drop-down
list. The default value is
`0` `W`.

#### Dependencies

To enable this parameter, on the **Source type** tab,
choose `Power`. The default value is
`0` `W`

### **Angle(degrees)** — Phase angle of power waves `0` (default) | vector of real numbers

Phase angle of power waves at the specified **Carrier
frequencies**, specified as a vector of real numbers. The
default value is `0` degrees.

#### Dependencies

To enable this parameter, on the **Source type** tab,
choose `Power`.

### **Carrier frequencies** — Carrier frequencies `0` (default) | vector of real positive numbers | `Hz` | `kHz` | `MHz` | `GHz`

Carrier frequencies, specified as a vector of real positive numbers. The
elements in the carrier frequencies are combinations of fundamental tones
and corresponding harmonics in the Configuration block. The default
value is `0`
`Hz`.

### **Add phase noise** — Add phase noise `off` (default) | `on`

Select this parameter, to add phase noise to your system with continuous
wave source.

### **Phase noise frequency offset (Hz)** — Phase noise frequency offset `0` (default) | scalar | vector | matrix

Phase noise frequency offset, specified as a scalar or vector or matrix
with each element units in hertz.

If you specify a matrix, each column should correspond to a non-DC carrier
frequency of the CW source. The frequency offset values must be bounded by
the envelope bandwidth of the simulation. For more information see, Configuration.

#### Dependencies

To enable this parameter, select **Add phase noise**.

### **Phase noise level (dBc/Hz)** — Phase noise level `0` (default) | scalar | vector | matrix

Phase noise level, specified as a scalar or vector or matrix with element
unit in decibel per hertz.

If you specify a matrix, each column should correspond to a non-DC carrier
frequency of the CW source. The frequency offset values must be bounded by
the envelope bandwidth of the simulation. For more information see, Configuration.

#### Dependencies

To enable this parameter, select **Add phase noise**.

### **Automatically estimate impulse response duration** — Automatically estimate impulse response duration `on` (default) | `off`

Select this parameter to automatically calculate impulse response for
phase noise. Clear this parameter to manually specify the impulse response
duration using **Impulse response duration**.

#### Dependencies

To enable this parameter, select **Add phase noise**.

### **Impulse response duration** — Impulse response duration `1e-10``s` (default) | scalar

Impulse response duration used to simulate phase noise, specified as a
scalar in seconds. You cannot specify impulse response if the amplifier is
nonlinear.

**Note**

The phase noise profile resolution in frequency is limited by the
duration of the impulse response used to simulate it. Increase this
duration to improve the accuracy of the phase noise profile. A warning
message appears if the phase noise frequency offset resolution is too
high for a given impulse response duration, specifying the minimum
duration suitable for the required resolution

#### Dependencies

To set this parameter, first clear **Automatically estimate
impulse response duration**.

### **Plot phase noise characteristics** — Phase noise magnitude response button

The block plots the phase noise characteristics based on the parameters
specified in the **Impairments** tab and either
the **Envelope
bandwidth** parameter in the Configuration
block when available or the value specified in the **Phase
noise frequency offset (Hz)** parameter.

#### Dependencies

To enable this parameter, select **Add phase noise**.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select this option to internally ground and hide the negative terminals.
To expose the negative terminals, clear the option. By exposing these
terminals, you can connect them to other parts of your model.
## Libraries

RF Blockset / Circuit Envelope / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2022b: Estimate impulse response duration using phase noise offset frequencies

The Continuous Wave block estimates the impulse response duration
using the **Phase noise
frequency offset (Hz)** parameter and visualizes the phase noise
characteristics when you click the **Plot phase noise
characteristics** button.

### R2021b: Continuous Wave block icon updated

Starting in R2021b, the Continuous Wave block icon is now updated.
The block icons are now dynamic and show the current state of the noise
parameter.

When you open a model created before R2021b containing a Continuous
Wave block, the software replaces the block icon with the R2021b
version.

## Description

Model constant envelope source

The Continuous Wave block models a constant modulation
on a carrier in the RF Blockset™ circuit envelope simulation environment.
For an introduction to RF simulation, see the example, Simulate High Frequency Components.

The block implements the relation

v(t)=v0ejωkt

or

i(t)=i0ejωkt

at the carrier *ωk*,
depending on the source type.

Continuous Wave block mask icons are dynamic and show the current state
of the applied noise parameter. For more information, see Continuous Wave Block Icons.
