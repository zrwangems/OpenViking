---
type: simulink-block
title: 'Electromagnetic Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electromagnetic Models / Magnetic Elements'
documentation_page: 'electromagneticconverter'
documentation_source_path: 'ref/electromagneticconverter.html'
language: en
---

# Electromagnetic Converter

## Ports

The block has the following ports:

`N`
:   Magnetic conserving port associated with the block North terminal.

`S`
:   Magnetic conserving port associated with the block South terminal.

`+`
:   Positive electrical conserving port.

`-`
:   Negative electrical conserving port.

## Parameters

**Number of winding turns**
:   Number of electrical winding turns. The default value is `1`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Lossless electromagnetic energy conversion device

The Electromagnetic Converter block provides
a generic interface between the electrical and magnetic domains.

The block is based on the following equations:

MMF=N⋅I

V=−N⋅dΦdt

where

|  |  |
| --- | --- |
| *MMF* | Magnetomotive force (mmf) across the magnetic ports |
| *Φ* | Flux through the magnetic ports |
| *I* | Current through the electrical ports |
| *V* | Voltage across the electrical ports |
| *N* | Number of electrical winding turns |
| *t* | Simulation time |

Connections N and S are magnetic conserving ports, and connections
+ and – are electrical conserving ports. If the current from
the electrical + to – ports is positive, then the resulting
mmf is positive acting across the magnetic N to S ports. A positive
rate of change of flux flowing from N to S results in a negative induced
voltage across the + and – ports.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
