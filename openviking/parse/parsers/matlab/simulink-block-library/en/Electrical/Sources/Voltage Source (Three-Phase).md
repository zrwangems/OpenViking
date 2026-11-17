---
type: simulink-block
title: 'Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'voltagesourcethreephase'
documentation_source_path: 'ref/voltagesourcethreephase.html'
language: en
---

# Voltage Source (Three-Phase)

## Ports
```yaml
ports:
- name: '~'
  summary: Three-phase port electrical
  direction: conserving
- name: n
  summary: Wye center electrical
  direction: conserving
```

### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
port associated with the three phases, *a*,
*b*, and *c*.

### **n** — Wye center electrical

Electrical conserving port associated with the center of the
wye.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: ''
- name: Rated voltage (phase-to-phase RMS)
  summary: RMS line voltage sqrt(3) * 100 / sqrt(2) V (default)
  group: Main
- name: Phase shift
  summary: Phase shift 0 deg (default)
  group: Main
- name: Frequency
  summary: Voltage frequency 60 Hz (default)
  group: Main
- name: Source impedance
  summary: Source impedance method X/R Ratio (default) | None | Series R | Series L | Series RL
  group: Main
- name: Short-circuit power level
  summary: Short-circuit power level 1e6 V*A (default)
  group: Main
- name: Source X/R ratio
  summary: Reactance-to-resistance ratio 15 (default)
  group: Main
- name: Source resistance
  summary: Source resistance 0.01 Ohm (default)
  group: Main
- name: Source inductance
  summary: Source inductance 3.97e-4 H (default)
  group: Main
- name: Source harmonics
  summary: Source Harmonics None (default) | Generate harmonics
  group: Harmonics
- name: Harmonic orders
  summary: Harmonic orders [5, 7, 11, 13] (default)
  group: Harmonics
- name: Harmonic magnitude to peak magnitude ratios
  summary: Harmonic magnitude to peak magnitude ratios [.1, .1, .1, .1] (default)
  group: Harmonics
- name: Source impedance parasitic parallel conductance
  summary: Source impedance parasitic parallel conductance 0 1/Ohm (default)
  group: Parasitics
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### Main

### **Rated voltage (phase-to-phase RMS)** — RMS line voltage `sqrt(3) * 100 / sqrt(2)` `V` (default)

RMS phase-to-phase, or line, voltage.

### **Phase shift** — Phase shift `0` `deg` (default)

Phase shift in angular units.

### **Frequency** — Voltage frequency `60` `Hz` (default)

Voltage frequency, specified in Hz or units directly convertible to Hz
(where Hz is defined as 1/s). For example, `kHz` and
`MHz` are valid units, but `rad/s`
is not.

### **Source impedance** — Source impedance method `X/R Ratio` (default) | `None` | `Series R` | `Series L` | `Series RL`

Choose a method for specifying source impedance. The default option is
`X/R Ratio`. Selecting any other options
enables other parameters. The options are:

- `None`
- `X/R Ratio`
- `Series R`
- `Series L`
- `Series RL`

### **Short-circuit power level** — Short-circuit power level `1e6` `V*A` (default)

Short-circuit power level.

#### Dependencies

This parameter is visible only when you select `X/R
Ratio` for the **Source
Impedance** parameter.

### **Source X/R ratio** — Reactance-to-resistance ratio `15` (default)

Complex impedance, that is, the reactance-to-resistance ratio.

#### Dependencies

This parameter is visible only when you select `X/R
Ratio` for the **Source
Impedance** parameter.

### **Source resistance** — Source resistance `0.01` `Ohm` (default)

Source resistance.

#### Dependencies

This parameter is visible only when you select `Series
R` or `Series RL` for the
**Source Impedance** parameter.

### **Source inductance** — Source inductance `3.97e-4` `H` (default)

Source inductance.

#### Dependencies

This parameter is visible only when you select `Series
L` or `Series RL` for the
**Source Impedance** parameter.

### Harmonics

### **Source harmonics** — Source Harmonics `None` (default) | `Generate harmonics`

Choose between `None` and
`Generate harmonics`. The default value is
`None`.

### **Harmonic orders** — Harmonic orders `[5, 7, 11, 13]` (default)

A row-vector of additional integer harmonic orders at which harmonics
are to be generated.

#### Dependencies

This parameter is visible only when you select
`Generate harmonics` for the
**Source representation** parameter.

### **Harmonic magnitude to peak magnitude ratios** — Harmonic magnitude to peak magnitude ratios `[.1, .1, .1, .1]` (default)

A row-vector of ratios of harmonic magnitudes relative to the
fundamental magnitude.

#### Dependencies

This parameter is visible only when you select
`Generate harmonics` for the
**Source representation** parameter.

### Parasitics

### **Source impedance parasitic parallel conductance** — Source impedance parasitic parallel conductance `0` `1/Ohm` (default)

Source impedance parasitic parallel conductance.

#### Dependencies

This parameter is visible only when you select `X/R
Ratio`, `Series L` or
`Series RL` for the **Source
Impedance** parameter.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Ideal three-phase voltage source with optional harmonics

The Voltage Source (Three-Phase) block models an ideal
three-phase voltage source or a three-phase voltage source with harmonics. You specify
the configuration using the Source representation parameter.

When you select `None` for the **Source
Impedance** parameter, the Voltage Source
block models an ideal three-phase voltage source that maintains sinusoidal voltage of
the specified magnitude across its terminals, independently of the current flowing
through the source.

The source has a wye configuration, and port **n** provides a
connection to the center of the wye. Port **~** is an expandable three-phase port representing the three phases,
*a*, *b*, and *c*. The current is
positive if it flows from the center of the wye to the positive terminal, and the
voltage across each phase is equal to the difference between the voltage at the positive
terminal and the center of the wye, *V*(+) – *V*n.

### Equations

The output voltage for the Voltage Source block is
defined by these equations:

v=vDC+vACsin(2πft+ϕ)+vN

va=V0sin(2πft+φ)

vN=Pv/2N(0,1)h

vc=V0sin(2πft+φ+120∘),

where:

- *V0* is the peak phase
  voltage.
- *vline\_rms* is the root-mean
  square (RMS) phase-to-phase voltage.
- *va*,
  *vb*,
  *vc* are the respective
  phase voltages.
- *f* is frequency.
- *φ* is the phase shift.
- *t* is time.

When you specify the three-phase voltage source with harmonics representation, the
output voltage for the Voltage Source block is
defined by these equations:

V0=23vline\_rmsHratios

va=V0sin((2πft+φ)Horders')

vb=V0sin((2πft+φ−θ)Horders'​)

vc=V0sin((2πft+φ+θ)Horders'),

where:

- *V0* is a row-vector
  containing the peak voltage of the fundamental and harmonic
  sinusoids.
- *vline\_rms* is the RMS
  phase-to-phase voltage.
- *Hratios* is a row-vector of
  harmonic ratios. The first element is 1 to represent the
  fundamental.
- *Horders* is a row-vector of
  harmonic orders. The first element is 1 to represent the
  fundamental.
- *va*,
  *v*b,
  *v*c are the respective
  phase voltages.
- *f* is a column-vector of harmonic frequencies. The
  first element is the fundamental frequency.
- *φ* is a column-vector of harmonic phase shifts. The
  first element is the fundamental phase shift.
- *θ* is a column-vector of harmonic phase offsets. The
  first element is `120°`.
- *t* is the time.

When you select `X/R ratio` for the **Source
Impedance** parameter, the equations for source impedance are:

R=vline\_rms2Ssc1+ϕ2

X=Rϕ

L=X2πf,

where:

- *Ssc* is the
  **Short-circuit power level** that you
  specify.
- *ϕ* is the **Source X/R ratio** that
  you specify.
- *R* is the calculated source resistance.
- *X* is the calculated source reactance.
- *L* is the calculated source inductance.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
