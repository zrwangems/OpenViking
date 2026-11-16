---
type: simulink-block
title: 'Custom Variable Mass 6DOF Wind (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'customvariablemass6dofwindquaternion'
documentation_source_path: 'customvariablemass6dofwindquaternion.html'
language: en
---

# Custom Variable Mass 6DOF Wind (Quaternion)

## Ports

### Input

### **Fxyz** — Applied forces three-element vector

Applied forces, specified as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **Mxyz** — Applied moments three-element vector

Applied moments, specified as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **dm/dt** — Rates of change of mass scalar

One or more rates of change of mass (positive if accreted, negative if ablated), specified as
a scalar

**Data Types:** `double`

### **m** — Mass scalar

Mass, specified as a scalar.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **dI/dt** — Rate of change of inertia tensor matrix 3-by-3 matrix

Rate of change of inertia tensor matrix, specified as a 3-by-3 matrix, in the units selected
in **Units**.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **I** — Inertia tensor matrix 3-by-3 matrix

Inertia tensor matrix, specified as a 3-by-3 matrix.

#### Dependencies

To enable this port, set **Mass type** to `Custom
Variable`.

**Data Types:** `double`

### **Vre** — Relative velocities three-element vector

One or more relative velocities at which the mass is accreted to or ablated from the body in
body-fixed axes, specified as a three-element vector.

#### Dependencies

To enable this port, select **Include mass flow relative velocity**.

**Data Types:** `double`
### Output

### **Ve** — Velocity in flat Earth reference frame three-element vector

Velocity in the flat Earth reference frame, returned as a three-element vector.

**Data Types:** `double`

### **Xe** — Position in flat Earth reference frame three-element vector

Position in the flat Earth reference frame, returned as a three-element vector.

**Data Types:** `double`

### **μ γ x (rad)** — Wind rotation angles three-element vector

Wind rotation angles [bank, flight path, heading], returned as a three-element vector, in
radians.

**Data Types:** `double`

### **DCMwe** — Coordinate transformation 3-by-3 matrix

Coordinate transformation from flat Earth axes to wind-fixed axes, returned as a 3-by-3 matrix.

**Data Types:** `double`

### **Vw** — Velocity in wind-fixed frame three-element vector

Velocity in wind-fixed frame, returned as a three-element vector.

**Data Types:** `double`

### **α β (rad)** — Angle of attack and sideslip angle two-element vector

Angle of attack and sideslip angle, returned as a two-element vector, in radians.

**Data Types:** `double`

### **dα/dt dβ/dt** — Rate of change of angle of attack and rate of change of sideslip angle two-element vector

Rate of change of angle of attack and rate of change of sideslip angle, returned as a two-element vector, in radians per second.

**Data Types:** `double`

### **ωb (rad/s)** — Angular rates in body-fixed axes three-element vector

Angular rates in body-fixed axes, returned as a three-element vector, in radians per second.

**Data Types:** `double`

### **dωb/dt** — Angular accelerations three-element vector

Angular accelerations in body-fixed axes, returned as a three-element vector, in radians per second squared.

**Data Types:** `double`

### **Abb** — Accelerations in body-fixed axes three-element vector

Accelerations of the body with respect to the body-fixed axes with the body-fixed coordinate
frame, returned as a three-element vector, in the units selected in
**Units**.

**Data Types:** `double`

### **Abe** — Accelerations with respect to inertial frame three-element vector

Accelerations in body-fixed axes with respect to inertial frame (flat Earth), returned as a three-element vector. You typically connect this signal to the accelerometer.

#### Dependencies

To enable this point, select **Include inertial acceleration**.

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

### **Mass type** — Mass type `Custom Variable` (default) | `Fixed` | `Simple Variable`

Mass type, specified as:

|  |  |
| --- | --- |
| `Fixed` | Mass is constant throughout the simulation (see 6DOF ECEF (Quaternion)). |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. |
| `Custom Variable` | Mass and inertia variations are customizable (see Custom Variable Mass 6DOF ECEF (Quaternion)). |

The `Custom Variable` selection conforms to the previously described
equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **Default:** `'Custom Variable'` |

### **Representation** — Equations of motion representation `Quaternion` (default) | `Wind Angles`

Equations of motion representation, specified according to the following table.

|  |  |
| --- | --- |
| `Quaternion` | Use quaternions within equations of motion. |
| `Wind Angles` | Use wind angles within equations of motion. |

The `Quaternion` selection conforms to the equations of motion in Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rep` |
| **Type:** character vector |
| **Values:** `Wind Angles` | `Quaternion` |
| **Default:** `'Quaternion'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — Position in inertial axes `[0 0 0]` (default) | three-element vector

Initial location of the body in the flat Earth reference frame, specified as a three-element vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `xme_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Initial airspeed, angle of attack, and sideslip angle [V,alpha,beta]** — Initial airspeed, angle of attack, and sideslip angle `[0 0 0]` (default) | three-element vector

Initial airspeed, angle of attack, and sideslip angle, specified as a three-element vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Vm_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Initial wind orientation [bank angle,flight path angle,heading angle]** — Initial wind orientation `[0 0 0]` (default) | three-element vector

Initial wind angles [bank, flight path, and heading], specified as a three-element vector in
radians.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `wind_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — Initial body rotation `[0 0 0]` (default) | three-element vector

Initial body-fixed angular rates with respect to the NED frame, specified as a three-element
vector, in radians per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pm_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Include mass flow relative velocity** — Mass flow relative velocity port `off` (default) | `on`

Select this check box to add a mass flow relative velocity port. This is the relative velocity at which the mass is accreted or ablated.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vre_flag` |
| **Type:** character vector |
| **Values:** `off` | `on` |
| **Default:** `off` |

### **Include inertial acceleration** — Include inertial acceleration port `off` (default) | `on`

Select this check box to add an inertial acceleration port.

#### Dependencies

To enable the **Ab ff** port, select this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `abi_flag` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `off` |

### State Attributes

Assign a unique name to each state. Use state names instead of block paths throughout the
linearization process.

- To assign a name to a single state, enter a unique name between quotes,
  for example, `'velocity'`.
- To assign names to multiple states, enter a comma-separated list
  surrounded by braces, for example, `{'a', 'b', 'c'}`. Each
  name must be unique.
- If a parameter is empty (`' '`), no name is
  assigned.
- The state names apply only to the selected block with the name
  parameter.
- The number of states must divide evenly among the number of state
  names.
- You can specify fewer names than states, but you cannot specify more names
  than states.

  For example, you can specify two names in a system with four states. The
  first name applies to the first two states and the second name to the last
  two states.
- To assign state names with a variable in the MATLAB® workspace, enter the variable without quotes. A variable can
  be a character vector, cell array, or structure.

### **Position: e.g., {'Xe','Ye','Ze'}** — Position state name `''` (default) | comma-separated list surrounded by braces

Position state names, specified as a comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `xme_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Velocity: e.g., 'V'** — Velocity state name `''` (default) | character vector

Velocity state names, specified as a character vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Vm_statename` |
| **Type:** character vector |
| **Values:** `''` | character vector |
| **Default:** `''` |

### **Incidence angle e.g., 'alpha'** — Incidence angle state name `''` (default) | character vector

Incidence angle state name, specified as a character vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `alpha_statename` |
| **Type:** character vector |
| **Values:** `''` |
| **Default:** `''` |

### **Sideslip angle e.g., 'beta'** — Sideslip angle state name `''` (default) | character vector

Sideslip angle state name, specified as a character vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `beta_statename` |
| **Type:** character vector |
| **Values:** `''` |
| **Default:** `''` |

### **Quaternion: e.g., {'qr','qi','qj','qk'}** — Quaternion vector state name `''` (default) | comma-separated list surrounded by braces

Quaternion vector state names, specified as a comma-separated list surrounded by
braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `quat_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — Body rotation state names `''` (default) | comma-separated list surrounded by braces

Body rotation rate state names, specified comma-separated list surrounded by
braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pm_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

## Libraries

Aerospace Blockset / Equations of Motion / 6DOF

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

## Description

Implement quaternion representation of six-degrees-of-freedom equations of motion of custom variable mass with respect to wind axes

The Custom Variable Mass 6DOF Wind (Quaternion) block
implements a quaternion representation of six-degrees-of-freedom equations of motion of
custom variable mass with respect to wind axes. It considers the rotation of a
wind-fixed coordinate frame
(*Xw*,*Yw*,
*Zw*) about an flat Earth reference
frame
(*Xe*,*Ye*,
*Ze*). The origin of the wind-fixed
coordinate frame is the center of gravity of the body. For more information on the
wind-fixed coordinate frame, see Algorithms.

Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention.
