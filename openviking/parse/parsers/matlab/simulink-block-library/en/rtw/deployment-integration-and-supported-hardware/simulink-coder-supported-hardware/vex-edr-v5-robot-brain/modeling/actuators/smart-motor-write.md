---
type: simulink-block
title: 'Smart Motor Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'smartmotorwrite'
documentation_source_path: 'vexv5/ref/smartmotorwrite.html'
language: en
---

# Smart Motor Write

## Ports

### Input

### **Velocity** — Input analog signal that sets motor velocity RPM, integer in [–100 100]

The input velocity for Smart Block Write block can range from –100
to 100. The sign determines the direction of rotation of the motor, and the amplitude
determines the velocity in RPM. Positive value rotates the motor in clockwise
direction and negative value rotates the motor in anticlockwise direction. A block
input value of `0` stops the motor.

For an input velocity value beyond the range of -100 to 100, the block supplies
the power for an amplitude of 100.

**Data Types:** `double`

### **Position** — Encoder tick count that sets target motor position integer

The Position input sets the target position of motor in terms of the tick count.
When this input value is equal to the tick count from the in-built encoder of V5 Smart
Motor, the target position of the motor is achieved.

For example, to stop the motor after 2 rotations:

- For a gear ratio of 36:1, set the Position input to
  `3600`
- For a gear ratio of 18:1, set the Position input to
  `1800`
- For a gear ratio of 6:1, set the Position input to
  `600`

#### Dependencies

This input appears only when you set the **Control mode**
parameter to `Position Control`.

**Data Types:** `double`

## Parameters

### **Smart Port** — Select the Smart Port to which V5 Smart Motor is connected 1 (default) | `1` to `21`

Select the Smart Port on the VEX EDR V5 Robot Brain to which the V5 Smart Motor is connected. There are 21
Smart Ports on the VEX EDR V5 Robot Brain that you can connect to V5 Smart Motor.

Smart Port must be unique for each block in the model. If multiple Smart Motor Write
blocks with the same port are used, the last executed Smart Motor Write block may only
be active. For the Vex Robotics Competition, you can use the same Smart Motor Write
block with the same Smart Port in the driver mode or the autonomous mode.

### **Gearing Ratio** — Select the gearing ratio for V5 Smart Motor 36:1 (default) | `18:1` | `6:1`

Select the internal gearing ratio that is used to drive the V5 Smart Motor.

### **Braking mode** — Select the braking mode of V5 Smart Motor `Coast` (default) | `Brake` | `Hold`

Select the braking mode to match the braking mechanism used for the V5 Smart Motor:

- l`Coast` – Set the motor to coast to a stop
- l`Brake` – Set the motor to stop immediately by applying a
  brake
- l`Hold` – Set the motor to stop immediately by applying a
  brake and attempt to hold its position

### **Control mode** — Select the control mode of V5 Smart Motor `Velocity Control` (default) | `Position Control`

Select the control mode to switch from velocity control to position control or vice
versa.

When you select `Position Control`, an additional input –
`Position` – is added, which sets the target position of the motor.

`Position Control` mode is used to turn the motor shaft to
an encoder tick value (corresponding to an angle). For example, opening claw to a
certain angle. `Velocity control` mode is used when a
continuous range of motion is required. For example, controlling drivetrain
motors.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent connected V5 Smart Motor and set its velocity and position

The Smart Motor Write block represents a V5 Smart Motor connected to a
specified port on a VEX® EDR V5 Robot Brain, and sets the velocity and position of the motor.
