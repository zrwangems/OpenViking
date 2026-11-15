---
type: simulink-block
title: '6DOF Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Equations of Motion / 6DOF'
documentation_page: '6dofacceleration'
documentation_source_path: '6dofacceleration.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF Acceleration

## 端口

### 输入

### **Vb** — 体坐标系中的速度三元素向量

体坐标系中的速度，指定为三元素向量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **ωb (rad/s)** — 体轴中的角速率三元素向量

体轴中的角速率，指定为三元素向量，以 radians per second 为单位。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，指定为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Simple Variable`。

**数据类型：** `double`

### **m** — 质量标量

质量，指定为标量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **Fxyz** — 施加的力三元素向量

施加的力，指定为三元素向量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量，采用在 **单位** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Simple Variable` 或 `Custom Variable`。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，质量以这些相对速度在体轴中增加至物体或从物体减少，指定为三元素向量，采用在 **单位** 中选择的单位。

#### 依赖关系

要启用此端口：

- 将 **质量类型** 设置为 `Simple Variable` 或 `Custom Variable`。
- 选择 **包含质量流相对速度**。

**数据类型：** `double`

### 输出

### **Abb** — 体轴中的加速度三元素向量

物体相对于体轴的加速度，使用体坐标系，返回为三元素向量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **Abe** — 相对于惯性系的加速度三元素向量

体轴中相对于惯性系（平坦地球）的加速度，返回为三元素向量。通常将此信号连接到加速度计，采用在 **单位** 中选择的单位。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **单位** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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

### **质量类型** — 质量类型 `Fixed`（默认） | `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 6DOF (Euler Angles) - 6DOF (Quaternion) |
| `Simple Variable` | 质量和惯性作为质量率的函数线性变化。 | - Simple Variable Mass 6DOF (Euler Angles) - Simple Variable Mass 6DOF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass 6DOF (Euler Angles) - Custom Variable Mass 6DOF (Quaternion) |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Fixed'` |

### **包含质量流相对速度** — 质量流相对速度端口 `off`（默认） | `on`

选中此复选框可添加质量流相对速度端口。这是质量增加或减少时的相对速度。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Simple Variable` 或 `Custom Variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `off` |

## 所属库

Aerospace Blockset / Equations of Motion / Acceleration

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

计算六自由度运动物体的加速度

6DOF Acceleration 模块计算物体在六自由度运动中相对于体坐标系和惯性（平坦地球）坐标系的加速度。仅将此模块用于以下 6DOF 运动方程模块：

- 6DOF (Euler Angles)
- 6DOF (Quaternion)
- Custom Variable Mass 6DOF (Euler Angles)
- Custom Variable Mass 6DOF (Quaternion)
- Simple Variable Mass 6DOF (Euler Angles)
- Simple Variable Mass 6DOF (Quaternion)

要为这些模块计算加速度：

- 选择 **输出用于加速度计算的质量属性**。
- 将相关联的 6DOF 运动方程模块的匹配输出端口信号馈入 6DOF Acceleration 的关联输入端口。

**提示**

匹配 6DOF Acceleration 和 6DOF 运动方程模块的所有参数值。
