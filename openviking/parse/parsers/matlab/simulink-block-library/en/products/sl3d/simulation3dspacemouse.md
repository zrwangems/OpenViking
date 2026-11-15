---
type: simulink-block
title: 'Simulation 3D Space Mouse'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: '3D Environment'
documentation_page: 'simulation3dspacemouse'
documentation_source_path: 'simulation3dspacemouse.html'
language: en
---

# Simulation 3D Space Mouse

## Ports

### Output

### **Translation** — Status of object translation `1` or `true` | `0` or `false`

Status of object translation, returned as `0` or
`false` if not pressed and `1` or
`true` if pressed.

**Data Types:** `Boolean`

### **Rotation** — Status of object rotation `1` or `true` | `0` or `false`

Status of object rotation, returned as `0` or
`false` if not pressed and `1` or
`true` if pressed.

**Data Types:** `Boolean`

### **Buttons** — Status of button `1` or `true` | `0` or `false`

Status of button, returned as `0` or
`false` if not pressed and `1` or
`true` if pressed.

**Data Types:** `Boolean`

## Parameters

### **Port** — Serial port where mouse is connected `COM1` (default) | `COM2` | `COM3` | `COM4` | `USB1` | `USB2` | `USB3` | `USB4`

Serial port to which the space mouse is connected. Possible values are
`USB1`...`USB4` and
`COM1`...`COM4`.

### **Output type** — Type of output `Speed` (default) | `Position` | `Viewpoint coordinates`

Specify how the inputs from the device are transformed:

- `Speed` — No transformations are done.
  Outputs are translation and rotation speeds.
- `Position` — Translations and rotations
  are integrated. Outputs are position and orientation in the form of
  roll/pitch/yaw angles.
- `Viewpoint coordinates` — Translations
  and rotations are integrated. Outputs are position and orientation
  in the form of an axis and an angle. You can use these values as
  viewpoint coordinates in a virtual world.

### **Dominant mode** — Option to accept only prevailing movement and rotation `off` (default) | `on`

If this check box is selected, the mouse accepts only the prevailing
movement and rotation and ignores the others. This mode can be useful for
beginners using Simulation 3D Space Mouse block.

### **Disable position movement** — Option to fix rotations at initial values `off` (default) | `on`

Select this check box to fix the rotations at initial values, allowing you
to change positions only.

### **Disable rotation movement** — Option to fix positions at initial values `off` (default) | `on`

Select this check box to fix the positions at the initial values, allowing
you to change rotations only.

### **Normalize output angle** — Option to determine whether rotation angles should wrap in full circle `off` (default) | `on`

Select whether the integrated rotation angles should wrap on a full circle
(360°). The software ignores this parameter when you set **Output
Type** to `Speed`.

#### Dependencies

To enable this parameter, set **Output type** to
`Position`.

### **Limit position** — Option to limit position of mouse `off` (default) | `on`

Select whether to limit the upper and lower positions of the mouse.

#### Dependencies

To enable this parameter, set **Output type** to
`Position`.

### **Position sensitivity** — Mouse sensitivity for translations `0.0001` (default)

Mouse sensitivity for translations. Higher values correspond to higher
sensitivity.

### **Rotation sensitivity** — Mouse sensitivity for rotations `0.00001` (default)

Mouse sensitivity for rotations. Higher values correspond to higher
sensitivity.

### **Initial position** — Initial condition for translations `[0 0 0]` (default)

Initial condition for integrated translations. The software ignores this
parameter when you set **Output Type** to
`Speed`.

#### Dependencies

To enable this parameter, set **Output type** to
`Position` or `Viewpoint
coordinates`.

### **Initial rotation** — Initial condition for rotations `[0 0 0]` (default)

Initial condition for integrated rotations. The software ignores this
parameter when you set **Output Type** to
`Speed`.

#### Dependencies

To enable this parameter, set **Output type** to
`Position` or `Viewpoint
coordinates`.

### **Lower position limit** — Lower limit of mouse `[-100 -100 -100]` (default)

Position coordinates for the lower limit of the mouse.

#### Dependencies

To enable this parameter:

- Set **Output type** to
  `Position`.
- Select **Limit position**
  parameter.

### **Upper position limit** — Upper limit of mouse `[100 100 100]` (default)

Position coordinates for the upper limit of the mouse.

#### Dependencies

To enable this parameter:

- Set **Output type** to
  `Position`.
- Select **Limit position**
  parameter.

## Libraries

Simulink 3D Animation / Simulation 3D / Hardware Interface

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007b**

### R2025a: Renamed from Space Mouse Input

To reflect the Simulink® library change, the Space Mouse Input block is now
called Simulation 3D Space Mouse. The behavior remains the
same.

## Description

Process input from space mouse device

A space mouse is a device similar to a joystick in purpose, but it also provides
movement control with six degrees of freedom. This block reads the status of the space
mouse and provides some commonly used transformations of the input. The
Simulation 3D Space Mouse block supports current models of 3D navigation devices
manufactured by 3Dconnexion (`https://www.3dconnexion.com`).
