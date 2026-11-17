---
type: simulink-block
title: 'Difference'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'difference'
documentation_source_path: 'slref/difference.html'
language: en
---

# Difference

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix | N-D array
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Current input minus previous input scalar | vector | matrix | N-D array
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

#### Dependencies

When you set **Input processing** to
`Columns as channels (frame based)`,
the input signal must have two dimensions or less.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Current input minus previous input scalar | vector | matrix | N-D array

Current input minus previous input, specified as a scalar, vector, matrix, or N-D
array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Initial condition for previous input
  summary: Initial condition 0.0 (default) | scalar | vector | matrix | N-D array
  group: Main
  block_parameter: ICPrevInput
  type: character vector
  values: scalar | vector | matrix | N-D array
  default: '''0.0'''
- name: Input processing
  summary: Specify sample- or frame-based processing Elements as channels (sample based) (default) | Columns as channels (frame
    based)
  group: Main
  block_parameter: InputProcessing
  type: character vector
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
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
  summary: 'Output data type Inherit: Inherit via internal rule (default) | Inherit via back propagation | double | single
    | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0) |
    <data type expression>'
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Inherit via back propagation'' | ''double'' | ''single'' |
    ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)''
    | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Option to prevent fixed-point tools from overriding Output data type off (default) | on
  group: Signal Attributes
  block_parameter: LockScale
  values: '''off'' (default) | ''on'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Signal Attributes
  block_parameter: RndMeth
  values: '''Floor'' (default) | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate to max or min when overflows occur
  summary: Method of overflow action off (default) | on
  group: Signal Attributes
  block_parameter: DoSatur
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### Main

### **Initial condition for previous input** — Initial condition `0.0` (default) | scalar | vector | matrix | N-D array

Set the initial condition for the previous input.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ICPrevInput` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'0.0'` |

### **Input processing** — Specify sample- or frame-based processing `Elements as channels (sample based)` (default) | `Columns as channels (frame based)`

Specify whether the block performs sample- or frame-based processing:

- `Columns as channels (frame based)` — Treat
  each column of the input as a separate channel (frame-based processing).

  **Note**

  Frame-based processing requires a DSP System Toolbox™ license.

  For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).
- `Elements as channels (sample based)` — Treat
  each element of the input as a separate channel (sample-based
  processing).

Use **Input processing** to specify whether the block performs
sample- or frame-based processing. For more information about these two processing
modes, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputProcessing` |
| **Type**: character vector |
| **Values**: `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **Default**: `'Elements as channels (sample based)'` |

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

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

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
| **Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

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

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |
## Libraries

Simulink / Discrete

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block is not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- The code generator does not explicitly group primitive blocks that
  constitute a nonatomic masked subsystem block in the generated code. This
  flexibility allows for more efficient code generation. In certain cases, you
  can achieve grouping by configuring the masked subsystem block to execute as
  an atomic unit by selecting the Treat as atomic unit option.

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

## Description

Calculate change in signal over one time step

The Difference block outputs the current input value minus the previous input
value.
