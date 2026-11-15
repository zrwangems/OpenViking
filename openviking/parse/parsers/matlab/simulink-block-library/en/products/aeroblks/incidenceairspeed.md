---
type: simulink-block
title: 'Incidence & Airspeed'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Flight Parameters'
documentation_page: 'incidenceairspeed'
documentation_source_path: 'incidenceairspeed.html'
language: en
---

# Incidence & Airspeed

## Ports

### Input

### **U, w** — Velocity two-element vector

Velocity of the body, specified as a two-element vector, resolved into
the body-fixed coordinate frame.

**Data Types:** `double`
### Output

### **ɑ** — Incidence angle scalar

Incidence angle, returned as a scalar, in radians.

**Data Types:** `double`

### **V** — Airspeed scalar

Airspeed of the body, returned as a scalar.

**Data Types:** `double`

## Parameters

Not documented in R2025b.

## Libraries

Aerospace Blockset / Flight Parameters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate incidence and airspeed

The Incidence & Airspeed block supports the 3DoF
equations of motion model by calculating the angle between the velocity vector and the
body, and also the total airspeed from the velocity components in the body-fixed
coordinate frame.

α=atan(wu)V=u2+w2

**Note**

- For fixed-wing aircraft, the angle, α, computed by the Incidence & Airspeed block is the
  angle between the relative wind and the longitudinal axis of the airframe. This
  angle is denoted in many aerospace engineering references as angle of attack.
  Incidence & Airspeed refers to this angle as the incidence angle.
- In the case of vertical takeoff and landing (VTOL) configurations, the equations
  used for computation are the same as that for fixed-wing aircraft [1]. However, in
  maneuvers involving transitions between cruise and hover, there are likely scenarios
  involving low or zero values of velocity resulting in incorrect incidence and
  side-slip angles. Therefore, the use of this block for analysis of VTOL
  configurations is not recommended. As an alternative, use the 6DOF Wind (Quaternion) or 6DOF Wind (Wind Angles) blocks,
  which provide α and β as outputs.
