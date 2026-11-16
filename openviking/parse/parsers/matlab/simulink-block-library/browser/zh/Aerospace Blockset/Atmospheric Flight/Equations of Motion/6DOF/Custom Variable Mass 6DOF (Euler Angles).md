---
type: simulink-block
title: 'Custom Variable Mass 6DOF (Euler Angles)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'customvariablemass6dofeulerangles'
documentation_source_path: 'customvariablemass6dofeulerangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Variable Mass 6DOF (Euler Angles)

## 端口

### 输入

### **Fxyz** — 施加的力三元向量

施加的力，指定为三元向量。

**数据类型：** `double`

### **Mxyz** — 施加的力矩三元向量

施加的力矩，指定为三元向量。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（如果质量增加则为正，如果质量减少则为负），指定为标量。

#### 依赖关系

要启用此端口，请选择 **包含质量流相对速度**。

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

### **Vre** — 相对速度三元向量

在机体固定轴中质量被增加至或从机体减少的一个或多个相对速度，指定为三元向量。

#### 依赖关系

要启用此端口，请选择 **包含质量流相对速度**。

**数据类型：** `double`

### 输出

### **Ve** — 平地参考系中的速度三元向量

平地参考系中的速度，返回为三元向量。

**数据类型：** `double`

### **Xe** — 平地参考系中的位置三元向量

平地参考系中的位置，返回为三元向量。

**数据类型：** `double`

### **φ θ ψ (rad)** — Euler 旋转角三元向量

Euler 旋转角 [roll, pitch, yaw]，返回为三元向量，以弧度为单位。

**数据类型：** `double`

### **DCMbe** — 坐标变换 3×3 矩阵

从平地轴到机体固定轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 机体固定系中的速度三元向量

机体固定系中的速度，返回为三元向量。

**数据类型：** `double`

### **ωb (rad/s)** — 机体固定轴中的角速率三元向量

机体固定轴中的角速率，返回为三元向量，以弧度每秒为单位。

**数据类型：** `double`

## 参数

### 主

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

### **质量类型** — 质量类型 `Custom Variable` (默认) | `Simple Variable` | `Fixed`

质量类型，按以下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

`Custom Variable` 选择符合前述运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Custom Variable'` |

### **惯性轴中的初始位置 [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]` (默认) | 三元向量

机体在平地参考系中的初始位置，指定为三元向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元向量 |
| **默认：** `'[0 0 0]'` |

### **机体轴中的初始速度 [U,v,w]** — 机体轴中的速度 `[0 0 0]` (默认) | 三元向量

在机体固定坐标系中，机体轴中的初始速度，指定为三元向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元向量 |
| **默认：** `'[0 0 0]'` |

### **初始 Euler 姿态 [roll, pitch, yaw]** — 初始 Euler 姿态 `[0 0 0]` (默认) | 三元向量

初始 Euler 姿态角 [roll, pitch, yaw]，指定为三元向量，以弧度为单位。Euler 旋转角是机体与北-东-地（NED）坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元向量 |
| **默认：** `'[0 0 0]'` |

### **初始机体旋转速率 [p,q,r]** — 初始机体旋转 `[0 0 0]` (默认) | 三元向量

相对于 NED 坐标系的初始机体固定角速率，指定为三元向量，以弧度每秒为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元向量 |
| **默认：** `'[0 0 0]'` |

### **包含质量流相对速度** — 质量流相对速度端口 `off` (默认) | `on`

选中此复选框可添加质量流相对速度端口。这是质量被增加或减少时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅应用于带有该名称参数的选定模块。
- 状态数必须能被状态名称数整除。
- 指定的名称数可以少于状态数，但不能多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作空间中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **位置：例如，{'Xe','Ye','Ze'}** — 位置状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **速度：例如，{'U','v','w'}** — 速度状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **Euler 旋转角：例如，{'phi','theta','psi'}** — Euler 旋转状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

Euler 旋转角状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

### **机体旋转速率：例如，{'p','q','r'}** — 机体旋转状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

机体旋转速率状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2025a：移除了 6DOF 运动方程模块的加速度端口

由于移除了加速度端口，对于 Custom Variable Mass 6DOF (Euler Angles)，**包含惯性加速度** 参数已替换为 **输出用于加速度计算的质量属性**。

与此更改相关，模块参数和输出端口已更改：

| 模块 | 端口 | 参数 |
| --- | --- | --- |
| Custom Variable Mass 6DOF (Euler Angles) | - dωb/dt 已移除 - Abb 已移除 - Abe 已移除 | - **表示形式** 已移除 |

由于这些更改，模块输出维度已从二维行向量（例如 2-by-*N* 向量）更改为 1D 向量 *N*。*N* 是元素数量。

## 描述

实现自定义变质量六自由度运动方程的欧拉角表示

Custom Variable Mass 6DOF (Euler Angles) 模块实现自定义变质量六自由度运动方程的欧拉角表示。它考虑机体固定坐标系 (*Xb, Yb, Zb*) 相对于平地参考系 (*Xe, Ye, Ze*) 的旋转。有关欧拉角的详细信息，请参阅算法。

Custom Variable Mass 6DOF (Euler Angles)、6DOF (Euler Angles) 和 Simple Variable Mass 6DOF (Euler Angles) 模块是同一模块的替代配置。

- Custom Variable Mass 6DOF (Euler Angles) — 实现自定义变质量六自由度运动方程的欧拉角表示
- 6DOF (Euler Angles) — 实现六自由度运动方程的欧拉角表示
- Simple Variable Mass 6DOF (Euler Angles) — 实现简单变质量六自由度运动方程的欧拉角表示
