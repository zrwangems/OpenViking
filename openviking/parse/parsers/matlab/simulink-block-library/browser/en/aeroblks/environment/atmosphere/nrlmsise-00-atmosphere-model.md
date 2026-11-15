---
type: simulink-block
title: 'NRLMSISE-00 Atmosphere Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'nrlmsise00atmospheremodel'
documentation_source_path: 'nrlmsise00atmospheremodel.html'
language: en
---

# NRLMSISE-00 Atmosphere Model

## Ports

### Input

### **Port\_1** — Geodetic latitudes, longitude, and altitude three-element matrix

Geodetic latitudes, in degrees, longitude, in degrees, and altitude,
in selected length units, specified as three-element matrix.

**Data Types:** `double`

### **Port\_2** — Years array

*N* years, specified as an array.

**Data Types:** `double`

### **Port\_3** — Days array

*N* days of a year (1 to 365 (or 366)), specified as
an array.

**Data Types:** `double`

### **Port\_4** — Seconds array

*N* seconds in a day, specified as an array, in
universal time (UT).

**Data Types:** `double`

### **Port\_5** — Local apparent solar time array

*N* local apparent solar timed, specified as an
array, in hours.

**Data Types:** `double`

### **Port\_6** — 81-day average F10.7 flux `150` (default) | array

*N* 81-day averages of F10.7 flux, centered on day of
year (doy), specified as an array.

**Data Types:** `double`

### **Port\_7** — Daily average F10.7 flux `150` (default) | array

*N* daily F10.7 fluxes for previous days, specified
as an array.

**Data Types:** `double`

### **Port\_8** — Magnetic index information *N*-by-7 array

Magnetic index information, specified as an *N*-by-7.
If you specify *magneticIndex*, you must also specify
*f107Average* and *f107Daily*. The
magnetic index information consists of:

|  |
| --- |
| Daily magnetic index (AP) |
| 3 hour AP for current time |
| 3 hour AP for 3 hours before current time |
| 3 hour AP for 6 hours before current time |
| 3 hour AP for 9 hours before current time |
| Average of eight 3 hour AP indices from 12 to 33 hours before current time |
| Average of eight 3 hour AP indices from 36 to 57 hours before current time |

The effects of daily magnetic index are not large or established below 80,000 m. As a
result, the block sets the default value to `4`. It
sets all other indices to `0` by default. See the
limitations in Limitations
for more information.

**Data Types:** `double`

### **Port\_9** — Flags array of 23

Flags, specified as an array of 21, to enable or disable particular variations for the
outputs.

| Field | Description |
| --- | --- |
| `Flags(1)` | F10.7 effect on mean |
| `Flags(2)` | Independent of time |
| `Flags(3)` | Symmetrical annual |
| `Flags(4)` | Symmetrical semiannual |
| `Flags(5)` | Asymmetrical annual |
| `Flags(6)` | Asymmetrical semiannual |
| `Flags(7)` | Diurnal |
| `Flags(8)` | Semidiurnal |
| `Flags(9)` | Daily AP. If you set this field to -1, the block uses the entire matrix of magnetic index information (APH) instead of `APH(:,1)` |
| `Flags(10)` | All UT, longitudinal effects |
| `Flags(11)` | Longitudinal |
| `Flags(12)` | UT and mixed UT, longitudinal |
| `Flags(13)` | Mixed AP, UT, longitudinal |
| `Flags(14)` | Terdiurnal |
| `Flags(15)` | Departures from diffusive equilibrium |
| `Flags(16)` | All exospheric temperature variations |
| `Flags(17)` | All variations from 120,000 meter temperature (TLB) |
| `Flags(18)` | All lower thermosphere (TN1) temperature variations |
| `Flags(19)` | All 120,000 meter gradient (S) variations |
| `Flags(20)` | All upper stratosphere (TN2) temperature variations |
| `Flags(21)` | All variations from 120,000 meter values (ZLB) |
| `Flags(22)` | All lower mesosphere temperature (TN3) variations |
| `Flags(23)` | Turbopause scale height variations |

**Data Types:** `double`
### Output

### **Port\_1** — Temperature *N*-by-2 array

Temperature values, returned in a *N*-by-2 array of
values, in selected temperature units. The first column contains
exospheric temperatures, the second column contains temperature at
altitude.

**Data Types:** `double`

### **Port\_2** — Densities *N*-by-9 array

Density values, returned in a *N*-by-9 array, in
selected density units.

| Density | Description |
| --- | --- |
| `Density(1)` | Density of He |
| `Density(2)` | Density of O |
| `Density(3)` | Density of N2 |
| `Density(4)` | Density of O2 |
| `Density(5)` | Density of Ar |
| `Density(6)` | Total mass density  `Density(6)`, total mass density, is defined as the sum of the mass densities of He, O, N2, O2, Ar, H, and N. Optionally, `Density(6)` can include the mass density of anomalous oxygen making `Density(6)`, the effective total mass density for drag. |
| `Density(7)` | Density of H |
| `Density(8)` | Density of N |
| `Density(9)` | Anomalous oxygen number density |

**Data Types:** `double`

## Parameters

### **Units** — Input and output units `Metric (MKS)` (default) | `English`

Input and output units, specified as:

| Units | Temperature | Height | Density |
| --- | --- | --- | --- |
| `Metric (MKS)` | Kelvin | Meters | kg/m3, some density outputs 1/m3 |
| `English` | Rankine | Feet | lbm/ft3, some density outputs 1/ft3 |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Input local apparent solar time** — Apparent solar time `off` (default) | `on`

Select this check box to input the local apparent solar time, in hours.
Otherwise, the block inputs the default value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `1st input` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Input flux and magnetic index information** — Daily F10.7 flux for previous day and magnetic index information `off` (default) | `on`

Select this check box to input the 81-day average of F10.7, the daily F10.7 flux for the
previous day, and the array of 7 magnetic index information (see the
`aph` argument in the `atmosnrlmsise00` function).
Otherwise, the block inputs the default value of `150` for
F10.7 and F10.7a, and `[4, 0, 0, 0, 0, 0, 0]` for
geomagnetic index.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `flux_ap_input` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Source for flags** — Variation flag source `Internal` (default) | `External`

Variation flag source, specified as `Internal` or
`External`. If you specify
`External`, specify the variation flag as an array of
23. If you specify `Internal`, the flag source is internal
to the block.

#### Dependencies

Setting **Source for flags** to
`Internal` enables the
**Flags** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `flags_input` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Flags** — Variation flags `ones(1,23)` (default)

Variation flag, specified as an array of 23
(`ones(1,23)`). This parameter applies only when
**Source for flags** has a value of
`Internal`. You can specify one of the following values
for a field. The default value for each field is `1`.

- 0.0

  Removes that value's effect on the output.
- 1.0

  Applies the main and the cross-term effects of that value on
  the output.
- 2.0

  Applies only the cross-term effect of that value on the
  output.

The array has the following fields.

| Field | Description |
| --- | --- |
| `Flags(1)` | F10.7 effect on mean |
| `Flags(2)` | Independent of time |
| `Flags(3)` | Symmetrical annual |
| `Flags(4)` | Symmetrical semiannual |
| `Flags(5)` | Asymmetrical annual |
| `Flags(6)` | Asymmetrical semiannual |
| `Flags(7)` | Diurnal |
| `Flags(8)` | Semidiurnal |
| `Flags(9)` | Daily AP. If you set this field to -1, the block uses the entire matrix of magnetic index information (APH) instead of `APH(:,1)` |
| `Flags(10)` | All UT, longitudinal effects |
| `Flags(11)` | Longitudinal |
| `Flags(12)` | UT and mixed UT, longitudinal |
| `Flags(13)` | Mixed AP, UT, longitudinal |
| `Flags(14)` | Terdiurnal |
| `Flags(15)` | Departures from diffusive equilibrium |
| `Flags(16)` | All exospheric temperature variations |
| `Flags(17)` | All variations from 120,000 meter temperature (TLB) |
| `Flags(18)` | All lower thermosphere (TN1) temperature variations |
| `Flags(19)` | All 120,000 meter gradient (S) variations |
| `Flags(20)` | All upper stratosphere (TN2) temperature variations |
| `Flags(21)` | All variations from 120,000 meter values (ZLB) |
| `Flags(22)` | All lower mesosphere temperature (TN3) variations |
| `Flags(23)` | Turbopause scale height variations |

#### Dependencies

Setting **Source for flags** to
`Internal` enables the
**Flags** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `flags` |
| **Type**: character vector |
| **Values**: `'ones(1,23)'` |
| **Default**: `'ones(1,23)'` |

### **Include anomalous oxygen number density in total mass density** — Anomalous oxygen `off` (default) | `on`

Select this check box to take into account the anomalous oxygen when
calculating the neutral atmosphere empirical model from the surface to lower
exosphere (0 to 1,000,000 meters). Taking into account this number can
affect the satellite drag above 500,000 meters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `oxygen_in` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as:

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

## Libraries

Aerospace Blockset / Environment / Atmosphere

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

## Description

Implement mathematical representation of 2001 United States Naval Research Laboratory Mass Spectrometer and Incoherent Scatter Radar Exosphere

The
NRLMSISE-00 Atmosphere Model block implements the mathematical representation
of the 2001 United States Naval Research Laboratory Mass Spectrometer
and Incoherent Scatter Radar Exosphere (NRLMSISE-00) of the MSIS® class model. This block calculates the neutral atmosphere empirical model from the surface to lower exosphere (0 to 1,000,000 meters). When configuring the block for this calculation, you can also take into account the anomalous oxygen, which can affect the satellite drag above 500,000 meters.
