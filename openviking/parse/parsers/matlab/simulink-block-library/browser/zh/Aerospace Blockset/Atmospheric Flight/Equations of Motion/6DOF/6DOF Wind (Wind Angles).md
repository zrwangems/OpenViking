---
type: simulink-block
title: '6DOF Wind (Wind Angles)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofwindwindangles'
documentation_source_path: '6dofwindwindangles.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF Wind (Wind Angles)

## 端口

### 输入

### **Fxyz(N)** — 施加力三元素向量

施加力，指定为三元素向量。

**数据类型:** `double`

### **Mxyz(N-m)** — 施加力矩三元素向量

施加力矩，指定为三元素向量。

**数据类型:** `double`
### 输出

### **Ve** — 平地参考系中的速度三元素向量

平地参考系中的速度，返回为三元素向量。

**数据类型:** `double`

### **Xe** — 平地参考系中的位置三元素向量

平地参考系中的位置，返回为三元素向量。

**数据类型:** `double`

### **μ γ x (rad)** — 风旋转角三元素向量

风旋转角 [bank, flight path, heading]，返回为三元素向量，以 radians 为单位。

**数据类型:** `double`

### **DCMwe** — 坐标变换 3×3 矩阵

从平地轴系到风固定轴系的坐标变换，返回为 3×3 矩阵。

**数据类型:** `double`

### **Vw** — 风固定坐标系中的速度三元素向量

风固定坐标系中的速度，返回为三元素向量。

**数据类型:** `double`

### **α β (rad)** — 迎角和侧滑角二元素向量

迎角和侧滑角，返回为二元素向量，以 radians 为单位。

**数据类型:** `double`

### **dα/dt dβ/dt** — 迎角变化率和侧滑角变化率二元素向量

迎角变化率和侧滑角变化率，返回为二元素向量，以 radians per second 为单位。

**数据类型:** `double`

### **ωb (rad/s)** — 体固定轴系中的角速率三元素向量

体固定轴系中的角速率，返回为三元素向量。

**数据类型:** `double`

### **dωb/dt** — 体固定轴系中的角加速度三元素向量

体固定轴系中的角加速度，返回为三元素向量，以 radians per second squared 为单位。

**数据类型:** `double`

### **Abb** — 体固定轴系中的加速度三元素向量

相对于体坐标系的体固定轴系中的加速度，返回为三元素向量。

**数据类型:** `double`

### **Abe** — 相对于惯性系的加速度三元素向量

相对于惯性系（平地）的体固定轴系中的加速度，返回为三元素向量。通常将此信号连接到加速度计。

#### 依赖关系

仅当选中 **Include inertial acceleration** 复选框时，此端口才会出现。

**数据类型:** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
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

### **Mass type** — 质量类型 `Fixed` (默认) | `Simple Variable` | `Custom Variable`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在仿真过程中保持恒定。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数:** `mtype` |
| **类型:** character vector |
| **值:** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值:** `'Fixed'` |

### **Representation** — 运动方程表示 `Wind Angles` (默认) | `Quaternion`

运动方程表示，根据下表指定。

| 表示 | 描述 |
| --- | --- |
| `Wind Angles` | 在运动方程中使用风角。 |
| `Quaternion` | 在运动方程中使用四元数。 |

`Quaternion` 选择符合算法中的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数:** `rep` |
| **类型:** character vector |
| **值:** `Wind Angles` | `Quaternion` |
| **默认值:** `'Wind Angles'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]` (默认) | 三元素向量

物体在平地参考系中的初始位置，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `xme_0` |
| **类型:** character vector |
| **值:** `'[0 0 0]'` | 三元素向量 |
| **默认值:** `'[0 0 0]'` |

### **Initial airspeed, angle of attack, and sideslip angle [V,alpha,beta]** — 初始空速、迎角和侧滑角 `[0 0 0]` (默认) | 三元素向量

初始空速、迎角和侧滑角，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数:** `Vm_0` |
| **类型:** character vector |
| **值:** `'[0 0 0]'` | 三元素向量 |
| **默认值:** `'[0 0 0]'` |

### **Initial wind orientation [bank angle,flight path angle,heading angle]** — 初始风朝向 `[0 0 0]` (默认) | 三元素向量

初始风角 [滚转, 航迹和航向]，指定为三元素向量，以 radians 为单位。

#### 程序化使用

|  |
| --- |
| **模块参数:** `wind_0` |
| **类型:** character vector |
| **值:** `'[0 0 0]'` | 三元素向量 |
| **默认值:** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始体旋转速率 `[0 0 0]` (默认) | 三元素向量

相对于 NED 坐标系的初始体固定角速率，指定为三元素向量，以 radians per second 为单位。

#### 程序化使用

|  |
| --- |
| **模块参数:** `pm_0` |
| **类型:** character vector |
| **值:** `'[0 0 0]'` | 三元素向量 |
| **默认值:** `'[0 0 0]'` |

### **Initial mass** — 初始质量 `1.0` (默认) | 标量

刚体的初始质量，指定为 double scalar。

#### 程序化使用

|  |
| --- |
| **模块参数:** `mass_0` |
| **类型:** character vector |
| **值:** `'1.0'` | double scalar |
| **默认值:** `'1.0'` |

### **Inertia in body axis** — 体轴中的惯性 `eye(3)` (默认) | 标量

刚体的惯性，指定为 double scalar。

#### 程序化使用

|  |
| --- |
| **模块参数:** `inertia` |
| **类型:** character vector |
| **值:** `'eye(3)'` | double scalar |
| **默认值:** `'eye(3)'` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off` (默认) | `on`

选中此复选框以添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数:** `abi_flag` |
| **类型:** character vector |
| **值:** `'off'` | `'on'` |
| **默认值:** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入由花括号括起的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果某参数为空 (`' '`)，则不分配任何名称。
- 状态名称仅应用于具有名称参数的所选模块。
- 状态数量必须能被状态名称数量整除。
- 你可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，你可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **Position: e.g., {'Xe','Ye','Ze'}** — 位置状态名称 `''` (默认) | 由花括号括起的逗号分隔列表

位置状态名称，指定为由花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数:** `xme_statename` |
| **类型:** character vector |
| **值:** `''` | 由花括号括起的逗号分隔列表 |
| **默认值:** `''` |

### **Velocity: e.g., 'V'** — 速度状态名称 `''` (默认) | character vector

速度状态名称，指定为 character vector。

#### 程序化使用

|  |
| --- |
| **模块参数:** `Vm_statename` |
| **类型:** character vector |
| **值:** `''` | character vector |
| **默认值:** `''` |

### **Incidence angle e.g., 'alpha'** — 迎角状态名称 `''` (默认) | character vector

迎角状态名称，指定为 character vector。

#### 程序化使用

|  |
| --- |
| **模块参数:** `alpha_statename` |
| **类型:** character vector |
| **值:** `''` |
| **默认值:** `''` |

### **Sideslip angle e.g., 'beta'** — 侧滑角状态名称 `''` (默认) | character vector

侧滑角状态名称，指定为 character vector。

#### 程序化使用

|  |
| --- |
| **模块参数:** `beta_statename` |
| **类型:** character vector |
| **值:** `''` |
| **默认值:** `''` |

### **Wind orientation e.g., {'mu', 'gamma', 'chi'}** — 风朝向状态名称 `''` (默认) | 由花括号括起的逗号分隔列表

风朝向状态名称，指定为由花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数:** `wind_statename` |
| **类型:** character vector |
| **值:** `''` |
| **默认值:** `''` |

### **Quaternion: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''` (默认) | 由花括号括起的逗号分隔列表

四元数向量状态名称，指定为由花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数:** `quat_statename` |
| **类型:** character vector |
| **值:** `''` | 由花括号括起的逗号分隔列表 |
| **默认值:** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 体旋转状态名称 `''` (默认) | 由花括号括起的逗号分隔列表

体旋转速率状态名称，指定为由花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数:** `pm_statename` |
| **类型:** character vector |
| **值:** `''` | 由花括号括起的逗号分隔列表 |
| **默认值:** `''` |

### **Mass: e.g., 'mass'** — 质量状态名称 `''` (默认) | character vector

质量状态名称，指定为 character vector。

#### 程序化使用

|  |
| --- |
| **模块参数:** `mass_statename` |
| **类型:** character vector |
| **值:** `''` | character vector |
| **默认值:** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

实现六自由度运动方程的风角表示

6DOF Wind (Wind Angles) 模块实现六自由度运动方程的风角表示。有关所用坐标系和平移动力学的描述，请参阅 6DOF Wind (Quaternion) 模块的模块说明。

有关风角之间关系的更多信息，请参阅算法。
