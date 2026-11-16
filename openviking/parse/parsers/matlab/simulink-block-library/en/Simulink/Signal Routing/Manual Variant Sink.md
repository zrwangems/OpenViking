---
type: simulink-block
title: 'Manual Variant Sink'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualvariantsink'
documentation_source_path: 'slref/manualvariantsink.html'
language: en
---

# Manual Variant Sink

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal passed to the active output port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — First variant output scalar | vector

First variant output signal. The block passes the input signal to this
output port when you connect the toggle switch to this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — *n*th variant output scalar | vector

*n*th variant output signal. The block passes the
input signal to this output port when you connect the toggle switch to
this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To access the block parameter, right-click the block and select **Mask** > **Mask Parameters**.

### **Number of choices** — Number of output choices 2 (default) | scalar

Specify the number of variant output ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumChoices` |
| **Type:** character vector |
| **Value:** `integer` |
| **Default:** `'2'` |

## Libraries

Simulink / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2016b**

## Description

Switch between multiple variant choices at output

The Manual Variant Sink block is a toggle switch that activates one of its
variant choices at the output to pass the input.

The block can have two or more output ports and has one input port. Each output port is
associated with a variant control. To change the number of output ports, right-click the
block and select **Mask Parameters**, then type a value in the
**Number of choices** box.

To toggle between the variant choices at output, double-click the block. The block displays
the active choice with a line connecting the input to the output. The block propagates
the active variant choice at output and discards the blocks connected to inactive output
ports during simulation.

**Note**

- Double-clicking the Manual Variant Sink block does not open
  the block dialog box instead it toggles the output choice.
- Changing the active choice during compile, simulation, or paused states is
  not supported.
