---
type: simulink-block
title: '6th Order Point Mass Forces (Coordinated Flight)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '6thorderpointmassforcescoordinatedflight'
documentation_source_path: '6thorderpointmassforcescoordinatedflight.html'
language: en
---

# 6th Order Point Mass Forces (Coordinated Flight)

## Ports
```yaml
ports:
- name: Lift
  summary: Lift scalar | array
  direction: input
  data_types: double
- name: Drag
  summary: Drag scalar | array
  direction: input
  data_types: double
- name: Weight
  summary: Weight scalar | array
  direction: input
  data_types: double
- name: Thrust
  summary: Thrust scalar | array
  direction: input
  data_types: double
- name: ɣ
  summary: Flight path angles scalar | array
  direction: input
  data_types: double
- name: μ
  summary: Bank angle scalar | array
  direction: input
  data_types: double
- name: ɑ
  summary: Angle of attack scalar | array
  direction: input
  data_types: double
- name: Fx
  summary: Force in *x*- axis scalar | array
  direction: output
  data_types: double
- name: Fy
  summary: Force in *y*- axis scalar | array
  direction: output
  data_types: double
- name: Fz
  summary: Force in *z*- axis scalar | array
  direction: output
  data_types: double
```

### Input

### **Lift** — Lift scalar | array

Lift, specified as a scalar or array, in units of force.

**Data Types:** `double`

### **Drag** — Drag scalar | array

Drag, specified as a scalar or array, in units of force.

**Data Types:** `double`

### **Weight** — Weight scalar | array

Weight, specified as a scalar or array, in units of force.

**Data Types:** `double`

### **Thrust** — Thrust scalar | array

Thrust, specified as a scalar or array, in units of force.

**Data Types:** `double`

### **ɣ** — Flight path angles scalar | array

Flight path angle, specified as a scalar or array, in radians.

**Data Types:** `double`

### **μ** — Bank angle scalar | array

Bank angle, specified as a scalar or array, in radians.

**Data Types:** `double`

### **ɑ** — Angle of attack scalar | array

Angle of attack, specified as a scalar or array, in radians.

**Data Types:** `double`
### Output

### **Fx** — Force in *x*- axis scalar | array

Force in *x*-axis, specified as a scalar or array, in
units of force.

**Data Types:** `double`

### **Fy** — Force in *y*- axis scalar | array

Force in *y*-axis, specified as a scalar or array, in
units of force.

**Data Types:** `double`

### **Fz** — Force in *z*- axis scalar | array

Force in *z*-axis, specified as a scalar or array, in
units of force.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Aerospace Blockset / Equations of Motion / Point Mass

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Calculate forces used by sixth-order point mass in coordinated flight

The 6th Order Point Mass Forces (Coordinated Flight) block
calculates the applied forces for a single point mass or multiple point masses. For more
information on the system for the applied forces, see Algorithms.
