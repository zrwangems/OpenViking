---
type: simulink-block
title: 'Linear Hydraulic Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'linearhydraulicresistance'
documentation_source_path: 'ref/linearhydraulicresistance.html'
language: en
---

# Linear Hydraulic Resistance

## Ports

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the resistance inlet.

`B`
:   Hydraulic conserving port associated with the resistance outlet.

## Parameters

**Resistance**
:   The linear resistance coefficient. The default value is `10e9`
    Pa/(m^3/s).

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

(To be removed) Hydraulic pipeline with linear resistance losses

The Linear Hydraulic Resistance block represents a hydraulic resistance where
pressure loss is directly proportional to flow rate. This block can be useful at preliminary
stages of development, or as a powerful means to speed up the simulation, especially if the flow
rate varies insignificantly with respect to the operating point.

Connections A and B are conserving hydraulic ports associated with the block inlet and
outlet, respectively.

The block positive direction is from port A to port B. This means that the flow rate is
positive if fluid flows from A to B, and the pressure loss is determined as p=pA−pB.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
