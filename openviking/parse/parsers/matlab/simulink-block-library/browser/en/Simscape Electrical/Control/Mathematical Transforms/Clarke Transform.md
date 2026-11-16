---
type: simulink-block
title: 'Clarke Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'clarketransform'
documentation_source_path: 'ref/clarketransform.html'
language: en
---

# Clarke Transform

## Ports

### Input

### **abc** — *a*-, *b*-, and *c*-phase components vector

Components of the three-phase system in the *abc*
reference frame.

#### Dependencies

To enable this port, either
clear the **Use block for embedded implementation (requires
Motor Control Blockset™)** parameter or select the
**Use block for embedded implementation (requires Motor
Control Blockset™)** parameter and set **Number
of inputs** to `Three
inputs`. *(since R2025a)*

**Data Types:** `single` | `double`

### **a** — *a*-phase component scalar

*Since R2025a*

*a*-phase component of the three-phase system in the
*abc* reference frame.

#### Dependencies

To enable this port, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter and set **Number of inputs** to
`Two inputs`.

**Data Types:** `single` | `double`

### **b** — *b*-phase component scalar

*Since R2025a*

*b*-phase component of the three-phase system in the
*abc* reference frame.

#### Dependencies

To enable this port, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter and set **Number of inputs** to
`Two inputs`.

**Data Types:** `single` | `double`
### Output

### **αβ0** — *α*-*β* axis and zero components vector

Alpha-axis component,*α*, beta-axis component
*β*, and zero component in the stationary reference
frame.

#### Dependencies

To enable this port, either
clear the **Use block for embedded implementation (requires
Motor Control Blockset™)** parameter or select the
**Use block for embedded implementation (requires Motor
Control Blockset™)** parameter and set **Number
of inputs** to `Three
inputs`. *(since R2025a)*

**Data Types:** `single` | `double`

### **α** — Alpha-axis component scalar

*Since R2025a*

Alpha-axis component,*α*, in the stationary reference
frame.

#### Dependencies

To enable this port, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter and set **Number of inputs** to
`Two inputs`.

**Data Types:** `single` | `double`

### **β** — Beta-axis component scalar

*Since R2025a*

Beta-axis component,*β*, in the stationary reference
frame.

#### Dependencies

To enable this port, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter and set **Number of inputs** to
`Two inputs`.

**Data Types:** `single` | `double`

## Parameters

### **Power Invariant** — Enable power invariance `off` (default) | `on`

Option to preserve the active and reactive power of the system in the
*abc* reference frame.

### **Use block for embedded implementation (requires Motor Control Blockset™)** — Option to use block for embedded implementation `off` (default) | `on`

*Since R2025a*

Option to use the block for embedded implementation. This option requires
the Motor Control Blockset toolbox.

### **Number of inputs** — Number of block inputs `Two inputs` (default) | `Three inputs`

*Since R2025a*

Select the number of inputs that you can specify:

- `Two inputs` — Configure the block to
  accept two separate input signals *a* and
  *b*. The block generates two separate
  output signals *α* and
  *β*.
- `Three inputs` — Configure the block
  to accept a multiplexed input containing *a*,
  *b*, and *c* signals. The
  block generates a multiplexed output containing
  *α*, *β*, and
  *0* signals.

#### Dependencies

To enable this parameter, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter.

## Libraries

Simscape / Electrical / Control / Mathematical Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2025a: Optimize block for embedded implementation

If you have a license for Motor Control Blockset toolbox, you can optimize the Clarke Transform block for embedded
implementation. To optimize this block for embedded implementation, select the
**Use block for embedded implementation (requires Motor Control
Blockset™)** parameter.

## Description

Implement abc to αβ0 transform

The Clarke Transform block converts the time-domain components of a
three-phase system in an *abc* reference frame to components in a
stationary *ɑβ0* reference frame. The block can preserve the active and
reactive powers with the powers of the system in the *abc* reference
frame by implementing a power invariant version of the Clarke transform. For a balanced
system, the zero component is equal to zero.

If you have a license for Motor Control Blockset™ toolbox, you can use this block for embedded implementation. Use the
**Number of inputs** parameter to specify either two or three
inputs. When you set the **Number of inputs** parameter to
`Two inputs`, the block accepts two signals out of the
three phases (*abc*), automatically calculates the
third signal, and outputs the corresponding components in the *αβ* reference frame. *(since R2025a)*

The figures show:

- The direction of the magnetic axes of the stator windings in the
  *abc* reference frame and the stationary
  *ɑβ0* reference frame
- Equivalent *ɑ*, *β*, and zero components
  in the stationary reference frame
- The time-response of the individual components of equivalent balanced
  *abc* and *ɑβ0* systems

### Equations

The block implements the Clarke transform as

[αβ0]=23[1−12−12032−32121212][abc],

where:

- *a*, *b*, and *c*
  are the components of the three-phase system in the
  *abc* reference frame.
- *α* and *β* are the components of
  the two-axis system in the stationary reference frame.
- *0* is the zero component of the two-axis system in
  the stationary reference frame.

The block implements the power invariant version of the Clarke transform as

[αβ0]=23[1−12−12032−32121212][abc].
