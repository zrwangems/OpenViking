---
type: simulink-block
title: 'Gyrator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'gyrator'
documentation_source_path: 'ref/gyrator.html'
language: en
---

# Gyrator

## Ports

The block has four electrical conserving ports. Polarity is indicated by the + and – signs.
Ports labeled 1+ and 1– are connected to the primary winding. Ports labeled 2+ and 2– are
connected to the secondary winding.

## Parameters

**Gyration conductance**
:   The gyration conductance constant *G*. The
    default value is `1`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Ideal gyrator in electrical systems

Gyrators can be used to implement an inductor with a capacitor.
The main benefit is that an equivalent inductance can be created with
a much smaller physically sized capacitance. In practice, a gyrator
is implemented with an op-amp plus additional passive components.

The Gyrator block models an ideal gyrator with
no losses, described with the following equations:

I1=G·V2

I2=G·V1

where

|  |  |
| --- | --- |
| *`V1`* | Input voltage |
| *`V2`* | Output voltage |
| *`I1`* | Current flowing into the input + terminal |
| *`I2`* | Current flowing out of the output + terminal |
| *`G`* | Gyration conductance |

The two electrical networks connected to the primary and secondary
windings must each have their own Electrical Reference block.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
