---
type: simulink-block
title: 'Current Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'currentsourcethreephase'
documentation_source_path: 'ref/currentsourcethreephase.html'
language: en
---

# Current Source (Three-Phase)

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
- name: Current (phase RMS)
  summary: RMS phase current 100 / sqrt(2) A (default)
  group: ''
- name: Phase shift
  summary: Phase shift 0 deg (default)
  group: ''
- name: Frequency
  summary: Current frequency 60 Hz (default)
  group: ''
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Current (phase RMS)** — RMS phase current `100 / sqrt(2)` `A` (default)

RMS phase current.

### **Phase shift** — Phase shift `0` `deg` (default)

Phase shift, in angular units.

### **Frequency** — Current frequency `60` `Hz` (default)

Current frequency, specified in Hz or units directly convertible to Hz
(where Hz is defined as 1/s). For example, `kHz` and
`MHz` are valid units, but `rad/s` is
not.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Ideal three-phase current source

The Current Source (Three-Phase) block models an ideal
three-phase current source that maintains sinusoidal currents of the specified magnitude
through its terminals, independent of the voltage across the source.

The output current is defined by the following equations:

I0=2iphase\_rms

ia=I0sin(2πft+φ)

ib=I0sin(2πft+φ−120∘)

ic=I0sin(2πft+φ+120∘),

where:

- *I0* is the peak phase current.
- *iphase\_rms* is the RMS phase
  current.
- *ia*,
  *ib*,
  *ic* are the respective phase
  currents.
- *f* is the frequency.
- *φ* is the phase shift.
- *t* is the time.

The arrow indicates the positive direction of the current flow. The source has a wye
configuration, and port **n** provides a connection to the center of
the wye.
