---
type: simulink-block
title: 'Simple Variable Mass 3DOF (Wind Axes)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / 3DOF '
documentation_page: 'simplevariablemass3dofwindaxes'
documentation_source_path: 'simplevariablemass3dofwindaxes.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 3DOF (Wind Axes)

## 端口

### 输入

### **Fx** — 沿风轴 *x* 方向的作用力 标量

沿风轴 *x* 方向的作用力，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **Fz** — 沿风轴 *z* 方向的作用力 标量

沿风轴 *z* 方向的作用力，指定为标量。

**数据类型：** `double`

### **M** — 作用俯仰力矩 标量

作用俯仰力矩，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **dm/dt** — 质量变化率 标量

质量变化率（累积为正，消融为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **g** — 重力 标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **Gravity source** 设置为 `External`。

**数据类型：** `double`

### **Vre** — 相对速度 二元素向量

质量在体坐标系中累积到机体或从机体消融的相对速度，指定为二元素向量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`
### 输出

### **γ** — 飞行路径角 标量

飞行路径角，在 ±pi 范围内，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **q** — 俯仰角速率 标量

俯仰角速率，以标量形式返回，单位为弧度每秒。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度 标量

俯仰角加速度，以标量形式返回，单位为弧度每二次方秒。

**数据类型：** `double`

### **XeZe** — 机体位置 二元素向量

机体在平面地球参考系中的位置，(*Xe, Ze*)，以二元素向量形式返回。

**数据类型：** `double`

### **Vw** — 风固坐标系中的速度 二元素向量

机体速度在风固坐标系中的分量，(*V, 0*)，以二元素向量形式返回。

**数据类型：** `double`

### **AxbAzb** — 机体加速度 二元素向量

机体相对于体坐标系系的加速度，(*Ax, Az*)，以二元素向量形式返回，单位在 **Units** 中选择。

**数据类型：** `double`

### **α** — 攻角 标量

攻角，以标量形式返回，单位为弧度。

**数据类型：** `double`

### **Fuel** — 燃料箱状态 标量

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱已空。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **AxeAze** — 机体加速度 二元素向量

机体相对于惯性（平面地球）坐标系系的加速度，以二元素向量形式返回。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **Include inertial acceleration** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | 牛顿 | 牛顿-米 | 米每二次方秒 | 米每秒 | 米 | 千克 | 千克米平方 |
| `English (Velocity in ft/s)` | 磅 | 英尺-磅 | 英尺每二次方秒 | 英尺每秒 | 英尺 | 斯勒格 | 斯勒格英尺平方 |
| `English (Velocity in kts)` | 磅 | 英尺-磅 | 英尺每二次方秒 | 节 | 英尺 | 斯勒格 | 斯勒格英尺平方 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值**：`Metric (MKS)` |

### **Axes** — 体轴或风轴 `Wind`（默认）| `Body`

体轴或风轴，指定为 `Wind` 或 `Body`。

#### 编程使用

|  |
| --- |
| **模块参数**：`axes` |
| **类型**：character vector |
| **值**：`Wind` | `Body` |
| **默认值**：`Wind` |

### **Mass type** — 质量类型 `Simple Variable`（默认）| `Fixed` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯量随质量变化率线性变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯量变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Simple Variable` 选项符合算法中描述的运动方程。

#### 编程使用

|  |
| --- |
| **模块参数**：`mtype` |
| **类型**：character vector |
| **值**：`Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值**：`'Simple Variable'` |

### **Initial airspeed** — 初始速度 `100`（默认）| 标量

机体的初始速度，(*V*0)，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`V_ini` |
| **类型**：character vector |
| **值**：`'100'` | scalar |
| **默认值**：`'100'` |

### **Initial flight path angle** — 初始飞行路径角 `0`（默认）| 标量

机体的初始飞行路径角，(*γ*0)，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`gamma_ini` |
| **类型**：character vector |
| **值**：`'0'` | scalar |
| **默认值**：`'0'` |

### **Initial body rotation rate** — 初始俯仰旋转速率 `0`（默认）| 标量

初始俯仰旋转速率，(*q*0)，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`q_ini` |
| **类型**：character vector |
| **值**：`'0'` | scalar |
| **默认值**：`'0'` |

### **Initial incidence** — 初始角度 `0`（默认）| 标量

速度向量与机体之间的初始角度，(*α*0)，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`alpha_ini` |
| **类型**：character vector |
| **值**：`'0'` | scalar |
| **默认值**：`'0'` |

### **Initial position (x,z)** — 初始位置 `[0 0]`（默认）| 二元素向量

机体在平面地球参考系中的初始位置，指定为二元素向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`pos_ini` |
| **类型**：character vector |
| **值**：`'[0 0]'` | two-element vector |
| **默认值**：`'[0 0]'` |

### **Initial mass** — 初始质量 `1.0`（默认）| 标量

刚体的初始质量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass` |
| **类型**：character vector |
| **值**：`'1.0'` | scalar |
| **默认值**：`'1.0'` |

### **Empty mass** — 燃料箱为空时的机体质量 `0.5`（默认）| 标量

燃料箱为空时的机体质量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass_e` |
| **类型**：character vector |
| **值**：`'0.5'` | scalar |
| **默认值**：`'0.5'` |

### **Full mass** — 燃料箱为满时的机体质量 `3.0`（默认）| 标量

燃料箱为满时的机体质量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass_f` |
| **类型**：character vector |
| **值**：`'3.0'` | scalar |
| **默认值**：`'3.0'` |

### **Empty inertia body axes** — 燃料箱为空时的机体惯量 `0.5`（默认）| 标量

燃料箱为空时的机体惯量，指定为标量。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple Variable`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Iyy_e` |
| **类型**：character vector |
| **值**：`'1.0'` | scalar |
| **默认值**：`'1.0'` |

### **Full inertia body axes** — 燃料箱为满时的机体惯量 `3.0`（默认）| 标量

燃料箱为满时的机体惯量，指定为标量。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple Variable`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Iyy_f` |
| **类型**：character vector |
| **值**：`'3.0'` | scalar |
| **默认值**：`'3.0'` |

### **Gravity Source** — 重力源 `Internal`（默认）| `External`

重力源，指定为：

|  |  |
| --- | --- |
| `External` | 可变重力输入到模块 |
| `Internal` | 在掩码中指定的恒定重力 |

#### 编程使用

|  |
| --- |
| **模块参数**：`g_in` |
| **类型**：character vector |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Acceleration due to gravity** — 重力源 `9.81`（默认）| 标量

重力加速度，指定为双精度标量，在选择内部重力源时使用。如果仿真中忽略重力，可将此值设置为 `0`。

#### 依赖关系

- 要启用此参数，请将 **Gravity Source** 设置为 `Internal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`g` |
| **类型**：character vector |
| **值**：`'9.81'` | scalar |
| **默认值**：`'9.81'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认）| `on`

选中此复选框以添加质量流相对速度端口。这是质量累积或消融的相对速度。

#### 编程使用

|  |
| --- |
| **模块参数**：`vre_flag` |
| **类型**：character vector |
| **值**：`off` | `on` |
| **默认值**：`'off'` |

### **Limit mass flow when mass is empty or full** — 限制质量流 `on`（默认）| `off`

选中此复选框以在以下任一情况为真时限制输入质量流率：

- 燃料箱已满且输入质量流率为正。
- 燃料箱已空且输入质量流率为负。

当输入质量流率可能导致质量超出其限制时，模块在运动方程中使用零质量流率值。有关详细信息，请参阅算法。

如果不希望限制输入质量流率，请清除此复选框。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple Variable`。

#### 编程使用

|  |
| --- |
| **模块参数**：`mdot_flag` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

**数据类型：** `double`

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认）| `on`

选中此复选框以添加平面地球坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`abi_flag` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化过程中，可以使用状态名称代替模块路径。

- 名称数量必须与状态数量匹配（如各项所示），或为空。请设置所有或全部不设置模块状态。
- 要为单变量状态分配名称，请输入引号内的唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符向量元胞数组或字符串。

### **Velocity: e.g., 'V'** — 速度状态名称 `''`（默认）| 字符向量

速度状态名称，指定为字符向量或字符串。

#### 编程使用

|  |
| --- |
| **模块参数**：`V_statename` |
| **类型**：character vector | string |
| **值**：`''` | scalar |
| **默认值**：`''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数**：`pos_statename` |
| **类型**：character vector |
| **值**：`''` | comma-separated list surrounded by braces |
| **默认值**：`''` |

### **Body rotation rate: e.g., 'q'** — 机体旋转状态名称 `''`（默认）| 标量

机体旋转速率状态名称，指定为字符向量或字符串。

#### 编程使用

|  |
| --- |
| **模块参数**：`q_statename` |
| **类型**：character vector | string |
| **值**：`''` | scalar |
| **默认值**：`''` |

### **Flight path angle: e.g., 'gamma'** — 飞行路径角状态名称 `''`（默认）

飞行路径角状态名称，指定为字符向量或字符串。

#### 编程使用

|  |
| --- |
| **模块参数**：`gamma_statename` |
| **类型**：character vector | string |
| **值**：`''` | scalar |
| **默认值**：`''` |

### **Incidence angle e.g., 'alpha'** — 攻角状态名称 `''`（默认）| 标量

攻角状态名称，指定为字符向量或字符串。

#### 编程使用

|  |
| --- |
| **模块参数**：`alpha_statename` |
| **类型**：character vector | string |
| **值**：`''` | scalar |
| **默认值**：`''` |

### **Mass: e.g., 'mass'** — 质量状态名称 `''`（默认）| 标量

质量状态名称，指定为字符向量或字符串。

#### 编程使用

|  |
| --- |
| **模块参数**：`mass_statename` |
| **类型**：character vector | string |
| **值**：`''` | scalar |
| **默认值**：`''` |

## 所属库

Aerospace Blockset / Equations of Motion / 3DOF

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2021b：Simple Variable Mass 3DOF (Wind Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型可继续运行。如果将 R2021b 之前的 3DOF 运动方程模块版本替换为 R2021b 或更高版本，更新后的模型可能更容易出现代数环。有关如何使用单位延迟消除代数环的示例，请参阅 Remove Algebraic Loops。有关代数环的更多信息，请参阅 Identify Algebraic Loops in Your Model。

## 描述

实现简单变质量三自由度运动方程（相对于风轴）

Simple Variable Mass 3DOF (Wind Axes) 模块实现简单变质量三自由度运动方程（相对于风轴）。该模块考虑风固坐标系在垂直平面内绕平面地球参考系的旋转。有关旋转和运动方程的更多信息，请参阅算法。
