---
type: simulink-block
title: 'Prismatic Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'prismaticjoint'
documentation_source_path: 'ref/prismaticjoint.html'
language: en
---

# Prismatic Joint

## Ports
```yaml
ports:
- name: B
  summary: Base frame frame
  direction: input
- name: F
  summary: Follower frame frame
  direction: input
- name: f
  summary: Actuation force physical signal
  direction: input
- name: p
  summary: Motion profile physical signal
  direction: input
- name: mode
  summary: Joint mode control physical signal
  direction: input
- name: p
  summary: Position of primitive physical signal
  direction: output
- name: v
  summary: Velocity of primitive physical signal
  direction: output
- name: a
  summary: Acceleration of primitive physical signal
  direction: output
- name: f
  summary: Actuator force acting on joint primitive physical signal
  direction: output
- name: fll
  summary: Lower-limit force physical signal
  direction: output
- name: ful
  summary: Upper-limit force physical signal
  direction: output
- name: fc
  summary: Constraint force, N physical signal
  direction: output
- name: tc
  summary: Constraint torque, N\*m physical signal
  direction: output
- name: ft
  summary: Total force, N physical signal
  direction: output
- name: tt
  summary: Total torque, N\*m physical signal
  direction: output
```

### Frame

### **B** — Base frame frame

Base frame of the joint block.

### **F** — Follower frame frame

Follower frame of the joint block.
### Input

### **f** — Actuation force physical signal

Physical signal input port that accepts the actuation force for the
joint primitive. The signal provides the value of the force that applies
on both the base and follower frames of the joint primitive.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Actuation**, set **Force** to `Provided
by Input`.

### **p** — Motion profile physical signal

Physical signal input port that accepts the motion profile for the
joint primitive. The signal provides the displacement of the follower
frame with respect to the base frame along the joint primitive axis.
Note that the signal must also contain the first and second derivatives
of the displacement.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Actuation**, set **Motion** to `Provided
by Input`.

#### Mode Configuration

### **mode** — Joint mode control physical signal

Input port that controls the mode of the joint. The signal must be a unitless scalar. The
joint mode is normal when the input signal is `0`, disengaged when
the input signal is `-1`, and locked when the input signal is
`1`. You can change the mode at any time during the
simulation.

The table shows how the position and velocity of the joint change during
transitions between modes.

| Transitions | Position | Velocity |
| --- | --- | --- |
| Normal to Locked | The joint position retains the current value and remains constant after the transition. | The joint velocity becomes zero and remains constant after the transition. |
| Normal to Disengaged | The joint position retains the current value but can change in any direction after the transition. | The joint velocity retains the current value but can change in any direction after the transition. |
| Locked to Normal | The joint position retains the current value but can change in the directions aligned with the joint degrees of freedom (DOFs) after the transition. | The joint velocity remains at zero but can change in the directions aligned with the joint DOFs after the transition. |
| Locked to Disengaged | The joint position retains the current value but can change in any direction after the transition. | The joint velocity remains at zero but can change in any direction after the transition. |
| Disengaged to Normal | For the directions aligned with the joint DOFs, the joint positions initially take values calculated by using Newton's method and can change thereafter. In the constrained directions, the joint positions become zero and remain constant after the transition. | For the directions aligned with the joint DOFs, the joint velocities initially take values calculated by using Newton's method and can change thereafter. In the constrained directions, the joint velocities become zero and remain constant after the transition. |
| Disengaged to Locked | For the directions aligned with the joint DOFs, the joint positions initially take values calculated by using Newton's method and remain constant after the transition. In the constrained directions, the joint positions become zero and remain constant after the transition. | The joint velocity becomes zero and remains constant after the transition. |

#### Dependencies

To enable this port, under **Mode Configuration**, set **Mode** to `Provided by Input`.
### Output

### **p** — Position of primitive physical signal

Physical signal port that outputs the position of the primitive. The
value is the displacement of the follower frame with respect to the base
frame.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Position**.

### **v** — Velocity of primitive physical signal

Physical signal port that outputs the velocity of the
primitive.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Velocity**.

### **a** — Acceleration of primitive physical signal

Physical signal port that outputs the acceleration of the
primitive.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Acceleration**.

### **f** — Actuator force acting on joint primitive physical signal

Physical signal port that outputs the actuator force acting on the
joint primitive.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Actuator Force**.

### **fll** — Lower-limit force physical signal

Physical signal port that outputs the lower-limit force. The block
applies the force when the joint primitive position is less than the
lower bound of the free region. The force applies to both the base and
follower frames of the joint primitive to accelerate the position back
to the free region.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Lower-Limit Force**.

### **ful** — Upper-limit force physical signal

Physical signal port that outputs the upper-limit force. The block
applies the force when the joint primitive position exceeds the upper
bound of the free region. The force applies to both the base and
follower frames of the joint primitive to accelerate the position back
to the free region.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Upper-Limit Force**.

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
```yaml
parameters:
- name: State Targets > Specify Position Target
  summary: Whether to specify position target off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: State Targets > Specify Position Target > Priority
  summary: Priority level of position target High (desired) (default) | Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: State Targets > Specify Position Target > Value
  summary: Position target 0 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: State Targets > Specify Velocity Target
  summary: Whether to specify velocity target off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: State Targets > Specify Velocity Target > Priority
  summary: Priority level of velocity target High (desired) (default) | Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: State Targets > Specify Velocity Target > Value
  summary: Velocity target of joint primitive 0 m/s (default) | scalar in units of linear velocity
  group: Z Prismatic Primitive (Pz)
- name: Internal Mechanics > Equilibrium Position
  summary: Position where internal force is zero 0 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: Internal Mechanics > Spring Stiffness
  summary: Stiffness of force law 0 N/m (default) | scalar in units of linear stiffness
  group: Z Prismatic Primitive (Pz)
- name: Internal Mechanics > Damping Coefficient
  summary: Damping coefficient of force law 0 N(m/s) (default) | scalar in units of linear damping coefficient
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Lower Limit
  summary: Whether to specify lower position limit off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Lower Limit > Bound
  summary: Lower bound of free region -1 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Lower Limit > Spring Stiffness
  summary: Stiffness of spring at lower bound 1e6 N/m (default) | scalar in units of linear stiffness
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Lower Limit > Damping Coefficient
  summary: Damping coefficient at lower bound 1e3 N/(m/s) (default) | scalar in units of linear damping coefficient
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Lower Limit > Transition Region Width
  summary: Region to smooth spring and damper forces 1e-4 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Upper Limit
  summary: Whether to specify upper position limit off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Upper Limit > Bound
  summary: Upper bound of free region 1 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Upper Limit > Spring Stiffness
  summary: Stiffness of spring at upper bound 1e6 N/m (default) | scalar in units of linear stiffness
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Upper Limit > Damping Coefficient
  summary: Damping coefficient at upper bound 1e3 N/(m/s) (default) | scalar in units of linear damping coefficient
  group: Z Prismatic Primitive (Pz)
- name: Limits > Specify Upper Limit > Transition Region Width
  summary: Region to smooth spring and damper forces 1e-4 m (default) | scalar in units of length
  group: Z Prismatic Primitive (Pz)
- name: Actuation > Force
  summary: Option to provide actuation force None (default) | Provided by Input | Automatically Computed
  group: Z Prismatic Primitive (Pz)
- name: Actuation > Motion
  summary: Option to provide actuation motion Automatically Computed (default) | Provided by Input
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Position
  summary: Whether to sense joint primitive position off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Velocity
  summary: Whether to sense joint primitive velocity off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Acceleration
  summary: Whether to sense joint primitive acceleration off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Actuator Force
  summary: Whether to sense joint actuator force off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Lower-Limit force
  summary: Whether sense to lower-limit force off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Sensing > Upper-Limit force
  summary: Whether sense to upper-limit force off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Mode
  summary: Joint mode Normal (default) | Locked | Disengaged | Provided by Input
  group: Mode Configuration
- name: Direction
  summary: Measurement direction Follower on Base (default) | Base on Follower
  group: Composite Force/Torque Sensing
- name: Resolution Frame
  summary: Frame used to resolve measurements Base (default) | Follower
  group: Composite Force/Torque Sensing
```

### Z Prismatic Primitive (Pz)

### **State Targets > Specify Position Target** — Whether to specify position target `off` (default) | `on`

Select this parameter to enable parameters that specify the position
target of the joint primitive.

### **State Targets > Specify Position Target > Priority** — Priority level of position target `High (desired)` (default) | `Low (approximate)`

Priority level of the position target, specified as `High
(desired)` or `Low
(approximate)`.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **State Targets**, select **Specify Position
Target**.

### **State Targets > Specify Position Target > Value** — Position target 0 `m` (default) | scalar in units of length

Position target of the joint primitive, specified as a scalar in units
of length.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **State Targets**, select **Specify Position
Target**.

### **State Targets > Specify Velocity Target** — Whether to specify velocity target `off` (default) | `on`

Select this parameter to enable parameters that specify the velocity
target of the joint primitive.

### **State Targets > Specify Velocity Target > Priority** — Priority level of velocity target `High (desired)` (default) | `Low (approximate)`

Priority level of the velocity target, specified as `High
(desired)` or `Low
(approximate)`.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **State Targets**, select **Specify Velocity
Target**.

### **State Targets > Specify Velocity Target > Value** — Velocity target of joint primitive 0 `m/s` (default) | scalar in units of linear velocity

Velocity target of the joint primitive, specified as a scalar in a
unit of linear velocity.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **State Targets**, select **Specify Velocity
Target**.

### **Internal Mechanics > Equilibrium Position** — Position where internal force is zero 0 `m` (default) | scalar in units of length

Position where the spring force is zero, specified as a scalar in
units of length. The value specifies the position of the
primitive.

### **Internal Mechanics > Spring Stiffness** — Stiffness of force law 0 `N/m` (default) | scalar in units of linear stiffness

Stiffness of the internal spring-damper force law for the joint
primitive, specified as a scalar in units of linear stiffness.

### **Internal Mechanics > Damping Coefficient** — Damping coefficient of force law 0 `N(m/s)` (default) | scalar in units of linear damping coefficient

Damping coefficient of the internal spring-damper force law for the
joint primitive, specified as a scalar in units of linear damping
coefficient.

### **Limits > Specify Lower Limit** — Whether to specify lower position limit `off` (default) | `on`

Select this parameter to enable parameters that specify the lower
limit of the joint primitive.

### **Limits > Specify Lower Limit > Bound** — Lower bound of free region -1 `m` (default) | scalar in units of length

Lower bound of the free region of the joint primitive, specified as a
scalar in units of length.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Lower
Limit**.

### **Limits > Specify Lower Limit > Spring Stiffness** — Stiffness of spring at lower bound 1e6 `N/m` (default) | scalar in units of linear stiffness

Stiffness of the spring at the lower bound, specified as a scalar in
units of linear stiffness.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Lower
Limit**.

### **Limits > Specify Lower Limit > Damping Coefficient** — Damping coefficient at lower bound 1e3 `N/(m/s)` (default) | scalar in units of linear damping coefficient

Damping coefficient at the lower bound, specified as a scalar in units
of linear damping coefficient.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Lower
Limit**.

### **Limits > Specify Lower Limit > Transition Region Width** — Region to smooth spring and damper forces 1e-4 `m` (default) | scalar in units of length

Region to smooth the spring and damper forces, specified as a scalar
in units of length.

The block applies the full value of this force when the penetration
reaches the width of the transition region. The smaller the region, the
sharper the onset of forces and the smaller the time step required of
the solver. In the tradeoff between simulation accuracy and simulation
speed, reducing the transition region improves accuracy while expanding
it improves speed.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Lower
Limit**.

### **Limits > Specify Upper Limit** — Whether to specify upper position limit `off` (default) | `on`

Select this parameter to enable parameters for specifying the upper
limit of the joint primitive.

### **Limits > Specify Upper Limit > Bound** — Upper bound of free region 1 `m` (default) | scalar in units of length

Upper bound for the free region of the joint primitive, specified as a
scalar in units of length.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Upper
Limit**.

### **Limits > Specify Upper Limit > Spring Stiffness** — Stiffness of spring at upper bound 1e6 `N/m` (default) | scalar in units of linear stiffness

Stiffness of the spring at the upper bound, specified as a scalar in
units of stiffness.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Upper
Limit**.

### **Limits > Specify Upper Limit > Damping Coefficient** — Damping coefficient at upper bound 1e3 `N/(m/s)` (default) | scalar in units of linear damping coefficient

Damping coefficient at the upper bound, specified as a scalar in units
of linear damping coefficient.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Upper
Limit**.

### **Limits > Specify Upper Limit > Transition Region Width** — Region to smooth spring and damper forces 1e-4 `m` (default) | scalar in units of length

Region to smooth the spring and damper forces, specified as a scalar
in units of length.

The block applies the full value of this force when the penetration
reaches the width of the transition region. The smaller the region, the
sharper the onset of forces and the smaller the time step required of
the solver. In the tradeoff between simulation accuracy and simulation
speed, reducing the transition region improves accuracy while expanding
it improves speed.

#### Dependencies

To enable this parameter, under **Z Prismatic Primitive (Pz)** > **Limits**, select **Specify Upper
Limit**.

### **Actuation > Force** — Option to provide actuation force `None` (default) | `Provided by Input` | `Automatically Computed`

Option to provide the actuation force for the joint primitive,
specified as the values in the table.

| Actuation Force Setting | Description |
| --- | --- |
| `None` | No actuation force. |
| `Provided by Input` | Input port **f** specifies the actuation force for the joint primitive.. |
| `Automatically computed` | The block automatically calculates the amount of force required to satisfy the motion inputs to the mechanism. Note that if you set this parameter to `Automatically computed`, it doesn’t mean that you must use `Provided by Input` for the **Motion** parameter for the same joint primitive. The automatically computed force could be to satisfy a motion input somewhere else in the mechanism. |

### **Actuation > Motion** — Option to provide actuation motion `Automatically Computed` (default) | `Provided by Input`

Option to provide the actuation motion for the joint primitive,
specified as the values in the table.

| Actuation Motion Setting | Description |
| --- | --- |
| `Automatically computed` | The block computes and applies the joint primitive motion based on model dynamics. |
| `Provided by Input` | Input port **p** specifies the actuation motion for the joint primitive. |

### **Sensing > Position** — Whether to sense joint primitive position off (default) | on

Select this parameter to enable the output port
**p**.

### **Sensing > Velocity** — Whether to sense joint primitive velocity off (default) | on

Select this parameter to enable port **v**.

### **Sensing > Acceleration** — Whether to sense joint primitive acceleration off (default) | on

Select this parameter to enable port **a**.

### **Sensing > Actuator Force** — Whether to sense joint actuator force off (default) | on

Select this parameter to enable port **f**.

### **Sensing > Lower-Limit force** — Whether sense to lower-limit force off (default) | on

Select this parameter to enable port **fll**.

### **Sensing > Upper-Limit force** — Whether sense to upper-limit force off (default) | on

Select this parameter to enable port **ful**.

### Mode Configuration

### **Mode** — Joint mode `Normal` (default) | `Locked` | `Disengaged` | `Provided by Input`

Joint mode for the simulation, specified as one of these values:

| Mode | Description |
| --- | --- |
| `Locked` | Locked mode constrains all the degrees of freedom (DOFs) for the joint. The locked joint maintains its initial assembly position with zero velocity during the simulation. The joint block can sense forces or torques in accordance with the settings of the **Internal Mechanics**, **Limits**, and **Actuation** parameters. |
| `Normal` | Normal mode enables the DOFs and the constraints of the joint work as intended during the simulation. |
| `Disengaged` | Disengaged mode releases the joint from all constraints throughout the simulation. The settings for **Internal Mechanics**,**Limits**, and **Actuation** parameters do not affect the disengaged joint. All output ports output zero. |
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

You can now model mode faults for all the joint blocks. Using the faults, you can
change the joint modes during a simulation without changing the model design. For
more information, see the **Faults** section in the
description.

## Description

Joint that allows relative motion along single axis

The Prismatic Joint block models a connection that
limits the relative motion between two frames to one translational degree of freedom.
This type of motion is common in hydraulic or pneumatic cylinders.

Degrees of Freedom for Prismatic Joint

The Prismatic Joint block has only one prismatic
primitive, which is along the *z*-axis of the base frame. During
simulation, the *z*-axes of the base and follower frames align, and
the follower frame moves with respect to the base frame along the
*z*-axis, as shown in the image.

Prismatic Primitive of a Prismatic Joint

Meanwhile, the *x* and *y* axes of the follower
frame remain parallel to the *x* and *y* axes of
the base frame, respectively.

To specify the target of the initial state for a joint primitive, use the parameters under
**State Targets**. The targets are specified in the base frame. You can
also set the priority levels for the targets. If the joint is not able to satisfy all the
state targets, the priority level determines which targets to satisfy first and how closely
to satisfy them. For an example, see the Guiding Assembly section of How Multibody Assembly Works.

To model damping and the spring behavior for a joint primitive, use the parameters under
**Internal Mechanics**. Use the **Damping
Coefficient** parameter to model energy dissipation and the **Spring
Stiffness** parameter to model energy storage. Joint springs attempt to
displace the joint primitive from its equilibrium position, and joint dampers act as energy
dissipation elements. The springs and dampers are strictly linear.

To specify the limits of a joint primitive, use the parameters under
**Limits**. The lower and upper bounds define the width of the free
region. The block applies a force to accelerate the joint position back to the free region
when the position exceeds the bounds. The block uses a smoothed spring-damper method to
compute the force. For more information about the smoothed spring-damper method, see the
Description section of the
Spatial Contact
Force block.

The **Force**, **Torque**, and **Motion**
parameters in the **Actuation** section control the motion of the joint
primitives during simulation. For more information, see Specifying Joint Actuation Inputs.
Additionally, the joint block has ports that output sensing data, such as position,
velocity, acceleration, force, and torque, that you can use to perform analytical tasks on a
model. For more information, see Sensing and Force and Torque Sensing.

To specify the joint mode configuration, use the **Mode** parameter. For
more details, see **Mode Configuration** under the
**Ports** and **Parameters** sections.

### Faults

Using mode faults, you can change the joint modes during a simulation without modifying the
model design. The fault injection overrides the mode setting. For example, if a joint has
the **Mode** parameter set to `Locked` and the
**Fault behavior** parameter set to `Disengaged`, the
joint becomes disengaged.

To add a mode fault to a joint block, click on the joint block, in the **Simscape Block** tab, and the **Faults** section,
click **Fault** > `Add Fault`.
Alternatively, you can click the joint block, hover over the ellipsis to open the action
bar, and click the Add a fault on the block icon Button to use to add a fault. You can add multiple faults to a joint block, but the
joint block can have only one active fault during a simulation.

As you add faults, in the Property Inspector, under the **Fault**
section, specify the behavior and the trigger type of the fault. To define the fault
behavior, click the link next to the **Fault Behavior**. This
joint supports `Locked`, `Normal`, or
`Disengaged` mode. The joint blocks support these trigger types:
`Always on`, `Timed`, `Manual`, and
`Conditional`. For more details of these trigger types, see Set Fault Triggers. To trigger a
conditional fault, you can use Simulink signals, Simscape language blocks, and MATLAB
workspace variables. To set the active fault for a block, use the Fault Table. For more
details, see Access the Fault Table and Fault Dashboard.

To enable fault simulation, in the **Simscape Block** tab and
the **Faults** section, turn on the **Fault
Simulation** button. The fault simulation is on when the button is green and
the status is **on**. The simulation logs the trigger status
data. To view the data, use the Simulation Data
Inspector. Also, you can see the fault status and a summary of the triggered
faults in the Fault Dashboard. To open the Fault Dashboard, in the **Simscape Block** tab, click **Faults** >
`Fault Dashboard`.

To create and modify faults, you can also use Simscape™ and Simulink® fault functions. For more details, see the function section of the Simulink Fault Controls and Simscape Faults Interface.
