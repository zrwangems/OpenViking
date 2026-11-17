---
type: simulink-block
title: 'Concatenation Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Combination Layers'
documentation_page: 'concatenationlayer'
documentation_source_path: 'ref/concatenationlayer.html'
language: en
---

# Concatenation Layer

## Ports
```yaml
ports:
- name: Port_1
  summary: First input data array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: Second input data scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_N
  summary: '*N*th input data scalar | vector | matrix'
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Concatenated output data array
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — First input data array

First input to concatenate, provided as an array that follows the format that you
specify with the **Data format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — Second input data scalar | vector | matrix

Second input to concatenate, provided as an array that follows the format that you
specify with the **Data format** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — *N*th input data scalar | vector | matrix

*N*th input to concatenate, provided as an array that follows the
format that you specify with the **Data format** parameter. The
block has a number of input ports equal to the value of the
`NumInputs` property of the object that you specify with the
**Layer** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Concatenated output data array

Concatenated output data. The output data has dimensions corresponding to the
format that you specify with the **Data format** block
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Layer
  summary: Corresponding layer object layerObject (default) | concatenationLayer object
  group: Main
  block_parameter: Layer
  type: workspace variable
  values: concatenationLayer object
  default: '''layerObject'''
- name: Data format
  summary: Format of input data SSC (default) | C | CT | SC | SSSC
  group: Main
  block_parameter: DataFormat
  type: character vector
  values: '''SSC'' | ''C'' | ''CT'' | ''SC'' | ''SSSC'''
  default: '''SSC'''
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

### **Layer** — Corresponding layer object `layerObject` (default) | `concatenationLayer` object

Specify the name of a workspace variable that contains a
`concatenationLayer` object from a trained network. The
Concatenation Layer block configures itself by using the properties
of the object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layer` |
| **Type:** workspace variable |
| **Values:** `concatenationLayer` object |
| **Default:** `'layerObject'` |

### **Data format** — Format of input data `SSC` (default) | `C` | `CT` | `SC` | `SSSC`

Data format for the input data. The options use the same
notation as the `fmt` argument of the
`dlarray` object, except layer blocks do not support the Batch
(`B`) dimension and instead assume an observation number of
`1`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataFormat` |
| **Type:** character vector |
| **Values:** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **Default:** `'SSC'` |

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

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: **Layer** parameter default value is `'layerObject'`

Starting in R2025a, the default value for the **Layer** parameter is `'layerObject'`. In previous versions, the default value is `'layer'`. If you have code that programmatically creates Simulink and relies on variables with the name `'layer'`, update your code so that the variable has the name `'layerObject'`.

## Description

Concatenation layer

The Concatenation Layer block takes inputs and concatenates them along a
specified dimension. The inputs must have the same size in all dimensions except the
concatenation dimension. This block accepts data that has dimensions corresponding to the
format that you specify with the **Data format** block parameter.

The `exportNetworkToSimulink` function generates this block to represent a `concatenationLayer`
object.
