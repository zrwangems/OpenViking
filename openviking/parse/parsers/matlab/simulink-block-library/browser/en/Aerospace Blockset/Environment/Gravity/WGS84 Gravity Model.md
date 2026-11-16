---
type: simulink-block
title: 'WGS84 Gravity Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'wgs84gravitymodel'
documentation_source_path: 'wgs84gravitymodel.html'
language: en
---

# WGS84 Gravity Model

## Ports

### Input

### **μ l h** — Position in geodetic latitude, longitude, and altitude three-element vector | *M*-by-3 array

Position in geodetic latitude, longitude, and altitude, specified as a three-element
vector or *M*-by-3 array, in selected units. Altitude
must be less than 20,000 m (approximately 65,620 feet).

For inputs outside the limits (0 to 20000 m), if the action input is
specified as 'None' or 'warning', the implementation is extended.
However, the usage of the block for inputs outside these limits is not
recommended.

**Data Types:** `double`

### **JD** — Julian date scalar | value greater than 2451545

Julian date, specified as a scalar. The year must be after January 1,
2000 (2451545).

#### Dependencies

To enable this port, select **Input Julian
date**.

**Data Types:** `double`
### Output

### **Output 1** — Gravity three-element vector | *M*-by-3 array

Gravity in the north-east-down (NED) coordinate system.

| Gravity Model Method | Output |
| --- | --- |
| Taylor Series and Close Approximation | Output only normal gravity (down in the NED coordinate system). |
| Exact | Both normal and tangent gravity (down and north in the NED coordinate system). |

**Data Types:** `double`

## Parameters

### **Type of gravity model** — Gravity model method `WGS84 Taylor Series` (default) | `WGS84 Close Approximation` | `WGS84 Exact`

Method to calculate gravity, specified as:

| Gravity Model Method | Output |
| --- | --- |
| `WGS84 Taylor Series` and `WGS84 Close Approximation` | Output only normal gravity (down in the NED coordinate system). |
| `WGS84 Exact` | Both normal and tangent gravity (down and north in the NED coordinate system). |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `model` |
| **Type**: character vector |
| **Values**: `'WGS84 Taylor Series'` | `'WGS84 Close Approximation'` | `'WGS84 Exact'` |
| **Default**: `'WGS84 Taylor Series'` |

### **Units** — Units `Metric (MKS)` (default) | `English`

Input and output units, specified as:

| Units | Height | Gravity |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters per second squared |
| `English` | Feet | Feet per second squared |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Exclude Earth's atmosphere** — Earth atmosphere `on` (default) | `off`

- To exclude the mass of the atmosphere for the Earth gravitational
  field, select this check box.
- To include the mass of the atmosphere for the Earth gravitation
  field, clear this check box.

#### Dependencies

To enable this check box, set **Type of gravity
model** to `Type of gravity model
WGS84 Close Approximation` or `WGS84 Exact`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `no_atmos` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Precessing reference frame** — Precessing reference frame `on` (default) | `off`

- To calculate the velocity of the Earth using the International
  Astronomical Union (IAU) value of the Earth's angular velocity and
  the precession rate in right ascension, select this check
  box.
- To calculate the velocity of the Earth using the angular velocity
  of the standard Earth rotating at a constant angular velocity, clear
  this check box.

To obtain the precession rate in right ascension, the block calculates
Julian centuries from Epoch J2000.0 using **Month**,
**Day**, and **Year**.

#### Dependencies

- To enable this check box, set **Type of gravity
  model** to `Type of
  gravity model WGS84 Close Approximation` or
  `WGS84 Exact`.
- Clearing this check box disables the **Input Julian
  date** parameter and the **JD**
  input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `precessing` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Input Julian date** — Julian date `off` (default) | `on`

- To specify the Julian date for the block with an input port,
  select this check box.
- To calculate the Julian date using the values of
  **Month**, **Day**, and
  **Year**, clear this check box. The year must
  be after January 1, 2000 (2451545).

#### Dependencies

- To enable the **JD** port, select this check
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `jd_loc` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Month** — Month `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

Month to calculate Julian centuries from Epoch J2000.0.

#### Dependencies

To enable this parameter:

- Set **Type of gravity model** to
  `WGS84 Close Approximation` or
  `WGS84 Exact`.
- Select **Precessing reference frame**.

To disable this parameter, select **Input Julian
date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `month` |
| **Type**: character vector |
| **Values:** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **Default**: `'January'` |

### **Day** — Day 10 (default) | `1` to `31`

Day to calculate Julian centuries from Epoch J2000.0.

#### Dependencies

To enable this parameter:

- Set **Type of gravity model** to
  `WGS84 Close Approximation` or
  `WGS84 Exact`.
- Select **Precessing reference frame**.

To disable this parameter, select **Input Julian
date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `day` |
| **Type:** character vector |
| **Values:** `'1'` to `'31'` |
| **Default:** `'10'` |

### **Year** — Year 2004 (default) | any year

Year to calculate Julian centuries from Epoch J2000.0. The year must be 2000 or
greater.

#### Dependencies

To enable this parameter:

- Set **Type of gravity model** to
  `WGS84 Close Approximation` or
  `WGS84 Exact`.
- Select **Precessing reference frame**.
- To disable this parameter, select **Input Julian
  date**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `year` |
| **Type:** character vector |
| **Values:** any year |
| **Default:** `'2004'` |

### **No centrifugal effects** — Centrifugal effects `on` (default) | `off`

- To base calculated gravity on pure attraction resulting from the
  normal gravitational potential, select this check box.
- To enable the calculated gravity to include the centrifugal force
  resulting from the Earth's angular velocity, clear this check
  box.

This option is available only with **Type of gravity
model WGS84 Close Approximation** or **WGS84 Exact**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `no_centrifugal` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Action for out-of-range input** — Out-of-range block behavior `Warning` (default) | `Error` | `None`

Out-of-range block behavior, specified as follows.

| Value | Description |
| --- | --- |
| `None` | No action. The block imposes upper and lower limits on an input signal. For inputs outside the limits, the implementation is extended. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. For Accelerator and Rapid Accelerator modes, setting the action to `Warning` has no effect and the model behaves as though the action is set to `None`. |
| `Error` | MATLAB® returns an exception, model simulation stops. For Accelerator and Rapid Accelerator modes, setting the action to `Error` has no effect and the model behaves as though the action is set to `None`. |

The WGS84 Gravity Model is not recommended for inputs outside the
limits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement 1984 World Geodetic System (WGS84) representation of Earth's gravity

The WGS84 Gravity Model block implements the mathematical
representation of the geocentric equipotential ellipsoid of the World Geodetic System
(WGS84). The block output is the Earth gravity at a specific location. To control
gravity precision, use the **Type of gravity model**
parameter.

The block icon displays the input and output units selected from the **Units** list.
