---
type: simulink-block
title: 'Attitude Profile (Nadir Pointing)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'attitudeprofilenadirpointing'
documentation_source_path: 'attitudeprofilenadirpointing.html'
language: en
---

# Attitude Profile (Nadir Pointing)

## Ports

### Input

### **X** — Velocity state vector position 3-element vector

Position state vector of spacecraft at time tutc.

**Data Types:** `double`

### **V** — Velocity state vector 3-element vector

Velocity state vector of spacecraft at time tutc, specified
as a 3-element vector.

#### Dependencies

To enable this port, set **Constraint coordinate frame (CCF)**
to `LVLH`.

**Data Types:** `double`

### **q** — Spacecraft attitude 4-element vector

Attitude of the spacecraft at *tutc*,
represented as a quaternion from body frame to port coordinate frame, specified as a
4-element vector.

**Data Types:** `double`

### **tutc** — Current data or time scalar

Current date or time, specified as a scalar, as a Julian date.

#### Dependencies

To enable this port, perform one of these:

- Set **Pointing mode** to `Point at celestial
  body` or `Point at LatLonAlt`
- Select the **Allow pointing mode change during run** check
  box.

**Data Types:** `double`

### **μ l** — Geodetic latitude and longitude 2-element vector

Geodetic latitude and longitude (deg) of a terrestrial point of interest,
specified as a 1-D array of size 2. This port is used together with altitude when
**Pointing mode** is `Point at
LatLongAlt`. This location is used as the primary constraint.

#### Dependencies

To enable this port, do one of these:

- Set **Pointing mode** to
  `LatLonAlt`.
- Select the **Allow pointing mode change during run** check
  box.

**Data Types:** `double`

### **h** — Altitude scalar

Altitude of terrestrial point of interest, specified as a scalar. This port is
used together with geodetic latitude and longitude when **Pointing
mode** is `Point at LatLongAlt`. This location is
used as the primary constraint.

#### Dependencies

To enable this port, do one of these:

- Set **Pointing mode** to
  `LatLonAlt`.
- Select the **Allow pointing mode change during run** check
  box.

**Data Types:** `double`

### **A1b** — Primary alignment vector 3-element vector

Primary alignment vector (in body frame), specified as a 3-element vector.

#### Dependencies

To enable this port, set **Primary alignment (body-frame)** to
`Port`.

**Data Types:** `double`

### **A2b** — Secondary alignment vector 3-element vector

Secondary alignment vector (in body frame), specified as a 3-element
vector.

#### Dependencies

To enable this port, set **Secondary alignment (Body-frame)**
to `Port`.

**Data Types:** `double`

### **C1lvlh** — Primary constraint vector 3-element vector

Primary constraint vector, specified as a 3-element vector, in constraint
coordinate frame.

#### Dependencies

To enable this port, set:

- **Pointing mode** to
  `Custom`.
- **Primary constraint (CCF)** to
  `Port`.

**Data Types:** `double`

### **C2lvlh** — Secondary constraint 3-element vector

Secondary constraint vector, specified as a 3-element vector.

#### Dependencies

To enable this port, set **Secondary constraint (CCF)** to
`Port`.

**Data Types:** `double`
### Output

### **qtgtb** — Quaternion rotation 4-element vector (scalar first)

Quaternion rotation by which to rotate from the spacecraft current orientation to
the desired orientation (in body frame), returned as a 4-element vector.

#### Dependency

To enable this port, select the **Output rotation from current to
updated attitude** check box.

**Data Types:** `double`

### **qnew** — Updated spacecraft attitude 4-element vector

Updated spacecraft attitude with respect to **Port Coordinate
Frame** following the quaternion rotation, returned as a 4-element
vector.

#### Dependency

To enable this port, select the **Output attitude** check
box.

**Data Types:** `double`

## Parameters

### **Output rotation from current to updated attitude** — Output rotation on (default) | off

To output the rotation, select this check box. Otherwise, clear this check
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `outputError` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output attitude** — Output updated attitude off (default) | on

To output the updated spacecraft attitude as a quaternion rotation from the body
frame to the **Port coordinate frame**, select this check box.
Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `outputFinalAttitude` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Port coordinate frame** — Coordinate frame for position, velocity, and attitude ports `ICRF` (default) | `Fixed-frame`

Coordinate frame for position, velocity, and attitude (**q**)
ports. For more information about coordinate systems, see Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `portFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **Pointing mode** — Primary vector alignment pointing mode `Point at nadir` (default) | `Point at celestial body` | `Point at LatLonAlt` | `Custom`

Primary vector alignment pointing mode, specified as `Point at
nadir`, `Point at celestial body`,
`Point at LatLonAlt`, or `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `pointingMode` |
| **Type:** character vector |
| **Values:** `'Point at nadir'` | `'Point at celestial body'` | `'Point at LatLonAlt'` | `'Custom'` |
| **Default:** `'Point at nadir'` |

### **Allow pointing mode change during run** — Allow pointing mode change during run off (default) | on

To allow pointing mode change during run, select this check box. Otherwise, clear
this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tunablePointing` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Celestial target** — Celestial body `Sun` (default) | `Mercury` | `Venus` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Pluto` | `Solar system barycenter` | `Earth-Moon barycenter`

Celestial body with which to align primary alignment vector.

#### Dependencies

To enable this parameter, set **Pointing mode** to
`Point at celestial body`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `celestialTarget` |
| **Type:** character vector |
| **Values:** `'Sun'` | `'Mercury'` | `'Venus'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Pluto'` | `'Solar'` | `'Solar system barycenter'` | `'Earth-Moon barycenter'` |
| **Default:** `'Sun'` |

### **Primary alignment (body-frame)** — Primary alignment vector `Dialog` (default) | `Port`

Primary alignment vector source, specified as `Port` or
`Dialog`.

- `Port` — Specify port alignment array through the
  **A1b** port.
- `Dialog` — Specify port alignment 3-element vector in
  the accompanying text box (default value of `[0 0 1]`).

#### Dependencies

To specify the port alignment array in a text box, set this parameter to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `primaryAlignmentSrc` | when `primaryAlignmentSrc` is `'Dialog'`, use `primaryAlignment` to set the primary alignment vector |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` | primary alignment vector, specified 3-element vector |
| **Default:** `'Dialog'` |

### **Secondary alignment (body-frame)** — Secondary alignment vector `Dialog` (default) | `Port`

Secondary alignment vector source, specified as `Port` or
`Dialog`.

- `Port` — Specify port alignment array through the
  **A2b** port.
- `Dialog` — Specify port alignment 3-element vector in
  the accompanying text box (default value of `[1 0 0]`).

#### Dependencies

To specify the port alignment array in a text box, set this parameter to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `secondaryAlignmentSrc` | when `secondaryAlignmentSrc` is `'Dialog'`, use `secondaryAlignment` to set the secondary alignment vector |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` | secondary alignment vector, specified as a 3-element vector |
| **Default:** `'Dialog'` |

### **Constraint coordinate frame, CCF** — Constraint coordinate frame `ICRF` (default) | `Fixed-frame` | `LVLH` | `NED` | `Body-fixed`

Coordinate frame in which constraint vectors are provided, specified as
`ICRF`, `Fixed-frame`,
`LVLH`, `NED`, or
`Body-fixed`. For more information about coordinate systems,
see Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `constraintFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` | `'LVLH'` | `'NED'` | `'Body-fixed'` |
| **Default:** `'ICRF'` |

### **Primary constraint (CCF)** — Primary constraint `Dialog` (default) | `Port`

Primary constraint vector source, specified as `Port` or
`Dialog`.

- `Port` — Specify primary constraint array through the
  **C1b** port.
- `Dialog` — Specify port constraint 3-element vector in
  the accompanying text box (default value of `[1 0 0]`).

#### Dependencies

- To specify the port alignment array in a text box, set this parameter to
  `Dialog`.
- This parameter is affected when **Constraint coordinate frame
  (CCF)** is set to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `primaryConstraintSrc` | when `primaryConstraintSrc` is `'Dialog'`, use `primaryConstraint` to set the primary constraint vector |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` | primary constraint vector, specified as a 3-element vector |
| **Default:** `'Dialog'` |

### **Secondary constraint (CCF)** — Secondary constraint `Dialog` (default) | `Port`

Secondary constraint vector source, specified as `Port` or
`Dialog`.

- `Port` — Specify secondary constraint array through the
  **C1b** port.
- `Dialog` — Specify port constraint 3-element vector in
  the accompanying text box (default value of `[0 1 0]`).

After the primary alignment vector is aligned with the primary constraint vector, to
fully define the rotation, the block attempts to align the secondary alignment vector
with the rotation vector. The rotation vector should be the secondary constraint
vector.

Whereas the primary constraint is enabled only for the custom pointing mode, the
secondary constraint is always enabled.

#### Dependencies

To specify the port alignment array in a text box, set this parameter to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `secondaryConstraintSrc` | when `secondaryConstraintSrc` is `'Dialog'`, use `secondaryConstraint` to set the secondary constraint vector |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` | secondary constraint vector, specified as a 3-element vector |
| **Default:** `'Dialog'` |

## Libraries

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2023a: Attitude Profile Block Update

To support idealized attitude control workflows, the Attitude Profile
blocks have new parameters and an output port:

- **Output rotation from current to updated attitude**
  parameter
- **Output attitude** parameter
- **qnew** port

## Description

Calculate shortest quaternion rotation

The Attitude Profile blocks calculate the shortest quaternion rotation
that aligns the primary alignment vector with the primary constraint vector. A quaternion is
defined using the scalar-first convention. Aerospace Blockset™ uses quaternions that are defined using the scalar-first convention.

Provide the primary constraint as either a pointing mode:

- `Point at nadir`
- `Point at celestial body`
- `Point at LatLonAlt`

or via a custom constraint vector. The block then aligns secondary alignment
and constraint vectors as much as possible without breaking primary alignment.

The library contains three versions of the Attitude Profile block
preconfigured for these common attitude control modes:

- Attitude Profile (Nadir Pointing) — `Point at
  nadir`
- Attitude Profile (Geographic Pointing) — `Point at
  LatLonAlt`
- Attitude Profile (Sun Tracking) — `Point at celestial
  body` with Sun as the celestial target

For more information on the coordinate systems the Attitude Profile blocks
use, see Algorithms.
