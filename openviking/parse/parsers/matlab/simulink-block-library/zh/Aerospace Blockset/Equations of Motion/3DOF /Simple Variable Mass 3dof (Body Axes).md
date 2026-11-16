---
type: simulink-block
title: 'Simple Variable Mass 3DOF (Body Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: 'simplevariablemass3dofbodyaxes'
documentation_source_path: 'simplevariablemass3dofbodyaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 3DOF (Body Axes)

## 端口

### 输入

### **Fx** — 沿 *x* 轴施加的力，标量

沿机体 *x* 轴施加的力，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力，标量

沿机体 *z* 轴施加的力，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **M** — 施加的俯仰力矩，标量

施加的俯仰力矩，指定为标量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率，标量

质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量。

#### 依赖项

要启用此端口，请选择 **包含质量流相对速度**。

**数据类型：** `double`

### **g** — 重力，标量

重力，指定为标量。

#### 依赖项

要启用此端口，请将 **重力源** 设置为 `External`。

**数据类型：** `double`

### **Vre** — 相对速度，二元素向量

在机体固定轴中，质量增加至机体或从机体减少时的相对速度，指定为二元素向量。

#### 依赖项

要启用此端口，请选择 **包含质量流相对速度**。

**数据类型：** `double`
### 输出

### **θ** — 俯仰姿态，标量

俯仰姿态，在 ±pi 范围内，以弧度为单位返回为标量。

**数据类型：** `double`

### **q** — 俯仰角速率，标量

俯仰角速率，以弧度每秒为单位返回为标量。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度，标量

俯仰角加速度，以弧度每二次方秒为单位返回为标量。

**数据类型：** `double`

### **XeZe** — 机体位置，二元素向量

机体在平面地球参考坐标系中的位置，(*Xe, Ze*)，返回为二元素向量。

**数据类型：** `double`

### **U w** — 机体速度，二元素向量

机体速度分解到机体固定坐标系中，(*u, w*)，返回为二元素向量。

**数据类型：** `double`

### **AxbAzb** — 机体加速度，二元素向量

机体相对于机体固定坐标系的加速度，(*Ax, Az*)，返回为二元素向量，采用 **单位** 中选择的单位。

**数据类型：** `double`

### **Fuel** — 燃料箱状态，标量

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

#### 依赖项

要启用此端口，请将 **质量类型** 设置为 `Simple Variable`。

**数据类型：** `double`

### **AxeAze** — 机体加速度，二元素向量

机体相对于惯性（平面地球）坐标系的加速度，返回为二元素向量。通常将此信号连接到加速度计。

#### 依赖项

要启用此端口，请选中 **包含惯性加速度** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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

### **轴** — 机体轴或风轴 `Body` (default) | `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** character vector |
| **值：** `Wind` | `Body` |
| **默认：** `Body` |

### **质量类型** — 质量类型 `Simple Variable` (default) | `Fixed` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯性作为质量率的线性函数变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Simple Variable` 选择符合算法中描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Simple Variable'` |

### **初始速度** — 机体初始速度 `100` (default) | 标量

机体初始速度，(*V*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `v_ini` |
| **类型：** character vector |
| **值：** `'100'` | 标量 |
| **默认：** `'100'` |

### **初始机体姿态** — 初始俯仰姿态 `0` (default) | 标量

机体的初始俯仰姿态，(*θ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始机体旋转速率** — 初始俯仰旋转速率 `0` (default) | 标量

机体的初始俯仰旋转速率，(*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始迎角** — 初始角度 `0` (default) | 标量

速度向量与机体之间的初始角度，(*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** character vector |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **初始位置 (x,z)** — 初始位置 `[0 0]` (default) | 二元素向量

机体在平面地球参考坐标系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** character vector |
| **值：** `'[0 0]'` | 二元素向量 |
| **默认：** `'[0 0]'` |

### **初始质量** — 初始质量 `1.0` (default) | 标量

刚体的初始质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** character vector |
| **值：** `'1.0'` | 标量 |
| **默认：** `'1.0'` |

### **空质量** — 燃料箱为空时机体的质量 `0.5` (default) | 标量

燃料箱为空时机体的质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** `'0.5'` | 标量 |
| **默认：** `'0.5'` |

### **满质量** — 燃料箱为满时机体的质量 `3.0` (default) | 标量

燃料箱为满时机体的质量，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** `'3.0'` | 标量 |
| **默认：** `'3.0'` |

### **空惯性** — 燃料箱为满时机体的惯性 `0.5` (default) | 标量

燃料箱为满时机体的惯性，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy_e` |
| **类型：** character vector |
| **值：** `'0.5'` | 标量 |
| **默认：** `'0.5'` |

### **满惯性** — 满惯性 `3.0` (default) | 标量

机体的满惯性，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Iyy_f` |
| **类型：** character vector |
| **值：** `'3.0'` | 标量 |
| **默认：** `'3.0'` |

### **重力源** — 重力源 `Internal` (default) | `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 模块的可变重力输入 |
| `Internal` | 在封装中指定的恒定重力 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `g_in` |
| **类型：** character vector |
| **值：** `'Internal'` | `'External'` |
| **默认：** `'Internal'` |

### **重力加速度** — 重力源 `9.81` (default) | 标量

重力加速度，指定为 double 标量，并在选择内部重力源时使用。如果要在仿真中忽略重力，可将此值设置为 `0`。

#### 依赖项

- 要启用此参数，请将 **重力源** 设置为 `Internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `g` |
| **类型：** character vector |
| **值：** `'9.81'` | 标量 |
| **默认：** `'9.81'` |

### **包含质量流相对速度** — 质量流相对速度端口 `off` (default) | `on`

选中此复选框可添加质量流相对速度端口。这是质量增加或减少时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认：** `'off'` |

### **当质量为空或满时限制质量流** — 限制质量流 `on` (default) | `off`

选中此复选框可在以下任一情况为 true 时限制输入质量流率：

- 燃料箱已满且输入质量流率为正。
- 燃料箱为空且输入质量流率为负。

当输入质量流率可能导致质量超出其限制时，模块在运动方程中使用零质量流率值。有关更多信息，请参阅算法。

如果不希望限制输入质量流率，请清除此复选框。

#### 依赖项

要启用此参数，请将 **质量类型** 设置为 `Simple Variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mdot_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'on'` |

**数据类型：** `double`

### **包含惯性加速度** — 包含惯性加速度端口 `off` (default) | `on`

选中此复选框可添加平面地球坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖项

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

- 名称数量必须与每个项所示的状态数量一致，或者为空。为模块状态全部设置或全部不设置。
- 要为单变量状态分配名称，请在引号之间输入唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array of character vectors 或 string。

### **速度：例如，{'u, 'w'}** — 速度状态名称 `''` (default) | 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vel_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **俯仰姿态：例如，'theta'** — 俯仰姿态状态名称 `''` (default)

俯仰姿态状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_statename` |
| **类型：** character vector | string |
| **值：** `''` |
| **默认：** `''` |

### **位置：例如，{'Xe', 'Ze'}** — 位置状态名称 `''` (default) | 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **俯仰角速率，例如，'q'** — 俯仰角速率状态名称 `''` (default)

俯仰角速率状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''` (default) | 标量

质量状态名称，指定为 character vector 或 string。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector | string |
| **值：** `''` | 标量 |
| **默认：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### Simple Variable Mass 3DOF (Body Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型将继续运行。如果将 3DOF 运动方程模块的 R2021b 之前版本替换为 R2021b 或更高版本，则更新后的模型可能更容易出现代数环。有关如何使用单位延迟消除代数环的示例，请参阅 Remove Algebraic Loops。有关代数环的更多信息，请参阅 Identify Algebraic Loops in Your Model。

## 描述

实现相对于机体轴的简单变质量三自由度运动方程

Simple Variable Mass 3DOF (Body Axes) 模块实现相对于机体轴的简单变质量三自由度运动方程。它考虑机体固定坐标系在垂直平面内绕平面地球参考坐标系的旋转。有关旋转和运动方程的更多信息，请参阅算法。
