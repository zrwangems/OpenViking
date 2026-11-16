---
type: simulink-block
title: 'Angle Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Other Constraints'
documentation_page: 'angleconstraint'
documentation_source_path: 'ref/angleconstraint.html'
language: en
---

# Angle Constraint

## Ports

The block provides two frame ports:

- B — Base frame port
- F — Follower frame port

In addition, the block provides two physical signal output ports:

- t — Angle constraint torque vector
- tm — Signed magnitude of the angle constraint torque

## Parameters

**Type**
:   Angle constraint type. The default setting is
    `General`.

    | Type | Purpose |
    | --- | --- |
    | `Parallel` | Align the base and follower frame +Z axes. |
    | `Anti-Parallel` | Align the base frame +Z axis with the follower frame -Z axis. |
    | `Perpendicular` | Make the base and follower frame Z axes perpendicular to each other. |
    | `General` | Hold the specified angle between the Z axes of the base and follower port frames. |

**Angle**
:   Constraint angle between the base and follower frame Z axes. The angle
    must lie in the range 0 < θ < 180 deg. For an angle of `0` or
    `180` deg, set **Type** to
    `Parallel` or
    `Anti-Parallel` instead. The default value is
    `45` deg.

### Constraint Torque Sensing

Select whether to compute and output the distance constraint torque vector and its
magnitude. The distance constraint torque is the torque the block must apply in
order to maintain the angle you specify between the base and follower port
frames.

**Direction**
:   Constraint torques act in pairs. As expressed by Newton’s third law of
    motion, if the base port frame exerts a constraint torque on the
    follower port frame, then the follower port frame must exert an equal
    and opposite torque on the base port frame. Select which of the two
    constraint torques to sense:

    - `Follower on Base` — Sense
      the constraint torque that the follower port frame exerts on
      the base port frame.
    - `Base on Follower` — Sense
      the constraint torque that the base port frame exerts on the
      follower port frame.

**Resolution Frame**
:   The block expresses the constraint torque vector in terms of its
    Cartesian vector components. The splitting of a vector into vector
    components is known as vector resolution. The frame whose axes define
    the vector component directions is known as the resolution frame. Select
    whether to resolve the constraint torque vector in the base or follower
    port frame.

**Torque Vector**
:   Compute and output the Cartesian components of the angle constraint
    torque vector. The output signal is a three-dimensional vector with
    components expressed about the X, Y, and Z axes of the resolution
    frame.

**Signed Torque Magnitude**
:   Compute and output the magnitude of the angle constraint torque,
    including its sign.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Fixed angle between two frame Z axes
