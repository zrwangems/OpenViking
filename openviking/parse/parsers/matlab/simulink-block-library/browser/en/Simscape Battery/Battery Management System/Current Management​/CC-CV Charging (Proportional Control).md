---
type: simulink-block
title: 'CC-CV Charging (Proportional Control)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Current Management\u200b'
documentation_page: 'cccvchargingproportionalcontrol'
documentation_source_path: 'ref/cccvchargingproportionalcontrol.html'
language: en
---

# CC-CV Charging (Proportional Control)

## Ports

### Input

### **ChargingEnabled** — Whether to enable battery charging boolean

Whether to enable battery charging, specified as `1` (enabled) or
`0` (disabled).

### **CellVoltage** — Voltage of cells, V scalar | vector

Voltage of the battery cells, specified as a scalar for a single cell or a vector
for multiple cells.

If you select the **Specify CellVoltage input as [Min,Max]**
parameter, you must specify a minimum and a maximum value for this port, for example
`CellVoltage=[CellVoltageMin,CellVoltageMax]`.

### **ChargeCurrentLimit** — Limit of charging current, A scalar

Limit of the current that the battery uses for charging, specified as a
scalar.

### **CellVoltageThreshold** — Current for discharging, V scalar

Maximum allowable cell voltage, specified as a scalar.
### Output

### **ChargeCurrentRequest** — Charging current scalar

Charging current command, returned as a scalar.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Specify CellVoltage input as [Min,Max]** — Option to specify CellVoltage input as minimum and maximum values `off` (default) | `on`

Option to specify the value at the **CellVoltage** input port as a vector
of minimum and maximum values. If you clear this parameter, you must specify an
individual value for the input port. The block then calculates the minimum and maximum
values internally.

### **Controller proportional gain** — Proportional gain of controller `0.02` (default) | scalar

Proportional gain, *Kp*, of the
controller.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | `-1` | positive integer

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this parameter as a
positive integer.

## Libraries

Simscape / Battery / BMS / Current Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Constant-current constant-voltage charging algorithm with proportional control

The CC-CV Charging (Proportional Control) block implements a
constant-current (CC), constant-voltage (CV) charging algorithm for a battery with
proportional control. To implement the CC-CV charging algorithm with proportional-integral
control, see the Battery CC-CV
block.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

To configure the block for discrete time, set the **Sample time (-1
for inherited)** parameter to a positive, nonzero value. To inherit the sample time
from an upstream block, set the **Sample time (-1 for
inherited)** parameter to `-1`.

This diagram illustrates the overall structure of the block:

Internal structure of the CC-CV Charging (Proportional Control) block

### Equations

This block implements the CC-CV algorithm in constant-current and constant-voltage
modes. This figure shows the operation of these modes:

Operation mode of CC-CV algorithm. The blue line shows the charge current, the red line shows the voltage, the green line shows the charge capacity.

This equation defines the battery charging current that the block outputs
at the discrete-time instant *k*:

ichg(k)={Maximum charge current,if battery is charging and vmax<vthresholdKp(vthreshold−vmax)+ichg(k−1),if battery is charging and vmax≥vthreshold0,if battery is not charging

where

- *i*chg*(k)* is the
  charging current at time instant *k*.
- *i*chg*(k-1)* is the
  charging current at the previous time instant.
- *v*max is the voltage of the highest
  cell.
- *v*threshold is the maximum allowable cell
  voltage.
- *Kp* is the value of the
  **Controller proportional gain** parameter.
