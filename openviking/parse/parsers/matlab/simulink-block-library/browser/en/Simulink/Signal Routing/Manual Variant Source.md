---
type: simulink-block
title: 'Manual Variant Source'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualvariantsource'
language: en
---

# Manual Variant Source

Switch between multiple variant choices at input

## Libraries

Simulink / Signal Routing

## Description

The Manual Variant Source block is a toggle switch that activates one of its
variant choices at the input to pass through to the output.

A Manual Variant Source block can have two or more input ports and has one
output port. Each input port is associated with a variant control. To change the number
of input ports, right-click the block and select **Mask
Parameters**, then type a value in the **Number of
choices** box.

To toggle between the variant choices at input, double-click the block. The block displays
the active choice with a line connecting the input to the output. The block propagates
the active variant choice at input directly to the output and discards the blocks
connected to inactive input ports during simulation.

**Note**

- Double-clicking the Manual Variant Source block does not
  open the block dialog box instead it toggles the output choice.
- Changing the active choice during compile, simulation, or paused states is
  not supported.

## Ports

### Input

### **Port\_1** — First variant input signal scalar | vector

First variant input signal. The block passes this input signal to the output port when
you connect the toggle switch to this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_n** — *n*th variant input signal scalar | vector

*n*th variant input signal. The block passes this
input signal to the output port when you connect the toggle switch to
this port.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal passed from the active variant input signal.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To access the block parameter, right-click the block and select **Mask** > **Mask Parameters**.

### **Number of choices** — Number of input choices 2 (default) | scalar

Specify the number of variant input ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumChoices` |
| **Type:** character vector |
| **Value:** `integer` |
| **Default:** `'2'` |

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
