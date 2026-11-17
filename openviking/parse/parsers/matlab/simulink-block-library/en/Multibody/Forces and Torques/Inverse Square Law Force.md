---
type: simulink-block
title: 'Inverse Square Law Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'inversesquarelawforce'
documentation_source_path: 'ref/inversesquarelawforce.html'
language: en
---

# Inverse Square Law Force

## Ports
```yaml
ports: []
```

The block contains frame ports B and F, representing base and
follower frames, respectively.

Selecting **Sense Force** in the block dialog
box exposes an additional physical signal port, **fm**.
## Parameters
```yaml
parameters: []
```

**Force Constant**
:   Specify the proportionality constant of the inverse square law
    force. This constant is a lumped parameter that encodes the dependence
    of the force magnitude on the inverse square distance between the
    two frame origins. The default value is `1`. Select
    or specify a physical unit.

**Sense Force**
:   Select the check box to sense the signed magnitude of the inverse
    square law force acting between the two frame origins. The block exposes
    an additional physical signal port to output the force signal. The
    output signal is a scalar value. This value is positive if the force
    is repulsive; it is negative if the force is attractive.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Force proportional to the inverse square distance between two frame origins

This block represents a force pair that is inversely proportional
to the square distance between the base and follower frame origins.
The two forces in the pair have equal magnitude but opposite directions.
One force acts on the base frame origin, along the vector connecting
the follower to base frame origins. The other force acts on the follower
frame origin, along the vector connecting base to follower frame origins.

The value of the force depends on a force constant that you
specify. A positive force constant represents a repulsive force that
pushes the two frame origins apart. A negative force constant represents
an attractive force that pulls the two frame origins together.
