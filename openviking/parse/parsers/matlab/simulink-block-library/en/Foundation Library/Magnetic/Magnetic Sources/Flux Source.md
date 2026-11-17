---
type: simulink-block
title: 'Flux Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'fluxsource'
documentation_source_path: 'ref/fluxsource.html'
language: en
---

# Flux Source

## Ports
```yaml
ports: []
```

The block has two magnetic conserving ports associated with
its terminals.
## Parameters
```yaml
parameters: []
```

**Constant flux**
:   Output flux. You can specify any real value. The default value
    is `0.001` Wb.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Ideal flux source

The Flux Source block represents an ideal flux
source that is powerful enough to maintain specified constant flux
through it, regardless of the mmf across its terminals.

You specify the output flux by using the **Constant
flux** parameter, which can be positive, negative, or zero.

The positive direction of the flux flow is indicated by the
arrow.
