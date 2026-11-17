---
type: simulink-block
title: '3DOF Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofacceleration'
documentation_source_path: '3dofacceleration.html'
language: en
---

# 3DOF Acceleration

## Ports
```yaml
ports:
- name: θ
  summary: Pitch altitude scalar
  direction: input
  data_types: double
- name: γ
  summary: Flight path angle scalar
  direction: input
  data_types: double
- name: q
  summary: Pitch angular rate scalar
  direction: input
  data_types: double
- name: Vw
  summary: Velocity in wind-fixed frame two-element vector
  direction: input
  data_types: double
- name: U w
  summary: Velocity of body two-element vector
  direction: input
  data_types: double
- name: α
  summary: Angle of attack scalar
  direction: input
  data_types: double
- name: g
  summary: Gravity scalar
  direction: input
  data_types: double
- name: Fuel
  summary: Fuel tank status scalar
  direction: input
  data_types: double
- name: m
  summary: Mass scalar
  direction: input
  data_types: double
- name: Fx
  summary: Applied force along *x*-axis scalar
  direction: input
  data_types: double
- name: Fz
  summary: Applied force along *z*-axis scalar
  direction: input
  data_types: double
- name: dm/dt
  summary: Rate of change of mass scalar
  direction: input
  data_types: double
- name: I
  summary: Inertia tensor scalar
  direction: input
  data_types: double
- name: Vre
  summary: Relative velocity two-element vector
  direction: input
  data_types: double
- name: AxbAzb
  summary: Acceleration of body two-element vector
  direction: output
  data_types: double
- name: AxeAze
  summary: Acceleration of body two-element vector
  direction: output
  data_types: double
```

### Input

### **θ** — Pitch altitude scalar

Pitch attitude, within ±pi, specified as a scalar, in radians.

#### Dependencies

To enable this port, set **Axes** to
`Body`.

**Data Types:** `double`

### **γ** — Flight path angle scalar

Flight path angle, within ±pi, specified as a scalar, in radians.

#### Dependencies

To enable this port, set **Axes** to
`Wind`.

**Data Types:** `double`

### **q** — Pitch angular rate scalar

Pitch angular rate, specified as a scalar, in radians per second.

**Data Types:** `double`

### **Vw** — Velocity in wind-fixed frame two-element vector

Velocity of the body resolved into the wind-fixed coordinate frame, (*V,
0*), returned as a two-element vector, in the units selected in
**Units**.

#### Dependencies

To enable this port, set **Axes** to
`Wind`.

**Data Types:** `double`

### **U w** — Velocity of body two-element vector

Velocity of the body resolved into the body-fixed coordinate frame, (*u, w*),
specified as a two-element vector, in the units selected in
**Units**.

#### Dependencies

To enable this port, set **Axes** to
`Body`.

**Data Types:** `double`

### **α** — Angle of attack scalar

Angle of attack, returned as a scalar, in radians.

#### Dependencies

To enable this port, set **Axes** to
`Wind`.

**Data Types:** `double`

### **g** — Gravity scalar

Gravity, specified as a scalar, in the units selected in
**Units**.

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

### **Fx** — Applied force along *x*-axis scalar

Applied force along the body *x*-axis, specified as a scalar, in the
units selected in **Units**.

**Data Types:** `double`

### **Fz** — Applied force along *z*-axis scalar

Applied force along the body *z*-axis, specified as a scalar, in the
units selected in **Units**.

**Data Types:** `double`

### **dm/dt** — Rate of change of mass scalar

Rate of change of mass (positive if accreted, negative if ablated), specified as a scalar, in
the units selected in **Units**.

#### Dependencies

To enable this port:

- Set **Mass type** to `Simple Variable` or `Custom Variable`.
- Select **Include mass flow relative velocity**.

**Data Types:** `double`

### **I** — Inertia tensor scalar

Inertia tensor, specified as a scalar, in the units selected in
**Units**.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **Vre** — Relative velocity two-element vector

Relative velocity at which mass is accreted to or ablated from the body in body-fixed axes,
specified as a two-element vector, in the units selected in
**Units**.

#### Dependencies

To enable this port:

- Set **Mass type** to `Simple
  Variable` or `Custom
  Variable`.
- Select **Include mass flow relative velocity**.

**Data Types:** `double`
### Output

### **AxbAzb** — Acceleration of body two-element vector

Acceleration of the body with respect to the body-fixed coordinate frame, (*Ax,
Az*), returned as a two-element vector, in the units
selected in **Units**.

**Data Types:** `double`

### **AxeAze** — Acceleration of body two-element vector

Accelerations of the body with respect to the inertial (flat Earth) coordinate
frame, returned as a two-element vector, in the units selected in
**Units**. You typically connect this signal to the
accelerometer.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Input and output units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: Metric (MKS) | English (Velocity in ft/s) | English (Velocity in kts)
  default: Metric (MKS)
- name: Mass type
  summary: Mass type Fixed (default) | Simple Variable | Custom Variable
  group: ''
  block_parameter: mtype
  type: character vector
  values: Fixed | Simple Variable | Custom Variable
  default: '''Fixed'''
- name: Axes
  summary: Body or wind axes Body (default) | Wind
  group: ''
  block_parameter: axes
  type: character vector
  values: Wind | Body
  default: Body
```

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

### **Axes** — Body or wind axes `Body` (default) | `Wind`

Body or wind axes, specified as `Wind` or `Body`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `axes` |
| **Type:** character vector |
| **Values:** `Wind` | `Body` |
| **Default:** `Body` |
## Libraries

Aerospace Blockset / Equations of Motion / Acceleration

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Compute acceleration of body in three-degrees-of-freedom motion

The 3DOF Acceleration block computes the acceleration of a body in
three-degrees-of-freedom motion with respect to body-fixed coordinate frame and inertial (flat
Earth) coordinate frame.

To compute the acceleration for equations of motions blocks:

- Select **Output mass properties for acceleration
  computation**.
- Feed signals from the matching output ports of the associated 3DOF equation of motion
  block into the associated input ports of 3DOF Acceleration.

**Tip**

Match all the parameter values for 3DOF Acceleration and the 3DOF equations of
motion blocks.
