---
type: simulink-block
title: 'Argument Inport'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Simulink Functions'
documentation_page: 'argumentinport'
documentation_source_path: 'slref/argumentinport.html'
language: en
---

# Argument Inport

## Ports

### Input

### **u** — Argument input scalar | vector | matrix

The Argument Inport block accepts complex or real
signals of any data type that Simulink® supports, including fixed-point and enumerated data types.
The Argument Inport block also accepts a bus object as a
data type.

The complexity and data type of the block output are the same as the
argument input. You can specify the signal type and data type of an
input argument to an Argument Inport block using the
**Signal type** and **Data type**
parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **out** — Block output scalar | vector | matrix

Block output signal from this block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Port number** — Specify port number of block `1` (default) | integer

Specify the order in which the port that corresponds to the block appears
in the parent subsystem or model block.

`1`
:   Specify the first port location for this block.

integer
:   Specify location of port.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Port` |
| **Type:** character vector |
| **Value:** `'1'` | `'<integer>'` |
| **Default:** `'1'` |

### **Argument name** — Specify input argument name `u` (default) | character vector

Specify input argument name for the function prototype displayed on the
face of the Simulink Function block.

`u`
:   Default name for the input argument.

character vector
:   Name of the input argument.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ArgumentName` |
| **Type:** character vector |
| **Value:** `'u'` | `'<character vector>'` |
| **Default:** `'u'` |

### **Minimum** — Specify minimum value for block output `[]` (default) | number

Specify the minimum value for the block output signal.

**Note**

If you specify a bus object as the data type for this block, do not
set the minimum value for bus data on the block. Simulink ignores this setting. Instead, set the minimum values for
bus elements of the bus object specified as the data type. For
information on the Minimum property of a bus element, see `Simulink.BusElement`.

Simulink uses this value to perform Simulation range checking and
automatic scaling of fixed-point data types.

`[]`
:   Minimum value not specified.

number
:   Finite real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMin` |
| **Type:** character vector |
| **Value:** `'[]'` | `'<number>'` |
| **Default:** `'[]'` |

### **Maximum** — Specify maximum value for block output `[]` (default) | number

Specify the maximum value for the block output signal.

**Note**

If you specify a bus object as the data type for this block, do not
set the maximum value for bus data on the block. Simulink ignores this setting. Instead, set the maximum values for
bus elements of the bus object specified as the data type. For
information on the Maximum property of a bus element, see `Simulink.BusElement`.

Simulink uses this value to perform Simulation range checking and
automatic scaling of fixed-point data types.

`[]`
:   Maximum value not specified.

number
:   Finite real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMax` |
| **Type:** character vector |
| **Value:** `'[]'` | `'<number>'` |
| **Default:** `'[]'` |

### **Data type** — Specify block output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `Enum: <class name>` | `Bus: <object name>` | `<data type expression>`

Specify the block output data type.

`double`
:   Data type is `double`.

`single`
:   Data type is `single`.

`int8`
:   Data type is `int8`.

`uint8`
:   Data type is `uint8`.

`int16`
:   Data type is `int16`.

`uint16`
:   Data type is `uint16`.

`int32`
:   Data type is `int32`.

`uint32`
:   Data type is `uint32`.

`int64`
:   Data type is `int64`.

`uint64`
:   Data type is `uint64`.

`boolean`
:   Data type is `boolean`.

`fixdt(1,16,0)`
:   Data type is fixed point
    `fixdt(1,16,0)`.

`fixdt(1,16,2^0,0)`
:   Data type is fixed point
    `fixdt(1,16,2^0,0)`.

`Enum: <class name>`
:   Data type is enumerated, for example, `Enum: Basic
    Colors`.

`Bus: <object name>`
:   Data type is a `Simulink.Bus` object.

`<data type expression>`
:   The name of a data type object, for example
    `Simulink.NumericType`

#### Tips

You cannot enter the name of a `Simulink.Bus` object as
a data type expression. To specify the **Data type**
for the block using a `Bus` object, select the
`Bus: <object name>` option and replace
`<object name>` with the name of the
`Bus` object.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Value:** `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default:** `'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data type off (default) | on

Control changes to data type settings from the Fixed-Point Tool and the
Fixed-Point Advisor. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

On
:   Locks all data type settings for this block.

Off
:   Allows the Fixed-Point Tool and the Fixed-Point Advisor to
    change data type settings for this block.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `LockScale` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Port dimensions** — Specify port dimensions `1` (default) | `n` | `[m n]`

Specify the dimensions of the argument input signal to the block. For more
information, see Outport.

`1`
:   Inherit port dimensions.

`n`
:   Vector signal of width `n`.

`[m n]`
:   Matrix signal having `m` rows and
    `n` columns.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PortDimensions` |
| **Type:** character vector |
| **Value:** `'1'` | `'n'` | `'[m n]'` |
| **Default:** `'1'` |

### **Signal type** — Select real or complex signal `real` (default) | `complex`

Select real or complex signal.

`real`
:   Specify the signal type as a real number.

`complex`
:   Specify the signal type as a complex number.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SignalType` |
| **Type:** character vector |
| **Value:** `'real'` | `'complex'` |
| **Default:** `'real'` |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Argument input port for Simulink Function block

This block is an argument input port for a function that you define in the Simulink Function block.
