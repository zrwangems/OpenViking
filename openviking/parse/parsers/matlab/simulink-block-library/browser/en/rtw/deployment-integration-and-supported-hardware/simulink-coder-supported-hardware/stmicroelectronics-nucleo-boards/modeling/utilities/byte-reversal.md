---
type: simulink-block
title: 'Byte Reversal'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Utilities'
documentation_page: 'bytereversal'
documentation_source_path: 'nucleo/ref/bytereversal.html'
language: en
---

# Byte Reversal

## Ports

### Input

### **Port\_1** — First of *N* input ports scalar | vector | matrix

Number of input ports specified in the **Number of inputs** parameter.
The block can have `1` to *N* input
ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Output port containing reversed data scalar | vector

Output ports from `1` to *N* as
specified in the **Number of inputs** parameter.
The number of output ports adjusts to match the number of input ports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Number of inputs** — Number of block inputs `1` (default)

The number of input ports and output ports adjusts to match
the value specified in this parameter.

When you use more than one input port, each input port maps
to the matching output port. Data entering input port 1 leaves through
output port 1, and so on. Reversing the bytes does not change the
data type.

### Example

Suppose that you are sending a signal. The signals have the
following attributes:

| Constant value | Type | Byte structure |
| --- | --- | --- |
| -234 | `int16` | `1111 1111 0001 0110` |
| 234 | `uint16` | `0000 0000 1110 1010` |
| 234 | `uint32` | `0000 0000 0000 0000 0000 0000 1110 1010` |

1. Set the number of inputs to 3.

   The block creates three input and three output ports.
2. Connect the signals to the Byte Reversal block.

The following model shows byte reversal. In the first signal,
with value -234, the low-order byte `0001 0110` is
swapped with the high-order byte `1111 1111`. Therefore,
the signal outputs to `0001 0110 1111 1111`.

## Libraries

Simulink Support Package for Arduino Hardware / Utilities Embedded Coder / Embedded Targets / Host Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Utilities Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities SoC Blockset Support Package for Infineon AURIX Microcontrollers / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Reverse little-endian data for big-endian processor

The Byte Reversal block changes the order of
the bytes in the input data. Use this block when your process communicates
between processors that use different endianness. For example, use
this block for communication between Intel® processors that are
little-endian and others that are big-endian. Processors compatible
with the Intel 80x86 processors and Texas Instruments® processors
are little-endian. In this case, insert a Byte Reversal block
before the Byte Pack block and another Byte
Reversal block just after the Byte Unpack block.

Using the parameter of this block, you specify the number of
block inputs.
