---
type: simulink-block
title: 'Wind Angular Rates'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'windangularrates'
documentation_source_path: 'windangularrates.html'
language: en
---

# Wind Angular Rates

## Ports

### Input

### **ɑ β** — Angles of attack and sideslip 2-by-1 vector

Angle of attack and sideslip, specified as a 2-by-1 vector, in
radians.

**Data Types:** `double`

### **dɑ/dt dβ/dt** — Rates of change 2-by-1 vector

Rate of change of the angle of attack and rate of change of the sideslip, specified as a
2-by-1 vector, in radians per second.

**Data Types:** `double`

### **ω** — Body angular rates three-element vector

Body angular rates, specified as a three-element vector, in radians
per second.

**Data Types:** `double`
### Output

### **ωw** — Wind angular rates three-element vector

Wind angular rates, returned as a three-element vector, in radians per second.

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

Calculate wind angular rates from body angular rates, angle of attack, sideslip angle, rate of change of angle of attack, and rate of change of sideslip

The Wind Angular Rates block supports the equations of motion in wind-fixed
frame models by calculating the wind-fixed angular rates
(*pw, qw,
rw*). For more information on the equation used
for the calculation, see Algorithms.
