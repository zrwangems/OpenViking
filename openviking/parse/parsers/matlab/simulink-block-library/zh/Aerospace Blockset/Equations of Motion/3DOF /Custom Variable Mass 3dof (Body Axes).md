---
type: simulink-block
title: 'Custom Variable Mass 3DOF (Body Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: 'customvariablemass3dofbodyaxes'
documentation_source_path: 'customvariablemass3dofbodyaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Variable Mass 3DOF (Body Axes)

## 端口

### 输入

### **Fx** — 沿 *x* 轴施加的力，标量

沿机体 *x* 轴施加的力，指定为标量，单位采用 **Units** 中选择的单位。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力，标量

沿机体 *z* 轴施加的力，指定为标量，单位采用 **Units** 中选择的单位。

**数据类型：** `double`

### **M** — 施加的俯仰力矩，标量

施加的俯仰力矩，指定为标量，单位采用 **Units** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率，标量

质量变化率（如果积聚则为正，如果烧蚀则为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **m** — 质量，标量

质量，指定为标量，单位采用 **Units** 中选择的单位。

**数据类型：** `double`

### **dI/dt** — 惯性张量变化率，标量

惯性张量 *Iyy* 的变化率，指定为标量，单位采用 **Units** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **I** — 惯性张量，标量

惯性张量，指定为标量，单位采用 **Units** 中选择的单位。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **g** — 重力，标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **Gravity source** 设置为 `External`。

**数据类型：** `double`

### **Vre** — 相对速度，二元素向量

质量在机体固定坐标系中积聚到机体或从机体烧蚀时的相对速度，指定为二元素向量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### 输出

### **θ** — 俯仰姿态，标量

俯仰姿态，在 ±pi 范围内，以标量形式返回，单位为 radians（*θ*）。

**数据类型：** `double`

### **q** — 俯仰角速率，标量

俯仰角速率，以标量形式返回，单位为 radians per second。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度，标量

俯仰角加速度，以标量形式返回，单位为 radians per second squared。

**数据类型：** `double`

### **XeZe** — 物体的位置，二元素向量

物体在平面地球参考系中的位置（*Xe, Ze*），以二元素向量形式返回。

**数据类型：** `double`

### **U w** — 物体的速度，二元素向量

分解到机体固定坐标系的物体速度（*u, w*），以二元素向量形式返回。

**数据类型：** `double`

### **AxbAzb** — 物体的加速度，二元素向量

物体相对于机体固定坐标系的加速度（*Ax, Az*），以二元素向量形式返回，单位采用 **Units** 中选择的单位。

**数据类型：** `double`

### **AxeAze** — 物体的加速度，二元素向量

物体相对于惯性（平面地球）坐标系的加速度，以二元素向量形式返回。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **Include inertial acceleration** 复选框。

**数据类型：** `double`

## 参数

### 主要

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
| **默认值：** `Metric (MKS)` |

### **Axes** — 机体轴或风轴 `Body`（默认） | `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** character vector |
| **值：** `Wind` | `Body` |
| **默认值：** `Body` |

### **Mass type** — 质量类型 `Custom Variable`（默认） | `Fixed` | `Simple Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯性随质量速率线性变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Custom Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Custom Variable'` |

### **Initial velocity** — 物体的初始速度 `100`（默认） | 标量

物体的初始速度（*V*0），指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `v_ini` |
| **类型：** character vector |
| **值：** `'100'` | 标量 |
| **默认值：** `'100'` |

### **Initial body attitude** — 初始俯仰姿态 `0`（默认） | 标量

物体的初始俯仰姿态（*θ*0），指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial body rotation rate** — 初始俯仰旋转速率 `0`（默认） | 标量

初始俯仰旋转速率（*q*0），指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial incidence** — 初始角度 `0`（默认） | 标量

速度矢量与机体之间的初始角度（*α*0），指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认值：** `'0'` |

### **Initial position (x,z)** — 初始位置 `[0 0]`（默认） | 二元素向量

物体在平面地球参考系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** character vector |
| **值：** `'[0 0]'` | 二元素向量 |
| **默认值：** `'[0 0]'` |

### **Gravity Source** — 重力源 `Internal`（默认） | `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 到模块的可变重力输入 |
| `Internal` | 在封装中指定的常量重力 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `g_in` |
| **类型：** character vector |
| **值：** `'Internal'` | `'External'` |
| **默认值：** `'Internal'` |

### **Acceleration due to gravity** — 重力源 `9.81`（默认） | 标量

重力加速度，指定为 double 标量，并在选择内部重力源时使用。如果仿真中要忽略重力，可将此值设置为 `0`。

#### 依赖关系

- 要启用此参数，请将 **Gravity Source** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** character vector |
| **值：** `'9.81'` | 标量 |
| **默认值：** `'9.81'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认） | `on`

选中此复选框可添加质量流相对速度端口。这是质量被积聚或烧蚀时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `'off'` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认） | `on`

选中此复选框可添加平面地球参考系中的惯性加速度输出端口。通常将此信号连接到加速度计。

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

为每个状态分配唯一名称。在线性化过程中，可以使用状态名称代替模块路径。

- 名称数必须与状态数匹配（如每个项所示），或者为空。请设置所有模块状态或不设置任何模块状态。
- 要为单变量状态分配名称，请在引号之间输入唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array of character vectors 或 string。

### **Velocity: e.g., {'u, 'w'}** — 速度状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vel_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Pitch angular rate e.g., 'q'** — 俯仰角速率状态名称 `''`（默认）

俯仰角速率状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **Pitch attitude: e.g., 'theta'** — 俯仰姿态状态名称 `''`（默认）

俯仰姿态状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_statename` |
| **类型：** character vector | string |
| **值：** `''` |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b：Custom Variable Mass 3DOF (Body Axes) 模块更改

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型将继续运行。如果将 3DOF 运动方程模块的 R2021b 之前版本替换为 R2021b 或更高版本，则更新后的模型可能更容易出现代数环。有关如何使用单位延迟移除代数环的示例，请参阅移除代数环。有关代数环的更多信息，请参阅识别模型中的代数环。

## 描述

实现相对于机体轴系的自定义变质量三自由度运动方程

Custom Variable Mass 3DOF (Body Axes) 模块实现相对于机体轴系的自定义变质量三自由度运动方程。它考虑机体固定坐标系在垂直平面内绕平面地球参考系的旋转。有关旋转和运动方程的更多信息，请参阅算法。
