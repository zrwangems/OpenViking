---
type: simulink-block
title: 'Gamepad Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'gamepadbutton'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gamepadbutton.html'
language: en
---

# Gamepad Button

## Ports

### Input

### **Port\_1** — Digital signal used during simulation `1` | `0`

Connect a source block, such as the Gamepad Simulator block from
the Utilities library in Simulink® Support Package for ARM®
Cortex®-based VEX Microcontroller.

#### Dependencies

This port appears only when you select the **Add input port for
simulation** parameter.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Logical value representing state of button `1` or `0`

When you press the button, the block output is `1`; otherwise (in
a released state of the button), the block output is `0`.

During simulations without the hardware, this block emits zeros if there is no
source block connected to the input port (see Block Produces Zeros or Does Nothing in Simulation).

**Data Types:** `Boolean`

## Parameters

### **Joystick** — Select joystick number `1` (default)

This parameter is read only. You can have a pair of VEX gamepads to control the
peripherals connected to the VEX microcontroller. However, in the VEX Robotics and the
BEST Robotics competitions, teams are allowed only one gamepad. Therefore, the
**Joystick** is set to 1 by default, and it cannot be changed.

### **Channel (5 to 8)** — Select channel or button group `5` | `6` | `7` | `8` (default)

Select the channel or button group on the VEX gamepad. The VEX gamepad has four
channels – 5, 6, 7, and 8 – which contain a total of 12 buttons.

### **Button (Down, Up)** — Select button in selected channel `Down` (default) | `Up` | `Right` | `Left`

The options for this parameter vary depending on the **Channel**
that you select. Channels 5 and 6 have Up and Down buttons only, while channels 7 and 8
have Up, Down, Right, and Left buttons. Before you make the selection, review the
labeling of the buttons on the VEX gamepad.

### **Add input port for simulation** — Add input port to simulate logical value of button `off` (default) | `on`

Select this check box to add an input port to specify a logical value of the button
during simulation.

### **Sample time** — Sample time for obtaining logical value of button `0.02` (default) | positive real number

How often the Gamepad Button block should read the logical value of
the button, specified in seconds. The default value is 0.02 seconds.

#### Dependencies

If you select the **Add input port for simulation** check box,
the **Sample time** parameter is hidden and its value is
inherited.

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

During code generation, any simulation block that is connected to the input port of the
Gamepad Button block is ignored and has no effect on the generated
code.

## Version History

**Introduced in R2016a**

## Description

Represent one button on VEX gamepad and read logical value

The Gamepad Button block is used to represent one of the 12 buttons on the
VEX® gamepad. The block reads the corresponding logical value (1 or 0) based on
whether the button is pressed or released.
