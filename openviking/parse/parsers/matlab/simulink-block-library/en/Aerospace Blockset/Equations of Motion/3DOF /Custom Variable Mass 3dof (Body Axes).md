---
type: simulink-block
title: 'Custom Variable Mass 3DOF (Body Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: 'customvariablemass3dofbodyaxes'
documentation_source_path: 'customvariablemass3dofbodyaxes.html'
language: en
---

# Custom Variable Mass 3DOF (Body Axes)

## Ports

### Input

### **Fx** — Applied force along *x*-axis scalar

Applied force along the body *x*-axis, specified as a scalar, in the
units selected in **Units**.

**Data Types:** `double`

### **Fz** — Applied force along *z*-axis scalar

Applied force along the body *z*-axis, specified as a scalar, in the
units selected in **Units**.

**Data Types:** `double`

### **M** — Applied pitching moment scalar

Applied pitching moment, specified as a scalar, in the units selected in
**Units**.

**Data Types:** `double`

### **dm/dt** — Rate of change of mass scalar

Rate of change of mass (positive if accreted, negative if ablated), specified as a
scalar.

#### Dependencies

To enable this port, select **Include mass flow relative
velocity**.

**Data Types:** `double`

### **m** — Mass scalar

Mass, specified as a scalar, in the units selected in **Units**.

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

### **I** — Inertia tensor scalar

Inertia tensor, specified as a scalar, in the units selected in
**Units**.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **g** — Gravity scalar

Gravity, specified as a scalar.

#### Dependencies

To enable this port, set **Gravity source** to
`External`.

**Data Types:** `double`

### **Vre** — Relative velocity two-element vector

Relative velocity at which mass is accreted to or ablated from the
body in body-fixed axes, specified as a two-element
vector.

#### Dependencies

To enable this port, select **Include mass flow
relative velocity**.

**Data Types:** `double`
### Output

### **θ** — Pitch attitude scalar

Pitch attitude, within ±pi, returned as a scalar, in radians (*θ*).

**Data Types:** `double`

### **q** — Pitch angular rate scalar

Pitch angular rate, returned as a scalar, in radians per second.

**Data Types:** `double`

### **dq/dt** — Pitch angular acceleration scalar

Pitch angular acceleration, returned as a scalar, in radians per second squared.

**Data Types:** `double`

### **XeZe** — Location of body two-element vector

Location of the body in the flat Earth reference frame, (*Xe, Ze*), returned
as a two-element vector.

**Data Types:** `double`

### **U w** — Velocity of body two-element vector

Velocity of the body resolved into the body-fixed coordinate frame, (*u, w*),
returned as a two-element vector.

**Data Types:** `double`

### **AxbAzb** — Acceleration of body two-element vector

Acceleration of the body with respect to the body-fixed coordinate frame, (*Ax,
Az*), returned as a two-element vector, in the units
selected in **Units**.

**Data Types:** `double`

### **AxeAze** — Acceleration of body two-element vector

Accelerations of the body with respect to the inertial (flat Earth) coordinate frame, returned
as a two-element vector. You typically connect this signal to
the accelerometer.

#### Dependencies

To enable this port, select the **Include inertial
acceleration** check box.

**Data Types:** `double`

## Parameters

### Main

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

### **Axes** — Body or wind axes `Body` (default) | `Wind`

Body or wind axes, specified as `Wind` or
`Body`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `axes` |
| **Type:** character vector |
| **Values:** `Wind` | `Body` |
| **Default:** `Body` |

### **Mass type** — Mass type `Custom Variable` (default) | `Fixed` | `Simple Variable`

Mass type, specified according to the following table.

| Mass Type | Description | Default for |
| --- | --- | --- |
| `Fixed` | Mass is constant throughout the simulation. | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | Mass and inertia variations are customizable. | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

The `Custom Variable` selection conforms to the
previously described equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **Default:** `'Custom Variable'` |

### **Initial velocity** — Initial velocity of body `100` (default) | scalar

Initial velocity of the body,
(*V*0),
specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `v_ini` |
| **Type:** character vector |
| **Values:** `'100'` | scalar |
| **Default:** `'100'` |

### **Initial body attitude** — Initial pitch altitude `0` (default) | scalar

Initial pitch attitude of the body, (*θ*0), specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `theta_ini` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:** `'0'` |

### **Initial body rotation rate** — Initial pitch rotation rate `0` (default) | scalar

Initial pitch rotation rate,
(*q*0),
specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `q_ini` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:** `'0'` |

### **Initial incidence** — Initial angle `0` (default) | scalar

Initial angle between the velocity vector and the body, (*α*0), specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `alpha_ini` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:** `'0'` |

### **Initial position (x,z)** — Initial location `[0 0]` (default) | two-element vector

Initial location of the body in the flat Earth reference frame, specified as a
two-element vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pos_ini` |
| **Type:** character vector |
| **Values:** `'[0 0]'` | two-element vector |
| **Default:** `'[0 0]'` |

### **Gravity Source** — Gravity source `Internal` (default) | `External`

Gravity source, specified as:

|  |  |
| --- | --- |
| `External` | Variable gravity input to block |
| `Internal` | Constant gravity specified in mask |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `g_in` |
| **Type:** character vector |
| **Values:** `'Internal'` | `'External'` |
| **Default:** `'Internal'` |

### **Acceleration due to gravity** — Gravity source `9.81` (default) | scalar

Acceleration due to gravity, specified as a double scalar and used if internal gravity source
is selected. If gravity is to be neglected in the simulation, this value can be set to
`0`.

#### Dependencies

- To enable this parameter, set **Gravity Source** to
  `Internal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `g` |
| **Type:** character vector |
| **Values:** `'9.81'` | scalar |
| **Default:** `'9.81'` |

### **Include mass flow relative velocity** — Mass flow relative velocity port `off` (default) | `on`

Select this check box to add a mass flow relative velocity port. This is the relative velocity at which the mass is accreted or ablated.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vre_flag` |
| **Type:** character vector |
| **Values:** `off` | `on` |
| **Default:** `'off'` |

### **Include inertial acceleration** — Include inertial acceleration port `off` (default) | `on`

Select this check box to add an inertial acceleration in flat Earth frame output port. You
typically connect this signal to the accelerometer.

#### Dependencies

To enable the **AxeAze** port, select this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `abi_flag` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### State Attributes

Assign a unique name to each state. You can use state names instead of block paths
during linearization.

- The number of names must match the number of states, as shown for each
  item, or be empty. Set all or none of the block states.
- To assign names to single-variable states, enter unique names between
  quotes, for example, `'q'` or
  `"q"`.
- To assign names to two-variable states, enter a comma-separated list
  surrounded by braces, for example, `{'Xe','Ze'}`.
- If a state parameter is empty (`' '`), no name is
  assigned.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable can
  be a character vector, cell array of character vectors, or string.

### **Velocity: e.g., {'u, 'w'}** — Velocity state name `''` (default) | comma-separated list surrounded by braces

Velocity state names, specified as a comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vel_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — Position state name `''` (default) | comma-separated list surrounded by braces

Position state names, specified as a comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pos_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Pitch angular rate e.g., 'q'** — Pitch angular rate state name `''` (default)

Pitch angular rate state name, specified as a character vector or string.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `q_statename` |
| **Type:** character vector | string |
| **Values:** `''` | scalar |
| **Default:** `''` |

### **Pitch attitude: e.g., 'theta'** — Pitch attitude state name `''` (default)

Pitch attitude state name, specified as a character vector or string.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `theta_statename` |
| **Type:** character vector | string |
| **Values:** `''` |
| **Default:** `''` |

## Libraries

Aerospace Blockset / Equations of Motion / 3DOF

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

### R2021b: Custom Variable Mass 3DOF (Body Axes) Block Changes

The 3DOF equations of motion have been updated. Existing models created prior to R2021b that contain 3DOF equations of motion blocks continue to run. If you replace a pre-R2021b version of a 3DOF equation of motion block with an R2021b or later version, your updated model might have a higher tendency for algebraic loops. For an example of how to remove algebraic loops using unit delays, see Remove Algebraic Loops. For further information about algebraic loops, see Identify Algebraic Loops in Your Model.

## Description

Implement three-degrees-of-freedom equations of motion of custom variable mass with respect to body axes

The Custom Variable Mass 3DOF (Body Axes) block implements
three-degrees-of-freedom equations of motion of custom variable mass with respect to
body axes. It considers the rotation in the vertical plane of a body-fixed coordinate
frame about a flat Earth reference frame. For more information about the rotation and
equations of motion, see Algorithms.
