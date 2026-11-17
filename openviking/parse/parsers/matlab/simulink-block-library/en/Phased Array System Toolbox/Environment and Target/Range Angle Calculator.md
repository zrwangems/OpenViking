---
type: simulink-block
title: 'Range Angle Calculator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'rangeanglecalculator'
documentation_source_path: 'ref/rangeanglecalculator.html'
language: en
---

# Range Angle Calculator

## Ports
```yaml
ports:
- name: Pos
  summary: Source point position real-valued 3-by-1 vector | real-valued 3-by-*N* matrix
  direction: input
  data_types: double
- name: RefPos
  summary: Reference point position [0;0;0] (default) | real-valued 3-by-1 vector | real-valued 3-by-*N* matrix
  direction: input
  data_types: double
- name: RefAxes
  summary: Local coordinate system axes [1 0 0;0 1 0;0 0 1] (default) | real-valued 3-by-3 vector | real-valued 3-by-3-by-*N*
    array
  direction: input
  data_types: double
- name: Ang
  summary: Azimuth and elevation angles real-valued 2-by-*N* matrix | real-valued 2-by-2*N* matrix
  direction: output
  data_types: double
- name: Range
  summary: Propagation range real-valued 1-by-*N* vector | real-valued 1-by-2*N* vector
  direction: output
  data_types: double
```

### Input

### **Pos** — Source point position real-valued 3-by-1 vector | real-valued 3-by-*N* matrix

Source point position, specified as a real-valued 3-by-1 vector or a real-valued
3-by-*N* matrix where *N* is the
number of source points. Each column contains the Cartesian coordinates
of a point in the form `[x;y;z]`.

When `Pos` is a 3-by-*N* matrix, you must specify
`RefPos` as a 3-by-*N* matrix
for *N* reference positions. If all the reference
points are identical, you can specify `RefPos` by a
single 3-by-1 vector. Units are in meters.

**Example:** [1000;2000;50]

**Data Types:** `double`

### **RefPos** — Reference point position `[0;0;0]` (default) | real-valued 3-by-1 vector | real-valued 3-by-*N* matrix

Reference point position, specified as a real-valued 3-by-1 vector or a real-valued
3-by-*N* matrix where *N* is the
number of reference points. Each column contains the Cartesian
coordinates of point in the form `[x;y;z]`.

When `RefPos` is a 3-by-*N* matrix, you must specify
`Pos` as a 3-by-*N* matrix for
*N* source positions. If all the source points are
identical, you can specify `Pos` by a single 3-by-1
vector. Reference position units are meters.

**Example:** [100;100;10]

#### Dependencies

To enable this port, set the **Reference position source** drop down
menu to `Input port`.

**Data Types:** `double`

### **RefAxes** — Local coordinate system axes `[1 0 0;0 1 0;0 0 1]` (default) | real-valued 3-by-3 vector | real-valued 3-by-3-by-*N* array

Local coordinate system axes, specified as a real-valued 3-by-3 matrix or a
3-by-3-by-*N* array. For an array, each page
corresponds to a local coordinate axes at each reference point. The
columns in `RefAxes` specify the direction of the
coordinate axes for the local coordinate system in Cartesian
coordinates. *N* must match the number of columns in
`Pos` or `RefPos` when these
dimensions are greater than one.

**Example:** [100;100;10]

#### Dependencies

To enable this port, set the **Reference axes source** drop down menu
to `Input port`.

**Data Types:** `double`
### Output

### **Ang** — Azimuth and elevation angles real-valued 2-by-*N* matrix | real-valued 2-by-2*N* matrix

Azimuth and elevation angles in degrees, returned as a
2-by-*N* matrix or 2-by-2*N*
matrix. Each column represents a direction angle in the form
[azimuth;elevation].

When **Propagation model** is set to **Free
space**, `Ang` is a
2-by-*N* matrix and represents the angle of the
path from a source point to a reference point.

When **Propagation model** is set to
**Two-ray**, `Ang` is a
2-by-2*N* matrix. Alternate columns of
`Ang` refer to the line-of-sight path and
reflected path, respectively.

#### Dependencies

To enable this port, set the **Output(s)** drop down menu to
`Angle` or `Range and
Angle`.

**Data Types:** `double`

### **Range** — Propagation range real-valued 1-by-*N* vector | real-valued 1-by-2*N* vector

Propagation range, returned as a real-valued 1-by-*N* vector or
real-valued 1-by-2*N* vector.

When **Propagation model** is set to **Free
space**, the size of **Range** is
1-by-*N*. The propagation range is the length of
the direct path from the position defined in `Pos` to
the corresponding reference position defined in
`RefPos`.

When **Propagation model** is set to **Two-ray**,
**Range** contains the ranges for the direct path
and the reflected path. Alternate columns of **Range**
refer to the line-of-sight path and reflected path, respectively for the
same source-reference point pair.

#### Dependencies

To enable this port, set the **Output(s)** drop down menu to
`Range` or `Range and
Angle`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Propagation model
  summary: Propagation model Free space (default) | Two-ray
  group: ''
- name: Reference position source
  summary: Reference position source Property (default) | Input port
  group: ''
- name: Reference position
  summary: Reference position [0;0;0] (default)
  group: ''
- name: Reference axes source
  summary: Reference axes source Property (default) | Input port
  group: ''
- name: Reference axes
  summary: Reference axes eye(3)
  group: ''
- name: Output(s)
  summary: Output(s) Angle (default) | Range | Range and Angle
  group: ''
- name: Simulate using
  summary: Block simulation method Interpreted Execution (default) | Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Propagation model** — Propagation model `Free space` (default) | `Two-ray`

Specify the propagation model by setting this parameter to
`Free space` or
`Two-ray`.

### **Reference position source** — Reference position source `Property` (default) | `Input port`

Specify the reference position source by setting this parameter to
`Property` or `Input
port`. If **Reference position source** is
set to `Property`, set the position using the
**Reference position** parameter. If
**Reference position source** is set to
`Input port`, use the input port labeled
`RefPos`.

### **Reference position** — Reference position `[0;0;0]` (default)

Specify the reference position as a 3-by-1 vector of rectangular
coordinates in meters in the form `[x;y;z]`. The reference
position serves as the origin of the local coordinate system. Ranges and
angles of the input positions are measured with respect to the reference
position. This parameter appears only when **Reference position
source** is set to `Property`.

### **Reference axes source** — Reference axes source `Property` (default) | `Input port`

Specify the reference axes source by setting this parameter to
`Property` or `Input port`. If
**Reference axes source** is set to
`Property`, set the axes using the **Reference
axes** parameter. If **Reference axes source**
is set to `Input port`, use the input port labeled
`RefAxes`.

### **Reference axes** — Reference axes `eye(3)`

Specify the reference axes of the local coordinate system with which to
calculate range and angles in the form of a 3-by-3 orthonormal matrix. Each
column of the matrix specifies the direction of an axis for the local
coordinate system in the form of `[x; y; z]` with origin at
the reference position. This parameter appears only when **Reference
axes source** is set to `Property`.

### **Output(s)** — Output(s) `Angle` (default) | `Range` | `Range and Angle`

Specify the desired output(s) of the block. Each type of output is sent to
a different port depending on the parameter value.

| Value | Port |
| --- | --- |
| `Angle` | `Ang` |
| `Range` | `Range` |
| `Range and Angle` | `Ang` and `Range` |

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |
## Libraries

Phased Array System Toolbox / Environment and Target

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Range and angle calculations

The Range Angle Calculator block calculates the range and/or the azimuth and
elevation angles of several positions with respect to a reference position and with
respect to a reference axes orientation. The reference position and reference axes can
be specified in the block dialog box or passed in through input ports.
