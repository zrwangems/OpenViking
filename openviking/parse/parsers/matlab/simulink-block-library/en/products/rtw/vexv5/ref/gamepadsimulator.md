---
type: simulink-block
title: 'Gamepad Simulator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'gamepadsimulator'
documentation_source_path: 'vexv5/ref/gamepadsimulator.html'
language: en
---

# Gamepad Simulator

## Ports

Not documented in R2025b.

## Parameters

**Select the type of Gamepad**
:   Select the gamepad type that is connected to your computer.

**Enter the joystick ID**
:   Enter the one-based joystick ID.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Get the simulation value of a VEX gamepad using Logitech F310 or XBOX Controller

Get the simulation value of a VEX® gamepad. The block is applicable for simulation purposes only. The values
returned are analog values in the range –127 to 127 for the first four output ports, and
logical values for the remaining 12 output ports. The first four ports correspond to the
four control axes on the joysticks. The remaining 12 ports correspond to the 12 buttons on
the VEX gamepad. The Logitech® Gamepad F310 buttons corresponding to the Gamepad Simulator
ports (1–8) are as shown.

Before simulating a model containing this block, you must connect a Gamepad F310 or an
XBOX gamepad to your computer. During simulation, use the attached gamepad to provide
simulation input to your Simulink® model.

**Note**

Ensure that the input mode switch on the
backside of the Gamepad F310 device is in position D for the block to function correctly.
For more information about the input mode switch on Gamepad F310, see https://support.logi.com/hc/en-us.

During code generation, the Gamepad Simulator block is ignored and has no effect on the
generated code.
