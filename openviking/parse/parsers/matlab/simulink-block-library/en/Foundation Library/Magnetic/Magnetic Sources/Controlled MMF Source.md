---
type: simulink-block
title: 'Controlled MMF Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'controlledmmfsource'
documentation_source_path: 'ref/controlledmmfsource.html'
language: en
---

# Controlled MMF Source

## Ports
```yaml
ports: []
```

The block has one physical signal input port and two magnetic
conserving ports associated with its magnetic terminals.
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

**Introduced in R2010a**

## Description

Ideal magnetomotive force source driven by input signal

The Controlled MMF Source block represents an
ideal magnetomotive force (mmf) source that is powerful enough to
maintain the specified mmf at its output regardless of the flux passing
through it.

The output mmf is *MMF = MMFI*, where *MMFI* is
the numerical value presented at the physical signal port.
