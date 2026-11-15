---
type: simulink-block
title: 'Index Vector'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'indexvector'
documentation_source_path: 'slref/indexvector.html'
language: en
---

# Index Vector

## Ports

### Input

### **Port\_1** — Control signal scalar

Control signal, specified as a scalar. When the control input is not an integer value,
the block truncates the value to an integer by rounding to zero.

For information on control signals of enumerated type, see Guidelines on Setting Parameters for Enumerated Control Port on the Multiport
Switch block ref page.

#### Limitations

- If the control signal is numeric, the control signal
  cannot be complex.
- If the control signal is an enumerated signal, the block
  uses the value of the underlying integer to select a data
  port.
- If the underlying integer does not correspond to a data
  input, an error occurs.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **0 or 1** — First data input scalar | vector

First data input, specified as a scalar or vector. The port is labeled
**0** when you set **Data port
order** to `Zero-based
contiguous`, and labeled **1** when you
set **Data port order** to `One-based
contiguous`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus` | `enumerated` | `string`
### Output

### **Port\_1** — Selected data input, based on control signal value scalar

The block outputs the selected value from the input data vector, according to the
control signal value. The output is a scalar.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### Main

### **Data port order** — Type of ordering for data input ports `Zero-based contiguous` (default) | `One-based contiguous` | `Specify indices`

Specify the type of ordering for your data input ports.

- `Zero-based contiguous` — Block uses
  zero-based indexing for ordering contiguous data ports. This is
  the default value of the Index Vector
  block.
- `One-based contiguous` — Block uses
  one-based indexing for ordering contiguous data ports. This is
  the default value of the Multiport Switch
  block.
- `Specify indices` — Block uses
  noncontiguous indexing for ordering data ports. This value is
  supported only for configurations with two or more input data
  ports.

#### Tips

- When the control port is of enumerated type, select
  `Specify indices`.
- If you select `Zero-based
  contiguous` or `One-based
  contiguous`, verify that the control port
  is not of enumerated type. This configuration is deprecated
  and produces an error. You can run the Upgrade Advisor on
  your model to replace each Multiport Switch
  block of this configuration with a block that explicitly
  specifies data port indices. See Model Upgrades.
- Avoid situations where the block contains unused data
  ports for simulation or code generation. When the control
  port is of fixed-point or built-in data type, verify that
  all data port indices are representable with that type.
  Otherwise, the following block behavior occurs:

  | If the block has unused data ports and data port order is: | The block produces: |
  | --- | --- |
  | `Zero-based contiguous` or `One-based contiguous` | A warning |
  | `Specify indices` | An error |

#### Dependencies

Selecting `Zero-based contiguous` or
`One-based contiguous` enables the
**Number of data ports** parameter.

Selecting `Specify indices` enables the
**Data port indices** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataPortOrder` |
| **Type:** character vector |
| **Values:** `'Zero-based contiguous' | 'One-based contiguous' | 'Specify indices'` |
| **Default:** `'Zero-based contiguous'` |

### **Number of data ports** — Number of data input ports `1` (default) | integer between 1 and 65536

Specify the number of data input ports to the block.

#### Dependencies

To enable this parameter, set **Data port order**
to `Zero-based contiguous` or
`One-based contiguous`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** integer between 1 and 65536 |
| **Default:** `'1'` |

### Signal Attributes

### **Require all data port inputs to have the same data type** — Require all inputs to have the same data type `off` (default) | `on`

Select this check box to require that all data input ports have the same data
type. When you clear this check box, the block allows data port inputs to have
different data types.

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first data input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `string` | `Simulink.ImageType(480,640,3)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule`—Simulink® chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware. If you change the embedded
  target settings, the data type selected by the internal rule might
  change. It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the internal rule
  doesn’t meet your specific needs for numerical accuracy or performance,
  use one of the following options:

  - Specify the output data type explicitly.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your model. For more
    information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use this block
    are available in the Signal Attributes library Data Type
    Propagation Examples block.
- `Inherit: Inherit via back propagation` —
  Uses the data type of the driving block.
- `Inherit: Same as first data input` — Uses
  the data type of the first data input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `Simulink.ImageType(480,640,3)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Integer rounding mode** — Specify the rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Choose one of these rounding modes.

`Ceiling`
:   Rounds both positive and negative numbers
    toward positive infinity. Equivalent to the
    MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds to the nearest even
    integer. Equivalent to the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds both positive and negative numbers
    toward negative infinity. Equivalent to the
    MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds toward positive
    infinity. Equivalent to the Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable
    value. If a tie occurs, rounds positive numbers
    toward positive infinity and rounds negative
    numbers toward negative infinity. Equivalent to
    the Fixed-Point Designer
    `round` function.

`Simplest`
:   Automatically chooses between round toward
    floor and round toward zero to generate rounding
    code that is as efficient as possible.

`Zero`
:   Rounds number toward zero. Equivalent to the
    MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RndMeth` |
| **Type**: character vector |
| **Values**: `'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **Default**: `'Floor'` |

#### See Also

For more information, see Rounding Modes (Fixed-Point Designer).

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

### **Allow different data input sizes (Results in variable-size output signal)** — Allow input signals with different sizes `off` (default) | `on`

Select this check box to allow input signals with different sizes.

- `On` — Allows input signals with different sizes, and
  propagate the input signal size to the output signal. In this mode, the
  block produces a variable-size output signal.
- `Off` — Requires that all nonscalar data input signals be
  the same size.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AllowDiffInputSizes` |
| **Type:** character vector |
| **Value:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

The Index Vector block is a Multiport Switch block with **Number of data
ports** set to 1. For HDL code generation information, see Multiport Switch.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Switch output between different inputs based on value of first input

The Index Vector block is a special configuration of the Multiport Switch block in which you specify one data input and the control
input is zero-based. The block output is the element of the input vector whose index
matches the control input. For example, if the input vector is `[18 15 17
10]` and the control input is `3`, the element that
matches the index of 3 (zero-based) is 10, and that becomes the output value.

The Index Vector and Multiport Switch blocks are alternative configurations of the same
block.

- Index Vector — Switch output between different inputs based on value of first
  input.
- Multiport Switch — Select output signal based on control
  signal.

To configure a Multiport Switch block to work as an Index
Vector block set **Number of data ports** to
`1` and **Data port order** to
`Zero-based contiguous`.
