---
type: simulink-block
title: '4th Order Point Mass (Longitudinal)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / Point Mass'
documentation_page: '4thorderpointmasslongitudinal'
documentation_source_path: '4thorderpointmasslongitudinal.html'
language: en
---

# 4th Order Point Mass (Longitudinal)

## Ports

### Input

### **Fx(N)** — Force in *x*-axis scalar | array

Force in *x*-axis, specified as a scalar or array, in
selected units.

**Data Types:** `double`

### **Fz(N)** — Force in *z*-axis scalar | array

Force in *z*-axis, specified as a scalar or array, in
selected units.

**Data Types:** `double`
### Output

### **ɣ** — Flight path angle scalar | array

Flight path angle, returned as a scalar or array, in radians.

**Data Types:** `double`

### **V** — Airspeed scalar | array

Airspeed, returned as a scalar or array, in selected units.

**Data Types:** `double`

### **XEast** — Downrange or amount traveled east scalar | array

Downrange or amount traveled east, returned as a scalar or array, in
selected units.

**Data Types:** `double`

### **XUp** — Altitude or amount traveled up scalar | array

Altitude or amount traveled up, returned as a scalar or array, in
selected units.

**Data Types:** `double`

## Parameters

### **Units** — Units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as:

| Units | Forces | Velocity | Position | Mass |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | newtons | meters per second | meters | kilograms |
| `English (Velocity in ft/s)` | pounds | feet per second | feet | slugs |
| `English (Velocity in kts)` | pounds | knots | feet | slugs |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Initial flight path angle** — Initial flight path angle `0` (default) | scalar | vector

Initial flight path angle of the point mass(es), specified as a scalar or
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gamma0` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'0'` |

### **Initial airspeed** — Initial airspeed `100` (default) | scalar | vector

Initial airspeed of the point mass(es), specified as a scalar or
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `V0` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'100'` |

### **Initial downrange [East]** — Initial downrange `0` (default) | scalar | vector

Initial downrange of the point mass(es), specified as a scalar or
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `x0` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'0'` |

### **Initial altitude [Up]** — Initial altitude of point masses `0` (default) | scalar | vector

Initial altitude of the point mass(es), specified as a scalar or
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `h0` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'0'` |

### **Initial mass** — Point mass `1.0` (default) | scalar | vector

Mass of the point mass(es), specified as a scalar or vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mass0` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'1.0'` |

## Libraries

Aerospace Blockset / Equations of Motion / Point Mass

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate fourth-order point mass

The 4th Order Point Mass (Longitudinal) block performs the
calculations for the translational motion of a single point mass or multiple point
masses. For more information on the system for the translational motion of a single
point mass or multiple mass, see Algorithms.

The 4th Order Point Mass (Longitudinal) block port labels change based
on the input and output units selected from the **Units** list.
