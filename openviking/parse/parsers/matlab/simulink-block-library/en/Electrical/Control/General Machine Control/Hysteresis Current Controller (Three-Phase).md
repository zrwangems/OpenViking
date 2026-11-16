---
type: simulink-block
title: 'Hysteresis Current Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control'
documentation_page: 'hysteresiscurrentcontrollerthreephase'
documentation_source_path: 'ref/hysteresiscurrentcontrollerthreephase.html'
language: en
---

# Hysteresis Current Controller (Three-Phase)

## Ports

### Input

### **iabc\*** — Current vector

Three-phase reference currents.

**Data Types:** `single` | `double`

### **iabc** — Current vector

Measured three-phase currents.

**Data Types:** `single` | `double`
### Output

### **S** — Controller output vector

Six-pulse vector for power converter control.

**Data Types:** `single` | `double`

## Parameters

### **Current hysteresis band (A)** — Hysteresis band `1` (default) | positive number

Hysteresis band, *h*, for the current controller. The switch-on point is
*h*/2 and the switch-off point is
-*h*/2.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / General Machine Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Three-phase hysteresis current control

The Hysteresis Current Controller (Three-Phase) block implements three-phase
hysteresis current control for power converters.
