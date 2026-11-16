---
type: simulink-block
title: '3DOF (Body Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: '3dofbodyaxes'
documentation_source_path: '3dofbodyaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# 3DOF (Body Axes)

## 端口

### 输入

### **Fx** — 沿 *x* 轴施加的力（标量）

沿机体 *x* 轴施加的力，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力（标量）

沿机体 *z* 轴施加的力，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **M** — 施加的俯仰力矩（标量）

施加的俯仰力矩，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **g** — 重力（标量）

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **重力源** 设置为 `External`。

**数据类型：** `double`
### 输出

### **θ** — 俯仰姿态（标量）

俯仰姿态，在 ±pi 范围内，以 radians 为单位返回为标量。

**数据类型：** `double`

### **q** — 俯仰角速率（标量）

俯仰角速率，返回为标量，以 radians per second 为单位。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度（标量）

俯仰角加速度，返回为标量，以 radians per second squared 为单位。

**数据类型：** `double`

### **XeZe** — 机体位置二元素向量

机体在平坦地球参考系中的位置，(*Xe, Ze*)，返回为二元素向量。

**数据类型：** `double`

### **U w** — 机体速度二元素向量

机体速度在机体固定坐标系中分解，(*u, w*)，返回为二元素向量。

**数据类型：** `double`

### **AxbAzb** — 机体加速度二元素向量

机体相对于机体固定坐标系的加速度，(*Ax, Az*)，返回为二元素向量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **AxeAze** — 机体加速度二元素向量

机体相对于惯性（平坦地球）坐标系的加速度，返回为二元素向量。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **包括惯性加速度** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

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

### **坐标轴** — 机体轴或风轴 `Body`（默认）| `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** character vector |
| **值：** `Wind` | `Body` |
| **默认：** `Body` |

### **质量类型** — 质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 说明 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯性随质量变化率线性变化。 | - Simple Variable Mass   3DOF (Body Axes) - Simple Variable Mass   3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   3DOF (Body Axes) - Custom Variable Mass   3DOF (Wind Axes) |

`Fixed` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Fixed'` |

### **初始速度** — 机体的初始速度 `100`（默认）| 标量

机体的初始速度，(*V*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `v_ini` |
| **类型：** character vector |
| **值：** `'100'` | 标量 |
| **默认：** `'100'` |

### **初始机体姿态** — 初始俯仰姿态 `0`（默认）| 标量

机体的初始俯仰姿态，(*θ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始机体旋转速率** — 初始俯仰旋转速率 `0`（默认）| 标量

初始俯仰旋转速率，(*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始迎角** — 初始角度 `0`（默认）| 标量

速度矢量与机体之间的初始角度，(*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始位置 (x,z)** — 初始位置 `[0 0]`（默认）| 二元素向量

机体在平坦地球参考系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** character vector |
| **值：** `'[0 0]'` | 二元素向量 |
| **默认：** `'[0 0]'` |

### **初始质量** — 初始质量 `1.0`（默认）| 标量

刚体的初始质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** character vector |
| **值：** `'1.0'` | 标量 |
| **默认：** `'1.0'` |

### **惯性** — 惯性 `1.0`（默认）| 标量

机体的惯性，指定为标量。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy` |
| **类型：** character vector |
| **值：** `'1.0'` | 标量 |
| **默认：** `'1.0'` |

### **重力源** — 重力源 `Internal`（默认）| `External`

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
| **默认：** `'Internal'` |

### **重力加速度** — 重力源 `9.81`（默认）| 标量

重力加速度，指定为 double 标量，并在选择内部重力源时使用。如果要在仿真中忽略重力，可将此值设置为 `0`。

#### 依赖关系

- 要启用此参数，请将 **重力源** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** character vector |
| **值：** `'9.81'` | 标量 |
| **默认：** `'9.81'` |

### **包括惯性加速度** — 包括惯性加速度端口 `off`（默认）| `on`

选中此复选框可添加平坦地球坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 名称数量必须与状态数量匹配（如各项所示），或者为空。请设置所有模块状态或都不设置。
- 要为单变量状态分配名称，请在引号之间输入唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array of character vectors 或 string。

### **Velocity: e.g., {'u, 'w'}** — 速度状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vel_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **Pitch angular rate e.g., 'q'** — 俯仰角速率状态名称 `''`（默认）

俯仰角速率状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认：** `''` |

### **Pitch attitude: e.g., 'theta'** — 俯仰姿态状态名称 `''`（默认）

俯仰姿态状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_statename` |
| **类型：** character vector | string |
| **值：** `''` |
| **默认：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b: 3DOF (Body Axes) 模块更改

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型可继续运行。如果将 3DOF 运动方程模块的 R2021b 之前版本替换为 R2021b 或更高版本，则更新后的模型可能更容易出现代数环。有关如何使用单位延迟移除代数环的示例，请参阅移除代数环。有关代数环的更多信息，请参阅识别模型中的代数环。

## 描述

实现相对于机体轴的三自由度运动方程

3DOF (Body Axes) 模块实现相对于机体轴的三自由度运动方程。它考虑机体固定坐标系在垂直平面内绕平坦地球参考系的旋转。有关旋转和运动方程的详细信息，请参阅算法。
