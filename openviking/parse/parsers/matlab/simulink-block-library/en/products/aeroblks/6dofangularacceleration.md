---
type: simulink-block
title: '6DOF Angular Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Equations of Motion / 6DOF'
documentation_page: '6dofangularacceleration'
documentation_source_path: '6dofangularacceleration.html'
language: en
---

# 6DOF Angular Acceleration

## Ports

### Input

### **ωb (rad/s)** — Angular rates in body-fixed axes three-element vector

Angular rates in body-fixed axes, specified as a three-element vector, in radians per second.

**Data Types:** `double`

### **I** — Inertia tensor matrix 3-by-3 matrix

Inertia tensor matrix, specified as a 3-by-3 matrix, in the units selected in
**Units**.

**Data Types:** `double`

### **dI/dt coeff** — Rate of change of inertia tensor matrix coefficient 3-by-3 matrix

Rate of change of inertia tensor matrix coefficient, specified as a 3-by-3 matrix.

#### Dependencies

To enable this port, set **Mass type** to `Simple
Variable`, in m2.

**Data Types:** `double`

### **Mxyz** — Applied moments three-element vector

Applied moments, specified as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **dI/dt** — Rate of change of inertia tensor matrix 3-by-3 matrix

Rate of change of inertia tensor matrix, specified as a 3-by-3 matrix, in the units selected
in **Units**.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **dm/dt** — Rates of change of mass scalar

One or more rates of change of mass (positive if accreted, negative if ablated), specified as
a scalar, in the units selected in **Units**.

#### Dependencies

To enable this port, set **Mass type** to `Simple Variable`.

**Data Types:** `double`
### Output

### **dωb/dt** — Angular accelerations three-element vector

Angular accelerations in body-fixed axes, returned as a three-element vector, in radians per second squared.

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

## Libraries

Aerospace Blockset / Equations of Motion / Acceleration

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Compute angular acceleration of body in six-degrees-of-freedom motion

The 6DOF Angular Acceleration computes the angular acceleration of a body
in six-degrees-of-freedom motion. Use this block for only these 6DOF equations of motion
blocks:

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

To compute the angular acceleration for these blocks:

- Select **Output mass properties for acceleration
  computation**.
- Feed signals from the matching output ports of the associated 6DOF equation of motion
  block into the associated input ports of 6DOF Angular Acceleration.

**Tip**

Match all the parameter values for 6DOF Angular Acceleration and the 6DOF equations of
motion blocks.
