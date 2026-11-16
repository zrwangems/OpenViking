---
type: simulink-block
title: 'Nonlinear Second-Order Actuator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Vehicle Components / Actuators'
documentation_page: 'nonlinearsecondorderactuator'
documentation_source_path: 'nonlinearsecondorderactuator.html'
language: en
---

# Nonlinear Second-Order Actuator

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

Natural frequency of actuator, specified as a scalar double, in radians per
second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `wn_fin` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'1'` |

### **Damping ratio** — Damping ratio `0.3` (default) | scalar

Damping ratio of actuator, specified as a scalar double.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `z_fin` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'0.3'` |

### **Maximum deflection** — Largest actuator position allowable `20*pi/180` (default) | scalar

Largest actuator position allowable, specified as a scalar double, in the same units as
demanded actuator position.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_max` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'20*pi/180'` |

### **Minimum deflection** — Smallest actuator position allowable `-20*pi/180` (default) | scalar

Smallest actuator position allowable, specified as a scalar double, in the same units as
demanded actuator position.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_min` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'-20*pi/180'` |

### **Rate limit** — Fastest speed allowable `500*pi/180` (default) | scalar

Fastest speed allowable for actuator motion, specified as a scalar double, in the units
of demanded actuator position per second.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_maxrate` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'500*pi/180'` |

### **Initial position** — Initial position `0` (default) | scalar

Initial position of actuator, specified as a scalar double, in the same units as demanded
actuator position.

- If the specified value is less than the value of **Minimum
  deflection**, the block sets the value of
  **Minimum deflection** as the initial position
  value.
- If the specified value is greater than the value of
  **Maximum deflection**, the block sets the
  value of **Maximum deflection** as the initial
  position value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fin_act_0` |
| **Type**: character vector |
| **Values**: scalar | double |
| **Default**: `'0'` |

### **Initial velocity** — Initial velocity `0` (default) | scalar

Initial velocity of actuator, specified as a scalar double, in the units of demanded
actuator position per second.

If the absolute value of the specified value is greater than the absolute
value of **Rate Limit**, this block sets the value of
**Rate Limit** as the initial velocity value.

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

Implement second-order actuator with rate and deflection limits

The Second Order Nonlinear Actuator block outputs the actual
actuator position using the input demanded actuator position and other dialog box
parameters that define the system.
