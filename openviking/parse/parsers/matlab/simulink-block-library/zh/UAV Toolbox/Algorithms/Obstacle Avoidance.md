---
type: simulink-block
title: 'Obstacle Avoidance'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'obstacleavoidance'
documentation_source_path: 'ref/obstacleavoidance.html'
language: zh-CN
chinese_source: worker-translation
---

# Obstacle Avoidance

## 端口
```yaml
ports:
- name: Position
  summary: 无人机位置向量
  direction: input
  data_types: double
- name: Orientation
  summary: 无人机姿态向量
  direction: input
  data_types: double
- name: ObstaclePoints
  summary: 障碍物位置矩阵
  direction: input
  data_types: double
- name: TargetPostion
  summary: 目标位置向量
  direction: input
  data_types: double
- name: DesiredDirection
  summary: 期望方向向量
  direction: output
  data_types: double
- name: DesiredYaw
  summary: 期望偏航角标量
  direction: output
  data_types: double
- name: Status
  summary: 无障碍方向的状态 0 | 1 | 2 | 3
  direction: output
  data_types: uint8
```

### 输入

### **Position** — 无人机位置向量

无人机的位置，指定为形式为 `[x; y;
z]` 的向量。`x`、`y` 和 `z` 定义无人机在任意右手坐标系（如 NED 和 ENU）中的 xyz 位置。单位为米。

**示例：**
`[1; 1; 1]`

**数据类型：** `double`

### **Orientation** — 无人机姿态向量

无人机在任意右手坐标系（如 NED 和 ENU）中的姿态，指定为形式为 `[w;
x; y;
z]` 的四元数向量。

**示例：** `[1; 0; 0; 0]`

**数据类型：** `double`

### **ObstaclePoints** — 障碍物位置矩阵

障碍物点位置，指定为 *N*×3 矩阵，每行形式为 `[x
y
z]`。`x`、`y` 和 `z` 定义障碍物点在距离传感器参考坐标系中的 xyz 位置。*N* 为障碍物点的数量。单位为米。

您可以使用传感器（如 UAV Scenario Lidar）获取障碍物点，该传感器将障碍物点输出为点云数据。

**示例：** `[1 1 1; 2 2 2]`

**数据类型：** `double`

### **TargetPostion** — 目标位置向量

目标的位置，指定为形式为 `[x; y;
z]` 的向量。`x`、`y` 和 `z` 定义目标在任意右手坐标系（如 NED 和 ENU）中的 xyz 位置。单位为米。

**示例：** `[2; 3; 4]`

**数据类型：** `double`
### 输出

### **DesiredDirection** — 期望方向向量

期望方向，返回为形式为 `[x; y;
z]` 的单位向量。`x`、`y` 和 `z` 定义在位置输入中指定的右手坐标系中的期望方向。单位为米。

**数据类型：** `double`

### **DesiredYaw** — 期望偏航角标量

在位置输入中指定的右手坐标系中的期望偏航角，返回为数值标量，单位为弧度，范围为 `[-pi,
pi]`。

**数据类型：** `double`

### **Status** — 无障碍方向的状态 `0` | `1` | `2` | `3`

无障碍方向的状态，返回为 `0`、`1`、`2` 或 `3`。

- `0` — 找到无障碍方向。
- `1` — 未找到无障碍方向。
- `2` — 找到无障碍方向但接近障碍物。
- `3` — 未找到无障碍方向且接近障碍物。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Sensor range limits (m)
  summary: 距离传感器的限制 [0.2 10]（默认）| 形式为 [min max] 的向量
  group: ''
- name: Sensor horizontal field of view (deg)
  summary: 距离传感器的水平视场限制 [-60 60]（默认）| 形式为 [min max] 的向量
  group: ''
- name: Sensor vertical field of view (deg)
  summary: 距离传感器的垂直视场限制 [-30 30]（默认）| 形式为 [min max] 的向量
  group: ''
- name: Sensor location [X, Y, Z] (m)
  summary: 传感器在无人机上的安装位置 [0 0 0]（默认）| 形式为 [x y z] 的向量
  group: ''
- name: Sensor orientation [Roll, Pitch, Yaw] (deg)
  summary: 安装在无人机上的传感器姿态 [0 0 0]（默认）| 形式为 [roll pitch yaw] 的向量
  group: ''
- name: Vehicle radius (m)
  summary: Radius of UAV 1 (default) | numeric scalar
  group: ''
- name: Minimum distance to obstacle (m)
  summary: Safety distance around UAV to obstacle 1 (default) | numeric scalar
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
- name: Histogram resolution (deg)
  summary: Histogram grid resolution 5 (default) | 1 | 3 | 6 | 10 | 15 | 18 | 30 | 45 | 60
  group: ''
- name: Histogram window size
  summary: 直方图窗口大小 1（默认）| 奇数
  group: ''
- name: Histogram threshold
  summary: 用于计算直方图的阈值 1（默认）| 正整数
  group: ''
- name: Maximum age of obstacle point
  summary: Maximum age of remembered obstacle point 0 (default) | numeric scalar
  group: ''
- name: Target direction weight
  summary: 目标方向的代价函数权重 5（默认）| 数值标量
  group: ''
- name: Current direction weight
  summary: 当前方向的代价函数权重 2（默认）| 数值标量
  group: ''
- name: Previous direction weight
  summary: 前一方向的代价函数权重 2（默认）| 数值标量
  group: ''
```

#### 主

### **Sensor range limits (m)** — 距离传感器的限制 `[0.2 10]`（默认）| 形式为 `[min max]` 的向量

将距离传感器的最小和最大限制指定为形式为 `[min
max]` 的向量，值以米为单位。

**数据类型：** `double`

### **Sensor horizontal field of view (deg)** — 距离传感器的水平视场限制 `[-60 60]`（默认）| 形式为 `[min max]` 的向量

将距离传感器的最小和最大水平视场限制指定为形式为 `[min
max]` 的向量，值以度为单位。

**数据类型：** `double`

### **Sensor vertical field of view (deg)** — 距离传感器的垂直视场限制 `[-30 30]`（默认）| 形式为 `[min max]` 的向量

将距离传感器的最小和最大垂直视场限制指定为形式为 `[min
max]` 的向量，值以度为单位。

**数据类型：** `double`

### **Sensor location [X, Y, Z] (m)** — 传感器在无人机上的安装位置 `[0 0 0]`（默认）| 形式为 `[x y z]` 的向量

将传感器在无人机机体坐标系上的安装位置指定为形式为 `[x
y
z]` 的向量，值以米为单位。

无人机机体坐标系的配置为 *x* 轴正向朝前，*y* 轴正向朝右，*z* 轴正向朝下。

**数据类型：** `double`

### **Sensor orientation [Roll, Pitch, Yaw] (deg)** — 安装在无人机上的传感器姿态 `[0 0 0]`（默认）| 形式为 `[roll pitch yaw]` 的向量

将传感器在无人机机体坐标系上的姿态指定为形式为 `[roll
pitch
yaw]` 的向量，值以度为单位。

**数据类型：** `double`

### **Vehicle radius (m)** — Radius of UAV `1` (default) | numeric scalar

此尺寸定义能够外接你的飞行器的最小圆，单位为米。飞行器半径用于在计算无障碍方向时考虑飞行器尺寸。

**数据类型：** `double`

### **Minimum distance to obstacle (m)** — Safety distance around UAV to obstacle `1` (default) | numeric scalar

安全距离指定了除飞行器半径之外，飞行器与障碍物之间所计入的空间，单位为米。飞行器半径和安全距离用于计算无障碍方向。

**数据类型：** `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定是使用 `Interpreted execution` 还是 `Code generation` 来仿真模型。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，你可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为此模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中复用。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。

**可调：** 否

#### Histogram

### **Histogram resolution (deg)** — Histogram grid resolution `5` (default) | `1` | `3` | `6` | `10` | `15` | `18` | `30` | `45` | `60`

要更改直方图网格分辨率，请从列表中选择一个值。所有值均以度为单位。

### **Histogram window size** — 直方图窗口大小 `1`（默认）| 奇数

直方图窗口大小决定无障碍开口在方位角和俯仰角方向上的角度宽度。此值无单位。

**数据类型：** `uint8`

### **Histogram threshold** — 用于计算直方图的阈值 `1`（默认）| 正整数

用于计算直方图的阈值指定了直方图单元格中被视为障碍物所需的最小障碍点数量。如果某个单元格包含的障碍点少于此数量，则该单元格被视为无障碍。

**数据类型：** `uint8`

### **Maximum age of obstacle point** — Maximum age of remembered obstacle point `0` (default) | numeric scalar

以数值标量形式指定所记忆障碍点的最大年龄。此值指定要记忆这些时间步中障碍点的先前时间步数量。

**数据类型：** `double`

#### Cost

### **Target direction weight** — 目标方向的代价函数权重 `5`（默认）| 数值标量

指定朝目标方向移动的函数权重。要遵循目标方向，请将此权重设置为大于 `Current direction weight` 与 `Previous direction weight` 之和。要忽略目标方向代价，请将此权重设置为 `0`。

**数据类型：** `double`

### **Current direction weight** — 当前方向的代价函数权重 `2`（默认）| 数值标量

指定使飞行器沿当前航向方向移动的函数权重。此权重值越高，生成的路径越高效。要忽略当前方向代价，请将此权重设置为 `0`。

**数据类型：** `double`

### **Previous direction weight** — 前一方向的代价函数权重 `2`（默认）| 数值标量

指定沿先前所选转向方向移动的函数权重。此权重值越高，生成的路径越平滑。要忽略先前方向代价，请将此权重设置为 `0`。

**数据类型：** `double`
## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

使用距离传感器数据和目标位置计算无障碍方向

Obstacle Avoidance 模块使用距离传感器数据和目标位置计算无障碍方向。
