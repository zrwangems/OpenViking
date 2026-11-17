---
type: simulink-block
title: 'Translational Multibody Interface'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Multibody Interfaces'
documentation_page: 'translationalmultibodyinterface'
documentation_source_path: 'ref/translationalmultibodyinterface.html'
language: en
---

# Translational Multibody Interface

## Ports
```yaml
ports:
- name: v
  summary: Relative velocity, m/s physical signal
  direction: input
- name: f
  summary: Force, N physical signal
  direction: output
- name: R
  summary: Rod mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Input

### **v** — Relative velocity, m/s physical signal

Physical signal input port that accepts the relative velocity sensing output from
the joint primitive. Connect this port to the velocity sensing port
**v** of the Simscape
Multibody joint.
### Output

### **f** — Force, N physical signal

Physical signal output port that provides the force actuation input to the joint
primitive. Connect this port to the force actuation port **f** of the
Simscape
Multibody joint.
### Conserving

### **R** — Rod mechanical translational

Mechanical translational conserving port with the same force and relative velocity
as the joint primitive. Connect this port to ports **R** of other
blocks in the mechanical translational network.

### **C** — Case mechanical translational

Mechanical translational conserving port with the same force and relative velocity
as the joint primitive. Connect this port to ports **C** of other
blocks in the mechanical translational network.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Mechanical / Multibody Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Interface between mechanical translational networks and Simscape Multibody joints

The Translational Multibody Interface block implements an
intuitive way to connect Simscape™ blocks that have mechanical translational ports with Simscape
Multibody™ joints that have prismatic primitives. Simscape blocks that can be connected to a Translational Multibody
Interface block include:

- Blocks from the Foundation > Mechanical > Translational Elements library, such as
  Translational Friction or Translational
  Damper.
- Blocks with mechanical translational ports from other Foundation libraries, such as
  Translational Mechanical Converter (G) or
  Translational Mechanical Converter (IL).
- Blocks with mechanical translational ports from add-on products, such as hydraulic
  actuators from the Simscape
  Fluids™ libraries.

The Translational Multibody Interface block matches the
force and relative velocity across the interface. You can connect it to any Simscape
Multibody joint that has a prismatic primitive:

1. Enable the velocity sensing port **v** and the force actuation port
   **f** on the joint. If the joint has multiple degrees of freedom, make
   sure that the selected velocity sensing and force actuation correspond to the same degree
   of freedom.
2. Connect physical signal ports **v** and **f** of
   the Translational Multibody Interface block to ports
   **v** and **f** of the Simscape
   Multibody joint.
3. Connect ports **C** and **R** of the
   Translational Multibody Interface block to a Simscape mechanical translational network.

Block diagram showing how to connect the Translational Multibody Interface block

For detailed step-by-step instructions, see Connecting Simscape Networks to Simscape Multibody Joints.

Blocks like Translational Friction and
Translational Damper do not require position information, and
for these blocks the interface based on force and relative velocity is sufficient. Other
blocks, like hydraulic actuators, require information on relative position between their
ports. To connect these blocks to a Simscape
Multibody joint:

1. Use the Translational Multibody Interface block. Enable
   the velocity sensing port **v** and the force actuation port
   **f** on the joint, and connect the ports as described above.
2. Additionally, enable the position sensing port **p** on the joint. If
   the joint has multiple degrees of freedom, make sure that the position and velocity
   sensing and force actuation all correspond to the same degree of freedom.
3. On the actuator block, enable the position input port **p**, by
   setting the **Interface displacement** parameter to `Provide
   input signal from Multibody joint`. Connect the position input port
   **p** on the actuator block to the position sensing port
   **p** of the Simscape
   Multibody joint.

Block diagram showing how to connect the Translational Multibody Interface block and pass the position information

### Assumptions and Limitations

For models with Translational Multibody Interface or Rotational Multibody Interface blocks, it is recommended that you use Simscape
Multibody blocks to model masses and inertias. The reason is that Simscape networks need to have a ground (reference) node, with all the masses and inertias in the network accelerating with respect to this node. In a Simscape
Multibody joint, both the base and follower frames may be accelerating. Therefore, a mass or inertia in the Simscape network connected to a joint may not have the correct inertial reference.
