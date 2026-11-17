---
type: simulink-block
title: 'MATLAB Animation'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation'
documentation_page: 'matlabanimation'
documentation_source_path: 'matlabanimation.html'
language: zh-CN
chinese_source: official
---

# MATLAB Animation

Create six-degrees-of-freedom multibody custom geometry block

Create six-degrees-of-freedom multibody custom geometry block

- MATLAB Animation block

**Libraries:**

Aerospace Blockset /
Animation /
MATLAB-Based Animation

## Description

The MATLAB Animation block creates a six-degrees-of-freedom multibody custom
geometry block based on the `Aero.Animation` object. This block
animates one or more vehicle geometries with  *`x-y-z`* position
and Euler angles through the specified bounding box, camera offset, and field of view.
This block expects the rotation order *`z-y-x`* (psi, theta,
phi).

To update the camera parameters in the animation, first set
the parameters then close and double-click the block to reopen the MATLAB® Animation window.

To access the parameters for this block, do one of:

- Right-click the block, then select **Mask** > **Mask Parameters**.
- Double-click the block to display the MATLAB Animation window, then click the **Block
  Parameters** icon.

**Note**

The underlying graphics system stores values in single precision. As a result, you
might notice that motion at coordinate positions greater than approximately 1e6
appear unstable. This is because a single-precision number has approximately six
digits of precision. The instability is due to quantization at the local value of
the `eps`
MATLAB function. To visualize more stable motion for coordinates beyond 1e6,
either offset the input data to a local zero, or scale down the coordinate values
feeding the visualization.

## Ports

### Input

### **Port\_1** — Downrange position, crossrange position, and altitude of vehicle three-element vector

Downrange position, crossrange position, and altitude of the vehicle
in Earth coordinates, specified as a three-element vector. The number on
the port indicates the vehicle number.

**Data Types:** `double`

### **1.Xe** — Downrange position, crossrange position, and altitude of vehicle three-element vector

Downrange position, crossrange position, and altitude of the vehicle
in Earth coordinates, specified as a three-element vector. The number on
the port indicates the vehicle number.

**Data Types:** `double`

### **1.φ θ ψ** — Euler angles three-element vector

Euler angles (roll, pitch, and yaw) of the vehicle, specified as a
three-element vector. The number on the port indicates the vehicle
number.

**Data Types:** `double`

### **Port\_N** — Downrange position, crossrange position, and altitude (positive down) three-element vector

Nth downrange position, crossrange position, and altitude (positive
down) of the vehicle, specified as a three-element vector. The number on
the port indicates the vehicle number.

#### Dependencies

To enable this port, select a **Vehicles** number
from `2` to
`10`.

**Data Types:** `double`

### **Port\_N** — Euler angles three-element vector

Nth input Euler angles (roll, pitch, and yaw) of the vehicle,
specified as a three-element vector. The number on the port indicates
the vehicle number.

#### Dependencies

To enable this port, select a **Vehicles** number
from `2` to
`10`.

**Data Types:** `double`

## Parameters

### **Vehicles** — Vehicle to animate `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

Vehicle to animate, specified from `1` to
`10`.

#### Dependencies

Selecting a vehicle number from `2` to
`10` adds corresponding input ports. Each
vehicle has its own set of input ports, denoted by the number at the
beginning of the input port label.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Vehicles` |
| **Type**: character vector |
| **Values**: `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` |
| **Default**: `'1'` |

### **Geometries (use 'quotes' on filenames)** — Vehicle geometries `'astredwedge.mat'` (default) | MAT-file

Vehicle geometries, specified in a MAT-file. You can specify these
geometries using:

- Variable name, for example `geomVar`
- Cell array of variable names, for example `{geomVar,
  AltGeomVar}`
- Character vector with single quotes, for example,
  `'astredwedge.mat'`
- Mixed cell array of variable names and character vectors, for
  example `{'file1.mat', 'file2.mat', 'file3.ac',
  geomVar}`

**Note**

All specified geometries specified must exist in the MATLAB workspace and file names must exist in the current folder
or be on the MATLAB path.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Geometries` |
| **Type**: character vector |
| **Values**: MAT-file |
| **Default**: `'astredwedge.mat'` |

### **Bounding box coordinates** — Boundary coordinates `[-50,50,-50,50,-50,50]` (default) | six-element vector

Boundary coordinates for the vehicle, specified as a six-element
vector.

This parameter is not tunable during simulation. A change to this
parameter takes effect after simulation stops.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BoundingBoxCoordinates` |
| **Type**: character vector |
| **Values**: six-element vector |
| **Default**: `'[-50,50,-50,50,-50,50]'` |

### **Camera offset** — Distance from camera aim point to camera `[-150,-50,0]` (default) | three-element vector

Distance from the camera aim point to the camera itself, specified as a
three-element vector.

This parameter is not tunable during simulation. A change to this
parameter takes effect after simulation stops.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CameraOffset` |
| **Type**: character vector |
| **Values**: three-element vector |
| **Default**: `'[-150,-50,0]'` |

### **Camera view angle** — Camera view angle `3` (default) | scalar

Camera view angle, specified as a double scalar. By default, the camera aim point is the
position of the first body lagged dynamically to indicate motion.

This parameter is not tunable during simulation. A change to this
parameter takes effect after simulation stops.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CameraViewAngle` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'3'` |

### **Sample time** — Sample time `0.2` (default) | scalar

Sample time (-1 for inherited), specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.2'` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## See Also

`Aero.Animation`

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
