---
type: simulink-block
title: 'Abs'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'abs'
documentation_source_path: 'slref/abs.html'
language: en
---

# Abs

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal to the absolute value block.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Absolute value output signal scalar | vector

Absolute value of the input signal.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

### **Output data type** — Specify the output data type `Inherit: Same as input` (default) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting of
the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
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
| **Values**: `'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Same as input'` |

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

### **Saturate on integer overflow** — Choose the behavior when integer overflow occurs `off` (default) | `on`

When you select this check box, saturation applies to every internal
operation on the block, not just the output or result. In general, the
code generation process can detect when overflow is not possible. In
this case, the code generator does not produce saturation code.

| Action | Reason for Taking This Action | What Happens | Example |
| --- | --- | --- | --- |
| Select this check box. | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to the maximum value that the data type can represent. | The number 130 does not fit in a signed 8-bit integer and saturates to 127. |
| Do not select this check box. | You want to optimize efficiency of your generated code. | Overflows wrap to the appropriate value that is representable by the data type. | The number 130 does not fit in a signed 8-bit integer and wraps to -126. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals with floating-point
types in `Native Floating Point` mode.

Code generation for the block with complex signals that use fixed-point types
is not supported. To calculate the magnitude of a complex number, use the Complex to Magnitude-Angle (DSP HDL Toolbox) block
instead.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Output absolute value of input

The Abs block outputs the absolute value of the input.

For signed-integer data types, the absolute value of the most negative value is not
representable by the data type. In this case, the **Saturate on integer
overflow** check box controls the behavior of the block.

| If you... | The block... | And... |
| --- | --- | --- |
| Select this check box | Saturates to the most positive value of the integer data type | - For 8-bit signed integers, -128 maps to 127. - For 16-bit signed integers, -32768 maps to 32767. - For 32-bit signed integers, -2147483648 maps to   2147483647. |
| Do not select this check box | Wraps to the most negative value of the integer data type | - For 8-bit signed integers, -128 remains -128. - For 16-bit signed integers, -32768 remains -32768. - For 32-bit signed integers, -2147483648 remains   -2147483648. |

The Abs block supports zero-crossing detection. However, when you select
**Enable zero-crossing detection** on the dialog box, the block
does not report the simulation minimum or maximum in the Fixed-Point Tool. If you want
to use the Fixed-Point Tool to analyze a model, disable zero-crossing detection for all
Abs blocks in the model first.
