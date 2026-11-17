---
type: simulink-block
title: 'Persistent Variable Read'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Target Management'
documentation_page: 'persistentvariableread'
documentation_source_path: 'io_ref/persistentvariableread.html'
language: en
---

# Persistent Variable Read

## Ports
```yaml
ports:
- name: Data
  summary: Persistent variable output data variable data
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean
```

### Output

### **Data** — Persistent variable output data variable data

The data type and dimensions of the Persistent Variable Read block
output port are set by the `Default value` parameter. If these
properties do not match those of the variable stored on the target computer, an error
occurs during real-time application load.

The block can take a complex number. The complexity of the Persistent
Variable Read block output port is set by the `Default
value` parameter. If this property does not match the complexity of the
variable stored on the target computer, an error occurs during real-time application
load.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
## Parameters
```yaml
parameters:
- name: Variable name
  summary: Name of persistent variable Variable1 (default) | character vector | string
  group: ''
  block_parameter: varName
- name: Default value
  summary: Starting value of persistent variable when variable does not exist on target computer 0 (default) | supports same
    data types as Data port
  group: ''
  block_parameter: defaultValue
```

### **Variable name** — Name of persistent variable `Variable1` (default) | character vector | string

The **Variable name** parameter provides the name of the persistent
variable. Use this name to access the variable in the structure of variable values
retrieved from the target computer by using the `getPersistentVariables` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `varName` |

### **Default value** — Starting value of persistent variable when variable does not exist on target computer `0` (default) | supports same data types as Data port

The **Default value** parameter provides a starting value for the
persistent variable when the variable does not exist on the target computer. This
parameter sets the data type and dimensions of the Persistent Variable
Read block output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `defaultValue` |
## Libraries

Simulink Real-Time / Target Management

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Read persistent variable value from target computer

The Persistent Variable Read block reads the selected persistent variable
from the Speedgoat® target computer when you load the real-time application. If the block cannot
find the selected variable, the block outputs the selected default value. The variable value
persists when the target computer is shut down.

Use the `getPersistentVariables` function and `setPersistentVariables` function to access the persistent variable values on the
target computer.
