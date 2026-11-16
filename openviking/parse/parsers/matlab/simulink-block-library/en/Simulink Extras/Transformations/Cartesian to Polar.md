---
type: simulink-block
title: 'Cartesian to Polar'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'cartesiantopolar'
documentation_source_path: '../simulink/ref_extras/cartesiantopolar.html'
language: en
---

# Cartesian to Polar

## Ports

### Input

### **Port\_1** — *x* Cartesian coordinate input scalar

Input signal specifying the *x* value in the cartesian coordinates
*(x,y)*. Both inputs must be real scalars of the
same data type.

**Data Types:** `single` | `double`

### **Port\_2** — *y* Cartesian coordinate input scalar

Input signal specifying the *y* value in the Cartesian coordinates
*(x,y)*. Both inputs must be real scalars of the
same data type.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — *r* Polar coordinate output scalar

Output signal specifying the *r* coordinate of the
Polar coordinates *(r,theta)*.

**Data Types:** `single` | `double`

### **Output 2** — *theta* Polar coordinate output scalar

Output signal specifying the *theta* coordinate of
the Polar coordinates *(r,theta)*.

**Data Types:** `single` | `double`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Extras / Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008b**

## Description

Cartesian coordinates to polar coordinates

The Cartesian to Polar block transforms Cartesian coordinates
(*x*, *y*) to polar coordinates
(*r*, *theta*).

The first and second inputs correspond to *x* and *y*,
respectively. The first and second outputs correspond to *r* and
*theta*, respectively. The angle *theta* is in
radians.

The Cartesian coordinates (*x*, *y*) describe a point with
respect to the *x*-axis and the *y*-axis. The polar
coordinates (*r*, *theta*) describe the same point
where *r* is the distance from the origin and
*theta* is the counterclockwise angle in radians from the positive
*x*-axis.

r=x2+y2theta=arctan(yx)
