---
type: simulink-block
title: 'Sqrt'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / HDL Math Library'
documentation_page: 'sqrt'
documentation_source_path: 'ref/sqrt.html'
language: en
---

# Sqrt

## Ports

### Input

### **dataIn** — Input data signal scalar | vector

Input signal to calculate the square root, specified as a scalar or vector.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validIn** — Whether input control signal is valid scalar

Input control signal that indicates whether the input signal is valid, specified
as a scalar.

**Data Types:** `Boolean`
### Output

### **dataOut** — Output data signal scalar | vector

Output signal that is the square root of the input signal, returned as a scalar or
vector.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validOut** — Whether output control signal is valid scalar

Output control signal that indicates whether output signal is valid, returned as a
scalar.

**Data Types:** `Boolean`

## Parameters

### **Latency strategy** — Latency strategy `Max` (default) | `Min` | `Custom` | `Custom(PerIteration)` | `Zero`

Specify whether to use minimum, maximum, custom, or zero latency. For more information,
see Latency Strategy.

To use custom latency for the block, set the **Latency strategy** to
`Custom` and enter the latency value in the **Custom
latency** field.

You can also control the number of pipeline stages
for the iterative algorithm. To customize the latency for iterative algorithm, set the
**Latency strategy** to `Custom(PerIteration)` and
enter the iterations per pipeline value in the **IterationsPerPipeline**
field. *(since R2025a)*

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `latencyMode` |
| **Type**: character vector |
| **Values**: `'Max'` | `'Min'` | `'Custom'` | `'Custom(PerIteration)'` | `'Zero'` |
| **Default**: `'Max'` |

### **Custom latency** — Custom latency 0 (default) | `positive integer`

Specify the custom latency value. The latency must be a nonnegative integer in the
range [0, *L*], where *L* is the maximum latency value
of Sqrt block. For more information, see CustomLatency.

#### Dependency

To use this parameter, set **Latency strategy** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `customLatencyValue` |
| **Type**: Integer |
| **Values**: `0 to Max latency` |
| **Default**: `0` |

### **IterationsPerPipeline** — Iterations per pipeline `1` (default) | `positive integer`

*Since R2025a*

Specify the iterations to use per each pipeline stage in the algorithm.

#### Dependency

To enable this parameter, set **Latency strategy** to
`Custom(PerIteration)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `iterationsPerPipelineValue` |
| **Type**: Integer |
| **Values**: `Positive integer` |
| **Default**: `1` |

### **Output data type** — Output data type `Inherit: Same as first input` (default) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. The data type can be inherited or specified directly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Same as first input'` |

### **Saturate on integer overflow** — Option to choose behavior when integer overflow occurs `off` (default) | `on`

| Action | Reasons for Taking This Action | What Happens for Overflows | Example |
| --- | --- | --- | --- |
| **Saturate on integer workflow** parameter is `on` | Your model has possible overflow, and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box selected, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of -128. |
| **Saturate on integer workflow** parameter is `off` | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Overflows wrap to the value that is representable by the data type. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box cleared, the software interprets the overflow-causing value as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8`, is -126. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
|  |
| **Default**: `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Zero` (default) | `Ceiling` | `Floor` | `Nearest` | `Simplest`

Specify the rounding mode for fixed-point operations. For more information,
see Rounding Modes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Zero' | 'Ceiling' | 'Floor' | 'Nearest' | 'Simplest'` |
| **Default:** `'Zero'` |

## Libraries

HDL Coder

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

The block supports HDL code generation using HDL Coder™. HDL Coder provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining. |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays. |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining. |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining. |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle. |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing. |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming. |

**Target Specification**

This block cannot be the DUT, so the block property settings in the **Target
Specification** tab are ignored.

**Limitations**

- You cannot use this block in a Synchronous Subsystem block.
- The block does not support resource sharing optimization.

## Version History

**Introduced in R2020b**

### R2025a: Control number of pipeline stages per iteration

You can control the pipeline stages for iterative algorithms by setting the
**LatencyStrategy** parameter HDL to
`Custom(PerIterations)`, then specifying the number of pipeline
stages per iteration by using the **IterationsPerPipeline** parameter. Use
this setting to control the pipeline stages in the generated code and optimize the design
for speed and resource utilization.

## Description

Compute Sqrt operation and simulate with latency

HDL Math Sqrt Block

The Sqrt block performs square root operation of the input data signal. The
block has control signals that indicate whether the input and output data are valid. You can
also specify the number of iterations of the algorithm and the latency strategy.

To use this block in your Simulink® model, open the `HDLMathLib` library by entering this command
in the MATLAB® Command
Window:

```
open_system("HDLMathLib")
```

You
can simulate the block with latency. For more information, see Latency Considerations.
