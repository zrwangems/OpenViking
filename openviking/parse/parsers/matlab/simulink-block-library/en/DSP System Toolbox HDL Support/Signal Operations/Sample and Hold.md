---
type: simulink-block
title: 'Sample and Hold'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'sampleandhold'
documentation_source_path: '../dsp/ref/sampleandhold.html'
language: en
---

# Sample and Hold

## Ports
```yaml
ports:
- name: In
  summary: Signal port scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Trigger
  summary: Trigger port scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Sample and hold value scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **In** — Signal port scalar | vector | matrix

The signal port can accept data in the form of a scalar, vector, or
matrix.

#### Dependencies

This port is named **In<Lo>** when you select
the **Latch (buffer) input** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — Trigger port scalar

The trigger input must be a sample-based scalar with sample rate equal
to the input frame rate at the signal port. You specify the trigger
event using the **Trigger type** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Sample and hold value scalar | vector | matrix

Sample and hold output, returned as a scalar, vector, or a matrix. The
block acquires input at the signal port whenever it receives a trigger
event at the trigger port. The block then holds the acquired data until
the next triggering event occurs.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Trigger type
  summary: Type of trigger Rising edge (default) | Falling edge | Either edge
  group: ''
- name: Initial condition
  summary: Block output prior to first trigger event 0 (default) | scalar | vector | matrix
  group: ''
- name: Latch (buffer) input
  summary: Latch buffer input off (default) | on
  group: ''
```

### **Trigger type** — Type of trigger `Rising edge` (default) | `Falling edge` | `Either edge`

The type of event that triggers the block to acquire the input
signal:

- `Rising edge` –– The trigger input rises
  from a negative value or zero to a positive value.
- `Falling edge` –– The trigger input falls
  from a positive value or zero to a negative value.
- `Either edge` –– The trigger input either
  rises from a negative value or zero to a positive value or falls
  from a positive value or zero to a negative value.

### **Initial condition** — Block output prior to first trigger event `0` (default) | scalar | vector | matrix

Specify the block's output before the first trigger event using the
**Initial condition** parameter. When the acquired
input is an *M*-by-*N* matrix, the
**Initial condition** can be an
*M*-by-*N* matrix or a scalar repeated
across all elements of the matrix. When the input is a
length-*M* unoriented vector, the **Initial
condition** can be a length-*M* row or column
vector, or a scalar to be repeated across all elements of the vector.

### **Latch (buffer) input** — Latch buffer input `off` (default) | `on`

If you select the **Latch (buffer) input** check box, the
block outputs the value of the input from the previous time step until the
next triggering event occurs. To use this block in a loop, select this check
box.
## Libraries

DSP System Toolbox / Signal Operations DSP System Toolbox HDL Support / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

HDL code for the Sample and Hold block is generated as a
Triggered Subsystem. Similar restrictions apply to both blocks.
See Using Triggered Subsystems for HDL Code Generation (HDL Coder).

**HDL Block Properties**

For HDL block property descriptions, see HDL Block Properties: General (HDL Coder).

**Best Practices**

When using the Sample and Hold block in models targeted for HDL
code generation, consider the following:

- For synthesis results to match Simulink® results, drive the trigger port with registered logic
  (with a synchronous clock) on the FPGA.
- It is good practice to put a unit delay on the output signal. Doing
  so prevents the code generator from inserting extra bypass registers in
  the HDL code.
- The use of triggered subsystems, such as the Sample and
  Hold block, can affect
  synthesis results in the following ways:

  - In some cases, the system clock speed can drop by a small
    percentage.
  - Generated code uses more resources, scaling with the number of
    triggered subsystem instances.

**Restrictions**

The Sample and Hold block must meet the following
conditions:

- The DUT (i.e., the top-level subsystem for which code is generated)
  must not be the Sample and Hold block.
- The trigger signal must be a scalar.
- The data type of the trigger signal must be either
  `boolean` or `ufix1`.
- The output of the Sample and Hold block must have an
  initial value of 0.
- The input, output, and trigger signal of the Sample and
  Hold block must run at the same rate. If one of the input or
  the trigger signals is an output of a Signal Editor
  block, see Using the Signal Editor Block (HDL Coder)
  for how to match rates.

## Version History

**Introduced before R2006a**

## Description

Sample and hold input signal

The Sample and Hold block acquires the input at the signal port
whenever it receives a trigger event at the trigger port (marked by ). The block then holds the output at the acquired input value until
the next triggering event occurs.
