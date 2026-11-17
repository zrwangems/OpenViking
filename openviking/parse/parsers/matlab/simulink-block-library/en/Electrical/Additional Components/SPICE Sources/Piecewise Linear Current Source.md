---
type: simulink-block
title: 'Piecewise Linear Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'piecewiselinearcurrentsource'
documentation_source_path: 'ref/piecewiselinearcurrentsource.html'
language: en
---

# Piecewise Linear Current Source

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

Electrical conserving port associated with the piecewise linear current source positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the piecewise linear current source negative
terminal.
## Parameters
```yaml
parameters:
- name: Time specification
  summary: Vector of time values [0, 1, 2, 3, 4] s (default)
  group: ''
- name: Current at specified time
  summary: Vector of current values [0, 0, 0, 0, 0] A (default)
  group: ''
- name: Interpolation method
  summary: Interpolation method Linear (default) | Smooth
  group: ''
- name: Extrapolation method
  summary: Extrapolation method Nearest (default) | Linear
  group: ''
- name: Include parallel conductance, GMIN
  summary: Whether to include parallel conductance Yes (default) | No
  group: ''
```

### **Time specification** — Vector of time values `[0, 1, 2, 3, 4]` `s` (default)

Vector of time values as a tabulated 1-by-*n* array. The time values
vector must be strictly monotonically increasing.

### **Current at specified time** — Vector of current values `[0, 0, 0, 0, 0]` `A` (default)

Vector of current values as a tabulated 1-by-*n* array. The current
values vector must be the same size as the time values vector.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Select the method that the block uses to determine the output current values at
intermediate time points that are not specified in the preceding vectors:

- `Linear` — Prioritize performance by using a linear
  function.
- `Smooth` — Prioritize accuracy by producing a
  continuous curve with continuous first-order derivatives.

### **Extrapolation method** — Extrapolation method `Nearest` (default) | `Linear`

Select the method that the block uses to determine the output current values at time
points that are outside the time range specified in the preceding vectors:

- `Nearest` — Select this option to use the nearest
  input value for extrapolation.
- `Linear` — Select this option to use a linear
  function.

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

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Time-dependent current source using lookup table

The Piecewise Linear Current Source block represents a
current source that you specify in lookup table form using a vector of time values and a vector
of the corresponding current values. You must specify at least two time-current value pairs. The
block generates a time-dependent current based on these time-current values using the selected
interpolation and extrapolation methods. You have a choice of two interpolation methods and
extrapolation methods. The output current is independent of the voltage across the terminals of
the source.

The block uses a small conductance internally to prevent numerical simulation issues. The
conductance connects the **+** and **-** ports of the device
and has a conductance *GMIN*:

- By default, *GMIN* matches the **GMIN** parameter of
  the Environment Parameters block, whose default value is
  `1e–12``1/Ohm`.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the **GMIN**
  parameter to the desired value.
