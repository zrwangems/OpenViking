---
type: simulink-block
title: '6DOF ECEF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofecefquaternion'
documentation_source_path: '6dofecefquaternion.html'
language: en
---

# 6DOF ECEF (Quaternion)

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

### **LG(0)** — Initial celestial longitude of Greenwich scalar

Greenwich meridian initial celestial longitude angle, specified as a scalar.

#### Dependencies

To enable this port

- Set **Celestial longitude of Greenwich** to
  `External`.
- set **Planet model** to
  `Earth`.

**Data Types:** `double`

### **LPM(0)** — Prime meridian initial celestial longitude angle scalar

Prime meridian initial celestial longitude angle, specified as a scalar.

#### Dependencies

To enable this port

- Set **Celestial longitude of prime meridian** to
  `External`.
- Set **Planet model** to
  `Custom`.

**Data Types:** `double`
### Output

### **Vff** — Velocity of body with respect to ECEF frame, three-element vector

Velocity of body with respect to ECEF frame, expressed in ECEF frame, returned as a
three-element vector.

**Data Types:** `double`

### **Xff** — Position in ECEF reference frame three-element vector

Position in ECEF reference frame, returned as a three-element vector.

**Data Types:** `double`

### **μ l h** — Position in geodetic latitude, longitude, and altitude three-element vector | M-by-3 array

Position in geodetic latitude, longitude, and altitude, in degrees, returned as a
three-element vector or M-by-3 array, in selected units of
length, respectively.

**Data Types:** `double`

### **φ θ Ψ (rad)** — Body rotation angles three-element vector

Body rotation angles [roll, pitch, yaw], returned as a three-element vector, in radians. Euler rotation angles are those between body and NED coordinate systems.

**Data Types:** `double`

### **DCMbi** — Coordinate transformation from ECI axes 3-by-3 matrix

Coordinate transformation from ECI axes to body-fixed axes, returned as a 3-by-3
matrix.

**Data Types:** `double`

### **DCMbe** — Coordinate transformation from NED axes to body-fixed axes 3-by-3 matrix

Coordinate transformation from NED axes to body-fixed axes, returned
as a 3-by-3 matrix.

**Data Types:** `double`

### **DCMef** — Coordinate transformation from fixed-frame axes 3-by-3 matrix

Coordinate transformation from fixed-frame axes to NED axes, returned as a 3-by-3
matrix.

**Data Types:** `double`

### **Vb** — Velocity of body with respect to fixed-frame three-element vector

Velocity of body with respect to fixed-frame, returned as a three-element
vector.

**Data Types:** `double`

### **ωrel** — Relative angular rates of body with respect to NED frame three-element vector

Relative angular rates of body with respect to NED frame, expressed in body frame and returned as a three-element vector, in radians per second.

**Data Types:** `double`

### **ωb** — Angular rates of body with respect to inertial frame three-element vector

Angular rates of the body with respect to inertial frame, expressed in body frame and
returned as a three-element vector, in radians per second.

**Data Types:** `double`

### **dωb/dt** — Angular accelerations of the body with respect to inertial frame three-element vector

Angular accelerations of the body with respect to inertial frame, expressed in body
frame and returned as a three-element vector, in radians per second squared.

**Data Types:** `double`

### **Abb** — Accelerations in body-fixed axes three-element vector

Accelerations of the body with respect to the fixed-frame, returned as a three-element
vector.

**Data Types:** `double`

### **Ab ff** — Accelerations in body-fixed axes three-element vector

Accelerations in body-fixed axes with respect to fixed-frame, returned as a
three-element vector.

#### Dependencies

To enable this point, **Include inertial acceleration**.

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

Select the type of mass to use:

| Mass Type | Description | Default for |
| --- | --- | --- |
| `Fixed` | Mass is constant throughout the simulation. | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind   (Wind Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | Mass and inertia vary linearly as a function of mass rate. | - Simple   Variable Mass 6DOF (Euler Angles) - Simple   Variable Mass 6DOF (Quaternion) - Simple   Variable Mass 6DOF Wind (Wind   Angles) - Simple   Variable Mass 6DOF Wind   (Quaternion) - Simple   Variable Mass 6DOF ECEF   (Quaternion) |
| `Custom Variable` | Mass and inertia variations are customizable. | - Custom   Variable Mass 6DOF (Euler Angles) - Custom   Variable Mass 6DOF (Quaternion) - Custom   Variable Mass 6DOF Wind (Wind   Angles) - Custom   Variable Mass 6DOF Wind   (Quaternion) - Custom   Variable Mass 6DOF ECEF   (Quaternion) |

The `Fixed` selection conforms to the previously
described equations of motion.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `mtype` |
| **Type:** character vector |
| **Values:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **Default:** `'Simple Variable'` |

### **Initial position in geodetic latitude, longitude and altitude [mu,l,h]** — Initial location of rigid body `[0 0 0]` (default) | three-element vector

Initial location of the rigid body in the geodetic
reference frame, specified as a three-element
vector. Latitude and longitude values can be any
value. However, latitude values of +90 and -90 may
return unexpected values because of singularity at
the poles.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `xg_0` |
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

### Planet

### **Planet model** — Planet model `Earth (WGS84)` (default) | `Custom`

Planet model to use, `Custom` or `Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'Earth (WGS84)'` | `'Custom'` |
| **Default**: `'Earth (WGS84)'` |

### **Equatorial radius of planet** — Radius of planet at equator `6378137` (default) | scalar

Radius of the planet at its equator, specified as a double scalar, in the same units
as the desired units for the ECEF position.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'6378137'` |

### **Flattening** — Flattening of planet `1/298.257223563` (default) | scalar

Flattening of the planet, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Planet model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1/298.257223563'` |

### **Rotational rate** — Rotational rate `7292115e-11` (default) | scalar

Rotational rate of the planet, specified as a scalar, in rad/s.

#### Dependencies

To enable this parameter, set **Planet model** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `w_E` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'7292115e-11'` |

### **Celestial longitude of Greenwich source** — Source of Greenwich meridian initial celestial longitude `Internal` (default) | `External`

Source of Greenwich meridian initial
celestial longitude, specified as:

|  |  |
| --- | --- |
| `Internal` | Use celestial longitude value from **Celestial longitude of Greenwich**. |
| `External` | Use external input for celestial longitude value. |

#### Dependencies

- To enable this parameter, set
  **Planet model** to
  `Earth`.
- Setting this parameter to
  `External` enables the
  **LG(0)**
  port.
- If **Planet model** is set
  to `Custom`, the
  parameter name changes to **Celestial
  longitude of prime meridian
  source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `angle_in` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Celestial longitude of Greenwich [deg]** — Initial angle `0` (default) | scalar

Initial angle between Greenwich meridian and the *x*-axis of the
inertial frame, specified as a double scalar.

#### Dependencies

- To enable this parameter, set:

  - **Celestial longitude of Greenwich source** to
    `Internal`.
  - **Planet model** to `Earth
    (WGS84)`.
- If **Planet model** is set to
  `Custom`, the parameter name changes to
  **Celestial longitude of prime meridian [deg]**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LPM0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0'` |

### **Celestial longitude of prime meridian source** — Source of prime meridian initial celestial longitude `Internal` (default) | `External`

Source of prime meridian initial celestial longitude, specified as:

|  |  |
| --- | --- |
| `Internal` | Use celestial longitude value from **Celestial longitude of prime meridian**. |
| `External` | Use external input for celestial longitude value. |

#### Dependencies

- To enable this parameter, set **Planet model** to
  `Custom`.
- Setting this parameter to `External`
  enables the
  **LPM(0)**
  port.
- If **Planet model** is set to `Earth
  (WGS84)`, the parameter name changes to **Celestial longitude of
  Greenwich source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `angle_in` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Celestial longitude of prime meridian [deg]** — Initial angle `0` (default) | scalar

Initial angle between prime meridian and the *x*-axis of the
ECI frame, specified as a double scalar.

#### Dependencies

- To enable this parameter, set:

  - **Celestial longitude of prime
    meridian source** to
    `Internal`.
  - **Planet model** to
    `Custom`.
- If **Planet model** is set to
  `Earth (WGS84)`, the
  parameter name changes to **Celestial
  longitude of Greenwich [deg]**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LPM0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0'` |

### State Attributes

Assign a unique name to each state. You can use state names instead of block paths
during linearization.

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

### **Velocity: e.g., {'U','v','w'}** — Velocity state name `''` (default) | comma-separated list surrounded by braces

Velocity state names, specified as comma-separated list surrounded by braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Vm_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Fixed frame position: e.g., {'Xff', 'Yff', 'Zff'}** — ECEF position state name `''` (default) | comma-separated list surrounded by braces

ECEF position state names, specified as a comma-separated list surrounded by
braces.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `posfixedframe_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Inertial position: e.g., {'Xinertial', 'Yinertial', 'Zinertial'}** — Inertial position state names `''` (default) | comma-separated list surrounded by braces

Inertial position state names, specified as a comma-separated list surrounded by
braces.

Default value is `''`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `posinertial_statename` |
| **Type:** character vector |
| **Values:** `''` | comma-separated list surrounded by braces |
| **Default:** `''` |

### **Celestial longitude of Greenwich: e.g., 'LG'** — Celestial longitude state name `''` (default) | character vector

Celestial longitude of Greenwich state name, specified as a character vector.

#### Dependencies

- To enable this parameter, set:**Planet model** to
  `Earth (WGS84)`.
- If **Planet model** is set to
  `Custom`, the parameter name changes to
  **Celestial longitude of prime meridian: e.g.,
  'LPM'**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LPM_statename` |
| **Type:** character vector |
| **Values:** `''` | scalar |
| **Default:** `''` |

### **Celestial longitude of prime meridian: e.g., 'LPM'** — Celestial longitude prime meridian `''` (default) | character vector

Celestial longitude of prime meridian state name, specified as a character vector.

#### Dependencies

- To enable this parameter, set:**Planet
  model** to
  `Custom`.
- If **Planet model** is set to
  `Earth (WGS84)`, the
  parameter name changes to **Celestial
  longitude of Greenwich: e.g.,
  'LG'**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LPM_statename` |
| **Type:** character vector |
| **Values:** `''` | scalar |
| **Default:** `''` |

## Libraries

Aerospace Blockset / Equations of Motion / 6DOF

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006a**

### R2023b: 6DOF ECEF (Quaternion) Block Coordinate Frame Changes

These updates better clarify the coordinate frame of the
6DOF ECEF (Quaternion) block when **Central body** is
`Custom`:

- New block icon.

  6DOF ECEF (Quaternion) block
- Port name subscripts of `ecef` have changed to
  `ff`.
- The **Celestial longitude of Greenwich source**
  programmatic name has changed from `LG0` to
  `LPM`. Existing scripts continue to work.
- Updated block parameter names, but models from previous releases continue
  to work.

  | Old Parameter Name or Setting | New Parameter Name |
  | --- | --- |
  | **ECEF position**... | **Fixed frame position**... |
  | When **Planet model** is `Earth` | **Celestial longitude of Greenwich source** and **Celestial longitude of Greenwich [deg]** |
  | When **Planet model** is `Custom` | **Celestial longitude of prime meridian source** and **Celestial longitude of prime meridian [deg]** |

## Description

Implement quaternion representation of six-degrees-of-freedom equations of motion in Earth-centered Earth-fixed (ECEF) coordinates

The 6DOF ECEF (Quaternion) block Implement quaternion
representation of six-degrees-of-freedom equations of motion in Earth-centered
Earth-fixed (ECEF) coordinates. It considers the rotation of a Earth-centered
Earth-fixed (ECEF) coordinate frame (*XECEF,
YECEF, ZECEF*) about an
Earth-centered inertial (ECI) reference frame (*XECI,
YECI, ZECI*). The origin
of the ECEF coordinate frame is the center of the Earth. For more information on the
ECEF coordinate frame, see Algorithms.
