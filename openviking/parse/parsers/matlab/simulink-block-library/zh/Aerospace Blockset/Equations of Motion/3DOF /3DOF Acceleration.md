---
type: simulink-block
title: '3DOF Acceleration'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofacceleration'
documentation_source_path: '3dofacceleration.html'
language: zh-CN
chinese_source: worker-translation
---

# 3DOF Acceleration

## 端口

### 输入

### **θ** — 俯仰姿态标量

俯仰姿态，在 ±pi 范围内，指定为标量，单位为弧度。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为
`Body`。

**数据类型：** `double`

### **γ** — 航迹角标量

航迹角，在 ±pi 范围内，指定为标量，单位为弧度。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为
`Wind`。

**数据类型：** `double`

### **q** — 俯仰角速率标量

俯仰角速率，指定为标量，单位为弧度每秒。

**数据类型：** `double`

### **Vw** — 风轴坐标系中的速度二元素向量

分解到风轴坐标系中的机体速度，(*V,
0*)，以二元素向量返回，单位由
**Units** 选择。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为
`Wind`。

**数据类型：** `double`

### **U w** — 机体速度二元素向量

分解到机体坐标系中的机体速度，(*u, w*)，
指定为二元素向量，单位由
**Units** 选择。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为
`Body`。

**数据类型：** `double`

### **α** — 迎角标量

迎角，以标量返回，单位为弧度。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为
`Wind`。

**数据类型：** `double`

### **g** — 重力标量

重力，指定为标量，单位由
**Units** 选择。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，指定为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple
Variable`。

**数据类型：** `double`

### **m** — 质量标量

质量，指定为标量，单位由 **Units** 选择。

**数据类型：** `double`

### **Fx** — 沿 *x* 轴施加的力标量

沿机体 *x* 轴施加的力，指定为标量，单位由
**Units** 选择。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力标量

沿机体 *z* 轴施加的力，指定为标量，单位由
**Units** 选择。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

质量变化率（累积为正，消融为负），指定为标量，单位由
**Units** 选择。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable` 或 `Custom Variable`。
- 选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **I** — 惯性张量标量

惯性张量，指定为标量，单位由
**Units** 选择。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom
Variable`。

**数据类型：** `double`

### **Vre** — 相对速度二元素向量

在机体坐标系中质量累积到机体或从机体消融的相对速度，
指定为二元素向量，单位由
**Units** 选择。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple
  Variable` 或 `Custom
  Variable`。
- 选择 **Include mass flow relative velocity**。

**数据类型：** `double`
### 输出

### **AxbAzb** — 机体加速度二元素向量

机体相对于机体坐标系的加速度，(*Ax,
Az*)，以二元素向量返回，单位由
**Units** 选择。

**数据类型：** `double`

### **AxeAze** — 机体加速度二元素向量

机体相对于惯性（平坦地球）坐标系的加速度，以二元素向量返回，单位由
**Units** 选择。通常将此信号连接到加速度计。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | 牛顿 | 牛顿-米 | 米每二次方秒 | 米每秒 | 米 | 千克 | 千克米平方 |
| `English (Velocity in ft/s)` | 磅 | 英尺-磅 | 英尺每二次方秒 | 英尺每秒 | 英尺 | 斯勒格 | 斯勒格英尺平方 |
| `English (Velocity in kts)` | 磅 | 英尺-磅 | 英尺每二次方秒 | 节 | 英尺 | 斯勒格 | 斯勒格英尺平方 |

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
| `Fixed` | 质量在整个仿真过程中恒定。 | - 3DOF (Body Axes) - 3DOF (Wind Axes) |
| `Simple Variable` | 质量和惯性随质量变化率线性变化。 | - Simple Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** 字符向量 |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Fixed'` |

### **Axes** — 机体轴或风轴 `Body`（默认）| `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** 字符向量 |
| **值：** `Wind` | `Body` |
| **默认：** `Body` |

## 所属库

Aerospace Blockset / Equations of Motion / Acceleration

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

计算三自由度运动中的机体加速度

3DOF Acceleration 模块计算三自由度运动中机体相对于机体坐标系和惯性（平坦地球）坐标系的加速度。

要为运动方程模块计算加速度：

- 选择 **Output mass properties for acceleration
  computation**。
- 将相关 3DOF 运动方程模块的匹配输出端口信号馈入 3DOF Acceleration 的相关输入端口。

**提示**

匹配 3DOF Acceleration 和 3DOF 运动方程模块的所有参数值。
