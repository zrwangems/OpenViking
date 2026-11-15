---
type: simulink-block
title: '3DoF Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Animation Based on MATLAB'
documentation_page: '3dofanimation'
documentation_source_path: '3dofanimation.html'
language: en
---

# 3DoF Animation

## Ports

### Input

### **xtzt** — Target downrange position and altitude (positive down) two-element vector

Downrange position and altitude (positive down) of the target,
specified as a two-element vector.

**Data Types:** `double`

### **xeze** — Craft downrange position and altitude (positive down) two-element vector

Downrange position and altitude (positive down) of the craft,
specified as a two-element vector.

**Data Types:** `double`

### **θ** — Attitude of craft 1-by-1 scalar

Attitude of the craft, specified as 1-by-1 scalar, in radians.

**Data Types:** `double`

## Parameters

### **Axes limits [xmin xmax ymin ymax zmin zmax]** — Axes limits `[0 5000 -2000 2000 -5050 -3050]` (default) | six-element vector

Three-dimensional space to be viewed, specified as a six-element
vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u1` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[0 5000 -2000 2000 -5050 -3050]'` |

### **Time interval between updates** — Time interval `0.05` (default) | scalar

Time interval at which the animation is redrawn, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u2` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.05'` |

### **Size of craft displayed** — Scale factor `1.0` (default) | scalar

Scale factor to adjust the size of the craft and target, specified as a double
scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u3` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1.0'` |

### **Enter view** — Entrance view `Fixed position` (default) | `Cockpit` | `Fly alongside`

Preset entrance views, specified as:

- `Fixed position`
- `Cockpit`
- `Fly alongside`

These preset views are specified by MATLAB Graphics parameters **CameraTarget** and **CameraUpVector** for the figure axes.

**Tip**

To customize the position and field of view for the selected view, use
the **Position of camera** and **View angle** parameters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u5` |
| **Type**: character vector |
| **Values**: `Fixed position` | `Cockpit` | `Fly alongside` |
| **Default**: `'Fixed position'` |

### **Position of camera [xc yc zc]** — Camera position `[2000 500 -3150]` (default) | three-element vector

Camera position, specified using the MATLAB Graphics parameter CameraPosition
for the figure axes as a three-element vector. Used in all cases except for
the Cockpit view.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u6` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[2000 500 -3150]'` |

### **View angle** — View angle `10` (default) | scalar

View angle, specified as MATLAB Graphics parameter CameraViewAngle for the figure axes in degrees as a double
scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u7` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'10'` |

### **Enable animation** — Display animation `on` (default) | `off`

To display the animation during the simulation, select this check box. If
not selected, the animation is not displayed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `u8` |
| **Type**: character vector |
| **Values**: `on` | `off` |
| **Default**: `'on'` |

## Libraries

Aerospace Blockset / Animation / MATLAB-Based Animation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create 3-D MATLAB Graphics animation of three-degrees-of-freedom object

The 3DoF Animation block displays a 3-D animated view of a
three-degrees-of-freedom (3DoF) craft, its trajectory, and its target using MATLAB® Graphics.

The 3DoF Animation block uses input values and dialog parameters to create
and display the animation.

This block does not produce deployable code, but you can use it with Simulink®
Coder™ external mode as a SimViewingDevice.
