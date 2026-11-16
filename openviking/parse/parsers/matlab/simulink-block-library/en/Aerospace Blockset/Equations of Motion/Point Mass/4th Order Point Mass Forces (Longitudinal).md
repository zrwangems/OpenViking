---
type: simulink-block
title: '4th Order Point Mass Forces (Longitudinal)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '4thorderpointmassforceslongitudinal'
documentation_source_path: '4thorderpointmassforceslongitudinal.html'
language: en
---

# 4th Order Point Mass Forces (Longitudinal)

## Ports

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

### **ɣ** — Flight path angle scalar | array

Flight path angle, specified as a scalar or array, in radians.

**Data Types:** `double`

### **μ** — Bank angle scalar | array

Bank angle, specified as a scalar or array, in radians.

**Data Types:** `double`

### **ɑ** — Angle of attack scalar | array

Angle of attack, specified as a scalar or array, in radians.

**Data Types:** `double`
### Output

### **Fx** — Force in *x*-axis scalar | array

Force in *x*-axis, returned as a scalar or array, in
units of force.

**Data Types:** `double`

### **Fz** — Force in *z*-axis scalar | array

Force in *z*-axis, returned as a scalar or array, in
units of force.

**Data Types:** `double`

## Parameters

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

Calculate forces used by fourth-order point mass

The 4th Order Point Mass Forces (Longitudinal) block
calculates the applied forces for a single point mass or multiple point masses. For
more information on the system for the applied forces, see Algorithms.
