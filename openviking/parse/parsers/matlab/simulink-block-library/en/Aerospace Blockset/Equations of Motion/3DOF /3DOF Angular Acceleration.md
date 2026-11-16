---
type: simulink-block
title: '3DOF Angular Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofangularacceleration'
documentation_source_path: '3dofangularacceleration.html'
language: en
---

# 3DOF Angular Acceleration

## Ports

### Input

### **q** — Pitch angular rate scalar

Pitch angular rate, specified as a scalar, in radians per second.

**Data Types:** `double`

### **I** — Inertia tensor scalar

Inertia tensor, specified as a scalar, in the units selected in
**Units**.

**Data Types:** `double`

### **dI/dt coeff** — Rate of change of inertia tensor matrix coefficient 3-by-3 matrix

Rate of change of inertia tensor matrix coefficient, specified as a 3-by-3 matrix, in m2.

#### Dependencies

To enable this port, set **Mass type** to `Simple Variable`.

**Data Types:** `double`

### **M** — Applied pitching moment scalar

Applied pitching moment, specified as a scalar, in the units selected in
**Units**.

**Data Types:** `double`

### **dm/dt** — Rate of change of mass scalar

Rate of change of mass (positive if accreted, negative if ablated), specified as a
scalar, in the units selected in **Units**.

#### Dependencies

To enable this port, set **Mass type** to `Simple
Variable`.

**Data Types:** `double`

### **dI/dt** — Rate of change of inertia tensor scalar

Rate of change of inertia tensor,
*Iyy*,
specified as scalar, in the units selected in
**Units**.

#### Dependencies

To enable this port, set **Mass type** to
`Custom Variable`.

**Data Types:** `double`
### Output

### **dq/dt** — Pitch angular acceleration scalar

Pitch angular acceleration, returned as a scalar, in radians per second squared.

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
| `Fixed` | Mass is constant throughout the simulation. | - 3DOF (Body Axes) - 3DOF (Wind Axes) |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. | - Simple Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | Mass and inertia variations are customizable. | - Custom Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **Default:** `'Fixed'` |

## Libraries

Aerospace Blockset / Equations of Motion / Acceleration

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Compute pitch or angular acceleration of body in three-degrees-of-freedom motion

The 3DOF Angular Acceleration block computes the pitch or angular acceleration of a body
in six-degrees-of-freedom motion with respect to body-fixed coordinate frame and inertial
(flat Earth) coordinate frame.

To compute the angular acceleration for equations of motions blocks:

- Select **Output mass properties for acceleration
  computation**.
- Feed signals from the matching output ports of the associated 3DOF equation of motion
  block into the associated input ports of 3DOF Angular Acceleration.

**Tip**

Match all the parameter values for 3DOF Angular Acceleration and the 3DOF equations of
motion blocks.
