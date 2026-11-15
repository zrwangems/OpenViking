---
type: simulink-block
title: 'Inverse Park Transform'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Math Transforms'
documentation_page: 'inverseparktransform'
documentation_source_path: 'ref/inverseparktransform.html'
language: en
---

# Inverse Park Transform

## Ports

### Input

### **d** — Axis component scalar

Direct axis component, *d*, in the rotating *dq*
reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **q** — Axis component scalar

Quadrature axis component, *q*, in the rotating
*dq* reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Two inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **dq0** — Axis components scalar

Multiplexed direct axis component, *d*, quadrature axis
component, *q*, and the *0* component in the
rotating *dq* reference frame.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
`Three inputs`.

**Data Types:** `single` | `double` | `fixed point`

### **sin θe** — Sine value of rotational angle scalar

Sine value of the angle of transformation,
*θe*.
*θe* is the angle between the rotating
reference frame and the *α*-axis.

**Data Types:** `single` | `double` | `fixed point`

### **cos θe** — Cosine value of rotational angle scalar

Cosine value of the angle of transformation,
*θe*.
*θe* is the angle between the rotating
reference frame and the *α*-axis.

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

### **Number of inputs** — Number of block inputs `Two inputs` (default) | `Three inputs`

Select the number of inputs that you can specify:

- `Two inputs` — Configure the block to accept two
  separate input signals *d* and *q*. The block
  generates two separate output signals *α* and
  *β*.
- `Three inputs` — Configure the block to accept a
  multiplexed input containing *d*,*q*, and
  *0* signals. The block generates a multiplexed output containing
  *α*, *β*, and *0*
  signals.

### **Alpha (phase-a) axis alignment** — *dq* reference frame alignment `D-axis` (default) | `Q-axis`

Align either the *d*- or *q*-axis of the rotating
reference frame to the *α*-axis of the stationary reference
frame.

### **Theta input** — Type of position input `Sine and Cosine electrical position` (default) | `Electrical position`

Type of position (theta) input:

- `Sine and Cosine electrical position` — Configure the
  block to directly accept *sinθe* and
  *cosθe* inputs.
- `Electrical position` — Configure the block to accept
  the electrical position (*θe*) input. The
  block internally computes the *sinθe* and
  *cosθe* signals from the
  *θe* input.

### **Theta units** — Unit of electrical position input `Per-unit` (default) | `Radians` | `Degrees`

Unit of the electrical position input
(*θe*).

#### Dependencies

To enable this parameter, set **Theta input** to
`Electrical position`.

### **Number of data points for lookup table** — Size of lookup table array `1024` (default) | scalar

Size of the lookup table array that the block uses to compute
*sinθe* and
*cosθe* signals from the
*θe* input. You can specify a value between
125 and 4095.

#### Dependencies

To enable this parameter, set **Theta input** to
`Electrical position`.

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
| **FlattenHierarchy** | Remove Inverse Park Transform block hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder).  If you are using resource sharing optimization for the Inverse Park Transform block (by setting the **SharingFactor** property to a value greater than 0), set the **FlattenHierarchy** property of the block to `on`. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Implement dq to αβ transformation

The Inverse Park Transform block computes the inverse Park transformation
of the orthogonal direct (*d*) and quadrature (*q*) axes
components or the multiplexed *dq0* components in the rotating
*dq* reference frame.

You can configure the block to align either the *d*- or
*q*-axis with the *α*-axis at time *t* =
0.

The block accepts the following inputs:

- Either *d-q* axes components or multiplexed components
  *dq0* in the rotating reference frame. Use the **Number of
  inputs** parameter to use either two or three inputs.
- Sine and cosine values of the corresponding angles of transformation.

When using two-input configuration, the block outputs the two-phase orthogonal components
in the stationary *αβ* reference frame. When using three-input configuration,
it outputs multiplexed components *αβ0*.

For a balanced system, the zero component is equal to zero.

The figures show a rotating *dq* reference frame and the
*α-β* axes components in an *αβ* reference frame for
when:

- The *d*-axis aligns with the *α*-axis.
- The *q*-axis aligns with the *α*-axis.

  In both cases, the angle *θ = ωt*, where:

  - *θ* is the angle between the *α*- and
    *d*-axes for the *d*-axis alignment or the angle
    between the *α*- and *q*-axes for the
    *q*-axis alignment. It indicates the angular position of the
    rotating *dq* reference frame with respect to the
    *α*-axis.
  - *ω* is the rotational speed of the *d-q*
    reference frame.
  - *t* is the time, in seconds, from the initial alignment.

The figures show the time-response of the individual components of the
*αβ* and *dq* reference frames when:

- The *d*-axis aligns with the *α*-axis.
- The *q*-axis aligns with the *α*-axis.

### Equations

If the **Number of inputs** parameter is set to `Two
inputs`, the following equations describe how the block implements inverse
Park transformation.

- When the *d*-axis aligns with the *α*-axis.

  [fαfβ]= [cosθ−sinθsinθcosθ][fdfq]
- When the *q*-axis aligns with the *α*-axis.

  [fαfβ]= [sinθcosθ−cosθsinθ][fdfq]

where:

- fd and fq are the direct and quadrature axis orthogonal components in the
  rotating *dq* reference frame.
- fα and fβ are the two-phase orthogonal components in the stationary
  *αβ* reference frame.

If the **Number of inputs** parameter is set to `Three
inputs`, the following equations describe how the block implements inverse
Park transformation:

- The Inverse Park block implements the transform for an
  *a*-phase to *q*-axis alignment as

  [αβ0]=[sin(θ)cos(θ)0−cos(θ)sin(θ)0001][dq0]

  where:

  - *d* and *q* are the direct-axis and
    quadrature-axis components of the two-axis system in the rotating reference
    frame.
  - *0* is the zero component.
  - *α* and *β* are the alpha-axis and
    beta-axis components of the two-phase system in the stationary reference
    frame.
- For an *a*-phase to *d*-axis alignment, the
  block implements the transform using this equation:

  [αβ0]=[cos(θ)−sin(θ)0sin(θ)cos(θ)0001][dq0]
