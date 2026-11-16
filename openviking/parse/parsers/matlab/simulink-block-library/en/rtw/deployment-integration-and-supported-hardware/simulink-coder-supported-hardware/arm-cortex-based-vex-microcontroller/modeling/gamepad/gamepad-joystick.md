---
type: simulink-block
title: 'Gamepad Joystick'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadjoystick'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadjoystick.html'
language: en
---

# Gamepad Joystick

## Ports

### Input

### **Port\_1** — Analog signal used during simulation integer in [ –128 127]

Connect a source block, such as the Gamepad Simulator block from
the Utilities library in Simulink® Support Package for ARM®
Cortex®-based VEX Microcontroller.

#### Dependencies

This port appears only when you select the **Add input port for
simulation** parameter.

**Data Types:** `double`
### Output

### **Port\_1** — Analog signal corresponding to position of joystick along axis integer in [ –128 127]

The block output ranges from –128 to 127 based on the position of the joystick
along the specified control axis. A value of 0 indicates that the joystick has not
been moved along the axis.

During simulations, without the hardware, this block emits zeros if there is no
source block connected the simulation input port (see Block Produces Zeros or Does Nothing in Simulation).

**Data Types:** `double`

## Parameters

### **Joystick Number** — Joystick number `1` (default)

This parameter is read only. You can have a pair of VEX gamepads to control the
peripherals connected to the VEX microcontroller. However, in the VEX Robotics and BEST
Robotics competitions, teams are allowed only one gamepad. Therefore, **Joystick
Number** is set to 1 by default, and it cannot be changed.

### **Analog Channel (1 to 4)** — Select control axis of *x-y* analog joystick 1 (default)

Select the control axis to read on the VEX gamepad. The right joystick has
horizontal axis labeled 1 and its vertical axis is labeled 2. The left joystick has
horizontal axis labeled 3 and its vertical axis is labeled 4. Based on your selection,
the mask icon of the block is updated in the Simulink Editor.

### **Add input port for simulation** — Add an input port to simulate joystick `off` (default) | `on`

Select this check box to add an input port to specify an analog value during
simulation.

### **Sample time** — Sample time for obtaining analog value from joystick `0.02` (default) | positive real number

How often the Gamepad Joystick block should read the values from the
gamepad joystick specified in seconds. The default value is 0.02 seconds.

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
Gamepad Joystick block is ignored and has no effect on the generated
code.

## Version History

**Introduced in R2016a**

## Description

Represent one control axis on x - y analog VEX gamepad joystick and read values

The Gamepad Joystick block is used to represent one of the control axes of
an *x-y* analog joystick on the VEX® gamepad. The block reads the corresponding analog value based on the position of
the joystick along that axis. There are two analog joysticks on the VEX gamepad with two
control axes (*x-y*) on each joystick.
