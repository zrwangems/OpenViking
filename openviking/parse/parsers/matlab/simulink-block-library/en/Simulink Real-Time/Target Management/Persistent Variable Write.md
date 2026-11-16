---
type: simulink-block
title: 'Persistent Variable Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Target Management'
documentation_page: 'persistentvariablewrite'
documentation_source_path: 'io_ref/persistentvariablewrite.html'
language: en
---

# Persistent Variable Write

## Ports

### Input

### **Data** — Persistent variable input data variable data

The data type of the Persistent Variable Write block input port is
inherited from its input signal. The signal can be any dimension.

The block can take a complex number. The complexity of the Persistent
Variable Write block input port is inherited from its input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## Parameters

### **Variable name** — Name of persistent variable `Variable1` (default) | character vector | string

The **Variable name** parameter provides the name of the persistent
variable. Use this name to access the variable in the structure of variable values
retrieved from the target computer by using the `getPersistentVariables` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `varName` |

## Libraries

Simulink Real-Time / Target Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Write persistent variable value to target computer

The Persistent Variable Write block writes a value to the selected
persistent variable when the real-time application starts and stops. The variable value
persists when the Speedgoat® target computer is shut down.

Use the `getPersistentVariables` function and `setPersistentVariables` function to access the persistent variable values on the
target computer.
