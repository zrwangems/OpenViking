---
type: simulink-block
title: 'Bearing Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'bearingjoint'
documentation_source_path: 'ref/bearingjoint.html'
language: en
---

# Bearing Joint

## Ports
```yaml
ports:
- name: B
  summary: Base frame frame
  direction: input
- name: F
  summary: Follower frame frame
  direction: input
- name: fz
  summary: Actuation force physical signal
  direction: input
- name: pz
  summary: Motion profile physical signal
  direction: input
- name: tx
  summary: Actuation torque physical signal
  direction: input
- name: qx
  summary: Motion profile physical signal
  direction: input
- name: ty
  summary: Actuation torque physical signal
  direction: input
- name: qy
  summary: Motion profile physical signal
  direction: input
- name: tz
  summary: Actuation torque physical signal
  direction: input
- name: qz
  summary: Motion profile physical signal
  direction: input
- name: mode
  summary: Joint mode control physical signal
  direction: input
- name: pz
  summary: Position of joint primitive physical signal
  direction: output
- name: vz
  summary: Velocity of joint primitive physical signal
  direction: output
- name: az
  summary: Acceleration of joint primitive physical signal
  direction: output
- name: fz
  summary: Actuator force acting on joint primitive physical signal
  direction: output
- name: fllz
  summary: Lower-limit force acting on joint primitive physical signal
  direction: output
- name: fulz
  summary: Upper-limit force acting on joint primitive physical signal
  direction: output
- name: qx
  summary: Position of joint primitive physical signal
  direction: output
- name: wx
  summary: Angular velocity of joint primitive physical signal
  direction: output
- name: bx
  summary: Angular acceleration of joint primitive physical signal
  direction: output
- name: tx
  summary: Actuator torque acting on joint primitive physical signal
  direction: output
- name: tllx
  summary: Lower-limit torque acting on joint primitive physical signal
  direction: output
- name: tulx
  summary: Upper-limit torque acting on joint primitive physical signal
  direction: output
- name: qy
  summary: Position of joint primitive physical signal
  direction: output
- name: wy
  summary: Angular velocity of joint primitive physical signal
  direction: output
- name: by
  summary: Angular acceleration of joint primitive physical signal
  direction: output
- name: ty
  summary: Actuator torque acting on joint primitive physical signal
  direction: output
- name: tlly
  summary: Lower-limit torque acting on joint primitive physical signal
  direction: output
- name: tuly
  summary: Upper-limit torque acting on joint primitive physical signal
  direction: output
- name: qz
  summary: Position of joint primitive physical signal
  direction: output
- name: wz
  summary: Angular velocity of joint primitive physical signal
  direction: output
- name: bz
  summary: Angular acceleration of joint primitive physical signal
  direction: output
- name: tz
  summary: Actuator torque acting on joint primitive physical signal
  direction: output
- name: tllz
  summary: Lower-limit torque acting on joint primitive physical signal
  direction: output
- name: tulz
  summary: Upper-limit torque acting on joint primitive physical signal
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

#### Z Prismatic Primitive (Pz)

### **fz** — Actuation force physical signal

Physical signal input port that accepts the actuation force for the joint
primitive. The block applies this force equally and oppositely to the base and
follower frames of the joint along the *z*-axis of the base
frame.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Actuation**, set **Force** to `Provided by
Input`.

### **pz** — Motion profile physical signal

Physical signal input port that accepts the motion profile for the joint
primitive. The block uses this signal to determine the displacement of the follower
frame with respect to the base frame along the *z*-axis of the
base frame. The signal must also contain the first and second derivatives of the
displacement.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Actuation**, set **Motion** to `Provided by
Input`.

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

#### Z Revolute Primitive (Rz)

### **tz** — Actuation torque physical signal

Physical signal input port that accepts the actuation torque for the joint primitive. The
block applies this torque equally and oppositely to both the base and follower
frames of the joint primitive. The torque is about the *z*-axis of
the base frame. The *z*-axes of the follower and base frames align
with each other during simulation.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Actuation**, set **Torque** to `Provided by Input`.

### **qz** — Motion profile physical signal

Physical signal input port that accepts the motion profile for the joint primitive. The block
uses this signal to determine the rotation of the follower frame with respect to the
base frame about the *z*-axis of the base frame. The signal must
also contain the first and second derivatives of the rotation.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Actuation**, set **Motion** to `Provided by Input`.

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

#### Z Prismatic Primitive (Pz)

### **pz** — Position of joint primitive physical signal

Physical signal port that outputs the position of the joint primitive. The value
is the displacement of the follower frame with respect to the base frame in the
*z*-axis of the base frame.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Position**.

### **vz** — Velocity of joint primitive physical signal

Physical signal port that outputs the velocity of the joint primitive. The value
is the first derivative of the signal from the port
**pz**.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Velocity**.

### **az** — Acceleration of joint primitive physical signal

Physical signal port that outputs the acceleration of the joint primitive. The
value is the second derivative of the signal from the port
**pz**.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Acceleration**.

### **fz** — Actuator force acting on joint primitive physical signal

Physical signal port that outputs the actuator force acting on the joint primitive.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Actuator Force**.

### **fllz** — Lower-limit force acting on joint primitive physical signal

Physical signal port that outputs the lower-limit force. The block applies this
force when the joint primitive position is less than the lower bound of the free
region. The block applies this force to both the base and follower frames of the
joint primitive in order to accelerate the relative position back to the free
region.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Lower-Limit Force**.

### **fulz** — Upper-limit force acting on joint primitive physical signal

Physical signal port that outputs the upper-limit force. The block applies this
force when the joint primitive position exceeds the upper bound of the free region.
The block applies this force to both the base and follower frames of the joint
primitive in order to accelerate the relative position back to the free
region.

#### Dependencies

To enable this port, under **Z Prismatic Primitive (Pz)** >  **Sensing**, select **Upper-Limit Force**.

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

#### Z Revolute Primitive (Rz)

### **qz** — Position of joint primitive physical signal

Physical signal port that outputs the position of the joint primitive. The value
is the rotation angle of the follower frame with respect to the base frame about the
*z*-axis of the base frame.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Position**.

### **wz** — Angular velocity of joint primitive physical signal

Physical signal port that outputs the angular velocity of the joint primitive. The
value is the first derivative of the signal from the port
**qz**.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Velocity**.

### **bz** — Angular acceleration of joint primitive physical signal

Physical signal port that outputs the angular acceleration of the joint primitive.
The value is the second derivative of the signal from the port
**qz**.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Acceleration**.

### **tz** — Actuator torque acting on joint primitive physical signal

Physical signal port that outputs the actuator torque acting on the joint primitive.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Actuator Torque**.

### **tllz** — Lower-limit torque acting on joint primitive physical signal

Physical signal port that outputs the lower-limit torque. The block applies this
torque when the joint primitive position is less than the lower bound of the free
region. The block applies this torque to both the base and follower frames of the
joint primitive in order to accelerate the relative position back to the free
region.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Lower-Limit Torque**.

### **tulz** — Upper-limit torque acting on joint primitive physical signal

Physical signal port that outputs the upper-limit torque. The block applies this
torque when the joint primitive position exceeds the upper bound of the free region.
The block applies this torque to both the base and follower frames of the joint
primitive in order to accelerate the relative position back to the free
region.

#### Dependencies

To enable this port, under **Z Revolute Primitive (Rz)** >  **Sensing**, select **Upper-Limit Torque**.

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
- name: Specify Position Target
  summary: Whether to specify position target off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Priority
  summary: Priority level of position target High (desired) (default) | Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: Value
  summary: Position target 0 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Specify Velocity Target
  summary: Whether to specify linear velocity target off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Priority
  summary: Priority level of linear velocity target High (desired) (default) | Low (approximate)
  group: Z Prismatic Primitive (Pz)
- name: Value
  summary: Velocity target 0 m/s (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Equilibrium Position
  summary: Position where internal force is zero 0 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: Stiffness of force law 0 N/m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: Damping coefficient of force law 0 N(m/s) (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Specify Lower Limit
  summary: Whether to specify lower position limit off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: Lower bound of free region -1 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: Stiffness of spring at lower bound 1e6 N/m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: Damping coefficient at lower bound 1e3 N/(m/s) (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: Region to smooth spring and damper forces 1e-4 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Specify Upper Limit
  summary: Whether to specify upper position limit off (default) | on
  group: Z Prismatic Primitive (Pz)
- name: Bound
  summary: Upper bound of free region 1 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Spring Stiffness
  summary: Stiffness of spring at upper bound 1e6 N/m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Damping Coefficient
  summary: Damping coefficient at upper bound 1e3 N/(m/s) (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Transition Region Width
  summary: Region to smooth spring and damper forces 1e-4 m (default) | scalar
  group: Z Prismatic Primitive (Pz)
- name: Force
  summary: Option to provide actuator force None (default) | Provided by Input | Automatically Computed
  group: Z Prismatic Primitive (Pz)
- name: Motion
  summary: Option to provide motion Automatically Computed (default) | Provided by Input
  group: Z Prismatic Primitive (Pz)
- name: Specify Position Target
  summary: Whether to specify position target off (default) | on
  group: X Revolute Primitive (Rx)
- name: Priority
  summary: Priority level of position target High (desired) (default) | Low (approximate)
  group: X Revolute Primitive (Rx)
- name: Value
  summary: Position target 0 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Specify Velocity Target
  summary: Whether to specify angular velocity target off (default) | on
  group: X Revolute Primitive (Rx)
- name: Priority
  summary: Priority level of velocity target High (desired) (default) | Low (approximate)
  group: X Revolute Primitive (Rx)
- name: Value
  summary: Velocity target 0 deg/s (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Equilibrium Position
  summary: Position where internal torque is zero 0 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Spring Stiffness
  summary: Stiffness of force law 0 N*m/deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Damping Coefficient
  summary: Damping coefficient of force law 0 N*m/(deg/s) (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Specify Lower Limit
  summary: Whether to specify lower position limit off (default) | on
  group: X Revolute Primitive (Rx)
- name: Bound
  summary: Lower bound of free region -90 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Spring Stiffness
  summary: Stiffness of spring at lower bound 1e4 N*m/deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Damping Coefficient
  summary: Damping coefficient at lower bound 10 N*m/(deg/s) (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Specify Upper Limit
  summary: Whether to specify upper position limit off (default) | on
  group: X Revolute Primitive (Rx)
- name: Bound
  summary: Upper bound of free region 90 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Spring Stiffness
  summary: Stiffness of spring at upper bound 1e4 N*m/deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Damping Coefficient
  summary: Damping coefficient at upper bound 10 N*m/(deg/s) (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: X Revolute Primitive (Rx)
- name: Torque
  summary: Option to provide actuator torque None (default) | Provided by Input | Automatically Computed
  group: X Revolute Primitive (Rx)
- name: Motion
  summary: Option to provide motion Automatically Computed (default) | Provided by Input
  group: X Revolute Primitive (Rx)
- name: Specify Position Target
  summary: Whether to specify position target off (default) | on
  group: Y Revolute Primitive (Ry)
- name: Priority
  summary: Priority level of position target High (desired) (default) | Low (approximate)
  group: Y Revolute Primitive (Ry)
- name: Value
  summary: Position target 0 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Specify Velocity Target
  summary: Whether to specify angular velocity target off (default) | on
  group: Y Revolute Primitive (Ry)
- name: Priority
  summary: Priority level of velocity target High (desired) (default) | Low (approximate)
  group: Y Revolute Primitive (Ry)
- name: Value
  summary: Velocity target 0 deg/s (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Equilibrium Position
  summary: Position where internal torque is zero 0 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Spring Stiffness
  summary: Stiffness of force law 0 N*m/deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Damping Coefficient
  summary: Damping coefficient of force law 0 N*m/(deg/s) (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Specify Lower Limit
  summary: Whether to specify lower position limit off (default) | on
  group: Y Revolute Primitive (Ry)
- name: Bound
  summary: Lower bound of free region -90 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Spring Stiffness
  summary: Stiffness of spring at lower bound 1e4 N*m/deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Damping Coefficient
  summary: Damping coefficient at lower bound 10 N*m/(deg/s) (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Specify Upper Limit
  summary: Whether to specify upper position limit off (default) | on
  group: Y Revolute Primitive (Ry)
- name: Bound
  summary: Upper bound of free region 90 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Spring Stiffness
  summary: Stiffness of spring at upper bound 1e4 N*m/deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Damping Coefficient
  summary: Damping coefficient at upper bound 10 N*m/(deg/s) (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: Y Revolute Primitive (Ry)
- name: Torque
  summary: Option to provide actuator torque None (default) | Provided by Input | Automatically Computed
  group: Y Revolute Primitive (Ry)
- name: Motion
  summary: Option to provide motion Automatically Computed (default) | Provided by Input
  group: Y Revolute Primitive (Ry)
- name: Specify Position Target
  summary: Whether to specify position target off (default) | on
  group: Z Revolute Primitive (Rz)
- name: Priority
  summary: Priority level of position target High (desired) (default) | Low (approximate)
  group: Z Revolute Primitive (Rz)
- name: Value
  summary: Position target 0 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Specify Velocity Target
  summary: Whether to specify angular velocity target off (default) | on
  group: Z Revolute Primitive (Rz)
- name: Priority
  summary: Priority level of velocity target High (desired) (default) | Low (approximate)
  group: Z Revolute Primitive (Rz)
- name: Value
  summary: Velocity target 0 deg/s (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Equilibrium Position
  summary: Position where internal torque is zero 0 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: Stiffness of force law 0 N*m/deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: Damping coefficient of force law 0 N*m/(deg/s) (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Specify Lower Limit
  summary: Whether to specify lower position limit off (default) | on
  group: Z Revolute Primitive (Rz)
- name: Bound
  summary: Lower bound of free region -90 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: Stiffness of spring at lower bound 1e4 N*m/deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: Damping coefficient at lower bound 10 N*m/(deg/s) (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Specify Upper Limit
  summary: Whether to specify upper position limit off (default) | on
  group: Z Revolute Primitive (Rz)
- name: Bound
  summary: Upper bound of free region 90 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Spring Stiffness
  summary: Stiffness of spring at upper bound 1e4 N*m/deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Damping Coefficient
  summary: Damping coefficient at upper bound 10 N*m/(deg/s) (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Transition Region Width
  summary: Region to smooth spring and damper torques 0.1 deg (default) | scalar
  group: Z Revolute Primitive (Rz)
- name: Torque
  summary: Option to provide actuator torque None (default) | Provided by Input | Automatically Computed
  group: Z Revolute Primitive (Rz)
- name: Motion
  summary: Option to provide motion Automatically Computed (default) | Provided by Input
  group: Z Revolute Primitive (Rz)
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

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Z Prismatic Primitive (Pz)

#### State Targets

### **Specify Position Target** — Whether to specify position target `off` (default) | `on`

Select this parameter to specify the position target for the *z* prismatic
primitive.

### **Priority** — Priority level of position target `High (desired)` (default) | `Low (approximate)`

Priority level of the position target, specified as `High (desired)`
or `Low (approximate)`.
For more information, see the Guiding Assembly
section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Value** — Position target 0 `m` (default) | scalar

Position target of the *z* prismatic primitive, specified as a scalar in
units of length.

#### Dependencies

To enable this parameter, select **Specify Position Target**.

### **Specify Velocity Target** — Whether to specify linear velocity target `off` (default) | `on`

Select this parameter to specify the linear velocity target for the *z*
prismatic primitive.

### **Priority** — Priority level of linear velocity target `High (desired)` (default) | `Low (approximate)`

Priority level of the linear velocity target, specified as `High
(desired)` or `Low
(approximate)`. For more information,
see the Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Velocity Target**.

### **Value** — Velocity target 0 `m/s` (default) | scalar

Linear velocity target for the
*z* prismatic primitive,
specified as a scalar in units of linear
velocity.

#### Dependencies

To enable this parameter, select
**Specify Velocity
Target**.

#### Internal Mechanics

### **Equilibrium Position** — Position where internal force is zero 0 `m` (default) | scalar

Position where the spring force is zero, specified as a scalar in units of length.

### **Spring Stiffness** — Stiffness of force law 0 `N/m` (default) | scalar

Stiffness of the internal spring-damper force law for the joint primitive, specified as a scalar in units of linear stiffness.

### **Damping Coefficient** — Damping coefficient of force law 0 `N(m/s)` (default) | scalar

Damping coefficient of the internal spring-damper force law for the joint primitive, specified as a scalar in units of linear damping coefficient.

#### Limits

### **Specify Lower Limit** — Whether to specify lower position limit `off` (default) | `on`

Select this parameter to specify the lower limit of the *z* prismatic
primitive.

### **Bound** — Lower bound of free region -1 `m` (default) | scalar

Lower bound of the free region of the *z* prismatic primitive, specified as a
scalar in units of length.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Spring Stiffness** — Stiffness of spring at lower bound 1e6 `N/m` (default) | scalar

Stiffness of the spring at the lower bound, specified as a scalar in units of linear stiffness.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Damping Coefficient** — Damping coefficient at lower bound 1e3 `N/(m/s)` (default) | scalar

Damping coefficient at the lower bound, specified as a scalar in units of linear damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Transition Region Width** — Region to smooth spring and damper forces 1e-4 `m` (default) | scalar

Region to smooth the spring and damper forces, specified as a scalar in units of length.

The block applies the full value of the lower-limit force when the penetration reaches the
width of the transition region. The smaller the
region, the sharper the onset of forces and the
smaller the time step required of the solver. In
the tradeoff between simulation accuracy and
simulation speed, reducing the transition region
improves accuracy and expanding it improves
speed.

#### Dependencies

To enable this parameter, select **Specify Lower Limit**.

### **Specify Upper Limit** — Whether to specify upper position limit `off` (default) | `on`

Select this parameter to specify the upper limit of the *z* prismatic
primitive.

### **Bound** — Upper bound of free region 1 `m` (default) | scalar

Upper bound for the free region of the joint primitive, specified as a scalar in units of length.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Spring Stiffness** — Stiffness of spring at upper bound 1e6 `N/m` (default) | scalar

Stiffness of the spring at the upper bound, specified as a scalar in units of linear stiffness.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Damping Coefficient** — Damping coefficient at upper bound 1e3 `N/(m/s)` (default) | scalar

Damping coefficient at the upper bound, specified as a scalar in units of linear damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

### **Transition Region Width** — Region to smooth spring and damper forces 1e-4 `m` (default) | scalar

Region to smooth the spring and damper forces, specified as a scalar in units of length.

The block applies the full value of the upper-limit force when the penetration reaches the
width of the transition region. The smaller the
region, the sharper the onset of forces and the
smaller the time step required of the solver. In
the tradeoff between simulation accuracy and
simulation speed, reducing the transition region
improves accuracy and expanding it improves
speed.

#### Dependencies

To enable this parameter, select **Specify Upper Limit**.

#### Actuation

### **Force** — Option to provide actuator force `None` (default) | `Provided by Input` | `Automatically Computed`

Option to provide the actuator force for the joint primitive, specified as one of these values:

| Force Setting | Description |
| --- | --- |
| `None` | No actuator force. |
| `Provided by Input` | The input port **fz** specifies the actuator force for the *z* prismatic primitive. |
| `Automatically Computed` | The block automatically calculates the amount of force required to satisfy the motion inputs to the mechanism. If you set this parameter to `Automatically Computed`, you do not need to set **Motion** to `Provided by Input` for the same joint primitive. The automatically computed force may satisfy a motion input elsewhere in the mechanism. |

### **Motion** — Option to provide motion `Automatically Computed` (default) | `Provided by Input`

Option to provide the motion for the joint primitive, specified as one of these values:

| Motion Setting | Description |
| --- | --- |
| `Automatically Computed` | The block computes and applies the joint primitive motion based on the model dynamics. |
| `Provided by Input` | The input port **pz** specifies the motion for the joint primitive. |

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

### Z Revolute Primitive (Rz)

#### State Targets

### **Specify Position Target** — Whether to specify position target `off` (default) | `on`

Select this parameter to specify the position target of the *z* revolute
primitive.

### **Priority** — Priority level of position target `High (desired)` (default) | `Low (approximate)`

Priority level of the position target, specified as `High
(desired)` or `Low (approximate)`. For
more information, see the Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Position
Target**.

### **Value** — Position target 0 `deg` (default) | scalar

Position target of the *z* revolute primitive, specified as a
scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Position
Target**.

### **Specify Velocity Target** — Whether to specify angular velocity target `off` (default) | `on`

Select this parameter to specify the angular velocity target for the
*z* revolute primitive.

### **Priority** — Priority level of velocity target `High (desired)` (default) | `Low (approximate)`

Priority level of the angular velocity target, specified as `High
(desired)` or `Low (approximate)`. For
more information, see the Guiding Assembly section of How Multibody Assembly Works.

#### Dependencies

To enable this parameter, select **Specify Velocity
Target**.

### **Value** — Velocity target 0 `deg/s` (default) | scalar

Angular velocity target of the *z* revolute primitive,
specified as a scalar with a unit of angular velocity.

#### Dependencies

To enable this parameter, select **Specify Velocity
Target**.

#### Internal Mechanics

### **Equilibrium Position** — Position where internal torque is zero 0 `deg` (default) | scalar

Position where the spring torque is zero, specified as a scalar with a unit of angle.

### **Spring Stiffness** — Stiffness of force law 0 `N*m/deg` (default) | scalar

Stiffness of the internal spring-damper force law for the *z* revolute
primitive, specified as a scalar with a unit of torsional stiffness.

### **Damping Coefficient** — Damping coefficient of force law 0 `N*m/(deg/s)` (default) | scalar

Damping coefficient of the internal spring-damper force law for the *z*
revolute primitive, specified as a scalar with a unit of damping
coefficient.

#### Limits

### **Specify Lower Limit** — Whether to specify lower position limit `off` (default) | `on`

Select this parameter to specify the lower limit of the *z* revolute
primitive.

### **Bound** — Lower bound of free region -90 `deg` (default) | scalar

Lower bound for the free region of the *z* revolute
primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Lower
Limit**.

### **Spring Stiffness** — Stiffness of spring at lower bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the lower bound, specified as a scalar with a unit
of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Lower
Limit**.

### **Damping Coefficient** — Damping coefficient at lower bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the lower bound, specified as a scalar with a unit of
damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Lower
Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a
unit of angle.

The block applies the full value of the lower-limit torque when the
penetration reaches the width of the transition region. The smaller the region,
the sharper the onset of forces and the smaller the time step required of the
solver. In the tradeoff between simulation accuracy and simulation speed,
reducing the transition region improves accuracy and expanding it improves
speed.

#### Dependencies

To enable this parameter, select **Specify Lower
Limit**.

### **Specify Upper Limit** — Whether to specify upper position limit `off` (default) | `on`

Select this parameter to specify the upper limit of the *z* revolute
primitive.

### **Bound** — Upper bound of free region 90 `deg` (default) | scalar

Upper bound for the free region of the *z* revolute
primitive, specified as a scalar with a unit of angle.

#### Dependencies

To enable this parameter, select **Specify Upper
Limit**.

### **Spring Stiffness** — Stiffness of spring at upper bound 1e4 `N*m/deg` (default) | scalar

Stiffness of the spring at the upper bound, specified as a scalar with a unit
of torsional stiffness.

#### Dependencies

To enable this parameter, select **Specify Upper
Limit**.

### **Damping Coefficient** — Damping coefficient at upper bound 10 `N*m/(deg/s)` (default) | scalar

Damping coefficient at the upper bound, specified as a scalar with a unit of
damping coefficient.

#### Dependencies

To enable this parameter, select **Specify Upper
Limit**.

### **Transition Region Width** — Region to smooth spring and damper torques 0.1 `deg` (default) | scalar

Region to smooth the spring and damper torques, specified as a scalar with a
unit of angle.

The block applies the full value of the upper-limit torque when the
penetration reaches the width of the transition region. The smaller the region,
the sharper the onset of forces and the smaller the time step required of the
solver. In the tradeoff between simulation accuracy and simulation speed,
reducing the transition region improves accuracy and expanding it improves
speed.

#### Dependencies

To enable this parameter, select **Specify Upper
Limit**.

#### Actuation

### **Torque** — Option to provide actuator torque `None` (default) | `Provided by Input` | `Automatically Computed`

Option to provide the actuator torque for the joint primitive, specified as
one of these values:

| Torque Setting | Description |
| --- | --- |
| `None` | No actuator torque. |
| `Provided by Input` | The input port **tz** specifies the actuator torque for the *z* revolute primitive. |
| `Automatically Computed` | The block computes the torque automatically. If you set this parameter to `Automatically Computed`, you do not need to set **Motion** to `Provided by Input` for the for the same joint primitive. The automatically computed torque may satisfy a motion input somewhere else in the mechanism. |

### **Motion** — Option to provide motion `Automatically Computed` (default) | `Provided by Input`

Option to provide the motion for the joint primitive, specified as one of
these values:

| Motion Setting | Description |
| --- | --- |
| `Automatically computed` | The block computes and applies the joint primitive motion based on model dynamics. |
| `Provided by Input` | The input port **qz** specifies the motion for the *z* revolute primitive. |

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

Joint with one prismatic and three revolute primitives

The Bearing Joint block provides one prismatic and three
rotational degrees of freedom between two frames as shown in the image.

Joint transformation sequence of bearing Joint

The follower frame can transform with respect to the base frame through a sequence of
movements that include a translation and a 3-D rotation.

Joint transformation sequence of bearing joint

The follower frame first translates along the *z*-axis of the base
frame and then rotates about the axes of the follower frame. The first rotation is about the
*x*-axis, the second rotation is about the *y*-axis of the follower frame generated after the first rotation,
and the third rotation is about the *z*-axis of the follower
frame generated after the second rotation.

The 3-D rotation has a kinematic singularity at configurations in which the second
rotation is positive or negative 90 degrees. In these configurations, the first and third
rotation axes are aligned and the joint loses a degree of freedom.

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
