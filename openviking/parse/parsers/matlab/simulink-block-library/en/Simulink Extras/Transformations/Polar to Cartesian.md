---
type: simulink-block
title: 'Polar to Cartesian'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Transformations'
documentation_page: 'polartocartesian'
documentation_source_path: '../simulink/ref_extras/polartocartesian.html'
language: en
---

# Polar to Cartesian

## Ports
```yaml
ports:
- name: Port_1
  summary: '*r* polar coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_2
  summary: '*theta* polar coordinate input scalar'
  direction: input
  data_types: single | double
- name: Port_1
  summary: '*x* coordinate output scalar'
  direction: output
  data_types: single | double
- name: Port_2
  summary: '*y* Cartesian coordinate output scalar'
  direction: output
  data_types: single | double
```

### Input

### **Port\_1** — *r* polar coordinate input scalar

Input signal specifying the *r* coordinate of the Polar coordinates
*(r,theta)*. Both inputs must be real scalars of
the same data type.

**Data Types:** `single` | `double`

### **Port\_2** — *theta* polar coordinate input scalar

Input signal specifying the *theta* coordinate of the Polar coordinates
*(r,theta)*. Both inputs must be real scalars of
the same data type.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — *x* coordinate output scalar

Output signal specifying the *x* value in the
Cartesian coordinates *(x,y)*.

**Data Types:** `single` | `double`

### **Port\_2** — *y* Cartesian coordinate output scalar

Output signal specifying the *y* value in the
Cartesian coordinates *(x,y)*.

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

Convert polar coordinates to Cartesian coordinates

The Polar to Cartesian block transforms the polar coordinates
(*r*, *theta*) to the Cartesian coordinates
(*x*, *y*).

The first and second inputs correspond to *r* and *theta*,
respectively. The angle *theta* is in radians. The first and second
outputs correspond to *x* and *y*,
respectively.

The polar coordinates (*r*, *theta*) describe a point
where *r* is the distance from the origin, and *theta*
is the counterclockwise angle in radians from the positive *x*-axis.
The Cartesian coordinates (*x*, *y*) describe the same
point with respect to the *x*-axis and
*y*-axis.

*x* = *r* ×
cos(*theta*)

*y* = *r* ×
sin(*theta*)
