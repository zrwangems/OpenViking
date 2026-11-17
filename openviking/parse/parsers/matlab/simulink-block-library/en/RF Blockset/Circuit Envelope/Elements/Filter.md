---
type: simulink-block
title: 'Filter'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'filter'
documentation_source_path: 'ref/filter.html'
language: en
---

# Filter

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Design method
  summary: Simulation type Butterworth (default) | Chebyshev | Inverse Chebyshev | Ideal
  group: Main
- name: Filter type
  summary: Filter type Lowpass (default) | Highpass | Bandpass | Bandstop
  group: Main
- name: Implementation
  summary: Implementation LC Tee | LC Pi | Transfer function | Constant per carrier | Frequency Domain
  group: Main
- name: Passband edge frequency
  summary: Passband edge frequency 1 GHz (default) | scalar
  group: Main
- name: Implement using filter order
  summary: Implement using filter order off (default) | on
  group: Main
- name: Filter order
  summary: Filter order 3 (default) | scalar
  group: Main
- name: Passband frequency
  summary: Passband frequency for lowpass and highpass filters scalar
  group: Main
- name: Passband frequencies
  summary: Passband frequencies for bandpass filters [2 3] GHz (default) | 2-tuple vector
  group: Main
- name: Passband attenuation (dB)
  summary: Passband attenuation 10*log10(2) (default) | scalar
  group: Main
- name: Stopband frequencies
  summary: Stopband frequencies for bandstop filters [2.1 2.9] GHz (default) | 2-tuple vector
  group: Main
- name: Stopband attenuation (dB)
  summary: Stopband attenuation 40 (default) | scalar
  group: Main
- name: Source impedance (Ohm)
  summary: Input source resistance 50 (default) | scalar
  group: Main
- name: Load impedance (Ohm)
  summary: Output load resistance 50 (default) | scalar
  group: Main
- name: Ground and hide negative terminals
  summary: Ground RF circuit terminals on (default) | off
  group: Main
- name: Export
  summary: Save filter design to a file button
  group: Main
- name: Parameter 1
  summary: Type of plots on y-axis Voltage transfer (default) | Phase delay | Group delay
  group: Visualization
- name: Parameter 2
  summary: Type of plots None (default) | Voltage transfer | Phase delay | Group delay
  group: Visualization
- name: Format 1
  summary: Scaling of y-axis Magnitude (decibels) (default) | Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: Visualization
- name: Format 2
  summary: Scaling of y-axis Magnitude (decibels) (default) | Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: Visualization
- name: Frequency points
  summary: Frequency points to plot on x-axis logspace(0,10,101) Hz (default) | vector
  group: Visualization
- name: X-axis scale
  summary: X-axis scale Linear (default) | Logarithmic
  group: Visualization
- name: Y-axis scale
  summary: Y-axis scale Linear (default) | Logarithmic
  group: Visualization
```

### Main

### **Design method** — Simulation type `Butterworth` (default) | `Chebyshev` | `Inverse Chebyshev` | `Ideal`

Simulation type, specified as one of the following:

- `Ideal` — Simulates an ideal filter
  of the type specified in **Filter type** and
  the model specified in
  **Implementation**.
- `Butterworth` — Simulates a
  Butterworth filter of the type specified in **Filter
  type** and the model specified in
  **Implementation**.
- `Chebyshev` — Simulates a Chebyshev
  filter of the type specified in **Filter type**
  and the model specified in **Implementation**.
- `Inverse Chebyshev` — Simulates a
  inverse Chebyshev filter of the type specified in
  **Filter type** and the
  `Transfer function` model specified
  in **Implementation**.

### **Filter type** — Filter type `Lowpass` (default) | `Highpass` | `Bandpass` | `Bandstop`

Filter type, specified as one of the following:

- `Lowpass` — Simulates a lowpass
  filter type of the design specified in **Design
  method**.
- `Highpass` — Simulates a highpass
  filter type of the design specified in **Design
  method**.
- `Bandpass` — Simulates a bandpass
  filter type of the design specified in **Design
  method**.
- `Bandstop` — Simulates a bandstop
  filter type of the design specified in **Design
  method**.

### **Implementation** — Implementation `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

Implementation, specified as one of the following:

- `LC Tee` — Model an analog filter
  with an LC lumped Tee structure when the **Design
  method** is Butterworth or Chebyshev.
- `LC Pi` — Model an analog filter with
  an LC lumped Pi structure when the **Design
  method** is Butterworth or Chebyshev.
- `Transfer Function` — Model an analog
  filter using two-port S-parameters when the **Design
  method** is Butterworth or Chebyshev.
- `Constant per carrier` — Model a
  filter with either full transmission or full reflection set as
  constant throughout the entire envelope band around each
  carrier.The **Design method** is specified
  as ideal.
- `Frequency Domain` — Model a filter
  using convolution with an impulse response. The **Design
  method** is specified as ideal. The impulse
  response is computed independently for each carrier frequency to
  capture the ideal filtering response. When a transition between
  full transmission and full reflection of the ideal filter occurs
  within the envelope band around a carrier, the frequency-domain
  implementation captures this transition correctly up to a
  frequency resolution specified in **Impulse response
  duration**.

By default, the **Implementation** is
`Constant per carrier` for an ideal filter
and `LC Tee` for Butterworth or Chebyshev.

**Note**

Due to causality, a delay of half the impulse response
duration is included for both reflected and transmitted signals.
This delay will impair the filter performance when the source
and load resistances differ from the values specified as filter
parameters.

### **Passband edge frequency** — Passband edge frequency `1 GHz` (default) | scalar

Passband edge frequency, specified as a scalar in Hz, kHz, MHz, or
GHz.

#### Dependencies

To enable this parameter, set **Design method**
to `Ideal`.

### **Implement using filter order** — Implement using filter order `off` (default) | `on`

Select this parameter to implement the filter order manually.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev`.

### **Filter order** — Filter order `3` (default) | scalar

Filter order, specified as a scalar within the range between [2, 60].
This order is the number of lumped storage elements in
`lowpass` or `highpass`. In
`bandpass` or `bandstop`, the
number of lumped storage (L and C) elements are twice the value.

**Note**

For even order Chebyshev filters, the resistance ratio RloadRsource>Rratio for Tee network implementation and RloadRsource<1Rratio for Pi network implementation.

Rratio = 1+ε2+ε1+ε2−ε

where:

- ε = 10(0.1Rp)−1

- *R*p is
  the passband ripple in dB.

#### Dependencies

To enable this parameter, select **Implement using filter
order**.

### **Passband frequency** — Passband frequency for lowpass and highpass filters scalar

Passband frequency for low[pass and highpass filters specified as a
scalar in Hz, kHz, MHz, or GHz. Based on the **Filter
type** you select, the default value of this parameter
varies. The default values are listed in this table.

| Filter Type | Default value of passband frequency |
| --- | --- |
| `Lowpass` | `1 GHz` |
| `Highpass` | `2 GHz` |

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev` and **Filter
type** to `Lowpass` , or
`Highpass`.

### **Passband frequencies** — Passband frequencies for bandpass filters `[2 3] GHz` (default) | 2-tuple vector

Passband frequencies for bandpass filters, specified as a 2-tuple
vector in Hz, kHz, MHz, or GHz. This option is not available for
bandstop filters.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev` and **Filter
type** to `Bandpass`.

### **Passband attenuation (dB)** — Passband attenuation `10*log10(2)` (default) | scalar

Passband attenuation, specified as a scalar dB. For bandpass filters,
this value is applied equally to both edges of the passband.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev`.

### **Stopband frequencies** — Stopband frequencies for bandstop filters `[2.1 2.9] GHz` (default) | 2-tuple vector

Stopband frequencies for bandstop filters, specified as a 2-tuple
vector in Hz, kHz, MHz, or GHz. This option is not available for
bandpass filters.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev` and **Filter
type** to `Bandstop`.

### **Stopband attenuation (dB)** — Stopband attenuation `40` (default) | scalar

Stopband attenuation, specified as a scalar dB. For bandstop filters,
this value is applied equally to both edges of the stopband.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev` and **Filter
type** to `Bandstop`.

### **Source impedance (Ohm)** — Input source resistance `50` (default) | scalar

Input source resistance, specified as a scalar in ohms.

**Note**

The source and load impedances must be equal when
**Implementation** is set to
`Transfer function`.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev`.

### **Load impedance (Ohm)** — Output load resistance `50` (default) | scalar

Output load resistance, specified as a scalar in ohms.

**Note**

The source and load impedances must be equal when
**Implementation** is set to
`Transfer function`.

#### Dependencies

To enable this parameter, set **Design method**
to `Butterworth` or
`Chebyshev`.

### **Ground and hide negative terminals** — Ground RF circuit terminals `on` (default) | `off`

Select to internally ground and hide the negative terminals. Clear to
expose the negative terminals. When the terminals are exposed, you can
connect them to other parts of your model.

### **Export** — Save filter design to a file button

Use this button to save filter design to a MAT or TXT file. For more
information, see Export Your Filter Design.

### Visualization

### **Parameter 1** — Type of plots on y-axis `Voltage transfer` (default) | `Phase delay` | `Group delay`

Type of plots, specified as `Voltage
transfer`, `Phase delay`, or
`Group delay`.

### **Parameter 2** — Type of plots `None` (default) | `Voltage transfer` | `Phase delay` | `Group delay`

Type of plots, specified as `None`,
`Voltage transfer`, `Phase
delay`, or `Group
delay`.

### **Format 1** — Scaling of y-axis `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

Scaling of y-axis, specified as,

- `Magnitude(decibels)`,
  `Magnitude(linear)` or
  `Angle(degrees)`, `Real`,
  or `Imaginary` for `Voltage
  transfer` parameters.
- `Magnitude(decibels)` or
  `Magnitude(linear)` for `Phase
  delay` or `Group delay`
  parameters.

### **Format 2** — Scaling of y-axis `Magnitude (decibels)` (default) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

Scaling of y-axis, specified as,

- `Magnitude(decibels)`,
  `Magnitude(linear)` or
  `Angle(degrees)`, `Real`,
  or `Imaginary` for `Voltage
  transfer` parameters.
- `Magnitude(decibels)` or
  `Magnitude(linear)` for `Phase
  delay` or `Group delay`
  parameters.

### **Frequency points** — Frequency points to plot on x-axis `logspace(0,10,101) Hz` (default) | vector

Frequency points to plot on x-axis, specified as a vector with each
element units in Hz, kHz, MHz, or GHz.

### **X-axis scale** — X-axis scale `Linear` (default) | `Logarithmic`

X-axis scale, specified as `Linear` or
`Logarithmic`.

### **Y-axis scale** — Y-axis scale `Linear` (default) | `Logarithmic`

Y-axis scale, specified as `Linear` or
`Logarithmic`.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Model RF Filter

The Filter block models RF filters of four designs:

- Butterworth — Butterworth filters have a magnitude response that is maximally
  flat in the passband and monotonic overall. This smoothness comes at the price
  of decreased roll-off steepness.
- Chebyshev — Chebyshev Type I filters have ripples of equal magnitude in the
  passband and monotonic in the stopband.
- Inverse Chebyshev — Chebyshev Type II filters have ripples of equal magnitude
  in the stopband and monotonic in the passband.
- Ideal — Ideal filters perfectly allow frequencies in the passband and
  completely reject frequencies in the stopband.

To filter RF complex baseband signals in Simulink, use the Idealized Baseband Filter
block.
