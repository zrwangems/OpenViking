---
type: simulink-block
title: 'Divide'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'divide'
documentation_source_path: 'slref/divide.html'
language: en
---

# Divide

## Ports

### Input

### **X** — Input signal to multiply scalar | vector | matrix | N-D array

Input signal to be multiplied with other inputs.

#### Dependencies

To enable one or more **X** ports, specify one or
more `*` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Element-wise(.*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **÷** — Input signal to divide or invert scalar | vector | matrix | N-D array

Input signal for division or inversion operations.

#### Dependencies

To enable one or more **÷** ports, specify one or
more `/` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Element-wise(.*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_1** — First input to multiply or divide scalar | vector | matrix | N-D array

First input to multiply or divide, provided as a scalar, vector,
matrix, or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — Nth input to multiply or divide scalar | vector | matrix | N-D array

Nth input to multiply or divide, provided as a scalar, vector, matrix,
or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **\*** — Input signal to multiply scalar | vector | matrix | N-D array

Input signal to be multiplied with other inputs.

#### Dependencies

To enable one or more **\*** ports, specify one or
more `*` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Matrix(*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Inv** — Input signal to divide or invert scalar | vector | matrix | N-D array

Input signal for division or inversion operations.

#### Dependencies

To enable one or more **Inv** ports, specify one
or more `/` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Matrix(*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output computed by multiplying, dividing, or inverting inputs scalar | vector | matrix | N-D array

Output computed by multiplying, dividing, or inverting inputs.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Number of inputs** — Control number of inputs and type of operation `*/` (default) | positive integer scalar | `*` or `/` for each input port

Control two properties of the block:

- The number of input ports on the block
- Whether each input is multiplied or divided into the
  output

When you specify:

- **`1` or
  `*` or
  `/`**

  The block has one input port. In element-wise mode, the block
  processes the input as described for the Product of
  Elements block. In matrix mode, if the parameter
  value is `1` or `*`, the block
  outputs the input value. If the value is `/`,
  the input must be a square matrix (including a scalar as a
  degenerate case) and the block outputs the matrix inverse. See
  Element-Wise Mode and Matrix Mode for more
  information.
- **Integer value > 1**

  The block has the number of inputs given by the integer value.
  The inputs are multiplied together in element-wise mode or
  matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.
- **Unquoted string of two or more
  `*` and `/`
  characters**

  The block has the number of inputs given by the length of the
  character vector. Each input that corresponds to a
  `*` character is multiplied into the
  output. Each input that corresponds to a `/`
  character is divided into the output. The operations occur in
  element-wise mode or matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** `'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **Default:** `'*/'` |

### **Multiplication** — Element-wise (.\*) or Matrix (\*) multiplication `Element-wise(.*)` (default) | `Matrix(*)`

Specify whether the block performs `Element-wise(.*)` or
`Matrix(*)` multiplication.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Multiplication` |
| **Type:** character vector |
| **Values:** `'Element-wise(.*)' | 'Matrix(*)'` |
| **Default:** `'Element-wise(.*)'` |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply the function along specified dimensions.

- `All dimensions` — Apply function for all input
  values for all dimensions.
- `Specified dimension` — Apply function for all input
  values for specified dimension.

For example, in this model, **Multiplication** is set to
`Element-wise(.*)`, and **Apply over**
is set to `All dimensions`. The block returns the product of
all values from all dimensions.

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for all dimensions

#### Dependencies

To enable this parameter, set **Number of inputs** to
`*` and **Multiplication** to
`Element-wise (.*)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseMode` |
| **Type:** character vector |
| **Values:** `'All dimensions' | 'Specified dimension'` |
| **Default:** `'All dimensions'` |

### **Dimension** — Dimension along which to multiply `1` (default) | positive integer

Specify the dimension along which to multiply, as a
positive integer. For example, for a 2-D matrix, `1`
applies the function to each column, and `2` applies
the function to each row.

For example, in this model,
**Multiplication** is set to
`Element-wise(.*)`,
**Apply over** is set to
`Specified dimension`,
and **Dimension** is set to
`2`. The block returns the
product of all values from each row.

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for dimension 2

#### Dependencies

To enable this parameter:

- Set **Number of inputs** to
  `*`
- Set **Multiplication** to
  `Element-wise
  (.*)`
- Set **Apply over** to
  `Specified
  dimension`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseDim` |
| **Type:** character vector |
| **Values:** `'1' | '2' | ...` |
| **Default:** `'1'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`. For more information, see
Control Data Types of Signals.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal rule`
  — Simulink® chooses a data type to balance numerical
  accuracy, performance, and generated code size, while taking
  into account the properties of the embedded target hardware.
  If you change the embedded target settings, the data type
  selected by the internal rule might change. For example, if
  the block multiplies an input of type
  `int8` by a gain of
  `int16` and
  `ASIC/FPGA` is specified as
  the targeted hardware type, the output data type is
  `sfix24`. If
  `Unspecified (assume 32-bit
  Generic)`, in other words, a generic
  32-bit microprocessor, is specified as the target hardware,
  the output data type is `int32`. If none of
  the word lengths provided by the target microprocessor can
  accommodate the output range, Simulink software displays an error in the Diagnostic
  Viewer.

  It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the
  internal rule doesn’t meet your specific needs for numerical
  accuracy or performance, use one of the following options:

  - Specify the output data type
    explicitly.
  - Use the simple choice of
    `Inherit: Same as
    input`.
  - Explicitly specify a default data type such
    as `fixdt(1,32,16)` and then use
    the Fixed-Point Tool to propose data types for
    your model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use data type of the
  driving block.
- `Inherit: Same as first input` — Use
  data type of first input signal.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting
of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
precision when the number of bits needed to encode the data type is
less than the 32 bits needed to encode the single-precision data
type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding mode for fixed-point operations. You can
select:

`Ceiling`
:   Rounds positive and negative numbers toward positive
    infinity. Equivalent to the MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds to the nearest even integer. Equivalent to
    the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds positive and negative numbers toward negative
    infinity. Equivalent to the MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds toward positive infinity. Equivalent to the
    Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds positive numbers toward positive infinity and
    rounds negative numbers toward negative infinity. Equivalent
    to the Fixed-Point Designer
    `round` function.

`Simplest`
:   Chooses between rounding toward floor and rounding toward
    zero to generate rounding code that is as efficient as
    possible. This rounding mode is affected by these
    configuration parameters on the **Hardware
    Implementation** pane.

    - If the **Signed integer division rounds
      to** parameter is set to
      `Zero` or
      `Undefined`,
      `Simplest` resolves to
      zero.
    - If the **Signed integer division rounds
      to** parameter is set to
      `Floor`,
      `Simplest` resolves to
      `floor`.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function into the mask field.

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

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

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

**Expected Differences Between Simulation and Code Generation**

These conditions may yield different results between simulation and the
generated code:

- The Divide block inputs contain a
  `NaN` or `inf` value
- The Divide block generates `NaN` or
  `inf` during execution

This difference is due to the nonfinite `NaN` or
`inf` values. In such cases, inspect your model
configuration and eliminate the conditions that produce `NaN`
or `inf`.

**Code Optimizations**

The Simulink
Coder™ build process provides efficient code for matrix inverse and
division operations. This table describes the benefits and when each benefit is
available.

| Benefit | Small Matrices  (2-by-2 to 5-by-5) | Medium Matrices  (6-by-6 to 20-by-20) | Large Matrices  (larger than 20-by-20) |
| --- | --- | --- | --- |
| Faster code execution time, compared to R2011a and earlier releases | Yes | No | Yes |
| Reduced ROM and RAM usage, compared to R2011a and earlier releases | Yes, for real values | Yes, for real values | Yes, for real values |
| Reuse of variables | Yes | Yes | Yes |
| Dead code elimination | Yes | Yes | Yes |
| Constant folding | Yes | Yes | Yes |
| Expression folding | Yes | Yes | Yes |
| Consistency with MATLAB Coder results | Yes | Yes | Yes |

For blocks that have three or more inputs of different dimensions, the code
might include an extra buffer to store temporary variables for intermediate
results.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

To perform an HDL-optimized divide operation, connect a Product block to a Divide
block and set the **Number of Inputs parameter** of the Divide
block to `/`.

**HDL Architecture**

The Divide block is the same as a Product block
with **Number of Inputs** set to `*/`.

| Architecture | Description |
| --- | --- |
| `ShiftAdd` (Default) | Perform divide operations by using a non-restoring division algorithm that performs multiple shift and add operations to compute the quotient.  When **Architecture** is set to `ShiftAdd`, the block uses pipelined architecture that breaks the computation into stages. This pipelined design introduces latency in HDL implementation. You can specify the latency by using the **LatencyStrategy** HDL block property. By default, **LatencyStrategy** is set to `Max`. To implement the block without latency, set **LatencyStrategy** to `Zero`. |

**Reciprocal Mode**

When **Number of Inputs** is set to `/`, the
Divide block is in reciprocal mode.

| Architectures | Description |
| --- | --- |
| `ShiftAdd` (Default) | Perform reciprocal operation by using a non-restoring division algorithm that performs multiple shift and add operations to compute the reciprocal. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | To enable this property, set HDL architecture to `ShiftAdd`. Specify whether to map the blocks in your design to `MAX`, `Min`, `Custom`, or `ZERO` latency for fixed-point and floating-point types. The default is `inherit`. See also LatencyStrategy (HDL Coder).  You can control the pipeline stages for the iterative algorithm by setting the **LatencyStrategy** to `Custom(PerIterations)`. For more information, see Divide (HDL Coder). |
| **CustomLatency** | To enable this property, set HDL architecture to `ShiftAdd`. When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |
| **IterationsPerPipeline** | When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages.  For more information, see Divide (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |
| **DivisionAlgorithm** | Specify whether to use the Radix-2 or Radix-4 algorithm to perform the floating-point division. The Radix-2 mode offers a tradeoff between latency and frequency. The Radix-4 mode offers a tradeoff between latency and resource usage. For more information, see DivisionAlgorithm (HDL Coder). |

**Latency Details**

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**Native Floating-Point Latency**

| Operator | Floating-Point Type | Latency Strategy | Latency (in cycles) | Custom Latency Support |
| --- | --- | --- | --- | --- |
| Divide | Double | Min | 31 | Yes |
| Max | 61 |
| Single | Min | 17 |
| Max | 32 |
| Half | Min | 10 |
| Max | 19 |
| Reciprocal | Double | Min | 6 | Yes |
| Max | 9 |
| Single | Min | 6 |
| Max | 8 |
| Half | Min | 4 |
| Max | 7 |

**Fixed-Point Latency**

| Operator | Additional cycles of latency | Latency Strategy Support | Custom Latency Support |
| --- | --- | --- | --- |
| Divide | Depends on word-length and fractional-length of input and output. For more information, see `HDLMathLib` Divide (HDL Coder). | Yes | Yes |
| Reciprocal | Depends on word-length and fractional-length of input and output. For more information, see `HDLMathLib` Reciprocal (HDL Coder). | Yes | Yes |

**Block Parameter Configuration**

HDL code generation supports different output data types for `divide
(*/)` and `reciprocal (/)` operations in
`ShiftAdd`. You can use these output data types for
the blocks:

- `Inherit: Inherit via internal
  rule`
- `Inherit: Keep MSB​`
- `Inherit: Match scaling​`
- `Inherit: Inherit via back
  propagation`​
- `Inherit: Same as first input​`
- `Integer types
  (uint8,int8,uint16,int16,uint32,int32,uint64,int64)​`
- `Fixed point types​`
- `Floating-point types`

You can use these integer rounding modes for the block:

| Blocks | Integer Rounding Modes |
| --- | --- |
| Divide | - `Zero` - `Simplest` - `Ceiling` *(since R2025a)* - `Convergent` *(since R2025a)* - `Floor` *(since R2025a)* - `Nearest` *(since R2025a)* - `Round` *(since R2025a)* |
| Reciprocal | - `Zero` - `Ceiling` *(since R2025a)* - `Convergent` *(since R2025a)* - `Floor` *(since R2025a)* - `Nearest` *(since R2025a)* - `Round` *(since R2025a)* - `Simplest` *(since R2025a)* |

**Note**

When you deploy the generated HDL code onto the target hardware, make sure
that you set the **signed integer division rounds to**
parameter in the **Hardware Implementation** pane of the
Configuration Parameters dialog box to `Zero` or
`Floor`.

**Complex Data Support**

This block does not support code generation for division with
complex signals.

**Optimizations**

You can use these HDL Coder optimizations to optimize the speed, area, and
I/Os.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

You can apply the sharing or streaming optimizations for Divide and Reciprocal
blocks using `ShiftAdd` architecture.

| Block (Inputs) | Resource Sharing | Streaming |
| --- | --- | --- |
| Divide(/\* or \*/) | Yes | Yes |
| Reciprocal (/) | Yes | No |

When you use sharing optimization on these blocks, make sure to enclose the
block in the atomic subsystem and set the **Default parameter
behavior** configuration parameter to
`Inlined`.

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior.  For the Divide and Reciprocal blocks, HDL Coder distributes pipeline registers around the blocks instead of within them. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**I/O Optimization**

| Optimization | Description |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | To optimize the I/O needed for your design, use frame-to-sample conversion. This optimization converts frame-based vector or matrix inputs to smaller-sized samples or pixels for HDL code generation to target stream-based hardware and reduce the FPGA I/O needed to handle large input and output signals. |

**HDL Modeling Guidelines**

For best practices of using the block, see:

- Design Considerations for Matrices and Vectors (HDL Coder)
- Modeling Efficient Multiplication and Division Operations for FPGA Targeting (HDL Coder)
- Guidelines for Using Rounding and Saturation Settings for Fixed-Point Data Types (HDL Coder)

**Restrictions**

When you use the Divide block in reciprocal mode, the following
restrictions apply:

- When you use fixed-point types, the input and output must be scalar.
  To use vector inputs, use floating-point types input and output.
- You must select the **Saturate on integer overflow**
  option on the block.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Divide and Reciprocal blocks use ShiftAdd as default architecture

The **Architecture** HDL block property is now
`ShiftAdd` by default for the Divide and Reciprocal
blocks. The code generated with the `ShiftAdd` setting is
more hardware-friendly than the other existing architectures.

These architecture settings were removed from the
**Architecture** HDL block property in the Divide and
Reciprocal blocks:

| Blocks | Architecture Settings |
| --- | --- |
| Divide | `Linear` |
| Reciprocal | `Linear`  `ReciprocalRsqrtBasedNewtonSingleRate` |

The linear architecture was using division operator (/) for implementing the
block, which did not support pipelining. This results to long combinational paths
and lower performance. The shift-add architecture uses pipelined architecture that
breaks the computation into stages. This pipelined design introduces latency in HDL
implementation. To implement the block without latency, set
**LatencyStrategy** to `Zero`.

## Description

Divide one input by another

The Divide block outputs the result of dividing its first input by its
second. The inputs can be scalars, a scalar and a nonscalar, or two nonscalars that have
the same dimensions. This block supports only complex input values at division ports
when all ports have the same single or double data type.

The Divide block is functionally a Product block that has two block
parameter values preset:

- **Multiplication —**
  `Element-wise(.*)`
- **Number of Inputs —**
  `*/`

Setting nondefault values for either of those parameters can change a Divide
block to be functionally equivalent to a Product block or a Product of Elements block.
