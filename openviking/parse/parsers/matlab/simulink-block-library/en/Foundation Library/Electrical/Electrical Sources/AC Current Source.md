---
type: simulink-block
title: 'AC Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'accurrentsource'
documentation_source_path: 'ref/accurrentsource.html'
language: en
---

# AC Current Source

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the source positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the source negative terminal.

## Parameters

### **Peak amplitude** — Peak current amplitude `1 A` (default) | scalar

Peak current amplitude.

### **Phase shift** — Phase shift in angular units `0 deg` (default) | scalar

Phase shift in angular units.

### **Frequency** — Current frequency `60 Hz` (default) | positive scalar

Current frequency, specified in Hz or units directly convertible to Hz (where Hz is
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

Ideal sinusoidal current source

The AC Current Source block represents an ideal current
source that maintains sinusoidal current through it, independent of the voltage across its
terminals.

The output current is defined by the following equation:

I=I0⋅sin(2π⋅f⋅t+φ)

where:

- *I* is current.
- *I*0 is peak amplitude.
- *f* is frequency.
- *φ* is phase shift.
- *t* is time.

The positive direction of the current flow is indicated by the arrow.
