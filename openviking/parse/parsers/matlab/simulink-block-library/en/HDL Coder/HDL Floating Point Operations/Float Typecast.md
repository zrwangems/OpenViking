---
type: simulink-block
title: 'Float Typecast'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'floattypecast'
documentation_source_path: 'ref/floattypecast.html'
language: en
---

# Float Typecast

## Ports
```yaml
ports:
- name: Port_1(u)
  summary: Input signal scalar | vector
  direction: input
  data_types: singledouble | uint32 | fixed point
- name: Port_1(y)
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double | uint32 | fixed point
```

### Input

### **Port\_1(u)** — Input signal `scalar` | `vector`

Port to provide input to the block.

**Data Types:** `singledouble` | `uint32` | `fixed point`
### Output

### **Port\_1(y)** — Output signal `scalar` | `vector`

Port to obtain calculated output from the block.

**Data Types:** `single` | `double` | `uint32` | `fixed point`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

HDL Coder / HDL Floating Point Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

The block supports HDL code generation in the `Native Floating
Point` mode. To use this mode, specify `single` or
`uint32` data types as input to the block. With the HDL Code
Advisor, you can replace Data Type Conversion blocks that use the
`Stored Integer (SI)` mode and convert between
floating-point and fixed-point data types.

The block supports code generation for complex signals.

## Version History

**Introduced in R2017b**

## Description

Typecast a floating-point type to an unsigned integer or vice versa

The block casts the underlying bits of the input to the corresponding fixed-point or
floating point representation. The input and output of the block contain the same number
of bits.

| Input Data Type | Output Data Type |
| --- | --- |
| `half` | `uint16` |
| `single` | `uint32` |
| `double` | `uint64` |
| `uint32` | `single` |
| `uint64` | `double` |
| `uint16` | `half` |

This figure shows how the block mask, behavior, and output data type
changes dynamically depending on the input data type that you specify.

Shows how the output data types vary in response to changes in the input data type.
