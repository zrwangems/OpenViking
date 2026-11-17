---
type: simulink-block
title: 'MMF Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'mmfsource'
documentation_source_path: 'ref/mmfsource.html'
language: en
---

# MMF Source

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

**Constant mmf**
:   Output mmf. You can specify any real value. The default value
    is `1` A.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Ideal magnetomotive force source

The MMF Source block represents an ideal magnetomotive
force (mmf) source that is powerful enough to maintain specified constant
mmf across its output terminals, regardless of the flux flowing through
the source.

You specify the output mmf by using the **Constant mmf** parameter,
which can be positive, negative, or zero.
