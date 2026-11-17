---
type: simulink-block
title: 'Trapezoidal Velocity Profile Trajectory'
family: 'utilities'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'trapezoidalvelocityprofiletrajectory'
documentation_source_path: 'ref/trapezoidalvelocityprofiletrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Trapezoidal Velocity Profile Trajectory

## 端口

### 输入

### **Time** — 沿轨迹的时间点 标量 | 向量

沿轨迹的时间点，指定为标量或向量。通常，当指定为标量时，此值与仿真时间同步，并用于指定对轨迹采样的时间点。模块在该时刻输出轨迹变量的向量。如果时间指定为向量，则模块输出一个矩阵，其中每一列对应于该向量的每个元素。

**数据类型：** `single` | `double`

### **Waypoints** — 沿轨迹的航点位置 *n*×*p* 矩阵

给定时间点处轨迹航点的位置，指定为 *n*×*p* 矩阵，其中 *n* 是轨迹的维度，*p* 是航点数量。

#### 依赖关系

要启用此输入，请将 **Waypoint source** 设置为 `External`。

### **PeakVel** — 速度曲线的峰值速度 `[1;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

曲线段的峰值速度，指定为标量、向量或矩阵。此峰值速度是梯形速度曲线期间达到的最高速度。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。将 **Parameter 1** 或 **Parameter 2** 设置为 `Peak Velocity`。然后，将 **Parameter source** 设置为 `External`。

**数据类型：** `single` | `double`

### **Accel** — 速度曲线的加速度 `[2;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

速度曲线的加速度，指定为标量、向量或矩阵。此加速度定义从零速度到 **Peak velocity** 值的恒定加速度。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。将 **Parameter 1** 或 **Parameter 2** 设置为 `Acceleration`。然后，将 **Parameter source** 设置为 `External`。

**数据类型：** `single` | `double`

### **EndTime** — 轨迹段的持续时间 `[1;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

轨迹段的持续时间，指定为标量、向量或矩阵。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。将 **Parameter 1** 或 **Parameter 2** 设置为 `End Time`。然后，将 **Parameter source** 设置为 `External`。

**数据类型：** `single` | `double`

### **AccelTime** — 速度曲线加速阶段的持续时间 `[1;1]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

速度曲线加速阶段的持续时间，指定为标量、向量或矩阵。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。将 **Parameter 1** 或 **Parameter 2** 设置为 `Acceleration Time`。然后，将 **Parameter source** 设置为 `External`。

**数据类型：** `single` | `double`

### 输出

### **q** — 轨迹的位置 标量 | 向量 | 矩阵

轨迹的位置，指定为标量、向量或矩阵。如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出是包含 *n* 个元素的向量。如果为 `Time` 输入指定包含 *m* 个元素的向量，则输出是 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qd** — 轨迹的速度 标量 | 向量 | 矩阵

轨迹的速度，指定为标量、向量或矩阵。如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出是包含 *n* 个元素的向量。如果为 `Time` 输入指定包含 *m* 个元素的向量，则输出是 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

### **qdd** — 轨迹的加速度 标量 | 向量 | 矩阵

轨迹的加速度，指定为标量、向量或矩阵。如果为 `Time` 输入指定标量且轨迹为 *n* 维，则输出是包含 *n* 个元素的向量。如果为 `Time` 输入指定包含 *m* 个元素的向量，则输出是 *n*×*m* 矩阵。

**数据类型：** `single` | `double`

## 参数

### **Waypoint source** — 航点的来源 `Internal` (默认) | `External`

指定 `External` 可将 **Waypoints** 和 **Time points** 参数指定为模块输入，而不是模块参数。

### **Waypoints** — 沿轨迹的航点位置 *n*×*p* 矩阵

给定时间点处轨迹航点的位置，指定为 *n*×*p* 矩阵，其中 *n* 是轨迹的维度，*p* 是航点数量。

### **Number of parameters** — 速度曲线参数的数量 `0` (默认) | `1` | `2`

速度曲线参数的数量，指定为 `0`、`1` 或 `2`。增大此值会添加 **Parameter 1** 和 **Parameter 2**，用于指定速度曲线的参数。

### **Parameter 1** — 速度曲线参数 `Peak Velocity` | `Acceleration` | `End Time` | `Acceleration Time`

速度曲线参数，指定为 `Peak Velocity`、`Acceleration`、`End Time` 或 `Acceleration Time`。设置此参数会在封装中创建一个参数，并以该值作为其名称。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。

如果 **Parameter Source** 设置为 `Internal`，则此参数会在封装中创建一个以该值作为名称的参数。

如果 **Parameter Source** 设置为 `External`，则此参数会基于该值创建一个输入端口。

### **Parameter 2** — 速度曲线参数 `Peak Velocity` | `Acceleration` | `End Time` | `Acceleration Time`

速度曲线参数，指定为 `Peak Velocity`、`Acceleration`、`End Time` 或 `Acceleration Time`。设置此参数会在封装中创建一个参数，并以该值作为其名称。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `2`。

如果 **Parameter Source** 设置为 `Internal`，则此参数会在封装中创建一个以该值作为名称的参数。

如果 **Parameter Source** 设置为 `External`，则此参数会基于该值创建一个输入端口。

### **Parameter source** — 航点的来源 `Internal` (默认) | `External`

指定 `External` 可将速度曲线参数指定为模块输入，而不是模块参数。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。

### **Peak velocity** — 速度曲线的峰值速度 `[1;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

曲线段的峰值速度，指定为标量、向量或矩阵。此峰值速度是梯形速度曲线期间达到的最高速度。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。然后，将 **Parameter 1** 或 **Parameter 2** 设置为 `Peak Velocity`。

**数据类型：** `single` | `double`

### **Acceleration** — 速度曲线的加速度 `[2;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

速度曲线的加速度，指定为标量、向量或矩阵。此加速度定义从零速度到 **Peak velocity** 值的恒定加速度。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。然后，将 **Parameter 1** 或 **Parameter 2** 设置为 `Acceleration`。

**数据类型：** `single` | `double`

### **End time** — 轨迹段的持续时间 `[1;2]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

轨迹段的持续时间，指定为标量、向量或矩阵。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。然后，将 **Parameter 1** 或 **Parameter 2** 设置为 `End Time`。

**数据类型：** `single` | `double`

### **Acceleration time** — 速度曲线加速阶段的持续时间 `[1;1]` (默认) | 标量 | *n* 元素向量 | *n*×(*p* – 1) 矩阵

速度曲线加速阶段的持续时间，指定为标量、向量或矩阵。

标量值应用于轨迹的所有元素以及所有航点之间。*n* 元素向量应用于所有航点之间轨迹的每个元素。*n*×(*p* – 1) 矩阵应用于每个航点处轨迹的每个元素。

#### 依赖关系

要启用此参数，请将 **Number of parameters** 设置为 `1` 或 `2`。然后，将 **Parameter 1** 或 **Parameter 2** 设置为 `Acceleration Time`。

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

## 所属库

Robotics System Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用梯形速度曲线生成通过多个航点的轨迹

Trapezoidal Velocity Profile Trajectory 模块生成一条通过给定航点集且遵循梯形速度曲线的轨迹。该模块基于给定航点和速度曲线参数，输出轨迹的位置、速度和加速度。
