---
type: simulink-block
title: 'Mechanism Configuration'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Utilities'
documentation_page: 'mechanismconfiguration'
documentation_source_path: 'ref/mechanismconfiguration.html'
language: en
---

# Mechanism Configuration

## Ports

### Frame

### **C** — Port to connect mechanism frame

Port to use to connect the mechanism. The settings of the Mechanism
Configuration block apply only to the mechanism to which the block
connects.
### Input

### **g** — Uniform gravity physical signal

Uniform gravity of the mechanism to which the Mechanism
Configuration block connects.

#### Dependencies

To enable this port, set **Uniform Gravity** to
`Time-Varying`.

## Parameters

#### Uniform Gravity

### **Uniform Gravity** — Method to specify gravitational acceleration vector `Constant` (default) | `Time-Varying` | `None`

Method used to calculate the uniform gravity for the mechanism to which the
Mechanism Configuration block connects, specified as
one of these options:

| Method | Description |
| --- | --- |
| `Constant` | Use the **Gravity** parameter to specify the gravitational acceleration vector that remains constant in space and in time. |
| `Time-Varying` | Use the physical port **g** to specify the gravitational acceleration vector that remains constant in space but varies in time. |
| `None` | Specify zero uniform gravity for the mechanism. This option must be used if the Simscape Multibody network contains a Gravitational Field block. |

### **Gravity** — Constant gravitational acceleration vector [0 0 –9.80665] `m/s^2` (default) | 1-by-3 vector

Constant gravitational acceleration vector, specified as a 1-by-3 vector,
[*gx*
*gy*
*gz*]. The block resolves the vector in the
world frame of the mechanical system.

#### Dependencies

To enable this parameter, specify **Uniform Gravity** to
`Constant`.

### **Linearization Delta** — Perturbation value for linearization 0.001 (default) | positive scalar

Perturbation value for computing numerical partial derivatives during linearization,
specified as a positive scalar. For more information about linearization, see Linearize Nonlinear Models (Simulink Control Design)
and `linmod`.

#### Joint Mode Transition

### **Nonlinear Iterations** — Number of Newton iterations for joints transitioning from disengaged to normal mode 2 (default) | positive integer

Number of Newton iterations to use for solving the positions of all the joints in
the mechanism when the mechanism has one or more joints that transition from disengaged
to normal mode, specified as a positive integer.

When a joint transitions from disengaged to normal mode, if that joint has large
discrepancies in its location and orientation, the Simscape
Multibody network may need a larger number of iterations to compute the required
positions of all joints in the mechanism that satisfy the kinematic constraints of that
transitioning joint.

## Libraries

Simscape / Multibody / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Mechanism-wide gravity and simulation parameters

The Mechanism Configuration block specifies the gravity and
simulation parameters of the mechanism to which the block connects. The simulation parameters
include the perturbation value for computing numerical partial derivatives during
linearization and the iteration number for the joint mode transition.

A Simscape™
Multibody™ network can have at most one instance of the Mechanism
Configuration block. If a model does not have the Mechanism
Configuration block, the uniform gravity applied to the mechanism is
zero.

If a Simscape
Multibody network contains a Gravitational
Field block, set the **Uniform Gravity** parameter of the
Mechanism Configuration block to
`None`.
