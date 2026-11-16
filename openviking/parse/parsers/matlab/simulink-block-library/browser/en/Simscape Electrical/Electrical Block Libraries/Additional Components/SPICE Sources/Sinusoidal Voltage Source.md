---
type: simulink-block
title: 'Sinusoidal Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'sinusoidalvoltagesource'
documentation_source_path: 'ref/sinusoidalvoltagesource.html'
language: en
---

# Sinusoidal Voltage Source

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the sinusoidal voltage source positive
voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the sinusoidal voltage source negative
voltage

## Parameters

### **Voltage offset, VO** — Voltage offset `0` `V` (default)

Magnitude of the time-independent part of the output voltage.

### **Sinusoidal amplitude, VA** — Sinusoidal amplitude `0` `V` (default)

Magnitude of the sinusoidal part of the output voltage.

### **Sinusoidal frequency, FREQ** — Sinusoidal frequency `1e6` `Hz` (default)

Frequency of the output sine wave. The value can be less than
`0`.

### **Time delay, TD** — Time delay `0` `s` (default)

Time at which the sine wave first starts. A value less than `0`
indicates a phase shift of 180 degrees.

### **Damping factor, DF** — Damping factor `0` `1/s` (default) | nonnegative scalar

Exponential damping factor for the sine wave to produce the output voltage. If
*DF* is greater than or equal to `0`, the exponential part
of the equation is always damping for time greater than *TD*. The value must
be greater than or equal to `0`.

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Damped sinusoidal voltage source

The Sinusoidal Voltage Source block represents a damped
sinusoidal voltage source whose output voltage is independent of the current through the source.
The following equations describe the output as a function of time:

Vout(Time≤TD)=VOVout(Time>TD)=VO+VA\*e−(Time−TD)\*DF\*sin(2π\*FREQ\*(Time−TD))

where:

- *V0* is the **Voltage offset, VO** parameter
  value.
- *VA* is the **Sinusoidal amplitude, VA** parameter
  value.
- *FREQ* is the **Sinusoidal frequency, FREQ** parameter
  value.
- *TD* is the **Time delay, TD** parameter value.
- *DF* is the **Damping factor, DF** parameter
  value.
