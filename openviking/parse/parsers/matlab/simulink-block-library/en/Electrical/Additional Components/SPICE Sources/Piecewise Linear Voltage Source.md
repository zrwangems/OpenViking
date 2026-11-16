---
type: simulink-block
title: 'Piecewise Linear Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'piecewiselinearvoltagesource'
documentation_source_path: 'ref/piecewiselinearvoltagesource.html'
language: en
---

# Piecewise Linear Voltage Source

## Ports

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the piecewise linear voltage source positive
voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the piecewise linear voltage source negative
voltage

## Parameters

### **Time specification** — Vector of time values `[0, 1, 2, 3, 4]` `s` (default)

Vector of time values as a tabulated 1-by-*n* array. The time values
vector must be strictly monotonically increasing.

### **Current at specified time** — Vector of current values `[0, 0, 0, 0, 0]` `V` (default)

Vector of voltage values as a tabulated 1-by-*n* array. The voltage
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

## Libraries

Simscape / Electrical / Sources Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Time-dependent voltage source using lookup table

The Piecewise Linear Voltage Source block represents a
voltage source that you specify in lookup table form using a vector of time values and a vector
of the corresponding voltage values. You must specify at least two time-current value pairs. The
block generates a time-dependent voltage based on these time-voltage values using the selected
interpolation and extrapolation methods. You have a choice of two interpolation methods and
extrapolation methods. The output voltage is independent of the current through the
source.
