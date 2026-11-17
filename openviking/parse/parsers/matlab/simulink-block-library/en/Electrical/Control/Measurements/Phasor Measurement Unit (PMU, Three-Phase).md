---
type: simulink-block
title: 'Phasor Measurement Unit (PMU, Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'phasormeasurementunitpmuthreephase'
documentation_source_path: 'ref/phasormeasurementunitpmuthreephase.html'
language: en
---

# Phasor Measurement Unit (PMU, Three-Phase)

## Ports
```yaml
ports:
- name: abc
  summary: Three-phase signal vector
  direction: input
  data_types: single | double
- name: freq
  summary: Frequency of positive sequence component scalar
  direction: output
  data_types: single | double
- name: angle
  summary: Phase angle of positive sequence component scalar
  direction: output
  data_types: single | double
- name: mag
  summary: Magnitude of positive sequence component scalar
  direction: output
  data_types: single | double
```

### Input

### **abc** — Three-phase signal vector

Three-phase input signal, specified as a vector.

**Data Types:** `single` | `double`
### Output

### **freq** — Frequency of positive sequence component scalar

Measured frequency of the positive sequence component, in Hz, returned
as a scalar.

**Data Types:** `single` | `double`

### **angle** — Phase angle of positive sequence component scalar

Measured phase angle of the positive sequence component, in degrees,
returned as a scalar.

**Data Types:** `single` | `double`

### **mag** — Magnitude of positive sequence component scalar

Measured magnitude of the positive sequence component, returned as a
scalar.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Rated frequency (Hz)
  summary: Rated frequency 60 (default) | 50
  group: ''
- name: Sampling points per cycle
  summary: Sampling points per cycle 64 (default) | 24 | 48
  group: ''
- name: Reporting rate factor
  summary: Reporting rate factor 1 (default) | scalar
  group: ''
```

### **Rated frequency (Hz)** — Rated frequency `60` (default) | `50`

Rated frequency of the input signal, in Hz.

### **Sampling points per cycle** — Sampling points per cycle `64` (default) | `24` | `48`

Number of sampling points per cycle.

### **Reporting rate factor** — Reporting rate factor `1` (default) | scalar

Ratio between the reporting rate and the sampling rate of the block.
## Libraries

Simscape / Electrical / Control / Measurements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Frequency, phase, and amplitude measurement of a three-phase system

The Phasor Measurement Unit (PMU, Three-Phase) block measures
the frequency, phase, and amplitude of the positive sequence component of the input
electrical signal in a three-phase system at a particular sample rate.

The block uses a system clock as the synchronous reference. This information is commonly
collected from a GPS in the real world.
