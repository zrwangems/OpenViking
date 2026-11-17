---
type: simulink-block
title: 'Obstacle Avoidance'
family: 'algorithms'
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

### 输入

### **Position** — UAV 的位置向量

UAV 的位置，指定为 `[x; y; z]` 形式的向量。`x`、`y` 和 `z` 定义 UAV 在任意右手坐标系（例如 NED 和 ENU）中的 xyz 位置。单位为 meters。

**示例:** `[1; 1; 1]`

**数据类型:** `double`

### **Orientation** — UAV 的姿态向量

UAV 的姿态，位于任意右手坐标系（例如 NED 和 ENU）中，指定为 `[w; x; y; z]` 形式的四元数向量。

**示例:** `[1; 0; 0; 0]`

**数据类型:** `double`

### **ObstaclePoints** — 障碍物的位置矩阵

障碍物点位置，指定为 *N*×3 矩阵，其行形式为 `[x y z]`。`x`、`y` 和 `z` 定义障碍物点在测距传感器参考坐标系中的 xyz 位置。*N* 是障碍物点的数量。单位为 meters。

你可以使用诸如 UAV Scenario Lidar 之类的传感器获取障碍物点，该传感器将障碍物点输出为点云数据。

**示例:** `[1 1 1; 2 2 2]`

**数据类型:** `double`

### **TargetPostion** — 目标的位置向量

目标的位置，指定为 `[x; y; z]` 形式的向量。`x`、`y` 和 `z` 定义目标在任意右手坐标系（例如 NED 和 ENU）中的 xyz 位置。单位为 meters。

**示例:** `[2; 3; 4]`

**数据类型:** `double`

### 输出

### **DesiredDirection** — 期望方向向量

期望方向，返回为 `[x; y; z]` 形式的单位向量。`x`、`y` 和 `z` 定义在 Position 输入中指定的右手坐标系中的期望方向。单位为 meters。

**数据类型:** `double`

### **DesiredYaw** — 期望偏航角标量

期望偏航角，位于你在 Position 输入中指定的右手坐标系中，返回为以 radians 为单位的数值标量，范围为 `[-pi, pi]`。

**数据类型:** `double`

### **Status** — 无障碍方向的状态 `0` | `1` | `2` | `3`

无障碍方向的状态，返回为 `0`、`1`、`2` 或 `3`。

- `0` — 找到无障碍方向。
- `1` — 未找到无障碍方向。
- `2` — 找到无障碍方向，但接近障碍物。
- `3` — 未找到无障碍方向，且接近障碍物。

**数据类型:** `uint8`

## 参数

#### 主要

### **Sensor range limits (m)** — 测距传感器的限制 `[0.2 10]` (默认) | `[min max]` 形式的向量

将测距传感器的最小和最大限制指定为 `[min max]` 形式的向量，值以 meters 为单位。

**数据类型:** `double`

### **Sensor horizontal field of view (deg)** — 测距传感器的水平视场限制 `[-60 60]` (默认) | `[min max]` 形式的向量

将测距传感器水平视场的最小和最大限制指定为 `[min max]` 形式的向量，值以 degrees 为单位。

**数据类型:** `double`

### **Sensor vertical field of view (deg)** — 测距传感器的垂直视场限制 `[-30 30]` (默认) | `[min max]` 形式的向量

将测距传感器垂直视场的最小和最大限制指定为 `[min max]` 形式的向量，值以 degrees 为单位。

**数据类型:** `double`

### **Sensor location [X, Y, Z] (m)** — 传感器在 UAV 上的安装位置 `[0 0 0]` (默认) | `[x y z]` 形式的向量

将传感器在 UAV 机体坐标系上的安装位置指定为 `[x y z]` 形式的向量，值以 meters 为单位。

UAV 机体坐标系的配置将 *x* 轴定向为前向正，将 *y* 轴定向为右向正，将 *z* 轴定向为下向正。

**数据类型:** `double`

### **Sensor orientation [Roll, Pitch, Yaw] (deg)** — 安装在 UAV 上的传感器的姿态 `[0 0 0]` (默认) | `[roll pitch yaw]` 形式的向量

将传感器在 UAV 机体坐标系上的姿态指定为 `[roll pitch yaw]` 形式的向量，值以 degrees 为单位。

**数据类型:** `double`

### **Vehicle radius (m)** — UAV 的半径 `1` (默认) | 数值标量

此维度定义可外接你的载具的最小圆，单位为 meters。在计算无障碍方向时，载具半径用于考虑载具尺寸。

**数据类型:** `double`

### **Minimum distance to obstacle (m)** — UAV 到障碍物的安全距离 `1` (默认) | 数值标量

安全距离以 meters 指定除载具半径外，在 UAV 与障碍物之间额外计入的空间。载具半径和安全距离用于计算无障碍方向。

**数据类型:** `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定是使用 `Interpreted execution` 还是 `Code generation` 来仿真模型。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，你可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为此模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 快。

**可调:** No

#### 直方图

### **Histogram resolution (deg)** — 直方图网格分辨率 `5` (默认) | `1` | `3` | `6` | `10` | `15` | `18` | `30` | `45` | `60`

要更改直方图网格分辨率，请从列表中选择一个值。所有值均以 degrees 为单位。

### **Histogram window size** — 直方图窗口大小 `1` (默认) | 奇数整数

直方图窗口大小确定无障碍开口在方位角和仰角方向上的角宽度。此值无单位。

**数据类型:** `uint8`

### **Histogram threshold** — 用于计算直方图的阈值 `1` (默认) | 正整数

用于计算直方图的阈值指定一个直方图单元中应包含的障碍物点最小数量，达到该数量才被视为障碍物。如果某个单元包含的障碍物点少于该数量，则该单元被视为无障碍。

**数据类型:** `uint8`

### **Maximum age of obstacle point** — 已记住的障碍物点的最大年龄 `0` (默认) | 数值标量

将已记住的障碍物点的最大年龄指定为数值标量。此值指定要记住来自那些时间步的障碍物点的先前时间步数。

**数据类型:** `double`

#### 成本

### **Target direction weight** — 目标方向的成本函数权重 `5` (默认) | 数值标量

指定朝向目标方向移动的函数权重。要沿目标方向行进，请将此权重设置为大于 `Current direction weight` 与 `Previous direction weight` 之和。要忽略目标方向成本，请将此权重设置为 `0`。

**数据类型:** `double`

### **Current direction weight** — 当前方向的成本函数权重 `2` (默认) | 数值标量

指定使载具沿当前航向方向移动的函数权重。此权重值越高，生成的路径越高效。要忽略当前方向成本，请将此权重设置为 `0`。

**数据类型:** `double`

### **Previous direction weight** — 先前方向的成本函数权重 `2` (默认) | 数值标量

指定沿先前选定的转向方向移动的函数权重。此权重值越高，生成的路径越平滑。要忽略先前方向成本，请将此权重设置为 `0`。

**数据类型:** `double`

## 所属库

UAV Toolbox / Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

使用测距传感器数据和目标位置计算无障碍方向

Obstacle Avoidance 模块使用测距传感器数据和目标位置计算无障碍方向。
