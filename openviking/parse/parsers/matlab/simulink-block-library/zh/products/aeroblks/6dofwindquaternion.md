---
type: simulink-block
title: '6DOF Wind (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofwindquaternion'
documentation_source_path: '6dofwindquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF Wind (Quaternion)

## 端口

### 输入

### **Fxyz(N)** — 施加的力三元素向量

施加的力，指定为三元素向量。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加的力矩三元素向量

施加的力矩，指定为三元素向量。

**数据类型：** `double`
### 输出

### **Ve** — 平地参考坐标系中的速度三元素向量

平地参考坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平地参考坐标系中的位置三元素向量

平地参考坐标系中的位置，返回为三元素向量。

**数据类型：** `double`

### **μ γ x (rad)** — 风旋转角三元素向量

风旋转角 [滚转角、航迹角、航向角]，返回为三元素向量，以 radians 为单位。

**数据类型：** `double`

### **DCMwe** — 坐标变换 3×3 矩阵

从平地坐标轴到风固定坐标轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vw** — 风固定坐标系中的速度三元素向量

风固定坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **α β (rad)** — 迎角和侧滑角二元素向量

迎角和侧滑角，返回为二元素向量，以 radians 为单位。

**数据类型：** `double`

### **dα/dt dβ/dt** — 迎角变化率和侧滑角变化率二元素向量

迎角变化率和侧滑角变化率，返回为二元素向量，以 radians per second 为单位。

**数据类型：** `double`

### **ωb (rad/s)** — 体固定轴中的角速率三元素向量

体固定轴中的角速率，返回为三元素向量。

**数据类型：** `double`

### **dωb/dt** — 体固定轴中的角加速度三元素向量

体固定轴中的角加速度，返回为三元素向量，以 radians per second squared 为单位。

**数据类型：** `double`

### **Abb** — 体固定轴中的加速度三元素向量

相对于机体坐标系的体固定轴中的加速度，返回为三元素向量。

**数据类型：** `double`

### **Abe** — 相对于惯性坐标系的加速度三元素向量

相对于惯性坐标系（平地）的体固定轴中的加速度，返回为三元素向量。通常将此信号连接到加速度计。

#### 依赖关系

要启用此点，选择 **包含惯性加速度**。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 编程使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **质量类型** — 质量类型 `Fixed` (默认) | `Simple Variable` | `Custom Variable`

质量类型，按下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持不变。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性作为质量速率的函数线性变化。 | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

`Simple Variable` 选择符合前面描述的运动方程。

#### 编程使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Fixed'` |

### **表示形式** — 运动方程表示形式 `Quaternion` (默认) | `Wind Angles`

运动方程表示形式，按下表指定。

|  |  |
| --- | --- |
| `Quaternion` | 在运动方程中使用四元数。 |
| `Wind Angles` | 在运动方程中使用风角。 |

`Quaternion` 选择符合算法中的运动方程。

#### 编程使用

|  |
| --- |
| **模块参数：** `rep` |
| **类型：** character vector |
| **值：** `Wind Angles` | `Quaternion` |
| **默认值：** `'Quaternion'` |

### **惯性轴中的初始位置 [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]` (默认) | three-element vector

刚体在平地参考坐标系中的初始位置，指定为三元素向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始空速、迎角和侧滑角 [V,alpha,beta]** — 初始空速、迎角和侧滑角 `[0 0 0]` (默认) | three-element vector

初始空速、迎角和侧滑角，指定为三元素向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始风朝向 [滚转角,航迹角,航向角]** — 初始风朝向 `[0 0 0]` (默认) | three-element vector

初始风角 [滚转角、航迹角和航向角]，指定为以 radians 为单位的三元素向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `wind_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始体旋转速率 [p,q,r]** — 初始体旋转 `[0 0 0]` (默认) | three-element vector

相对于 NED 坐标系的初始体固定角速率，指定为三元素向量，以 radians per second 为单位。

#### 编程使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始质量** — 初始质量 `1.0` (默认) | scalar

刚体的初始质量，指定为 double scalar。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double scalar |
| **默认值：** `'1.0'` |

### **体轴中的惯性** — 刚体惯性 `eye(3)` (默认) | scalar

刚体的惯性，指定为 double scalar。

#### 编程使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `'eye(3)'` | double scalar |
| **默认值：** `'eye(3)'` |

### **包含惯性加速度** — 包含惯性加速度端口 `off` (默认) | `on`

选择此复选框可添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用大括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅适用于具有 name 参数的选定模块。
- 状态数必须能够被状态名称数整除。
- 指定的名称可以少于状态数，但不能多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **位置：例如，{'Xe','Ye','Ze'}** — 位置状态名称 `''` (默认) | comma-separated list surrounded by braces

位置状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | comma-separated list surrounded by braces |
| **默认值：** `''` |

### **速度：例如，'V'** — 速度状态名称 `''` (默认) | character vector

速度状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | character vector |
| **默认值：** `''` |

### **迎角，例如，'alpha'** — 迎角状态名称 `''` (默认) | character vector

迎角状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `alpha_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **侧滑角，例如，'beta'** — 侧滑角状态名称 `''` (默认) | character vector

侧滑角状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `beta_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **风朝向，例如，{'mu', 'gamma', 'chi'}** — 风朝向状态名称 `''` (默认) | comma-separated list surrounded by braces

风朝向状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `wind_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **四元数向量：例如，{'qr','qi','qj','qk'}** — 四元数向量状态名称 `''` (默认) | comma-separated list surrounded by braces

四元数向量状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | comma-separated list surrounded by braces |
| **默认值：** `''` |

### **体旋转速率：例如，{'p','q','r'}** — 体旋转状态名称 `''` (默认) | comma-separated list surrounded by braces

体旋转速率状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | comma-separated list surrounded by braces |
| **默认值：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''` (默认) | character vector

质量状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector |
| **值：** `''` | character vector |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

## 描述

实现相对于风轴的四元数表示六自由度运动方程

6DOF Wind (Quaternion) 模块考虑风固定坐标系（*Xw, Yw, Zw*）绕平地参考坐标系（*Xe, Ye, Ze*）的旋转。有关风固定坐标系的详细信息，请参阅算法。

Aerospace Blockset™ 使用按标量优先约定定义的四元数。
