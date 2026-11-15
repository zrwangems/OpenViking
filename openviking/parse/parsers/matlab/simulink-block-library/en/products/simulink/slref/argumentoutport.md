---
type: simulink-block
title: 'Argument Outport'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Simulink Functions'
documentation_page: 'argumentoutport'
documentation_source_path: 'slref/argumentoutport.html'
language: en
---

# Argument Outport

## Ports

### Input

### **in** — Block input scalar | vector | matrix

Block input signal to this block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **y** — Argument output scalar | vector | matrix

The Argument Outport block accepts real or complex
signals of any data type that Simulink® supports. An Argument Outport block can
also accept fixed-point and enumerated data types when the block is not
a root-level output port. The Argument Outport block also
accepts a bus object as a data type.

The complexity and data type of the block input are the same as the
argument output. You can specify the signal type and data type of an
output argument from an Argument Outport block using the
**Signal type** and **Data type**
parameters. For more information, see Data Types Supported by Simulink.

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

### **Argument name** — Specify output argument name `u` (default) | character vector

Specify output argument name for the function prototype displayed on the
face of the Simulink Function block.

`u`
:   Default name of the output argument.

character vector
:   Name of the output argument.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ArgumentName` |
| **Type:** character vector |
| **Value:** `'u'` | `'<character vector>'` |
| **Default:** `'u'` |

### **Minimum** — Specify minimum value for block input `[]` (default) | number

Specify the minimum value for the block input signal.

**Note**

If you specify a bus object as the data type for this block, do not
set the minimum value for bus data on the block. Simulink ignores this setting. Instead, set the minimum values for
bus elements of the bus object specified as the data type. For
information on the Minimum property of a bus element, see `Simulink.BusElement`.

Simulink uses this value to perform Simulation range checking (see
Specify Signal Ranges) and
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

### **Maximum** — Specify maximum value for block input `[]` (default) | number

Specify the maximum value for the block input signal.

**Note**

If you specify a bus object as the data type for this block, do not
set the maximum value for bus data on the block. Simulink ignores this setting. Instead, set the maximum values for
bus elements of the bus object specified as the data type. For
information on the Maximum property of a bus element, see `Simulink.BusElement`.

Simulink uses this value to perform Simulation range checking (see
Specify Signal Ranges) and
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

### **Data type** — Specify block input data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `Enum: <class name>` | `Bus: <object name>` | `<data type expression>`

Specify block input data type. For more information, see

- Outport
- Specify Data Types Using Data Type Assistant

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

`int6a4`
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
| **Value:** `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'`| `'boolean'` | `'<fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
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

Specify the dimensions of the output argument signal from the block. For
more information, see Outport.

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

Select real or complex signal. For more information, see Outport.

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

Argument output port for Simulink Function block

This block is an output argument port for a function that you define in the Simulink Function block.
