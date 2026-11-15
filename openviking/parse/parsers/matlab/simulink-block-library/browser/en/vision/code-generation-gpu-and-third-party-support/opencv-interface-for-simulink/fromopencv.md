---
type: simulink-block
title: 'FromOpenCV'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'fromopencv'
documentation_source_path: 'ref/fromopencv.html'
language: en
---

# FromOpenCV

## Ports

### Inputs

### **Port\_1** — First input signal scalar | vector | matrix | simulink bus | simulink image

Input signal to the FromOpenCV block. The input can be
of different data types. Each of the input data types determines the
output data type of the block. For more information, see Mapping Input and
Output Data Types.

**Data Types:** `OpenCV types`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | simulink bus | simulink image

Output signal from the FromOpenCV block.

**Data Types:** `Converted Simulink types`

## Parameters

### **DataType** — Data type of the Input signal of FromOpenCV block `input data type` (default)

Specifies the input data type of the FromOpenCV block. The
table lists the
one-to-one mapping of the input versus output data types of the
FromOpenCV block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector |
| **Value:** input data type |
| **Default:** `'Point2i'` |

## Libraries

Computer Vision Toolbox Interface for OpenCV in Simulink

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `Yes` |
| **Multidimensional Signals** | `Yes` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports C++ code generation.

## Version History

**Introduced in R2020a**

## Description

Converts OpenCV data types to Simulink data types

The FromOpenCV block converts the Simulink® OpenCV data types to Simulink data types.
