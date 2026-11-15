---
type: simulink-block
title: 'MATLAB System'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'matlabsystem'
language: en
---

# MATLAB System

## Ports

### Input

### **In** — Signal input to a MATLAB System block scalar | vector | matrix

The MATLAB System block accepts inputs of the types
listed in the Block Characteristics table. For more information, see
Data Types Supported by Simulink.

For information on fixed-point support for this block, see Code Acceleration and Code Generation from MATLAB (Fixed-Point Designer).

The MATLAB System block supports Simulink frames. For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Out** — Signal output of a MATLAB System block scalar | vector | matrix

Signal output of a MATLAB System
block that the System object returns.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **System Object Name** — Name of the System object cell array (default)

Specify the full name of the user-defined System object class without the file extension. This entry is case
sensitive. The class name must exist on the MATLAB path.

You can specify a System object name in one of these ways:

- Enter the name in the text box.
- Click the list arrow attached to the text box. If valid System
  objects exist in the current folder, the names appear in the list.
  Select a System object from this list.
- Browse to a folder that contains a valid System object. If the folder is not on your MATLAB path, the software prompts you to add it.

If you need to create a System object, you can create one from a template by clicking
**New**.

After you save the System object, the name appears in the **System object
name** text box.

Use the full name of the user-defined System object class name. The block does not accept a MATLAB variable that you have assigned to a System object class name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `System` |
| **Type:** character vector |
| **Value:** name of the System object |
| **Default:** `' '` |

### **New** — Create a System object from a template `Basic` (default) | `Advanced` | `Simulink Extension`

Select one of the options for a System object template.

`Basic`
:   Starts MATLAB Editor and displays a template for a simple
    System object using the fewest System object methods.

`Advanced`
:   Starts MATLAB Editor and displays a template for a more
    advanced System object using most of the System object methods.

`Simulink Extension`
:   Starts MATLAB Editor and displays a file that contains
    utilities for customizing the block for Simulink. This is the same file available in MATLAB when you select **New** > **System Object** > **Simulink Extension**.

After you save the System object, you can enter the name in the **System object
name** text box.

### **Simulate using** — Select the simulation mode `Code generation` (default) | `Interpreted Execution`

Select the simulation mode.

`Code generation`
:   On the first model run, simulate and generate code for
    MATLAB System block using only MATLAB functions supported for code generation. If the
    structure of the block does not change, subsequent model runs do
    not regenerate the code.

    If the simulation mode is `Code
    generation`, System Objects accept a maximum of
    32 inputs.

`Interpreted execution`
:   Simulate model using all supported MATLAB functions. Choosing this option can slow
    simulation performance.

### **Dependency** — Dependency parameter for MATLAB System block auto (default)

After you assign a valid System object class name to the block, the next time you open the block
dialog box, the parameter is visible. This parameter appears for every
MATLAB System block. You cannot remove it.

- If the block has no tabs, this parameter appears at the bottom of
  the dialog box.
- If the block has multiple tabs, this parameter appears at the
  bottom of the first tab of the dialog box.

### **Saturate on integer overflow** — Specify whether overflows saturate `Off` (default) | `On`

On
:   Overflows saturate to either the minimum or maximum value
    that the data type can represent. For example, an overflow
    associated with a signed 8-bit integer can saturate to -128
    or 127.

Off
:   Overflows wrap to the appropriate value that the data type
    can represent. For example, the number 130 does not fit in a
    signed 8-bit integer and wraps to -126.

#### Tips

- Consider selecting this check box when your model has a
  possible overflow and you want explicit saturation protection in
  the generated code.
- Consider clearing this check box when you want to optimize
  efficiency of your generated code. Clearing this check box also
  helps you to avoid overspecifying how a block handles
  out-of-range signals. For more information, see Troubleshoot Signal Range Errors.
- When you select this check box, saturation applies to every
  internal operation on the block, not just the output or
  result.
- In general, the code generation process can detect when
  overflow is not possible. In this case, the code generator does
  not produce saturation code.

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Treat these inherited Simulink signal types as fi objects** — Specify `fi` data types `Fixed-point` (default) | `Fixed-point & Integer`

Select which inherited data types to treat `fi` data
types,

`Fixed-point`
:   Treat fixed-point data types as `fi` data
    types.

`Fixed-point & Integer`
:   Treat fixed-point and integer data types as
    `fi` data types.

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

### **MATLAB System fimath** — Specify fixed-point settings to use `Same as MATLAB` (default) | `Specify Other`

Select which fixed-point math settings to use.

**Same as MATLAB**
:   Use the current MATLAB fixed-point math settings.

**Specify Other**
:   Enable the edit box for specifying the desired fixed-point
    math settings. For information on setting fixed-point math, see
    `fimath` (Fixed-Point Designer).

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

## Libraries

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesca` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation.  b See Nonvirtual Buses and MATLAB System Block for more information.  c See Variable-Size Signals for more information. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

You can define a System object and use it in a MATLAB System block for HDL code
generation.

**Tunable Parameter Support**

HDL Coder supports tunable parameters with the following data types:

- Numeric
- Fixed point
- Character
- Logical

When using tunable parameters with the MATLAB System block, the
tunable parameter should be a `Simulink.Parameter` object with
the `StorageClass` set to
`ExportedGlobal`.

```
x = Simulink.Parameter
x.Value = 1
x.CoderInfo.StorageClass = 'ExportedGlobal'
```

For details, see
Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

If you use a predefined System object, the HDL block properties available are the same as the properties
available for the corresponding block.

By default, the following HDL block properties are available.

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **VariablesToPipeline** | **Warning**  `VariablesToPipeline` is not recommended. Use `coder.hdl.pipeline` (HDL Coder) instead.  Insert a pipeline register at the output of the specified MATLAB variable or variables. Specify the list of variables as a character vector, with spaces separating the variables. |

**Restrictions**

- The DUT subsystem must be single-rate.
- Inputs cannot have non-discrete (constant or
  `Inf`) sample time.
- To find predefined System objects that are
  supported for HDL code generation when you use them in the
  MATLAB System block, see Predefined System Objects Supported for HDL Code Generation (HDL Coder).
- If you use a user-defined System object, it must support HDL code generation. For information
  about user-defined System objects and requirements
  for HDL code generation, see HDL Code Generation for System Objects (HDL Coder).

See also Generate Code for User-Defined System Objects (HDL Coder) and HDL Code Generation for System Objects (HDL Coder).

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2013b**

### R2025a: MATLAB System block supports unbounded variable-size signals

MATLAB System block now supports unbounded variable-size signals at
the block input and output ports. This enables you to use variable-size signals
whose dimensions are unknown during model compilation. For more information about
unbounded variable-size signals, see Unbounded Variable-Size Signals.

### R2024a: Report runtime errors for MATLAB System blocks in rapid accelerator mode

Report runtime errors for MATLAB System blocks when simulating in
rapid accelerator mode by setting the **Enable memory integrity checks**
configuration parameter to `Always on`.

## Description

Include System object in model

The MATLAB System block brings existing System objects (based on `matlab.System`) into Simulink®. It also enables you to use System object APIs to develop new blocks for
Simulink. For more information on this block, see Create Custom Blocks Using MATLAB System Block and System objects.

For interpreted execution, the model simulates the block using the MATLAB® execution engine.

For code generation, the model simulates the block using code generation (using the
subset of MATLAB code supported for code generation). The MATLAB System
block supports only a subset of the functions available in MATLAB. See Functions and Objects Supported for C/C++ Code Generation for a complete
list of functions. These functions include those in common categories, such as:

- Array vs. Matrix Operations,
  like `plus`, `minus`, and
  `power`
- Matrix operations, like `size` and `length`
- Advanced matrix operations, like `lu`, `inv`, `svd`, and `chol`
- Trigonometric functions, like `sin`, `cos`, `sinh`, and `cosh`

By default, the block recognizes 1-D input signals and propagates 1-D output signals
as 2-D. Use the `supports1DVectorsImpl` method to enable the block to recognize and
propagate 1-D inputs and outputs as 1-D signals.

Starting in R2025a, the block supports unbounded variable-size signals at its input
and output ports. For more information about unbounded variable-size signals, see Unbounded Variable-Size Signals.

### System Objects

To use the MATLAB System block, you must first have a new
System object™ or use an existing one. For more information, see Author Blocks Using MATLAB System Objects.
