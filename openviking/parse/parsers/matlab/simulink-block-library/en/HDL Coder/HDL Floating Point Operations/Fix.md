---
type: simulink-block
title: 'Math Function'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'ALG / AlgExpression'
documentation_page: 'mathfunction'
documentation_source_path: '../simulink/slref/mathfunction.html'
language: en
---

# Math Function

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_2
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Result of the operation of the function on the input or inputs scalar | vector | matrix
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix. Supported modes accept real and
complex inputs, except for `reciprocal`, which does not
accept complex fixed-point inputs. See Description.

#### Dependencies

Data type support for this block depends on the **Function** that you
select and the size of the inputs. For more information, see Data Type Support.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix. Supported modes accept real and
complex inputs, except for `reciprocal`, which does not
accept complex fixed-point inputs.

#### Dependencies

To enable this port, set **Function** to
`hypot`,
`rem`, or
`mod`.

Data type support for this block depends on the **Function** that you
select, and the size of the inputs. For more information, see Data Type Support.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Result of the operation of the function on the input or inputs scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix. The dimensions of the block
output depend on the **Function** that you select and
the size of the inputs. The block output is real or complex, depending
on what you select for **Output signal type**. See
Description.

#### `reciprocal` with Newton-Raphson Method

The `reciprocal` with Newton-Raphson method
output data type depends on the input data type:

| Input Data Type | Output Data Type |
| --- | --- |
| single | single |
| double | double |
| built-in integer | built-in integer |
| built-in fixed-point | built-in fixed-point |
| `fi` (*value*, 0, *word\_length*, *fraction\_length*) | `fi` (*value*, 0, *word\_length*, *word\_length*–*fraction\_length*–1) |
| `fi` (*value*, 1, *word\_length*, *fraction\_length*) | `fi` (*value*, 1, *word\_length*, *word\_length*–*fraction\_length*–2) |

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Function
  summary: Math function exp (default) | log | 2^u | 10^u | log10 | magnitude^2 | square | pow | conj | reciprocal | hypot
    | rem | mod | transpose | hermitian
  group: Main
  block_parameter: Operator
  type: character vector
  values: '''exp'' | ''log'' | ''2^u'' | ''10^u'' | ''log10'' | ''magnitude^2'' | ''square'' | ''pow'' | ''conj'' | ''reciprocal''
    | ''hypot'' | ''rem'' | ''mod'' | ''transpose'' | ''hermitian'''
  default: '''exp'''
- name: Algorithm method
  summary: Algorithm method for reciprocal function Exact (default) | Newton-Raphson
  group: Main
  block_parameter: AlgorithmType
  type: character vector
  values: '''Exact'' | ''Newton-Raphson'''
  default: '''Exact'''
- name: Signed power
  summary: Power signedness on (default) | off
  group: Main
  block_parameter: SignedPower
  type: character vector
  values: '''on'' | ''off'' |'
  default: '''on'''
- name: Output signal type
  summary: Complexity of output signal auto (default) | real | complex
  group: Main
  block_parameter: OutputSignalType
  type: character vector
  values: '''auto'' | ''real'' | ''complex'''
  default: '''auto'''
- name: Number of iterations
  summary: Number of Newton-Raphson iterations 3 (default) | scalar
  group: Main
  block_parameter: Iterations
  type: character vector
  values: '''3'' | scalar'
  default: '''3'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: Main
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  values: '''[]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  values: '''[]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Specify the output data type Inherit: Same as first input (default) | Inherit: Inherit via internal rule | Inherit:
    Inherit via back propagation | double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64
    | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule | ''Inherit: Same as first input'' | ''Inherit: Inherit via back propagation''
    | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64''
    | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Same as first input'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Signal Attributes
  block_parameter: RndMeth
  type: character vector
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: Choose the behavior when integer overflow occurs on (default) | boolean
  group: Signal Attributes
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
```

### Main

### **Function** — Math function `exp` (default) | `log` | `2^u` | `10^u` | `log10` | `magnitude^2` | `square` | `pow` | `conj` | `reciprocal` | `hypot` | `rem` | `mod` | `transpose` | `hermitian`

Specify the mathematical function. For more information about the options for this
parameter, see Description.

#### Dependency

Setting **Function** to
`pow` enables the **Signed
power** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'exp' | 'log' | '2^u' | '10^u' | 'log10' | 'magnitude^2' | 'square' | 'pow' | 'conj' | 'reciprocal' | 'hypot' | 'rem' | 'mod' | 'transpose' | 'hermitian'` |
| **Default:** `'exp'` |

### **Algorithm method** — Algorithm method for `reciprocal` function `Exact` (default) | `Newton-Raphson`

Algorithm method for `reciprocal` function, specified
as `Exact` or
`Newton-Raphson`. To calculate reciprocal
with the Newton-Raphson approximation method, select
`Newton-Raphson`. Otherwise, select
`Exact`.

#### Dependency

Setting **Function** to
`reciprocal` enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AlgorithmType` |
| **Type:** character vector |
| **Values:** `'Exact' | 'Newton-Raphson'` |
| **Default:** `'Exact'` |

### **Signed power** — Power signedness on (default) | off

When calculating power, specified as on or off, take into account sign of the input
signal. Math Function uses this parameter only when the
output signal is real.

- on — Calculate power of the absolute value of the input,
  multiplied by the sign of the input.
- off — Calculate power of the actual input value. If the first
  input is negative, the second input is not an integer, and the
  output signal is real, the function returns
  `NaN`.

#### Dependency

Setting **Function** to
`pow` enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignedPower` |
| **Type:** character vector |
| **Values:** `'on' | 'off' |` |
| **Default:** `'on'` |

### **Output signal type** — Complexity of output signal `auto` (default) | `real` | `complex`

Specify the output signal type of the Math Function block as
`auto`, `real`, or
`complex`.

| Function | Input Signal Type | Output Signal Type | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| `exp`, `log`, `2^u`, `10^u`, `log10`, `square`, `pow`, `reciprocal`, `conjugate`, `transpose`, `hermitian` | `real`  `complex` | `real`  `complex` | `real`  `error` | `complex`  `complex` |
| `magnitude squared` | `real`  `complex` | `real`  `real` | `real`  `real` | `complex`  `complex` |
| `hypot`, `rem`, `mod` | `real`  `complex` | `real`  `error` | `real`  `error` | `complex`  `error` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSignalType` |
| **Type:** character vector |
| **Values:** `'auto' | 'real' | 'complex'` |
| **Default:** `'auto'` |

### **Number of iterations** — Number of Newton-Raphson iterations 3 (default) | scalar

Number of Newton-Raphson iterations, specified as a scalar.

#### Dependencies

To enable this parameter, set:

- **Function** to
  `reciprocal`.
- **Algorithm method** to
  `Newton-Raphson`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Iterations` |
| **Type:** character vector |
| **Values:** `'3' | scalar` |
| **Default:** `'3'` |

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

### **Output data type** — Specify the output data type `Inherit: Same as first input` (default) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

- To enable this parameter, set the
  **Function** to
  `magnitude^2`,
  `square`, or
  `reciprocal`.
- For the `magnitude^2` and
  `square`, when input is a
  floating-point data type smaller than single precision, the
  `Inherit: Inherit via internal
  rule` output data type depends on the
  setting of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than
  single-precision when the number of bits needed to encode
  the data type is less than the 32 bits needed to encode the
  single precision data type. For example,
  `half` and `int16` are
  smaller than single precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Same as first input'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding
the **Output** data type you specify on the block. For
more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`, or
`reciprocal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Rounding mode for fixed-point operations. For more information, see
Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function into the mask field.

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`, or
`reciprocal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Choose the behavior when integer overflow occurs `on` (default) | boolean

| Action | Rationale | Overflows | Example |
| --- | --- | --- | --- |
| Select **Saturate on integer overflow** check box. | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box selected, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of -128. |
| Do not select **Saturate on integer overflow** check box. | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Overflows wrap to the appropriate value that is representable by the data type. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box cleared, the software interprets the overflow-causing value as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8`, is -126. |

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. The code generation process can
detect when overflow is not possible. In this case, the code generator
does not produce saturation code.

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`,
`conj`,
`reciprocal`, or
`hermitian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |
## Libraries

Simulink / Math Operations HDL Coder / Math Operations

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

**HDL Architecture**

| Function | Architecture | Description |
| --- | --- | --- |
| `conj` | `ComplexConjugate` | Calculate complex conjugate. |
| `hermitian` | `Hermitian` | Calculate hermitian. |
| `transpose` | `Transpose` | Calculate array transpose. See Math Function in the Simulink documentation. |
| `mod`  `rem` | `ShiftAdd` | Perform modulus or remainder operation on a built-in integer types input by using a non-restoring division algorithm that performs multiple shift and add operations to compute the `mod` and `rem` operations.  `ShiftAdd` is a pipelined implementation, and it can introduce additional latency in the generated code. Using this architecture, you can also set the latency strategy by setting the **LatencyStrategy** parameter. |

**Reciprocal Architecture**

When you set the **Algorithm method** to
`Exact`, you can select this options in HDL Block
properties of this block.

| Architecture | Parameters | Additional Cycles of Latency | Description |
| --- | --- | --- | --- |
| `ShiftAdd(default)` | None | Signed input: (Input word length + 4)  Unsigned input: (Input word length + 4)  For floating-point latency of the block, see Latency Values of Floating-Point Operators (HDL Coder). | Perform reciprocal operation on a fixed-point or floating point input by using a non-restoring division algorithm that performs multiple shift and add operations to compute the reciprocal. This architecture provides improved accuracy compared to the Newton-Raphson approximation method.  When you use fixed-point data types, following criteria must be satisfied for generating the HDL code:  - Input word length (`WL`) must be   less than or equal to 63. - `[WL input + Abs(FL Sum)]` must   be less than or equal to 63. Where, `FL   Sum` is given by,  `FL sum = FL input + FL   output` |

You can apply sharing optimization for Math Function Reciprocal block in
`ShiftAdd` architecture. For more information, see
Resource Sharing (HDL Coder).

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

HDL code generation also supports the Newton-Raphson algorithm method for
`reciprocal` function. Select the **Algorithm
method** as `Newton-Raphson` to use these
architectures for `reciprocal` function in the Math
Function block.

| Architecture | Additional Cycles of Latency | Description |
| --- | --- | --- |
| `ReciprocalNewton` (default) | `Iterations` + 1 | Use the multirate implementation of the iterative Newton method. Select this option to optimize area for your design.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is from 2 through 10. If `Iterations` value is outside the recommended range, HDL Coder displays a message. |
| `ReciprocalNewtonSingleRate` | (`Iterations` \* 2) + 1 | Use the single rate pipelined Newton method. Select this option to optimize speed for your design, or if you want a single rate implementation.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is between 2 and 10. If `Iterations` value is outside the recommended range, HDL Coder displays a message. |
| ReciprocalRsqrtBasedNewtonSingleRate | Signed input: (`Iterations` \* 4) + 8  Unsigned input: (`Iterations` \* 4) + 6 | Use the single rate pipelined Newton method. Select this option to optimize speed, or if you want a single rate implementation.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is from 2 through 10. If `Iterations` is outside the recommended range, the coder generates a message. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | To enable this property, set HDL architecture to `ShiftAdd`. Specify whether to map the blocks in your design to `MAX`, `Min`, `CUSTOM`, or `ZERO` latency for fixed-point types. The default is `MAX`. See also LatencyStrategy (HDL Coder). |
| **CustomLatency** | To enable this property, set HDL architecture to `ShiftAdd`. When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **CheckResetToZero** | Use this property for the `mod` and `rem` functions of the Math Function block. If you have numbers `a` and `b` such that the quotient `a/b` is close to an integer, this setting treats `a` as an integral multiple of `b`, and `rem(a,b)` = 0. This result is numerically accurate and matches the simulation results. Calculating this result uses additional resources and increases the area footprint on the target FPGA device. For more information, see CheckResetToZero (HDL Coder). |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |
| **MaxIterations** | Use this property for the `mod` and `rem` functions of the Math Function block. If you have numbers `a` and `b` that are significantly large integers, you can increase **MaxIterations** to match the simulation results. Calculating this result uses additional resources and increases the area footprint on the target FPGA device. For more information, see MaxIterations (HDL Coder). |
| **IterationsPerPipeline** | Use this property for the `reciprocal` function of the Math Function block. To enable this property, set **Algorithm method** parameter to `Exact`. When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages. For more information, see Reciprocal (HDL Coder). |

**Supported Datatypes and Functions in Native Floating-Point**

The Math Function block supports scalar, vector, or matrix data types. This
block supports these functions with Native Floating-Point.

| Math Functions | Supported Floating-Point Datatypes | | | Fixed-Point Datatype Support | Complex Data Support |
| --- | --- | --- | --- | --- | --- |
| Half | Single | Double |
| `exp` | No | Yes | No | No | No |
| `log` | No | Yes | Yes | No | No |
| `2^u` | No | Yes | No | No | No |
| `10^u` | No | Yes | No | No | No |
| `log10` | No | Yes | No | No | No |
| `magnitude^2` | No | Yes | Yes | Yes | Yes |
| `square` | No | Yes | No | Yes | Yes |
| `pow` | No | Yes | No | No | No |
| `conj` | No | Yes | No | Yes | Yes |
| `reciprocal` | Yes | Yes | Yes | Yes | No |
| `hypot` | No | Yes | No | No | No |
| `rem` | No | Yes | No | No | No |
| `mod` | No | Yes | No | No | No |
| `transpose` | Yes | Yes | Yes | Yes | Yes |
| `hermitian` | No | Yes | No | Yes | Yes |

**Restrictions**

When you use a `reciprocal` implementation:

- Input must be scalar and must have integer or fixed-point (signed or
  unsigned) data type.
- The output must be scalar and have integer or fixed-point (signed or
  unsigned) data type.
- The **Saturate on integer overflow** option on the
  block must be selected.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The Math Function block only supports fixed-point conversion in certain
configurations. For more information, see the Block Support Table.

## Version History

**Introduced before R2006a**

### R2023a: `Math Function` Block Supports 2^u

The Math Function block now supports the
`2^u` function. The MATLAB equivalent is `2.^u` (see `power`).

## Description

Perform mathematical function

The Math Function block performs many common mathematical functions.

You can select one of these functions from the **Function** parameter list
in Math Function block.

| Function | Description | Mathematical Expression | MATLAB® Equivalent |
| --- | --- | --- | --- |
| `exp` | Exponential | `eu` | `exp` |
| `log` | Natural logarithm | `ln u` | `log` |
| `2^u` | Power of base 2 | `2u` | `2.^u`  (see `power`) |
| `10^u` | Power of base 10 | `10u` | `10.^u`  (see `power`) |
| `log10` | Common (base 10) logarithm | `log u` | `log10` |
| `magnitude^2` | Complex modulus | `|u|2` | `real(u).^2 + imag(u).^2`   (see `real`, `imag`, and `power`) |
| `square` | Power 2 | `u2` | `u.^2`  (see `power`) |
| `pow` | Power | - With **Signed power** selected and   **Output signal type** set to   `real`, the expression is   `sign(u)*|u|v`. - With **Signed power** cleared or   **Output signal type** set to   `complex`, the expression is   `uv`. - When **Output signal type** is set to   `auto`, the expression depends on the   complexity type that the software compiles. | `power` |
| `conj` | Complex conjugate | `ū` | `conj` |
| `reciprocal` with Exact method | Reciprocal | `1/u` | `1./u`  (see `rdivide`) |
| `reciprocal` with Newton-Raphson method | Reciprocal | See Newton-Raphson Reciprocal Algorithm Method | None |
| `hypot` | Square root of sum squares | `(u2+v2)0.5` | `hypot` |
| `rem` | Remainder after division | — | `rem` |
| `mod` | Modulus after division | — | `mod` |
| `transpose` | Transpose | `uT` | `u.'`  (see Array vs. Matrix Operations) |
| `hermitian` | Complex conjugate transpose | `uH` | `u'`  (see Array vs. Matrix Operations) |

**Tip**

To perform square root calculations, use the Sqrt block.

The block output is the result of the operation of the function on the input or inputs. The
functions support these types of operations.

| Function | Scalar Operations | Element-Wise Vector and Matrix Operations | Vector and Matrix Operations |
| --- | --- | --- | --- |
| `exp` | Yes | Yes | Not applicable |
| `log` | Yes | Yes | Not applicable |
| `2^u` | Yes | Yes | Not applicable |
| `10^u` | Yes | Yes | Not applicable |
| `log10` | Yes | Yes | Not applicable |
| `magnitude^2` | Yes | Yes | Not applicable |
| `square` | Yes | Yes | Not applicable |
| `pow` | Yes | Yes | Not applicable |
| `conj` | Yes | Yes | Not applicable |
| `reciprocal` with Exact method | Yes | Yes | Not applicable |
| `reciprocal` with Newton-Raphson method | Yes | Yes | Not applicable |
| `hypot` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | — |
| `rem` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | Not applicable |
| `mod` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | Not applicable |
| `transpose` | Yes | — | Yes |
| `hermitian` | Yes | — | Yes |

The name of the function and the appropriate number of input ports appear on the block.

**Tip**

Use the Math Function block when you want vector or matrix output.

### Newton-Raphson Reciprocal Algorithm Method

The `reciprocal` function that has the Newton-Raphson algorithm method
calculates the reciprocal by using the Newton-Raphson approximation method. The
function uses recursive approximation to find better approximations to the roots of
a real-value function.

The reciprocal of a real number a is defined as a zero of the function:

f(x)=1x−a.

Simulink® chooses an initial estimate in the range 0<x0<2a, because this is the domain of convergence for the
function.

To successively calculate the roots of the function, specify the **Number of
iterations** parameter. The process is repeated as follows:

xi+1=xi−f(xi)f'(xi)=xi+(xi−axi2)=xi.(2−axi)

f'(x) is the derivative of the function f(x).

### Data Type Support

This table lists the input data types that each function of the block can support.

| Function | Single | Double | Half\* | Boolean | Built-In Integer | Fixed Point |
| --- | --- | --- | --- | --- | --- | --- |
| `exp` | Yes | Yes | Yes | — | — | — |
| `log` | Yes | Yes | Yes | — | — | — |
| `2^u` | Yes | Yes | Yes | — | — | — |
| `10^u` | Yes | Yes | Yes | — | — | — |
| `log10` | Yes | Yes | Yes | — | — | — |
| `magnitude^2` | Yes | Yes | Yes | — | Yes | Yes |
| `square` | Yes | Yes | Yes | — | Yes | Yes |
| `pow` | Yes | Yes | Yes | — | — | — |
| `conj` | Yes | Yes | Yes | — | Yes | Yes |
| `reciprocal` with Exact method | Yes | Yes | Yes | — | Yes | Yes |
| `reciprocal` with Newton-Raphson method (for more information, see Output) | Yes | Yes | — | — | Yes | Yes |
| `hypot` | Yes | Yes | Yes | — | — | — |
| `rem` | Yes | Yes | Yes | — | Yes | — |
| `mod` | Yes | Yes | Yes | — | Yes | — |
| `transpose` | Yes | Yes | Yes | Yes | Yes | Yes |
| `hermitian` | Yes | Yes | Yes | — | Yes | Yes |

For more information on half-precision arithmetic operations, see The Half-Precision Data Type in Simulink (Fixed-Point Designer).
