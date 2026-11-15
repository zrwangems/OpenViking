---
type: simulink-block
title: '6DOF Angular Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Equations of Motion / 6DOF'
documentation_page: '6dofangularacceleration'
documentation_source_path: '6dofangularacceleration.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF Angular Acceleration

## 端口

### 输入

### **ωb (rad/s)** — 机体固定轴中的角速率三元素向量

机体固定轴中的角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3×3 矩阵

惯性张量矩阵，指定为 3×3 矩阵，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **dI/dt coeff** — 惯性张量矩阵系数的变化率 3×3 矩阵

惯性张量矩阵系数的变化率，指定为 3×3 矩阵。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Simple Variable`，in m2.

**数据类型：** `double`

### **Mxyz** — 施加的力矩三元素向量

施加的力矩，指定为三元素向量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵的变化率 3×3 矩阵

惯性张量矩阵的变化率，指定为 3×3 矩阵，采用在 **单位** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（积聚为正，烧蚀为负），指定为标量，采用在 **单位** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Simple Variable`。

**数据类型：** `double`
### 输出

### **dωb/dt** — 角加速度三元素向量

机体固定轴中的角加速度，返回为三元素向量，单位为 radians per second squared。

**数据类型：** `double`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **质量类型** — 质量类型 `Fixed` (默认) | `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 6DOF (Euler Angles) - 6DOF (Quaternion) |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 | - Simple Variable Mass 6DOF (Euler Angles) - Simple Variable Mass 6DOF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass 6DOF (Euler Angles) - Custom Variable Mass 6DOF (Quaternion) |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Fixed'` |

## 所属库

Aerospace Blockset / Equations of Motion / Acceleration

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

计算六自由度运动刚体的角加速度

6DOF Angular Acceleration 计算六自由度运动刚体的角加速度。此模块仅用于以下 6DOF 运动方程模块：

- 6DOF (Euler Angles)
- 6DOF (Quaternion)
- Custom Variable Mass 6DOF (Euler Angles)
- Custom Variable Mass 6DOF (Quaternion)
- Simple Variable Mass 6DOF (Euler Angles)
- Simple Variable Mass 6DOF (Quaternion)

要为这些模块计算角加速度：

- 选择 **输出用于加速度计算的质量属性**。
- 将关联的 6DOF 运动方程模块的匹配输出端口信号馈入 6DOF Angular Acceleration 的关联输入端口。

**提示**

匹配 6DOF Angular Acceleration 和 6DOF 运动方程模块的所有参数值。
