---
type: simulink-block
title: 'Polynomial Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Motion and Path Planning / Trajectory Generation'
documentation_page: 'polynomialtrajectory'
documentation_source_path: 'ref/polynomialtrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Polynomial Trajectory

## 端口

### 输入

### **Time** — 沿轨迹的时间点 标量 | 向量

沿轨迹的时间点，指定为标量或向量。通常，当指定为标量时，此值与仿真时间同步，并用于指定对轨迹进行采样时的时间点。模块在该时刻输出轨迹变量的向量。如果时间指定为向量，则模块输出一个矩阵，其中每一列对应于该向量的每个元素。

**数据类型：** `single` | `double`

### **Waypoints** — 沿轨迹的航点位置 *n*×*p* 矩阵

给定时间点处轨迹航点的位置，指定为 *n*×*p* 矩阵，其中 *n* 是轨迹的维度，*p* 是航点的数量。如果将 **Method** 指定为 `B-spline`，这些航点实际上定义 B-spline 凸包的控制点，但仍满足第一个和最后一个航点。

#### 依赖关系

要启用此输入，请将 **Waypoint Source** 设置为 `External`。

### **TimePoints** — 轨迹航点的时间点 由 *p* 个元素组成的向量

轨迹航点的时间点，指定为由 *p* 个元素组成的向量。

#### 依赖关系

要启用此输入，请将 **Waypoint Source** 设置为 `External`。

### **VelBC** — 航点的速度边界条件 *n*×*p* 矩阵

航点的速度边界条件，指定为 *n*×*p* 矩阵。每一行对应于轨迹中相应变量在各个 *p* 个航点处的速度。

#### 依赖关系

要启用此输入，请将 **Method** 设置为 `Cubic Polynomial` 或 `Quintic Polynomial`，并将 **Parameter Source** 设置为 `External`。

### **AccelBC** — 轨迹的加速度边界条件 *n*×*p* 矩阵

航点的加速度边界条件，指定为 *n*×*p* 矩阵。每一行对应于轨迹中相应变量在各个 *p* 个航点处的加速度。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Quintic Polynomial`，并将 **Parameter Source** 设置为 `External`。

### 输出

### **q** — 轨迹的位置 标量 | 向量 | 矩阵

轨迹的位置，指定为标量、向量或矩阵。如果为 **Time** 输入指定标量，且轨迹为 *n* 维，则输出为包含 *n* 个元素的向量。如果为 **Time** 输入指定包含 *m* 个元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qd** — 轨迹的速度 标量 | 向量 | 矩阵

轨迹的速度，指定为标量、向量或矩阵。如果为 **Time** 输入指定标量，且轨迹为 *n* 维，则输出为包含 *n* 个元素的向量。如果为 **Time** 输入指定包含 *m* 个元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qdd** — 轨迹的加速度 标量 | 向量 | 矩阵

轨迹的加速度，指定为标量、向量或矩阵。如果为 **Time** 输入指定标量，且轨迹为 *n* 维，则输出为包含 *n* 个元素的向量。如果为 **Time** 输入指定包含 *m* 个元素的向量，则输出为 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

## 参数

### **Waypoint source** — 航点的来源 `Internal` (默认) | `External`

指定 `External` 以将 **Waypoints** 和 **Time points** 参数指定为模块输入而不是模块参数。

### **Waypoints** — 沿轨迹的航点位置 *n*×*p* 矩阵

给定时间点处轨迹航点的位置，指定为 *n*×*p* 矩阵，其中 *n* 是轨迹的维度，*p* 是航点的数量。如果将 **Method** 指定为 `B-spline`，这些航点实际上定义 B-spline 凸包的控制点，但仍满足第一个和最后一个航点。

#### 依赖关系

要在模块掩码中指定此参数，请将 **Waypoint Source** 设置为 `Internal`。

### **Time points** — 轨迹航点的时间点 由 *p* 个元素组成的向量

轨迹航点的时间点，指定为由 *p* 个元素组成的向量，其中 *p* 是航点的数量。

#### 依赖关系

要在模块掩码中指定此参数，请将 **Waypoint Source** 设置为 `Internal`。

### **Method** — 轨迹生成方法 `Cubic Polynomial` (默认) | `Quintic Polynomial` | `B-Spline`

轨迹生成方法，指定为 `Cubic Polynomial`、`Quintic Polynomial` 或 `B-Spline`。

### **Parameter source** — 航点的来源 `Internal` (默认) | `External`

指定 `External` 以将 **Velocity boundary conditions** 和 **Acceleration boundary conditions** 参数指定为模块输入而不是模块参数。

### **Velocity boundary conditions** — 航点的速度边界条件 `zeroes(2,5)` (默认) | *n*×*p* 矩阵

航点的速度边界条件，指定为 *n*×*p* 矩阵。每一行对应于轨迹中相应变量在各个 *p* 个航点处的速度。

#### 依赖关系

要启用此输入，请将 **Method** 设置为 `Cubic Polynomial` 或 `Quintic Polynomial`。

### **Acceleration boundary conditions** — 轨迹的加速度边界条件 *n*×*p* 矩阵

航点的加速度边界条件，指定为 *n*×*p* 矩阵。每一行对应于轨迹中相应变量在各个 *p* 个航点处的加速度。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Quintic Polynomial`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。只要模型不发生变化，后续仿真就会复用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

## 所属库

Robotics System Toolbox / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

生成穿过航点的多项式轨迹

Polynomial Trajectory 模块生成轨迹，以在给定时间点使用三次、五次或 B-spline 多项式穿过航点。该模块基于 **Time** 输入输出用于实现此轨迹的位置、速度和加速度。对于 B-spline 多项式，航点实际上定义 B-spline 凸包的控制点，而不是实际航点，但仍满足第一个和最后一个航点。

在 **Time points** 定义的时间段之外，初始值和最终值保持不变。
