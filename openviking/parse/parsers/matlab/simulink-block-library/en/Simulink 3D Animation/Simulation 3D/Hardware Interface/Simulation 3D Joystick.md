---
type: simulink-block
title: 'Simulation 3D Joystick'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Hardware Interface'
documentation_page: 'simulation3djoystick'
documentation_source_path: 'simulation3djoystick.html'
language: en
---

# Simulation 3D Joystick

## Ports

### Input

### **Force** — Force feedback input scalar | vector

Provide the force-feedback to be applied along supported joystick axes as a scalar or a
vector in the range [-1,1].

The length of the **Force** vector corresponds to the number of joystick axes
that support force-feedback. The force-feedback input provided to the
joystick is a scaled value. This value is subsequently multiplied by the
maximum force capability of the device.

#### Dependencies

To enable this parameter, select the **Enable force-feedback input**
parameter.

**Data Types:** `double`
### Output

### **Axes** — Joystick position along any given axis vector with each element in the range [-1,1]

The first joystick axes element is `x`, the second element is
`y`, and so on, up to the total number of axes.
What the `x`-axis represents depends on the type and
shape of the joystick. The Simulation 3D Joystick block uses the
mapping between the joystick driver and the joystick.

**Data Types:** `double`

### **Buttons** — Status of joystick buttons vector of 0 and 1

Status of joystick buttons.

**Data Types:** `double`

### **Point of view** — Current status of joystick point-of-view selector -1 (selector inactive) | scalar

The output signal is the angle of the point-of-view selector, or POV
Hat, in degrees from 0 to 360. If the selector is inactive, the signal
is -1.

**Data Types:** `double`

## Parameters

### **Joystick ID** — ID assigned to given joystick device `1` (default)

You can find the properties of the joystick that is connected to the
system in the Game Controllers section of the system Control Panel.

### **Adjust I/O ports according to joystick capabilities** — Option to dynamically adjust ports to correspond to joystick capabilities `on` (default) | `off`

If you enable this parameter, the Simulink
3D Animation software dynamically adjusts the ports to correspond to the
capabilities of the connected joystick each time that you open the model. If
the connected device does not have force-feedback capability, selecting this
check box causes the removal of the force-feedback input from the block,
even if you enable the **Enable force-feedback input**
parameter.

The block ports do not have the full widths provided by the Windows® Game Controllers interface.

### **Enable force-feedback input** — Option to support joysticks with force-feedback `on` (default) | `off`

If you select this check box, the Simulink
3D Animation software can support force-feedback joystick, steering wheel,
and haptic (one that enables tactile feedback) devices.

## Libraries

Simulink 3D Animation / Simulation 3D / Hardware Interface

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2025a: Renamed from Joystick Input

To reflect the Simulink library change, the Joystick Input block is now called
Simulation 3D Joystick. The behavior remains the same.

## Description

Process input from asynchronous joystick device

The Simulation 3D Joystick block provides interaction between a Simulink® model and the virtual world associated with a Simulink
3D Animation™ block. This block uses axes, buttons, and the point-of-view selector, if
present. You can use this block as you would use any other Simulink source block. Its output ports reflect the status of the joystick controls
for axes and buttons. The block also supports force-feedback devices.

The Simulation 3D Joystick block supports all joystick devices that use the Microsoft® APIs `DirectInput` and `XInput`
components as their communication protocols.
