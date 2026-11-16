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

俯仰姿态，在 ±pi 范围内，指定为标量，以 radians 为单位。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为 `Body`。

**数据类型：** `double`

### **γ** — 航迹角标量

航迹角，在 ±pi 范围内，指定为标量，以 radians 为单位。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为 `Wind`。

**数据类型：** `double`

### **q** — 俯仰角速率标量

俯仰角速率，指定为标量，以 radians per second 为单位。

**数据类型：** `double`

### **Vw** — 风固连坐标系中的速度二元素向量

机体速度分解到风固连坐标系，(*V, 0*)，返回为二元素向量，以 **Units** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为 `Wind`。

**数据类型：** `double`

### **U w** — 机体速度二元素向量

机体速度分解到体固连坐标系，(*u, w*)，指定为二元素向量，以 **Units** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为 `Body`。

**数据类型：** `double`

### **α** — 迎角标量

迎角，返回为标量，以 radians 为单位。

#### 依赖关系

要启用此端口，请将 **Axes** 设置为 `Wind`。

**数据类型：** `double`

### **g** — 重力标量

重力，指定为标量，以 **Units** 中选择的单位。

**数据类型：** `double`

### **Fuel** — 燃油箱状态标量

燃油箱状态，指定为：

- `1` — 油箱已满。
- `0` — 油箱既未满也未空。
- `-1` — 油箱为空。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **m** — 质量标量

质量，指定为标量，以 **Units** 中选择的单位。

**数据类型：** `double`

### **Fx** — 沿 *x* 轴施加的力标量

沿机体 *x* 轴施加的力，指定为标量，以 **Units** 中选择的单位。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力标量

沿机体 *z* 轴施加的力，指定为标量，以 **Units** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量，以 **Units** 中选择的单位。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable` 或 `Custom Variable`。
- 选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **I** — 惯性张量标量

惯性张量，指定为标量，以 **Units** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **Vre** — 相对速度二元素向量

质量在体固连轴中增加至机体或从机体减少的相对速度，指定为二元素向量，以 **Units** 中选择的单位。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable` 或 `Custom Variable`。
- 选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### 输出

### **AxbAzb** — 机体加速度二元素向量

机体相对于体固连坐标系的加速度，(*Ax, Az*)，返回为二元素向量，以 **Units** 中选择的单位。

**数据类型：** `double`

### **AxeAze** — 机体加速度二元素向量

机体相对于惯性（平地）坐标系的加速度，返回为二元素向量，以 **Units** 中选择的单位。通常将此信号连接到加速度计。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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
| **默认：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Fixed`（默认） | `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定。 | - 3DOF (Body Axes) - 3DOF (Wind Axes) |
| `Simple Variable` | 质量和惯性作为质量变化率的线性函数变化。 | - Simple Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Fixed'` |

### **Axes** — 机体轴或风轴 `Body`（默认） | `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** character vector |
| **值：** `Wind` | `Body` |
| **默认：** `Body` |

## 所属库

Aerospace Blockset / Equations of Motion / Acceleration

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

计算三自由度运动中的机体加速度

3DOF Acceleration 模块计算三自由度运动中机体相对于体固连坐标系和惯性（平地）坐标系的加速度。

要为运动方程模块计算加速度：

- 选择 **Output mass properties for acceleration computation**。
- 将关联的 3DOF 运动方程模块的匹配输出端口信号馈入 3DOF Acceleration 的关联输入端口。

**提示**

使 3DOF Acceleration 和 3DOF 运动方程模块的所有参数值匹配。
