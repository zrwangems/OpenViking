---
type: simulink-block
title: 'Custom Variable Mass 3DOF (Wind Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: 'customvariablemass3dofwindaxes'
documentation_source_path: 'customvariablemass3dofwindaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Variable Mass 3DOF (Wind Axes)

## 端口

### 输入

### **Fx** — 沿风 *x* 轴的施加力 标量

沿风 *x* 轴的施加力，指定为标量，单位在 **Units** 中选择。

**Data Types:** `double`

### **Fz** — 沿风 *z* 轴的施加力 标量

沿风 *z* 轴的施加力，指定为标量。

**Data Types:** `double`

### **M** — 施加的俯仰力矩 标量

施加的俯仰力矩，指定为标量，单位在 **Units** 中选择。

**Data Types:** `double`

### **dm/dt** — 质量变化率 标量

质量变化率（若吸积则为正，若烧蚀则为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**Data Types:** `double`

### **m** — 质量 标量

质量，指定为标量，单位在 **Units** 中选择。

**Data Types:** `double`

### **dI/dt** — 惯量张量变化率 标量

惯量张量 *Iyy* 的变化率，指定为标量，单位在 **Units** 中选择。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**Data Types:** `double`

### **I** — 惯量张量 标量

惯量张量，指定为标量，单位在 **Units** 中选择。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**Data Types:** `double`

### **g** — 重力 标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **Gravity source** 设置为 `External`。

**Data Types:** `double`

### **Vre** — 相对速度 二元素向量

质量吸积到机体或从机体烧蚀时的相对速度，在体固轴中，指定为二元素向量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**Data Types:** `double`

### 输出

### **γ** — 飞行路径角 标量

飞行路径角，在 ±pi 内，返回为标量，单位为 radians。

**Data Types:** `double`

### **q** — 俯仰角速度 标量

俯仰角速度，返回为标量，单位为 radians per second。

**Data Types:** `double`

### **dq/dt** — 俯仰角加速度 标量

俯仰角加速度，返回为标量，单位为 radians per second squared。

**Data Types:** `double`

### **XeZe** — 机体位置 二元素向量

机体在平地参考系中的位置，(*Xe, Ze*)，返回为二元素向量。

**Data Types:** `double`

### **Vw** — 风固坐标系中的速度 二元素向量

机体速度在风固坐标系中分解为 (*V, 0*)，返回为二元素向量。

**Data Types:** `double`

### **AxbAzb** — 机体加速度 二元素向量

机体相对于体固坐标系的加速度，(*Ax, Az*)，返回为二元素向量，单位在 **Units** 中选择。

**Data Types:** `double`

### **α** — 迎角 标量

迎角，返回为标量，单位为 radians。

**Data Types:** `double`

### **AxeAze** — 机体加速度 二元素向量

机体相对于惯性（平地）坐标系的加速度，返回为二元素向量。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选择 **Include inertial acceleration** 复选框。

**Data Types:** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| Units | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 程序化使用

|  |
| --- |
| **模块参数:** `units` |
| **类型:** character vector |
| **值:** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值:** `Metric (MKS)` |

### **Axes** — 体轴或风轴 `Wind`（默认）| `Body`

体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数:** `axes` |
| **类型:** character vector |
| **值:** `Wind` | `Body` |
| **默认值:** `Wind` |

### **Mass type** — 质量类型 `Custom Variable`（默认）| `Simple Variable` | `Fixed`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body Axes) - 3DOF (Wind Axes) |
| `Simple Variable` | 质量和惯量随质量变化率线性变化。 | - Simple Variable Mass 3DOF (Body Axes) - Simple Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯量变化可自定义。 | - Custom Variable Mass 3DOF (Body Axes) - Custom Variable Mass 3DOF (Wind Axes) |

选择 `Custom Variable` 符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数:** `mtype` |
| **类型:** character vector |
| **值:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值:** `'Custom Variable'` |

### **Initial airspeed** — 初始速度 `100`（默认）| 标量

机体的初始速度，(*V*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `V_ini` |
| **类型:** character vector |
| **值:** `'100'` | scalar |
| **默认值:** `'100'` |

### **Initial flight path angle** — 初始飞行路径角 `0`（默认）| 标量

机体的初始飞行路径角，(*γ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `gamma_ini` |
| **类型:** character vector |
| **值:** `'0'` | scalar |
| **默认值:** `'0'` |

### **Initial body rotation rate** — 初始俯仰旋转速率 `0`（默认）| 标量

初始俯仰旋转速率，(*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `q_ini` |
| **类型:** character vector |
| **值:** `'0'` | scalar |
| **默认值:** `'0'` |

### **Initial incidence** — 初始角度 `0`（默认）| 标量

速度矢量与机体之间的初始角度，(*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `alpha_ini` |
| **类型:** character vector |
| **值:** `'0'` | scalar |
| **默认值:** `'0'` |

### **Initial position (x,z)** — 初始位置 `[0 0]`（默认）| 二元素向量

机体在平地参考系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `pos_ini` |
| **类型:** character vector |
| **值:** `'[0 0]'` | two-element vector |
| **默认值:** `'[0 0]'` |

### **Gravity Source** — 重力源 `Internal`（默认）| `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 模块的可变重力输入 |
| `Internal` | 在 mask 中指定的恒定重力 |

#### 程序化使用

|  |
| --- |
| **模块参数:** `g_in` |
| **类型:** character vector |
| **值:** `'Internal'` | `'External'` |
| **默认值:** `'Internal'` |

### **Acceleration due to gravity** — 重力源 `9.81`（默认）| 标量

重力加速度，指定为 double 标量，并在选择内部重力源时使用。如果仿真中要忽略重力，可将此值设为 `0`。

#### 依赖关系

- 要启用此参数，请将 **Gravity Source** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数:** `g` |
| **类型:** character vector |
| **值:** `'9.81'` | scalar |
| **默认值:** `'9.81'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认）| `on`

选中此复选框可添加质量流相对速度端口。这是质量吸积或烧蚀时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数:** `vre_flag` |
| **类型:** character vector |
| **值:** `off` | `on` |
| **默认值:** `'off'` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认）| `on`

选中此复选框可添加平地参考系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数:** `abi_flag` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入由花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空 (`' '`)，则不分配名称。
- 状态名称仅应用于具有该名称参数的所选模块。
- 状态数必须能被状态名称数整除。
- 可以指定的名称数少于状态数，但不能多于状态数。

  例如，在具有四个状态的系统中可以指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **Velocity: e.g., 'V'** — 速度状态名称 `''`（默认）| character vector

速度状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数:** `V_statename` |
| **类型:** character vector | string |
| **值:** `''` | scalar |
| **默认值:** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认）| 由花括号括起来的逗号分隔列表

位置状态名称，指定为逗号分隔列表，并由花括号括起来。

#### 程序化使用

|  |
| --- |
| **模块参数:** `pos_statename` |
| **类型:** character vector |
| **值:** `''` | comma-separated list surrounded by braces |
| **默认值:** `''` |

### **Body rotation rate: e.g., 'q'** — 机体旋转状态名称 `''`（默认）| 标量

机体旋转速率状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数:** `q_statename` |
| **类型:** character vector | string |
| **值:** `''` | scalar |
| **默认值:** `''` |

### **Flight path angle: e.g., 'gamma'** — 飞行路径角状态名称 `''`（默认）

飞行路径角状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数:** `gamma_statename` |
| **类型:** character vector | string |
| **值:** `''` | scalar |
| **默认值:** `''` |

### **Incidence angle e.g., 'alpha'** — 迎角状态名称 `''`（默认）| 标量

迎角状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数:** `alpha_statename` |
| **类型:** character vector | string |
| **值:** `''` | scalar |
| **默认值:** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b: Custom Variable Mass 3DOF (Wind Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型将继续运行。如果将 3DOF 运动方程模块的 pre-R2021b 版本替换为 R2021b 或更高版本，则更新后的模型可能更容易出现代数环。有关如何使用单位延迟移除代数环的示例，请参阅 Remove Algebraic Loops。有关代数环的更多信息，请参阅 Identify Algebraic Loops in Your Model。

## 描述

实现相对于风轴的自定义变质量三自由度运动方程

Custom Variable Mass 3DOF (Wind Axes) 模块实现相对于风轴的自定义变质量三自由度运动方程。它考虑风固坐标系在垂直平面内绕平地参考系的旋转。有关旋转和运动方程的更多信息，请参阅 Algorithms。
