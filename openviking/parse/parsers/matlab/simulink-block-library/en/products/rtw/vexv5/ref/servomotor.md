---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'vexv5/ref/servomotor.html'
language: en
---

# Servo Motor

## Ports

### Input

### **Port\_1** — Input signal that sets angular position of servo motor integer in [–128 127]

The input signal for the Servo Motor block can be derived from
other blocks in the model. For example:

- If a Gamepad Joystick block is connected as the input for a
  Servo Motor block, the input value can range from –128 to 127
  based on the position of the joystick on the gamepad, which then translates to
  an angular position value (in degrees) of the servo. For block input value ‘0’,
  the servo motor is stationary.
- If a Gamepad Button block along with a Gain block is
  connected as the input for a Servo Motor block, the input can be
  set to a particular value for the duration for which the button is kept pressed,
  which translates to an angular position value (in degrees) of the servo.

**Data Types:** `double`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX EDR V5 Robot Brain to which the expander is connected.

### **Port** — Select the 3-wire port connected to the servo motor A (default) | `A` to `H`

Select the 3-wire port on the VEX EDR V5 Robot Brain that is connected to the servo motor.

Do not assign the same port to more than one Servo Motor block within
the same model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent connected servo motor and set angular position value

The Servo Motor block represents a servo motor connected to a specified
3-wire port on a VEX® EDR V5 Robot Brain. The input signal to the block sets the angular position
value of the servo motor. There are eight 3-wire ports on VEX EDR V5 Robot Brain that you can connect to servo motors.
