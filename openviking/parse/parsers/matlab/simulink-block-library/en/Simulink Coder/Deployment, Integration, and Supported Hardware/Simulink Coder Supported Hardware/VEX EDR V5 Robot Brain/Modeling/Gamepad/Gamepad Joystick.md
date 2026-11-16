---
type: simulink-block
title: 'Gamepad Joystick'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'gamepadjoystick'
documentation_source_path: 'vexv5/ref/gamepadjoystick.html'
language: en
---

# Gamepad Joystick

## Ports

### Output

### **Port\_1** — Output port with the value of the analog signal corresponding to the position of joystick along the axis `-128` to `127`

The block output ranges from -128 to 127 based on the position of the joystick
along the specified control axis. A value of 0 indicates that the joystick has not
been moved along the axis.

During simulations, without the hardware, this block emits zeros if there is no
Source block connected the simulation input port (see Block Produces Zeros or Does Nothing in Simulation). During code
generation, any simulation block that is connected to the input port of Gamepad
Joystick block is ignored and has no effect on the generated code.

**Data Types:** `double`

## Parameters

### **Gamepad Type** — Select the type of gamepad control `Primary` (default) | `Partner`

You can have a pair of VEX V5 Controller gamepads to control the peripherals
connected to VEX EDR V5 Robot Brain.

### **Analog Channel (1 to 4)** — Select the control axis (1 to 4) of the x-y analog joystick on the VEX V5 Controller gamepad 1 (default)

Select the control axis based on the labeling of the joysticks on the VEX gamepad.
The right joystick has horizontal axis labeled as **1** and
vertical axis labeled as **2**. The left joystick has
horizontal axis labeled as **3** and vertical axis labeled
as **4**. Based on your selection of this parameter, the
mask icon of the block is updated in the Simulink® Editor.

### **Sample time** — Sample time for obtaining the analog value from joystick `0.02` (default) | seconds

Specify how often the Gamepad Joystick block should read the values
from the gamepad's joystick. The default value is 0.02 seconds.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent one of the control axis on an x-y analog joystick on VEX V5 Controller gamepad and read the values

The Gamepad Joystick block is used to represent one of the control axis of
an x-y analog joystick on the VEX® V5 Controller gamepad, and read the corresponding analog value based on the
position of the joystick along that axis. There are two analog joysticks on the VEX V5
Controller gamepad with two control axes on each joystick.
