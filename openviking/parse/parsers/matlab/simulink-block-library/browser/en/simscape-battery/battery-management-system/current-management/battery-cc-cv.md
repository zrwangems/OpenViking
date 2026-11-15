---
type: simulink-block
title: 'Battery CC-CV'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Current Management\u200b'
documentation_page: 'batterycccv'
documentation_source_path: 'ref/batterycccv.html'
language: en
---

# Battery CC-CV

## Ports

### Input

### **ChargingEnabled** — Whether to enable battery charging boolean

Whether to enable battery charging, specified as `1` (enabled) or
`0` (disabled).

### **CellVoltage** — Cell voltages, V scalar | vector

Voltage of the cells, specified as a scalar for a single cell or a
vector for multiple cells.

If you select the
**Specify CellVoltage input as [Min,Max]**
parameter, you must specify a minimum and a maximum value for this port,
for example
`CellVoltage=[CellVoltageMin,CellVoltageMax]`. *(since R2025a)*

### **CurrentWhenCharging** — Current for charging, A scalar

Value of the current that the battery uses for charging, specified as
a scalar.

### **CurrentWhenDischarging** — Current for discharging, A scalar

Value of the current that the battery uses for discharging, specified
as a scalar.
### Output

### **Current** — Computed reference current, A scalar

Reference current for the battery pack, returned as a scalar.

## Parameters

### **Specify CellVoltage input as [Min,Max]** — Option to specify CellVoltage input as minimum and maximum values `off` (default) | `on`

*Since R2025a*

Option to specify the value at the **CellVoltage** input port as a vector of
minimum and maximum values. If you clear this parameter, you must specify an
individual value for the input port. The block then calculates the minimum
and maximum values internally.

### **Cell voltage threshold (V)** — Maximum allowable cell voltage `4.5` (default) | scalar

Maximum allowable cell voltage, in volt.

### **Controller proportional gain** — Proportional gain of PI controller `100` (default) | scalar

Proportional gain, *Kp*, of the PI
controller.

### **Controller integral gain** — Integral gain of PI controller `10` (default) | scalar

Integral gain, *Ki*, of the PI
controller.

### **Controller anti-windup gain** — Anti-windup gain of PI controller `1` (default) | scalar

Anti-windup gain of the PI controller.

### **Gain of signal-tracking feedback loop** — Tracking coefficient of PI controller `1` (default) | scalar

Tracking coefficient, *Kt*, of the
PI controller.

The block feeds the difference between the tracking signal and the controller output back
to the integrator input with a gain value
*Kt*. Use this parameter to
specify the gain in that feedback loop.

Signal tracking has several applications, including bumpless control
transfer and avoiding windup in multiloop control structures.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | `0` | `-1` | positive integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as `-1`.
For discrete-time operation, specify this parameter as a positive integer.
For continuous-time operation, specify this parameter as
`0`.

If this block is in a masked subsystem or a variant subsystem that allows you to switch
between continuous operation and discrete operation, promote the sample time
parameter. Promoting the sample time parameter ensures correct switching
between the continuous and discrete implementations of the block. For more
information, see Promote Block Parameters on a Mask.

## Libraries

Simscape / Battery / BMS / Current Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Specify minimum and maximum values for **CellVoltage** input port

You can specify the minimum and maximum values for the **CellVoltage**
input port. To specify this input as a vector of minimum and maximum values, select
the **Specify CellVoltage input as [Min,Max]** parameter.

## Description

Constant current constant voltage charging algorithm

The Battery CC-CV block implements a constant-current (CC), constant-voltage
(CV) charging algorithm for a battery. For a discharging battery, the block uses the
value of the **CurrentWhenDischarging** input port. To implement a
simpler version of the CC-CV charging algorithm with proportional control, see the
CC-CV Charging
(Proportional Control) block.

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

This diagram illustrates the overall structure of the block:

### Equations

This block implements the CC-CV algorithm in constant-current and constant-voltage modes.
This figure shows the operation of these modes:

This equation defines the battery reference current that the block
outputs:

Current={Maximum charge current,if battery is charging and vmeas<vmax(Kp+Ki1s)(vmax−vmeas),if battery is charging and vmeas≥vmaxMaximum discharge current,if battery is discharging

where

- *vmax* is the value of the
  **Cell voltage threshold (V)** parameter.
- *vmeas* is the voltage of the
  highest cell.
- *Kp* and
  *Ki* are the values of
  the **Controller proportional gain** and
  **Controller integral gain** parameters.
