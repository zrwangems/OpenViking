---
type: simulink-block
title: 'SFFM Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'sffmcurrentsource'
documentation_source_path: 'ref/sffmcurrentsource.html'
language: en
---

# SFFM Current Source

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the SFFM current source
positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the SFFM current source
negative terminal.

## Parameters

### **Current offset, IO** — Current offset `0` `A` (default)

Magnitude of the time-independent part of the output current.

### **Current amplitude, IA** — Current amplitude `0` `A` (default)

Magnitude of the sinusoidal part of the output current.

### **Carrier frequency, FC** — Carrier frequency `0` `Hz` (default) | nonnegative scalar

Frequency of the carrier wave. The value must be greater than or equal to
`0`.

### **Modulation index, MI** — Modulation index `0` (default) | nonnegative scalar

Amount by which the modulated signal varies around its unmodulated level.
The value must be greater than or equal to `0`.

### **Signal frequency, FS** — Signal frequency `0` `Hz` (default) | nonnegative scalar

Frequency of the modulated signal. The value must be greater than or equal
to `0`.

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

Single-frequency frequency-modulated current source

The SFFM Current Source block represents a
frequency-modulated AC current source whose output current value is independent of the
voltage across its terminals. The following equation describes the current through the
source as a function of time:

Iout = IO+IA\*sin((2π\*FC\*Time)+MI\*sin(2π\*FS\*Time))

where:

- *I0* is the **Current offset, IO**
  parameter value.
- *IA* is the **Current amplitude, IA**
  parameter value.
- *FC* is the **Carrier frequency, FC**
  parameter value.
- *MI* is the **Modulation index, MI**
  parameter value.
- *FS* is the **Signal frequency, FS**
  parameter value.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the + and - ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is 1e–12.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
