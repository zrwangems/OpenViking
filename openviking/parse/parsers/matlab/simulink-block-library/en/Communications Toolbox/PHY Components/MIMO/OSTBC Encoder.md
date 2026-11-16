---
type: simulink-block
title: 'OSTBC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / MIMO'
documentation_page: 'ostbcencoder'
documentation_source_path: 'ref/ostbcencoder.html'
language: en
---

# OSTBC Encoder

## Ports

### Input

### **In** — Input data column vector | matrix

Input data, specified as a column vector or matrix of values with
power-of-two slope and zero bias. For more information, see Input-to-Output Dimensions.

This port is unnamed on the block icon.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Out** — Output data matrix | 3-D array

Output data, returned as a matrix or 3-D array. For more information,
see Input-to-Output Dimensions.

The output signal inherits the data type from the input signal. For
fixed-point signals, the **Saturate on integer overflow** parameter specifies how
the block handles integer overflows due to complex conjugation.

This port is unnamed on the block icon.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Number of transmit antennas** — Number of transmit antennas `2` (default) | `3` | `4`

Number of transmit antennas, specified as `2`,
`3`, or `4`.

### **Rate** — Symbol rate `3/4` (default) | `1/2`

Symbol rate of the code, specified as `3/4` or
`1/2`. When you set **Number of
transmit antennas** to `2`, the symbol rate
is `1`.

#### Dependencies

To enable this parameter, set **Number of transmit
antennas** to `3` or
`4`.

#### Data Types

### **Saturate on integer overflow** — Option to saturate on integer overflow off (default) | on

For fixed-point calculations, use this parameter to specify the method to
be used if the magnitude of a fixed-point calculation result does not fit
into the range of the data type and scaling that stores the result.

- To saturate on integer overflow, select this parameter.
- To wrap on integer overflow, do not select this
  parameter.

For more information, see Precision and Range.

**Data Types:** `Boolean`

## Libraries

Communications Toolbox / MIMO

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Signed only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Encode input message using orthogonal space-time block code

The OSTBC Encoder block encodes an input symbol sequence using an
orthogonal space-time block code (OSTBC). The block maps the input symbols block-wise
and concatenates the output codeword matrices in the time domain. For more information,
see OSTBC Encoding Algorithm.
