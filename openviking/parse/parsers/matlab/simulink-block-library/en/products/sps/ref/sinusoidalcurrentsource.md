---
type: simulink-block
title: 'Sinusoidal Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'sinusoidalcurrentsource'
documentation_source_path: 'ref/sinusoidalcurrentsource.html'
language: en
---

# Sinusoidal Current Source

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the sinusoidal current source positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the sinusoidal current source negative
terminal.

## Parameters

### **Current offset, IO** — Current offset `0` `A` (default)

The magnitude of the time-independent part of the output current.

### **Sinusoidal amplitude, IA** — Sinusoidal amplitude `0` `A` (default)

The magnitude of the sinusoidal part of the output current.

### **Sinusoidal frequency, FREQ** — Sinusoidal frequency `1e6` `Hz` (default)

The frequency of the output sine wave. The value can be less than
`0`.

### **Time delay, TD** — Time delay `0` `s` (default)

The time at which the sine wave first starts. A value less than `0`
indicates a phase shift of 180 degrees.

### **Damping factor, DF** — Damping factor `0` `1/s` (default) | nonnegative scalar

The exponential damping factor for the sine wave to produce the output current. If
*DF* is greater than or equal to `0`, the exponential part
of the equation is always damping for time greater than *TD*. The value must
be greater than or equal to `0`.

### **Include parallel conductance, GMIN** — Whether to include parallel conductance `Yes` (default) | `No`

Specify if the current source includes a parallel conductance. The value of the parallel conductance, *GMIN*, depends on whether your model contains an Environment Parameters block.

This table shows the possible values of the parallel conductance,
*GMIN*:

**Values of parallel conductance, GMIN**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **Model contains Environment Parameters block** | **Model does not contain Environment Parameters block** | Parallel conductance, *GMIN*, is not included and it does not affect the current source. | | |
| *GMIN* is equal to the value of the **GMIN** parameter in the Environment Parameters block. | *GMIN* = `1e-12` `Ohm` |

## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Damped sinusoidal current source

The Sinusoidal Current Source block represents a damped
sinusoidal current source whose output current is independent of the voltage across the terminals
of the source. The following equations describe the current through the source as a function of time:

Iout(Time≤TD)=IOIout(Time>TD)=IO+IA\*e−(Time−TD)\*DF\*sin(2π\*FREQ\*(Time−TD))

where:

- *I0* is the **Current offset, IO** parameter
  value.
- *IA* is the **Sinusoidal amplitude, IA** parameter
  value.
- *FREQ* is the **Sinusoidal frequency, FREQ** parameter
  value.
- *TD* is the **Time delay, TD** parameter value.
- *DF* is the **Damping factor, DF** parameter
  value.

The block uses a small conductance internally to prevent numerical simulation issues. The
conductance connects the + and - ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN** parameter of
  the Environment Parameters block, whose default value is
  `1e–12`.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the **GMIN**
  parameter to the desired value.
