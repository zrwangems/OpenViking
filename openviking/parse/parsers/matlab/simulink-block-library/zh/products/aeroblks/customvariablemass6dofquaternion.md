---
type: simulink-block
title: 'Custom Variable Mass 6DOF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'customvariablemass6dofquaternion'
documentation_source_path: 'customvariablemass6dofquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Variable Mass 6DOF (Quaternion)

## 端口

### 输入

### **Fxyz** — 施加力三元素向量

施加力，指定为三元素向量。

**数据类型：** `double`

### **Mxyz** — 施加力矩三元素向量

施加力矩，指定为三元素向量。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（若质量增加则为正，若质量减少则为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### **m** — 质量标量

质量，指定为标量。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵变化率 3×3 矩阵

惯性张量矩阵变化率，指定为 3×3 矩阵。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3×3 矩阵

惯性张量矩阵，指定为 3×3 矩阵。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

质量在体固定轴系中附着到机体或从机体剥离时的一个或多个相对速度，指定为三元素向量。

#### 依赖关系

要启用此端口，请选择 **Include mass flow relative velocity**。

**数据类型：** `double`
### 输出

### **Ve** — 平地参考系中的速度三元素向量

平地参考系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平地参考系中的位置三元素向量

平地参考系中的位置，返回为三元素向量。

**数据类型：** `double`

### **φ θ ψ (rad)** — 欧拉旋转角三元素向量

欧拉旋转角 [roll, pitch, yaw]，返回为三元素向量，单位为 radians。

**数据类型：** `double`

### **DCMbe** — 坐标变换 3×3 矩阵

从平地轴系到体固定轴系的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 体固定坐标系中的速度三元素向量

体固定坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **ωb (rad/s)** — 体固定轴系中的角速率三元素向量

体固定轴系中的角速率，返回为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

### 主

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 编程用法

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Custom Variable`（默认） | `Simple Variable` | `Fixed`

质量类型，根据下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 在整个仿真过程中质量恒定。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性随质量流率线性变化。 | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

`Custom Variable` 选择符合前面描述的运动方程。

#### 编程用法

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Custom Variable'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — 惯性轴系中的位置 `[0 0 0]`（默认） | 三元素向量

机体在平地参考系中的初始位置，指定为三元素向量。

#### 编程用法

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial velocity in body axes [U,v,w]** — 体轴系中的速度 `[0 0 0]`（默认） | 三元素向量

体轴系中的初始速度，指定为三元素向量，位于体固定坐标系中。

#### 编程用法

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial Euler orientation [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]`（默认） | 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，单位为 radians。欧拉旋转角是机体坐标系与 north-east-down (NED) 坐标系之间的角度。

#### 编程用法

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始体旋转 `[0 0 0]`（默认） | 三元素向量

相对于 NED 坐标系的初始体固定角速率，指定为三元素向量，单位为 radians per second。

#### 编程用法

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认） | `on`

选中此复选框可添加质量流相对速度端口。这是质量被附着或剥离时的相对速度。

#### 编程用法

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅应用于带名称参数的所选模块。
- 状态数量必须能被状态名称数量整除。
- 指定的名称数量可以少于状态数量，但不能多于状态数量。

  例如，在具有四个状态的系统中可以指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **Position: e.g., {'Xe','Ye','Ze'}** — 位置状态名称 `''`（默认） | 用花括号括起的逗号分隔列表

位置状态名称，指定为用花括号括起的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认值：** `''` |

### **Velocity: e.g., {'U','v','w'}** — 速度状态名称 `''`（默认） | 用花括号括起的逗号分隔列表

速度状态名称，指定为用花括号括起的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认值：** `''` |

### **Quaternion: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''`（默认） | 用花括号括起的逗号分隔列表

四元数向量状态名称，指定为用花括号括起的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认值：** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 体旋转状态名称 `''`（默认） | 用花括号括起的逗号分隔列表

体旋转速率状态名称，指定为用花括号括起的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2025a: 6DOF equations of motion 模块加速度端口已移除

由于移除了加速度端口，对于 Custom Variable Mass 6DOF (Quaternion)，**Include inertial acceleration** 参数已替换为 **Output mass properties for acceleration computation**。

与此更改相关，模块参数和输出端口已更改：

| 模块 | 端口 | 参数 |
| --- | --- | --- |
| Custom Variable Mass 6DOF (Quaternion) | - dωb/dt 已移除 - Abb 已移除 - Abe 已移除 | - **Representation** 已移除 - **Gain for quaternion   normalization** 已移除 |

由于这些更改，模块输出维度已从 2D 行向量（例如 2-by-*N* 向量）变为 1D 向量 *N*。*N* 是元素数量。

## 描述

实现相对于体轴系的自定义变质量六自由度运动方程的四元数表示

Custom Variable Mass 6DOF (Quaternion) 模块实现相对于体轴系的自定义变质量六自由度运动方程的四元数表示。有关坐标系和平移动力学的描述，请参阅 Custom Variable Mass 6DOF (Euler Angles) 模块的模块描述。

Aerospace Blockset™ 使用按 scalar-first 约定定义的四元数。有关四元数向量变化率积分的信息，请参阅算法。

Custom Variable Mass 6DOF (Quaternion)、6DOF (Quaternion) 和 Simple Variable Mass 6DOF (Quaternion) 模块是同一模块的替代配置。

- Custom Variable Mass 6DOF (Quaternion)— 实现相对于体轴系的自定义变质量六自由度运动方程的四元数表示
- 6DOF (Quaternion) — 实现相对于体轴系的六自由度运动方程的四元数表示
- Simple Variable Mass 6DOF (Quaternion) — 实现相对于体轴系的简单变质量六自由度运动方程的四元数表示
