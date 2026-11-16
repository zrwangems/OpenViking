---
type: simulink-block
title: 'Arcade Module'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'arcademodule'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/arcademodule.html'
language: en
---

# Arcade Module

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Get the right and left wheel speed values of a robot in an Arcade configuration

Get the speed value for the right and left wheels of an Arcade robot. Arcade-style
control of a robot uses both the axes on a single joystick to control the forward and
reverse motion and the left and right differential. The first input port maps to the
vertical axis on the joystick. The second input port maps to the horizontal axis on the same
joystick. The first output is the right motor speed, and the second output is the left motor
speed.

The Arcade Module block uses these formulas to determine the motor speed:

- *RightMotorSpeed* = min(max((*y*−*x*),−127), 127)
- *LeftMotorSpeed* = min(max((*x*+*y*),−127), 127)

Here, *x* and *y* represent the position of the
joystick.

For example, when the joystick is moved fully forward, *y* = 127 and
*x* = 0. This results in a `RightMotorSpeed` value of
127 and a `LeftMotorSpeed` value of 127, which makes the robot move
forward.

**Note**

The Arcade Module block is not compatible with the Field
Simulator block. Avoid using the Field Simulator block with the
Arcade Module block in your model.
