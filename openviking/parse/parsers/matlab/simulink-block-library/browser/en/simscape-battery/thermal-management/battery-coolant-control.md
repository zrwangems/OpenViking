---
type: simulink-block
title: 'Battery Coolant Control'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Thermal Management'
documentation_page: 'batterycoolantcontrol'
documentation_source_path: 'ref/batterycoolantcontrol.html'
language: en
---

# Battery Coolant Control

## Ports

### Input

### **CellTemperature** — Cell temperature, K scalar | vector

Temperature of the battery cell, specified as a scalar for a single
cell or a vector for multiple cells.

If you select the
**Specify CellTemperature input as [Min,Max]**
parameter, you must specify a minimum and a maximum value for this port,
for example
`CellTemperature=[CellTemperatureMin,CellTemperatureMax]`. *(since R2025a)*

### **AmbientTemperature** — Ambient temperature, K scalar

Temperature of the ambient, specified as a scalar.

### **CoolantTemperature** — Coolant temperature, K scalar

Temperature of the coolant, specified as a scalar.
### Output

### **FlowRateCommand** — Flow rate command scalar

Flow rate command, returned as a scalar in the range [0, 1]. This output denotes the
flow rate relative to the maximum and minimum flow rate values. A value
of 0 corresponds to the minimum flow rate. A value of 1 corresponds to
the maximum flow rate.

### **FlowTemperature** — Flow temperature scalar

Temperature of the flow, returned as a positive or negative scalar. The total coolant
inlet temperature is equal to the sum of this value and the value at the
**AmbientTemperature** input port.

## Parameters

### **Specify CellTemperature input as [Min,Max]** — Option to specify CellTemperature input as minimum and maximum values `off` (default) | `on`

*Since R2025a*

Option to specify the value at the **CellTemperature** input port as a vector of
minimum and maximum values. If you clear this parameter, you must specify an
individual value for the **CellTemperature** input port. The block
then calculates the minimum and maximum values internally.

### **Control strategy** — Control strategy `ON-OFF control` (default) | `Step control`

Control strategy for the calculation of the flow rate command.

### **Switch-on temperature** — Coolant switch-on temperature `305.15` (default) | positive scalar

Temperature at which the coolant pump switches on. The value of this
parameter must be greater than or equal to the value of the
**Switch-off temperature** parameter.

#### Dependencies

To enable this parameter, set **Control strategy** to
`ON-OFF control`.

### **Switch-off temperature** — Coolant switch-off temperature `301.15` (default) | positive scalar

Temperature at which the coolant pump switches off.

#### Dependencies

To enable this parameter, set **Control strategy** to
`ON-OFF control`.

### **Constant used in f(deltaT)=c\*deltaT** — Constant for coolant strategy `0.1` (default) | positive scalar

Constant that controls how aggressive the coolant strategy is.

#### Dependencies

To enable this parameter, set **Control strategy** to
`Step control`.

### **Flow rate step** — Flow rate step `0.2` (default) | positive scalar

Step value used in the calculation of the flow rate command. The value of
this parameter must be less than or equal to `1`.

#### Dependencies

To enable this parameter, set **Control strategy** to
`Step control`.

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

### R2025a: Specify minimum and maximum values for **CellTemperature** input port

You can specify the minimum and maximum values for the
**CellTemperature** input port. To specify this input as a vector of
minimum and maximum values, select the **Specify CellTemperature input as
[Min,Max]** parameter.

## Description

Battery coolant control algorithm

The Battery Coolant Control block implements a battery coolant control
algorithm.

Temperature is crucial in batteries because high temperatures significantly decrease the
battery life. It is import to keep the temperature of each cell of the battery under
control and activate heaters or coolers to keep the temperature within safe limits. If
the temperature is too high, the battery management system (BMS) enables a cooling
fan.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable single-precision floating-point simulation, the data type of all inputs and
parameters must be `single`.

This diagram shows the structure of the block:

### Equations

The Battery Coolant Control block uses this equation to compute the
flow temperature:

FlowTemperature=Tamb−Tcool

where *Tamb* is the
ambient temperature and *Tcool* is the
coolant temperature.

If the value at the **FlowRateCommand** output port is equal to
`0`, there is no flow in the battery. If this value is equal to
`1`, then the flow rate in the battery takes its highest
possible value.

If you set the **Control strategy** parameter to
`ON-OFF control`, the block uses this equation to
calculate the flow rate command:

FlowRateCommand={1,Thottest≥TonFlowRateCommandold,Toff<Thottest<Ton0,Thottest<Toff

where

- *Thottest* is the temperature
  of the hottest cell.
- *Ton* is the switch-on
  temperature.
- *Toff* is the switch-off
  temperature, which must be less than Ton.
- *FlowRateCommandold* is the
  flow rate command at the previous time step.

If you set the **Control strategy** parameter to `Step
control`, the block uses these equations to calculate the flow rate command:

f(ΔT)=c(Thottest−min(Tcoolest,Tamb−Tcool))FlowRateCommand=min(f(ΔT)−mod(f(ΔT),step),1)

where

- *Tcoolest* is the temperature
  of the coolest cell.
- *step* is the flow rate step command. For example, if
  *step = 0.2*, the value at the
  **FlowRateCommand** output port is one of these
  values: [0,0.2,0.4,0.6,0.8,1].
- *c* controls how aggressive the coolant strategy is.
  This value is a constant such that, if *f(ΔT)≥ 1*, the
  value at the **FlowRateCommand** output port is equal
  to 1. Otherwise, the block scales the flow rate command linearly to
  `0`.

The step control strategy allows intermediate flow commands with the
value you specify for the **Flow rate step** parameter. To compute
the actual command, the block uses a function of the temperature gradient.
