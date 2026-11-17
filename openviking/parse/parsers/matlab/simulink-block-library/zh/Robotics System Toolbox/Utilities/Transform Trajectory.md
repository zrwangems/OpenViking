---
type: simulink-block
title: 'Transform Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'transformtrajectory'
documentation_source_path: 'ref/transformtrajectory.html'
language: zh-CN
chinese_source: worker-translation
---

# Transform Trajectory

## 端口

### 输入

### **Time** — 沿轨迹的时间点 标量 | 向量

沿轨迹的时间点，指定为标量或向量。通常，当指定为标量时，该值与仿真时间同步，用于指定采样轨迹的时间点。模块在该时刻输出轨迹变量的向量。如果时间指定为向量，则模块输出一个矩阵，其中每一列对应向量的每个元素。

**数据类型：** `single` | `double`

### **T0** — 初始变换矩阵 4×4 齐次变换

初始变换矩阵，指定为 4×4 齐次变换。该函数生成一条从初始姿态 **T0** 开始到最终姿态 **TF** 的轨迹。

**示例：** `trvec2tform([1 10 -1])`

#### 依赖关系

要启用此参数，请将 **Waypoint source** 设置为 `External`。

**数据类型：** `single` | `double`

### **TF** — 最终变换矩阵 4×4 齐次变换

最终变换矩阵，指定为 4×4 齐次变换。该函数生成一条从初始姿态 **T0** 开始到最终姿态 **TF** 的轨迹。

**示例：** `trvec2tform([1 10 -1])`

#### 依赖关系

要启用此参数，请将 **Waypoint source** 设置为 `External`。

**数据类型：** `single` | `double`

### **TimeInterval** — 轨迹的开始和结束时间 二元素向量

轨迹的开始和结束时间，指定为二元素向量。

**示例：** `[0 10]`

#### 依赖关系

要启用此参数，请将 **Waypoint source** 设置为 `External`。

**数据类型：** `single` | `double`

### **TSTime** — 时间缩放时间点 标量 | *p* 元素向量

时间缩放时间点，指定为标量或 *p* 元素向量，其中 *p* 是时间缩放的点数。默认情况下，时间缩放是跨越 **TimeInterval** 的线性时间缩放。在 **TimeScaling** 中指定实际的时间缩放值。

如果 **Time** 输入指定的时间不在这些点指定的范围内，则使用插值来找到正确的缩放时间。

#### 依赖关系

要启用此参数，请选中 **Use custom time scaling** 复选框并将 **Parameter source** 设置为 `External`。

要指定标量，**Time** 输入必须为标量。

**数据类型：** `single` | `double`

### **TimeScaling** — 时间缩放向量及其前两阶导数 三元素向量 | 3×*p* 矩阵

时间缩放向量及其前两阶导数，指定为三元素向量或 3×*p* 矩阵，其中 *m* 是 **TSTime** 的长度。默认情况下，时间缩放是跨越 **TimeInterval** 的线性时间缩放。

对于非线性时间缩放，在第一行指定时间点的值。第二行和第三行分别是时间点的速度和加速度。例如，要以线性速度沿路径到达中点，然后跳到终点，时间缩放为：

```
s(1,:) = [0 0.25 0.5 1 1 1] % Position
s(2,:) = [1    1   1 0 0 0] % Velocity
s(3,:) = [0    0   0 0 0 0] % Acceleration
```

#### 依赖关系

要启用此参数，请选中 **Use custom time scaling** 复选框并将 **Parameter source** 设置为 `External`。

要指定三元素向量，**Time** 和 **TSTime** 输入必须为标量。

**数据类型：** `single` | `double`
### 输出

### **tform** — 齐次变换矩阵 4×4×*m* 齐次矩阵数组

齐次变换矩阵，返回为 4×4×*m* 齐次矩阵数组，其中 *m* 是输入到 **Time** 的点数。

### **vel** — 变换速度 6×*m* 矩阵

变换速度，返回为 6×*m* 矩阵，其中
*m* 是输入到 **Time** 的点数。
向量的每一行是变换的角速度和线速度，表示为
`[wx wy wz vx vy vz]`。*w* 表示角
速度，*v* 表示线速度。

### **alpha** — 变换加速度 6×*m* 矩阵

变换速度，返回为 6×*m* 矩阵，其中
*m* 是输入到 **Time** 的点数。
向量的每一行是变换的角加速度和线加速度，表示为
`[alphax alphay alphaz ax ay az]`。*alpha*
表示角加速度，*a* 表示线
加速度。

## 参数

### **Waypoint source** — 路点来源 `Internal`（默认）| `External`

指定 `External` 以将 **Waypoints**
和 **Time points** 参数指定为模块输入，而不是模块
参数。

### **Initial transform** — 初始变换矩阵 `trvec2tform([1 10 -1])`（默认）| 4×4 齐次变换

初始变换矩阵，指定为 4×4 齐次变换。该
函数生成一条从 **Initial
transform** 开始并到达 **Final transform** 的轨迹。

**数据类型：** `single` | `double`

### **Final transform** — 最终变换矩阵 `eul2tform([0 pi pi/2])`（默认）| 4×4 齐次变换

最终变换矩阵，指定为 4×4 齐次变换。该
函数生成一条从 **Initial
transform** 开始并到达 **Final transform** 的轨迹。

**数据类型：** `single` | `double`

### **Time interval** — 轨迹的开始和结束时间 `[2 3]` | 二元素向量

轨迹的开始和结束时间，指定为以
秒为单位的二元素向量。

**数据类型：** `single` | `double`

### **Use custom time scaling** — 启用自定义时间缩放 `off`（默认）| `on`

启用以使用
**Parameter Source**、**Time scaling time** 和
**Time scaling values** 参数为轨迹指定自定义时间缩放。

### **Parameter source** — 路点来源 `Internal`（默认）| `External`

指定 `External` 以将 **Time scaling
time** 和 **Time scaling values** 参数指定为模块
输入，而不是模块参数。

#### 依赖关系

要启用此参数，请选中 **Use custom time scaling**
复选框。

### **Time scaling time** — 时间缩放时间点 `2:0.1:3`（默认）| 标量 | *p* 元素向量

时间缩放时间点，指定为标量或 *p* 元素
向量，其中 *p* 是时间缩放的点数。默认情况下，
时间缩放是跨越 **Time
interval** 的线性时间缩放。在 **Time scaling
values** 中指定实际的时间缩放值。

如果 **Time** 输入指定的时间不在这些
点所指定的时间内，则使用插值来找到正确的时间缩放。

#### 依赖关系

要启用此参数，请选中 **Use custom time scaling**
复选框。

要指定标量，**Time** 输入必须是标量。

**数据类型：** `single` | `double`

### **Time scaling values** — 时间缩放向量及其前两阶导数 `[0:0.1:1; ones(1,11); zeros(1,11)]`（默认）| 三元素向量 | 3×*m* 矩阵

时间缩放向量及其前两阶导数，指定为三元素
向量或 3×*p* 矩阵，其中 *p* 是
**Time scaling time** 的长度。默认情况下，时间缩放是跨越 **Time
interval** 的线性时间缩放。

对于非线性时间缩放，在第一行中指定时间点的值。
第二行和第三行分别是时间点的速度和加速度。
例如，要以线性速度沿路径到达中点，
然后跳到终点，时间缩放
为：

```
s(1,:) = [0 0.25 0.5 1 1 1] % Position
s(2,:) = [1    1   1 0 0 0] % Velocity
s(3,:) = [0    0   0 0 0 0] % Acceleration
```

#### 依赖关系

要启用此参数，请选中 **Use custom time scaling** 复选框。

要指定三元素向量，**Time** 和 **TSTime** 输入必须为标量。

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，后续仿真将复用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否

## 所属库

Robotics System Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

生成两个齐次变换之间的轨迹

Transform Trajectory 模块在两个齐次变换矩阵之间生成插值轨迹。该模块在 **Time** 输入给定的时刻输出变换，**Time** 输入可以是标量或向量。

该轨迹使用四元数球面线性插值（SLERP）计算旋转，使用线性插值计算平移。此方法可找到变换的位置和旋转之间的最短路径。选中 **Use custom time scaling** 复选框可使用自定义时间缩放计算轨迹。该模块默认使用线性时间缩放。

初始值和最终值在 **Time interval** 中定义的时间段之外保持恒定。
