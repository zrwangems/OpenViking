---
type: simulink-block
title: 'Discrete FIR Filter'
family: 'hdlcoder'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretefirfilter'
documentation_source_path: '../simulink/slref/discretefirfilter.html'
language: en
---

# Discrete FIR Filter

## Ports

### Input

### **In** — Input signal scalar | vector | matrix

Input signal to filter, specified as a scalar, vector, or
matrix.

The Discrete FIR Filter block accepts real and complex
signals of any numeric data type supported by Simulink.

#### Dependencies

When you set **Coefficient source** to
`Dialog parameters`, the port for the
input signal is unlabeled. When you set **Coefficient
source** to `Input port`, the
port for the input signal is labeled **In**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Num** — Filter coefficients scalar | vector

Specify the filter coefficients as a scalar or a vector. When you specify a row vector
of filter taps, the block applies a single filter to the input. To apply
multiple filters to the input, specify the coefficients in the matrix
form through the **Coefficients** parameter.

#### Dependencies

To enable this port, set **Coefficient source**
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **External reset** — External reset signal scalar

External reset signal, specified as a scalar. When the specified
trigger event occurs, the block resets the states to their initial conditions.

**Tip**

The icon for this port changes based on the value of the
**External reset** parameter.

#### Dependencies

To enable this port, set **External reset** to
`Rising`,
`Falling`,
`Either`,
`Level`, or `Level
hold`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **⎍** — Enable signal scalar

Enable signal, specified as a scalar. This port can control execution
of the block. The block is enabled when the input to this port is
nonzero, and is disabled when the input is `0`. The
value of the input is checked at the same time step as the block
execution.

#### Dependencies

To enable this port, select the **Show enable
port** check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Filtered output signal scalar | vector | matrix

Filtered output signal, returned as a scalar, vector, or a matrix. The Discrete
FIR Filter block outputs real and complex signals of any
numeric data type supported by Simulink.

When the input to the block is fixed-point, the data type of the block output is
determined based on the value you specify in the
**Output** parameter. When the input is
floating-point, the output data type matches the input data type since
floating-point inheritance takes precedence over the fixed-point
settings.

When you set **Sample time** to
`-1`, sample time of the output signal is same as the
sample time of the input signal **In**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Coefficient source** — Source of coefficients `Dialog parameters` (default) | `Input port`

Choose to specify the filter coefficients using tunable dialog parameters or through an
input port, which is useful for time-varying coefficients.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CoefSource` |
| **Type:** character vector |
| **Values:** `'Dialog parameters' | 'Input port'` |
| **Default:** `'Dialog parameters'` |

### **Filter structure** — Filter structure `Direct form` (default) | `Direct form symmetric` | `Direct form antisymmetric` | `Direct form transposed` | `Lattice MA`

Select the filter structure you want the block to implement. For more information, see
Algorithms.

#### Dependencies

You must have an available DSP System Toolbox license to run a model with a Discrete FIR
Filter block that implements any filter structure other
than `Direct form`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterStructure` |
| **Type:** character vector |
| **Values:** `'Direct form' | 'Direct form symmetric' | 'Direct form antisymmetric' | 'Direct form transposed' | 'Lattice MA'` |
| **Default:** `'Direct form'` |

### **Coefficients** — Filter coefficients `[0.5 0.5]` (default) | scalar | vector | matrix

Specify the filter coefficients as a scalar, vector or a matrix.

When you specify a row vector of filter taps, the block applies a
single filter to the input. To apply multiple filters to the same input,
specify a matrix of coefficients, where each row represents a different
set of filter taps. To implement multiple filters, set **Filter
structure** to `Direct form` and
the input must be a scalar.

#### Dependencies

To enable this parameter, set **Coefficient
source** to `Dialog
parameters`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Coefficients` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0.5 0.5]'` |

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing.
You can select one of the following options:

- `Elements as channels (sample based)`
  — Treat each element of the input as an independent
  channel (sample-based processing).
- `Columns as channels (frame based)`
  — Treat each column of the input as an independent
  channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputProcessing` |
| **Type:** character vector |
| **Values:** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **Default:** `'Elements as channels (sample based)'` |

### **Initial states** — Initial conditions of filter states `0` (default) | scalar | vector | matrix

Specify the initial conditions of the filter states. To learn how to
specify initial states, see Specifying Initial States.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialStates` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0'` |

### **Show enable port** — Create enable port `off` (default) | `on`

Select to control execution of this block with an enable port. The block is considered
enabled when the input to this port is nonzero, and is disabled when the input is
`0`. The value of the input is checked at the same time step as the
block execution.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **External reset** — External state reset `None` (default) | `Rising` | `Falling` | `Either` | `Level` | `Level hold`

Specify the trigger event to use to reset the states to the initial conditions.

| Reset Mode | Behavior |
| --- | --- |
| `None` | No reset |
| `Rising` | Reset on a rising edge |
| `Falling` | Reset on a falling edge |
| `Either` | Reset on either a rising or falling edge |
| `Level` | Reset in either of these cases:  - When the reset signal is nonzero at the current time   step - When the reset signal value changes from nonzero at the   previous time step to zero at the current time step |
| `Level hold` | Reset when the reset signal is nonzero at the current time step |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ExternalReset` |
| **Type**: character vector |
| **Values**: `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **Default**: `'None'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### **View Filter Response** — View filter response button

Click this button to open the Filter Visualization Tool (`fvtool` (DSP System Toolbox)) and display the filter response of the filter
defined in the block dialog box.

#### Dependencies

To enable this parameter, set the **Coefficient source** parameter to
`Dialog parameters`.

This parameter appears only if you have a valid DSP System Toolbox license.

### Data Types

### **Tap sum** — Tap sum data type `Inherit: Same as input` (default) | `Inherit: Inherit via internal rule` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the tap sum data type of a direct form symmetric or direct
form antisymmetric filter, which is the data type the filter uses when
it sums the inputs prior to multiplication by the coefficients. You can
set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

This parameter is only visible when you set the **Filter
structure** to `Direct form
symmetric` or `Direct form
antisymmetric`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `TapSumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Coefficients** — Coefficient data type `Inherit: Same wordlength as input` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the coefficient data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `CoefDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same word length as input'| 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same wordlength as input'` |

### **Coefficients minimum** — Minimum value of coefficients `[]` (default) | scalar

Specify the minimum value that a filter coefficient should have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `CoeffMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Coefficients maximum** — Maximum value of coefficients `[]` (default) | scalar

Specify the maximum value that a filter coefficient should have. The
default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `CoeffMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the product output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `ProductDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the accumulator data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `AccumDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **State** — State data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the state data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Lattice
MA`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `StateDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as accumulator'` |

### **Output** — Output data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

When the input to the block is floating-point, the output data type
matches the input data type since floating-point inheritance takes
precedence over the fixed-point settings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as accumulator'` |

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock data type settings of this block against changes by the
Fixed-Point Tool and the Fixed-Point Advisor. For more information,
see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

## Libraries

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports custom state attributes to customize and generate code more
efficiently. To access or set these attributes, open the Model Data Editor. On the
**Modeling** tab, click **Model
Data Editor**. For an example, see Custom State Attributes in Discrete FIR Filter block.

**Generate SIMD code using Intel AVX2 code replacement
library**

**Note**

Requires Embedded Coder® license

The Discrete FIR Filter block supports SIMD code generation using Intel AVX2
code replacement library under these conditions:

- **Filter structure** is set to `Direct
  form` or `Direct form
  transposed`.
- **Input processing** is set to `Columns
  as channels (frame based)`.
- Input signal is real-valued with real filter coefficients.
- When **Filter structure** is set to
  `Direct form`, input signal is
  complex-valued with real or complex filter coefficients.
- Input signal has a data type of `single` or
  `double`.

**Generate SIMD code by
leveraging target hardware instruction set extensions** *(since R2022b)*

**Note**

Requires Simulink
Coder™ or Embedded Coder license

You can generate SIMD code for the Discrete FIR Filter block on all
Intel® platforms, ARM®
Cortex®-A processors, and Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions** under
these conditions:

- You set **Filter structure** to `Direct
  form`
- You set **Input processing** to `Columns
  as channels (frame based)`
- Input signal is real-valued with real filter coefficients
- Input signal is real-valued or complex-valued.
- Data type of the input signal is `single`
  (ARM
  Cortex-A processors)
- Data type of the input signal is `single` or
  `double` (Intel platforms)

In addition, configure your model appropriately.

In the **Modeling** tab of the Simulink model window, click **Model Settings** and configure
these parameters under **Code Generation**.

- In the **Optimization** pane:

  - Provide a specific instruction set in the
    **Leverage target hardware instruction set
    extensions** parameter.
  - Select the **Optimize reductions**
    parameter.
  - Under **Optimization levels**, set
    **Level** to
    `Maximum` and
    **Priority** to `Maximize
    execution speed`.
- In the **Interface** pane, under **Software
  environment**, clear **non-finite
  numbers**.

To generate SIMD code from this block using this workflow, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks (DSP System Toolbox).

For computationally intensive operations on supported blocks, SIMD intrinsics can
significantly improve the performance of the generated code on Intel platforms. For
more details, see Optimize Code for Reduction Operations by Using SIMD (Simulink Coder). To generate SIMD
code from this block, see Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Note**

For hardware-friendly valid and reset control signals, and to model exact
hardware latency behavior in Simulink, use the Discrete FIR Filter (DSP HDL Toolbox) block
instead.

**HDL Architecture**

The block has `HDLDataPath` as a default
architecture. This architecture provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Block Properties**

| HDL Block Properties | Description |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **FlattenFilter** | Remove hierarchy of Filter subsystem from generated HDL code. The default is `auto`. See FlattenHierarchy (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **MultiplerArchitecture** | Select the multipler architecture as `linear` or `shiftadd`. The default is `linear`. For more information, see HDL Code Generation section in Product, Matrix Multiply. |
| **MultiplierInputPipeline** | Specify the number of pipeline stages to add at filter multiplier inputs. See also MultiplierInputPipeline (HDL Coder). |
| **MultiplierOutputPipeline** | Specify the number of pipeline stages to add at filter multiplier outputs. See also MultiplierOutputPipeline (HDL Coder). |
| **AdderChainArchitecture** | Select the adder architecture to generate linear chain or tree structure of adders to compute sum of elements. The default is `tree`. For more information, see HDL Code Generation section in Sum. |
| **AdderOutputPipeline** | Number of output pipeline stages to insert in the generated code for addition operation. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Enumerated | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes | Yes | Yes |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**Limitations and Considerations**

The block has these limitations:

- You must set **Initial conditions** to
  `0`. HDL code generation is not supported for
  nonzero initial states.
- **Filter Structure**: `Lattice
  MA`.
- **External reset** parameter must be set to
  `None` or `Level
  hold`.

To configure the Discrete FIR Filter block for special cases
such as a programmable filter or a multichannel filter, use the following block
settings:

| Filter Case | Considerations |
| --- | --- |
| **Programmable Filter** | HDL Coder supports programmable filters for Discrete FIR Filter blocks.  1. On the filter block mask, set    **Coefficient source** to    **Input port**. 2. Connect a vector signal to the    `Num` coefficient port. |
| **Multichannel Filter** | HDL Coder supports the use of vector inputs to Discrete FIR Filter blocks, where each element of the vector represents an independent channel.  1. Connect a vector signal to the Discrete FIR    Filter block input port. 2. Specify **Input processing** as    `Elements as channels (sample    based)`. |
| **Frame-Based Input** | HDL Coder supports the use of vector inputs to Discrete FIR Filter blocks, where each element of the vector represents a sample in time. You can use an input vector of up to 512 samples. The frame-based implementation supports fixed-point input and output data types, and uses full-precision internal data types. You can use real input signals with real coefficients, complex input signals with real coefficients, or real input signals with complex coefficients. You can also use frame-based input with programmable coefficients.  1. Connect a vector signal to the Discrete FIR    Filter block input port. 2. Specify **Input processing** as    `Columns as channels (frame    based)`. For frame-based input with    programmable coefficients, set **Filter    structure**  to `Direct    form`.  When you use frame-based input data you can use either complex input signals and real coefficients, or complex coefficients and real input signals. |
| **Filter with Control Ports** | You can generate HDL code for filters with the optional enable port, and with the optional reset port. |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2008a**

### R2024b: Generate SIMD code for Apple silicon processors

In R2024b, if you have Embedded Coder, you can generate SIMD code for the Discrete FIR Filter
block for Apple silicon processors by using the model configuration parameter
**Leverage target hardware instruction set extensions**. For
more information, see Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon (DSP System Toolbox).

### R2024b: View filter response

Click the **View Filter Response** button to visualize the frequency
response of the filter that you specify in the block dialog box.

### R2023b: Generate SIMD Code for Complex Signals

In R2023b, if you have Embedded Coder, you can generate SIMD code for the Discrete FIR Filter
block when the input signal is complex-valued by using the model configuration
parameter **Leverage target hardware instruction set
extensions**.

### R2023b: Conditional display of the **Sample time** parameter

The Discrete FIR Filter block no longer displays the
**Sample time** parameter in the block parameters dialog box by
default. The parameter is visible only if you set the sample time to a value other
the default value (`-1`) at the command line or in an existing
model. For more information, see Blocks for Which Sample Time Is Not Recommended.

## Description

Model FIR filters

The Discrete FIR Filter block independently filters each channel of the input
signal with the specified digital FIR filter. The block can implement static filters
with fixed coefficients, and time-varying filters with coefficients that change over
time. You can tune the coefficients of a static filter during simulation.

This block filters each channel of the input signal independently
over time. The **Input processing** parameter allows
you to specify whether the block treats each element of the input
as an independent channel (sample-based processing), or each column
of the input as an independent channel (frame-based processing). To
perform frame-based processing, you must have a DSP System Toolbox™ license.

The output dimensions equal the input dimensions, except when you specify a matrix of filter
taps for the **Coefficients** parameter. When you do so, the output
dimensions depend on the number of different sets of filter taps you specify.

This block supports custom state attributes to customize and generate code more efficiently.
For an example, see Custom State Attributes in Discrete FIR Filter block. Under certain
conditions, the block also supports SIMD code generation. For details, see Code Generation.

The outputs of this block numerically match the outputs of the DSP System Toolbox
Digital Filter Design (DSP System Toolbox) block.

This block supports the Simulink® state logging feature. For more information, see State.

### Filter Structure Support

You can change the filter structure implemented with the Discrete FIR Filter block by selecting one of the following from the **Filter structure** parameter:

- `Direct form`
- `Direct form symmetric`
- `Direct form antisymmetric`
- `Direct form transposed`
- `Lattice MA`

You must have an available DSP System Toolbox license
to run a model with any of these filter structures other than `Direct form`.

For more information on the filter structures, see Algorithms.

### Specifying Initial States

The Discrete FIR Filter block initializes the
internal filter states to zero by default, which has the same effect
as assuming that past inputs and outputs are zero. You can optionally
use the **Initial states** parameter to specify nonzero initial conditions for the filter delays.

To determine the number of initial states you must specify and
how to specify them, see the table on valid initial states. The **Initial states** parameter can take one of the forms described in the next table.

**Valid Initial States**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel:  - The vector length equals the product of the number of   input channels and the number of delay elements in the   filter, `#_of_filter_coeffs-1` (or   `#_of_reflection_coeffs` for   `Lattice MA`). - The matrix must have the same number of rows as the   number of delay elements in the filter, `#_of_filter_coeffs-1` (`#_of_reflection_coeffs` for `Lattice MA`), and must have one column for each channel of the input signal. |
