---
type: simulink-block
title: 'Rotational Multibody Interface'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Simscape Mechanical Interfaces'
documentation_page: 'rotationalmultibodyinterface'
documentation_source_path: '../simscape/ref/rotationalmultibodyinterface.html'
language: en
---

# Rotational Multibody Interface

## Ports

### Input

### **w** — Relative angular velocity, rad/s physical signal

Physical signal input port that accepts the relative angular velocity sensing
output from the joint primitive. Connect this port to the velocity sensing port
**w** of the Simscape
Multibody joint.
### Output

### **t** — Torque, N\*m physical signal

Physical signal output port that provides the torque actuation input to the joint
primitive. Connect this port to the torque actuation port **t** of
the Simscape
Multibody joint.
### Conserving

### **R** — Rod mechanical rotational

Mechanical rotational conserving port with the same torque and relative angular
velocity as the joint primitive. Connect this port to ports **R** of
other blocks in the mechanical rotational network.

### **C** — Case mechanical rotational

Mechanical rotational conserving port with the same torque and relative angular
velocity as the joint primitive. Connect this port to ports **C** of
other blocks in the mechanical rotational network.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Mechanical / Multibody Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Interface between mechanical rotational networks and Simscape Multibody joints

The Rotational Multibody Interface block implements an
intuitive way to connect Simscape™ blocks that have mechanical rotational ports with Simscape
Multibody™ joints that have revolute primitives. Simscape blocks that can be connected to a Rotational Multibody
Interface block include:

- Blocks from the Foundation > Mechanical > Rotational Elements library, such as
  Rotational Friction or Rotational
  Damper.
- Blocks with mechanical rotational ports from other Foundation libraries, such as
  Rotational Mechanical Converter (G) or
  Rotational Mechanical Converter (IL).
- Blocks with mechanical rotational ports from add-on products, such as hydraulic
  actuators from the Simscape
  Fluids™ libraries.

The Rotational Multibody Interface block matches the torque
and relative angular velocity across the interface. You can connect it to any Simscape
Multibody joint that has a revolute primitive:

1. Enable the velocity sensing port **w** and the torque actuation port
   **t** on the joint. If the joint has multiple degrees of freedom, make
   sure that the selected velocity sensing and torque actuation correspond to the same degree
   of freedom.
2. Connect physical signal ports **w** and **t** of the
   Rotational Multibody Interface block to ports
   **w** and **t** of the Simscape
   Multibody joint.
3. Connect ports **C** and **R** of the
   Rotational Multibody Interface block to a Simscape mechanical rotational network.

Block diagram showing how to connect the Rotational Multibody Interface block

For detailed step-by-step instructions, see Connecting Simscape Networks to Simscape Multibody Joints.

Blocks like Rotational Friction and
Rotational Damper do not require position information, and
for these blocks the interface based on torque and relative angular velocity is sufficient.
Other blocks, like hydraulic actuators, require information on relative position between their
ports. To connect these blocks to a Simscape
Multibody joint:

1. Use the Rotational Multibody Interface block. Enable
   the velocity sensing port **w** and the torque actuation port
   **t** on the joint, and connect the ports as described above.
2. Additionally, enable the position sensing port **q** on the joint. If
   the joint has multiple degrees of freedom, make sure that the position and velocity
   sensing and torque actuation all correspond to the same degree of freedom.
3. On the actuator block, enable the position input port **q**, by
   setting the **Interface rotation** parameter to `Provide
   input signal from Multibody joint`. Connect the position input port
   **q** on the actuator block to the position sensing port
   **q** of the Simscape
   Multibody joint.

Block diagram showing how to connect the Rotational Multibody Interface block and pass the position information

### Assumptions and Limitations

For models with Translational Multibody Interface or Rotational Multibody Interface blocks, it is recommended that you use Simscape
Multibody blocks to model masses and inertias. The reason is that Simscape networks need to have a ground (reference) node, with all the masses and inertias in the network accelerating with respect to this node. In a Simscape
Multibody joint, both the base and follower frames may be accelerating. Therefore, a mass or inertia in the Simscape network connected to a joint may not have the correct inertial reference.
