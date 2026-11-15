---
type: simulink-block
title: 'Dead Zone'
family: discontinuities
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'deadzone'
language: en
---

# Dead Zone

Provide region of zero output

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Description

The Dead Zone block generates zero output within a specified region,
called its dead zone. You specify the lower limit (`LL`) and upper
limit (`UL`) of the dead zone as the **Start of dead
zone** and **End of dead zone** parameters. The block
output depends on the input (`U`) and the values for the lower and
upper limits.

| Input | Output |
| --- | --- |
| `U >= LL` and `U <= UL` | Zero |
| `U > UL` | `U` – `UL` |
| `U < LL` | `U` – `LL` |

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal to the dead-zone algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal after the dead-zone algorithm is applied to the input
signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Start of dead zone** — Specify the lower bound of the dead zone `'-0.5'` (default) | scalar | vector

Specify dead zone lower limit. Set the value for **Start of dead
zone** less than or equal to **End of dead
zone**. When the input value is less than **Start of
dead zone**, then the block shifts the output value down by the
**Start of dead zone** value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LowerValue` |
| **Type**: character vector |
| **Value**: scalar or vector less than or equal to `UpperValue`. |
| **Default**: `'-0.5'` |

### **End of dead zone** — Specify the upper limit of the dead zone `'0.5'` (default) | scalar | vector

Specify dead zone upper limit. Set the value for **End of dead
zone** greater than or equal to **Start of dead
zone**. When the input value is greater than **End of
dead zone**, then the block shifts the output value down by the
**End of dead zone** value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UpperValue` |
| **Type**: character vector |
| **Value**: scalar or vector greater than or equal to `LowerValue`. |
| **Default**: `'0.5'` |

### **Saturate on integer overflow** — Method of overflow action `on` (default) | `off`

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
| **Values:** | `'on'` (default) | `'off'` |

### **Treat as gain when linearizing** — Specify the gain value `on` (default) | `off`

The linearization commands in Simulink® software treat this block as a gain in state space. Select this parameter
to cause the commands to treat the gain as 1. Clear this parameter to have the commands
treat the gain as 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearizeAsGain` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
