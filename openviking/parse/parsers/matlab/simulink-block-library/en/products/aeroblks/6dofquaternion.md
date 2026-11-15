---
type: simulink-block
title: '6DOF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofquaternion'
documentation_source_path: '6dofquaternion.html'
language: en
---

# 6DOF (Quaternion)

## Ports

### Input

### **Fxyz(N)** — Applied forces three-element vector

Applied forces, specified as a three-element vector in body-fixed
axes. For more information on the frame, see Body Coordinates.

**Data Types:** `double`

### **Mxyz(N-m)** — Applied moments three-element vector

Applied moments, specified as a three-element vector in body-fixed
axes. For more information on the frame, see Body Coordinates.

**Data Types:** `double`
### Output

### **Ve** — Velocity in flat Earth reference frame three-element vector

Velocity in the flat Earth reference frame, returned as a
three-element vector.

**Data Types:** `double`

### **Xe** — Position in flat Earth reference frame three-element vector

Position in the flat Earth reference frame, returned as a
three-element vector.

**Data Types:** `double`

### **φ θ ψ (rad)** — Euler rotation angles three-element vector

Euler rotation angles [roll, pitch, yaw] defining an intrinsic
*x*-*y*-*z*
rotation, as a three-element vector, in radians. Yaw, pitch, and roll
angles are applied using the
*z*-*y*-*x*
rotation sequence, such as
`angle2dcm(yaw,pitch,roll,"ZYX")`.

**Data Types:** `double`

### **q** — Quaternion 4-by-1 vector

Quaternion that represents a transformation from flat Earth axes to
body-fixed axes, returned as a 4-by-1 vector.

**Data Types:** `double`

### **DCMbe** — Coordinate transformation 3-by-3 matrix

Coordinate transformation from flat Earth axes to body-fixed axes,
returned as a 3-by-3 matrix.

**Data Types:** `double`

### **Vb** — Velocity in the body-fixed frame three-element vector

Velocity in the body-fixed frame, returned as a three-element
vector.

**Data Types:** `double`

### **ωb (rad/s)** — Angular rates in body-fixed axes three-element vector

Angular rates in body-fixed axes, returned as a three-element vector,
in radians per second.

**Data Types:** `double`

### **m** — Mass scalar

Mass, returned as a scalar.

#### Dependencies

To enable this port, select the **Output mass properties
for acceleration computation** parameter.

**Data Types:** `double`

### **I** — Inertia tensor matrix 3-by-3 matrix

Inertia tensor matrix, returned as a 3-by-3 matrix.

#### Dependencies

To enable this port, select the **Output mass properties
for acceleration computation** parameter.

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

### **Mass type** — Mass type `Fixed` (default) | `Simple Variable` | `Custom Variable`

Mass type, specified according to the following table.

| Mass Type | Description | Default for |
| --- | --- | --- |
| `Fixed` | Mass is constant throughout the simulation. | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | Mass and inertia variations are customizable. | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

The `Simple Variable` selection conforms to the previously described
equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **Default:** `'Fixed'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — Position in inertial axes `[0 0 0]` (default) | three-element vector

Initial location of the body in the flat Earth reference frame, specified as a three-element vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `xme_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Initial velocity in body axes [U,v,w]** — Velocity in body axes `[0 0 0]` (default) | three-element vector

Initial velocity in body axes, specified as a three-element vector, in the body-fixed
coordinate frame.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Vm_0` |
| **Type:** character vector |
| **Values:** `'[0 0 0]'` | three-element vector |
| **Default:** `'[0 0 0]'` |

### **Initial Euler orientation [roll, pitch, yaw]** — Initial Euler orientation `[0 0 0]` (default) | three-element vector

Initial Euler orientation angles [roll, pitch, yaw], specified as a three-element vector, in
radians. Euler rotation angles are those between the body and
north-east-down (NED) coordinate systems.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `eul_0` |
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

### **Inertia** — Inertia `eye(3)` (default) | scalar

Inertia of the body, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Mass type** to
`Fixed`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `inertia` |
| **Type:** character vector |
| **Values:** `eye(3)` | double scalar |
| **Default:** `eye(3)` |

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

### **Velocity: e.g., {'U','v','w'}** — Velocity state name `''` (default) | comma-separated list surrounded by braces

Velocity state names, specified as comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Vm_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
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

### **Output mass properties for acceleration computation** — Include mass properties for acceleration port `off` (default) | `on`

Select this check box to enable ports for mass properties for acceleration. You can
then use these ports as inputs for these blocks:

- 6DOF Acceleration — **m** output port
- 6DOF Angular Acceleration — **I** and **dI/dt
  coeff** ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mass_flag` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `off` |

## Libraries

Aerospace Blockset / Equations of Motion / 6DOF

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

### R2025a: 6DOF equations of motion block acceleration ports removed

As a result of the removal of the acceleration ports, the **Include
inertial acceleration** parameter has been replaced with
**Output mass properties for acceleration computation** for
6DOF (Quaternion).

Related to this change, the block parameters and output ports have changed:

| Block | Ports | Parameters |
| --- | --- | --- |
| 6DOF (Quaternion) | - dωb/dt removed - Abb removed - Abe removed | - **Representation** removed - **Gain for quaternion   normalization** removed |

As a result of the changes, the block output dimension has changed from a 2D row
vector, such as a 2-by-*N* vector, to a 1D vector,
*N*. *N* is the number of elements.

## Description

Implement quaternion representation of six-degrees-of-freedom equations of motion with respect to body axes

The 6DOF (Quaternion) block implements quaternion representation of
six-degrees-of-freedom equations of motion with respect to body axes. For a description
of the coordinate system and the translational dynamics, see the block description for
the 6DOF (Euler Angles) block.

For more information on the integration of the rate of change of the quaternion
vector, see Algorithms.

The 6DOF (Quaternion), Simple Variable Mass 6DOF (Quaternion), and Custom Variable Mass 6DOF (Quaternion) blocks are alternative
configurations of the same block.

- 6DOF (Quaternion) — Implement quaternion representation of six-degrees-of-freedom
  equations of motion with respect to body axes
- Simple Variable Mass 6DOF (Quaternion) — Implement quaternion
  representation of six-degrees-of-freedom equations of motion of simple variable
  mass with respect to body axes
- Custom Variable Mass 6DOF (Quaternion) — Implement quaternion
  representation of six-degrees-of-freedom equations of motion of custom variable
  mass with respect to body axes
