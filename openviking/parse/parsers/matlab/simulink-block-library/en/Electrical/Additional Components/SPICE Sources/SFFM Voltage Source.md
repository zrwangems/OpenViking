---
type: simulink-block
title: 'SFFM Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'sffmvoltagesource'
documentation_source_path: 'ref/sffmvoltagesource.html'
language: en
---

# SFFM Voltage Source

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the SFFM voltage source
positive voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the SFFM voltage source
negative voltage

## Parameters

### **Voltage offset, VO** — Voltage offset `0` `V` (default)

Magnitude of the time-independent part of the output voltage.

### **Voltage amplitude, VA** — Voltage amplitude `0` `V` (default)

Magnitude of the sinusoidal part of the output voltage.

### **Carrier frequency, FC** — Carrier frequency `0` `Hz` (default) | nonnegative scalar

Frequency of the carrier wave. The value must be greater than or equal to
`0`.

### **Modulation index, MI** — Modulation index `0` (default) | nonnegative scalar

Amount by which the modulated signal varies around its unmodulated level.
The value must be greater than or equal to `0`.

### **Signal frequency, FS** — Signal frequency `0` `Hz` (default) | nonnegative scalar

Frequency of the modulated signal. The value must be greater than or equal
to `0`.

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Single-frequency frequency-modulated voltage source

The SFFM Voltage Source block represents a
frequency-modulated AC voltage source whose output voltage value is independent of the
current through the source. The following equation describes the output voltage as a
function of time:

Vout = VO+VA\*sin((2π\*FC\*Time)+MI\*sin(2π\*FS\*Time))

where:

- *V0* is the **Voltage offset, VO**
  parameter value.
- *VA* is the **Voltage amplitude, VA**
  parameter value.
- *FC* is the **Carrier frequency, FC**
  parameter value.
- *MI* is the **Modulation index, MI**
  parameter value.
- *FS* is the **Signal frequency, FS**
  parameter value.
