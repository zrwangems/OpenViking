---
type: simulink-block
title: 'Aerodynamic Forces and Moments'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Aerodynamics'
documentation_page: 'aerodynamicforcesandmoments'
documentation_source_path: 'aerodynamicforcesandmoments.html'
language: en
---

# Aerodynamic Forces and Moments

## Ports

### Input

### **Coef** — Aerodynamic coefficients six-element vector

Aerodynamic coefficients (in the chosen input axes) for forces and
moments, specified as a vector. These coefficients are ordered into a
vector depending on the choice of axes:

| Input Axes | Input Vector |
| --- | --- |
| Body | (axial force *C*x, side force *C*y, normal force *C*z, rolling moment *C*l, pitching moment *C*m, yawing moment *C*n) |
| Stability | (drag force *C*D(β=0), side force *C*y, lift force *C*L, rolling moment *C*l, pitching moment *C*m, yawing moment *C*n) |
| Wind | (drag force *C*D, cross-wind force *C*c, lift force *C*L, rolling moment *C*l, pitching moment *C*m, yawing moment *C*n) |

**Data Types:** `double`

### **qbar** — Dynamic pressure scalar | three-element vector

Dynamic pressure, specified as a 1-by-3 array.

**Data Types:** `double`

### **CG** — Center of gravity three-element vector

Center of gravity, specified as a 1-by-3 vector.

**Data Types:** `double`

### **CP** — Center of pressure three-element vector

Center of pressure, specified as a 1-by-3 vector. This can also be
taken as any general moment reference point as long as the rest of the
model reflects the use of the moment reference point.

**Data Types:** `double`

### **Vb** — Velocity in the body axes three-element vector

Velocity in the body axes. specified as a 1-by-3 vector.

#### Dependencies

This port is enabled if the **Input axes**
parameter is set to `Wind` or
`Stability`.

**Data Types:** `double`
### Output

### **F** — Aerodynamic forces three-element vector

Aerodynamic forces (in the chosen output axes), returned as
three-element vector, at the center of gravity in *x*-,
*y*-, and *z*-axes.

**Data Types:** `double`

### **M** — Aerodynamic moments three-element vector

Aerodynamic moments (in the chosen output axes), returned as
three-element vector, at the center of gravity in *x*-,
*y*-, and *z*-axes.

**Data Types:** `double`

## Parameters

### **Input axes** — Coordinate system for input coefficients `Body` (default) | `Stability` | `Wind`

Coordinate system for input coefficients, specified as
`Body` (default), `Stability`, or
`Wind`.

#### Dependencies

Selecting `Stability` or
`Wind` enables input port Port\_5.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `inputAxes` |
| **Type**: character vector |
| **Values**: `'Body'` | `'Stability'` | `'Wind'` |
| **Default**: `'Body'` |

### **Force axes** — Coordinate system for aerodynamic force `Body` (default) | `Stability` | `Wind`

Coordinate system for aerodynamic force, specified as
`Body` (default), `Stability`, or
`Wind`.

#### Dependencies

Selecting `Stability` or
`Wind` enables input port Port\_5.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outputForcesAxes` |
| **Type**: character vector |
| **Values**: `'Body'` | `'Stability'` | `'Wind'` |
| **Default**: `'Body'` |

### **Moment axes** — Coordinate system for aerodynamic moment `Body` (default) | `Stability` | `Wind`

Coordinate system for aerodynamic moment, specified as
`Body` (default), `Stability`, or
`Wind`.

#### Dependencies

Selecting `Stability` or
`Wind` enables input port Port\_5.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `outputMomentAxes` |
| **Type**: character vector |
| **Values**: `'Body'` | `'Stability'` | `'Wind'` |
| **Default**: `'Body'` |

### **Reference area** — Reference area `1` (default) | any double value

Reference area for calculating aerodynamic forces and moments, specified
as any double value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `S` |
| **Type**: character vector |
| **Values**: any double value |
| **Default**: `'1'` |

### **Reference span** — Reference span `1` (default) | any double value

Reference span for calculating aerodynamic moments in
*x*-axes and *z*-axes, specified as any
double value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `b` |
| **Type**: character vector |
| **Values**: any double value |
| **Default**: `'1'` |

### **Reference length** — Reference length `1` (default) | any double value

Reference length for calculating aerodynamic moment in the
*y*-axes, specified as any double value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `cbar` |
| **Type**: character vector |
| **Values**: any double value |
| **Default**: `'1'` |

## Libraries

Aerospace Blockset / Aerodynamics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute aerodynamic forces and moments using aerodynamic coefficients, dynamic pressure, center of gravity, center of pressure, and velocity

The Aerodynamic Forces and Moments block computes the
aerodynamic forces and moments about the center of gravity.

The Aerodynamic Forces and Moments block port labels change based on
the coordinate system selected from the **Input axes**, **Force
axes**, and **Moment axes** list.
