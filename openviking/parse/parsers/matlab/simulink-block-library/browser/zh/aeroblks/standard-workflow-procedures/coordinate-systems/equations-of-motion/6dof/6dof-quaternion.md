---
type: simulink-block
title: '6DOF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofquaternion'
documentation_source_path: '6dofquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF (Quaternion)

## 端口

### 输入

### **Fxyz(N)** — 施加的力三元素向量

施加的力，指定为机体固连轴中的三元素向量。有关坐标系的更多信息，请参阅 Body Coordinates。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加的力矩三元素向量

施加的力矩，指定为机体固连轴中的三元素向量。有关坐标系的更多信息，请参阅 Body Coordinates。

**数据类型：** `double`
### 输出

### **Ve** — 平面地球参考坐标系中的速度三元素向量

平面地球参考坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **Xe** — 平面地球参考坐标系中的位置三元素向量

平面地球参考坐标系中的位置，返回为三元素向量。

**数据类型：** `double`

### **φ θ ψ (rad)** — 欧拉旋转角三元素向量

欧拉旋转角 [roll, pitch, yaw]，定义内旋 *x*-*y*-*z* 旋转，为三元素向量，以弧度为单位。Yaw、pitch 和 roll 角使用 *z*-*y*-*x* 旋转序列应用，例如 `angle2dcm(yaw,pitch,roll,"ZYX")`。

**数据类型：** `double`

### **q** — 四元数 4-by-1 向量

四元数，表示从平面地球轴到机体固连轴的变换，返回为 4-by-1 向量。

**数据类型：** `double`

### **DCMbe** — 坐标变换 3-by-3 矩阵

从平面地球轴到机体固连轴的坐标变换，返回为 3-by-3 矩阵。

**数据类型：** `double`

### **Vb** — 机体固连坐标系中的速度三元素向量

机体固连坐标系中的速度，返回为三元素向量。

**数据类型：** `double`

### **ωb (rad/s)** — 机体固连轴中的角速率三元素向量

机体固连轴中的角速率，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **m** — 质量标量

质量，返回为标量。

#### 依赖关系

要启用此端口，请选择 **Output mass properties for acceleration computation** 参数。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3-by-3 矩阵

惯性张量矩阵，返回为 3-by-3 矩阵。

#### 依赖关系

要启用此端口，请选择 **Output mass properties for acceleration computation** 参数。

**数据类型：** `double`

## 参数

### 主要

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
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

质量类型，按下表指定。

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 质量在整个仿真过程中恒定。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind (Wind   Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性随质量率线性变化。 | - Simple Variable Mass   6DOF (Euler Angles) - Simple Variable Mass   6DOF (Quaternion) - Simple Variable Mass   6DOF Wind (Wind Angles) - Simple Variable Mass   6DOF Wind (Quaternion) - Simple Variable Mass   6DOF ECEF (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom Variable Mass   6DOF (Euler Angles) - Custom Variable Mass   6DOF (Quaternion) - Custom Variable Mass   6DOF Wind (Wind Angles) - Custom Variable Mass   6DOF Wind (Quaternion) - Custom Variable Mass   6DOF ECEF (Quaternion) |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认：** `'Fixed'` |

### **Initial position in inertial axes [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]`（默认）| 三元素向量

刚体在平面地球参考坐标系中的初始位置，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **Initial velocity in body axes [U,v,w]** — 体轴中的速度 `[0 0 0]`（默认）| 三元素向量

体轴中的初始速度，指定为三元素向量，在机体固连坐标系中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **Initial Euler orientation [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]`（默认）| 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与 north-east-down (NED) 坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始机体旋转速率 `[0 0 0]`（默认）| 三元素向量

相对于 NED 坐标系的初始机体固连角速率，指定为三元素向量，以弧度每秒为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认：** `'[0 0 0]'` |

### **Initial mass** — 初始质量 `1.0`（默认）| 标量

刚体的初始质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double scalar |
| **默认：** `'1.0'` |

### **Inertia** — 惯性 `eye(3)`（默认）| 标量

机体的惯性，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `eye(3)` | double scalar |
| **默认：** `eye(3)` |

### 状态属性

为每个状态分配唯一名称。在线性化过程中，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅适用于带名称参数的所选模块。
- 状态数量必须能被状态名称数量整除。
- 可以指定的名称数量少于状态数量，但不能多于状态数量。

  例如，在具有四个状态的系统中可以指定两个名称。第一个名称适用于前两个状态，第二个名称适用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、元胞数组或结构体。

### **Position: e.g., {'Xe','Ye','Ze'}** — 位置状态名称 `''`（默认）| 用花括号括起的逗号分隔列表

位置状态名称，指定为用花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认：** `''` |

### **Velocity: e.g., {'U','v','w'}** — 速度状态名称 `''`（默认）| 用花括号括起的逗号分隔列表

速度状态名称，指定为用花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认：** `''` |

### **Quaternion: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''`（默认）| 用花括号括起的逗号分隔列表

四元数向量状态名称，指定为用花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认：** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 机体旋转状态名称 `''`（默认）| 用花括号括起的逗号分隔列表

机体旋转速率状态名称，指定为用花括号括起的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起的逗号分隔列表 |
| **默认：** `''` |

### **Output mass properties for acceleration computation** — 包括用于加速度端口的质量属性 `off`（默认）| `on`

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

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2025a：6DOF 运动方程模块加速度端口已移除

由于移除了加速度端口，对于 6DOF (Quaternion)，**Include inertial acceleration** 参数已替换为 **Output mass properties for acceleration computation**。

与此更改相关，模块参数和输出端口已更改：

| 模块 | 端口 | 参数 |
| --- | --- | --- |
| 6DOF (Quaternion) | - dωb/dt 已移除 - Abb 已移除 - Abe 已移除 | - **Representation** 已移除 - **Gain for quaternion normalization** 已移除 |

由于这些更改，模块输出维度已从 2D 行向量（例如 2-by-*N* 向量）更改为 1D 向量 *N*。*N* 是元素数量。

## 描述

实现相对于体轴的六自由度运动方程的四元数表示

6DOF (Quaternion) 模块实现相对于体轴的六自由度运动方程的四元数表示。有关坐标系和平移动力学的描述，请参阅 6DOF (Euler Angles) 模块的模块描述。

有关四元数向量变化率积分的更多信息，请参阅 Algorithms。

6DOF (Quaternion)、Simple Variable Mass 6DOF (Quaternion) 和 Custom Variable Mass 6DOF (Quaternion) 模块是同一模块的替代配置。

- 6DOF (Quaternion) — 实现相对于体轴的六自由度运动方程的四元数表示
- Simple Variable Mass 6DOF (Quaternion) — 实现相对于体轴的简单变质量六自由度运动方程的四元数表示
- Custom Variable Mass 6DOF (Quaternion) — 实现相对于体轴的自定义变质量六自由度运动方程的四元数表示
