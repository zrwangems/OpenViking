---
type: simulink-block
title: 'Lapse Rate Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'lapseratemodel'
documentation_source_path: 'lapseratemodel.html'
language: en
---

# Lapse Rate Model

## Ports

### Input

### **h (m)** — Geopotential height scalar | array

Geopotential height, specified as a scalar or array.

**Data Types:** `double`
### Output

### **T (K)** — Temperature scalar | array

Temperature, returned as a scalar or array, in K.

**Data Types:** `double`

### **a (m/s)** — Speed of sound scalar | array

Speed of sound, returned as a scalar or array, in m/s.

**Data Types:** `double`

### **P (Pa)** — Air pressure scalar | array

Air pressure, returned as a scalar or array, in Pa.

**Data Types:** `double`

### **ρ (kg/m3)** — Air density scalar | array

Air density, returned as scalar or array, in
kg/m3.

**Data Types:** `double`

### **ν (m2/s)** — Kinematic viscosity scalar | *m*-by-*n* array

Kinematic viscosity, returned as a scalar or
*m*-by-*n* array, in
m2/s.

#### Dependencies

Selecting the **Output kinematic and dynamic
viscosity** check box adds the **ν
(m2/s)** output
port.

**Data Types:** `double`

### **μ (N s/m2)** — Dynamic viscosity scalar | *m*-by-*n* array

Dynamic viscosity, returned as a scalar or
*m*-by-*n* array, in N
s/m2.

#### Dependencies

Selecting the **Output kinematic and dynamic
viscosity** check box adds the **μ (N
s/m2)** output
port.

**Data Types:** `double`

## Parameters

### **S** — Sutherland temperature 110.4 K (default) | scalar

Sutherland temperature in Kelvin, specified as a scalar.

#### Dependencies

This optional input is available when the **Output kinematic
and dynamic viscosity** and **Change atmospheric
parameters** are e.

### **Tref** — Reference temperature 273.15 K (default) | scalar

Reference temperature in Kelvin, specified as a scalar.

#### Dependencies

This optional input is available when the **Output kinematic
and dynamic viscosity** is selected.

#### Dependencies

This optional input is available when the **Output kinematic
and dynamic viscosity** and **Change atmospheric
parameters** are e.

### **μref** — Reference dynamic viscosity 1.716e-5 kg/ms (default) | scalar

Reference dynamic viscosity in kilograms per meter second, specified as a
scalar.

#### Dependencies

This optional input is available when the **Output kinematic
and dynamic viscosity** and **Change atmospheric
parameters** are e.

### **Output kinematic and dynamic viscosity** — Option to output kinematic and dynamic viscosity `off` (default) | `on`

Option to output kinematic and dynamic viscosity.

#### Dependencies

Selecting this check box:

- Adds the **ν
  (m2/s)** output
  port.
- Adds the **μ (N
  s/m2)** output
  port.

#### Dependencies

If selected simultaneously with the **Change atmospheric
parameters** checkbox, adds the **Viscosity
parameters** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `viscosityOut` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Change atmospheric parameters** — Customize parameters `off` (default) | `on`

Customize various atmospheric parameters to be different from the lapse
rate values. Selecting this check box converts the block from Lapse
Rate Model to ISA Atmosphere Model.

#### Dependencies

Selecting this check box enables the **Atmospheric
parameters** tab with these parameters:

- **Acceleration due to gravity
  (m/s^2)**
- **Ratio of specific heats**
- **Characteristic gas constant
  (J/Kg/K)**
- **Lapse rate (K/m)**
- **Height of troposphere (m)**
- **Height of tropopause (m)**
- **Air density at mean sea level
  (Kg/m^3)**
- **Ambient pressure at mean sea level
  (N/m^2)**
- **Lowest altitude (m)**

Selecting in conjunction with **Output kinematic and dynamic
viscosity** enables the **Viscosity
parameters** tab with these parameters:

- **S**
- **Tref**
- **μref**

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `custom` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Acceleration due to gravity (m/s^2)** — Acceleration `9.80665` (default) | scalar

Acceleration from gravity (*g*). in m/s2,
specified as double scalar.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `g` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `9.80665` |

### **Ratio of specific heats** — Ratio of heats `1.4` (default) | scalar

Ratio of specific heats *γ*, specified as a double value.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gamma` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1.4` |

### **Characteristic gas constant (J/Kg/K)** — Gas constant `287.0531` (default) | scalar

Characteristic gas constant (R), specified as double scalar, in J/Kg/K.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `R` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `287.0531` |

### **Lapse rate (K/m)** — Lapse rate `0.0065` (default) | scalar

Lapse rate of the troposphere, specified as double scalar, in K/m.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `L` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0.0065` |

### **Height of troposphere (m)** — Troposphere height `11000` (default) | scalar

Height of the troposphere (range of decreasing temperatures), specified as double scalar,
in m.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `h_trop` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `11000` |

### **Height of tropopause (m)** — Tropopause height `20000` (default) | scalar

Height of the tropopause (range of constant temperature), specified as double scalar, in
m.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `h_strat` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `20000` |

### **Air density at mean sea level (Kg/m^3)** — Air density `1.225` (default) | scalar

Air density at mean sea level, specified as double scalar, in
Kg/m3.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rho0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `1.225` |

### **Ambient pressure at mean sea level (N/m^2)** — Ambient pressure `101325` (default) | scalar

Ambient pressure at mean sea level, specified as double scalar, in
N/m2.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `P0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `101325` |

### **Ambient temperature at mean sea level (K)** — Ambient temperature `288.15` (default) | scalar

Ambient temperature at mean sea level (*T*0),
specified as double scalar, in K.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `K` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `101325` |

### **Lowest altitude (m)** — Lowest altitude `0` (default) | scalar

Lowest altitude above which temperature and pressure lapse, specified as double scalar,
in m. **Lowest altitude (m)** must be below
**Height of tropopause**.

#### Dependencies

This parameter is enabled when the **Change atmospheric
parameters** check box is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `h0` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0` |

## Libraries

Aerospace Blockset / Environment / Atmosphere

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement lapse rate model for atmosphere

The Lapse Rate Model block implements the mathematical representation of the lapse rate
atmospheric equations for ambient temperature, pressure, density, and speed of sound for
the input geopotential altitude.

The Lapse Rate Model and ISA Atmosphere Model blocks are alternative configurations of the same
block.

The Lapse Rate Model block has these implementations:

- Lapse Rate Model — The lapse rate model implements the
  mathematical representation of the lapse rate atmospheric equations for ambient
  temperature, pressure, density, and speed of sound for the input geopotential
  altitude. You can customize this atmospheric model by specifying atmospheric
  properties.
- ISA Atmosphere Model — The ISA model implements the
  mathematical representation of the ISA values for ambient temperature, pressure,
  density, and speed of sound for the input geopotential altitude between sea
  level (0 m) and tropopause (20000 m). To convert from the Lapse Rate
  implementation to the ISA implementation, clear the **Change atmospheric
  parameters** parameter.

The Lapse Rate Model block icon displays the input and output port labels in metric
units.
