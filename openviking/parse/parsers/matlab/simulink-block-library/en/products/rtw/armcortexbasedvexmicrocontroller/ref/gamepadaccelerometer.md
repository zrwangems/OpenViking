---
type: simulink-block
title: 'Gamepad Accelerometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadaccelerometer'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadaccelerometer.html'
language: en
---

# Gamepad Accelerometer

## Ports

### Input

### **Port\_1** — Analog signal used during simulation integer in [–128 127]

Connect a source block such as the Gamepad Simulator block from the
Utilities library in Simulink® Support Package for ARM®
Cortex®-based VEX Microcontroller.

#### Dependencies

This port appears only when you select the **Add input port for
simulation** parameter.

**Data Types:** `double`
### Output

### **Port\_1** — Analog value from accelerometer integer in [ –128 127]

The block output ranges from –128 to 127 based on the axis selected and the
orientation of the gamepad.

During simulations, without the hardware, this block emits zeros if there is no
Source block connected the simulation input port (see Block Produces Zeros or Does Nothing in Simulation).

**Data Types:** `double`

## Parameters

### **Joystick** — Joystick number `1` (default)

This parameter is read only. You can have a pair of VEX gamepads to control the
peripherals connected to the VEX microcontroller. However, in the VEX Robotics and BEST
Robotics competitions, teams are allowed only one gamepad. Therefore,
**Joystick** is set to 1 by default, and it cannot be changed.

### **Axis of Rotation (X-axis = 1, Y-axis = 2)** — Select axis of rotation of gamepad `1` | `2` (default)

The axis of rotation determines which accelerometer is used to generate the output
value. Select 1 for the horizontal *x*-axis and 2 for the vertical
*y*-axis.

### **Add input port for simulation** — Add input port to simulate input acceleration `off` (default) | `on`

Select this check box to add an input port to specify an analog value for
acceleration.

### **Sample time** — Sample time for obtaining analog value of acceleration `0.02` (default) | positive real number

How often the Gamepad Accelerometer block should read the values from
the gamepad, specified in seconds. The default value is 0.02 seconds.

If you select the **Add input port for simulation** check box, the
**Sample time** parameter is hidden and its value is
inherited.

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

During code generation, any simulation block that is connected to the input port of
Gamepad Accelerometer block is ignored and has no effect on the generated
code.

## Version History

**Introduced in R2016a**

## Description

Read analog value from VEX gamepad accelerometer

The Gamepad Accelerometer block is used to read an analog value from the VEX® gamepad accelerometer based on the axis of rotation (*x* or
*y*) of the gamepad.

The output for this block ranges from –128 to 127. There are two accelerometers on the
VEX gamepad, and their axes are aligned perpendicular to each other. Rotation of the
VEX gamepad along either the horizontal axis (1) or the vertical axis (2) results in an output
value in the range –128 to 127. You can use this analog value to control peripherals, such as
a DC motor, that are connected to the VEX microcontroller.
