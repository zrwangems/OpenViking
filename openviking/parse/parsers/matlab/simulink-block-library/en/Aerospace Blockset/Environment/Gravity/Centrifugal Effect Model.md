---
type: simulink-block
title: 'Centrifugal Effect Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'centrifugaleffectmodel'
documentation_source_path: 'centrifugaleffectmodel.html'
language: en
---

# Centrifugal Effect Model

## Ports

### Input

### **Xecef** — Planet-centered planet-fixed coordinates m-by-3 matrix

Planet-centered planet-fixed coordinates from the center of the
planet, specified as a scalar. If **Planet model** has
a value of `Earth`, this matrix contains Earth-centered
Earth-fixed (ECEF) coordinates. The block does not use explicit
units.

**Data Types:** `double`

### **ω** — Planetary rotation rate scalar

Planetary rotation rate, specified as a scalar, in rad/sec.

#### Dependencies

To enable this parameter, set **Planetary rotational rate
(rad/sec)** to `Custom`.

**Data Types:** `double`
### Output

### **Output 1** — Gravity values m-by-3 array

Gravity values, returned as an m-by-3 array, in the *x*-axis,
*y*-axis, and *z*-axis of the
planet-centered planet-fixed coordinates, in input distance units per
second squared.

**Data Types:** `double`

## Parameters

### **Planet model** — Planetary model `Earth` (default) | `Venus` | `Mercury` | `Moon` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Custom`

Planetary model, specified as `Mercury`,
`Venus`, `Earth`,
`Moon`, `Mars`,
`Jupiter`, `Saturn`,
`Uranus`, `Neptune`,
or `Custom`. The block uses the rotation of the
selected planet to implement the mathematical representation of the
centrifugal effect.

#### Dependencies

Selecting `Custom` enables the
**Planetary rotational rate (rad/sec)** and
**Input planetary rotation rate**
parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ptype` |
| **Type**: character vector |
| **Values**: `'Mercury'` | `'Venus'` | `'Earth'` | `'Moon'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Custom'` |
| **Default**: `'Earth'` |

### **Planetary rotational rate (rad/sec)** — Planetary rotational rate `7.2921150e-05` (default) | scalar

Planetary rotational rate in radians per second.

If you want to specify the planetary rotational rate as an input to the
block, see the **Input planetary rotation rate** parameter.

#### Dependencies

Selecting the **Input planetary rotation rate** check
box disables the **Planetary rotational rate
(rad/sec)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `omega` |
| **Type**: character vector |
| **Values**: `'7.2921150e-05'` | scalar |
| **Default**: `'7.2921150e-05'` |

### **Input planetary rotation rate** — Planetary rotation rate port `off` (default) | `on`

Select this check box to enable the ω input port. You can then input a
planetary rotation rate as a block input.

#### Dependencies

Selecting this check box enables the ω and disables the
**Planetary rotational rate (rad/sec)**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rate_loc` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Libraries

Aerospace Blockset / Environment / Gravity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**

## Description

Implement mathematical representation of centrifugal effect for planetary gravity

The Centrifugal Effect Model block implements the mathematical representation
of centrifugal effect for planetary gravity. The gravity centrifugal effect is the
acceleration portion of centrifugal force effects due to the rotation of a planet. This
block implements this representation using planetary rotation rates. You use centrifugal
force values in rotating or non-inertial coordinate systems.
