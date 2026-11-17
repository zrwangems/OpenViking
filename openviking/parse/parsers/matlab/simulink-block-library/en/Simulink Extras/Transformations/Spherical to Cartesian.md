---
type: simulink-block
title: 'Spherical to Cartesian'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'sphericaltocartesian'
documentation_source_path: '../simulink/ref_extras/sphericaltocartesian.html'
language: en
---

# Spherical to Cartesian

## Ports
```yaml
ports:
- name: Port_1
  summary: '*r* spherical coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_2
  summary: '*theta* spherical coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_3
  summary: '*phi* spherical coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_1
  summary: '*x* Cartesian coordinate output scalar'
  direction: output
  data_types: single | double
- name: Port_2
  summary: '*y* Cartesian coordinate output scalar'
  direction: output
  data_types: single | double
- name: Port_3
  summary: '*z* Cartesian coordinate output scalar'
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — *r* spherical coordinate input scalar

Input signal specifying the *r* coordinate of the spherical coordinates
*(r,theta,phi)*. All inputs must be real scalars of
the same data type.

**Data Types:** `single` | `double`

### **Port\_2** — *theta* spherical coordinate input scalar

Input signal specifying the *r* coordinate of the spherical coordinates
*(r,theta,phi)*. All inputs must be real scalars of
the same data type.

**Data Types:** `single` | `double`

### **Port\_3** — *phi* spherical coordinate input scalar

Input signal specifying the *r* coordinate of the spherical coordinates
*(r,theta,phi)*. All inputs must be real scalars of
the same data type.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — *x* Cartesian coordinate output scalar

Output signal specifying the *x* value in the
cartesian coordinates *(x,y,z)*.

**Data Types:** `single` | `double`

### **Port\_2** — *y* Cartesian coordinate output scalar

Output signal specifying the *x* value in the
cartesian coordinates *(x,y,z)*.

**Data Types:** `single` | `double`

### **Port\_3** — *z* Cartesian coordinate output scalar

Output signal specifying the *x* value in the
cartesian coordinates *(x,y,z)*.

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

Transform spherical coordinates to Cartesian coordinates

The Spherical to Cartesian block transforms the spherical coordinates
*(r*, *theta*, *phi*) to the
Cartesian coordinates (*x*, *y*,
*z*).

The first input is *r*, the second input is *theta*, and
the third input is *phi*. The angles *theta* and
*phi* are in radians. The first output is *x*, the
second output is *y*, and the third output is
*z*.

The spherical coordinate *r*  is the length of the line from the origin to
a point *P*. The spherical coordinate *theta* (the
azimuth) is the angle measured in radians from the positive x-axis to the projection, in
the *x*-*y* plane, of the line from the origin to
*P*. The spherical coordinate *phi* (the zenith)
is the angle, measured in radians, from the positive *z*-axis to the
line from the origin to *P*. The Cartesian coordinates
(*x*, *y*, *z*) describe the
point *P* with respect to the *x*-axis,
*y*-axis, and *z*-axis.

**Note**

The MATLAB® function `cart2sph` measures *phi* from
the *x*-*y* plane.

*x* = *r* ×
sin(*phi*) ×
cos(*theta*)

*y* = *r* ×
sin(*phi*) ×
sin(*theta*)

*z* = *r* ×
cos(*phi*)

**Note**

The notation for spherical coordinates might differ from that
used in other references. Sometimes, the order of *theta*  and *phi* is
reversed. Sometimes, *theta* denotes the zenith and *phi* denotes the azimuth.
