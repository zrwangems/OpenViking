---
type: simulink-block
title: 'Simple Variable Mass 3DOF (Wind Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 3DOF'
documentation_page: 'simplevariablemass3dofwindaxes'
documentation_source_path: 'simplevariablemass3dofwindaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 3DOF (Wind Axes)

## 端口

### 输入

### **Fx** — 沿风轴 *x* 轴施加的力标量

沿风轴 *x* 轴施加的力，指定为标量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **Fz** — 沿风轴 *z* 轴施加的力标量

沿风轴 *z* 轴施加的力，指定为标量。

**数据类型：** `double`

### **M** — 施加的俯仰力矩标量

施加的俯仰力矩，指定为标量，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **包括质量流相对速度**。

**数据类型：** `double`

### **g** — 重力标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **重力源** 设置为 `External`。

**数据类型：** `double`

### **Vre** — 相对速度二元素向量

在体固定轴中质量被添加至物体或从物体剥离时的相对速度，指定为二元素向量。

#### 依赖关系

要启用此端口，请选择 **包括质量流相对速度**。

**数据类型：** `double`
### 输出

### **γ** — 航迹角标量

航迹角，在 ±pi 范围内，以标量形式返回，单位为 radians。

**数据类型：** `double`

### **q** — 俯仰角速率标量

俯仰角速率，以标量形式返回，单位为 radians per second。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度标量

俯仰角加速度，以标量形式返回，单位为 radians per second squared。

**数据类型：** `double`

### **XeZe** — 物体的位置二元素向量

物体在平地参考坐标系中的位置 (*Xe, Ze*)，以二元素向量形式返回。

**数据类型：** `double`

### **Vw** — 风固定坐标系中的速度二元素向量

分解到风固定坐标系的物体速度 (*V, 0*)，以二元素向量形式返回。

**数据类型：** `double`

### **AxbAzb** — 物体的加速度二元素向量

物体相对于体固定坐标系的加速度 (*Ax, Az*)，以二元素向量形式返回，采用在 **单位** 中选择的单位。

**数据类型：** `double`

### **α** — 迎角标量

迎角，以标量形式返回，单位为 radians。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Simple Variable`。

**数据类型：** `double`

### **AxeAze** — 物体的加速度二元素向量

物体相对于惯性（平地）坐标系的加速度，以二元素向量形式返回。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **包括惯性加速度** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **坐标轴** — 机体轴或风轴 `Wind` (默认) | `Body`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** character vector |
| **值：** `Wind` | `Body` |
| **默认值：** `Wind` |

### **质量类型** — 质量类型 `Simple Variable` (默认) | `Fixed` | `Custom Variable`

质量类型，按下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯量随质量流率线性变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯量变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Simple Variable` 选择符合算法中描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Simple Variable'` |

### **初始空速** — 初始速度 `100` (默认) | 标量

物体的初始速度 (*V*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `V_ini` |
| **类型：** character vector |
| **值：** `'100'` | 标量 |
| **默认值：** `'100'` |

### **初始航迹角** — 初始航迹角 `0` (默认) | 标量

物体的初始航迹角 (*γ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gamma_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **初始机体旋转速率** — 初始俯仰旋转速率 `0` (默认) | 标量

初始俯仰旋转速率 (*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **初始入射角** — 初始角度 `0` (默认) | 标量

速度向量与物体之间的初始角度 (*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **初始位置 (x,z)** — 初始位置 `[0 0]` (默认) | 二元素向量

物体在平地参考坐标系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** character vector |
| **值：** `'[0 0]'` | 二元素向量 |
| **默认值：** `'[0 0]'` |

### **初始质量** — 初始质量 `1.0` (默认) | 标量

刚体的初始质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** character vector |
| **值：** `'1.0'` | 标量 |
| **默认值：** `'1.0'` |

### **空载质量** — 燃料箱为空时物体的质量 `0.5` (默认) | 标量

燃料箱为空时物体的质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** `'0.5'` | 标量 |
| **默认值：** `'0.5'` |

### **满载质量** — 燃料箱为满时物体的质量 `3.0` (默认) | 标量

燃料箱为满时物体的质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** `'3.0'` | 标量 |
| **默认值：** `'3.0'` |

### **机体轴空载惯量** — 燃料箱为空时物体的惯量 `0.5` (默认) | 标量

燃料箱为空时物体的惯量，指定为标量。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Simple Variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy_e` |
| **类型：** character vector |
| **值：** `'1.0'` | 标量 |
| **默认值：** `'1.0'` |

### **机体轴满载惯量** — 燃料箱为满时物体的惯量 `3.0` (默认) | 标量

燃料箱为满时物体的惯量，指定为标量。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Simple Variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy_f` |
| **类型：** character vector |
| **值：** `'3.0'` | 标量 |
| **默认值：** `'3.0'` |

### **重力源** — 重力源 `Internal` (默认) | `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 到模块的可变重力输入 |
| `Internal` | 在封装中指定的恒定重力 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `g_in` |
| **类型：** character vector |
| **值：** `'Internal'` | `'External'` |
| **默认值：** `'Internal'` |

### **重力加速度** — 重力源 `9.81` (默认) | 标量

重力加速度，指定为 double 标量，并在选择内部重力源时使用。如果要在仿真中忽略重力，可将此值设置为 `0`。

#### 依赖关系

- 要启用此参数，请将 **重力源** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** character vector |
| **值：** `'9.81'` | 标量 |
| **默认值：** `'9.81'` |

### **包括质量流相对速度** — 质量流相对速度端口 `off` (默认) | `on`

选中此复选框可添加质量流相对速度端口。这是质量被添加或剥离时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `'off'` |

### **当质量为空或满时限制质量流** — 限制质量流 `on` (默认) | `off`

当以下情况之一为真时，选中此复选框以限制输入质量流率：

- 燃料箱已满且输入质量流率为正。
- 燃料箱为空且输入质量流率为负。

当输入质量流率可能导致质量超出其限制时，模块在运动方程中使用零质量流率值。有关详细信息，请参阅算法。

如果不希望限制输入质量流率，请清除此复选框。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Simple Variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mdot_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

**数据类型：** `double`

### **包括惯性加速度** — 包括惯性加速度端口 `off` (默认) | `on`

选中此复选框可添加平地参考坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 名称数必须与每个项所示的状态数匹配，或者为空。设置模块的所有状态或都不设置。
- 要为单变量状态分配名称，请在引号之间输入唯一名称，例如 `'q'` 或 `"q"`。
- 要为二变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array of character vectors 或 string。

### **速度：例如，'V'** — 速度状态名称 `''` (默认) | character vector

速度状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `V_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **位置：例如，{'Xe', 'Ze'}** — 位置状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **机体旋转速率：例如，'q'** — 机体旋转状态名称 `''` (默认) | 标量

机体旋转速率状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **航迹角：例如，'gamma'** — 航迹角状态名称 `''` (默认)

航迹角状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gamma_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **入射角 例如，'alpha'** — 入射角状态名称 `''` (默认) | 标量

入射角状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''` (默认) | 标量

质量状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b：Simple Variable Mass 3DOF (Wind Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型可继续运行。如果将 R2021b 之前的 3DOF 运动方程模块版本替换为 R2021b 或更高版本，则更新后的模型可能更容易出现代数环。有关如何使用单位延迟移除代数环的示例，请参阅移除代数环。有关代数环的详细信息，请参阅在模型中识别代数环。

## 描述

实现相对于风轴系的简单变质量三自由度运动方程

Simple Variable Mass 3DOF (Wind Axes) 模块实现相对于风轴系的简单变质量三自由度运动方程。该模块考虑风固定坐标系在垂直平面内绕平地参考坐标系的旋转。有关旋转和运动方程的详细信息，请参阅算法。
