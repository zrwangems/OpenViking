---
type: simulink-block
title: 'SOC Estimator (Coulomb Counting, Variable Capacity)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / State-of-Charge Estimators'
documentation_page: 'socestimatorcoulombcountingvariablecapacity'
documentation_source_path: 'ref/socestimatorcoulombcountingvariablecapacity.html'
language: en
---

# SOC Estimator (Coulomb Counting, Variable Capacity)

## Ports

### Input

### **Current** — Battery current, ampere scalar | vector

Battery current, in ampere, specified as a scalar for a single cell or a vector for
multiple cells. To specify this input as a vector of cell currents,
select the **Specify Current input as cell current(s)**
parameter.

### **InitialSOC** — Initial state of charge, unitless scalar | vector

Initial state of charge, specified as a scalar or vector of entries in
the range [0, 1]. The size of this input port must be equal to the size
of the **Current** input port.

### **AH** — Battery cell capacity, A\*Hr nonnegative scalar

Cell capacity of the battery, in ampere-hour, specified as a strictly positive scalar.
The block calculates the state of charge by dividing the accumulated
charge by this value. The block calculates accumulated charge by
integrating the battery current.
### Output

### **SOC** — Battery state of charge scalar | vector

State of charge of the battery, returned as a scalar or a vector. The
size of this output port is equal to the size of the
**Current** and **InitialSOC**
input ports.

## Parameters

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `on` (default) | `off`

*Since R2023b*

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | 0 | -1 | integer

Time between consecutive block executions.
During execution, the block produces outputs and, if appropriate, updates
its internal state. For more information, see What Is Sample Time? and
Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this
parameter as a positive integer. For continuous-time operation, specify this
parameter as `0`.

If this block is in a masked subsystem or a variant subsystem that
supports switching between continuous operation and discrete operation,
promote the sample time parameter. Promoting the sample time parameter
ensures correct switching between the continuous and discrete
implementations of the block. For more information, see Promote Block Parameters on a Mask.

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

Simscape / Battery / BMS / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

### R2023b: Specify the value of the Current input as a vector of cell currents

You can now specify the value of the **Current** input port as a
vector of cell currents.

To enable a vectorized input, select the **Specify Current input as cell
current(s)** parameter. If you select this parameter, the
**Current** input port must have the same size as the other
inputs and represents individual cell currents.

## Description

State of charge estimator with Coulomb counting and variable capacity

The SOC Estimator (Coulomb Counting, Variable Capacity) block implements an
estimator that calculates the state of charge (SOC) of a battery by using the Coulomb
counting method. The cell capacity of the battery is an input to the block. The block
calculates the state of charge by dividing the accumulated charge by the value of this
input. The block then calculates the accumulated charge by integrating the battery
current.

The SOC is the ratio of the released capacity
*C*releasable to the rated capacity
*C*rated. Manufacturers provide the value of
the rated capacity of each battery, which represents the maximum amount of charge in the battery:

SOC=CreleasableCrated.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable inherited single-precision floating-point simulation, the data type of all
inputs and parameters, except for the **Sample time (-1 for
inherited)** parameter, must be `single`.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
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

To compute the SOC of the battery, the SOC Estimator (Coulomb Counting, Variable
Capacity) block counts the Ampere hour and current integration:

SOC=SOC(t0)+1Crated∫t0t0+τIbatt,

where *C*rated is the
nominal battery capacity and *I*batt is the
battery current.
