---
type: simulink-block
title: 'Fixed-Wing Point Mass'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: 'fixedwingpointmass'
documentation_source_path: 'fixedwingpointmass.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Wing Point Mass

## 端口

### 输入

### **Lift** — 升力标量

升力，指定为以力为单位的标量。

**数据类型：** `double`

### **Drag** — 阻力标量

阻力，指定为以力为单位的标量。

**数据类型：** `double`

### **Weight** — 重力标量

重力，指定为以力为单位的标量。

**数据类型：** `double`

### **Thrust** — 推力标量

推力，指定为以力为单位的标量。

**数据类型：** `double`

### **ɣa** — 相对于气流的航迹角标量

相对于气流的航迹角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **μ** — 滚转角标量

滚转角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **ɑ** — 迎角标量

迎角，指定为以弧度为单位的标量。

**数据类型：** `double`

### **Vwind** — 风矢量三元向量

沿气流运动方向的风矢量，指定为三元向量。

**数据类型：** `double`
### 输出

### **V** — 空速标量

空速，以标量形式返回。

**数据类型：** `double`

### **G** — 地速投影标量

相对于地球的地速（地面运动速度），以标量形式返回。

**数据类型：** `double`

### **Va** — 相对于气流的速度矢量三元向量

相对于气流的速度矢量，以三元向量形式返回。

**数据类型：** `double`

### **Ve** — 相对于地球的速度矢量，`[North East Down]` 方向三元向量

相对于地球的速度矢量，`[North East
Down]` 方向，以三元向量形式返回。

#### 依赖关系

要启用此端口，请将 **Reference frame
orientation** 设置为 `[North East
Down]`。

**数据类型：** `double`

### **VENU** — 相对于地球的速度矢量三元向量

相对于地球的速度矢量，`[East North
Up]` 方向，以三元向量形式返回。

#### 依赖关系

要启用此端口，请将 **Reference frame
orientation** 设置为 `[East North
Up]`。

**数据类型：** `double`

### **Xe** — 相对于地球的位置矢量三元向量

相对于地球的位置矢量，`[North East
Down]` 方向，以三元向量形式返回。

#### 依赖关系

要启用此端口，请将 **Reference frame
orientation** 设置为 `[North East
Down]`。

**数据类型：** `double`

### **XENU** — 相对于地球的位置矢量三元向量

相对于地球的位置矢量，`[East North
Up]` 方向，以三元向量形式返回。

#### 依赖关系

要启用此端口，请将 **Reference frame
orientation** 设置为 `[East North
Up]`。

**数据类型：** `double`

### **γa** — 相对于气流的航迹角标量

相对于气流的航迹角，以标量形式返回。

**数据类型：** `double`

### **γ** — 相对于地球的航迹角标量

相对于地球的航迹角，以标量形式返回。

**数据类型：** `double`

### **χa** — 相对于气流的航向角标量

相对于气流的航向角，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Degrees of Freedom**
设置为 `6th Order (Coordinated Flight)`。

**数据类型：** `double`

### **χ** — 相对于地球的航向角标量

相对于地球的航向角，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Degrees of Freedom**
设置为 `6th Order (Coordinated Flight)`。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)`（默认）| `English (velocity in ft/s)` | `English (velocity in kts)`

输入和输出单位，指定如下：

| 单位 | 力 | 速度 | 位置 | 质量 |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | 牛顿 | 米每秒 | 米 | 千克 |
| `English (velocity in ft/s)` | 磅 | 英尺每秒 | 英尺 | 斯勒格 |
| `English (velocity in kts)` | 磅 | 节 | 英尺 | 斯勒格 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (velocity in ft/s)'` | `'English (velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Reference frame orientation** — 参考坐标系 `[North East Down]`（默认）| `[East North Up]`

用于输入端口和输出端口的参考坐标系，指定为
`[East North Up]` 或 `[North East
Down]`。

#### 编程使用

|  |
| --- |
| **模块参数**：`frame` |
| **类型**：字符向量 |
| **值**：`'[East North Up]'` | `'[North East Down]'` |
| **默认值**：`'[North East Down]'` |

### **Degrees of freedom** — 自由度 `6th Order (Coordinated Flight)`（默认）| `4th Order (Longitudinal)`

自由度，指定为 `4th Order
(Longitudinal)` 或 `6th Order (Coordinated
Flight)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`order` |
| **类型**：字符向量 |
| **值**：`'4th Order (Longitudinal)'` | `'6th Order (Coordinated Flight)'` |
| **默认值**：`'6th Order (Coordinated Flight)'` |

### **Initial crossrange** — 初始东向（地球）横向距离 `0`（默认）| 标量

`[North East Down]` 方向下的初始东向（地球）位置，指定为标量。

#### 依赖关系

此参数的方向指定取决于
**Reference frame orientation** 和
**Degrees of Freedom** 设置：

| Initial crossrange | Reference frame orientation | Degrees of freedom |
| --- | --- | --- |
| East | [North East Down] | 6th Order (Coordinated Flight) |
| North | [East North Up] | 6th Order (Coordinated Flight) |

#### 编程使用

|  |
| --- |
| **模块参数**：`east` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Initial downrange** — 初始北向（地球）纵向距离 `0`（默认）| 标量

质点模型的初始北向（地球）纵向距离，指定为标量。

#### 依赖关系

此参数的方向指定取决于
**Reference frame orientation** 和
**Degrees of Freedom** 设置：

| Initial downrange | Reference frame orientation | Degrees of freedom |
| --- | --- | --- |
| North | [North East Down] | 6th Order (Coordinated Flight) |
| North | [North East Down] | 4th Order (Longitudinal) |
| East | [East North Up] | 6th Order (Coordinated Flight) |
| East | [East North Up] | 4th Order (Longitudinal) |

#### 编程使用

|  |
| --- |
| **模块参数**：`north` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Initial altitude** — 初始高度 `0`（默认）| 标量

质点模型的初始高度，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`altitude` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Initial airspeed** — 初始空速 `50`（默认）| 标量

质点模型的初始空速，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`'airspeed'` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'50'` |

### **Initial flight path angle** — 初始航迹角 `0`（默认）| 标量

质点模型的初始航迹角，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Initial heading angle** — 初始航向角 `0`（默认）| 标量

质点模型的初始航向角，指定为标量。

#### 依赖关系

要启用此参数，请将 **Degrees of Freedom**
设置为 `6th Order (Coordinated Flight)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`chi` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Mass** — 质点质量 `10`（默认）| 标量

质点模型的质量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'10'` |

## 所属库

Aerospace Blockset / Equations of Motion / Point Mass UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

在协调飞行中积分四阶或六阶质点运动方程

Fixed-Wing Point Mass 模块在协调飞行中积分四阶或六阶质点运动方程。
