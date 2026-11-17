---
type: simulink-block
title: 'Orbit Follower'
family: 'algorithms'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'orbitfollower'
documentation_source_path: 'ref/orbitfollower.html'
language: zh-CN
chinese_source: worker-translation
---

# Orbit Follower

## 端口

### 输入

### **Pose** — 当前 UAV 位姿 `[x y z course]` 向量

当前 UAV 位姿，指定为 `[x y z course]` 向量。
`[x y z]` 是 UAV 在 NED 坐标（north-east-down）中的位置，以 meters 为单位指定。`course` 是地面速度与北向之间的夹角，以 radians per second 为单位。

**示例：**
`[1,1,-10,pi/4]`

**数据类型：** `single` | `double`

### **Center** — 轨道中心 `[x y z]` 向量

轨道中心，指定为 `[x y z]` 向量。`[x y z]` 是轨道中心在 NED 坐标（north-east-down）中的位置，以 meters 为单位指定。

**示例：**
`[5,5,-10]`

**数据类型：** `single` | `double`

### **Radius** — 轨道半径，正标量

轨道半径，指定为以 meters 为单位的正标量。

**示例：**
`5`

**数据类型：** `single` | `double`

### **TurnDirection** — 轨道方向，标量

轨道方向，指定为标量。正值表示从上方看为顺时针转弯。负值表示逆时针转弯。值为 `0` 时，根据 **Pose** 的输入自动确定该值。

**示例：**
`-1`

**数据类型：** `single` | `double`

### **LookaheadDistance** — 用于跟踪轨道的预瞄距离，正标量

用于跟踪轨道的预瞄距离，指定为正标量。调整此值有助于调节 UAV 跟随轨道圆的紧密程度。较小的值可改善跟踪，但可能导致路径振荡。

**示例：**
`2`

**数据类型：** `single` | `double`

### **ResetNumTurns** — 用于计数圈数的复位，数值信号

用于计数圈数的复位，指定为数值信号。任何上升信号都会触发 **NumTurns** 输出的复位。

**示例：**
`2`

#### 依赖关系

要启用此输入，请为 **External reset** 选择 `rising`。

**数据类型：** `single` | `double`

### 输出

### **LookaheadPoint** — 路径上的预瞄点，`[x y z]` 位置向量

路径上的预瞄点，以 `[x y z]` 位置向量形式返回，单位为 meters。

**数据类型：** `double`

### **DesiredCourse** — 期望航向，数值标量

期望航向，以 radians 为单位、范围在 `[-pi, pi]` 的数值标量返回。UAV 航向是速度矢量方向相对于北向的夹角，以 radians 为单位测量。对于 fixed-wing 类型 UAV，期望航向和期望偏航的值相等。

**数据类型：** `double`

### **DesiredYaw** — 期望偏航，数值标量

期望偏航，以 radians 为单位、范围在 `[-pi, pi]` 的数值标量返回。UAV 偏航是 UAV 的前向方向（与速度矢量无关）相对于北向的角度，以 radians 为单位测量。对于 fixed-wing 类型 UAV，期望航向和期望偏航的值相等。

**数据类型：** `double`

### **OrbitRadiusFlag** — 轨道半径标志 `0`（默认） | `1`

轨道半径标志，返回为 `0` 或 `1`。`0` 表示轨道半径未饱和，`1` 表示轨道半径已饱和到指定的最小轨道半径值。

**数据类型：** `uint8`

### **LookaheadDistFlag** — 预瞄距离标志 `0`（默认） | `1`

预瞄距离标志，返回为 `0` 或 `1`。`0` 表示预瞄距离未饱和，`1` 表示预瞄距离已饱和到指定的最小预瞄距离值。

**数据类型：** `uint8`

### **CrossTrackError** — 从 UAV 位置到路径的横向跟踪误差，正数值标量

从 UAV 位置到路径的横向跟踪误差，以 meters 为单位的正数值标量返回。该误差测量从 UAV 位置到路径上最近点的垂直距离。

#### 依赖关系

仅当选中 **Show CrossTrackError output port** 时，此端口可见。

**数据类型：** `double`

### **NumTurns** — UAV 完成轨道的次数，数值标量

UAV 完成轨道的次数，以数值标量返回。当 UAV 绕中心点盘旋时，此值根据指定的 **Turn Direction** 增加或减少。小数值表示圆的部分完成。如果 UAV 横向跟踪误差超过预瞄距离，圈数不会更新。

每当 **Center**、**Radius** 或 **TurnDirection** 发生变化时，**NumTurns** 会复位。您也可以使用 **ResetNumTurns** 输入。

#### 依赖关系

仅当选中 **Show NumTurns output port** 时，此端口可见。

## 参数

### **UAV type** — UAV 类型 `fixed-wing`（默认） | `multirotor`

UAV 类型，指定为 `fixed-wing` 或 `multirotor`。

此参数不可调。

### **Minimum orbit radius (m)** — 最小轨道半径 `1`（默认） | 正数值标量

最小轨道半径，指定为以 meters 为单位的正数值标量。

当轨道的 **Radius** 端口输入小于最小轨道半径时，**OrbitRadiusFlag** 返回为 `1`，并且轨道半径值指定为最小轨道半径的值。

此参数不可调。

### **Minimum lookahead distance (m)** — 最小预瞄距离 `0.1`（默认） | 正数值标量

最小预瞄距离，指定为以 meters 为单位的正数值标量。

当 **LookaheadDistance** 端口的输入小于最小预瞄距离时，**LookaheadDistFlag** 返回为 `1`，并且预瞄距离值指定为最小预瞄距离的值。

此参数不可调。

### **External reset** — 复位触发源 `none`（默认） | `rising`

选择 `rising` 以启用 **ResetNumTurns** 模块输入。

此参数不可调。

### **Show CrossTrackError output port** — 输出横向跟踪误差 `off`（默认） | `on`

从 **CrossTrackError** 端口输出横向跟踪误差。

此参数不可调。

### **Show NumTurns output port** — 输出 UAV 航点状态 `off`（默认） | `on`

从 **Status** 端口输出 UAV 航点状态。

此参数不可调。

## 所属库

UAV Toolbox / Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用 UAV 环绕关注位置

Orbit Follower 模块基于无人驾驶航空器（UAV）的当前位姿，生成用于围绕关注位置沿圆形轨道飞行的 course 和 yaw 控制。选择 **UAV type** 为 fixed-wing 或 multirotor UAV。您可以指定任意轨道中心位置、轨道半径和转弯方向。预瞄距离 **LookaheadDistance** 用于调整路径跟踪并生成 **LookaheadPoint** 输出。
