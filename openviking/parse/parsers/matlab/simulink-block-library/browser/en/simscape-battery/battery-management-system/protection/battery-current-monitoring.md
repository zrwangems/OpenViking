---
type: simulink-block
title: 'Battery Current Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'batterycurrentmonitoring'
documentation_source_path: 'ref/batterycurrentmonitoring.html'
language: en
---

# Battery Current Monitoring

## Ports

### Input

### **PackCurrent** — Battery pack current, A scalar

Battery pack current, in ampere, specified as a scalar.

### **ChargingLimit** — Charging current limit, A scalar

Charging current limit of the battery, in ampere, specified as a
scalar.

### **DischargingLimit** — Discharging current limit, A scalar

Discharging current limit of the battery, in ampere, specified as a
scalar.
### Output

### **OvercurrentError** — Indication of overcurrent error `0` | `1`

Indication of an overcurrent error. If this output is equal to
`1`, the battery is in an overcurrent state.

## Parameters

### **Current error limit (A)** — Current error limit `0` (default) | nonnegative scalar

Threshold to allow small deviation from the charging and discharging limits, in
ampere.

### **Qualification time (s)** — Error qualification time `2` (default) | positive scalar

Time required to qualify the error, in seconds.

### **Disqualification time (s)** — Error disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the error, in seconds. If you set this
parameter to `0`, the block does not disqualify the
error.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify this
parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that allows
you to switch between continuous operation and discrete operation, promote
the sample time parameter. Promoting the sample time parameter ensures
correct switching between the continuous and discrete implementations of the
block. For more information, see Promote Block Parameters on a Mask.

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

Simscape / Battery / BMS / Protection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Monitor for battery current

The Battery Current Monitoring block implements battery overcurrent
monitoring. Overcurrent protection is necessary in electrical circuits. A battery that
is exposed to overcurrent experiences a considerable increase in cell temperature and is
in a dangerously unstable state.

You can switch between continuous and discrete implementations of the block by using
the **Sample time (-1 for inherited)** parameter. To configure the
block for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the block for
discrete time, set the **Sample time (-1 for inherited)**
parameter to a positive, nonzero value, or to `-1` to inherit the
sample time from an upstream block.

This diagram shows the structure of the block:

### Equations

This block computes the overcurrent symptom with this equation:

Overcurrent Symptom=(i− Chargelimit)>ErrorLimit∥( DischargeLimit−i )>ErrorLimit.

The Battery Current Monitoring block then passes the overcurrent symptom to
a Fault
Qualification block, which qualifies the error.
