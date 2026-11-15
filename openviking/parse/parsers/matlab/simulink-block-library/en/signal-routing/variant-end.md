---
type: simulink-block
title: 'Variant End'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantend'
language: en
---

# Variant End

## Ports

### Input

### **Port\_1** — Input branch scalar | vector | matrix

Input branch that defines the end of the bounded region with the
corresponding Variant Start block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — Input port associated with *N*th branch scalar | vector | matrix

Input port associated with the *N*th branch that defines
the end of the bounded region with the corresponding Variant
Start block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal from the active variant.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Variant Start End Tag** — Unique identifier of bounded region `A` (default) | valid MATLAB® identifier

Unique identifier to identify the correct Variant Start and
Variant End pair that form the bounded region, specified as a
valid MATLAB identifier. A valid MATLAB identifier is a character vector of alphanumerics (A–Z, a–z, 0–9)
and underscores, such that the first character is a letter and the length of the
character vector is less than or equal to `namelengthmax`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantStartEndTag` |
| **Type:** character vector |
| **Values:** `'A'` | valid MATLAB identifier |
| **Default:** `'A'` |

### **Variant Paired Block** — Option to highlight paired Variant Start block `off` (default) | `on`

Select this parameter to highlight the Variant Start with the
same **Variant Start End Tag** as the Variant End.
If there are multiple Variant Start blocks with the same
**Variant Start End Tag**, then the first block found is
highlighted.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantPairedBlock` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024a**

## Description

Define end of bounded region

The Variant End block defines the end of the bounded region that allows
you to limit variant condition propagation without introducing a level of hierarchy. Define
the start of the bounded region by using the Variant Start block. For every
Variant Start block, there is a single corresponding Variant
End block. When you specify the variant conditions on the Variant
Start block, the corresponding Variant End block inherits the
conditions and other parameters based on the unique **Variant Start End
Tag** on compile.
