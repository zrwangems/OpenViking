---
type: simulink-block
title: 'Fixed-Wing UAV Point Mass'
family: 'algorithms'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'fixedwinguavpointmass'
documentation_source_path: 'ref/fixedwinguavpointmass.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Wing UAV Point Mass

## 端口

### 输入

### **Lift** — 升力标量

Lift，指定为以力为单位的标量。

**数据类型：** `double`

### **Drag** — 阻力标量

Drag，指定为以力为单位的标量。

**数据类型：** `double`

### **Weight** — 重量标量

Weight，指定为以力为单位的标量。

**数据类型：** `double`

### **Thrust** — 推力标量

Thrust，指定为以力为单位的标量。

**数据类型：** `double`

### **ɣa** — 相对于空气团的飞行路径角标量

Flight path angle relative to the air mass，指定为以 radians 为单位的标量。

**数据类型：** `double`

### **μ** — 滚转角标量

Bank angle，指定为以 radians 为单位的标量。

**数据类型：** `double`

### **ɑ** — 迎角标量

Angle of attack，指定为以 radians 为单位的标量。

**数据类型：** `double`

### **Vwind** — 风向量三元素向量

Wind vector in the direction in which the air mass is moving，指定为三元素向量。

**数据类型：** `double`
### 输出

### **V** — 空速标量

Airspeed，返回为标量。

**数据类型：** `double`

### **G** — 地速投影标量

Ground speed over the Earth (speed of motion over the ground)，返回为标量。

**数据类型：** `double`

### **Va** — 相对于空气团的速度向量三元素向量

Velocity vector relative to the air mass，返回为三元素向量。

**数据类型：** `double`

### **Ve** — 相对于地球且采用 [North East Down] 取向的速度向量三元素向量

Velocity vector relative to Earth with `[North East Down]` orientation，返回为三元素向量。

#### 依赖关系

要启用此端口，请将 **参考坐标系方向** 设置为 `[North East Down]`。

**数据类型：** `double`

### **VENU** — 相对于地球的速度向量三元素向量

Velocity vector relative to Earth with `[East North Up]` orientation，返回为三元素向量。

#### 依赖关系

要启用此端口，请将 **参考坐标系方向** 设置为 `[East North Up]`。

**数据类型：** `double`

### **Xe** — 相对于地球的位置向量三元素向量

Position vector relative to Earth with `[North East Down]` orientation，返回为三元素向量。

#### 依赖关系

要启用此端口，请将 **参考坐标系方向** 设置为 `[North East Down]`。

**数据类型：** `double`

### **XENU** — 相对于地球的位置向量三元素向量

Position vector relative to Earth with `[East North Up]` orientation，返回为三元素向量。

#### 依赖关系

要启用此端口，请将 **参考坐标系方向** 设置为 `[East North Up]`。

**数据类型：** `double`

### **γa** — 相对于空气团的飞行路径角标量

Flight path angle relative to the air mass，返回为标量。

**数据类型：** `double`

### **γ** — 相对于地球的飞行路径角标量

Flight path angle relative to Earth，返回为标量。

**数据类型：** `double`

### **χa** — 相对于空气团的航向角标量

Heading angle relative to air mass，返回为标量。

#### 依赖关系

要启用此端口，请将 **自由度** 设置为 `6th Order (Coordinated Flight)`。

**数据类型：** `double`

### **χ** — 相对于地球的航向角标量

Heading angle relative to Earth，返回为标量。

#### 依赖关系

要启用此端口，请将 **自由度** 设置为 `6th Order (Coordinated Flight)`。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (默认) | `English (velocity in ft/s)` | `English (velocity in kts)`

输入和输出单位，指定如下：

| 单位 | 力 | 速度 | 位置 | 质量 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | newtons | meters per second | meters | kilograms |
| `English (velocity in ft/s)` | pounds | feet per second | feet | slugs |
| `English (velocity in kts)` | pounds | knots | feet | slugs |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (velocity in ft/s)'` | `'English (velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **参考坐标系方向** — 参考坐标系 `[North East Down]` (默认) | `[East North Up]`

用于输入端口和输出端口的参考坐标系，指定为 `[East North Up]` 或 `[North East Down]`。

#### 编程使用

|  |
| --- |
| **模块参数**: `frame` |
| **类型**: character vector |
| **值**: `'[East North Up]'` | `'[North East Down]'` |
| **默认值**: `'[North East Down]'` |

### **自由度** — 自由度 `6th Order (Coordinated Flight)` (默认) | `4th Order (Longitudinal)`

自由度，指定为 `4th Order (Longitudinal)` 或 `6th Order (Coordinated Flight)`。

#### 编程使用

|  |
| --- |
| **模块参数**: `order` |
| **类型**: character vector |
| **值**: `'4th Order (Longitudinal)'` | `'6th Order (Coordinated Flight)'` |
| **默认值**: `'6th Order (Coordinated Flight)'` |

### **初始横向距离** — 初始 East (Earth) 横向距离位置 `0` (默认) | scalar

`[North East Down]` 取向中的初始 East（地球）位置，指定为标量。

#### 依赖关系

此参数的方向指定取决于 **参考坐标系方向** 和 **自由度** 设置：

| 初始横向距离 | 参考坐标系方向 | 自由度 |
| --- | --- | --- |
| East | [North East Down] | 6th Order (Coordinated Flight) |
| North | [East North Up] | 6th Order (Coordinated Flight) |

#### 编程使用

|  |
| --- |
| **模块参数**: `east` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

### **初始纵向距离** — 初始 North (Earth) 纵向距离 `0` (默认) | scalar

质点的初始 North（地球）纵向距离，指定为标量。

#### 依赖关系

此参数的方向指定取决于 **参考坐标系方向** 和 **自由度** 设置：

| 初始纵向距离 | 参考坐标系方向 | 自由度 |
| --- | --- | --- |
| North | [North East Down] | 6th Order (Coordinated Flight) |
| North | [North East Down] | 4th Order (Longitudinal) |
| East | [East North Up] | 6th Order (Coordinated Flight) |
| East | [East North Up] | 4th Order (Longitudinal) |

#### 编程使用

|  |
| --- |
| **模块参数**: `north` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

### **初始高度** — 初始高度 `0` (默认) | scalar

质点的初始高度，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**: `altitude` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

### **初始空速** — 初始空速 `50` (默认) | scalar

质点的初始空速，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**: `'airspeed'` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'50'` |

### **初始飞行路径角** — 初始飞行路径角 `0` (默认) | scalar

质点的初始飞行路径角，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**: `gamma` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

### **初始航向角** — 初始航向角 `0` (默认) | scalar

质点的初始航向角，指定为标量。

#### 依赖关系

要启用此参数，请将 **自由度** 设置为 `6th Order (Coordinated Flight)`。

#### 编程使用

|  |
| --- |
| **模块参数**: `chi` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

### **质量** — 质点质量 `10` (默认) | scalar

质点质量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**: `mass` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'10'` |

## 所属库

UAV Toolbox / Algorithms Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

在协调飞行中积分四阶或六阶质点运动方程

Fixed-Wing Point Mass 模块在协调飞行中积分四阶或六阶质点运动方程。
