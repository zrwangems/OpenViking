---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/servomotor.html'
language: en
---

# Servo Motor

## Ports

### Input

### **Port\_1** — Input signal that sets angular position of servo motor integer in [ –128 127]

The input signal for the Servo Motor block can be derived from
other blocks in the model. For example:

- If a Gamepad Joystick block is connected as the input for a
  Servo Motor block, the input value can range from –128 to 127
  based on the position of the joystick, which then translates to an angular
  position value (in degrees) of the servo. For block input value ‘0’, the servo
  motor is stationary.
- If a Gamepad Button block along with a Gain block is
  connected as the input for a Servo Motor block, the input can be
  set to a particular value for the duration for which the button is kept pressed,
  which translates to an angular position value (in degrees) of the servo.

During simulations without the hardware, the Servo Motor
block emits zeros if there is no block connected to the input port (see Block Produces Zeros or Does Nothing in Simulation). If the input value to
the Servo Motor is beyond the range of –128 to 127, you receive an error message
during simulation.

**Data Types:** `double`
### Output

### **Port\_1** — Servo angle during simulation scalar

The output is the angle, in degrees, of the servo motor. Connect a Sink block,
such as a Display or Scope block, to the output port to view the simulation output.
The Sink blocks are available in the Utilities library in Simulink® Support Package for ARM
Cortex-based VEX Microcontroller.

#### Dependencies

This port appears only when you select the **Add output port to measure
the servo angle during simulation** parameter.

**Data Types:** `double`

## Parameters

### **Motor Channel** — Select motor channel for servo motor 1 (default) | `1` to `10`

Select the motor channel or pin on the ARM
Cortex-based VEX Microcontroller that is connected to the servo motor.

Do not assign the same channel number to more than one Servo Motor
block within the same model.

### **Add output port to measure the servo angle during simulation** — Add output port for simulation `off` (default) | `on`

Select this check box to add the output port to emit the angle of the servo motor
during simulation.

## Libraries

Simulink Coder Support Package for ARM Cortex-based Microcontroller / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

During code generation, any simulation block that is connected to the output port of a
Servo Motor block is ignored and has no effect on the generated code.

## Version History

**Introduced in R2016a**

## Description

Represent connected servo motor and set angular position value

The Servo Motor block reprsents a servo motor connected to a specified
motor channel on an ARM®
Cortex®-based VEX® Microcontroller. The input signal sets the angular position value of the servo
motor. There are 10 motor channels, or pins, on the VEX microcontroller that you can connect to servo motors. For information on the pin
layout of the microcontroller, see the VEX Cortex
Pin-Out diagram from VEX Robotics.
