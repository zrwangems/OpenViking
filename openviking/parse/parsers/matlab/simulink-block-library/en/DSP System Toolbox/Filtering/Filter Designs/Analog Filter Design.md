---
type: simulink-block
title: 'Analog Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'analogfilterdesign'
documentation_source_path: 'ref/analogfilterdesign.html'
language: en
---

# Analog Filter Design

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar
  direction: input
  data_types: double
- name: Port_1
  summary: Output signal scalar
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input signal scalar

Input signal to filter, specified as a sample-based, continuous-time,
real-valued scalar value.

**Data Types:** `double`
### Output

### **Port\_1** — Output signal scalar

Filtered signal, returned as a real double scalar value.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Design method
  summary: Filter design Butterworth (default) | Chebyshev I | Chebyshev II | Elliptic | Bessel
  group: ''
- name: Filter type
  summary: Filter type Lowpass (default) | Highpass | Bandpass | Bandstop
  group: ''
- name: Filter order
  summary: Filter order 8 (default) | scalar value
  group: ''
- name: Passband edge frequency (rad/s)
  summary: Passband edge frequency 30 (default) | scalar value
  group: ''
- name: Lower passband edge frequency (rad/s)
  summary: Lower passband edge frequency 30 (default) | scalar value
  group: ''
- name: Upper passband edge frequency (rad/s)
  summary: Upper passband edge frequency 80 (default) | scalar value
  group: ''
- name: Stopband edge frequency (rad/s)
  summary: Stopband edge frequency 30 (default) | scalar value
  group: ''
- name: Lower stopband edge frequency (rad/s)
  summary: Lower stopband edge frequency 30 (default) | scalar value
  group: ''
- name: Upper stopband edge frequency (rad/s)
  summary: Upper stopband edge frequency 80 (default) | scalar value
  group: ''
- name: Passband ripple in dB
  summary: Passband ripple 2 (default) | scalar value
  group: ''
- name: Stopband attenuation in dB
  summary: Stopband attenuation 40 (default) | scalar value
  group: ''
```

### **Design method** — Filter design `Butterworth` (default) | `Chebyshev I` | `Chebyshev II` | `Elliptic` | `Bessel`

The filter design methods are:

- `Butterworth` — The magnitude
  response of a Butterworth filter is maximally flat in the
  passband and monotonic overall. The Butterworth design uses the
  toolbox function `butter`.
- `Chebyshev I` — The magnitude
  response of a Chebyshev I filter is equiripple in the passband
  and monotonic in the stopband. The Chebyshev I design uses the
  toolbox function `cheby1`.
- `Chebyshev II` — The magnitude
  response of a Chebyshev II filter is monotonic in the passband
  and equiripple in the stopband. The Chebyshev II design uses the
  toolbox function `cheby2`.
- `Elliptic` — The magnitude response
  of an elliptic filter is equiripple in both the passband and the
  stopband. The elliptic design uses the toolbox function
  `ellip`.
- `Bessel` — The magnitude response of
  a bessel filter is maximally flat in the passband and monotonic
  overall. The filter has a maximally flat linear phase response.
  The bessel design uses the function `besself`.

**Tunable:** Yes

### **Filter type** — Filter type `Lowpass` (default) | `Highpass` | `Bandpass` | `Bandstop`

The type of filter to design:

- `Lowpass`
- `Highpass`
- `Bandpass`
- `Bandstop`

**Tunable:** Yes

### **Filter order** — Filter order `8` (default) | scalar value

The order of the filter when `Filter
type` is set to:

- `Lowpass`
- `Highpass`

The order of the final filter is *twice*
the value of **Filter order** when **Filter
type** is set to:

- `Bandpass`
- `Bandstop`

.

### **Passband edge frequency (rad/s)** — Passband edge frequency `30` (default) | scalar value

The passband edge frequency, in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

and `Filter
type` is set to:

- `Lowpass`
- `Highpass`

### **Lower passband edge frequency (rad/s)** — Lower passband edge frequency `30` (default) | scalar value

The lower passband edge frequency, specified in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

and `Filter
type` is set to:

- `Bandpass`
- `Bandstop`

### **Upper passband edge frequency (rad/s)** — Upper passband edge frequency `80` (default) | scalar value

The upper passband edge frequency, specified in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

and `Filter
type` is set to:

- `Bandpass`
- `Bandstop`

### **Stopband edge frequency (rad/s)** — Stopband edge frequency `30` (default) | scalar value

The stopband edge frequency, specified in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Chebyshev II`

and `Filter
type` is set to:

- `Lowpass`
- `Highpass`

### **Lower stopband edge frequency (rad/s)** — Lower stopband edge frequency `30` (default) | scalar value

The lower stopband edge frequency, in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Chebyshev II`

and `Filter
type` is set to:

- `Bandpass`
- `Bandstop`

### **Upper stopband edge frequency (rad/s)** — Upper stopband edge frequency `80` (default) | scalar value

The upper stopband edge frequency, specified in rad/s.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Chebyshev II`

and `Filter
type` is set to:

- `Bandpass`
- `Bandstop`

### **Passband ripple in dB** — Passband ripple `2` (default) | scalar value

The passband ripple, specified in dB.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Chebyshev I`
- `Elliptic`

### **Stopband attenuation in dB** — Stopband attenuation `40` (default) | scalar value

The stopband attenuation, in dB.

**Tunable:** Yes

#### Dependencies

This parameter appears only when `Design
method` is set to:

- `Chebyshev II`
- `Elliptic`
## Libraries

DSP System Toolbox / Filtering / Filter Designs

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block is not recommended for production code generation.

Consider using the Model Discretizer (Simulink) to map this continuous block into a
discrete equivalent that supports code generation. To access the Model Discretizer,
on the **Apps** tab, under **Apps**, under
**Control Systems**, click **Model
Discretizer**.

## Version History

**Introduced before R2006a**

## Description

Design and implement analog filters

The Analog Filter Design block designs and implements a Butterworth,
Chebyshev type I, Chebyshev type II, elliptic, or bessel filter in a highpass, lowpass,
bandpass, or bandstop configuration.

You select the design and band configuration of the filter from the `Design
method` and `Filter type`
drop-down lists in the dialog box. For each combination of design method and band
configuration, an appropriate set of secondary parameters is displayed. For more
details, see Design/Band Combination Table.

The Analog Filter Design block uses a state-space filter representation, and applies
the filter using the State-Space (Simulink) block in the Simulink® Continuous library. All of the design methods use Signal Processing Toolbox™ functions to design the filter.

The Analog Filter Design block is built on the filter design capabilities of
Signal Processing Toolbox software.

**Note**

The Analog Filter Design block does not work with the Simulink discrete solver, which is enabled when you set the
**Solver** list to `Discrete (no continuous
states)` in the **Solver** pane of the
**Model Configuration Parameters** dialog box. Select one
of the continuous solvers (such as `ode4`) instead.
