---
type: simulink-block
title: 'Waypoint Follower'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'waypointfollower'
documentation_source_path: 'ref/waypointfollower.html'
language: zh-CN
chinese_source: worker-translation
---

# Waypoint Follower

## 端口

### 输入

### **Pose** — 当前无人机位姿 `[x y z chi]` 向量

当前无人机位姿，指定为 `[x y z chi]` 向量。该位姿用于根据 **LookaheadDistance** 端口的输入计算前视点。`[x y z]` 是当前位置，单位为米。`chi` 是当前航向，单位为弧度。航向输入仅在航点为空时使用。无人机航向是速度矢量方向相对于北向的角度，以弧度为单位。

**示例：**
`[0.5;1.75;-2.5;pi]`

**数据类型：** `single` | `double`

### **Waypoints** — 航点集合 *n*×3 矩阵 | *n*×4 矩阵 | *n*×5 矩阵

无人机要跟随的航点集合，指定为一个矩阵，行数 *n* 等于航点数量。列数取决于 **Show Yaw input variable** 和 **Transition radius source** 参数。

矩阵的每一行前三个元素为航点序列中的 `[x y z]` 位置。

如果选中 **Show Yaw input variable**，则将期望偏航角 `yaw` 指定为向量中的第四个元素，单位为弧度。

如果未选中 **Show Yaw input variable**，且 **Transition radius source** 为 `external`，则过渡半径为向量中的第四个元素，单位为米。

如果选中 **Show Yaw input variable**，且 **Transition radius source** 为 `external`，则过渡半径为向量中的第五个元素，单位为米。

模块显示会随航点矩阵大小的变化而更新。

**数据类型：** `single` | `double`

### **LookaheadDistance** — 前视距离 正数值标量

沿路径的前视距离，指定为正数值标量，单位为米。

**数据类型：** `single` | `double`
### 输出

### **LookaheadPoint** — 路径上的前视点 `[x y z]` 位置向量

路径上的前视点，返回为 `[x y z]` 位置向量，单位为米。

**数据类型：** `single` | `double`

### **DesiredCourse** — 期望航向 数值标量

期望航向，返回为数值标量，单位为弧度，范围为 `[-pi, pi]`。无人机航向是速度矢量方向相对于北向的角度，以弧度为单位。对于固定翼型无人机，期望航向和期望偏航角的值相等。

**数据类型：** `single` | `double`

### **DesiredYaw** — 期望偏航角 数值标量

期望偏航角，返回为数值标量，单位为弧度，范围为 `[-pi, pi]`。无人机偏航角是无人机的前进方向，与速度矢量相对于北向的方向无关，以弧度为单位。期望偏航角通过对每个航点的偏航角进行线性插值计算得到。对于固定翼型无人机，期望航向和期望偏航角的值相等。

**数据类型：** `single` | `double`

### **LookaheadDistFlag** — 前视距离标志 `0`（默认）| `1`

前视距离标志，返回为 `0` 或 `1`。`0` 表示前视距离未饱和，`1` 表示前视距离已饱和至指定的最小前视距离值。

**数据类型：** `uint8`

### **CrossTrackError** — 从无人机位置到路径的横向跟踪误差 正数值标量

从无人机位置到路径的横向跟踪误差，返回为正数值标量，单位为米。该误差衡量从无人机位置到路径上最近点的垂直距离。

#### 依赖关系

仅当选中 **Show CrossTrackError output port** 时，此端口才可见。

**数据类型：** `single` | `double`

### **Status** — 航点导航状态 `0` | `1`

航点导航状态，返回为 `0` 或 `1`。当跟随器已导航完所有航点时，模块输出 `1`。否则，模块输出 `0`。

#### 依赖关系

仅当选中 **Show UAV Status output port** 时，此端口才可见。

**数据类型：** `uint8`

## 参数

### **UAV type** — 无人机类型 `fixed-wing`（默认）| `multirotor`

UAV 类型，指定为 `fixed-wing` 或 `multirotor`。

此参数不可调。

### **StartFrom** — Waypoint start behavior `first` (default) | `closest`

航点起始行为，指定为 `first` 或 `closest`。

当设置为 `first` 时，UAV 飞往航点之间的第一个路径段。如果 `Waypoints` 中输入的航点集发生变化，UAV 将从第一个路径段重新开始。

当设置为 `closest` 时，UAV 飞往航点之间最近的路径段。当航点输入发生变化时，UAV 会重新计算最近的路径段。

此参数不可调。

### **Transition radius source** — Source of transition radius `internal` (default) | `external`

过渡半径的来源，指定为 `internal` 或 `external`。如果指定为 `internal`，则每个航点的过渡半径使用模块掩码中的 **Transition radius (r)** 参数设置。如果指定为 `external`，则使用 **Waypoints** 端口的输入独立指定每个航点的过渡半径。

当 UAV 位于过渡半径内时，模块将过渡到沿航点之间的下一个路径段飞行。

此参数不可调。

### **Transition radius (r)** — 航点的过渡半径 `10`（默认）| 正数值标量

航点的过渡半径，指定为正数值标量，单位为米。

当 UAV 位于过渡半径内时，模块将过渡到沿航点之间的下一个路径段飞行。

此参数不可调。

### **Minimum lookahead distance (m)** — Minimum lookahead distance `0.1` (default) | positive numeric scalar

最小前视距离，指定为正数值标量，单位为米。

当 **LookaheadDistance** 端口的输入小于最小前视距离时，**LookaheadDistFlag** 返回为 `1`，并且前视距离值指定为最小前视距离的值。

此参数不可调。

### **Hover at last waypoint** — Lookahead point location at last waypoint `off` (default) | `on`

航点导航结束时前视点的位置。如果启用，前视点将保持静止在最后一个航点处。如果禁用，前视点将继续沿连接最后两个航点的直线路径移动。

此参数不可调。

#### 依赖关系

要启用此参数，请将 **UAV type** 设置为 `multirotor`

### **Show Yaw input variable** — 接受航点的偏航角输入 `off`（默认）| `on`

选中时接受航点的偏航角输入。如果选中，**Waypoints** 输入将接受每个航点的偏航角输入。

### **Show CrossTrackError output port** — 输出横向轨迹误差 `off`（默认）| `on`

从 **CrossTrackError** 端口输出横向轨迹误差。

此参数不可调。

### **Show UAV Status output port** — 输出无人机航点状态 `off`（默认）| `on`

从 **Status** 端口输出 UAV 航点状态。

此参数不可调。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

此参数不可调。

**Tunable:** No

## 所属库

UAV Toolbox / Algorithms

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2024b: 在最后一个航点悬停

现在，您可以通过启用 **Hover at last waypoint** 参数，将前视点配置为在最终航点保持静止。仅当您将 **UAV Type** 设置为 `multirotor` 时，此参数才可用。

## 描述

跟随 UAV 的航点

Waypoint Follower 模块生成前视点、期望航向、期望偏航角和横向偏差。该模块接受 UAV 位姿、一组航点和前视距离。

指定 **UAV type** 参数以选择您的 UAV 类型。使用 **StartFrom** 参数指定航点起始行为。指定 **Transition radius source** 参数以在统一过渡半径和每个航点的可变过渡半径之间进行选择。
