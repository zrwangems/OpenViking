---
type: simulink-block
title: 'Signal Conversion'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalconversion'
language: en
---

# Signal Conversion

## Ports

### Input

### **Port\_1** — Input signal to convert scalar | vector | matrix | array | bus

The input signal is a scalar, vector, matrix, array, or bus that this block converts to
another type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Converted signal scalar | vector | matrix | array | bus

The output signal is the input signal converted to the specified type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Output** — Type of conversion `Signal copy` | `Virtual bus` | `Nonvirtual bus`

Specify the type of conversion to perform.

- `Signal copy` — Create a contiguous copy of the input
  signal. This value is the default value for the Signal Conversion and
  Signal Copy blocks.
- `Virtual bus` — Convert a nonvirtual bus to a virtual
  bus. This value is the default value for the To Virtual Bus
  block.
- `Nonvirtual bus` — Convert a virtual bus to a
  nonvirtual bus. This value is the default value for the To Nonvirtual
  Bus block.

For the `Signal copy` option, the type of input determines how
the block makes the copy.

For example, suppose the block receives a mux signal, which has elements that occupy
discontiguous areas of memory. The conversion allocates a contiguous area of memory for
the elements of the mux signal and copies the values from the discontiguous areas
represented by the block input to the contiguous areas represented by the block output
at each time step. The output is a vector with elements that occupy contiguous areas of
memory.

The type of conversion that you use depends on your modeling goal.

| Modeling Goal | Option |
| --- | --- |
| Reduce generated code for a muxed signal.  For an example involving Simulink Coder™ software, see Generate Reentrant Code from Subsystems (Simulink Coder). | `Signal copy` |
| Connect a block with a constant sample time to an output port of an enabled subsystem. | `Signal copy` |
| Save memory by converting a nonvirtual bus to a virtual bus. | `Virtual bus` |
| Pass a virtual bus to a modeling construct that requires a nonvirtual bus. | `Nonvirtual bus` |
| Create a copy of an array of buses.  The block cannot convert an array of buses to a nonvirtual or virtual bus. To extract a bus from an array of buses, use a Selector block. | `Signal copy` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ConversionOutput` |
| **Values:** | `'Signal copy'` (default) | `'Virtual bus'` | `'Nonvirtual bus'` |

**Example:** `set_param(gcb,'ConversionOutput','Virtual
bus')`

### **Data type** — Nonvirtual bus data type `Inherit: auto` (default) | `Bus: <object name>` | `<data type expression>`

Specify the output data type of the nonvirtual bus that this block
produces.

- `Inherit: auto` — Inherit the data type from an
  upstream block. For example, inherit the `Simulink.Bus` object
  data type from an upstream Bus Creator
  block.
- `Bus: <object name>` or `<data type
  expression>` — Specify a `Simulink.Bus`
  object that matches the hierarchy of the input bus. If an upstream
  Bus Creator block specifies a bus object, specify
  the same bus object.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Output** to `Nonvirtual
bus`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: auto'` (default) | `'Bus: <object name>'` | `'<data type expression>'` |

**Example:** `set_param(gcb,'OutDataTypeStr','Bus:
myBusObj')`

### **Exclude this block from 'Block reduction' optimization** — Option to exclude block from block reduction optimization `off` (default) | `on`

When the elements of the input signal occupy contiguous areas of memory, by default,
the software eliminates this block from the compiled model as an optimization. For more
information, see Block reduction.

To prevent this block from being eliminated from the compiled model, select this
parameter.

Changes to this parameter take effect the next time you compile the model.

#### Dependencies

To enable this parameter, set **Output**
to `Signal copy`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OverrideOpt` |
| **Values:** | `'off'` (default) | `'on'` |

**Example:** `set_param(gcb,'OverrideOpt','on')`

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has a pass-through implementation.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Convert signal to new type without altering signal values

The Signal Conversion block converts a signal from one type to another. To
select the type of conversion to perform, use the **Output**
parameter or one of the preconfigured Signal Conversion blocks:

- Signal Copy block
- To Virtual Bus block
- To Nonvirtual Bus block
