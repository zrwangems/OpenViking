---
type: simulink-block
title: 'Battery Temperature Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'batterytemperaturemonitoring'
documentation_source_path: 'ref/batterytemperaturemonitoring.html'
language: en
---

# Battery Temperature Monitoring

## Ports

### Input

### **CellTemperature** — Cell temperature, K scalar | vector

Temperature of the battery cell, specified as a scalar for a single
cell or a vector for multiple cells.

If you select the
**Specify input as [Min,Max]** parameter, you must
specify a minimum and a maximum value for this port, for example
`CellTemperature=[CellTemperatureMin,CellTemperatureMax]`. *(since R2025a)*
### Output

### **UndertemperatureError** — Indication of undertemperature error, unitless `0` | `1`

Indication of an undertemperature error. If this output is equal to
`1`, the battery is in an undertemperature
state.

### **OvertemperatureError** — Indication of overtemperature error, unitless `0` | `1`

Indication of an overtemperature error. If this output is equal to
`1`, the battery is in an overtemperature
state.

## Parameters

### **Specify input as [Min,Max]** — Option to specify input as minimum and maximum values `off` (default) | `on`

*Since R2025a*

Option to specify the value at the **CellTemperature** input port as a vector of
minimum and maximum values. If you clear this parameter, you must specify an
individual value for the input port. The block then calculates the minimum
and maximum values internally.

### **Undertemperature limit** — Undertemperature limit `270` (default) | nonnegative scalar

Temperature limit under which the battery is in an undertemperature state.

### **Overtemperature limit** — Overtemperature limit `320` (default) | nonnegative scalar

Temperature limit over which the battery is in an undertemperature state. The value of
this parameter must be greater than the value of the
**Undertemperature limit** parameter.

### **Qualification time undertemperature (s)** — Undertemperature qualification time `2` (default) | positive scalar

Time required to qualify the undertemperature error, in seconds.

### **Disqualification time undertemperature (s)** — Undertemperature disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the undertemperature error, in seconds. If you
set this parameter to `0`, the block does not disqualify
the error.

### **Qualification time overtemperature (s)** — Overtemperature qualification time `2` (default) | positive scalar

Time required to qualify the overtemperature error, in seconds.

### **Disqualification time overtemperature (s)** — Overtemperature disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the overtemperature error, in seconds. If you
set this parameter to `0`, the block does not disqualify
the error.

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

### R2025a: Specify minimum and maximum values for **Temperature** input port

You can specify the minimum and maximum values for the **CellTemperature** input
port. To specify this input as a vector of minimum and maximum values, select the
**Specify input as [Min,Max]** parameter.

## Description

Monitor for battery temperature

The Battery Temperature Monitoring block monitors the temperature of a
battery. Temperature protection is necessary in electrical circuits. A battery that is
exposed to extremely high or extremely low temperatures can enter a dangerously unstable
state.

You can switch between continuous and discrete implementations of the block by using
the **Sample time (-1 for inherited)** parameter. To configure the
block for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the block for
discrete time, set the **Sample time (-1 for inherited)**
parameter to a positive, nonzero value, or to `-1` to inherit the
sample time from an upstream block.

This diagram illustrates the overall structure of the block:

### Equations

This block computes the undertemperature symptom with this equation:

Undertemperature Symptom=min(Temperature)≤ UndertemperatureLimit

This block computes the overtemperature symptom with this equation:

Overtemperature Symptom=max(Temperature)≥ OvertemperatureLimit

The Battery Temperature Monitoring block then passes the undertermperature
and overtemperature symptoms to a Fault
Qualification block, which qualifies the error.
