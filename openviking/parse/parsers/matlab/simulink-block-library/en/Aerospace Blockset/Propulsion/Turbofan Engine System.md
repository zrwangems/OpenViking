---
type: simulink-block
title: 'Turbofan Engine System'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'turbofanenginesystem'
documentation_source_path: 'turbofanenginesystem.html'
language: en
---

# Turbofan Engine System

## Ports

### Input

### **Throttle position** — Throttle position scalar | vector

Throttle position, specified as a scalar or vector. This value can
vary from zero to one, corresponding to no and full throttle.

**Data Types:** `double`

### **Mach** — Mach number scalar

Mach number, specified as a scalar.

**Data Types:** `double`

### **Altitude** — Altitude scalar | vector

Altitude, specified as scalar or vector, in the units specified in the
**Units** parameter.

**Data Types:** `double`

### **Initial thrust** — Initial thrust scalar | vector

Initial thrust, specified as a scalar or vector, in the units specified in the
**Units** parameter.

#### Dependencies

To enable this port, set **Initial thrust
source** to `External`.

**Data Types:** `double`
### Output

### **Thrust** — Thrust scalar | vector

Thrust, returned as a scalar or vector, in the units specified in the
**Units** parameter.

**Data Types:** `double`

### **Fuel flow** — Fuel flow scalar | vector

Fuel flow, returned as scalar or vector, in the units specified in the
**Units** parameter units per second.

**Data Types:** `double`

## Parameters

### **Units** — Input and output units `Metric (MKS)` (default) | `English`

Input and output units, specified as:

| Units | Altitude | Thrust | Fuel Flow |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Newtons | Kilograms per second |
| `English` | Feet | Pound force | Pound mass per second |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English'` |
| **Default**: `'Metric (MKS)'` |

### **Initial thrust source** — Initial thrust source `Internal` (default) | `External`

Initial thrust, specified as:

|  |  |
| --- | --- |
| `Internal` | Use the value of the **Initial thrust** parameter. |
| `External` | Use external input for initial thrust value. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ic_source` |
| **Type**: character vector |
| **Values**: `'Internal'` | `'External'` |
| **Default**: `'Internal'` |

### **Initial thrust** — Initial `0` (default) | scalar

Initial thrust value, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IC` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0'` |

### **Maximum sea-level static thrust** — Maximum thrust at sea-level `45000` (default) | scalar

Maximum thrust at sea-level, specified as a double scalar, at a Mach value of 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Fmax` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'45000'` |

### **Fastest engine time constant at sea-level static (sec)** — Fastest engine time at sea level `1` (default) | scalar

Fastest engine time at sea level, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `tau` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Sea-level static thrust specific fuel consumption** — Thrust-specific fuel consumption at sea level `0.35` (default) | scalar

Thrust-specific fuel consumption at sea level, specified as a double scalar, in specified
mass units per hour per specified thrust units, at:

- Mach value of 0
- Maximum thrust

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SFC` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.35'` |

### **Ratio of installed thrust to uninstalled thrust** — Coefficient representing loss `0.9` (default) | scalar

Coefficient representing the loss in thrust due to engine installation, specified as a
double value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nt` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.9'` |

## Libraries

Aerospace Blockset / Propulsion

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement first-order representation of turbofan engine with controller

The Turbofan Engine System block computes the thrust and the
fuel mass flow rate of a turbofan engine and controller at a specific throttle position,
Mach number, and altitude. For more information on this system, see Algorithms.

The Turbofan Engine System block icon displays the input and output units
selected from the **Units** parameter.
