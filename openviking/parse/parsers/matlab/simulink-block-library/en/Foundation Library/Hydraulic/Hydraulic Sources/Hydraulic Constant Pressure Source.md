---
type: simulink-block
title: 'Hydraulic Constant Pressure Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantpressuresource'
documentation_source_path: 'ref/hydraulicconstantpressuresource.html'
language: en
---

# Hydraulic Constant Pressure Source

## Ports

The block has the following ports:

`T`
:   Hydraulic conserving port associated with the source inlet.

`P`
:   Hydraulic conserving port associated with the source outlet.

## Parameters

**Pressure**
:   Specifies the pressure difference between the source inlet and outlet. The
    default value is `1e6` Pa.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Ideal source of hydraulic energy, characterized by constant pressure

The Hydraulic Constant Pressure Source block represents an ideal source
of hydraulic energy that is powerful enough to maintain the specified pressure
differential between its inlet and outlet regardless of the flow rate through the
source.

The **Pressure** parameter specifies the pressure differential across
the source

p=pP−pT

where *p*P,
*p*T are the gauge pressures at the source
ports.

Block connections T and P correspond to the hydraulic inlet and outlet ports,
respectively. The block positive direction is from port P to port T.
