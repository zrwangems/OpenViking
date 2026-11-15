---
type: simulink-block
title: 'Unit System Configuration'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'unitsystemconfiguration'
language: en
---

# Unit System Configuration

## Ports

Not documented in R2025b.

## Parameters

### **Disallowed unit systems** — Disallowed unit systems `SI` | `English` | `SI (extended)` | `CGS`

Displays a list of the disallowed unit systems. By default, the
**Allow all unit systems** check box is selected, and
all unit systems are allowed.

To designate a unit system as disallowed, select it in the
**Allowed unit systems** column and click
**<< Disallow**.

#### Dependencies

To enable changes to this parameter, you must first clear the
**Allow all unit systems** check box.

### **Allowed unit systems** — Allowed unit systems `SI` | `English` | `SI (extended)` | `CGS`

Displays a list of the allowed unit systems. By default, the
**Allow all unit systems** check box is selected, and
all unit systems are allowed.

To designate a unit system as allowed, use the **Allow
>>** and **<< Disallow**
buttons to move unit systems between the **Disallowed unit
systems** and **Allowed unit systems**
columns.

#### Dependencies

To enable changes to this parameter, you must first clear the
**Allow all unit systems** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UnitSystems` |
| **Type:** cell array of character vectors |
| **Values:** cell array of the following character vectors: `'SI'` | `'English'` | `'SI (extended)'` | `'CGS'` |
| **Default:** `{'SI', 'English', 'SI (extended)', 'CGS'}` |

### **Allow all unit systems** — Allow all unit systems `on` (default) | `off`

When you select this check box, all unit systems are allowed. To restrict
the allowed unit systems to only the ones specified in the **Allowed
unit systems** column, clear this check box.

#### Dependencies

Selecting the **Allow all unit systems** check box
disables the **Disallowed unit systems** and
**Allowed unit systems** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowAllUnitSystems` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

## Libraries

Simulink / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2016a**

## Description

Restrict units to specified allowed unit systems

The Unit System Configuration block specifies allowed and disallowed
unit systems for the component. It restricts units systems for a subsystem or top model
and all its children, unless you override it with another Unit System
Configuration block in a child.

This block supports normal, accelerator, and rapid accelerator modes and fast
restart.
