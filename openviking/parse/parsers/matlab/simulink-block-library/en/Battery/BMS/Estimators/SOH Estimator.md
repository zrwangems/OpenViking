---
type: simulink-block
title: 'SOH Estimator'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'sohestimator'
documentation_source_path: 'ref/sohestimator.html'
language: en
---

# SOH Estimator

## Ports
```yaml
ports:
- name: SOC
  summary: State of charge of battery, unitless scalar | vector
  direction: input
- name: Temperature
  summary: Cell temperature scalar | vector
  direction: input
- name: R0
  summary: Terminal resistance, ohm scalar | vector
  direction: input
- name: SOH
  summary: State of health of battery scalar | vector
  direction: output
```

### Input

### **SOC** — State of charge of battery, unitless scalar | vector

State of charge of the battery, specified as a scalar or vector of
entries in the range [0, 1]. The size of this input port must be equal
to the size of the **Temperature** and
**R0** input ports.

### **Temperature** — Cell temperature scalar | vector

Temperature of a battery cell, specified as a scalar for a single cell or a vector for
multiple cells. The size of this input port must be equal to the size of
the **SOC** and **R0** input
ports.

### **R0** — Terminal resistance, ohm scalar | vector

Terminal resistance, specified as a scalar for a single cell or a
vector for multiple cells. The size of this input port must be equal to
the size of the **SOC** and
**Temperature** input ports.
### Output

### **SOH** — State of health of battery scalar | vector

State of health of the battery, returned as a scalar or vector of
entries in the range [0, 1]. The size of this output port is equal to
the size of the vectors at the input ports.
## Parameters
```yaml
parameters:
- name: Vector of state-of-charge values, SOC (-)
  summary: SOC breakpoints [0, .1, .25, .5, .75, .9, 1] (default) | vector of nonnegative scalars between 0 and 1
  group: ''
- name: Vector of temperatures, T
  summary: Temperature breakpoints [278, 293, 313] (default) | vector of positive scalars
  group: ''
- name: Terminal resistance when battery cell is new, R0new(SOC,T), (ohm)
  summary: Terminal resistance when battery cell is new [.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107,
    .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089] (default) | matrix of nonnegative scalars
  group: ''
- name: Terminal resistance at end of life, R0eol(SOC,T), (ohm)
  summary: Terminal resistance at end of life [.0234,.017,.018;.022,.017,.018;.0228,.0174,.0184;.0214,.0164,.0176;.0214,.0166,.0182;.0226,.017,.0178;.0232,.017,.0178]
    (default) | matrix of nonnegative scalar
  group: ''
- name: Algorithm data type
  summary: 'Option to choose data type for block algorithm Inherit: auto (default) | double | single | <data type expression>'
  group: ''
```

### **Vector of state-of-charge values, SOC (-)** — SOC breakpoints `[0, .1, .25, .5, .75, .9, 1]` (default) | vector of nonnegative scalars between `0` and `1`

Vector of SOC breakpoints defining the points at which you specify lookup data. This
vector must be strictly ascending.

### **Vector of temperatures, T** — Temperature breakpoints `[278, 293, 313]` (default) | vector of positive scalars

Vector of temperature breakpoints defining the points at which you specify
lookup data. This vector must be strictly ascending and greater than
`0`
`K`. The physical unit of this parameter must be
the same as the physical unit of the **Temperature** input
port.

### **Terminal resistance when battery cell is new, R0new(SOC,T), (ohm)** — Terminal resistance when battery cell is new `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]` (default) | matrix of nonnegative scalars

Terminal resistance when the battery cell is new, in ohm. The number of
rows of this matrix is equal to the size of the **Vector of
state-of-charge values, SOC (-)** parameter. The number of
columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### **Terminal resistance at end of life, R0eol(SOC,T), (ohm)** — Terminal resistance at end of life `[.0234,.017,.018;.022,.017,.018;.0228,.0174,.0184;.0214,.0164,.0176;.0214,.0166,.0182;.0226,.017,.0178;.0232,.017,.0178]` (default) | matrix of nonnegative scalar

Terminal resistance when the battery is at the end of its life, in ohm. The number of
rows of this matrix is equal to the size of the **Vector of
state-of-charge values, SOC (-)** parameter. The number of
columns of this matrix is equal to the size of the **Vector of
temperatures, T** parameter.

### **Algorithm data type** — Option to choose data type for block algorithm `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*Since R2025a*

Option to choose the data type for the block algorithm, specified as one of these values:

- `Inherit: auto` — You can simulate the block in
  both `single` and `double`
  precision. You must explicitly provide the inputs and parameters as either
  `single` or
  `double`.
- `double` — The block algorithm casts all inputs
  and parameters to `double` data type.
- `single` — The block algorithm casts all inputs
  and parameters to `single` data type.
- `<data type expression>` — The block
  algorithm casts all inputs and parameters to the data type object you
  specify.

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant and Control Data Types of Signals.
## Libraries

Simscape / Battery / BMS / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

State of health estimator

The SOH Estimator block implements an estimator that calculates the state of
health (SOH) of a battery. The SOH reflects the condition of a battery relative to its
ideal conditions. Health variations imply that the capacity and power of the battery
fade over time.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable single-precision floating-point simulation, the data type of all inputs and
parameters must be `single`.

This diagram shows the structure of the block:

### Equations

The terminal resistance *R*0 is an important
indicator of the aging of a battery. You can estimate the terminal resistance by
using the SOC Estimator
(Adaptive Kalman Filter) block. The SOH Estimator block
computes the SOH as a function of the terminal resistance
*R*0:

SOH=REOL−R0REOL−R0,new

where *R*EOL is the
end-of-life resistance and *R*0,new is the
terminal resistance when the battery is new.
