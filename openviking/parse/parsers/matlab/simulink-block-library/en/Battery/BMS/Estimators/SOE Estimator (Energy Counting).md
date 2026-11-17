---
type: simulink-block
title: 'SOE Estimator (Energy Counting)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'soeestimatorenergycounting'
documentation_source_path: 'ref/soeestimatorenergycounting.html'
language: en
---

# SOE Estimator (Energy Counting)

## Ports
```yaml
ports:
- name: Current
  summary: Battery current, ampere scalar | vector
  direction: input
- name: Voltage
  summary: Battery voltage, volt scalar | vector
  direction: input
- name: InitialSOE
  summary: Initial state of energy, unitless scalar | vector
  direction: input
- name: SOE
  summary: Battery state of energy scalar | vector
  direction: output
```

### Input

### **Current** — Battery current, ampere scalar | vector

Battery current, in ampere, specified as a scalar for a single cell or
a vector for multiple cells. To specify this input as a vector of cell
currents, select the **Specify Current input as cell
current(s)** parameter.

### **Voltage** — Battery voltage, volt scalar | vector

Battery voltage, in volt, specified as a scalar for a single cell or a
vector for multiple cells.

### **InitialSOE** — Initial state of energy, unitless scalar | vector

Initial state of energy, specified as a scalar or vector of entries in
the range [0, 1]. The size of this input port must be equal to the size
of the **Current** input port.
### Output

### **SOE** — Battery state of energy scalar | vector

State of energy of the battery, returned as a scalar or a vector. The
size of this output port is equal to the size of the
**Current** and **InitialSOE**
input ports.
## Parameters
```yaml
parameters:
- name: Specify Current input as cell current(s)
  summary: Option to specify current input port as vector off (default) | on
  group: ''
- name: Nominal cell energy capacity, Enom, (W\*Hr)
  summary: Nominal energy capacity of cell 113.1300 (default) | positive scalar
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time 1 (default) | 0 | -1 | integer
  group: ''
- name: Algorithm data type
  summary: 'Option to choose data type for block algorithm Inherit: auto (default) | double | single | <data type expression>'
  group: ''
```

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `off` (default) | `on`

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Nominal cell energy capacity, Enom, (W\*Hr)** — Nominal energy capacity of cell `113.1300` (default) | positive scalar

Nominal energy capacity of the battery cell, in watt-hour.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify this
parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote the sample time
parameter. Promoting the sample time parameter ensures correct switching
between the continuous and discrete implementations of the block. For more
information, see Promote Block Parameters on a Mask.

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

**Introduced in R2023b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

State of energy estimator with energy counting

The SOE Estimator (Energy Counting) block implements an estimator that
calculates the state of energy (SOE) of a battery by using the energy counting
method.

The SOE is the ratio of the remaining energy
*E*remain to the total energy
*E*total:

SOE=EremainEtotal.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

You can switch between continuous and discrete implementations of the block by using
the **Sample time (-1 for inherited)** parameter. To configure the
block for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the block for
discrete time, set the **Sample time (-1 for inherited)**
parameter to a positive, nonzero value, or to `-1` to inherit the
sample time from an upstream block.

**Note**

Continuous-time implementation of this block works only in a double-precision
floating-point simulation. If you provide single-precision floating-point parameters and
inputs, this block casts them to double-precision floating-point values to prevent
errors.

This diagram shows the structure of the block:

### Equations

To compute the SOE of the battery, the SOE Estimator (Energy Counting) block
uses this equation:

SOE=SOE(t0)+1Enom∫0tVt(t)i(t)dt

where *V*t is the
terminal voltage, *i* is the current, and
*E*nom is the battery nominal energy
capacity in watt-hour.
