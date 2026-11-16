---
type: simulink-block
title: 'Fundamental Reluctance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'fundamentalreluctance'
documentation_source_path: 'ref/fundamentalreluctance.html'
language: en
---

# Fundamental Reluctance

## Ports

The block has the following ports:

`N`
:   Magnetic conserving port associated with the block North terminal.

`S`
:   Magnetic conserving port associated with the block South terminal.

## Parameters

**Reluctance**
:   The ratio of the magnetomotive force (mmf) across the component
    to the resulting flux that flows through the component. The default
    value is `8e4` 1/H.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

## Description

Simplified implementation of magnetic reluctance

The Fundamental Reluctance block provides a simplified
model of a magnetic reluctance, that is, a component that resists
flux flow. Unlike the Reluctance block, which computes
reluctance based on the geometry of the section being modeled, the Fundamental
Reluctance block lets you specify a value of reluctance directly
as a block parameter.

The block is based on the following equation:

MMF=Φ⋅ℜ

where

|  |  |
| --- | --- |
| *MMF* | Magnetomotive force (mmf) across the component |
| *Φ* | Flux through the component |
| ℜ | Reluctance |

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
