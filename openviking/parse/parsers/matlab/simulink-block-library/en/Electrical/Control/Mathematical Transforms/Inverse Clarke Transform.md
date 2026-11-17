---
type: simulink-block
title: 'Inverse Clarke Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inverseclarketransform'
documentation_source_path: 'ref/inverseclarketransform.html'
language: en
---

# Inverse Clarke Transform

## Ports
```yaml
ports:
- name: αβ0
  summary: '*α*-*β* axis and zero components vector'
  direction: input
  data_types: single | double
- name: α
  summary: Alpha-axis component scalar
  direction: input
  data_types: single | double
- name: β
  summary: Beta-axis component scalar
  direction: input
  data_types: single | double
- name: abc
  summary: '*a*-, *b*-, and *c*-phase components vector'
  direction: output
  data_types: single | double
- name: a
  summary: '*a*-phase component scalar'
  direction: output
  data_types: single | double
- name: b
  summary: '*b*-phase component scalar'
  direction: output
  data_types: single | double
- name: c
  summary: '*c*-phase component scalar'
  direction: output
  data_types: single | double
```

### Input

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
### Output

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

### **c** — *c*-phase component scalar

*Since R2025a*

*c*-phase component of the three-phase system in the
*abc* reference frame.

#### Dependencies

To enable this port, select the **Use block for embedded
implementation (requires Motor Control Blockset™)**
parameter and set **Number of inputs** to
`Two inputs`.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Power Invariant
  summary: Enable power invariance off (default) | on
  group: ''
- name: Use block for embedded implementation (requires Motor Control Blockset™)
  summary: Option to use block for embedded implementation off (default) | on
  group: ''
- name: Number of inputs
  summary: Number of block inputs Two inputs (default) | Three inputs
  group: ''
```

### **Power Invariant** — Enable power invariance `off` (default) | `on`

Option to preserve the active and reactive power of the system in the
rotating reference frame.

### **Use block for embedded implementation (requires Motor Control Blockset™)** — Option to use block for embedded implementation `off` (default) | `on`

*Since R2025a*

Option to use the block for embedded implementation. This option requires
the Motor Control Blockset toolbox.

### **Number of inputs** — Number of block inputs `Two inputs` (default) | `Three inputs`

*Since R2025a*

Select the number of inputs that you can specify:

- `Two inputs` — Configure the block to
  accept two separate input signals *α* and
  *β*. The block generates three separate
  output signals *a*, *b*, and
  *c*.
- `Three inputs` — Configure the block
  to accept a multiplexed input containing *α*,
  *β*, and *0* signals. The
  block generates a multiplexed output containing
  *a*, *b*, and
  *c* signals.

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

If you have a license for Motor Control Blockset toolbox, you can optimize the Inverse Clarke Transform block for embedded
implementation. To optimize this block for embedded implementation, select the
**Use block for embedded implementation (requires Motor Control
Blockset™)** parameter.

## Description

Implement αβ0 to abc transform

The Inverse Clarke Transform block converts the time-domain alpha,
beta, and zero components in a stationary reference frame to three-phase components in
an *abc* reference frame. The block can preserve the active and
reactive powers with the powers of the system in the stationary reference frame by
implementing an invariant power version of the inverse Clarke transform. If the zero
component is zero, the components in the three-phase system are balanced.

If you have a license for Motor Control Blockset™ toolbox, you can use this block for embedded implementation. Use the
**Number of inputs** parameter to specify either two or three
inputs. When you set the **Number of inputs** parameter to
`Two inputs`, the block accepts two signals out of the
three phases (*abc*), automatically calculates the
third signal, and outputs the corresponding components in the *αβ* reference frame. *(since R2025a)*

The figures show:

- Balanced *ɑ*, *β*, and zero components
  in a stationary reference frame
- The direction of the magnetic axes of the stator windings in the
  stationary *ɑβ0* reference frame and the
  *abc* reference frame
- The time-response of the individual components of equivalent balanced
  *ɑβ0* and *abc* systems

### Equations

The block implements the inverse Clarke transform as

[abc]=[101−12321−12−321][αβ0]

where:

- *α* and *β* are the components in
  the stationary reference frame.
- *0* is the zero component in the stationary reference
  frame.
- *a*, *b*, and *c*
  are the components of the three-phase system in the
  *abc* reference frame.

The block implements this power invariant version of the inverse Clarke transform as

[abc]=23[1012−123212−12−3212][αβ0]
