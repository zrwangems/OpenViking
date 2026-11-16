---
type: simulink-block
title: 'Simple Variable Mass 6DOF Wind (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofwindquaternion'
documentation_source_path: 'simplevariablemass6dofwindquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 6DOF Wind (Quaternion)

## 端口

### 输入

### **Fxyz(N)** — 施加的力三元素向量

施加的力，指定为三元素向量。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加的力矩三元素向量

施加的力矩，指定为三元素向量。

**数据类型：** `double`

### **dm/dt (kg/s)** — 质量变化率标量

质量变化率（若质量增加则为正，若质量减少则为负），指定为标量。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，指定为三元素向量，质量以该速度在体坐标系中增加或减少。

#### 依赖

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### 输出

### **Ve** — 平坦地球参考系中的速度三元素向量

平坦地球参考系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平坦地球参考系中的位置三元素向量

平坦地球参考系中的位置，返回为三元素向量。

**数据类型：** `double`

### **μ γ x (rad)** — 风旋转角三元素向量

风旋转角 [bank, flight path, heading]，返回为三元素向量，单位为弧度。

**数据类型：** `double`

### **DCMwe** — 坐标变换 3×3 矩阵

从平坦地球坐标系到风固坐标系的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vw** — 风固坐标系中的速度三元素向量

风固坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **α β (rad)** — 攻角和侧滑角二元素向量

攻角和侧滑角，返回为二元素向量，单位为弧度。

**数据类型：** `double`

### **dα/dt dβ/dt** — 攻角变化率和侧滑角变化率二元素向量

攻角变化率和侧滑角变化率，返回为二元素向量，单位为弧度每秒。

**数据类型：** `double`

### **ωb (rad/s)** — 体坐标系中的角速率三元素向量

体坐标系中的角速率，返回为三元素向量。

**数据类型：** `double`

### **dωb/dt** — 体坐标系中的角加速度三元素向量

体坐标系中的角加速度，返回为三元素向量，单位为弧度每二次方秒。

**数据类型：** `double`

### **Abb** — 体坐标系中的加速度三元素向量

相对于体坐标系的体坐标系中的加速度，返回为三元素向量。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，返回为：

- `1` — 油箱已满。
- `0` — 油箱既未满也未空。
- `-1` — 油箱已空。

**数据类型：** `double`

### **Abe** — 相对于惯性系的加速度三元素向量

相对于惯性系（平坦地球）的体坐标系中的加速度，返回为三元素向量。通常将此信号连接到加速度计。

#### 依赖

仅当选中 **Include inertial acceleration** 复选框时，此端口才会出现。

**数据类型：** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)` （默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

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

### **Mass type** — 质量类型 `Simple Variable` （默认）| `Fixed` | `Custom Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定（参见 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯量作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯量变化可自定义（参见 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Simple Variable` 选择符合前述运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认值：** `'Simple Variable'` |

### **Representation** — 运动方程表示 `Quaternion` （默认）| `Wind Angles`

运动方程表示，根据下表指定。

|  |  |
| --- | --- |
| `Quaternion` | 在运动方程中使用四元数。 |
| `Wind Angles` | 在运动方程中使用风角。 |

`Quaternion` 选择符合算法中的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rep` |
| **类型：** character vector |
| **值：** `Wind Angles` | `Quaternion` |
| **默认值：** `'Quaternion'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — 惯性轴中的初始位置 `[0 0 0]` （默认）| 三元素向量

体在平坦地球参考系中的初始位置，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial airspeed, angle of attack, and sideslip angle [V,alpha,beta]** — 初始空速、攻角和侧滑角 `[0 0 0]` （默认）| 三元素向量

初始空速、攻角和侧滑角，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial wind orientation [bank angle,flight path angle,heading angle]** — 初始风取向 `[0 0 0]` （默认）| 三元素向量

初始风角 [bank, flight path, heading]，指定为三元素向量，单位为弧度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `wind_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始体旋转 `[0 0 0]` （默认）| 三元素向量

相对于 NED 系的初始体固角速率，指定为三元素向量，单位为弧度每秒。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial mass** — 初始质量 `1.0` （默认）| 标量

刚体的初始质量，指定为双精度标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | 双精度标量 |
| **默认值：** `'1.0'` |

### **Empty mass** — 空载质量 `0.5` （默认）| 标量

体的空载质量，指定为双精度标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** 双精度标量 |
| **默认值：** `'0.5'` |

### **Full mass** — 体的满载质量 `2.0` （默认）| 标量

体的满载质量，指定为双精度标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** 双精度标量 |
| **默认值：** `'2.0'` |

### **Inertia in body axis** — 体的惯量 `eye(3)` （默认）| 标量

体的惯量，指定为双精度标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `'eye(3)'` | 双精度标量 |
| **默认值：** `'eye(3)'` |

### **Empty inertia matrix in body axis** — 空载惯量的惯量张量矩阵 `eye(3)` （默认）| 3×3 矩阵

体的空载惯量的惯量张量矩阵，指定为 3×3 矩阵，位于体固坐标系中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_e` |
| **类型：** character vector |
| **值：** `'eye(3)'` | 3×3 矩阵 |
| **默认值：** `'eye(3)'` |

### **Full inertia matrix in body axis** — 满载惯量的惯量张量矩阵 `2*eye(3)` （默认）| 3×3 矩阵

体的满载惯量的惯量张量矩阵，指定为 3×3 矩阵，位于体固坐标系中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_f` |
| **类型：** character vector |
| **值：** `'2*eye(3)'` | 3×3 矩阵 |
| **默认值：** `'2*eye(3)'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off` （默认）| `on`

选中此复选框可添加质量流相对速度端口。这是质量增加或减少时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `off` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off` （默认）| `on`

选中此复选框可添加惯性加速度端口。

#### 依赖

要启用 **Ab ff** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化过程中，您可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请输入用引号括起来的唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用大括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅适用于带名称参数的所选模块。
- 状态数必须均匀分配给状态名称数。
- 您可以指定的名称数少于状态数，但不能多于状态数。

  例如，在具有四个状态的系统中，您可以指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、元胞数组或结构体。

### **Position: e.g., {'Xe','Ye','Ze'}** — 位置状态名称 `''` （默认）| 用大括号括起来的逗号分隔列表

位置状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Velocity: e.g., 'V'** — 速度状态名称 `''` （默认）| 字符向量

速度状态名称，指定为字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 字符向量 |
| **默认值：** `''` |

### **Incidence angle e.g., 'alpha'** — 迎角状态名称 `''` （默认）| 字符向量

迎角状态名称，指定为字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `alpha_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **Sideslip angle e.g., 'beta'** — 侧滑角状态名称 `''` （默认）| 字符向量

侧滑角状态名称，指定为字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `beta_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **Wind orientation e.g., {'mu', 'gamma', 'chi'}** — 风取向状态名称 `''` （默认）| 用大括号括起来的逗号分隔列表

风取向状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `wind_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **Quaternion vector: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''` （默认）| 用大括号括起来的逗号分隔列表

四元数向量状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 体旋转状态名称 `''` （默认）| 用大括号括起来的逗号分隔列表

体旋转速率状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Mass: e.g., 'mass'** — 质量状态名称 `''` （默认）| 字符向量

质量状态名称，指定为字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector |
| **值：** `''` | 字符向量 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

实现简单变质量六自由度运动方程的 quaternion 表示，相对于风轴

Simple Variable Mass 6DOF Wind (Quaternion) 模块实现了简单变质量六自由度运动方程的 quaternion 表示，相对于风轴。它考虑了风固坐标系（*Xw*、*Yw*、*Zw*）绕平坦地球参考系（*Xe*、*Ye*、*Ze*）的旋转。

Aerospace Blockset™ 使用按标量优先约定定义的 quaternion。有关风固坐标系的更多信息，请参见算法。
