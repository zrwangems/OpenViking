---
type: simulink-block
title: 'Battery Discharging Current Limit'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Current Management'
documentation_page: 'batterydischargingcurrentlimit'
documentation_source_path: 'ref/batterydischargingcurrentlimit.html'
language: en
---

# Battery Discharging Current Limit

## Ports

### Input

### **CellVoltage** — Cell voltages, V scalar | vector

Cell voltage, in volt, specified as a scalar for a single cell or a
vector for multiple cells.

*In R2025a: If you select the **Specify inputs as
[Min,Max]** parameter, you must specify a minimum and a
maximum value for this port, for example
`CellVoltage=[CellVoltageMin,CellVoltageMax]`.*

### **CellTemperature** — Temperature of cells, K scalar | vector

Temperature of the cells, specified as a scalar for a single cell or a
vector for multiple cells. The size of this input port must be equal to
the size of the **CellVoltage** parameter.

If you select the
**Specify inputs as [Min,Max]** parameter, you must
specify a minimum and a maximum value for this port, for example
`CellTemperature=[CellTemperatureMin,CellTemperatureMax]`. *(since R2025a)*
### Output

### **CurrentLimit** — Charging current limit for battery pack scalar

Discharging current limit for the battery pack, returned as a
scalar.

## Parameters

### **Specify inputs as [Min,Max]** — Option to specify inputs as minimum and maximum values `off` (default) | `on`

*Since R2025a*

Option to specify the values at the **CellVoltage** and
**CellTemperature** input ports as a vector of minimum and
maximum values. If you clear this parameter, you must specify individual
values for the input ports. The block then calculates the minimum and
maximum values internally.

### **Cell undervoltage limit (V)** — Undervoltage limit for cell `2.5` (default) | positive scalar

Limit under which the battery cell is undercharged, in volt.

### **Terminal resistance (ohm)** — Terminal resistance `0.0025` (default) | positive scalar

Terminal resistance, *R0*, in
ohm.

### **Vector of temperatures, T** — Cell temperatures `[243.15, 258.15, 273.15, 288.15, 303.15, 318.15, 333.15]` (default) | vector of scalars

Cell temperatures. The physical unit of this parameter must be the same as
the physical unit of the **CellTemperature** input
port.

### **Current limit for coolest cell, iCool(T), (A)** — Current limit for coolest cell `[ 0, 0, 0, 0, 100, 100, 100]` (default) | vector of positive scalars

Current limit for the coolest cell, in ampere. The size of this vector
must be equal to the size of the **Vector of temperature,
T** parameter.

### **Current limit for hottest cell, iHot(T), (A)** — Current limit for hottest cell `[100, 100, 100, 100, 0, 0, 0]` (default) | vector of positive scalars

Current limit for the hottest cell, in ampere. The size of this vector
must be equal to the size of the **Vector of temperature,
T** parameter.

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

Simscape / Battery / BMS / Current Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

### R2025a: Specify minimum and maximum values for input ports

You can specify the minimum and maximum values for the **CellVoltage**
and **CellTemperature** input ports. To specify these inputs as minimum and
maximum values, select the **Specify inputs as [Min,Max]**
parameter.

## Description

Maximum battery discharging current

The Battery Discharging Current Limit block calculates the maximum
discharging current of a battery. Limiting the charging and discharging currents is an
important consideration when you model battery packs.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable single-precision floating-point simulation, the data type of all inputs and
parameters must be `single`.

This diagram shows the structure of the block:

### Equations

The discharging current limit is equal to the minimum of these values:

- The temperature-dependent limit for the coolest and hottest
  cells
- The theoretical current based on the undervoltage limit of the
  cell
- The terminal resistance

CurrentLimit=−min(i1,i2,i3)i1=min(CellVoltage)−UndervoltageLimitR0i2=f(min(CellTemperature))i3=g(max(CellTemperature))

where

- *UndervoltageLimit* is the value of the
  **Cell undervoltage limit (V)** parameter.
- *CellVoltage* is the value of the
  **CellVoltage** input port.
- *R0* is the value of the
  **Terminal resistance (ohm)** parameter.
- *CellTemperature* is the value of the
  **CellTemperature** input port.
