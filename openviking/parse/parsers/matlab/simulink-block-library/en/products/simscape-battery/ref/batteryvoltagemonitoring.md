---
type: simulink-block
title: 'Battery Voltage Monitoring'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Protection\u200b'
documentation_page: 'batteryvoltagemonitoring'
documentation_source_path: 'ref/batteryvoltagemonitoring.html'
language: en
---

# Battery Voltage Monitoring

## Ports

### Input

### **CellVoltage** — Cell voltage, V scalar | vector

Cell voltage, in volt, specified as a scalar for a single cell or a
vector for multiple cells.

### **PackVoltage** — Battery pack voltage, V scalar

Battery pack voltage, in volt, specified as a scalar.
### Output

### **UndervoltageError** — Indication of undervoltage error `0` | `1`

Indication of an undervoltage error. If this output is equal to
`1`, the battery is in an undervoltage
state.

### **OvervoltageError** — Indication of overvoltage error `0` | `1`

Indication of an overvoltage error. If this output is equal to
`1`, the battery is in an overvoltage state.

### **SensoryFaultyError** — Indication of sensor faulty error `0` | `1`

Indication of a sensor faulty error. If this output is equal to
`1`, the sensor is faulty.

## Parameters

### **Undervoltage limit (V)** — Undervoltage limit `2.5` (default) | positive scalar

Voltage limit under which the battery is in an undervoltage state, in volt.

### **Overvoltage limit (V)** — Overvoltage limit `4.5` (default) | positive scalar

Voltage limit over which the battery is in an overvoltage state, in volt. The value of
this parameter must be greater than the value of the **Undervoltage
limit (V)** parameter.

### **Voltage sensor fault threshold (V)** — Threshold for voltage sensor fault `0.25` (default) | positive scalar

Voltage threshold over which the sensor is faulty, in volt.

### **Qualification time undervoltage (s)** — Undervoltage qualification time `2` (default) | positive scalar

Time required to qualify the undervoltage error, in seconds.

### **Disqualification time undervoltage (s)** — Undervoltage disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the undervoltage error, in seconds. If you set
this parameter to `0`, the block does not disqualify the
error.

### **Qualification time overvoltage (s)** — Overvoltage qualification time `2` (default) | positive scalar

Time required to qualify the overvoltage error, in seconds.

### **Disqualification time overvoltage (s)** — Overvoltage disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the overvoltage error, in seconds. If you set
this parameter to `0`, the block does not disqualify the
error.

### **Qualification time faulty sensor (s)** — Faulty sensor qualification time `2` (default) | positive scalar

Time required to qualify the faulty sensor error, in seconds.

### **Disqualification time faulty sensor (s)** — Faulty sensor disqualification time `0` (default) | nonnegative scalar

Time required to disqualify the faulty sensor error, in seconds. If you
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

## Description

Monitor for battery voltage

The Battery Voltage Monitoring block monitors the voltage of a battery.
Voltage protection is necessary in electrical circuits. A battery that is exposed to
extremely high or extremely low voltages can enter a dangerously unstable state.

You can switch between continuous and discrete implementations of the block by using
the **Sample time (-1 for inherited)** parameter. To configure the
block for continuous time, set the **Sample time (-1 for
inherited)** parameter to `0`. To configure the block for
discrete time, set the **Sample time (-1 for inherited)**
parameter to a positive, nonzero value, or to `-1` to inherit the
sample time from an upstream block.

This diagram shows the structure of the block:

### Equations

This block computes the undervoltage symptom with this equation:

Undervoltage Symptom=min(CellVoltage)≤ UndervoltageLimit

This block computes the overvoltage symptom with this equation:

Overvoltage Symptom=max(CellVoltage)≥ OvervoltageLimit

This block computes the faulty sensor symptom with this equation:

FaultySensor Symptom=|PackVoltage−∑i−1nCellVoltagei|≥ FaultySensorThreshold

The check on the sum of the cell voltages assumes that all the cells are in series.

The Battery Voltage Monitoring block then passes these symptoms to a Fault
Qualification block, which qualifies the errors.
