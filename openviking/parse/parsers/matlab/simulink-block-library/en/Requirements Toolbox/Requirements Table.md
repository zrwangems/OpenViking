---
type: simulink-block
title: 'Requirements Table'
family: 'slrequirements'
product_id: 'slrequirements'
product_name: 'Requirements Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'requirementstable'
documentation_source_path: 'ref/requirementstable.html'
language: en
---

# Requirements Table

## Ports

### Input

### **Port\_1** — Input data scalar | vector | matrix

Input data, specified as a real-valued scalar, vector, or matrix. Each input data
that you define has a corresponding input port.

#### Dependencies

To create input ports, open the block and create input data in the
**Symbols** pane. See Define Data in Requirements Table Blocks.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output data scalar | vector | matrix

Output data, specified as a real-valued scalar, vector, or matrix. Each output
data that you define has a corresponding output port.

#### Dependencies

To create output ports, open the block and create output data in the
**Symbols** pane. See Define Data in Requirements Table Blocks.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit the block parameters interactively:

- Use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
  **Prepare** gallery, select **Property
  Inspector**.
- Use the Table Properties window. Open the block. Then, in the
  **Simulation** tab, in the **Prepare** section,
  click **Table Properties**.

**Note**

Requirements Table blocks also have Subsystem (Simulink) block parameters that you can access by right-clicking the block and
clicking **Block Parameters (Subsystem)**. However, updating these
block parameters is not recommended.

### **Update method** — Method used for activating block `Inherited` (default) | `Discrete`

Specify the method for activating the Requirements Table block as one
of these values:

- `Inherited` — Input from the Simulink model activates the Requirements Table block.

  If you define input data, the Requirements Table block samples at
  the rate of the fastest input data. If you do not define input data, the
  Requirements Table block samples at the rate defined by the
  execution behavior of the parent subsystem.
- `Discrete` — Sample the Requirements
  Table block by using the rate you specify in the **Sample
  time** parameter of the Requirements Table block. The
  Requirements Table block generates an implicit event at regular
  time intervals that correspond to the specified rate. Other blocks in the model can
  have different sample times.

### **Sample time** — Time interval at which block activates up during simulation `-1` (default) | scalar | vector

Specify the time interval at which the Requirements Table block
activates during simulation. The default value indicates that the block inherits the
sample time from Simulink. This property uses the same format that you use in Simulink. For more information on specifying sample time, see Specify Sample Time (Simulink).

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the Table Properties
window.

#### Dependencies

To enable this parameter, set the block parameter **Update
method** to `Discrete`.

### **Saturate on interger overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Specify whether the data in the Requirements Table block saturates on
integer overflow as one of these values:

- `on` — The block saturates an integer by setting it to the
  maximum positive or negative value allowed by the word size. This setting matches
  MATLAB® behavior.
- `off` — The block wraps the value.

For more information, see Saturation and Wrapping (Fixed-Point Designer).

### **Support variable-size arrays** — Whether block supports variable-size data `on` (default) | `off`

Specify whether the Requirements Table block supports input and
output data that varies in dimension during simulation. When this parameter is
`on`, you can define variable-size outputs by enabling the
**Variable size** property on output data. For more information, see
Variable size.

### **Enable outputs in preconditions** — Whether block supports output data in preconditions `off` (default) | `on`

Specify whether the block can use data with **Scope** set to
`Output` in preconditions. If you disable this parameter, the
block highlights the cell and displays an alert icon  in preconditions that use output data, unless the data
is an input argument of `getPrevious`. However, if `getPrevious`
attempts to return the value of the data at a time step when it is not defined,
`getPrevious` returns undefined behavior.

#### Tips

- When you use output data in preconditions, you may encounter read-before-write
  issues in your requirements during simulation. To resolve these issues, specify
  your requirements in order. For more information, see Detect Read-Before-Write Issues and
  Leverage Evaluation Order of Formal Requirements.

### Fixed-point properties

### **Requirements Table fimath** — Default `fimath` object properties `Same as MATLAB` (default) | `Specify Other`

Specify the default `fimath` object properties for the
Requirements Table block as one of these values:

- `Same as MATLAB` — The block uses the same
  `fimath` object properties as the current default
  `fimath` object. The text box is dimmed and displays the current
  global `fimath` object.
- `Specify other` — Specify your own `fimath`
  object in the text box one of two ways:

  - Construct the `fimath` object inside the text box.
  - Construct the `fimath` object in the MATLAB or model workspace and then enter its variable name in the text
    box. If you use this option and plan to share your model with others, define
    the variable in the model workspace.
- For more information on `fimath` objects, see fimath Object Construction (Fixed-Point Designer).

#### Tips

- The `fimath` object of a Requirements Table
  block behaves as a `globalfimath` (Fixed-Point Designer) for the contents
  of the block. The block associates the `fimath` object properties
  in this parameter with the fixed-point and integer input signals to the block
  that you choose to treat as `fi` objects. Constructing
  `fi` objects in the Requirements Table block
  introduces additional considerations.

  - If no
    `fimath` object is associated with a `fi`
    object when it is constructed, then the `fi` constructor
    uses the default `fimath` object settings regardless of the
    properties in **Requirements Table fimath**. If you
    perform operations on the `fi` object after it is
    constructed, the object adopts the properties in **Requirements
    Table fimath**.
  - If you specify a `fimath` object in the
    `fi` constructor, then the `fi`
    constructor obeys that `fimath` object when quantizing the
    value. `fimath` settings not specified in the
    `fi` constructor use the specified properties in
    **Requirements Table fimath**.

## Libraries

Requirements Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### GPU Code Generation Generate CUDA® code for NVIDIA® GPUs using GPU Coder™.

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options for HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **GuardIndexVariables** | Specify whether to hoist array indices out of conditional statements or not. When you enable certain optimizations such as RAM Mapping, loop streaming, sharing, and so on, expressions are moved out of the array indices. A temporary variable is created for the expression that might result in an index out-of- bounds error during simulation. The default is `off`. See GuardIndexVariables (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **InstantiateFunctions** | Generate a VHDL® `entity` or Verilog® `module` for each function. The default is `off`. See also InstantiateFunctions (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Speed and Area Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Understand Delay Balancing in HDL Coder (HDL Coder) | When optimizations or block implementation options introduce delays along the critical path in a model, *Delay Balancing* detects introduction of new delays along one path, and then inserts matching delays on the other paths. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Restrictions**

When you apply optimizations, the block has these limitations:

- HDL optimizations are not supported for the block that has **Trigger**
  port.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2022a**

### R2022b: String support for Requirements Table blocks

You can now create and manipulate string data in Requirements Table
blocks. The string data type is compatible with strings in MATLAB and Simulink.

## Description

Model formal requirements with input conditions

The Requirements Table block models formal requirements. The block first
evaluates the conditions in the **Precondition** column. If the conditions
are satisfied, the block checks if other simulation data meets the conditions in the
**Postcondition** column or executes the actions in the
**Action** column. For more information, see Use a Requirements Table Block to Create Formal Requirements.

You can constrain requirements based on the physical limitations of your model by defining
assumptions in the **Assumptions** tab. See Add Assumptions to Requirements.

You can configure this block only if you have Requirements Toolbox™.
