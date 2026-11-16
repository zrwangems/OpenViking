---
type: simulink-block
title: 'External Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'externalforceandtorque'
documentation_source_path: 'ref/externalforceandtorque.html'
language: en
---

# External Force and Torque

## Ports

### Frame

### **F** — Follower frame frame

Follower frame at which the external forces and torques apply.
### Input

#### Force

### **fx** — External force along *x*-axis physical signal

Physical signal port that accepts the external force in the
*x*-direction of the force resolution frame. The input signal is a
scalar that can vary over time.

This signal is independent of the *x*-component inputs at the
**f** port. When you provide signals to both this port and the
**f** port, the external force in the
*x*-direction equals the sum of these inputs.

#### Dependencies

To enable this port, under **Force**, select **Force
(X)**.

### **fy** — External force along *y*-axis physical signal

Physical signal port that accepts the external force in the
*y*-direction of the force resolution frame. The input signal is a
scalar that can vary over time.

This signal is independent of the *y*-component inputs at the
**f** port. When you provide signals to both this port and the
**f** port, the external force in the
*y*-direction equals the sum of these inputs.

#### Dependencies

To enable this port, under **Force**, select **Force
(Y)**.

### **fz** — External force along *z*-axis physical signal

Physical signal port that accepts the external force in the
*z*-direction of the force resolution frame. The input signal is a
scalar that can vary over time.

This signal is independent of the *z*-component inputs at the
**f** port. When you provide signals to both this port and the
**f** port, the external force in the
*z*-direction equals the sum of these inputs.

#### Dependencies

To enable this port, under **Force**, select **Force
(Z)**.

### **f** — External force vector physical signal

Physical signal port that accepts the external force. The input signal is a 1-by-3
or 3-by-1 vector, [*Fx*
*Fy*
*Fz*], that can vary over time. This signal is
independent of the inputs to the **fx**, **fy**, and
**fz** ports. If you provide signals to both the
**f** port and the **fx**,
**fy**, and **fz** ports, the input force becomes
the sum of all inputs.

#### Dependencies

To enable this port, under **Force**, select
**Force**.

#### Torque

### **tx** — External torque about *x*-axis physical signal

Physical signal port that accepts the external torque about the
*x*-axis of the torque resolution frame. The input signal is a
scalar that can vary over time.

#### Dependencies

To enable this port, under **Torque**, select **Torque
(X)**.

### **ty** — External torque about *y*-axis physical signal

Physical signal port that accepts the external torque about the
*y*-axis of the torque resolution frame. The input signal is a
scalar that can vary over time.

#### Dependencies

To enable this port, under **Torque**, select **Torque
(Y)**.

### **tz** — External torque about *z*-axis physical signal

Physical signal port that accepts the external torque about the
*z*-axis of the torque resolution frame. The input signal is a
scalar that can vary over time.

#### Dependencies

To enable this port, under **Torque**, select **Torque
(Z)**.

### **t** — External torque vector physical signal

Physical signal port that accepts the external torque. The input signal is a
1-by-3 or 3-by-1 vector, [*Tx*
*Ty*
*Tz*], that can vary over time.

#### Dependencies

To enable this port, under **Torque**, select
**Torque**.

## Parameters

#### Force

### **Force Resolution Frame** — Frame to use to resolve each force input `Attached Frame` (default) | `World`

Frame used to resolve the force inputs, specified as:

- `Attached Frame` — The block resolves the inputs in the
  frame that connects to the follower frame of the External Force and
  Torque block.
- `World` — The block resolves the inputs in the world
  frame of the model.

#### Torque

### **Torque Resolution Frame** — Frame to use to resolve each torque input `Attached Frame` (default) | `World`

Frame used to resolve the torque inputs, specified as:

- `Attached Frame` — The block resolves the inputs in the
  frame that connects to the follower frame of the External Force and
  Torque block.
- `World` — The block resolves the inputs in the world
  frame of the model.

## Libraries

Simscape / Multibody / Forces and Torques

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Apply external force and/or torque to connected frame

The External Force and Torque block applies the external
force and/or torque to the frame that connects to the **F** port of the
block. The forces act at the origin of the frame and the torques act about the corresponding
axes of the frame. The block accepts physical signals to specify the forces and torques. The
signal can be a constant or time-varying value throughout a simulation.

You can specify the resolution frame to resolve the force and torque inputs. A force input
with a positive value acts along the positive direction of the associated frame axis. A torque
input with a positive value acts about the associated frame axis according to the right-hand
rule.
