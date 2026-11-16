---
type: simulink-block
title: 'Linear Second-Order Actuator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Actuators'
documentation_page: 'linearsecondorderactuator'
documentation_source_path: 'linearsecondorderactuator.html'
language: en
---

# Linear Second-Order Actuator

## Ports

### Input

### **Ademand** — Demanded actuator position scalar | array

Demanded actuator position, specified as a scalar or array.

**Data Types:** `double`
### Output

### **Aactual** — Actual actuator position scalar | array

Actual actuator position, returned as a scalar or array.

**Data Types:** `double`

## Parameters

### **Natural frequency** — Natural frequency `1` (default) | scalar

Natural frequency of the actuator, specified as a scalar double, in radians per
second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `wn_fin` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'1'` |

### **Damping ratio** — Damping ratio `0.3` (default) | scalar

Damping ratio of the actuator, specified as a scalar double.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_fin` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'0.3'` |

### **Initial position** — Initial position `0` (default) | scalar

Initial position of the actuator, specified as a scalar double. The units of initial
position must be the same as the
**Ademand** input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_act_0` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'0'` |

### **Initial velocity** — Initial velocity `0` (default) | scalar

Initial velocity of the actuator, specified as a scalar double. The units of initial
velocity must be the same as the
**Ademand** input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_act_vel` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'0'` |

## Libraries

Aerospace Blockset / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Implement second-order linear actuator

The Second Order Linear Actuator block outputs the actual
actuator position using the input demanded actuator position and other parameters that
define the system.
