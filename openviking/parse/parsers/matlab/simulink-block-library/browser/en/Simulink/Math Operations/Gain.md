---
type: simulink-block
title: 'Gain'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'gain'
language: en
---

# Gain

Multiply input by constant

## Libraries

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Description

The Gain block multiplies the input by a constant value, or gain. The input
and the gain can each be a scalar, vector, or matrix.

You specify the value of gain in the **Gain** parameter. The
**Multiplication** parameter lets you specify element-wise or
matrix multiplication. For matrix multiplication, this parameter also lets you indicate
the order of the multiplicands.

The gain is converted from doubles to the data type specified in the block mask offline
using round-to-nearest and saturation. The input and gain are then multiplied, and the
result is converted to the output data type using the specified rounding and overflow
modes.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

The Gain block accepts real or complex-valued scalar, vector, or matrix
input. The Gain block supports fixed-point data types. If
the input of the Gain block is real and gain is complex,
the output is complex.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Input multiplied by gain scalar | vector | matrix

The Gain block outputs the input multiplied by a constant gain value.
When the input to the Gain block is real and gain is
complex, the output is complex.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Gain** — Value by which to multiply the input `1` (default) | real or complex-valued scalar, vector, or matrix

Specify the value by which to multiply the input. The gain can be a real or
complex-valued scalar, vector, or matrix.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Gain` |
| **Values:** | `'1'` (default) | real or complex-valued scalar, vector, or matrix in quotes |

### **Multiplication** — Specify the multiplication mode `Element-wise(K.*u)` (default) | `Matrix(K*u)` | `Matrix(u*K)` | `Matrix(K*u) (u vector)`

Specify one of these multiplication modes:

- `Element-wise(K.*u)` — Each element
  of the input is multiplied by each element of the gain. The
  block performs expansions, if necessary, so that the input and
  gain have the same dimensions.
- `Matrix(K*u)` — The input and gain are matrix-multiplied with
  the input as the second operand.
- `Matrix(u*K)` — The input and gain are matrix-multiplied with
  the input as the first operand.
- `Matrix(K*u) (u vector)` — The input
  and gain are matrix multiplied with the input as the second
  operand. This mode is identical to
  `Matrix(K*u)`, except for how dimensions
  are determined.

  Suppose that `K` is an
  `m-by-n` matrix. `Matrix(K*u)(u
  vector)` sets the input to a vector of length
  `n` and the output to a vector of length
  `m`. In contrast,
  `Matrix(K*u)` uses propagation to determine
  dimensions for the input and output. For an
  `m-by-n` gain matrix, the input can
  propagate to an `n-by-q` matrix, and the output
  becomes an `m-by-q` matrix.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Multiplication` |
| **Values:** | `'Element-wise(K.*u)'` (default) | `'Matrix(K*u)'` | `'Matrix(u*K)'` | `'Matrix(K*u) (u vector)'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule`
  — The software chooses a data type to balance numerical
  accuracy, performance, and generated code size, while taking
  into account the properties of the embedded target hardware. If
  you change the embedded target settings, the data type selected
  by the internal rule might change. For example, if the block
  multiplies an input of type `int8` by a gain of
  `int16` and
  `ASIC/FPGA` is specified as the
  targeted hardware type, the output data type is
  `sfix24`. If `Unspecified
  (assume 32-bit Generic)`, in other words, a
  generic 32-bit microprocessor, is specified as the target
  hardware, the output data type is `int32`. If
  none of the word lengths provided by the target microprocessor
  can accommodate the output range, the software displays an error
  in the Diagnostic Viewer.
- `Inherit: Keep MSB`– The software chooses a data type that
  maintains the full range of the operation, then reduces the
  precision of the output to a size appropriate for the embedded
  target hardware.

  **Tip**

  For more efficient generated code, clear
  **Saturate on integer
  overflow**.

  This rule never produces overflows.
- `Inherit: Match scaling` – The
  software chooses a data type whose scaling matches the scaling
  of the input types. If the full range of the type does not fit
  on the embedded target hardware, the range is reduced yielding a
  type appropriate for the embedded target hardware. This rule can
  produce overflows.

  It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If these
  internal rules do not meet your specific needs for numerical
  accuracy or performance, use one of the following options:

  - Specify the output data type explicitly.
  - Use the simple choice of `Inherit:
    Same as input`.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your
    model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use the data type of the driving
  block.
- `Inherit: Same as input` — Use the
  data type of the input signal.

#### Dependencies

When the input is a floating-point data type smaller than single precision, the
`Inherit: Inherit via internal rule`
output data type depends on the setting of the **Inherit floating-point output type smaller than single
precision** configuration parameter. Data types are
smaller than single precision when the number of bits needed to
encode the data type is less than the 32 bits needed to encode the
single-precision data type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

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

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

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

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for
  data types. Selecting `Inherit` enables a
  second menu/text box to the right where you can select the
  inheritance mode.
- `Built in` — Built-in data types.
  Selecting `Built in` enables a second menu/text
  box to the right where you can select a built-in data
  type.
- `Fixed point` — Fixed-point data
  types. Selecting `Fixed point` enables
  additional parameters that you can use to specify a fixed-point
  data type.
- `Expression` — Expressions that
  evaluate to data types. Selecting `Expression`
  enables a second menu/text box to the right, where you can enter
  the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the Show data type assistant
button .

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

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### Parameter Attributes

### **Parameter minimum** — Specify the minimum value of gain `[]` (default) | scalar

Specify the minimum value of gain. The default value is `[]`
(unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter maximum** — Specify the maximum value of gain `[]` (default) | scalar

Specify the maximum value of gain. The default value is `[]`
(unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter data type** — Specify the data type of the Gain parameter `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Inherit from 'Gain'` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the **Gain**
parameter.

Setting **Parameter data type** to
`Inherit: Inherit via internal rule` lets
the Gain block select a data type based on an internal
heuristic that looks at the current gain value and provides a full
precision data type to represent the current gain value. When you update
the diagram, the software deduces a data type to fit the gain value
`3` with high precision and no range loss. For
example, with this heuristic, if the specified gain value is
`3`, the Gain block deduces a
selected data type of `sfix32_En29`. Consequently, this
deduced data type cannot hold values greater than `4`.
During simulation, if you tune the gain value to `6`,
an overflow occurs in the selected data type and the behavior is
unexpected.

While tuning a parameter with this **Parameter data
type** setting, specify the **Parameter
Minimum** and **Parameter Maximum**
parameters. These settings tell the software about the range of values
you want during the simulation and allows the software to provide a full
precision data type with sufficient range to allow safe tuning of the
gain value within the specified range.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as input'` | `'Inherit: Inherit from 'Gain''` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

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

**Tunable Parameters**

You can use a tunable parameter in a Gain block intended for
HDL code generation. For details, see Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

| `ConstMultiplierOptimization` | Description |
| --- | --- |
| `none`(*Default*) | By default, HDL Coder does not perform CSD or FCSD optimizations. Code generated for the Gain block retains multiplier operations. |
| `csd` | When you specify this option, the generated code decreases the area used by the model while maintaining or increasing clock speed, using canonical signed digit (CSD) techniques. CSD replaces multiplier operations with add and subtract operations.  CSD minimizes the number of addition operations required for constant multiplication by representing binary numbers with a minimum count of nonzero digits. |
| `fcsd` | This option uses factored CSD (FCSD) techniques, which replace multiplier operations with shift and add/subtract operations on certain factors of the operands. These factors are generally prime but can also be a number close to a power of 2, which favors area reduction. You can achieve a greater area reduction with FCSD at the cost of decreasing clock speed. |
| `auto` | When you specify this option, the coder chooses between the CSD or FCSD optimizations. The coder chooses the optimization that yields the most area-efficient implementation, based on the number of adders required. When you specify `auto`, the coder does not use multipliers, unless conditions are such that CSD or FCSD optimizations are not possible (for example, if the design uses floating-point arithmetic). |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Note**

For certain values of the **Gain** parameter, native
floating point implements the algorithm differently instead of using
multipliers. For example, if you set the **Gain** parameter
to `1`, the generated model uses a wire to pass the input
to the output. If you set the **Gain** parameter to
`-1`, the generated model shows a Unary
Minus block that inverts the polarity of the input signal. This
implementation reduces the latency and resource usage on the target
platform.

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
