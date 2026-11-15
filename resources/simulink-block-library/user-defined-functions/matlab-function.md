---
type: simulink-block
title: 'MATLAB Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'matlabfunction'
---

# MATLAB Function

Include MATLAB code in Simulink models

## Libraries

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## Description

The MATLAB Function block enables you to write MATLAB® functions that execute in Simulink® models. The MATLAB function executes during simulation at each time step. For more
information about integrating MATLAB code into your Simulink models, see Implement MATLAB Functions in Simulink with MATLAB Function Blocks. If you
have a Simulink
Coder™ license, you can also generate C/C++ code from a MATLAB
Function block for a Simulink
Coder target.

Double-click the MATLAB Function block to open the MATLAB Function Block Editor, where you write the MATLAB function. You can also define variables, add an input trigger, and create
function call outputs by using the Model Explorer or the **Symbols**
pane. For more information, see Create and Define MATLAB Function Block Variables, Manage the Input Trigger of a MATLAB Function Block,
and Manage Function Call Outputs of a MATLAB Function Block.

In the **Symbols** pane, you can declare a block input to be a
Simulink parameter instead of a port. The MATLAB Function block also
supports inheritance of types and size for inputs, outputs, and parameters. You can
specify these properties explicitly. See Define and Modify Variable Data Types, Specify Size of MATLAB Function Block Variables, and Use Data in Multiple MATLAB Function Blocks by Defining Parameter Variables.

When you simulate a model that contains a MATLAB Function block, the
software generates binary code or C/C++ MATLAB executable (MEX) code from the block and integrates this code with the
model. The MATLAB Function block uses the same infrastructure as
MATLAB
Coder, which you use to generate C/C++ code from MATLAB code outside of Simulink. Consequentially, the MATLAB Function block code must use
MATLAB conventions that are supported for code generation. See Code and Integration Limitations for MATLAB Function Blocks.

To support visualization of data, the MATLAB Function block supports
calls to MATLAB functions for simulation only. See Use MATLAB Engine to Execute a Function Call in MATLAB Function Blocks. If you generate code using Simulink
Coder, the calls do not appear in the generated code if the function calls do
not directly affect the Simulink inputs or outputs.

## Ports

### Input

### **Port\_1** — Input variable scalar | vector | matrix

Input variable in the MATLAB function, specified as a real-valued scalar, vector, or
matrix. Each input variable has an associated port that uses the name of
the variable.

You cannot pass data types supported by MATLAB but not supported by Simulink between the Simulink model and the function in the MATLAB
Function block. You can use these data types in the
MATLAB Function block.

For more information on fixed-point data type support for this block,
see Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)
and Data Type Override with MATLAB Function Block (Fixed-Point Designer).

#### Dependencies

To create input ports, open the block and create input variables
in the **Symbols** pane. See Create and Define MATLAB Function Block Variables.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output variable scalar | vector | matrix

Output variable in the MATLAB function, specified as a real-valued scalar, vector, or
matrix. Each output variable has an associated port that uses the name
of the variable.

#### Dependencies

To create output ports, open the block and create output variables
in the **Symbols** pane. See Create and Define MATLAB Function Block Variables.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

**Note**

MATLAB Function blocks also have Subsystem block parameters that you
can access by right-clicking the block and clicking **Block Parameters
(Subsystem)**. However, updating these block parameters is not
recommended.

### **Update method** — Method used for activating block `Inherited` (default) | `Discrete` | `Continuous`

Specify the method for activating the MATLAB Function block as one of
these values:

- `Inherited` — Input from the Simulink model activates the MATLAB Function
  block.

  If you define an input trigger, the MATLAB Function
  block executes in response to a Simulink signal or function-call event on the trigger port. If
  you do not define an input trigger, the MATLAB
  Function block implicitly inherits triggers from the
  model. These implicit events are the discrete or continuous sample
  times of the signals that provide inputs to the block.

  If you define data inputs, the MATLAB Function
  block samples at the rate of the fastest data input. If you do not
  define data inputs, the MATLAB Function block samples
  at the rate defined by the execution behavior of the parent
  subsystem.
- `Discrete` — The MATLAB
  Function block activates by using the rate you specify
  in the **Sample time** parameter of the block.
  The block generates an implicit event at regular time intervals that
  correspond to the specified rate. Other blocks in the model can have
  different sample times.
- `Continuous` — The MATLAB
  Function block activates during major time steps only,
  and computes outputs and local continuous variables during major and
  minor time steps. The block can register zero crossings, which
  allows Simulink models to sample the block whenever state changes
  occur. The block computes derivatives for local continuous
  variables.

#### Programmatic Use

To set the block parameter value programmatically, access the `MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

If you use the `MATLABFunctionConfiguration` object,
specify the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `UpdateMethod` |
| **Values:** | `"Inherited"` (default) | `"Continuous"` | `"Discrete"` |

If you use the `Stateflow.EMChart` object, specify the
property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **Values:** | `"INHERITED"` (default) | `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — Time interval at which block activates up during simulation `-1` (default) | scalar | vector

Specify the time interval at which the MATLAB Function block activates
during simulation. The default value indicates that the block inherits the
sample time from Simulink. For more information on specifying sample time, see Specify Sample Time.

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the
Property Inspector.

#### Dependencies

To enable this parameter, set **Update method** to
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the `MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar | vector |
| **Data Types:** | `string` | `char` |

### Advanced

### **Saturate on integer overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Specify whether the data in the MATLAB Function block saturates on
integer overflow as one of these values:

- `on` — The block saturates an integer by
  setting it to the maximum positive or negative value allowed
  by the word size. This setting matches MATLAB behavior.
- `off` — The block generates a run-time
  error in simulation mode when a overflow condition occurs.
  When you use Simulink
  Coder to generate code, the behavior depends on your
  C language compiler.

#### Tips

- When this parameter is `on`, MATLAB adds additional checks during simulation to
  detect integer overflow or underflow. If integer overflow
  does not occur in the MATLAB Function block
  code, it is more efficient to disable this option.
- Code generated by Simulink
  Coder does not check for integer overflow or
  underflow and, therefore, may produce unpredictable results
  when this parameter is `off`. In this
  situation, simulate your model to test for overflow and
  underflow before generating code.
- This parameter setting is relevant only for integer
  arithmetic. It has no effect on fixed-point or
  double-precision arithmetic.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Support variable-size arrays** — Whether block supports variable-size data `on` (default) | `off`

Specify whether the MATLAB Function block supports input and output data
that varies in dimension during simulation. When this parameter is
`on`, you can define variable-size outputs by
enabling the **Variable size** property on output
variables. For more information, see Declare Variable-Size MATLAB Function Block Variables and Variable size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SupportVariableSizing` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Allow direct feedthrough** — Whether block supports direct feedthrough semantics `on` (default) | `off`

Specify whether the MATLAB Function block supports direct feedthrough
semantics, so that the output of the block is controlled directly by the
value of an input. When this parameter is `off`, the
block outputs rely only on the current state of the block. Using
nondirect feedthrough enables you to use MATLAB Function
blocks in a feedback loop and prevent algebraic loops. For more
information, see Use Nondirect Feedthrough in a MATLAB Function Block.

#### Dependencies

To disable this parameter, you must set **Update method** to
`Inherited` or
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `AllowDirectFeedthrough` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Interpret output column vectors as one-dimensional data** — Whether block treats output variables with dimension of length 1 as fixed size `off` (default) | `on`

*Since R2021b*

Specify whether the MATLAB Function block treats output variables with a
dimension of length 1 as fixed size as one of these values:

- `off` — The block treats output variables
  that have at least one dimension of length 1 as fixed size,
  regardless of whether you specify the variables as having
  variable size.
- `on` — The MATLAB Function
  block treats output variables as variable size if you
  specify the variables as having variable size.

For more information, see Variable size.

**Note**

In release R2021b and earlier, MATLAB Function
blocks always convert output column vectors to one-dimensional
signals.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `VectorOutputs1D` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Treat dimensions of length 1 as fixed size** — Whether variables with at least one dimension of length 1 are fixed size `on` (default) | `off`

*Since R2023a*

Specify whether variables with at least one dimension of length 1 are fixed size as one
of these values:

- `on` — Variables that are variable size
  with a dimension of 1 are fixed size.
- `off` — Variables in the block that have
  the **Variable size** property enabled are
  always variable size.

This parameter only affects output variables that have the
**Variable size** property enabled. See Variable size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### Fixed-point properties

### **Treat these inherited Simulink signal types as fi objects** — Inherited Simulink signals to treat as `fi` objects `Fixed-point` (default) | `Fixed-point & Integer`

Specify whether to treat inherited fixed-point and integer signals as Fixed-Point Designer™
`fi` (Fixed-Point Designer) objects as one of
these values:

- `Fixed-point` — The MATLAB
  Function block treats all fixed-point inputs as
  Fixed-Point Designer
  `fi` objects.
- `Fixed-point & Integer` — The
  MATLAB Function block treats all
  fixed-point and integer inputs as Fixed-Point Designer
  `fi` objects.

For more information, see Ways to Construct fi Objects (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatAsFi` |
| **Values:** | `"Fixed-point"` (default) | `"Fixed-point & Integer"` |

### **MATLAB function fimath** — Default `fimath` properties `Same as MATLAB` (default) | `Specify Other`

Specify the default `fimath` (Fixed-Point Designer) object
properties for the MATLAB Function block as one of these
values:

- `Same as MATLAB` — The block uses the same
  `fimath` object properties as the current
  default `fimath` object. The text box is dimmed
  and displays the current global `fimath` object
  in read-only form.
- `Specify other` — Specify your own
  `fimath` object in the text box one of two
  ways:

  - Constructing the `fimath` object inside
    the text box.
  - Constructing the `fimath` object in the
    MATLAB or model workspace and then entering its
    variable name in the text box. If you use this option
    and plan to share your model with others, define the
    variable in the model workspace.

For more information, see fimath Object Construction (Fixed-Point Designer)
and Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer).

#### Tips

- The `fimath` object of a MATLAB Function block behaves
  as a `globalfimath` (Fixed-Point Designer) object for the contents of the
  block. The block associates the `fimath`
  object properties in this parameter with all fixed-point and
  integer input signals to the MATLAB Function
  block that you choose to treat as `fi`
  objects. Constructing `fi` objects in the
  MATLAB Function block introduces
  additional considerations.

  - If no `fimath` object is
    associated with a `fi` object when
    it is constructed, then the `fi`
    constructor uses the default
    `fimath` object settings regardless
    of the properties in **MATLAB function
    fimath**. If you perform operations on
    the `fi` object after it is
    constructed, the object adopts the properties in
    **MATLAB function
    fimath**.
  - If you specify a `fimath`
    object in the `fi` constructor,
    then the `fi` constructor obeys
    that `fimath` object when
    quantizing the value. Any `fimath`
    object settings not specified in the
    `fi` constructor use the
    specified properties in **MATLAB function
    fimath**.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or the `Stateflow.EMChart` object of the block and change the
associated object property by using dot notation.

If you use the `MATLABFunctionConfiguration`
object, specify the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `FimathMode` |
| **Values:** | `"SameAsMATLAB"` (default) | `"UserSpecified"` |

If you use the `Stateflow.EMChart` object, specify
the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `EmlDefaultFimath` |
| **Values:** | `"Same as MATLAB Default"` (default) | `"Other:UserSpecified"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `yesa` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

You can generate Halide code if you have Embedded Coder® license. For more information, see Speed Up Generated Code Execution with Halide Code (Embedded Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. Actual data type or capability support depends
on block implementation. For best practices of using the MATLAB
Function block, see:

- Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder)
- Design Guidelines for the MATLAB Function Block (HDL Coder)
- Generate Instantiable Code for Functions (HDL Coder)
- Optimize MATLAB Loops (HDL Coder)
- Pipeline MATLAB Expressions (HDL Coder)

**HDL Architecture**

|  |  |
| --- | --- |
| `MATLAB Function` (Default) | This is the default architecture for MATLAB Function blocks with fixed-point data types. When you use this architecture, you can use speed and area optimizations for blocks that surround the MATLAB Function block. The code inside the MATLAB Function block is not optimized. |
| `MATLAB Datapath` | This is the default architecture for MATLAB Function blocks with floating-point data types. When you use this architecture, the code generator treats the MATLAB Function block like a regular Subsystem block. By enabling this architecture for fixed-point types, you can use speed and area optimizations for blocks inside the MATLAB Function block and across the MATLAB Function block with other Simulink blocks.  This capability enables you to specify additional properties for the MATLAB Function block that you would specify for a Subsystem such as **ClockRatePipelining** and **FlattenHierarchy**. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also AdaptivePipelining (HDL Coder). |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also ClockRatePipelining (HDL Coder). |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove MATLAB Function block hierarchy from generated HDL code. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also FlattenHierarchy (HDL Coder). |
| **GuardIndexVariables** | Choose whether or not to lift matrix accesses out of conditional MATLAB statements. The default is `off`. To specify this property, set **Architecture** to `MATLAB Function`. See also GuardIndexVariables (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **InstantiateFunctions** | Generate a VHDL® `entity` or Verilog® `module` for each function. The default is `off`. See also InstantiateFunctions (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. If you set **Architecture** to `MATLAB Datapath`, you can only unroll loops. If you want to use loop streaming with the `MATLAB Datapath` architecture, you can use the streaming optimization by specifying a **StreamingFactor**. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. To specify this property, set **Architecture** to `MATLAB Datapath`. See also Streaming (HDL Coder). |
| **VariablesToPipeline** | **Warning**  `VariablesToPipeline` is not recommended. Use `coder.hdl.pipeline` (HDL Coder) instead.  Insert a pipeline register at the output of the specified variable or variables. Specify the list of variables as a character vector, with spaces separating the variables. To specify this property, set **Architecture** to `MATLAB Function`. |

**Data Type Support**

HDL code generation supports half-precision data types for these functions in
MATLAB Function block:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `all` | `and, &` | `any` | `cast` | `conj` | `ctranspose` |
| `end` | `=` | `eq` | `==` | `ge, >=` | `gt, >` |
| `half` | `inf` | `int8` | `int16` | `int32` | `int64` |
| `isa` | `iscolumn` | `isempty` | `isequal` | `isfinite` | `isfloat` |
| `isinf` | `isinteger` | `islogical` | `isnan` | `isnumeric` | `isreal` |
| `isrow` | `isscalar` | `isvector` | `le, <=` | `length` | `logical` |
| `lt, <` | `max` | `min` | `minus, -` | `NaN` | `ndims` |
| `ne, ~=` | `not` | `numel` | `or, |` | `plus, +` | `prod` |
| `reshape` | `single` | `size` | `sqrt` | `sum` | `times, .*` |
| `transpose` | `uint8` | `uint16` | `uint32` | `uint64` | `uminus` |
| `uplus` | `vertconcat` | - | - | - | - |

**Complex Data Support**

This block supports code generation for complex signals.

See also Complex Data Type Support (HDL Coder).

**Use `hdlfimath` Setting**

The `hdlfimath` function is a utility that defines
`fimath` properties optimized for HDL code generation. For
more information, see Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder).

**Tunable Parameter Support**

HDL Coder supports both tunable and non-tunable parameters with the
following data types:

- Scalar
- Vector
- Complex
- Structure
- Enumeration

For details, see Generate DUT Ports for Tunable Parameters (HDL Coder) and Design Guidelines for the MATLAB Function Block (HDL Coder).

**Generate HDL Code with Algebraic Loops**

To generate HDL code for models that contain Matlab Function
blocks:

- In the Configuration Parameters dialog box, click
  **Diagnostics**, and set the
  **Algebraic loop** parameter to
  `none` or
  `warning`.
- Open the block mask for the Matlab Function block and
  select the **Treat as atomic unit** and
  **Minimize algebraic loop occurrences**
  parameters.

**Restrictions**

- If the block contains a System object™, block inputs cannot have non-discrete (constant or
  `Inf`) sample time.
- HDL Coder does not support a MATLAB Function that
  contains the same variable as the input and output of the function. For
  example, this MATLAB code is not
  supported.

  ```
  function y = myFun(y)
  %#codegen

  y = 3 * y;
  ```
- The block supports floating-point data types only in the Native
  Floating Point mode.

For the MATLAB language subset supported for HDL code generation from a
MATLAB Function block, see Supported MATLAB Data Types, Operators, and Control Flow Statements (HDL Coder).

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

**PLC Block Properties**

|  |  |
| --- | --- |
| **UseExternalDefinition** | Suppress block definition in generated code. The default is `Off`. See also UseExternalDefinition (Simulink PLC Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2011a**

### R2023a: Specify how to treat output variables with dimension of length 1

With the new **Treat dimensions of length 1 as fixed size** parameter,
you can specify how MATLAB Function blocks treat output variables
when at least one dimension has length 1. Prior to R2023a, MATLAB
Function blocks treat output variables with a dimension of length 1 as
fixed size, regardless of whether you specify the variables as having variable
size.

### R2021b: Output column vectors as two-dimensional or one-dimensional data

You can now output column vectors in MATLAB Function blocks as
two-dimensional or one-dimensional data with the **Interpret output column
vectors as one-dimensional data** parameter.

### R2021a: Report runtime errors for MATLAB Function blocks in rapid accelerator mode

Report runtime errors for MATLAB Function blocks when simulating in
rapid accelerator mode by setting the **Enable memory integrity checks**
configuration parameter to `Always on`.

### R2020a: 64-bit integer type support for MATLAB Function block

MATLAB Function blocks now support 64-bit integer data. The block
implements `int64` and `uint64` data types as
fixed-point numbers with a word length of 64 bits and a fraction length of 0.

### R2019b: String support for MATLAB Function block

Simulink strings are now supported in MATLAB Function
blocks.
