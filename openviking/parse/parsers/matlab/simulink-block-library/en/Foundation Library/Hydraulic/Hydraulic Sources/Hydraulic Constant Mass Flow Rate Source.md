---
type: simulink-block
title: 'Hydraulic Constant Mass Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantmassflowratesource'
documentation_source_path: 'ref/hydraulicconstantmassflowratesource.html'
language: en
---

# Hydraulic Constant Mass Flow Rate Source

## Ports
```yaml
ports: []
```

The block has the following ports:

`T`
:   Hydraulic conserving port associated with the source inlet.

`P`
:   Hydraulic conserving port associated with the source outlet.
## Parameters
```yaml
parameters: []
```

**Mass flow rate**
:   Specifies the mass flow rate through the source. The default value is
    `0.001` kg/s.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Ideal source of mechanical energy in hydraulic network, characterized by constant mass flow rate

The Hydraulic Constant Mass Flow Rate Source block represents an ideal
mechanical energy source in a hydraulic network that can maintain a constant mass flow
rate regardless of the pressure differential across the source. The source does not
generate any losses due to friction. The **Mass flow rate** parameter
specifies the mass flow rate through the source.

Block connections T and P correspond to the hydraulic inlet and outlet ports,
respectively. A positive mass flow rate causes liquid to flow from port T to port P.
