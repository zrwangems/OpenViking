---
type: simulink-block
title: 'Universal Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'universaljoint'
documentation_source_path: 'ref/universaljoint.html'
language: en
---

# Universal Joint

## Ports

### Frame

### **B** — Base frame frame

Base frame of the joint block.

### **F** — Follower frame frame

Follower frame of the joint block.
### Input

#### X Revolute Primitive (Rx)

### **tx** — Actuation torque physical signal

Physical signal input port that accepts the actuation torque for the joint primitive. The
block applies this torque equally and oppositely
to both the base and follower frames of the joint
primitive. The torque is about the
*x*-axis of the base frame. The
*x*-axes of the follower and base
frames align with each other during
simulation.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Actuation**, set **Torque** to `Provided by Input`.

### **qx** — Motion profile physical signal

Physical signal input port that accepts the motion profile for the joint primitive. The block
uses this signal to determine the rotation of the follower frame with respect to the
base frame about the *x*-axis of the base frame. The signal must
also contain the first and second derivatives of the rotation.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Actuation**, set **Motion** to `Provided by Input`.

#### Y Revolute Primitive (Ry)

### **ty** — Actuation torque physical signal

Physical signal input port that accepts the actuation torque for the joint primitive. The
block applies this torque equally and oppositely
to both the base and follower frames of the joint
primitive. The torque is about the
*y*-axis of the base frame. The
*y*-axes of the follower and base
frames align with each other during
simulation.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Actuation**, set **Torque** to `Provided by Input`.

### **qy** — Motion profile physical signal

Physical signal input port that accepts the motion profile for the joint primitive. The block
uses this signal to determine the rotation of the follower frame with respect to the
base frame about the *y*-axis of the base frame. The signal must
also contain the first and second derivatives of the rotation.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Actuation**, set **Motion** to `Provided by Input`.

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

#### X Revolute Primitive (Rx)

### **qx** — Position of joint primitive physical signal

Physical signal port that outputs the position of the joint primitive. The value is the rotation angle of the follower frame with respect to the base frame about the *x*-axis of the base frame.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Position**.

### **wx** — Angular velocity of joint primitive physical signal

Physical signal port that outputs the angular velocity of the joint primitive. The value is the first derivative of the signal from the port **qx**.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Velocity**.

### **bx** — Angular acceleration of joint primitive physical signal

Physical signal port that outputs the angular acceleration of the joint primitive. The value is the second derivative of the signal from the port **qx**.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Acceleration**.

### **tx** — Actuator torque acting on joint primitive physical signal

Physical signal port that outputs the actuator torque acting on the joint primitive.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Actuator Torque**.

### **tllx** — Lower-limit torque acting on joint primitive physical signal

Physical signal port that outputs the lower-limit torque. The block applies this torque when the joint primitive position is less than the lower bound of the free region. The block applies this torque to both the base and follower frames of the joint primitive in order to accelerate the relative position back to the free region.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Lower-Limit Torque**.

### **tulx** — Upper-limit torque acting on joint primitive physical signal

Physical signal port that outputs the upper-limit torque. The block applies this torque when the joint primitive position exceeds the upper bound of the free region. The block applies this torque to both the base and follower frames of the joint primitive in order to accelerate the relative position back to the free region.

#### Dependencies

To enable this port, under **X Revolute Primitive (Rx)** >  **Sensing**, select **Upper-Limit Torque**.

#### Y Revolute Primitive (Ry)

### **qy** — Position of joint primitive physical signal

Physical signal port that outputs the position of the joint primitive. The value is the rotation angle of the follower frame with respect to the base frame about the *y*-axis of the base frame.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Position**.

### **wy** — Angular velocity of joint primitive physical signal

Physical signal port that outputs the angular velocity of the joint primitive. The value is the first derivative of the signal from the port **qy**.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Velocity**.

### **by** — Angular acceleration of joint primitive physical signal

Physical signal port that outputs the angular acceleration of the joint primitive. The value is the second derivative of the signal from the port **qy**.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Acceleration**.

### **ty** — Actuator torque acting on joint primitive physical signal

Physical signal port that outputs the actuator torque acting on the joint primitive.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Actuator Torque**.

### **tlly** — Lower-limit torque acting on joint primitive physical signal

Physical signal port that outputs the lower-limit torque. The block applies this torque when the joint primitive position is less than the lower bound of the free region. The block applies this torque to both the base and follower frames of the joint primitive in order to accelerate the relative position back to the free region.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Lower-Limit Torque**.

### **tuly** — Upper-limit torque acting on joint primitive physical signal

Physical signal port that outputs the upper-limit torque. The block applies this torque when the joint primitive position exceeds the upper bound of the free region. The block applies this torque to both the base and follower frames of the joint primitive in order to accelerate the relative position back to the free region.

#### Dependencies

To enable this port, under **Y Revolute Primitive (Ry)** >  **Sensing**, select **Upper-Limit Torque**.

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

### X Revolute Primitive (Rx)

#### State Targets

### **Specify Position Target** — Whether to specify position target `off` (default) | `on`

Select this parameter to specify the position target of the *x* revolute primitive.

### **Priority** — Priority level of position target `High (desired)` (default) | `Low (approximate)`

Priority level of the position target, specified as `High (desired)`
or `Low (approximate)`. For more information, see the
Guiding Assembly section of How Multibody Assembly Works..

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Value** — Position target 0 `deg` (default) | scalar

Position target of the *x* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Specify Velocity Target** — Whether to specify angular velocity target `off` (default) | `on`

Select this parameter to specify the angular velocity target for the *x* revolute primitive.

### **Priority** — Priority level of velocity target `High (desired)` (default) | `Low (approximate)`

Priority level of the angular velocity target, specified as `High
(desired)` or `Low (approximate)`. For
more information, see the Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Velocity Target**.

### **Value** — Velocity target 0 `deg/s` (default) | scalar

Angular velocity target of the *x* revolute primitive, specified as a scalar with a unit of angular velocity.

#### Dependencies

To enable this parameter, select **Specify Velocity Target**.

#### Internal Mechanics

### **Equilibrium Position** — Position where internal torque is zero 0 `deg` (default) | scalar

Position where the spring torque is zero, specified as a scalar with a unit of angle.

### **Spring Stiffness** — Stiffness of force law 0 `N*m/deg` (default) | scalar

Stiffness of the internal spring-damper force law for the *x* revolute primitive, specified as a scalar with a unit of torsional stiffness.

### **Damping Coefficient** — Damping coefficient of force law 0 `N*m/(deg/s)` (default) | scalar

Damping coefficient of the internal spring-damper force law for the *x* revolute primitive, specified as a scalar with a unit of damping coefficient.

#### Limits

### **Specify Lower Limit** — Whether to specify lower position limit `off` (default) | `on`

Select this parameter to specify the lower limit of the *x* revolute primitive.

### **Bound** — Lower bound of free region -90 `deg` (default) | scalar

Lower bound for the free region of the *x* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Spring Stiffness** — Stiffness of spring at lower bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the lower bound, specified as a scalar with a unit of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Damping Coefficient** — Damping coefficient at lower bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the lower bound, specified as a scalar with a unit of damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a unit of angle.

The block applies the full value of the lower-limit torque when the penetration reaches the
width of the transition region. The smaller the region, the sharper the onset of
forces and the smaller the time step required of the solver. In the tradeoff
between simulation accuracy and simulation speed, reducing the transition region
improves accuracy and expanding it improves speed.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Specify Upper Limit** — Whether to specify upper position limit `off` (default) | `on`

Select this parameter to specify the upper limit of the *x* revolute primitive.

### **Bound** — Upper bound of free region 90 `deg` (default) | scalar

Upper bound for the free region of the *x* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Spring Stiffness** — Stiffness of spring at upper bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the upper bound, specified as a scalar with a unit of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Damping Coefficient** — Damping coefficient at upper bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the upper bound, specified as a scalar with a unit of damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a unit of angle.

The block applies the full value of the upper-limit torque when the penetration reaches the
width of the transition region. The smaller the region, the sharper the onset of
forces and the smaller the time step required of the solver. In the tradeoff
between simulation accuracy and simulation speed, reducing the transition region
improves accuracy and expanding it improves speed.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

#### Actuation

### **Torque** — Option to provide actuator torque `None` (default) | `Provided by Input` | `Automatically Computed`

Option to provide the actuator torque for the joint primitive, specified as one of these values:

| Torque Setting | Description |
| --- | --- |
| `None` | No actuator torque. |
| `Provided by Input` | The input port **tx** specifies the actuator torque for the *x* revolute primitive. |
| `Automatically Computed` | The block computes the torque automatically. If you set this parameter to `Automatically Computed`, you do not need to set **Motion** to `Provided by Input` for the for the same joint primitive. The automatically computed torque may satisfy a motion input somewhere else in the mechanism. |

### **Motion** — Option to provide motion `Automatically Computed` (default) | `Provided by Input`

Option to provide the motion for the joint primitive, specified as one of these values:

| Motion Setting | Description |
| --- | --- |
| `Automatically computed` | The block computes and applies the joint primitive motion based on model dynamics. |
| `Provided by Input` | The input port **qx** specifies the motion for the *x* revolute primitive. |

### Y Revolute Primitive (Ry)

#### State Targets

### **Specify Position Target** — Whether to specify position target `off` (default) | `on`

Select this parameter to specify the position target of the *y* revolute primitive.

### **Priority** — Priority level of position target `High (desired)` (default) | `Low (approximate)`

Priority level of the position target, specified as `High (desired)`
or `Low (approximate)`. For more information, see the
Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Value** — Position target 0 `deg` (default) | scalar

Position target of the *y* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Specify Velocity Target** — Whether to specify angular velocity target `off` (default) | `on`

Select this parameter to specify the angular velocity target for the *y* revolute primitive.

### **Priority** — Priority level of velocity target `High (desired)` (default) | `Low (approximate)`

Priority level of the angular velocity target, specified as `High
(desired)` or `Low (approximate)`. For
more information, see the Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Velocity Target**.

### **Value** — Velocity target 0 `deg/s` (default) | scalar

Angular velocity target of the *y* revolute primitive, specified as a scalar with a unit of angular velocity.

#### Dependencies

To enable this parameter, select **Specify Velocity Target**.

#### Internal Mechanics

### **Equilibrium Position** — Position where internal torque is zero 0 `deg` (default) | scalar

Position where the spring torque is zero, specified as a scalar with a unit of angle.

### **Spring Stiffness** — Stiffness of force law 0 `N*m/deg` (default) | scalar

Stiffness of the internal spring-damper force law for the *y* revolute primitive, specified as a scalar with a unit of torsional stiffness.

### **Damping Coefficient** — Damping coefficient of force law 0 `N*m/(deg/s)` (default) | scalar

Damping coefficient of the internal spring-damper force law for the *y* revolute primitive, specified as a scalar with a unit of damping coefficient.

#### Limits

### **Specify Lower Limit** — Whether to specify lower position limit `off` (default) | `on`

Select this parameter to specify the lower limit of the *y* revolute primitive.

### **Bound** — Lower bound of free region -90 `deg` (default) | scalar

Lower bound for the free region of the *y* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Spring Stiffness** — Stiffness of spring at lower bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the lower bound, specified as a scalar with a unit of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Damping Coefficient** — Damping coefficient at lower bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the lower bound, specified as a scalar with a unit of damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a unit of angle.

The block applies the full value of the lower-limit torque when the penetration reaches the
width of the transition region. The smaller the region, the sharper the onset of
forces and the smaller the time step required of the solver. In the tradeoff
between simulation accuracy and simulation speed, reducing the transition region
improves accuracy and expanding it improves speed.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Specify Upper Limit** — Whether to specify upper position limit `off` (default) | `on`

Select this parameter to specify the upper limit of the *y* revolute primitive.

### **Bound** — Upper bound of free region 90 `deg` (default) | scalar

Upper bound for the free region of the *y* revolute primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Spring Stiffness** — Stiffness of spring at upper bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the upper bound, specified as a scalar with a unit of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Damping Coefficient** — Damping coefficient at upper bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the upper bound, specified as a scalar with a unit of damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a unit of angle.

The block applies the full value of the upper-limit torque when the penetration reaches the
width of the transition region. The smaller the region, the sharper the onset of
forces and the smaller the time step required of the solver. In the tradeoff
between simulation accuracy and simulation speed, reducing the transition region
improves accuracy and expanding it improves speed.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

#### Actuation

### **Torque** — Option to provide actuator torque `None` (default) | `Provided by Input` | `Automatically Computed`

Option to provide the actuator torque for the joint primitive, specified as one of these values:

| Torque Setting | Description |
| --- | --- |
| `None` | No actuator torque. |
| `Provided by Input` | The input port **ty** specifies the actuator torque for the *y* revolute primitive. |
| `Automatically Computed` | The block computes the torque automatically. If you set this parameter to `Automatically Computed`, you do not need to set **Motion** to `Provided by Input` for the for the same joint primitive. The automatically computed torque may satisfy a motion input somewhere else in the mechanism. |

### **Motion** — Option to provide motion `Automatically Computed` (default) | `Provided by Input`

Option to provide the motion for the joint primitive, specified as one of these values:

| Motion Setting | Description |
| --- | --- |
| `Automatically computed` | The block computes and applies the joint primitive motion based on model dynamics. |
| `Provided by Input` | The input port **qy** specifies the motion for the *y* revolute primitive. |

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

You can now model mode faults for all the joint blocks. Using the faults, you can change
the joint modes during a simulation without changing the model design. For more information,
see the **Faults** section in the description.

## Description

Joint that allows for transfer of rotary motion between unaligned shafts

The Universal Joint block models a coupling between two
spinning shafts. The two shafts align with the *z*-axes of
the base and follower frames and rotate at the same average angular velocity. However, the
relative velocities of the shafts fluctuate if the shafts are not aligned. The fluctuation
increases as the bend angle increases. This joint constrains the origins of the two frames to
be coincident.

The joint has two revolute primitives that represent two sequential rotations. The
rotations specify the orientation of the follower frame with respect to the base frame. The
first rotation is about the *x*-axis of the follower frame,
and the second rotation is about the *y*-axis of the follower
frame generated after the first rotation, as shown in the image.

Illustration of the transformation sequence

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
