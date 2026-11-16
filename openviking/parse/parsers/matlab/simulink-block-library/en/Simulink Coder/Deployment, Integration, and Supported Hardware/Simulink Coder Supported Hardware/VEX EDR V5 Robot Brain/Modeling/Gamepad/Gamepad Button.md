---
type: simulink-block
title: 'Gamepad Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'gamepadbutton'
documentation_source_path: 'vexv5/ref/gamepadbutton.html'
language: en
---

# Gamepad Button

## Ports

### Output

### **Port\_1** — Output port with a logical value (1 or 0) `1` or `0`

When you press the button, the block output is 1; otherwise (in a released state
of the button), the block output is 0.

**Data Types:** `Boolean`

## Parameters

### **Gamepad type** — Select the type of gamepad control `Primary` (default) | `Partner`

You can have a pair of VEX V5 Controller gamepads to control the peripherals
connected to VEX EDR V5 Robot Brain.

### **Button** — Select a button on the V5 Controller gamepad `R1` (default)

Before you make the selection, review the labeling of the buttons on the VEX V5
Controller gamepad.

### **Sample time** — Sample time for obtaining the logical value of the button `0.02` (default) | seconds

Specify how often the Gamepad Button block should read the logical
value of the button.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent one of the 12 buttons on VEX V5 Controller gamepad and read the logical value of the button

The Gamepad Button block is used to represent one of the 12 buttons on the
VEX® V5 Controller gamepad, and read the corresponding logical value (1 or 0) based
on whether the button is pressed or released.
