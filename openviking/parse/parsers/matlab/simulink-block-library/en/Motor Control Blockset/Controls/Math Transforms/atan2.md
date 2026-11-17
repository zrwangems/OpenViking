---
type: simulink-block
title: 'atan2'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'atan2'
documentation_source_path: 'ref/atan2.html'
language: en
---

# atan2

## Ports
```yaml
ports:
- name: A
  summary: y-coordinate value (real number) scalar
  direction: input
  data_types: single | double | fixed point
- name: B
  summary: x-coordinate value (real number) scalar
  direction: input
  data_types: single | double | fixed point
- name: θ
  summary: Angle represented by arctangent scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **A** — y-coordinate value (real number) scalar

Real number on the y-axis that you provide as input to the block.

**Data Types:** `single` | `double` | `fixed point`

### **B** — x-coordinate value (real number) scalar

Real number on the x-axis that you provide as input to the block.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **θ** — Angle represented by arctangent scalar

Angle represented by arctangent. This is the angle made by a vector from the
origin to a specified point (x,y) with the positive x-axis.

**Data Types:** `single` | `double` | `fixed point`

The following figure shows the representation of input values A, B, and arctangent on
the x-y coordinate plane.
## Parameters
```yaml
parameters:
- name: Approximation method
  summary: Type of approximation used for atan2 computation None (default) | CORDIC | Lookup
  group: ''
- name: Output unit
  summary: Unit of output values Radians (default) | PerUnit
  group: ''
```

### **Approximation method** — Type of approximation used for atan2 computation `None` (default) | `CORDIC` | `Lookup`

Type of approximation that the block uses for atan2 computation:

- `None` — The block does not use any
  approximation.
- `CORDIC` — The block uses the approximation based on
  coordinate rotation digital computer (CORDIC) algorithm.
- `Lookup` — The block uses the lookup table based
  approximation.

**Note**

When you use the block for code generation:

- `None` option works better with single data
  type.
- `CORDIC` option works better for FPGA
  deployment.
- `Lookup` option works better with fixed-point data
  type.

### **Output unit** — Unit of output values `Radians` (default) | `PerUnit`

Unit of the output values.
## Libraries

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

**Restriction**

If you run third-party (3p) simulation, the block may show a minor mismatch (of the
order `1e-7`) in the simulation results because of an internal
trigonometric function that uses the floating point datatype.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute four-quadrant arctangent

The atan2 block performs the four-quadrant arctangent on two real
numbers.

### Equations

This equation describes how the block computes the four-quadrant arctangent
(`θ`).

Theta=atan2(A,B)={arctan(AB)                 if B>0,arctan(AB)+π           if B<0 and A≥0,arctan(AB)−π           if B<0 and A<0,+π2                            if B=0 and A>0, −π2                            if B=0 and A<0,undefined                 if B=0 and A=0.

where:

−π<Theta≤π    (Radians)
