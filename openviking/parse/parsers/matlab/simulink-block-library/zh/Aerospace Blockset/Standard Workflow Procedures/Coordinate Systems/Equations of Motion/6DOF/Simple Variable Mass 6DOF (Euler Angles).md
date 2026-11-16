---
type: simulink-block
title: 'Simple Variable Mass 6DOF (Euler Angles)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofeulerangles'
documentation_source_path: 'simplevariablemass6dofeulerangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 6DOF (Euler Angles)

## 端口

### 输入

### **Fxyz** — 施加力三元素向量

施加力，指定为三元素向量。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加力矩三元素向量

施加力矩，指定为三元素向量。

**数据类型：** `double`

### **dm/dt (kg/s)** — 质量变化率标量

一个或多个质量变化率（若质量增加则为正，若质量减少则为负），指定为标量。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，指定为三元素向量，表示在体固定轴中质量增加至物体或从物体减少时的相对速度。

#### 依赖关系

要启用此端口，请选择 **包括质量流相对速度**。

**数据类型：** `double`

### 输出

### **Ve** — 平地参考系中的速度三元素向量

在平地参考系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平地参考系中的位置三元素向量

在平地参考系中的位置，返回为三元素向量。

**数据类型：** `double`

### **φ θ ψ (rad)** — 欧拉旋转角三元素向量

欧拉旋转角 [roll, pitch, yaw]，返回为三元素向量，单位为弧度。

**数据类型：** `double`

### **DCMbe** — 坐标变换 3×3 矩阵

从平地轴到体固定轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 体固定坐标系中的速度三元素向量

体固定坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **ωb (rad/s)** — 体固定轴中的角速率三元素向量

体固定轴中的角速率，返回为三元素向量，单位为弧度每秒。

**数据类型：** `double`

### **m** — 质量标量

质量，返回为标量。

#### 依赖关系

要启用此端口，请选择 **用于加速度计算输出质量属性** 参数。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱已空。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3×3 矩阵

惯性张量矩阵，返回为 3×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **用于加速度计算输出质量属性** 参数。

**数据类型：** `double`

### **dI/dt coeff** — 惯性张量矩阵系数变化率 3×3 矩阵

惯性张量矩阵系数变化率，返回为 3×3 矩阵。

#### 依赖关系

要启用此端口，请选择 **用于加速度计算输出质量属性** 参数。

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

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认：** `Metric (MKS)` |

### **质量类型** — 质量类型 `Simple Variable` (默认) | `Fixed` | `Custom Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定（参见 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯性变化可自定义（参见 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认：** `'Simple Variable'` |

### **表示形式** — 运动方程表示形式 `Euler Angles` (默认) | `Quaternion`

运动方程表示形式，根据下表指定。

| 表示形式 | 描述 |
| --- | --- |
| `Euler Angles` | 在运动方程中使用欧拉角。 |
| `Quaternion` | 在运动方程中使用四元数。 |

`Euler Angles` 选择符合算法中的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `rep` |
| **类型：** character vector |
| **值：** `Euler Angles` | `Quaternion` |
| **默认：** `'Euler Angles'` |

### **惯性轴中的初始位置 [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]` (默认) | 三元素向量

物体在平地参考系中的初始位置，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **体轴中的初始速度 [U,v,w]** — 体轴中的速度 `[0 0 0]` (默认) | 三元素向量

体轴中的初始速度，指定为三元素向量，在体固定坐标系中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始欧拉姿态 [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]` (默认) | 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，单位为弧度。欧拉旋转角是体坐标系与北-东-下 (NED) 坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始体旋转速率 [p,q,r]** — 初始体旋转 `[0 0 0]` (默认) | 三元素向量

相对于 NED 坐标系的初始体固定角速率，指定为三元素向量，单位为弧度每秒。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **初始质量** — 初始质量 `1.0` (默认) | 标量

刚体的初始质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double 标量 |
| **默认：** `'1.0'` |

### **空质量** — 空质量 `0.5` (默认) | 标量

物体的空质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** double 标量 |
| **默认：** `'0.5'` |

### **满质量** — 物体的满质量 `2.0` (默认) | 标量

物体的满质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** double 标量 |
| **默认：** `'2.0'` |

### **空惯性** — 空惯性矩阵 `eye(3)` (默认) | 3×3 矩阵

物体空惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_e` |
| **类型：** character vector |
| **值：** `'eye(3)'` | 3×3 矩阵 |
| **默认：** `'eye(3)'` |

### **满惯性** — 物体的满惯性 `2*eye(3)` (默认) | 3×3 矩阵

物体满惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_f` |
| **类型：** character vector |
| **值：** `'2*eye(3)'` | 3×3 矩阵 |
| **默认：** `'2*eye(3)'` |

### **包括质量流相对速度** — 质量流相对速度端口 `off` (默认) | `on`

选中此复选框可添加质量流相对速度端口。这是质量增加或减少时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认：** `off` |

### **用于加速度计算输出质量属性** — 包含用于加速度的质量属性端口 `off` (默认) | `on`

选中此复选框可启用用于加速度的质量属性端口。然后可以将这些端口用作以下模块的输入：

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
- 要为多个状态分配名称，请输入用大括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅应用于具有该名称参数的所选模块。
- 状态数必须能被状态名称数整除。
- 可以指定的名称数少于状态数，但不能多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **位置：例如，{'Xe','Ye','Ze'}** — 位置状态名称 `''` (默认) | 用大括号括起来的逗号分隔列表

位置状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **速度：例如，{'U','v','w'}** — 速度状态名称 `''` (默认) | 用大括号括起来的逗号分隔列表

速度状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **欧拉旋转角：例如，{'phi','theta','psi'}** — 欧拉旋转状态名称 `''` (默认) | 用大括号括起来的逗号分隔列表

欧拉旋转角状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **体旋转速率：例如，{'p','q','r'}** — 体旋转状态名称 `''` (默认) | 用大括号括起来的逗号分隔列表

体旋转速率状态名称，指定为用大括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用大括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''` (默认) | character vector

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

### R2025a: 6DOF equations of motion block acceleration ports removed

由于移除了加速度端口，对于 Simple Variable Mass 6DOF (Euler Angles)，**包括惯性加速度** 参数已替换为 **用于加速度计算输出质量属性**。

与此更改相关，模块参数和输出端口已更改：

| 模块 | 端口 | 参数 |
| --- | --- | --- |
| Simple Variable Mass 6DOF (Euler Angles) | - 移除了 dωb/dt - 移除了 Abb - 移除了 Abe | - 移除了 **表示形式** |

由于这些更改，模块输出维度已从 2D 行向量（例如 2-by-*N* 向量）更改为 1D 向量 *N*。*N* 是元素数量。

## 描述

实现简单变质量的六自由度运动方程的欧拉角表示

Simple Variable Mass 6DOF (Euler Angles) 模块考虑体固定坐标系 (*Xb*, *Yb*, *Zb*) 相对于平地参考系 (*Xe*, *Ye*, *Ze*) 的旋转。

有关坐标系和平移动力学的描述，请参阅 Simple Variable Mass 6DOF (Euler Angles) 模块的描述。有关体固定坐标系的更多信息，请参阅算法。

Simple Variable Mass 6DOF (Euler Angles)、6DOF (Euler Angles) 和 Custom Variable Mass 6DOF (Euler Angles) 模块是同一模块的替代配置。

- Simple Variable Mass 6DOF (Euler Angles) — 实现简单变质量的六自由度运动方程的欧拉角表示
- 6DOF (Euler Angles) — 实现六自由度运动方程的欧拉角表示
- Custom Variable Mass 6DOF (Euler Angles) — 实现自定义变质量的六自由度运动方程的欧拉角表示
