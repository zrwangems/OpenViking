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
```yaml
ports:
- name: Fx
  summary: 沿 *x* 轴施加的力 标量
  direction: input
  data_types: double
- name: Fz
  summary: 沿 *z* 轴施加的力 标量
  direction: input
  data_types: double
- name: M
  summary: 施加的俯仰力矩 标量
  direction: input
  data_types: double
- name: dm/dt
  summary: 质量变化率 标量
  direction: input
  data_types: double
- name: m
  summary: 质量 标量
  direction: input
  data_types: double
- name: dI/dt
  summary: 惯性张量变化率 标量
  direction: input
  data_types: double
- name: I
  summary: 惯性张量 标量
  direction: input
  data_types: double
- name: g
  summary: 重力 标量
  direction: input
  data_types: double
- name: Vre
  summary: 相对速度 二元素向量
  direction: input
  data_types: double
- name: θ
  summary: 俯仰姿态 标量
  direction: output
  data_types: double
- name: q
  summary: 俯仰角速率 标量
  direction: output
  data_types: double
- name: dq/dt
  summary: 俯仰角加速度 标量
  direction: output
  data_types: double
- name: XeZe
  summary: 机体位置 二元素向量
  direction: output
  data_types: double
- name: U w
  summary: 机体速度 二元素向量
  direction: output
  data_types: double
- name: AxbAzb
  summary: 机体加速度 二元素向量
  direction: output
  data_types: double
- name: AxeAze
  summary: 机体加速度 二元素向量
  direction: output
  data_types: double
```

### 输入

### **Fx** — 沿 *x* 轴施加的力 标量

沿机体 *x* 轴施加的力，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴施加的力 标量

沿机体 *z* 轴施加的力，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **M** — 施加的俯仰力矩 标量

施加的俯仰力矩，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **dm/dt** — 质量变化率 标量

质量变化率（累积为正，烧蚀为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **m** — 质量 标量

质量，指定为标量，单位在 **Units** 中选择。

**数据类型：** `double`

### **dI/dt** — 惯性张量变化率 标量

惯性张量 *Iyy* 的变化率，指定为标量，单位在 **Units** 中选择。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **I** — 惯性张量 标量

惯性张量，指定为标量，单位在 **Units** 中选择。

#### 依赖关系

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **g** — 重力 标量

重力，指定为标量。

#### 依赖关系

要启用此端口，请将 **Gravity source** 设置为 `External`。

**数据类型：** `double`

### **Vre** — 相对速度 二元素向量

质量在机体坐标系中累积到机体或从机体烧蚀的相对速度，指定为二元素向量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`
### 输出

### **θ** — 俯仰姿态 标量

俯仰姿态，在 ±pi 范围内，以弧度（*θ*）返回为标量。

**数据类型：** `double`

### **q** — 俯仰角速率 标量

俯仰角速率，以弧度每秒返回为标量。

**数据类型：** `double`

### **dq/dt** — 俯仰角加速度 标量

俯仰角加速度，以弧度每二次方秒返回为标量。

**数据类型：** `double`

### **XeZe** — 机体位置 二元素向量

机体在平面地球参考坐标系中的位置，(*Xe, Ze*)，返回为二元素向量。

**数据类型：** `double`

### **U w** — 机体速度 二元素向量

机体速度在机体坐标系中的分量，(*u, w*)，返回为二元素向量。

**数据类型：** `double`

### **AxbAzb** — 机体加速度 二元素向量

机体相对于机体坐标系的加速度，(*Ax, Az*)，返回为二元素向量，单位在 **Units** 中选择。

**数据类型：** `double`

### **AxeAze** — 机体加速度 二元素向量

机体相对于惯性（平面地球）坐标系的加速度，返回为二元素向量。通常将此信号连接到加速度计。

#### 依赖关系

要启用此端口，请选中 **Include inertial acceleration** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: 主
  block_parameter: units
  type: 字符向量
  values: Metric (MKS) | English (Velocity in ft/s) | English (Velocity in kts)
- name: Axes
  summary: 机体轴或风轴 Body（默认）| Wind
  group: 主
  block_parameter: axes
  type: 字符向量
  values: Wind | Body
- name: Mass type
  summary: 质量类型 Custom Variable（默认）| Fixed | Simple Variable
  group: 主
  block_parameter: mtype
  type: 字符向量
  values: Fixed | Simple Variable | Custom Variable
- name: Initial velocity
  summary: 机体初始速度 100（默认）| 标量
  group: 主
  block_parameter: v_ini
  type: 字符向量
  values: '''100'' | 标量'
- name: Initial body attitude
  summary: 初始俯仰姿态 0（默认）| 标量
  group: 主
  block_parameter: theta_ini
  type: 字符向量
  values: '''0'' | 标量'
- name: Initial body rotation rate
  summary: 初始俯仰旋转速率 0（默认）| 标量
  group: 主
  block_parameter: q_ini
  type: 字符向量
  values: '''0'' | 标量'
- name: Initial incidence
  summary: 初始角度 0（默认）| 标量
  group: 主
  block_parameter: alpha_ini
  type: 字符向量
  values: '''0'' | 标量'
- name: Initial position (x,z)
  summary: 初始位置 [0 0]（默认）| 二元素向量
  group: 主
  block_parameter: pos_ini
  type: 字符向量
  values: '''[0 0]'' | 二元素向量'
- name: Gravity Source
  summary: 重力源 Internal（默认）| External
  group: 主
  block_parameter: g_in
  type: 字符向量
  values: '''Internal'' | ''External'''
- name: Acceleration due to gravity
  summary: 重力源 9.81（默认）| 标量
  group: 主
  block_parameter: g
  type: 字符向量
  values: '''9.81'' | 标量'
- name: Include mass flow relative velocity
  summary: 质量流相对速度端口 off（默认）| on
  group: 主
  block_parameter: vre_flag
  type: 字符向量
  values: off | on
- name: Include inertial acceleration
  summary: 包含惯性加速度端口 off（默认）| on
  group: 主
  block_parameter: abi_flag
  type: 字符向量
  values: '''off'' | ''on'''
- name: 'Velocity: e.g., {''u, ''w''}'
  summary: 速度状态名称 ''（默认）| 用花括号括起来的逗号分隔列表
  group: 状态属性
  block_parameter: vel_statename
  type: 字符向量
  values: ''''' | 用花括号括起来的逗号分隔列表'
- name: 'Position: e.g., {''Xe'', ''Ze''}'
  summary: 位置状态名称 ''（默认）| 用花括号括起来的逗号分隔列表
  group: 状态属性
  block_parameter: pos_statename
  type: 字符向量
  values: ''''' | 用花括号括起来的逗号分隔列表'
- name: Pitch angular rate e.g., 'q'
  summary: 俯仰角速率状态名称 ''（默认）
  group: 状态属性
  block_parameter: q_statename
  type: 字符向量 | 字符串
  values: ''''' | 标量'
- name: 'Pitch attitude: e.g., ''theta'''
  summary: 俯仰姿态状态名称 ''（默认）
  group: 状态属性
  block_parameter: theta_statename
  type: 字符向量 | 字符串
  values: ''''''
```

### 主

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

### **Axes** — 机体轴或风轴 `Body`（默认）| `Wind`

机体轴或风轴，指定为 `Wind` 或 `Body`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `axes` |
| **类型：** 字符向量 |
| **值：** `Wind` | `Body` |
| **默认：** `Body` |

### **Mass type** — 质量类型 `Custom Variable`（默认）| `Fixed` | `Simple Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 3DOF (Body   Axes) - 3DOF (Wind   Axes) |
| `Simple Variable` | 质量和惯性随质量速率线性变化。 | - Simple   Variable Mass 3DOF (Body Axes) - Simple   Variable Mass 3DOF (Wind Axes) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom   Variable Mass 3DOF (Body Axes) - Custom   Variable Mass 3DOF (Wind Axes) |

`Custom Variable` 选项符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** 字符向量 |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Custom Variable'` |

### **Initial velocity** — 机体初始速度 `100`（默认）| 标量

机体的初始速度，(*V*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `v_ini` |
| **类型：** 字符向量 |
| **值：** `'100'` | 标量 |
| **默认：** `'100'` |

### **Initial body attitude** — 初始俯仰姿态 `0`（默认）| 标量

机体的初始俯仰姿态，(*θ*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **Initial body rotation rate** — 初始俯仰旋转速率 `0`（默认）| 标量

初始俯仰旋转速率，(*q*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **Initial incidence** — 初始角度 `0`（默认）| 标量

速度向量与机体之间的初始角度，(*α*0)，指定为标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_ini` |
| **类型：** 字符向量 |
| **值：** `'0'` | 标量 |
| **默认：** `'0'` |

### **Initial position (x,z)** — 初始位置 `[0 0]`（默认）| 二元素向量

机体在平面地球参考坐标系中的初始位置，指定为二元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_ini` |
| **类型：** 字符向量 |
| **值：** `'[0 0]'` | 二元素向量 |
| **默认：** `'[0 0]'` |

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
| **默认：** `'Internal'` |

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
| **默认：** `'9.81'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认）| `on`

选中此复选框可添加质量流相对速度端口。这是质量累积或烧蚀的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** 字符向量 |
| **值：** `off` | `on` |
| **默认：** `'off'` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认）| `on`

选中此复选框可添加平面地球坐标系中的惯性加速度输出端口。通常将此信号连接到加速度计。

#### 依赖关系

要启用 **AxeAze** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### 状态属性

为每个状态分配唯一名称。在线性化过程中，可以使用状态名称代替模块路径。

- 名称数量必须与状态数量匹配（如每个项所示），或为空。设置所有或全部不设置模块状态。
- 要为单变量状态分配名称，请输入引号内的唯一名称，例如 `'q'` 或 `"q"`。
- 要为双变量状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'Xe','Ze'}`。
- 如果状态参数为空（`' '`），则不分配名称。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符向量元胞数组或字符串。

### **Velocity: e.g., {'u, 'w'}** — 速度状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vel_statename` |
| **类型：** 字符向量 |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **Position: e.g., {'Xe', 'Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pos_statename` |
| **类型：** 字符向量 |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **Pitch angular rate e.g., 'q'** — 俯仰角速率状态名称 `''`（默认）

俯仰角速率状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `q_statename` |
| **类型：** 字符向量 | 字符串 |
| **值：** `''` | 标量 |
| **默认：** `''` |

### **Pitch attitude: e.g., 'theta'** — 俯仰姿态状态名称 `''`（默认）

俯仰姿态状态名称，指定为字符向量或字符串。

#### 程序化使用

|  |
| --- |
| **模块参数：** `theta_statename` |
| **类型：** 字符向量 | 字符串 |
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

### R2021b：Custom Variable Mass 3DOF (Body Axes) 模块变更

3DOF 运动方程已更新。在 R2021b 之前创建的包含 3DOF 运动方程模块的现有模型继续运行。如果将 R2021b 之前版本的 3DOF 运动方程模块替换为 R2021b 或更高版本，更新后的模型可能更容易出现代数环。有关如何使用单位延迟消除代数环的示例，请参阅 Remove Algebraic Loops。有关代数环的更多信息，请参阅 Identify Algebraic Loops in Your Model。

## 描述

实现相对于机体轴的自定义可变质量三自由度运动方程

Custom Variable Mass 3DOF (Body Axes) 模块实现相对于机体轴的自定义可变质量三自由度运动方程。它考虑机体固定坐标系在平面地球参考坐标系中垂直平面内的旋转。有关旋转和运动方程的更多信息，请参阅 Algorithms。
