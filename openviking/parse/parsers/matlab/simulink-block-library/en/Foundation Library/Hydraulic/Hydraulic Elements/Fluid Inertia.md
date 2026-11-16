---
type: simulink-block
title: 'Fluid Inertia'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'fluidinertia'
documentation_source_path: 'ref/fluidinertia.html'
language: en
---

# Fluid Inertia

## Ports

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the passage inlet.

`B`
:   Hydraulic conserving port associated with the passage outlet.

## Parameters

**Passage area**
:   Fluid passage cross-sectional area. The default value is
    `8e-5` m^2.

**Passage length**
:   Length of the fluid passage. The default value is `1`
    m.

**Initial flow rate**
:   Initial flow rate through the passage. This parameter specifies the
    initial condition for use in computing the block's initial state at the
    beginning of a simulation run. For more information, see Initial Conditions Computation. The default value is `0`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Pressure differential across tube or channel due to change in fluid velocity

The Fluid Inertia block models pressure differential, due to change in fluid velocity,
across a fluid passage of constant cross-sectional area. The pressure differential is
determined according to the following equation:

p=ρLAdqdt

where

|  |  |
| --- | --- |
| *p* | Pressure differential |
| *ρ* | Fluid density |
| *L* | Passage length |
| *A* | Passage area |
| *q* | Flow rate |
| *t* | Time |

Use this block in various pipe or channel models that require fluid inertia to be
accounted for.

The block positive direction is from port A to port B. This means that the flow rate
is positive if it flows from A to B.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
