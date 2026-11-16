---
type: simulink-block
title: 'Hydraulic Constant Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantflowratesource'
documentation_source_path: 'ref/hydraulicconstantflowratesource.html'
language: en
---

# Hydraulic Constant Flow Rate Source

## Ports

The block has the following ports:

`T`
:   Hydraulic conserving port associated with the source inlet.

`P`
:   Hydraulic conserving port associated with the source outlet.

## Parameters

**Source flow rate**
:   Specifies the flow rate through the source. The default value is
    `0.001` m^3/s.

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

(To be removed) Ideal source of hydraulic energy, characterized by constant flow rate

The Hydraulic Constant Flow Rate Source block represents an ideal
source of hydraulic energy that is powerful enough to maintain specified flow rate at
its outlet regardless of the pressure differential across the source. The
**Source flow rate** parameter specifies the flow rate through the
source.

Block connections T and P correspond to the hydraulic inlet and outlet ports,
respectively. The block positive direction is from port T to port P.
