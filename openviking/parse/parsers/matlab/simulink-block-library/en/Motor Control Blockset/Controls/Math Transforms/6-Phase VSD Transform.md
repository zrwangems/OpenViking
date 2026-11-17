---
type: simulink-block
title: '6-Phase VSD Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: '6phasevsdtransform'
documentation_source_path: 'ref/6phasevsdtransform.html'
language: en
---

# 6-Phase VSD Transform

## Ports

### Input

### **a1b1c1** — First set of three-phase inputs scalar

First set of three-phase inputs. For a six-phase PMSM, this port accepts the
three-phase stator voltages or currents belonging to the first three-phase
winding set.

**Data Types:** `single` | `double` | `fixed point`

### **a2b2c2** — Second set of three-phase inputs scalar

Second set of three-phase inputs. For a six-phase PMSM, this port accepts
the three-phase stator voltages or currents belonging to the second three-phase
winding set.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **αβxyz+z-** — Six axis components in three different subspaces scalar

Six axis components (*α*, *β*,
*x*, *y*,
*z+*, and
*z-*) in the following three
subspaces, such that phase *a1* axis aligns with the
*α* axis:

- *α*-*β* subspace (containing
  *α* and *β* components)
- *x*-*y* subspace (containing
  *x* and *y* components)
- Zero sequence subspace (containing
  *z+* and
  *z-* components)

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Power invariant** — Option to enable power invariant transformation `off` (default) | on

Select this parameter to enable the block to use power invariant
transformation. If you clear this parameter, the block uses amplitude invariant
transformation.

### **Motor type** — Type of six-phase PMSM `Asymmetric (30 degree offset)` (default) | `Symmetric (60 degree offset)`

Select the type of six-phase PMSM for which you want to compute the VSD
transformation.

## Libraries

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation
and synthesized logic.

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024b**

## Description

Compute vector space decomposition (VSD) based transformation on six-phase inputs

The 6-Phase VSD Transform block applies vector space decomposition (VSD)
transform (or decoupling transform) on six-phase inputs (*a1*,
*b1*, *c1*, *a2*,
*b2*, and *c2*) to generate the corresponding six axis
components (*α*, *β*, *x*,
*y*, *z+*, and
*z-*) in the following three
subspaces.

- *α*-*β* subspace (containing
  *α* and *β* components)
- *x*-*y* subspace (containing
  *x* and *y* components)
- Zero sequence subspace (containing *z+*
  and *z-* components)

The block accepts the six-phase inputs as two sets of three-phase signals.

You can use the block to determine these six axis components corresponding to the
six-phase stator voltages or currents of an asymmetric or a symmetric six-phase permanent
magnet synchronous motor (PMSM). For example, you can use this block to determine the
*α*, *β*, *x*, and
*y* components of the six-phase stator feedback currents and use them
to implement field-oriented control (FOC) of an asymmetric six-phase PMSM. For more
information, see Field-Oriented Control of Six-Phase PMSM.

Six-phase motors have different configurations based on the spatial angle (or spatial
shift) between the two sets of three-phase windings. An asymmetric six-phase PMSM uses a
spatial angle of 30 electrical degrees, whereas a symmetric six-phase PMSM uses a spatial
angle of 60 electrical degrees.

By default, the block uses amplitude invariant transformation. However, you can use the
parameter **Power invariant** to configure the block to use power
invariant transformation.

The following image shows the comparison between input signals
*a1* and
*b1* as well as the output signals
*α* and *β*.

For more information about the block algorithm, see Algorithm.
