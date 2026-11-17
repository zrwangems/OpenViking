---
type: simulink-block
title: 'Clarke Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'clarketransform'
documentation_source_path: 'ref/clarketransform.html'
language: en
---

# Clarke Transform

## Ports
```yaml
ports:
- name: a
  summary: Phase component scalar
  direction: input
  data_types: single | double | fixed point
- name: b
  summary: Phase component scalar
  direction: input
  data_types: single | double | fixed point
- name: abc
  summary: Phase components scalar
  direction: input
  data_types: single | double | fixed point
- name: α
  summary: Axis component scalar
  direction: output
  data_types: single | double | fixed point
- name: β
  summary: Axis component scalar
  direction: output
  data_types: single | double | fixed point
- name: αβ0
  summary: Axis components scalar
  direction: output
  data_types: single | double | fixed point
```

### Input

### **a** — Phase component scalar

Component of the three-phase system in the *abc* reference
frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **b** — Phase component scalar

Component of the three-phase system in the *abc* reference
frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **abc** — Phase components scalar

Multiplexed phase components *a*, *b*, and
*c* of the three-phase system in the *abc*
reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Three inputs`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **α** — Axis component scalar

Alpha-axis component, *α*, in the stationary
*αβ* reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **β** — Axis component scalar

Beta-axis component, *β*, in the stationary *αβ*
reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **αβ0** — Axis components scalar

Multiplexed alpha-axis component, *α* and beta-axis component,
*β* and `0` component, in the stationary
*αβ* reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Three inputs`.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of inputs
  summary: Number of block inputs Two inputs (default) | Three inputs
  group: ''
- name: Power invariant
  summary: Enable power invariance off (default) | on
  group: ''
```

### **Number of inputs** — Number of block inputs `Two inputs` (default) | `Three inputs`

Select the number of inputs that you can specify:

- `Two inputs` — Configure the block to accept two
  separate input signals *a* and *b*. The block
  generates two separate output signals *α* and
  *β*.
- `Three inputs` — Configure the block to accept a
  multiplexed input containing *a*, *b*, and
  *c* signals. The block generates a multiplexed output containing
  *α*, *β*, and *0*
  signals.

### **Power invariant** — Enable power invariance `off` (default) | `on`

To enable the power invariance property in the block output, select this parameter.
To disable power invariance (enable amplitude invariance) in the block output, clear
this parameter.
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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Implement ab to αβ transformation

The Clarke Transform block computes the Clarke transformation of balanced
three-phase components in the *abc* reference frame and outputs the balanced
two-phase orthogonal components in the stationary *αβ* reference frame.
Alternatively, the block can compute Clarke transformation of three-phase components
*a*, *b*, and *c* and output the
components *α*, *β*, and `0`. For a
balanced system, the zero component is equal to zero. Use the **Number of
inputs** parameter to use either two or three inputs.

When using two-input configuration, the block accepts two signals out of the three phases
(*abc*), automatically calculates the third signal, and outputs the
corresponding components in the *αβ* reference frame.

For example, the block accepts either *a* and *b* input
values or the multiplexed input value *abc* where the
phase-*a* axis aligns with the *α*-axis.

- This figure shows the direction of the magnetic axes of the stator windings in the
  *abc* reference frame and the stationary *αβ*
  reference frame.
- This figure shows the equivalent *α* and *β*
  components in the stationary *αβ* reference frame.
- The time-response of the individual components of equivalent balanced
  *abc* and *αβ* systems.

### Equations

The following equation describes the Clarke transform computation:

[fαfβf0]=(23)×[1−12−120 32−3212 12 12][fafbfc]

For balanced systems like motors, the zero sequence component calculation is always
zero. For example, the currents of the motor can be represented as,

ia+ib+ic=0

Therefore, you can use only two current sensors in three-phase motor drives, where you
can calculate the third phase as,

ic=−(ia+ib)

By using these equations, the block implements the Clarke transform as,

[fαfβ]= [1013  23][fafb]

where:

- fa, fb, and fc are the balanced three-phase components in the *abc*
  reference frame.
- fα and fβ are the balanced two-phase orthogonal components in the stationary
  *αβ* reference frame.
- f0 is the zero component in the stationary *αβ*
  reference frame.
