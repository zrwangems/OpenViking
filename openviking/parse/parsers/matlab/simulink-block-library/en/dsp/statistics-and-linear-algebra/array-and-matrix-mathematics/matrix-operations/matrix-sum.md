---
type: simulink-block
title: 'Sum'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'sum'
documentation_source_path: 'slref/sum.html'
language: en
---

# Sum

## Ports

### Inputs

The inputs can be of different data types unless you select **Require all
inputs to have the same data type**.

### **Port\_1** — First input operand signal scalar | vector | matrix

Input signal to the addition or subtraction operation. If there is
only one input signal, then addition or subtraction is performed on the
elements over all dimensions or the specified dimension.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_n** — *n*th input operand signal scalar | vector | matrix

*n*th input signal to the operations. The number of
inputs matches the number of signs in the **List of
signs** parameter. The block applies the operations to the
inputs in the order listed. You can also use a numerical value equal to
the number of input ports as the **List of signs**
parameter. The block creates the input ports and applies addition to all
inputs. For example, if you assign `5` for the
**List of signs** parameter, the block creates
`5` input ports and adds them together to produce
the output.

All nonscalar inputs must have the same dimensions. Scalar inputs are
expanded to have the same dimensions as other inputs.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal resulting from addition and/or subtraction operations.
The output signal has the same dimension as the input signals.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Icon shape** — Block icon shape `rectangular` | `round`

Designate the icon shape of the block as rectangular or round.

The default value depends on the block configuration.

- `round` default —
  Sum block
- `rectangular` default —
  Add, Subtract, and
  Sum of Element blocks

For a rectangular block, the first input port is the top port. For a
round Sum block, the first input port is the port closest
to the 12 o'clock position going in a counterclockwise direction around
the block. Similarly, other input ports appear in counterclockwise order
around the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IconShape` |
| **Type**: character vector |
| **Values**: `'rectangular'` | `'round'` |

### **List of signs** — Operations performed on inputs `+` | `-` | `|` | integer

Enter addition and subtraction operations performed on the inputs. An
input port is created for each operation. A spacer
(`|`) creates extra space between the input ports on
the block icon. Addition is the default operation. If you only want to
add the inputs, enter the number of input ports. The operations are
performed in the order listed.

The default value depends on the block configuration.

- `|++` default — Sum
  block
- `++` default — Add
  block
- `+-` default — Subtract
  block
- `+` default — Sum of
  Element block

When you enter only one sign, the block enables the **Apply
over** parameter. For a vector input, `+`
or `-` adds or subtracts the elements over all
dimensions or in the specified dimension.

#### Tips

You can manipulate the positions of the input ports on the block
by inserting spacers (`|`) between the signs in the
**List of signs** parameter. For
example, “`++|--`” creates an extra
space between the second and third input ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Inputs` |
| **Type**: character vector |
| **Values**: `'+'` | `'-'` | `|` | integer |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply function along specified dimensions.

- `All dimensions` — Apply function for
  all input values for all dimensions.

  For example, in this model, **List of
  signs** is set to `+`, and
  **Apply over** is set to `All
  dimensions`. The block returns the sum of all
  input values from all dimensions.

  2D matrix with Constant block value [1 2 3 4 5 6] as input to Sum block configured for all dimensions

  When you select configuration parameter **Use algorithms optimized for row-major array
  layout**, the software enables row-major
  algorithms for simulation. To generate row-major code, set the
  configuration parameter **Array layout (Simulink Coder)** to
  `Row-major`, and select
  **Use algorithms optimized for row-major array
  layout**. The column-major and row-major algorithms
  differ only in the summation order. In some cases, due to
  different operation order on the same data set, you might
  experience minor numeric differences in the outputs of
  column-major and row-major algorithms.
- `Specified dimensions` — Apply
  function for all input values for specified dimension.

#### Dependencies

To enable this parameter, enter only one sign in the
**List of signs** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CollapseMode` |
| **Type**: character vector |
| **Values**: `'All dimensions'` | `'Specified dimension'` |
| **Default**: `'All dimensions'` |

### **Dimension** — Dimension along which to apply summation `1` (default) | positive integer

Specify the dimension along which to apply the summation as a positive
integer.

The block follows the same summation rules as the MATLAB®
`sum` function. For more information, see Algorithms.

For example, in this model, **List of signs** is
set to `+`, **Apply over** is set to
`Specified dimension`, and
**Dimension** is set to `2`. The
block returns the sum of the input values of each row.

2D matrix with Constant block value [1 2 3;4 5 6] as input to Sum block configured for dimension 2

If the specified dimension is greater than the dimension of the input,
an error message appears.

#### Dependencies

To enable this parameter, set **Apply over** to
`Specified dimension`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CollapseDim` |
| **Type**: character vector |
| **Value**: integer |
| **Default**: `'1'` |

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

### Signal Attributes

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as a
`Simulink.NumericType` object.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule` — The software chooses a data type to
  balance numerical accuracy, performance, and generated code
  size, while taking into account the properties of the
  embedded target hardware.

  **Note**

  The accumulator internal rule favors greater numerical
  accuracy, possibly at the cost of less efficient
  generated code. To get the same accuracy for the output,
  set the output data type to `Inherit:
  Inherit same as accumulator`.

  **Note**

  When input is a floating-point data type smaller than
  single precision, the `Inherit: Inherit via
  internal rule` output data type depends
  on the setting of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than
  single precision when the number of bits needed to
  encode the data type is less than the 32 bits needed to
  encode the single-precision data type. For example,
  `half` and `int16`
  are smaller than single precision.
- `Inherit: Keep MSB` – The
  software chooses a data type that maintains the full range
  of the operation, then reduces the precision of the output
  to a size appropriate for the embedded target hardware.

  **Tip**

  For more efficient generated code, set
  **Accumulator data type** to
  `Inherit: Inherit via internal
  rule`, and clear **Saturate
  on integer overflow**.

  This rule never produces overflows.
- `Inherit: Keep LSB`– The software
  chooses a data type that maintains the precision of the
  operation, but reduces the range if the full type does not
  fit on the embedded target hardware.

  **Tip**

  For more efficient generated code, set
  **Accumulator data type** to
  `Inherit: Inherit via internal
  rule`, and clear **Saturate
  on integer overflow**.

  This rule can produce overflows.

  If you change the embedded target settings, the data type
  selected by these internal rules might change. It is not
  always possible for the software to optimize code efficiency
  and numerical accuracy at the same time. If the rules do not
  meet your specific needs for numerical accuracy or
  performance, use one of the following options:

  - Specify the output data type
    explicitly.
  - Use the simple choice of `Inherit:
    Same as first input`.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your
    model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use data type of the driving
  block.
- `Inherit: Same as first input` —
  Use data type of the first input signal.
- `Inherit: Inherit same as
  accumulator`— Use data type of the
  accumulator.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'`|`'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Accumulator data type** — Data type of the accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type of the accumulator. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`. When you choose
`Inherit: Inherit via internal
rule`, Simulink® chooses a data type to balance numerical accuracy,
performance, and generated code size, while taking into account the
properties of the embedded target hardware.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**:  `AccumDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Require all inputs to have the same data type** — Require that all inputs have the same data type `off` (default) | `on`

Specify if input signals must all have the same data type. If you enable
this parameter, then an error occurs during simulation if the input
signal types are different.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture of Sum, Add, and Subtract Blocks**

The default `Linear` architecture generates a chain
of N operations (adders) for N inputs.

**HDL Architecture of Sum of Elements Block**

For the Sum of Elements block, HDL Coder supports `Tree` architectures for Sum of
Elements blocks that have a single vector input with multiple elements.

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

| Architecture | Additional cycles of latency | Description |
| --- | --- | --- |
| `Linear` | 0 | Generates a linear chain of adders to compute the sum of products.  For multiple inputs that have different bit widths, the `Linear` architecture optimizes the resource utilization by implementing adders in multiple stages with pipelines in between the stages. The output of each stage is calculated based on the width of the inputs to that stage. |
| `Tree` | 0 | Generates a tree structure of adders to compute the sum of products. |

**HDL
Block Properties**

**Note**

To use the **LatencyStrategy** setting in the **Native
Floating Point** tab of the HDL Block Properties dialog box, specify
`Linear` or `Tree` as the HDL
Architecture.

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Note**

The Sum of Elements block does not support HDL code generation with double data types
in the Native Floating Point mode.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Complex Data Support**

The default `Linear` implementation
supports complex data.

The `Tree`  implementation supports complex data with
`+` for the **List of signs** block parameter. With
native floating point support, the `Tree`  implementation supports
complex data with both `+` and `-` for **List of
signs**.

**Limitations and Considerations**

To generate HDL code for multi-input Sum block that has mixed
scalar and vector inputs, you must specify vector input at one of the first two
inputs of the Sum block.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Specify how to apply function using **Apply over** parameter, renamed from **Sum over**

When you enter only one sign for **List of signs**, the block
enables the **Apply over** parameter. For a vector input,
`+` or `-` adds or subtracts the elements over
all dimensions or in the specified dimension.

To better reflect the supported behavior, the **Sum over**
parameter is now called **Apply over**.

## Description

Add or subtract inputs

The Sum block performs addition or subtraction on its inputs. The
Add, Subtract, Sum of Elements, and
Sum blocks are alternative configurations of the same block. This
block can add or subtract scalar, vector, or matrix inputs. It can also collapse the
elements of a signal and perform a summation.

You specify the operations of the block with the **List of signs**
parameter with plus signs (`+`), minus signs (`-`),
and spacers (`|`).

- The number of `+` and `-` characters equals
  the number of inputs. For example, `+-+` requires three inputs.
  The block subtracts the second (middle) input from the first (top) input, and
  then adds the third (bottom) input.
- A spacer character creates extra space between ports on the block icon.
- If performing only addition, you can use a numerical value equal to the number
  of inputs.
- If there is only one input port, one `+` or
  `-` adds or subtracts the elements over all dimensions or
  in the specified dimension.

The Sum block first converts the input data type to its accumulator
data type, then performs the specified operations. The block converts the result to its
output data type using the specified rounding and overflow modes.

### Calculation of Block Output

Output calculation for the Sum block depends on the number of block
inputs and the sign of input ports.

| Number of Sum Block Input Ports | Input Port Signs | Block Output Calculation Formula | Output Formula Variables |
| --- | --- | --- | --- |
| One input port | The input port sign is + | y = e[0] + e[1] + e[2] ... + e[m] | `e[i]` is the *i*th element of input u |
| The input port sign is – | y = 0.0 – e[0] – e[1] – e[2] ... – e[m] |
| Two or more input ports | All input port signs are – | y = 0.0 – u[0] – u[1] – u[2] ... – u[n] | `u[i]` is the input to the *i*th input port |
| The *k*th input port is the first port where the sign is + | y = u[k] – u[0] – u[1] – u[2] – u[k–1] (+/–) u[k+1] ... (+/–) u[n] |
