---
type: simulink-block
title: 'Hydraulic Mass Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicmassflowratesource'
documentation_source_path: 'ref/hydraulicmassflowratesource.html'
language: en
---

# Hydraulic Mass Flow Rate Source

## Ports
```yaml
ports: []
```

The block has the following ports:

`T`
:   Hydraulic conserving port associated with the source inlet.

`P`
:   Hydraulic conserving port associated with the source outlet.

`M`
:   Control signal port.
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

**Introduced in R2016b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Ideal source of mechanical energy in hydraulic network, characterized by mass flow rate

The Hydraulic Mass Flow Rate Source block represents an ideal
mechanical energy source in a hydraulic network that can maintain a specified mass flow
rate regardless of the pressure differential across the source. The source does not
generate any losses due to friction. Block connections T and P correspond to the
hydraulic inlet and outlet ports, respectively. The mass flow rate through the source is
directly proportional to the signal at the control port M.

A positive mass flow rate causes liquid to flow from port T to port P.
