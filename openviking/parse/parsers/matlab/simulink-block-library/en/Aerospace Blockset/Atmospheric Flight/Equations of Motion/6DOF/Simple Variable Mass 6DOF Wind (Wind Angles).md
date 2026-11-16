---
type: simulink-block
title: 'Simple Variable Mass 6DOF Wind (Wind Angles)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofwindwindangles'
documentation_source_path: 'simplevariablemass6dofwindwindangles.html'
language: en
---

# Simple Variable Mass 6DOF Wind (Wind Angles)

## Ports

### Input

### **Fxyz(N)** — Applied forces three-element vector

Applied forces, specified as a three-element vector.

**Data Types:** `double`

### **Mxyz(N-m)** — Applied moments three-element vector

Applied moments, specified as a three-element vector.

**Data Types:** `double`

### **dm/dt (kg/s)** — Rate of change of mass scalar

One or more rates of change of mass (positive if accreted, negative if ablated), specified as a scalar.

**Data Types:** `double`

### **Vre** — Relative velocity three-element vector

One or more relative velocities, specified as a three-element vector, at which the mass is accreted to or ablated from the body in body-fixed axes.

#### Dependencies

To enable this port, select **Include mass flow relative
velocity**.

**Data Types:** `double`
### Output

### **Ve** — Velocity in flat Earth reference frame three-element vector

Velocity in the flat Earth reference frame, returned as a three-element vector.

**Data Types:** `double`

### **Xe** — Position in flat Earth reference frame three-element vector

Position in the flat Earth reference frame, returned as a three-element vector.

**Data Types:** `double`

### **μ γ x (rad)** — Wind rotation angles three-element vector

Wind rotation angles [bank, flight path, heading], returned as three-element vector, in radians.

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

Angular rates in body-fixed axes, returned as a three-element vector.

**Data Types:** `double`

### **dωb/dt** — Angular accelerations in body-fixed axes three-element vector

Angular accelerations in body-fixed axes, returned as a three-element vector, in radians per second squared.

**Data Types:** `double`

### **Abb** — Accelerations in body-fixed axes three-element vector

Accelerations in body-fixed axes with respect to body frame, returned as a three-element vector.

**Data Types:** `double`

### **Fuel** — Fuel tank status scalar

Fuel tank status, returned as:

- `1` — Tank is full.
- `0` — Tank is neither full nor empty.
- `-1` — Tank is empty.

**Data Types:** `double`

### **Abe** — Accelerations with respect to inertial frame three-element vector

Accelerations in body-fixed axes with respect to inertial frame (flat Earth), returned as a three-element vector. You typically connect this signal to the accelerometer.

#### Dependencies

This port appears only when the **Include inertial acceleration** check box is selected.

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

### **Mass type** — Mass type `Simple Variable` (default) | `Fixed` | `Custom Variable`

Mass type, specified as:

|  |  |
| --- | --- |
| `Fixed` | Mass is constant throughout the simulation (see 6DOF ECEF (Quaternion)). |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. |
| `Custom Variable` | Mass and inertia variations are customizable (see Custom Variable Mass 6DOF ECEF (Quaternion)). |

The `Simple Variable` selection conforms to the previously described equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **Default:** `'Simple Variable'` |

### **Representation** — Equations of motion representation `Wind Angles` (default) | `Quaternion`

Equations of motion representation, specified according to the following table.

| Representation | Description |
| --- | --- |
| `Wind Angles` | Use Wind angles within equations of motion. |
| `Quaternion` | Use quaternions within equations of motion. |

The `Quaternion` selection conforms to the equations of motion in Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rep` |
| **Type:** character vector |
| **Values:** `Wind Angles` | `Quaternion` |
| **Default:** `'Wind Angles'` |

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

### **Initial mass** — Initial mass `1.0` (default) | scalar

Initial mass of the rigid body, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass_0` |
| **Type:** character vector |
| **Values:** `'1.0'` | double scalar |
| **Default:** `'1.0'` |

### **Empty mass** — Empty mass `0.5` (default) | scalar

Empty mass of the body, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass_e` |
| **Type:** character vector |
| **Values:** double scalar |
| **Default:** `'0.5'` |

### **Full mass** — Full mass of body `2.0` (default) | scalar

Full mass of the body, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass_f` |
| **Type:** character vector |
| **Values:** double scalar |
| **Default:** `'2.0'` |

### **Empty inertia matrix in body axis** — Inertia tensor matrix for empty inertia `eye(3)` (default) | 3-by-3 matrix

Inertia tensor matrix for the empty inertia of the body, specified as 3-by-3 matrix, in body-fixed axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertia_e` |
| **Type:** character vector |
| **Values:** `'eye(3)'` | 3-by-3 matrix |
| **Default:** `'eye(3)'` |

### **Full inertia matrix in body axis** — Inertia tensor matrix for full inertia `2*eye(3)` (default) | 3-by-3 matrix

Inertia tensor matrix for the full inertia of the body, specified as a 3-by-3 matrix, in body-fixed axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertia_f` |
| **Type:** character vector |
| **Values:** `'2*eye(3)'` | 3-by-3 matrix |
| **Default:** `'2*eye(3)'` |

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

Assign a unique name to each state. You can use state names instead of block paths during
linearization.

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

### **Wind orientation e.g., {'mu', 'gamma', 'chi'}** — Wind orientation state names `''` (default) | comma-separated list surrounded by braces

Wind orientation state names, specified as a comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `wind_statename` |
| **Type:** character vector |
| **Values:** `''` |
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

### **Mass: e.g., 'mass'** — Mass state name `''` (default) | character vector

Mass state name, specified as a character vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass_statename` |
| **Type:** character vector |
| **Values:** `''` | character vector |
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

Implement wind angle representation of six-degrees-of-freedom equations of motion of simple variable mass

The Simple Variable Mass 6DOF Wind (Wind Angles) block implements a wind
angle representation of six-degrees-of-freedom equations of motion of simple variable
mass. For more information of the relationship between the wind angles, see Algorithms.
For a description of the coordinate system employed and the translational dynamics, see
the block description for the Simple Variable Mass 6DOF (Quaternion)
block.
