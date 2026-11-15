---
type: simulink-block
title: 'Saturation'
family: discontinuities
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'saturation'
language: en
---

# Saturation

Limit input signal to the upper and lower saturation values

## Libraries

Simulink / Commonly Used Blocks Simulink / Discontinuities HDL Coder / Discontinuities

## Description

The Saturation block produces an output signal that is the value of the input signal bounded
to the upper and lower saturation values. The upper and lower limits are specified by
the parameters **Upper limit** and **Lower
limit**.

| Input | Output |
| --- | --- |
| Lower limit ≤ Input value ≤ Upper limit | Input value |
| Input value < Lower limit | Lower limit |
| Input value > Upper limit | Upper limit |

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

The input signal to the saturation algorithm.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal that is the value of the input signal, upper saturation
limit, or lower saturation limit.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Upper limit** — Upper saturation boundary for the input signal `0.5` (default) | scalar | vector

Specify the upper bound on the input signal. If the input signal is
greater than this boundary, then the output signal is set to this
saturation value. The **Upper limit** parameter is
converted to the output data type using round-to-nearest and saturation.
**Upper limit** must be greater than the
**Output minimum** parameter and less than the
**Output maximum** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UpperLimit` |
| **Type**: character vector |
| **Value**: real scalar or vector |
| **Default**: `'0.5'` |

### **Lower limit** — Lower saturation boundary for the input signal `-0.5` (default) | scalar | vector

Specify the lower bound on the input signal. If the input signal is less than this
boundary, then the output signal is set to this saturation value. The
**Lower limit** parameter is converted to the
output data type using round-to-nearest and saturation. **Lower
limit** must be greater than the **Output
minimum** parameter and less than the **Output
maximum** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LowerLimit` |
| **Type**: character vector |
| **Value**: real scalar or vector |
| **Default**: `'-0.5'` |

### **Treat as gain when linearizing** — Specify the gain value `on` (default) | `off`

Select this parameter to cause the commands to treat the gain as 1. The linearization
commands in Simulink® software treat this block as a gain in state space. Clear this parameter
to have the commands treat the gain as 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearizeAsGain` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
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

### **Output data type** — Specify the output data type `Inherit: Same as input` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as a
`Simulink.NumericType` object. For more information,
see Control Data Types of Signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Same as input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
