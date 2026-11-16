---
type: simulink-block
title: 'Weld Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'weldjoint'
documentation_source_path: 'ref/weldjoint.html'
language: en
---

# Weld Joint

## Ports

### Frame

### **B** — Base frame frame

Base frame of the joint block.

### **F** — Follower frame frame

Follower frame of the joint block.
### Input

#### Mode Configuration

### **mode** — Joint mode control physical signal

Input port that controls the mode of the joint. The signal must be a unitless
scalar. The joint mode is normal when the input signal is `0` and
disengaged when the input signal is `-1`. You can change the mode at
any time during the simulation.

The table shows how the position and velocity of the joint change during
transitions between modes.

| Transitions | Position | Velocity |
| --- | --- | --- |
| Normal to Disengaged | The joint position remains at zero but can change in any direction after the transition. | The joint velocity remains at zero but can change in any direction after the transition. |
| Disengaged to Normal | The joint positions become zero and remain constant after the transition. | The joint velocities become zero and remain constant after the transition. |

#### Dependencies

To enable this port, under **Mode Configuration**, set
**Mode** to `Provided by Input`.
### Output

#### Composite Force/Torque Sensing

### **fc** — Constraint force, N physical signal

Physical signal port that outputs the constraint forces that act across the joint.
These forces maintain the translational constraints of the joint. The output has a
3-by-1 vector format and represents the force components along the
`x`, `y`, and `z` axes of the
resolution frame. For more information, see Force and Torque Sensing.

#### Dependencies

To enable this port, under **Composite Force/Torque
Sensing**, select **Constraint Force**.

### **tc** — Constraint torque, N\*m physical signal

Physical signal port that outputs the constraint torques that act across the
joint. These torques maintain the rotational constraints of the joint. The output
has a 3-by-1 vector format and represents the torque components about the
`x`, `y`, and `z` axes of the
resolution frame. For more information, see Force and Torque Sensing.

#### Dependencies

To enable this port, under **Composite Force/Torque
Sensing**, select **Constraint Torque**.

### **ft** — Total force, N physical signal

Physical signal port that outputs the total force that acts across the joint. The
total force is the sum of the of all forces transmitted between the connected frames
through the joint. The output has a 3-by-1 vector format and represents the force
components along the `x`, `y`, and
`z` axes of the resolution frame.

To demonstrate the total force acting on a joint, the figure shows a model using a
Prismatic Joint block.

IIllustration of total force

The total force includes the actuator force
(*F*A), internal force
(*F*I), and constraint forces
(*F*C). For more information, see Force and Torque Sensing.

#### Dependencies

To enable this port, under **Composite Force/Torque
Sensing**, select **Total Force**.

### **tt** — Total torque, N\*m physical signal

Physical signal port that outputs the total torque that acts across the joint. The
total torque is the sum of all torques transmitted between the connected frames
through the joint. The torque includes the actuation, internal, limit, and
constraint torques. The output has a 3-by-1 vector format and represents the torque
components about the `x`, `y`, and
`z` axes of the resolution frame. For more information, see
Force and Torque Sensing.

#### Dependencies

To enable this port, under **Composite Force/Torque
Sensing**, select **Total Torque**.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Mode Configuration

### **Mode** — Joint mode `Normal` (default) | `Disengaged` | `Provided by Input`

Joint mode for the simulation, specified as one of these values:

| Mode | Description |
| --- | --- |
| `Normal` | Normal mode enables the joint constraints work as intended during the simulation. |
| `Disengaged` | Disengaged mode releases the joint from all constraints throughout the simulation. The settings for **Internal Mechanics**, **Limits**, and **Actuation** parameters do not affect the disengaged joint. All output ports output zero. |
| `Provided by Input` | The `Provided by Input` option allows you to specify the joint mode by using an input signal. For more information, see the port **mode** in the **Input** section. |

### Composite Force/Torque Sensing

### **Direction** — Measurement direction `Follower on Base` (default) | `Base on Follower`

Measurement direction, specified as one of these values:

- `Follower on Base` — The block senses the
  force and torque that the follower frame exerts on the base
  frame.
- `Base on Follower` — The block senses the
  force and torque that the base frame exerts on the follower
  frame.

This parameter affects only the output signals under the **Composite Force/Torque
Sensing** section. Reversing the direction changes the sign of the
measurements. For more information, see Force and Torque Measurement Direction.

### **Resolution Frame** — Frame used to resolve measurements `Base` (default) | `Follower`

Frame used to resolve the measurements, specified as one of these values:

- `Base` — The block resolves the measurements
  in the coordinates of the base frame.
- `Follower` — The block resolves the
  measurements in the coordinates of the follower frame.

This parameter affects only the output signals under the **Composite Force/Torque
Sensing** section.

## Libraries

Simscape / Multibody / Joints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

### R2025a: Model mode faults

You can now model mode faults for all the joint blocks. Using the faults, you can change
the joint modes during a simulation without changing the model design. For more information,
see the **Faults** section in the description.

## Description

Joint with zero primitives

This block represents a joint with zero degrees of freedom. It contains no joint
primitives. Base and follower frames, each connected to a separate rigid body, are coincident
for all time. The block dialog box provides sensing options for constraint and total forces
and torques.

**Joint Degrees of Freedom**

### Faults

Using mode faults, you can change the joint modes during a simulation without modifying
the model design. The fault injection overrides the mode setting. For example, if a joint
has the **Mode** parameter set to `Locked` and the
**Fault behavior** parameter set to `Disengaged`, the
joint becomes disengaged.

To add a mode fault to a joint block, click on the joint block, in the **Simscape Block** tab, and the **Faults**
section, click **Fault** > `Add Fault`.
Alternatively, you can click the joint block, hover over the ellipsis to open the action
bar, and click the Add a fault on the block icon Button to use to add a fault. You can add multiple faults to a joint block, but the
joint block can have only one active fault during a simulation.

As you add faults, in the Property Inspector, under the **Fault** section, specify the behavior and the trigger type of the fault. To
define the fault behavior, click the link next to the **Fault
Behavior**. This joint supports `Normal` or
`Disengaged` mode. The joint blocks support these trigger types:
`Always on`, `Timed`, `Manual`, and
`Conditional`. For more details of these trigger types, see Set Fault Triggers. To trigger a
conditional fault, you can use Simulink signals, Simscape language blocks, and MATLAB
workspace variables. To set the active fault for a block, use the Fault Table. For more
details, see Access the Fault Table and Fault Dashboard.

To enable fault simulation, in the **Simscape Block** tab
and the **Faults** section, turn on the **Fault Simulation** button. The fault simulation is on when the button is green
and the status is **on**. The simulation logs the trigger
status data. To view the data, use the Simulation Data
Inspector. Also, you can see the fault status and a summary of the triggered faults
in the Fault Dashboard. To open the Fault Dashboard, in the **Simscape
Block** tab, click **Faults** > `Fault
Dashboard`.

To create and modify faults, you can also use Simscape™ and Simulink® fault functions. For more details, see the function section of the Simulink Fault Controls and Simscape Faults Interface.
