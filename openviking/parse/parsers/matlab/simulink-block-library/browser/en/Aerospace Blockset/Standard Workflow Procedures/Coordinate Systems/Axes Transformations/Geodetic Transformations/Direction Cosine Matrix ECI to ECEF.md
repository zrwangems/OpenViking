---
type: simulink-block
title: 'Direction Cosine Matrix ECI to ECEF'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixecitoecef'
documentation_source_path: 'directioncosinematrixecitoecef.html'
language: en
---

# Direction Cosine Matrix ECI to ECEF

## Ports

### Input

### **ΔUT1** — Difference between UTC and Universal Time scalar

Difference between UTC and Universal Time (UT1) in seconds, specified
as a scalar, for which the function calculates the direction cosine or
transformation matrix.

**Example:**
`0.234`

#### Dependencies

To enable this port, select the **Higher accuracy parameters** check
box.

**Data Types:** `double`

### **ΔAT** — Difference between International Atomic Time and UTC scalar

Difference between International Atomic Time (TAI) and UTC, specified as a scalar, in
seconds, for which the function calculates the direction cosine or
transformation matrix.

**Example:**
`32`

#### Dependencies

To enable this port, select the **Higher accuracy parameters** check
box.

**Data Types:** `double`

### **[xp,yp]** — Polar displacement of Earth 1-by-2 array

Polar displacement of Earth, specified as a 1-by-2 array, in radians, from the motion of
the Earth crust, along the *x*-axis and
*y*-axis.

**Example:**
`[-0.0682e-5 0.1616e-5]`

#### Dependencies

To enable this port, select the **Higher accuracy parameters** check
box.

**Data Types:** `double`

### **Port\_5** — Adjustment based on reduction method 1-by-2 array

Adjustment based on reduction method, specified as 1-by-2 array. The
name of the port depends on the setting of the
**Reduction** parameter:

- If the reduction method is
  `IAU-2000/2006`, this input is the
  adjustment to the location of the Celestial Intermediate Pole
  (CIP), specified in radians. This location
  ([d*X*, d*Y*]) is along
  the *x*-axis and
  *y*-axis.
- If the reduction method is
  `IAU-76/FK5`, this input is the
  adjustment to the longitude ([Δδψ, Δδε]), specified in
  radians.

For historical values, see the International Earth Rotation and Reference Systems
Service website (`https://www.iers.org`).

**Example:**
`[-0.2530e-6 -0.0188e-6]`

#### Dependencies

To enable this port, select the **Higher accuracy
parameters** check box.

**Data Types:** `double`

### **Port\_6** — Time increment source scalar

Time increment source, specified as a scalar, such as the Clock block.

#### Dependencies

- The port name and time increment depend on the
  **Time Increment** parameter.

  | **Time Increment** Value | Port Name |
  | --- | --- |
  | `Day` | **day** |
  | `Hour` | **hour** |
  | `Min` | **min** |
  | `Sec` | **sec** |
  | `None` | No port |
- To disable this port, set the **Time
  Increment** parameter to
  `None`.

**Data Types:** `double`
### Output

### **DCMfi** — Direction cosine matrix 3-by-3 matrix

Direction cosine matrix ECI to ECEF.

**Data Types:** `double`

## Parameters

### **Reduction** — Reduction method `IAU-76/FK5` (default) | `IAU-2000/2006`

Reduction method to calculate the direction cosine matrix. The method can be one of the
following:

- `IAU-76/FK5`

  Reduce the calculation using the IAU-76/Fifth Fundamental Catalogue (FK5) reference
  system. Choose this reduction method if the reference coordinate
  system for the conversion is FK5.

  **Note**

  This method uses the IAU 1976 precession model and the IAU
  1980 theory of nutation to reduce the calculation. This model
  and theory are no longer current, but the software provides this
  reduction method for existing implementations. Because of the
  polar motion approximation that this reduction method uses, the
  block calculates the transformation matrix rather than the
  direction cosine matrix.
- `IAU-2000/2006`

  Reduce the calculation using the International Astronomical Union
  (IAU)-2000/2006 reference system. Choose this reduction method if
  the reference coordinate system for the conversion is IAU-2000. This
  reduction method uses the P03 precession model to reduce the
  calculation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `red` |
| **Type**: character vector |
| **Values**: `'IAU-2000/2006'` | `'IAU-76/FK5'` |
| **Default**: `'IAU-2000/2006'` |

### **Year** — Year `2013` (default) | double, whole number, greater than 1

Year to calculate the Coordinated Universal Time (UTC) date. Enter a double value that is
a whole number greater than 1, such as `2013`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `year` |
| **Type**: character vector |
| **Values**: double, whole number, greater than 1 |
| **Default**: `'2013'` |

### **Month** — Month `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

Month to calculate the UTC date.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `month` |
| **Type**: character vector |
| **Values**: `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **Default**: `'January'` |

### **Day** — Day `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

Day to calculate the UTC date.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `day` |
| **Type**: character vector |
| **Values**: `'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **Default**: `'1'` |

### **Hour** — Hour `0` (default) | double, whole number, in the range of `0` and `24`

Hour to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `24`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `hour` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `24` |
| **Default**: `'0'` |

### **Minutes** — Minutes `0` (default) | double, whole number, in the range of `0` and `60`

Minutes to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `min` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Seconds** — Seconds `0` (default) | double, whole number, in the range of `0` and `60`

Seconds to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sec` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Time increment** — Time increment `Day` (default) | `Hour` | `Min` | `Sec` | `None`

Time increment between the specified date and the desired model simulation
time. The block adjusts the calculated direction cosine matrix to take into
account the time increment from model simulation. For example, selecting
`Day` and connecting a simulation timer to the port
means that each time increment unit is one day and the block adjusts its
calculation based on that simulation time.

This parameter corresponds to the time increment input, the clock source.

If you select `None`, the calculated Julian date does not
take into account the model simulation time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `deltaT` |
| **Type**: character vector |
| **Values**: `'None'` | `'Day'` | `'Hour'` | `'Min'` | `'Sec'` |
| **Default**: `'Day'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as follows.

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `errorflag` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Error'` |

### **Higher accuracy parameters** — Enable higher accuracy parameters `on` (default) | `off`

Select this check box to enable these inputs. These inputs let you better
control the conversion result. See Input for a
description.

- Δ *UT1*
- Δ *AT*
- [ *xp* , *yp* ]
- [Δδψ, Δδε] or [d *X*, d *Y*
  ]

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `extraparamflag` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Convert Earth-centered inertial (ECI) to Earth-centered Earth-fixed (ECEF) coordinates

The Direction Cosine Matrix ECI to ECEF block calculates the position
direction cosine matrix ( Earth-centered inertial to Earth-centered Earth-fixed ), based
on the specified reduction method and Coordinated Universal Time (UTC), for the
specified time and geophysical data.
