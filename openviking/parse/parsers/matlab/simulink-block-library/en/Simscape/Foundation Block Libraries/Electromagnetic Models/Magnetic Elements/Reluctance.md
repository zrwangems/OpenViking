---
type: simulink-block
title: 'Reluctance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'reluctance'
documentation_source_path: 'ref/reluctance.html'
language: en
---

# Reluctance

## Ports

The block has the following ports:

`N`
:   Magnetic conserving port associated with the block North terminal.

`S`
:   Magnetic conserving port associated with the block South terminal.

## Parameters

**Thickness or length of section or gap**
:   Thickness of the section being modeled, or length of air gap.
    The default value is `0.001` m.

**Cross-sectional area**
:   Area of the section being modeled. The default value is `0.01` m^2.

**Relative permeability of material**
:   Relative permeability of the section material. The default value
    is `1`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Magnetic reluctance

The Reluctance block models a magnetic reluctance,
that is, a component that resists flux flow. The ratio of the magnetomotive
force (mmf) across the component to the resulting flux that flows
through the component is constant, and the ratio value is defined
as the reluctance. Reluctance depends on the geometry of the section
being modeled.

The block is based on the following equations:

MMF=Φ⋅ℜ

ℜ=gμ0⋅μr⋅A

where

|  |  |
| --- | --- |
| *MMF* | Magnetomotive force (mmf) across the component |
| *Φ* | Flux through the component |
| ℜ | Reluctance |
| *g* | Thickness of the section being modeled, or length of air gap |
| *μ*0 | Permeability constant |
| *μ*r | Relative permeability of the material |
| *A* | Cross-sectional area of the section being modeled |

Connections N and S are magnetic conserving ports. The mmf across
the reluctance is given by MMF(N)−MMF(S),
and the sign of the flux is positive when flowing through the device
from N to S.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
