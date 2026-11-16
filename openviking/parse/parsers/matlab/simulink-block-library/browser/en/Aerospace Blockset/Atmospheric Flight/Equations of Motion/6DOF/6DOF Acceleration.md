---
type: simulink-block
title: '6DOF Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Equations of Motion / 6DOF'
documentation_page: '6dofacceleration'
documentation_source_path: '6dofacceleration.html'
language: en
---

# 6DOF Acceleration

## Ports

### Input

### **Vb** — Velocity in body-fixed frame three-element vector

Velocity in body-fixed frame, specified as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **ωb (rad/s)** — Angular rates in body-fixed axes three-element vector

Angular rates in body-fixed axes, specified as a three-element vector, in radians per second.

**Data Types:** `double`

### **Fuel** — Fuel tank status scalar

Fuel tank status, specified as:

- `1` — Tank is full.
- `0` — Tank is neither full nor empty.
- `-1` — Tank is empty.

#### Dependencies

To enable this port, set **Mass type** to `Simple
Variable`.

**Data Types:** `double`

### **m** — Mass scalar

Mass, specified as a scalar, in the units selected in **Units**.

**Data Types:** `double`

### **Fxyz** — Applied forces three-element vector

Applied forces, specified as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **dm/dt** — Rates of change of mass scalar

One or more rates of change of mass (positive if accreted, negative if ablated), specified as
a scalar, in the units selected in **Units**.

#### Dependencies

To enable this port, set **Mass type** to `Simple Variable` or `Custom Variable`.

**Data Types:** `double`

### **Vre** — Relative velocities three-element vector

One or more relative velocities at which the mass is accreted to or ablated from the body in
body-fixed axes, specified as a three-element vector, in the units selected in
**Units**.

#### Dependencies

To enable this port:

- Set **Mass type** to `Simple Variable` or `Custom Variable`.
- Select **Include mass flow relative velocity**.

**Data Types:** `double`
### Output

### **Abb** — Accelerations in body-fixed axes three-element vector

Accelerations of the body with respect to the body-fixed axes with the body-fixed coordinate
frame, returned as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **Abe** — Accelerations with respect to inertial frame three-element vector

Accelerations in body-fixed axes with respect to inertial frame (flat Earth), returned as a
three-element vector. You typically connect this signal to the accelerometer, in the
units selected in **Units**.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Units** — Input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as `Metric (MKS)`, `English (Velocity in ft/s)`, or `English (Velocity in kts)`.

| Units | Forces | Moment | Acceleration | Velocity | Position | Mass | Inertia |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **Default:** `Metric (MKS)` |

### **Mass type** — Mass type `Fixed` (default) | `Simple Variable` | `Custom Variable`

Mass type, specified according to the following table.

| Mass Type | Description | Default for |
| --- | --- | --- |
| `Fixed` | Mass is constant throughout the simulation. | - 6DOF (Euler Angles) - 6DOF (Quaternion) |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. | - Simple Variable Mass 6DOF (Euler Angles) - Simple Variable Mass 6DOF (Quaternion) |
| `Custom Variable` | Mass and inertia variations are customizable. | - Custom Variable Mass 6DOF (Euler Angles) - Custom Variable Mass 6DOF (Quaternion) |

The `Simple Variable` selection conforms to the previously described equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **Default:** `'Fixed'` |

### **Include mass flow relative velocity** — Mass flow relative velocity port `off` (default) | `on`

Select this check box to add a mass flow relative velocity port. This is the relative velocity at which the mass is accreted or ablated.

#### Dependencies

To enable this parameter, set **Mass type** to `Simple Variable` or `Custom Variable`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vre_flag` |
| **Type:** character vector |
| **Values:** `off` | `on` |
| **Default:** `off` |

## Libraries

Aerospace Blockset / Equations of Motion / Acceleration

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Compute acceleration of body in six-degrees-of-freedom motion

The 6DOF Acceleration block computes the acceleration of a body in
six-degrees-of-freedom motion with respect to body-fixed coordinate frame and inertial (flat
Earth) coordinate frame. Use this block for only these 6DOF equations of motion blocks:

- 6DOF (Euler Angles)
- 6DOF (Quaternion)
- Custom Variable Mass 6DOF (Euler
  Angles)
- Custom Variable Mass 6DOF
  (Quaternion)
- Simple Variable Mass 6DOF (Euler
  Angles)
- Simple Variable Mass 6DOF
  (Quaternion)

To compute the acceleration for these blocks:

- Select **Output mass properties for acceleration
  computation**.
- Feed signals from the matching output ports of the associated 6DOF equation of motion
  block into the associated input ports of 6DOF Acceleration.

**Tip**

Match all the parameter values for 6DOF Acceleration and the 6DOF equations of
motion blocks.
