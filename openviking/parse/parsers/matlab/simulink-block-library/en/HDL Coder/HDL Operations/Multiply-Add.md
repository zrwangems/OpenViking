---
type: simulink-block
title: 'Multiply-Add'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Operations'
documentation_page: 'multiplyadd'
documentation_source_path: 'ref/multiplyadd.html'
language: en
---

# Multiply-Add

## Ports
```yaml
ports:
- name: a
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: b
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: c
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: Output signal scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### Input

### **a** — Input signal `scalar` | `vector` | `matrix`

Input signal to be multiplied with input to Port
`b`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **b** — Input signal `scalar` | `vector` | `matrix`

Input signal to be multiplied with input to Port
`a`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **c** — Input signal `scalar` | `vector` | `matrix`

Input signal that gets added or subtracted to the product of
`a` and `b` depending on
**Function** setting.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Output signal `scalar` | `vector` | `matrix`

Output data from the multiply-add operation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
## Parameters
```yaml
parameters:
- name: Function
  summary: Specify function c+(a.*b) (default) | c-(a.*b) | (a.*b)-c
  group: ''
  block_parameter: Function
  type: string scalar | character vector
  values: '"c+(a.*b)" | "c-(a.*b)" |"(a.*b)-c"'
  default: '''c+(a.*b)'''
- name: Output data type
  summary: 'Specify output data type Inherit: Inherit via internal rule (default) | Inherit: Inherit via back propagation
    | Inherit: Same as first input | double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64
    | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: ''
- name: Integer rounding mode
  summary: Specify rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest
    | Zero
  group: ''
  block_parameter: RndMeth
  type: string scalar | character vector
  values: '"Ceiling" | "Convergent" |"Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: Specify whether overflows saturate Off (default) | On
  group: ''
  block_parameter: SaturateOnIntegerOverflow
  type: string scalar | character vector
  values: '"off" | "on"'
  default: '''off'''
```

### **Function** — Specify function `c+(a.*b)` (default) | `c-(a.*b)` | `(a.*b)-c`

Specify the function to perform a combined multiply and add or a multiply
and subtract operation.

#### Programmatic Use

|  |
| --- |
| **Parameter:**`Function` |
| **Type:**  string scalar | character vector |
| **Value:**`"c+(a.*b)"` | `"c-(a.*b)"` |`"(a.*b)-c"` |
| **Default:**  `'c+(a.*b)'` |

### **Output data type** — Specify output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. This parameter sets the output data type for
the addition operation. You can set the output data type to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- An expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the Data Type Assistant dialog
box, which helps you to set the **Output data type**
parameter.

For more information, see Control Data Types of Signals.

### **Integer rounding mode** — Specify rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations as either:

`Ceiling`
:   Rounds positive and negative numbers toward positive
    infinity. Equivalent to the MATLAB
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
    possible.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

#### Programmatic Use

|  |
| --- |
| **Parameter:**`RndMeth` |
| **Type:**  string scalar | character vector |
| **Value:**`"Ceiling"` | `"Convergent"` |`"Floor"` | `"Nearest"` | `"Round"` | `"Simplest"` | `"Zero"` |
| **Default:**  `'Floor'` |

#### See Also

For more information, see Rounding Modes.

### **Saturate on integer overflow** — Specify whether overflows saturate **Off** (default) | **On**

On
:   Overflows saturate to either the minimum or maximum value
    that the data type can represent.

    For example, an overflow associated with a signed 8-bit
    integer can saturate to -128 or 127.

Off
:   Overflows wrap to the
    appropriate value that the
    data type can represent.

    For example, the number 130 does not fit in a signed 8-bit
    integer and wraps to -126.

#### Tips

- Consider selecting this check box when your model has a
  possible overflow and you want explicit saturation protection in
  the generated code.
- Consider clearing this check box when you want to optimize
  efficiency of your generated code.

  Clearing this check box also helps you to avoid overspecifying
  how a block handles out-of-range signals. For more information,
  see Troubleshoot Signal Range Errors.
- When you select this check box, saturation applies to every
  internal operation on the block, not just the output or
  result.
- In general, the code generation process can detect when
  overflow is not possible. In this case, the code generator does
  not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Parameter:**`SaturateOnIntegerOverflow` |
| **Type:**  string scalar | character vector |
| **Value:**  `"off"` | `"on"` |
| **Default:**  `'off'` |
## Libraries

HDL Coder / HDL Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that
affect HDL implementation and synthesized
logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **PipelineDepth** | Number of pipeline stages. The default is `auto` which means that the code generator determines the number of pipeline stages based on your synthesis tool. For adaptive pipelines to be inserted, when **PipelineDepth** is set to `auto`, you must specify the synthesis tool and enter a target frequency value greater than zero.  You can enter an integer between 0 and 3. For Altera® hardware targets, the maximum pipeline depth is 2. |

| General | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals. |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy. |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy. |

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

- When the block has floating-point inputs, HDL Coder ignores the **PipelineDepth** parameter
  and does not insert pipeline registers.
- If the block is in a feedback loop and you do not have
  sufficient delays at the block
  output, the code generator reduces the
  **PipelineDepth** to prevent delay balancing
  failure. For sufficient delays,
  add Delay blocks at the output of the
  Multiply-Add block.
- To map the combined multiply-add operation to a DSP unit, the width of
  the third input *c* has to be less than 64 bits for
  Altera and 48 bits for Xilinx® respectively.
- The subtraction operation in the **Function** setting
  `(a.*b)-c` does not map to a DSP unit in
  Altera FPGA libraries.

## Version History

**Introduced in R2015b**

## Description

Multiply-add combined operation

The Multiply-Add block computes the product of the first two inputs, a
and b, and adds the result to the third input, c. The inputs can be vectors or
scalars.

The multiplication operation is full precision, regardless of the output type. The
**Integer rounding mode**, **Output data type**,
and **Saturate on integer overflow** settings apply only to the
addition operation. The addition operation uses the accumulator data type setting as
`Inherit : Inherit via internal rule` by default.

Use the Multiply-Add block to map a combined multiply-add or a
multiply-subtract operation to a DSP unit in your target hardware. You can select the
**Function** setting in the Block Parameters dialog box for
the Multiply-Add block.

To map to a DSP unit, specify the `SynthesisTool` property for your
model. When you generate HDL code for your model, HDL Coder™ configures the multiply-add operation so that your synthesis tool can map
to a DSP unit.

**Note**

Some DSP units do not have the multiply-add capability. To see if your hardware
has the multiply-add capability, refer to the documentation for the hardware.
