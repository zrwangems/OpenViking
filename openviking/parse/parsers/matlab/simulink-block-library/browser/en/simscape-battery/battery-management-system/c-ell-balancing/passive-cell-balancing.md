---
type: simulink-block
title: 'Passive Cell Balancing'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / C\u200bell Balancing'
documentation_page: 'passivecellbalancing'
documentation_source_path: 'ref/passivecellbalancing.html'
language: en
---

# Passive Cell Balancing

## Ports

### Input

### **u** — Cell voltages or cell SOC values vector

Cell voltages or cell SOC values, specified as a vector.

**Note**

The input port **u** expects cell
voltages from a realistic sensor. To emulate the sensor and solve
algebraic loops, if you are feeding simulation outputs from a model,
add a unit delay, transfer function, or any other filter.

### **Enable** — Whether to enable cell balancing scalar

Whether to enable passive cell balancing, specified as `1` (enabled) or
`0` (disabled).
### Output

### **Command** — Balancing command vector

Balancing command, returned as a vector of entries equal to `0` or
`1`. The size of this vector is equal to the size
of the **u** input.

### **BalancingActive** — Whether the balancing procedure is active scalar

Whether the balancing procedure is active, returned as a scalar.

## Parameters

### Main

### **Threshold for balancing** — Balancing threshold `0.2` (default) | nonnegative scalar

Threshold that the block uses for balancing.

### **Hysteresis band for switching balancing off** — Hysteresis band for switching off passive balancing `0` (default) | nonnegative scalar

*Since R2023b*

Hysteresis band for switching off the passive cell balancing. The
value of this parameter must be less than or equal to the value of the
**Threshold for balancing** parameter.

### **ON delay time (s)** — Time delay before balancing activation `1` (default) | nonnegative scalar

Time delay before activating the cell balancing, in seconds.

### **OFF delay time (s)** — Time delay after balancing completion `1` (default) | nonnegative scalar

Time delay after the block completes the balancing procedure, in
seconds.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | 0 | positive integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate,
updates its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify
this parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that
allows you to switch between continuous operation and discrete
operation, promote the sample time parameter. Promoting the sample time
parameter ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.

### Signal Attributes

### **Command Data Type** — Data type of Command output `double` (default) | `single` | `boolean` | `<data type expression>`

Specify the data type of the **Command** output. You
can specify the type directly or you can express it as a data type
object such as `Simulink.NumericType`.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes.
For more information, see Specify Data Types Using Data Type Assistant.

## Libraries

Simscape / Battery / BMS / Cell Balancing

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Passive battery cell balancing algorithm

This block implements a passive battery cell balancing algorithm. The passive cell
balancing technique keeps a similar state-of-charge value in all cells by dissipating
the excess charge in a bleed resistor.

The value at the **u** input port can be cell voltages or cell
state-of-charge (SOC) values. The **Enable** input port acts as a
trigger for the balancing procedure. When **Enable** is
`1`, the block starts balancing the battery until the battery is
fully balanced.

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

When the value at the **Enable** input port is `1`, the
block starts balancing the battery until the battery is fully balanced. To balance
the battery, the algorithm discharges some of the cells until their voltage or
state-of-charge is equal to the voltage or state-of-charge of the cell with the
lowest value.

The **Command** output port specifies the balancing command as a vector of
elements equal to 0 or 1. This equation determines each element of
**Command**:

Command={0if u−min(u)≤Threshold−HysteresisBandCommandoldif Threshold−HysteresisBand<u−min(u)<Threshold1if u−min(u)≥Threshold

where *Threshold* is the value of
**Threshold for balancing** parameter,
*HysteresisBand* is the value of the **Hysteresis band
for switching balancing off** parameter, and
*Commandold* is the command at the
previous step.

To specify the data type of the **Command** output port, use the
**Command Data Type** parameter.

The **BalancingActive** output port is true if any cell of the battery
exceeds the threshold value.
