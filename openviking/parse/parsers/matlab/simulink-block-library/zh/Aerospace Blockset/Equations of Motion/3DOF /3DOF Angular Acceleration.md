---
type: simulink-block
title: '3DOF Angular Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofangularacceleration'
documentation_source_path: '3dofangularacceleration.html'
language: zh-CN
chinese_source: worker-translation
---

# 3DOF Angular Acceleration

## 端口

### 输入

### **q** — 俯仰角速率标量

俯仰角速率，指定为标量，单位为弧度每秒。

**数据类型：** `double`

### **I** — 惯性张量标量

惯性张量，指定为标量，单位由 **Units** 中选择的单位决定。

**数据类型：** `double`

### **dI/dt coeff** — 惯性张量矩阵系数变化率 3×3 矩阵

惯性张量矩阵系数变化率，指定为 3×3 矩阵，单位为 m2。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **M** — 施加的俯仰力矩标量

施加的俯仰力矩，指定为标量，单位由 **Units** 中选择的单位决定。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

质量变化率（累积为正，消融为负），指定为标量，单位由 **Units** 中选择的单位决定。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **dI/dt** — 惯性张量变化率标量

惯性张量变化率，*Iyy*，指定为标量，单位由 **Units** 中选择的单位决定。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`
### 输出

### **dq/dt** — 俯仰角加速度标量

俯仰角加速度，返回为标量，单位为弧度每二次方秒。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

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
| **类型：** 字符向量 |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body Axes) - 3DOF (Wind Axes) |
| `Simple Variable` | 质量和惯性随质量变化率线性变化。 | - Simple Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** 字符向量 |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Fixed'` |

## 所属库

Aerospace Blockset / Equations of Motion / Acceleration

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

计算三自由度运动中物体的俯仰角加速度或角加速度

3DOF Angular Acceleration 模块计算六自由度运动中物体相对于体固连坐标系和惯性（平坦地球）坐标系的俯仰角加速度或角加速度。

要为运动方程模块计算角加速度：

- 选择 **Output mass properties for acceleration computation**。
- 将关联的 3DOF 运动方程模块的匹配输出端口信号馈入 3DOF Angular Acceleration 的关联输入端口。

**提示**

匹配 3DOF Angular Acceleration 和 3DOF 运动方程模块的所有参数值。
