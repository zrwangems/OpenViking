---
type: simulink-block
title: 'Byte Reversal'
family: 'slrealtime'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'bytereversal'
documentation_source_path: 'ref/bytereversal.html'
language: en
---

# Byte Reversal

## Ports
```yaml
ports:
- name: Port_1
  summary: Data to convert scalar, vector, matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: Port_1
  summary: Converted data scalar, vector, matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### Input

### **Port\_1** — Data to convert scalar, vector, matrix

Data for which the block changes the byte ordering. The number of input ports
used by the block depends on the value that you specify for the **Number of
inputs** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Converted data scalar, vector, matrix

Data with modified byte ordering. The number of output ports used by the block
depends on the value that you specify for the **Number of inputs**
parameter. Each input port maps to the matching output port. Data received on input
port 1 is sent through output port 1, and so on.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Number of inputs
  summary: Number of block inputs 1 (default) | integer
  group: ''
```

### **Number of inputs** — Number of block inputs 1 (default) | integer

Specify the number of block inputs. The block creates that number of input ports
and output ports. Each input port maps to the matching output port. Data received on
input `Port_1` is sent through output `Port_1`, and so
on.

Reversing the byte ordering does not change the data type. Input and output retain
matching data types.
## Libraries

Embedded Coder / Embedded Targets / Host Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Reverse order of bytes in input word

The Byte Reversal block changes the order of the bytes in data that you input to the
block. Use this block when a process communicates between target computers that use different
endianness, such as between Intel® processors that are little endian and other processors that are big endian.
Texas Instruments® processors are little-endian by default.

To exchange data between processors that have different endianness, place a Byte Reversal
block just before the send block and immediately after the receive block.

This model shows byte reversal for three inputs. The input and output ports match for each
path.
