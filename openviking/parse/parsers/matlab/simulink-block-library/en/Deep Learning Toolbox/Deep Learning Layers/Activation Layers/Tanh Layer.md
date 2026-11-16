---
type: simulink-block
title: 'Tanh Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'tanhlayer'
documentation_source_path: 'ref/tanhlayer.html'
language: en
---

# Tanh Layer

## Ports

### Input

### **Port\_1** — Input data scalar | vector | matrix

The matrix on which to perform the hyperbolic tangent operation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output data scalar | vector | matrix

The result of performing the hyperbolic tangent operation on the input
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Data Types

### **Approximation method** — Approximation method for computing layer output `None` (default) | `CORDIC` | `Lookup`

Specify the type of approximation for computing the output.

| Approximation Method | Data Types Supported | When to Use This Method |
| --- | --- | --- |
| `None` (default) | Floating point | You are processing only floating point data. |
| `CORDIC` | Floating point (double and single) and fixed point with a **Bias** value of `0` and a **Slope** value of a power of 2 | You are processing fixed point data and want to deploy to FPGA hardware. |
| `Lookup` | Floating point and fixed point | You are processing fixed point data and want to generate C/C++ code. |

For more information about the CORDIC approximation method, see `cordictanh` (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApproximationMethod` |
| **Type:** character vector |
| **Values:** `'none'` | `'CORDIC'` | `'Lookup'` |
| **Default:** `'none'` |

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

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Hyperbolic tangent (tanh) layer

The Tanh Layer block applies the tanh function to layer inputs.

The `exportNetworkToSimulink` function generates this block to represent a `tanhLayer` object.
Because it applies an element-wise operation, this block supports input data of any format and
outputs data that has the same dimensions and format as the input.
