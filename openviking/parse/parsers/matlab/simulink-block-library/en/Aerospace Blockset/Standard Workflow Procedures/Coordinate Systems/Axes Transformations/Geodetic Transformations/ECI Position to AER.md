---
type: simulink-block
title: 'ECI Position to AER'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'ecipositiontoaer'
documentation_source_path: 'ecipositiontoaer.html'
language: en
---

# ECI Position to AER

## Ports

### Input

### **Xi** — Position 3-by-1 element vector

Position, specified as a 3-by-1 element vector, in ECI
coordinates.

**Data Types:** `double`

### **ΔUT1** — Difference between UTC and Universal Time scalar

Difference between UTC and Universal Time (UT1) in seconds, specified
as a scalar, for which the block calculates the direction cosine or
transformation matrix.

**Example:** `0.234`

#### Dependencies

To enable this port, select **Higher accuracy parameters**.

**Data Types:** `double`

### **ΔAT** — Difference between International Atomic Time and UTC scalar

Difference between International Atomic Time (TAI) and UTC, specified as a scalar, in
seconds, for which the function calculates the direction cosine or
transformation matrix.

**Example:** `32`

#### Dependencies

This port is disabled if the **Higher accuracy
parameters** check box is cleared.

**Data Types:** `double`

### **[xp,yp]** — Polar displacement of Earth 1-by-2 array

Polar displacement of Earth, specified as a 1-by-2 array, in radians, from the motion of
the Earth crust, along the *x*-axis and
*y*-axis.

**Example:** `[-0.0682e-5 0.1616e-5]`

#### Dependencies

To enable this port, select **Higher accuracy parameters**.

**Data Types:** `double`

### **Port\_5** — Adjustment based on reduction method 1-by-2 array

Adjustment based on reduction method, specified as 1-by-2 array. The
name of the port depends on the setting of the
**Reduction** parameter:

- If the reduction method is
  `IAU-2000/2006`, this input is the
  adjustment to the location of the Celestial Intermediate Pole
  (CIP), specified in radians. This location
  ([d*X*,d*Y*]) is along the
  *x*-axis and *y*-axis, for
  example, `[-0.2530e-6 -0.0188e-6]`.
- If the reduction method is
  `IAU-76/FK5`, this input is the
  adjustment to the longitude ([Δδψ, Δδε]), specified in
  radians.

For historical values, see the International Earth Rotation and Reference Systems
Service website (`https://www.iers.org`) and navigate
to the Earth Orientation Data Data/Products page.

**Example:** `[-0.2530e-6 -0.0188e-6]`

#### Dependencies

To enable this port, select **Higher accuracy
parameters**.

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

### **AER** — Azimuth, elevation, and slant range 3-by-1 element vector

Local reference coordinates azimuth (degrees), elevation (degrees),
and slant range (meters), specified as a 3-by-1 element vector.

**Data Types:** `double`

## Parameters

### **Reduction** — Reduction method `IAU-76/FK5` (default) | `IAU-2000/2006`

Reduction method to convert the coordinates. Method can be one of:

- `IAU-76/FK5`

  Reduce the calculation using the International Astronomical Union
  76/Fifth Fundamental Catalogue (IAU-76/FK5) reference system. Choose
  this reduction method if the reference coordinate system for the
  conversion is FK5.

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
  2000/2006 reference system. Choose this reduction method if the
  reference coordinate system for the conversion is IAU-2000. This
  reduction method uses the P03 precession model to reduce the
  calculation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `red` |
| **Type**: character vector |
| **Values**: `'IAU-2000/2006'` | `'IAU-76/FK5'` |
| **Default**: `'IAU-2000/2006'` |

### **Year** — Year `2014` (default) | double, whole number, greater than 1

Year to calculate the Coordinated Universal Time (UTC) date. Enter a double value that is
a whole number greater than 1, such as `2014`.

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

### **Hour** — Hour `0` (default) | double, whole number, `0` to `24`

Hour to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `24`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `hour` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `24` |
| **Default**: `'0'` |

### **Minutes** — Minutes `0` (default) | double, whole number, `0` to `60`

Minutes to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `min` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Seconds** — Seconds `0` (default)

Seconds to calculate the UTC date. Enter a double value that is a whole
number, from `0` to `60`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sec` |
| **Type**: character vector |
| **Values**: double, whole number, `0` to `60` |
| **Default**: `'0'` |

### **Time increment** — Time increment `None` (default) | `Day` | `Hour` | `Min` | `Sec`

Time increment between the specified date and the desired model simulation
time. The block adjusts the calculated direction cosine matrix to take into
account the time increment from model simulation. For example, selecting
`Day` and connecting a simulation timer to the port
means that each time increment unit is one day and the block adjusts its
calculation based on that simulation time.

This parameter corresponds to the time increment input, the clock
source.

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

Select this check box to allow the following as block inputs. These inputs
let you better control the conversion result. See Input for
a description.

- Δ *UT1*
- Δ *AT*
- [ *xp* , *yp* ]
- [Δδψ, Δδε] or [d *X* ,d *Y* ]

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `extraparamflag` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Units** — Units `Metric (MKS)` (default) | `English`

Specifies the parameter and output units.

| Units | Position | Equatorial Radius | Altitude |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### Dependencies

To enable this option, set **Earth model** to
`WGS84`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `eunits` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Earth model** — Earth model `Custom` (default) | `WGS84`

Earth model to use, `Custom` or
`Earth (WGS84)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `earthmodel` |
| **Type**: character vector |
| **Values**: `'Earth (WGS84)'` | `'Custom'` |
| **Default**: `'Earth (WGS84)'` |

### **Flattening** — Flattening of planet `1/298.257223563` (default) | scalar

Flattening of the planet, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Earth
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `flat` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1/298.257223563` |

### **Equatorial radius** — Radius of planet at equator `6378137` (default) | double scalar

Radius of the planet at its equator.

#### Dependencies

To enable this parameter, set **Earth
model** to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `eqradius` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `6378137` |

### **Initial geodetic latitude and longitude [deg]** — Initial geodetic latitude and longitude `[0 0]` (default) | 2-by-1 vector

Reference location in latitude and longitude, specified as 2-by-1 vector,
in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `latlon0` |
| **Type**: character vector |
| **Values**: 2-by-1 vector |
| **Default**: `[0 0]` |

### **Angular direction of the local reference system (degrees clockwise from north)** — Angular direction `0` (default) | scalar

Specifies angle for converting the flat Earth *x* and
*y* coordinates to north and east coordinates,
respectively. An example is the angle between the vessel and the true
geodetic north.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `psi0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0` |

### **Reference height** — Reference height `0` (default) | scalar

Specifies the reference height measured from the surface of the Earth to
the flat Earth frame. It uses the same units as the ECI position. Estimate
the reference height relative to the Earth frame.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `href` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0` |

## Libraries

Aerospace Blockset / Utilities / Axes Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Convert Earth-centered inertial (ECI) coordinates to azimuth coordinates

The ECI Position to AER block converts Earth-centered inertial (ECI) position
coordinates to azimuth, elevation, and slant-range coordinates (AER), based on the
geodetic position (latitude, longitude, and altitude).

- Azimuth (A) — Angle measured clockwise from true north. It ranges from 0 to
  360 degrees.
- Elevation (E) — Angle between a plane perpendicular to the ellipsoid and the
  line that goes from the local reference to the object position. It ranges from
  –90 to 90 degrees.
- Slant range (R) — Straight line distance between the local reference and the
  object.
