---
type: simulink-block
title: 'Hydraulic Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydraulicreference'
documentation_source_path: 'ref/hydraulicreference.html'
language: en
---

# Hydraulic Reference

## Ports
```yaml
ports: []
```

The block has one hydraulic conserving port.
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

**Introduced in R2007a**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Connection to atmospheric pressure

The Hydraulic Reference block represents a connection to atmospheric
pressure. Hydraulic conserving ports of all the blocks that are referenced to atmosphere
(for example, suction ports of hydraulic pumps, or return ports of valves, cylinders,
pipelines, if they are considered directly connected to atmosphere) must be connected to
a Hydraulic Reference block.
