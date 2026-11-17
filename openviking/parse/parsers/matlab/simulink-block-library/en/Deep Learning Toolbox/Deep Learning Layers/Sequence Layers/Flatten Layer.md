---
type: simulink-block
title: 'Flatten Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Sequence Layers'
documentation_page: 'flattenlayer'
documentation_source_path: 'ref/flattenlayer.html'
language: en
---

# Flatten Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: Input data array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Flattened output data array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input data array

Input data to flatten.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Flattened output data array

Flattened output data. The output data collapses the spatial dimensions of the
input data into the channel dimension.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Flattened output size
  summary: Size of flattened output matrix [1 1 1] (default) | array of positive scalars
  group: Main
  block_parameter: FlattenedOutputSize
  type: array
  values: '[1 1 1] | ''<array>'''
  default: '''[1 1 1]'''
- name: Sample time
  summary: Option to specify sample time -1 (default) | scalar
  group: Execution
  block_parameter: SampleTime
  values: '''-1'' (default) | scalar'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Flattened output size** — Size of flattened output matrix `[1 1 1]` (default) | array of positive scalars

Size of the flattened output matrix, specified as an array of positive scalars. To
determine the activation output of a `flattenLayer` object, you can use
the `analyzeNetwork` function and ignore the batch (`B`)
dimension.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `FlattenedOutputSize` |
| **Type:** array |
| **Values:** `[1 1 1]` | `'<array>'` |
| **Default:**  `'[1 1 1]'` |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### Execution

### **Sample time** — Option to specify sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample time, such as continuous (`0`) or inherited (`-1`). For more options, see Types of Sample Time (Simulink).

By default, the block inherits its sample time based on the context of the block within the
model.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` (Simulink) function.

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **Values:** `'-1'` (default) | scalar |
## Libraries

Deep Learning Toolbox / Deep Learning Layers / Sequence Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Flatten layer

The Flatten Layer block collapses the spatial dimensions of layer input
into the channel dimension.

For example, if the input to the layer is an
*H*-by-*W*-by-*C*-by-*N*-by-*S*
array (sequences of images), then the flattened output is an
(*H*\**W*\**C*)-by-*N*-by-*S*
array.

The `exportNetworkToSimulink` function generates this block to represent a `flattenLayer` object.
