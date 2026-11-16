---
type: simulink-block
title: 'Internal Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'internalforce'
documentation_source_path: 'ref/internalforce.html'
language: en
---

# Internal Force

## Ports

This block contains frame ports **B** and **F**,
representing base and follower port frames, respectively. A physical
signal port, **fm**, provides the means to specify
the internal force acting between the two port frames.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

General force acting reciprocally between two frame origins

This block represents a general force pair acting reciprocally
between base and follower frame origins. The two forces in the pair
have equal magnitude but opposite directions. One force acts on the
base frame origin, along the vector connecting follower to base frame
origins. The other force acts on the follower frame origin, along
the vector connecting base to follower frame origins.

To specify the internal force, the block provides physical signal
port **fm**. A positive input signal represents a
repulsive force, which pushes base and follower frame origins apart.
A negative input signal represents an attractive force, which pulls
base and follower frame origins together. If at any time the two frame
origins are coincident, the internal force direction becomes undefined
and Simscape™
Multibody™ might stop with an error.
