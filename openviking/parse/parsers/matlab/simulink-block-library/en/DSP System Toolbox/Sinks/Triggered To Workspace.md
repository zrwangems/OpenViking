---
type: simulink-block
title: 'Triggered To Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'triggeredtoworkspace'
documentation_source_path: 'ref/triggeredtoworkspace.html'
language: en
---

# Triggered To Workspace

## Ports
```yaml
ports:
- name: Input
  summary: Data to log to workspace scalar | vector | matrix | bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string
    | fixed point | enumerated | bus | image
- name: Trigger
  summary: Trigger signal scalar | vector | matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Input** — Data to log to workspace scalar | vector | matrix | bus

Specify the data to log to the workspace when the block receives a trigger at the
**Trigger** port. The Triggered To
Workspace block supports logging real and complex data of
any built-in data type or user-defined data types such as buses,
enumerations, and fixed-point data.

#### Tips

Logging fixed-point data requires a Fixed-Point Designer™ license.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes

### **Trigger** — Trigger signal scalar | vector | matrix

Specify the trigger signal that controls the execution of the block as
a scalar, vector, or a matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Trigger type
  summary: Trigger type Rising edge (default) | Falling edge | Either edge
  group: ''
- name: Variable name
  summary: Workspace variable name yout (default) | character vector | string
  group: ''
- name: Decimation
  summary: Decimation factor 1 (default) | scalar
  group: ''
- name: Maximum number of rows
  summary: Maximum number of rows to be saved 1000 (default) | positive integer
  group: ''
- name: Save 2-D signals as
  summary: Arrangement of 2-D samples values in logged data 2-D array (concatenate along first dimension) (default) | 3-D
    array (concatenate along third dimension)
  group: ''
- name: Log fixed-point data as a fi object
  summary: Log fixed-point data as a fi object off (default) | on
  group: ''
```

### **Trigger type** — Trigger type `Rising edge` (default) | `Falling edge` | `Either edge`

The type of event that triggers the execution of the block.

The block acquires and buffers a single frame from input 1 whenever it is
triggered by the control signal at input 2 (). At all other times, the block ignores input 1. You
specify the triggering event at input 2 using the **Trigger
type** parameter:

- `Rising edge` triggers execution of the
  block when the trigger input rises from a negative value to zero or
  a positive value, or from zero to a positive value.
- `Falling edge` triggers execution of the
  block when the trigger input falls from a positive value to zero or
  a negative value, or from zero to a negative value.
- `Either edge` triggers execution of the
  block for a `Rising edge` or a
  `Falling edge`.

### **Variable name** — Workspace variable name `yout` (default) | character vector | string

The name of the workspace variable in which to store the data. By default, the
Triggered To Workspace block saves logged data in a
variable called `yout`. When a model contains multiple
Triggered To Workspace blocks, you must specify a unique
value in the **Variable name** parameter of
each block.

### **Decimation** — Decimation factor `1` (default) | scalar

Specify a decimation factor to reduce the effective sample rate for the logged data. For
a decimation factor *D* the Triggered To
Workspace block logs the value of every
*D*th sample. For example,
when you specify the **Decimation** value as
`2`, the Triggered To Workspace block
logs every other data point.

For more information about controlling which samples the block logs during simulation,
see Specify Signal Values to Log (Simulink).

### **Maximum number of rows** — Maximum number of rows to be saved `1000` (default) | positive integer

Specify the maximum number of rows (one row per time step) that the block saves
(*P*) as a positive integer.

### **Save 2-D signals as** — Arrangement of 2-D samples values in logged data `2-D array (concatenate along first dimension)` (default) | `3-D array (concatenate along third dimension)`

Specify whether the block saves 2-D signals as a 2-D or 3-D array in the
MATLAB workspace.

When you select:

- `2-D array (concatenate along first
  dimension)` — The block vertically
  concatenates each *M*-by-*N* matrix input with the previous input
  to produce a 2-D output array. The block saves the data as a
  *P*-by-*N* matrix, where
  *P* is the value of the **Maximum
  number of rows** parameter.

  When the simulation progresses long enough for the block to
  acquire more than *P* samples, the block stores
  only the most recent *P* samples. The
  **Decimation factor**
  *D* allows you to store only every
  *Dth* input
  matrix.
- `3-D array (concatenate along third
  dimension)` — The block saves an
  *M*-by-*N* input as a 3-D
  array in which each *M*-by-*N*
  page represents a single sample from each of the
  *M*\**N* channels (the most
  recent input matrix occupies the last page). The maximum size of
  this 3-D array is limited to
  *M*-by-*N*-by-*P*,
  where *P* is the value of the value of the
  **Maximum number of rows** parameter.

  When the simulation progresses long enough for the block to
  acquire more than *P* inputs, the block stores only
  the last *P* inputs. The **Decimation
  factor**
  *D* allows you to store only every
  *Dth* input
  matrix.

### **Log fixed-point data as a fi object** — Log fixed-point data as a `fi` object `off` (default) | `on`

Specify how to log fixed-point input data. By default, the
Triggered To Workspace block logs fixed-point input data
as `double`. When you select this parameter, the
Triggered To Workspace block logs fixed-point input as a
Fixed-Point Designer
`fi` (Fixed-Point Designer) object.

Using the Triggered To Workspace block to log fixed-point
data requires a license for Fixed-Point Designer.
## Libraries

DSP System Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility in subsystems
that generate HDL code, but is not included in the hardware implementation.

## Version History

**Introduced before R2006a**

## Description

Write input sample to MATLAB workspace when triggered

The Triggered To Workspace block creates a matrix or array variable in the
MATLAB® workspace, where it stores the acquired inputs at the end of a simulation.
The block overwrites an existing variable with the same name.

To save a record of the sample time corresponding to each sample value, open the
Configuration Parameters dialog box. To open the Configuration Parameters, in the
**Modeling** tab of the Simulink® model toolstrip, click **Model Settings**. In the left
pane of the window that opens, click **Data Import/Export** and
select the **Time** check box.

The nontriggered version of this block is the To Workspace (Simulink) block.
