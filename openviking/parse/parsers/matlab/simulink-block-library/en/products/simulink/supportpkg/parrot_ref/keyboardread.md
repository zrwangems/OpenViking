---
type: simulink-block
title: 'Keyboard Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'keyboardread'
documentation_source_path: 'supportpkg/parrot_ref/keyboardread.html'
language: en
---

# Keyboard Read

## Ports

### Output

### **Port\_1** — ASCII code of the basic character pressed on the keyboard ASCII

The supported basic characters include all printable characters –
letters, numbers, punctuation marks, and common symbols present on the
keyboard.

**Data Types:** `uint8`

## Parameters

### **Sample time** — Interval at which block reads data `0.005` (default) | any non-negative value that is a multiple of 0.005 (5 ms) | -1

Enter the time interval at which to receive data.

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Receive key presses from keyboard of host computer and output ASCII code

The Keyboard Read block receives the key presses for any basic character on the
keyboard of the host computer, and outputs the corresponding ASCII code of the
character.

This block can be used in a Simulink® model created using Simulink Support Package for Parrot® Minidrones, to perform real-time flight control of Parrot minidrone using the keyboard keys.

**Note**

Only one Keyboard Read block is allowed in the entire Simulink model. Any number of connections can be derived from the output
signal of this block.

In the Simulink model, you can connect multiple Compare to Constant blocks to the output
of the Keyboard Read block to map the different ASCII codes.

After the Simulink model has started running on the drone, you can use the `Keyboard
Control Panel` on the Flight Control Interface to type the basic characters
that you have mapped to the control logic.
