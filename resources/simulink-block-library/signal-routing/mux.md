---
type: simulink-block
title: 'Mux'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'mux'
---

# Mux

Combine input signals of same data type and complexity into virtual vector

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## Description

The Mux block combines inputs with the same data type and complexity
into a virtual vector. You can use multiple Mux blocks to create a mux signal
in stages, but the result is flat as if you used a single Mux block.

Ideally, use Mux blocks to group only function-call signals.

While a Mux block can create a virtual vector from signals that have the
same data type and complexity, other blocks group signals in ways that provide more
flexibility and efficiency.

- To group signals or messages, use a Bus Creator block instead of a Mux block. The Bus
  Creator block creates virtual buses, which give you the flexibility to group
  elements of different data types and complexity. Virtual buses also let you access
  elements by name instead of by index. If a block requires a virtual vector instead of a
  virtual bus, model compilation converts the bus to a vector.
- To concatenate input signals, use a Vector Concatenate block instead of a Mux block. The
  Vector Concatenate block creates a nonvirtual vector, which improves the
  efficiency of generated code.

For a comparison of mux signals, virtual buses, and concatenated signals, see Explore Composite Interfaces.

## Ports

### Input

### **Port\_1** — Input signal to include in mux signal scalar | vector

Input signal to include in the mux signal, specified as a scalar or
vector.

The input signals for a Mux block can be any
combination of scalars and vectors, but they must have the same data type and
complexity or be function-call signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output mux signal vector

Output mux signal composed of the combined input signals, returned as
a vector.

The elements of the output mux signal take their order from the port
order of the input signals. For a description of the port order for
various block orientations, see Identify Port Location on Rotated or Flipped Block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## Parameters

### **Number of inputs** — Number of input signals 2 (default) | scalar | vector | cell array | comma-separated list of signal names

The number of input signals, specified as a scalar, vector, cell array, or
comma-separated list of signal names. Some of these formats allow you to specify the
signal names and sizes, as described in this table.

| Format | Block Behavior |
| --- | --- |
| Scalar | The number of inputs to the Mux block.  When you use this format, the block accepts scalar or vector signals of any size. The software assigns each input the name `signalN`, where `N` is the input port number. |
| Vector | The length of the vector specifies the number of inputs. Each element specifies the size of the corresponding input.  A positive value specifies that the corresponding port can accept only vectors of that size. For example, `[2 3]` specifies two input ports of sizes `2` and `3`, respectively. If an input signal width does not match the expected width, an error message appears. A value of `-1` specifies that the corresponding port can accept scalars or vectors of any size. |
| Cell array | The length of the cell array specifies the number of inputs. The value of each cell specifies the size of the corresponding input.  A scalar value `N` specifies a vector of size `N`. A value of `-1` means that the corresponding port can accept scalar or vector signals of any size. |
| Comma-separated list of signal names | A list of signal names separated by commas. The software assigns each name to the corresponding port and signal. For example, if you enter `position,velocity`, the Mux block has two inputs, named `position` and `velocity`. |

Specifying
a nondouble value, such as `single(3)`, is not
supported.

#### Tips

If you specify a scalar for the **Number of inputs** parameter
and all of the input ports are connected, as you draw a new signal line close to input
side of a Mux block, the software adds a port and updates the
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Inputs` |
| **Values:** | `'2'` (default) | scalar in quotes | vector in quotes | cell array in quotes | comma-separated list of signal names in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'Inputs','5')`

**Example:** `set_param(gcb,'Inputs','[2 3]')`

**Example:** `set_param(gcb,'Inputs','{3}')`

**Example:** `set_param(gcb,'Inputs','position,velocity')`

### **Display option** — Block icon appearance `bar` (default) | `signals` | `none`

Block icon appearance, specified as `bar`,
`signals`, or `none`.

- `bar` — Displays no text
- `signals` — Displays the input signal names
- `none` — Displays the type of block
  (Mux)

Resize the block as necessary to fit the text on the block icon.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DisplayOption` |
| **Values:** | `'bar'` (default) | `'signals'` | `'none'` |

**Example:** `set_param(gcb,'DisplayOption','signals')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

To improve the efficiency of generated code, use a Vector
Concatenate block instead of a Mux block. The Vector
Concatenate block creates a nonvirtual vector.

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

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

Buses are not supported for HDL code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced before R2006a**
