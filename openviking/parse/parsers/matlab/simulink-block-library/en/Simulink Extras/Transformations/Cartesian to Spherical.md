---
type: simulink-block
title: 'Cartesian to Spherical'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'cartesiantospherical'
documentation_source_path: '../simulink/ref_extras/cartesiantospherical.html'
language: en
---

# Cartesian to Spherical

## Ports
```yaml
ports:
- name: Port_1
  summary: '*x* Cartesian coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_2
  summary: '*y* Cartesian coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_3
  summary: '*z* Cartesian coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_1
  summary: '*r* spherical coordinate output scalar'
  direction: output
  data_types: single | double
- name: Port_2
  summary: '*theta* spherical coordinate output scalar'
  direction: output
  data_types: single | double
- name: Port_3
  summary: '*phi* spherical coordinate output scalar'
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — *x* Cartesian coordinate input scalar

Input signal specifying the *x* value in the cartesian coordinates
*(x,y,z)*. All inputs must be real scalars of the
same data type.

**Data Types:** `single` | `double`

### **Port\_2** — *y* Cartesian coordinate input scalar

Input signal specifying the *y* value in the cartesian coordinates
*(x,y,z)*. All inputs must be real scalars of the
same data type.

**Data Types:** `single` | `double`

### **Port\_3** — *z* Cartesian coordinate input scalar

Input signal specifying the *z* value in the cartesian coordinates
*(x,y,z)*. All inputs must be real scalars of the
same data type.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — *r* spherical coordinate output scalar

Output signal specifying the *r* coordinate of the
spherical coordinates *(r,theta,phi)*.

**Data Types:** `single` | `double`

### **Port\_2** — *theta* spherical coordinate output scalar

Output signal specifying the *theta* coordinate of the spherical
coordinates *(r,theta,phi)*.

**Data Types:** `single` | `double`

### **Port\_3** — *phi* spherical coordinate output scalar

Output signal specifying the *phi* coordinate of the spherical
coordinates *(r,theta,phi)*.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters: []
```

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

Cartesian coordinates to spherical coordinates

The Cartesian to Spherical block transforms the Cartesian coordinates
(*x*, *y*, *z*) to the spherical
coordinates (*r*, *theta*,
*phi*).

The first input is *x*, the second input is *y*, and the
third input is *z*. The first output is *r*, the
second output is *theta*, and the third output is
*phi*. The angles *theta* and
*phi* are in radians.

The Cartesian coordinates (*x*, *y*, *z*)
describe a point *P* with respect to the *x*-axis,
*y*-axis, and *z*-axis. The spherical coordinate
*r*  is the length of the line from the origin to the point
*P*. The spherical coordinate *theta* (the
azimuth) is the angle measured in radians from the positive *x*-axis to
the projection, in the *x*-*y* plane, of the line from
the origin to *P*. The spherical coordinate *phi* (the
zenith) is the angle, measured in radians, from the positive *z*-axis
to the line from the origin to *P*.

**Note**

The MATLAB® function `cart2sph` measures *phi* from
the *x*-*y* plane.

r=x2+y2+z2theta=arctan(yx)phi=arctan(x2+y2z)

**Note**

The notation for spherical coordinates might differ in other
references. Sometimes, the order of *theta*  and *phi* is
reversed. Sometimes, *theta* denotes the zenith and *phi* denotes the azimuth.
