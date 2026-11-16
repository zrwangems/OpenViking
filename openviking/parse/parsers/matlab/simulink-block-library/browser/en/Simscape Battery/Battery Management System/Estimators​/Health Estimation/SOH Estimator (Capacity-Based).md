---
type: simulink-block
title: 'SOH Estimator (Capacity-Based)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / Health Estimation'
documentation_page: 'sohestimatorcapacitybased'
documentation_source_path: 'ref/sohestimatorcapacitybased.html'
language: en
---

# SOH Estimator (Capacity-Based)

## Ports

### Input

### **AH** — Cell capacity, A\*Hr scalar | vector

Cell capacity, in ampere-hour, specified as a scalar for a single cell
or a vector for multiple cells.
### Output

### **SOH** — State of health of battery scalar | vector

State of health of the battery, returned as a scalar or vector with
entries in the range [0, 1]. The size of this output port is equal to
the size of the **AH** input port.

## Parameters

### **Cell capacity when battery is new, AH\_new, (A\*Hr)** — Cell capacity when battery is new `27` (default) | nonnegative scalar

Cell capacity, in ampere-hour, when the battery is new.

### **Cell capacity at end of life, AH\_eol, (A\*Hr)** — Cell capacity at end of life `21.6` (default) | nonnegative scalar

Cell capacity, in ampere-hour, when the battery is at the end of its life.

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

**Introduced in R2023b**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

State of health estimator based on capacity fade

The SOH Estimator (Capacity-Based) block implements an estimator that
calculates the state of health (SOH) of a battery based on the capacity fade. The SOH
reflects the condition of a battery relative to its ideal conditions. Health variations
imply that the capacity and power of the battery fade over time.

This block supports single-precision and double-precision
floating-point simulation.

**Note**

To enable single-precision floating-point simulation, the data type of all inputs and
parameters must be `single`.

This diagram shows the structure of the block:

### Equations

The cell capacity is an important indicator of the aging of a battery. During the life
cycle of a battery, the cell capacity decreases over time. Usually, the cell SOH is
0 when the cell capacity decreases to about 80% of its nominal value.

The SOH Estimator (Capacity Based) block computes the SOH as a function of
the cell capacity *Q*:

SOHQ=Q−QeolQnew−Qeol,

where *Q*eol is the
end-of-life capacity and *Q*new is the
capacity when the battery is new.
