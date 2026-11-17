---
type: simulink-block
title: 'AC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'acvoltagesource'
documentation_source_path: 'ref/acvoltagesource.html'
language: en
---

# AC Voltage Source

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the source positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the source negative terminal.
## Parameters
```yaml
parameters:
- name: Peak amplitude
  summary: Peak voltage amplitude 1 V (default) | scalar
  group: ''
- name: Phase shift
  summary: Phase shift in angular units 0 deg (default) | scalar
  group: ''
- name: Frequency
  summary: Voltage frequency 60 Hz (default) | positive scalar
  group: ''
```

### **Peak amplitude** — Peak voltage amplitude `1 V` (default) | scalar

Peak voltage amplitude.

### **Phase shift** — Phase shift in angular units `0 deg` (default) | scalar

Phase shift in angular units.

### **Frequency** — Voltage frequency `60 Hz` (default) | positive scalar

Voltage frequency, specified in Hz or units directly convertible to Hz (where Hz is
defined as 1/s). For example, kHz and MHz are valid units, but rad/s is not.
## Libraries

Simscape / Foundation Library / Electrical / Electrical Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal constant voltage source

The AC Voltage Source block represents an ideal voltage
source that maintains sinusoidal voltage across its output terminals, independent of the
current flowing through the source.

The output voltage is defined by the following equation:

V=V0⋅sin(2π⋅f⋅t+φ)

where:

- *V* is voltage.
- *V*0 is peak amplitude.
- *f* is frequency.
- *φ* is phase shift.
- *t* is time.

Connections **+** and **-** are conserving electrical
ports corresponding to the positive and negative terminals of the voltage source,
respectively. The current is positive if it flows from positive to negative, and the voltage
across the source is equal to the difference between the voltage at the positive and the
negative terminal, *V*(+) – *V*(-).
