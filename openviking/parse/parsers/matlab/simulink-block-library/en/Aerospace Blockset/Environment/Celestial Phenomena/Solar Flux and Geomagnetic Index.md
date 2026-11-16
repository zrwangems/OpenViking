---
type: simulink-block
title: 'Solar Flux and Geomagnetic Index'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Celestial Phenomena'
documentation_page: 'solarfluxandgeomagneticindex'
documentation_source_path: 'solarfluxandgeomagneticindex.html'
language: en
---

# Solar Flux and Geomagnetic Index

## Ports

### Input

### **Year** — Year scalar

Year, specified as a scalar. The `aeroReadSpaceWeatherData`
function ignores the value of `year`.

#### Dependencies

To enable this port, set the **Input time specification**
parameter to `Year, day, sec`.

**Data Types:** `double`

### **DOY** — Day of year scalar

Day of year, specified as a scalar.

#### Dependencies

To enable this port, set the **Input time specification**
parameter to `Year, day, sec`.

**Data Types:** `double`

### **UTC (sec)** — Coordinated Universal Time (UCT) scalar

Coordinated Universal Time (UTC), specified as a scalar in seconds. This value is
the number of seconds relative to midnight of **DOY**.

#### Dependencies

To enable this port, set the **Input time specification**
parameter to `Year, day, sec`.

**Data Types:** `double`

### **TJD** — Coordinated Universal Time (UTC) scalar

Coordinated Universal Time (UTC), specified as a scalar Julian date.

#### Dependencies

To enable this port, set the **Input time specification**
parameter to `Julian date`.

**Data Types:** `double`
### Output

### **F107A** — 81-day average of F10.7 flux scalar

81-day average of F10.7 flux, centered on day of year
(`dayOfYear`), specified as a scalar. This value corresponds to
the 10.7 cm radio flux at the actual distance of the Earth from the Sun. The value
does not correspond to the radio flux at 1 AU.

**Data Types:** `double`

### **F107** — Daily F10.7 flux for previous day scalar

Daily F10.7 flux for previous day, specified as a scalar. This value corresponds
to the 10.7 cm radio flux at the actual distance of the Earth from the Sun. The value
does not correspond to the radio flux at 1 AU.

**Data Types:** `double`

### **aph** — Magnetic index information 1-by-7 array

Magnetic index information, specified as an 1-by-7 array. This information
consists of:

- Daily magnetic index (AP)
- 3-hour AP for current time
- 3-hour AP for 3 hours before current time
- 3-hour AP for 6 hours before current time
- 3-hour AP for 9 hours before current time
- Average of eight 3-hour AP indices from 12 to 33 hours before current
  time
- Average of eight 3-hour AP indices from 36 to 57 hours before current
  time

  For more information, see Limitations.

**Data Types:** `double`

## Parameters

### **Space weather data file** — MAT file of space weather data `aeroSpaceWeatherData.mat` (default) | MAT file name

MAT file of space weather data. This file is the output from the `aeroReadSpaceWeatherData` function.

Aerospace Blockset™ includes a default space weather data file,
`aeroSpaceWeatherData.mat`. To use the most recent data available,
use `aeroReadSpaceWeatherData` to generate a new MAT file, and
specify the file name for this parameter. For more information, see `aeroReadSpaceWeatherData`.

If the file is not on the MATLAB® path, specify the full pathname. The MAT file must contain these variables
from the space weather data file:

- `YEAR`
- `MONTH`
- `DAY`
- `AP1`
- `AP2`
- `AP3`
- `AP4`
- `AP5`
- `AP6`
- `AP7`
- `AP8`
- `AP_AVG`
- `F107_OBS`
- `F107_DATA_TYPE`
- `F107_OBS_CENTER81`

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SpaceWeatherDataFile` |
| **Type**: character vector |
| **Values**: `'aeroSpaceWeatherData.mat'` | MAT file name |
| **Default**: `'aeroSpaceWeatherData.mat'` |

### **Input time specification** — Input time format `Year, day, sec` (default) | `Julian date`

Input time format, specified as:

- `Year, day, sec` — Enter the year, day, and seconds
  through the **Year**, **DOY**, and **UT
  (sec)** input ports.
- `Julian date` — Enter the Julian date through the
  **TJD** input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputSpec` |
| **Type**: character vector |
| **Values**: `'Year, day, sec.'` | `'Julian date'` |
| **Default**: `'Year, day, sec.'` |

### **F10.7 extrapolation method** — Extrapolation method for `f107Average` and `f107Daily` `None - clip` (default) | `Constant` | `Least squares fit`

Extrapolation method for `f107Average` and `f107Daily`
for times outside the range of the MAT file data, specified as one of these
values.

| Method | Description |
| --- | --- |
| `None - clip` | Set `f107Average` and `f107Daily` to the nearest data point available in the MAT file. |
| `Constant` | Set `f107Average` and `f107Daily` to a constant value specified by the **Magnetic index extrapolation method** parameter value. |
| `Least squares fit` | Approximate `f107Average` and `f107Daily` using a least-squares fit of the space weather data from October 1, 1957, to December 1, 2040. This method uses a trigonometric function of the form:  `a + b*cos(c*t + d*sin(e*t))`,  where:    - *a* is `128.2351780622538` - *b* is `54.3285872213434` - *c* is `0.0015460708364` - *d* is `0.2429462096495` - *e* is `0.0015563188188` - *t* is *jdCurrent* -   *jdReftime* - *jdCurrent* is the current Julian date - *jdRef* is `2436112.5` |

**Note**

For `f107Average` values, if part of the 81-day period falls
inside the MAT file range of space weather data, the Solar Flux and
Geomagnetic Index block uses the actual daily values from the
overlapping portion. To calculate the average for the nonoverlapping portion, the
block uses the clipped, constant, or least squares daily value.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F107ExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **Default**: `'None - clip'` |

### **F10.7 extrapolation value** — Extrapolation value to assign to `f107Average` and to calculate `f107Daily` `150.0` (default) | scalar

Extrapolation value to assign to `f107Average` and to calculate `f107Daily`, specified as a scalar.

**Tunable:** Yes

#### Dependencies

This value is assigned when:

- **F10.7 extrapolation method** is set to `Constant`.
- Time specified by the **Year**, **DOY**,
  and **UT (sec)** ports is outside the range of the data in
  the MAT file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `F107ExtrapValue` |
| **Type**: character vector |
| **Values**: `'150.0'` | scalar |
| **Default**: `'150.0'` |

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.
- Set **F10.7 extrapolation method** to
  `Constant`.

### **Magnetic index extrapolation method** — Extrapolation method for magnetic index information `None - clip` (default) | `Constant` | `IGRF`

Extrapolation method for magnetic index information values for times outside the range
of the MAT file data, specified as one of these values.

| Method | Description |
| --- | --- |
| `None - clip` | Set elements of magnetic index information to the nearest data point available in the MAT file. |
| `Constant` | Set elements of magnetic index information to a constant value specified by the **Magnetic index extrapolation method** parameter.  The elements of magnetic index for times outside this range are based on clipped values of the horizontal magnetic field strength at these time limits. |
| `IGRF` | Calculate the elements of magnetic index information using the International Geomagnetic Reference Field. Because this model is defined for times between January 1, 1900, 12:00 AM UTC and January 1, 2025, 12:00 AM UTC, the predictions for times outside this range are clipped to values at these time limits. |

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MagneticIndexExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'IGRF'` |
| **Default**: `'None - clip'` |

### **Magnetic index extrapolation value** — Extrapolation value used to calculate magnetic index elements `4.0` (default) | scalar

Extrapolation value used to calculate magnetic index elements, specified as a scalar.

**Tunable:** Yes

#### Dependencies

This parameter is enabled when **Magnetic index extrapolation method** is set to `Constant`.

#### Dependencies

To enable this parameter:

- Set the **Propagation method** parameter to
  `Numerical (high precision)`.
- Set the **Central Body** parameter to
  `Earth`.
- Select the **Include atmospheric drag** check box.
- Set the **Atmospheric density source** parameter to
  `Dialog`.
- Set **Atmospheric model** to
  `NRLMSISE-00`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MagneticIndexExtrapValue` |
| **Type**: character vector |
| **Values**: `'4.0'` | scalar |
| **Default**: `'4.0'` |

## Libraries

Aerospace Blockset / Environment / Celestial Phenomena

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Return solar flux and geomagnetic index

The Solar Flux and Geomagnetic Index block extracts the solar flux and
geomagnetic index from the MAT file that is generated as
`aeroSpaceWeatherData.mat` by the `aeroReadSpaceWeatherData` function.
