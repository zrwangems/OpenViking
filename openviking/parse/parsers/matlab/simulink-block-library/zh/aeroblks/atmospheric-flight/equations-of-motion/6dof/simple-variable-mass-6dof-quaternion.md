---
type: simulink-block
title: 'Simple Variable Mass 6DOF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofquaternion'
documentation_source_path: 'simplevariablemass6dofquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 6DOF (Quaternion)

## 端口

### 输入

### **Fxyz** — 施加力三元素向量

施加力，指定为三元素向量。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加力矩三元素向量

施加力矩，指定为三元素向量。

**数据类型：** `double`

### **dm/dt (kg/s)** — 质量变化率标量

一个或多个质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，指定为三元素向量，质量以该速度在体轴坐标系中吸积到机体或从机体烧蚀。

#### 依赖关系

要启用此端口，请选择 **包括质量流相对速度**。

**数据类型：** `double`
### 输出

### **Ve** — 平面地球参考系中的速度三元素向量

平面地球参考系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平面地球参考系中的位置三元素向量

平面地球参考系中的位置，返回为三元素向量。

**数据类型：** `double`

### **φ θ ψ (rad)** — 欧拉旋转角三元素向量

欧拉旋转角 [roll, pitch, yaw]，返回为三元素向量，以弧度为单位。

**数据类型：** `double`

### **DCMbe** — 坐标变换 3×3 矩阵

从平面地球轴到体轴坐标系的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 体轴坐标系中的速度三元素向量

体轴坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **ωb (rad/s)** — 体轴中的角速率三元素向量

体轴中的角速率，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **m** — 质量标量

质量，返回为标量。

#### 依赖关系

要启用此端口，请选择 **输出用于加速度计算的质量属性** 参数。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3×3 矩阵

惯性张量矩阵，返回为 3×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **输出用于加速度计算的质量属性** 参数。

**数据类型：** `double`

### **dI/dt coeff** — 惯性张量矩阵系数的变化率 3×3 矩阵

惯性张量矩阵系数的变化率，返回为 3×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **输出用于加速度计算的质量属性** 参数。

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

### **质量类型** — 质量类型 `Simple Variable`（默认）| `Fixed` | `Custom Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定（请参阅 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯性变化可自定义（请参阅 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认：** `'Simple Variable'` |

### **惯性轴中的初始位置 [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]`（默认）| 三元素向量

机体在平面地球参考系中的初始位置，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **体轴中的初始速度 [U,v,w]** — 体轴中的速度 `[0 0 0]`（默认）| 三元素向量

体轴中的初始速度，指定为三元素向量，位于体轴坐标系中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始欧拉姿态 [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]`（默认）| 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与 north-east-down (NED) 坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始机体旋转速率 [p,q,r]** — 初始机体旋转 `[0 0 0]`（默认）| 三元素向量

相对于 NED 坐标系的初始体轴角速率，指定为三元素向量，以弧度每秒为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始质量** — 初始质量 `1.0`（默认）| 标量

刚体的初始质量，指定为 double scalar。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double scalar |
| **默认：** `'1.0'` |

### **空质量** — 空质量 `0.5`（默认）| 标量

机体的空质量，指定为 double scalar。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** double scalar |
| **默认：** `'0.5'` |

### **满质量** — 机体满质量 `2.0`（默认）| 标量

机体的满质量，指定为 double scalar。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** double scalar |
| **默认：** `'2.0'` |

### **惯性** — 惯性 `eye(3)`（默认）| 标量

机体的惯性，指定为 double scalar。

#### 依赖关系

要启用此参数，请将 **质量类型** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `eye(3)` | double scalar |
| **默认：** `eye(3)` |

### **空惯性** — 空惯性矩阵 `eye(3)`（默认）| 3×3 矩阵

机体空惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_e` |
| **类型：** character vector |
| **值：** `'eye(3)'` | 3×3 矩阵 |
| **默认：** `'eye(3)'` |

### **满惯性** — 机体满惯性 `2*eye(3)`（默认）| 3×3 矩阵

机体满惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_f` |
| **类型：** character vector |
| **值：** `'2*eye(3)'` | 3×3 矩阵 |
| **默认：** `'2*eye(3)'` |

### **包括质量流相对速度** — 质量流相对速度端口 `off`（默认）| `on`

选择此复选框可添加质量流相对速度端口。这是质量吸积或烧蚀时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认：** `off` |

### **输出用于加速度计算的质量属性** — 包括用于加速度的质量属性端口 `off`（默认）| `on`

选择此复选框可启用用于加速度的质量属性端口。然后可以将这些端口用作以下模块的输入：

- 6DOF Acceleration — **m** 输出端口
- 6DOF Angular Acceleration — **I** 和 **dI/dt coeff** 端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空 (`' '`)，则不分配名称。
- 状态名称仅应用于具有该名称参数的选定模块。
- 状态数必须能被状态名称数整除。
- 可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **速度：例如，{'U','v','w'}** — 速度状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **位置：例如，{'Xe','Ye','Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **机体旋转速率：例如，{'p','q','r'}** — 机体旋转状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

机体旋转速率状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **四元数：例如，{'qr','qi','qj','qk'}** — 四元数向量状态名称 `''`（默认）| 用花括号括起来的逗号分隔列表

四元数向量状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''`（默认）| character vector

质量状态名称，指定为 character vector。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector |
| **值：** `''` | character vector |
| **默认：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2025a：6DOF 运动方程模块加速度端口已移除

由于移除了加速度端口，对于 Simple Variable Mass 6DOF (Quaternion)，**包括惯性加速度** 参数已替换为 **输出用于加速度计算的质量属性**。

与此变化相关，模块参数和输出端口已更改：

| 模块 | 端口 | 参数 |
| --- | --- | --- |
| Simple Variable Mass 6DOF (Quaternion) | - dωb/dt 已移除 - Abb 已移除 - Abe 已移除 | - **表示** 已移除 - **四元数归一化增益** 已移除 |

由于这些变化，模块输出维度已从 2D 行向量（例如 2×*N* 向量）更改为 1D 向量 *N*。*N* 是元素数。

## 描述

实现相对于体轴的简单可变质量六自由度运动方程的四元数表示

Simple Variable Mass 6DOF (Quaternion) 实现相对于体轴的简单可变质量六自由度运动方程的四元数表示。

关于坐标系和平移动力学的描述，请参阅 Simple Variable Mass 6DOF (Euler Angles) 模块的描述。Aerospace Blockset™ 使用按标量在前约定定义的四元数。有关四元数向量变化率积分的详细信息，请参阅 Algorithms。

Simple Variable Mass 6DOF (Quaternion)、6DOF (Quaternion) 和 Custom Variable Mass 6DOF (Quaternion) 模块是同一模块的替代配置。

- Simple Variable Mass 6DOF (Quaternion) — 实现相对于体轴的简单可变质量六自由度运动方程的四元数表示
- 6DOF (Quaternion) — 实现相对于体轴的六自由度运动方程的四元数表示
- Custom Variable Mass 6DOF (Quaternion) — 实现相对于体轴的自定义可变质量六自由度运动方程的四元数表示
