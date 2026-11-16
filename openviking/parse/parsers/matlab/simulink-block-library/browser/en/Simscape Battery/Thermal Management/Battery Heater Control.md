---
type: simulink-block
title: 'Battery Heater Control'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Thermal Management'
documentation_page: 'batteryheatercontrol'
documentation_source_path: 'ref/batteryheatercontrol.html'
language: en
---

# Battery Heater Control

## Ports

### Input

### **AmbientTemperature** — Ambient temperature scalar

Temperature of the ambient, specified as a scalar.

### **CoolantTemperature** — Coolant temperature scalar

Temperature of the coolant, specified as a scalar.
### Output

### **Command** — Heater command scalar

Heater command, returned as a scalar. If this value is equal to `0`,
the heater switches off. If this value is equal to `1`,
the heater switches on.

## Parameters

### **Ambient temperature threshold for heater** — Ambient temperature threshold for heater `278.15` (default) | positive scalar

Ambient temperature at which the block activates the heater.

### **Switch-on coolant temperature** — Switch-on coolant temperature `278.15` (default) | positive scalar

Coolant temperature at which the heater switches on.

### **Switch-off coolant temperature** — Switch-off coolant temperature `290.15` (default) | positive scalar

Coolant temperature at which the heater turns off. The value of this
parameter must be greater than the value of the **Switch-on coolant
temperature** parameter.

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

Simscape / Battery / BMS / Thermal Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Battery heater control algorithm

The Battery Heater Control block implements a battery heater control
algorithm.

Temperature is crucial in batteries as low temperatures significantly decrease the battery
life. It is then fundamental to keep the temperature of each cell of the battery under
control and activate heaters or coolers to keep the temperature under safe limits. If
the temperature is too low, the battery management system (BMS) enables a heater.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable single-precision floating-point simulation, the data type of all inputs and
parameters must be `single`.

This diagram shows the structure of the block:

### Equations

The Battery Heater Control block activates the heater only if the
temperature of the ambient drops below the value of the **Ambient
temperature threshold for heater** parameter. If the temperature drops
below this threshold, the value at the **Command** output port is
equal to:

Command={0,Tcoolant≥ToffCommandold,Ton<Tcoolant<Toff1,Tcoolant≤Ton

where

- *Tcoolant* is the coolant
  temperature.
- *Ton* is the coolant
  temperature at which the heater switches on.
- *Toff* is the coolant
  temperature at which the heater switches off. This value is greater than
  *T*on.
- *Commandold* is the command at
  the previous time step.
