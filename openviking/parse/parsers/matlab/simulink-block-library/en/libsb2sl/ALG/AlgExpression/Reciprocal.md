---
type: simulink-block
title: 'Reciprocal'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'ALG / AlgExpression'
documentation_page: 'reciprocal'
documentation_source_path: '../hdlcoder/ref/reciprocal.html'
language: en
---

# Reciprocal

## Ports
```yaml
ports:
- name: dataIn
  summary: Data input signal scalar
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: validIn
  summary: Whether input control signal is valid scalar
  direction: input
  data_types: Boolean
- name: dataOut
  summary: Output data signal scalar
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: validOut
  summary: Whether output control signal is valid scalar
  direction: output
  data_types: Boolean
```

### Input

### **dataIn** — Data input signal scalar

Data input to calculate the reciprocal, specified as a scalar.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **validIn** — Whether input control signal is valid scalar

Input control signal that indicates whether the input signal is valid, specified
as a scalar.

**Data Types:** `Boolean`
### Output

### **dataOut** — Output data signal scalar

Output signal that is the reciprocal of the input signal, returned as a
scalar.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **validOut** — Whether output control signal is valid scalar

Output control signal that indicates whether output signal is valid, returned as a
scalar.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Latency strategy
  summary: Latency strategy Max (default) | Min | Custom | Custom(PerIteration) | Zero
  group: ''
  block_parameter: latencyMode
  type: character vector
  values: '''Max'' | ''Min'' | ''Custom'' | ''Custom(PerIteration)'' | ''Zero'''
  default: '''Max'''
- name: Custom latency
  summary: Custom latency 0 (default)
  group: ''
  block_parameter: customLatencyValue
  type: Integer
  values: 0 to Max latency
  default: '0'
- name: IterationsPerPipeline
  summary: Iterations per pipeline 1 (default) | positive integer
  group: ''
  block_parameter: iterationsPerPipelineValue
  type: Integer
  values: Positive integer
  default: '1'
- name: Output data type
  summary: 'Output data type Inherit: Inherit via internal rule (default) | Inherit: Same as first input | Inherit: Inherit
    via back propagation | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) |
    <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Inherit via back propagation'' | ''Inherit: Same as first input''
    | ''int8'' | ''uint8'' | int16 | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | fixdt(1,16,0) | ''<data
    type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Zero (default) | Ceiling | Convergent | Floor | Nearest | Round | Simplest
  group: ''
  block_parameter: RndMeth
  type: character vector
  values: '''Zero'' | ''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''ROund'' | ''Simplest'''
  default: '''Zero'''
```

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

### **Custom latency** — Custom latency 0 (default)

Specify the custom latency value. The latency must be a nonnegative integer in the
range [0, *L*], where *L* is the maximum latency value
of Reciprocal block. For more information, see CustomLatency.

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

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type. The data type can be inherited or specified directly.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Zero` (default) | `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Simplest`

Specify the rounding mode for fixed-point operations. For more information,
see Rounding Modes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Zero' | 'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'ROund' | 'Simplest'` |
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

- You cannot use this block in the Synchronous Subsystem.
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

Compute reciprocal operation and simulate with latency

The Reciprocal block performs the reciprocal operation on the input data
signal. The block has control signals that indicate whether the input and output data are
valid. You can also specify the number of iterations of the algorithm and the latency
strategy.

To use this block in your Simulink® model, open the `HDLMathLib` library by entering this command
in the MATLAB® Command
Window:

```
open_system("HDLMathLib")
```

You
can simulate the block with latency. For more information, see Latency Considerations.
