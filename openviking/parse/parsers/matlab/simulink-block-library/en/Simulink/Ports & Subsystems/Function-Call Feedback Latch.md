---
type: simulink-block
title: 'Function-Call Feedback Latch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallfeedbacklatch'
documentation_source_path: 'slref/functioncallfeedbacklatch.html'
language: en
---

# Function-Call Feedback Latch

## Ports

### Input

### **In** — Signal from function-call subsystem block scalar | vector | matrix

Signal from function-call subsystem block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Out** — Signal to function-call subsystem scalar | vector | matrix

Signal to function-call subsystem.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Ports & Subsystems

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2011a**

## Description

Break feedback loop involving data signals between function-call blocks

Use the Function-Call Feedback Latch block to break a feedback loop of
data signals between one or more function-call blocks. Specifically, break a feedback
loop formed in one of the following ways.

- **When function-call blocks connect to branches of the
  same function-call signal**

  Place the Function-Call Feedback Latch block on the feedback
  signal between the branched blocks. As a result, the latch block delays the
  signal at the input of the destination function-call block, and the destination
  function-call block executes prior to the source function-call block of the
  latch block.

  To run this model, see Function-Call Blocks Connected to Branches of the Same Function-Call Signal.
- **When the loop involves parent and child function-call
  blocks, where the child initiator is inside the parent**

  Place the Function-Call Feedback Latch block on the feedback
  signal between the child and the parent. This arrangement prevents the signal
  value, read by the parent (FCSS1), from changing during execution of the child.
  In other words, the parent reads the value from the previous execution of the
  child (FCSS2).

  To run this model, see Function-Call Feedback Latch on Feedback Signal Between Child and Parent.

Using the latch block is equivalent to selecting the **Latch input for
function-call feedback signals** check box on the Inport
block in the destination function-call subsystem or model. However, an advantage of the
latch block over using the dialog parameter is that one can design the destination
function-call subsystem or model in a modular fashion and then use it either in or out
of the context of loops.

The Function-Call Feedback Latch block is better suited than
Unit Delay or Memory blocks in breaking function-call
feedback loops for the following reasons:

- The latch block delays the feedback signal for exactly one execution of the
  source function-call block. This behavior is different from the Unit
  Delay or Memory blocks for cases where the
  function-call subsystem blocks may execute multiple times in a given simulation
  step.
- Unlike the Unit Delay or Memory blocks, the
  latch block may be used to break loops involving asynchronous function-call
  subsystems.
- The latch block can result in better performance, in terms of memory
  optimization, for generated code.
