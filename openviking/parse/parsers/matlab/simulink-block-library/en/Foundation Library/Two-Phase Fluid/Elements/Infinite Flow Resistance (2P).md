---
type: simulink-block
title: 'Infinite Flow Resistance (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'infiniteflowresistance2p'
documentation_source_path: 'ref/infiniteflowresistance2p.html'
language: en
---

# Infinite Flow Resistance (2P)

## Ports
```yaml
ports: []
```

The block has a pair of two-phase fluid conserving ports, A
and B, representing branches of adjacent two-phase fluid networks.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Perfectly insulated break in two-phase fluid network

The Infinite Flow Resistance (2P) block represents a break in a two-phase fluid
network. There is no mass or energy flow through the break. However, the fluid
properties, specified by the Two-Phase Fluid Properties (2P) block connected to the circuit, are
the same on both sides of the break. Use this block to set the priority and initial
target value to the differences in pressure and specific internal energy between port
**A** and port **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
