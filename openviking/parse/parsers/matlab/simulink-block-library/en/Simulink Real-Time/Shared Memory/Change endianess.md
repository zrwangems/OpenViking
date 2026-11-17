---
type: simulink-block
title: 'Byte Reversal/Change Endianess'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Shared Memory'
documentation_page: 'bytereversalchangeendianess'
documentation_source_path: 'io_ref/bytereversalchangeendianess.html'
language: en
---

# Byte Reversal/Change Endianess

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Number of input ports
  summary: Number of ports 1 (default)
  group: Block Parameters for Change Endianess
  block_parameter: numInp
- name: Machine word length
  summary: Word length for conversion Byte (default) | Word | Double Word
  group: Block Parameters for Change Endianess
  block_parameter: />
- name: Number of inputs
  summary: Number of ports 1 (default)
  group: Byte Reversal Block Parameters
  block_parameter: numInp
```

### Block Parameters for Change Endianess

### **Number of input ports** — Number of ports `1` (default)

The number of input ports adjusts to follow this parameter and the number of
outputs is equal to the number of inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numInp` |

### **Machine word length** — Word length for conversion `Byte` (default) | `Word` | `Double Word`

Select a machine word length from the list to which to convert the data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** /> |

### Byte Reversal Block Parameters

### **Number of inputs** — Number of ports `1` (default)

The number of input ports adjusts to follow this parameter and the number of
outputs is equal to the number of inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numInp` |
## Libraries

Simulink Real-Time / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

## Description

Reverse little-endian data for big-endian processor

The Byte Reversal/Change Endianess block provides communication between a
Simulink®
Real-Time™ system and a system running with a processor that is
*big-endian*. Processors compatible with the Intel® 80x86 family are *little-endian*. For this situation, insert
a Byte Reversal/Change Endianess block before the Pack block and
another just after the Unpack block. The following is the Change
Endianess block.
