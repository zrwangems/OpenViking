---
type: simulink-block
title: 'Cos+jSin'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'cosjsin'
documentation_source_path: '../hdlcoder/ref/cosjsin.html'
language: en
---

# Cos+jSin

## Ports
```yaml
ports:
- name: dataIn
  summary: Input data signal scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point | bus
- name: validIn
  summary: Whether input control signal is valid scalar
  direction: input
  data_types: Boolean
- name: cos+jsinOut
  summary: Output data signal scalar | vector
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point | bus
- name: validOut
  summary: Whether output control signal is valid scalar
  direction: output
  data_types: Boolean
```

### Input

### **dataIn** — Input data signal scalar | vector

Input data signal to compute `Cos+jSin` function, specified as a
scalar or vector. The input value ranges from -2π to 2\*π.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validIn** — Whether input control signal is valid scalar

Input control signal that indicates whether the input signal is valid, specified
as a scalar.

**Data Types:** `Boolean`
### Output

### **cos+jsinOut** — Output data signal scalar | vector

Output data signal that is the `Cos+jSin` of the input signal,
returned as a scalar or vector.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validOut** — Whether output control signal is valid scalar

Output control signal that indicates whether output signal is valid, returned as a
scalar.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Number of iterations
  summary: Number of iterations for CORDIC algorithm 11 (default) | positive integer
  group: ''
  block_parameter: iter
  type: character vector
  values: Integer values
  default: '''11'''
- name: Latency strategy
  summary: Latency strategy Max (default) | Min | Custom | Custom(PerIteration) | Zero
  group: ''
  block_parameter: latencyMode
  type: character vector
  values: '''Max'' | ''Min'' | ''Custom'' | ''Custom(PerIteration)'' | ''Zero'''
  default: '''Max'''
- name: Custom latency
  summary: Custom latency value 0 (default) | positive integer
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
```

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | `positive integer`

Specify the number of iterations for CORDIC algorithm.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `iter` |
| **Type**: character vector |
| **Values**: `Integer values` |
| **Default**: `'11'` |

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

### **Custom latency** — Custom latency value 0 (default) | `positive integer`

Specify the custom latency value. The latency must be a nonnegative integer in the
range [0, *L*], where *L* is the maximum latency value
of `Cos+jSin` block. For more information, see CustomLatency.

#### Dependency

To enable this parameter, set **Latency strategy** to
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

You can use a new custom latency setting that enables you to control the pipeline stages
for iterative algorithms. Set the **LatencyStrategy** HDL block property to
`Custom(PerIterations)`, then specify the number of pipeline
stages per iteration using the **IterationsPerPipeline** parameter. Use the
new setting to control the pipeline stages in the generated code and optimize the design for
speed and resource utilization.

## Description

Compute Cos+jSin operation using CORDIC approximation method and simulate with latency

The Cos+jSin block computes the complex exponential of the input signal by
using the coordinate rotation digital computer (CORDIC) approximation method. For more
information, see CORDIC approximation method in Algorithms. The block has control
signals that indicate whether the input and output data are valid. You can also specify the
number of iterations of the algorithm and the latency strategy.

To use this block in your Simulink® model, open the `HDLMathLib` library by entering this command
in the MATLAB® Command
Window:

```
open_system('HDLMathLib')
```

You
can simulate the SinCos block with latency. For more information, Latency Considerations.
