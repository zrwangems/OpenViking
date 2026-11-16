---
type: simulink-block
title: 'Second-Order Low-Pass Filter (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Filters'
documentation_page: 'secondorderlowpassfilterdiscreteorcontinuous'
documentation_source_path: 'ref/secondorderlowpassfilterdiscreteorcontinuous.html'
language: en
---

# Second-Order Low-Pass Filter (Discrete or Continuous)

## Ports

### Input

### **u** — Filter input scalar or vector

Filter input.

**Data Types:** `single` | `double`
### Output

### **y** — Filtered output scalar or vector

Filtered output. The output has the same number of elements as the input.

**Data Types:** `single` | `double`

## Parameters

### **Coefficient of s, A1** — *A1* coefficient `0.1` (default) | positive scalar

*A1*, the signal conditioning frequency filter coefficient of
*s*.

### **Coefficient of s^2, A2** — *A2* coefficient `0.2` (default) | positive scalar

*A2*, the signal conditioning frequency filter coefficient of
*s2*.

### **Initialization** — Initial state specification `Inherited from block input` (default) | `Specify as parameter`

Specify the initial state condition for this block. For more information,
see Initial Conditions.

### **Initial state** — Initial state `0` (default) | real number

Block initial state.

#### Dependencies

To enable this parameter, set **Initialization** to
`Specify as parameter`.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete-time or continuous-time second-order low-pass filter

The Second-Order Low-Pass Filter (Discrete or Continuous) block implements a
second-order low pass filter in conformance with IEEE Std 421.5-2016[1]. In
the standard, the filter is a single input, single output signal conditioner that is
used in the Power System Stabilizer PSS1A.

In the PSS1A, the filter accounts for some of the low-frequency effects of high-frequency
torsional filters. It can also help shape the gain and phase characteristics of the
stabilizer.

To switch between continuous and discrete implementations of the Second-Order
Low-Pass Filter (Discrete or Continuous) block, adjust the **Sample
time** parameter value.

### Initial Conditions

To specify the initial conditions of this block, set
**Initialization** to:

- `Inherited from block input` — The block sets
  the state and output initial conditions to the initial input.
- `Specify as parameter` — The block sets the
  state initial condition to the value of **Initial
  state**.
