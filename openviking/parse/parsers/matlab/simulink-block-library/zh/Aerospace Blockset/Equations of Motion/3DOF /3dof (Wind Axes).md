---
type: simulink-block
title: '3DOF (Wind Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofwindaxes'
documentation_source_path: '3dofwindaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# 3DOF (Wind Axes)

## 端口

### 输入

### **Fx** — 沿风轴 *x* 方向施加的力 标量

沿风轴 *x* 方向施加的力，指定为标量，单位由 **Units** 选择。

**数据类型：** `double`

### **Fz** — 沿风轴 *z* 方向施加的力 标量

沿风轴 *z* 方向施加的力，指定为标量。

**数据类型：** `double`

### **M** — 施加的俯仰力矩 标量

施加的俯仰力矩，指定为标量，单位由 **Units** 选择。

**数据类型：** `double`

### **g** — 重力 标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **Gravity source** 设置为 `External`。

**数据类型：** `double`
### 输出

### **γ** — 航迹角 标量

航迹角，在 ±pi 范围内，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **q** — 俯仰角速率 标量

俯仰角速率，以标量形式返回，单位为弧度每秒。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度 标量

俯仰角加速度，以标量形式返回，单位为弧度每二次方秒。

**数据类型：** `double`

### **XeZe** — 刚体位置 二元向量

刚体在平面地球参考坐标系中的位置，(*Xe, Ze*)，以二元向量形式返回。

**数据类型：** `double`

### **Vw** — 风固定坐标系中的速度 二元向量

刚体速度在风固定坐标系中的分量，(*V, 0*)，以二元向量形式返回。

**数据类型：** `double`

### **AxbAzb** — 刚体加速度 二元向量

刚体相对于体固定坐标系的加速度，(*Ax, Az*)，以二元向量形式返回，单位由 **Units** 选择。

**数据类型：** `double`

### **α** — 迎角 标量

迎角，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **AxeAze** — 刚体加速度 二元向量

刚体相对于惯性（平面地球）坐标系的加速度，以二元向量形式返回。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **Include inertial acceleration** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯量 |
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
| **默认值：** `Metric (MKS)` |

### **Axes** — 体轴或风轴 `Wind`（默认）| `Body`

体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** 字符向量 |
| **值：** `Wind` | `Body` |
| **默认值：** `Wind` |

### **Mass type** — 质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯量随质量速率线性变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯量变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Fixed` 选项符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** 字符向量 |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Fixed'` |

### **Initial airspeed** — 初始速度 `100`（默认）| 大于 `0` 的标量

刚体的初始速度，(*V*0)，指定为大于 `0` 的标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `V_ini` |
| **类型：** 字符向量 |
| **值：** `'100'` | 标量 |
| **默认值：** `'100'` |

### **Initial flight path angle** — 初始航迹角 `0`（默认）| 标量

刚体的初始航迹角，(*γ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gamma_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial body rotation rate** — 初始俯仰角速率 `0`（默认）| 标量

初始俯仰角速率，(*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial incidence** — 初始角度 `0`（默认）| 标量

速度矢量与刚体之间的初始角度，(*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial position (x,z)** — 初始位置 `[0 0]`（默认）| 二元向量

刚体在平面地球参考坐标系中的初始位置，指定为二元向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** 字符向量 |
| **值：** `'[0 0]'` | 二元向量 |
| **默认值：** `'[0 0]'` |

### **Initial mass** — 初始质量 `1.0`（默认）| 标量

刚体的初始质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** 字符向量 |
| **值：** `'1.0'` | 标量 |
| **默认值：** `'1.0'` |

### **Inertia body axes** — 刚体惯量 `1.0`（默认）| 标量

刚体的惯量，指定为标量。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy` |
| **类型：** 字符向量 |
| **值：** `'1.0'` | 标量 |
| **默认值：** `'1.0'` |

### **Gravity Source** — 重力源 `Internal`（默认）| `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 可变重力输入到模块 |
| `Internal` | 在掩码中指定的恒定重力 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `g_in` |
| **类型：** 字符向量 |
| **值：** `'Internal'` | `'External'` |
| **默认值：** `'Internal'` |

### **Acceleration due to gravity** — 重力源 `9.81`（默认）| 标量

重力加速度，指定为双精度标量，在选择内部重力源时使用。如果仿真中忽略重力，可将此值设置为 `0`。

#### 依赖关系

- 要启用此参数，请将 **Gravity Source** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** 字符向量 |
| **值：** `'9.81'` | 标量 |
| **默认值：** `'9.81'` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认）| `on`

选中此复选框以添加平面地球坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 名称数量必须与状态数量匹配（如各项所示），或为空。请全部设置或全部不设置模块状态。
- 要为单变量状态分配名称，请在引号内输入唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符向量元胞数组或字符串。

### **Velocity: e.g., 'V'** — 速度状态名称 `''`（默认）| 字符向量

速度状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `V_statename` |
| **类型：** 字符向量 | 字符串 |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** 字符向量 |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Body rotation rate: e.g., 'q'** — 体旋转状态名称 `''`（默认）| 标量

体旋转角速率状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** 字符向量 | 字符串 |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **Flight path angle: e.g., 'gamma'** — 航迹角状态名称 `''`（默认）

航迹角状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gamma_statename` |
| **类型：** 字符向量 | 字符串 |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **Incidence angle e.g., 'alpha'** — 迎角状态名称 `''`（默认）| 标量

迎角状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_statename` |
| **类型：** 字符向量 | 字符串 |
| **值：** `''` | 标量 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b：3DOF (Wind Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型将继续运行。如果将 R2021b 之前的 3DOF 运动方程模块版本替换为 R2021b 或更高版本，更新后的模型可能更容易出现代数环。有关如何使用单位延迟消除代数环的示例，请参阅 Remove Algebraic Loops。有关代数环的更多信息，请参阅 Identify Algebraic Loops in Your Model。

## 描述

实现相对于风轴的三自由度运动方程

3DOF (Wind Axes) 模块实现相对于风轴的三自由度运动方程。它考虑风固定坐标系在平面地球参考坐标系垂直平面内的旋转。有关旋转和运动方程的更多信息，请参阅 Algorithms。
