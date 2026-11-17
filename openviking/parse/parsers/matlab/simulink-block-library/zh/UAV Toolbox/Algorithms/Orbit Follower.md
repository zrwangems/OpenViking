---
type: simulink-block
title: 'Orbit Follower'
family: 'uav'
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
```yaml
ports:
- name: Pose
  summary: 当前无人机位姿 [x y z course] 向量
  direction: input
  data_types: single | double
- name: Center
  summary: 环绕中心 [x y z] 向量
  direction: input
  data_types: single | double
- name: Radius
  summary: 环绕半径 正标量
  direction: input
  data_types: single | double
- name: TurnDirection
  summary: 环绕方向 标量
  direction: input
  data_types: single | double
- name: LookaheadDistance
  summary: 跟踪环绕的前视距离 正标量
  direction: input
  data_types: single | double
- name: ResetNumTurns
  summary: 圈数计数复位 数值信号
  direction: input
  data_types: single | double
- name: LookaheadPoint
  summary: 路径上的前视点 [x y z] 位置向量
  direction: output
  data_types: double
- name: DesiredCourse
  summary: 期望航向 数值标量
  direction: output
  data_types: double
- name: DesiredYaw
  summary: 期望偏航 数值标量
  direction: output
  data_types: double
- name: OrbitRadiusFlag
  summary: 环绕半径标志 0（默认）| 1
  direction: output
  data_types: uint8
- name: LookaheadDistFlag
  summary: 前视距离标志 0（默认）| 1
  direction: output
  data_types: uint8
- name: CrossTrackError
  summary: 从无人机位置到路径的横向跟踪误差 正数值标量
  direction: output
  data_types: double
- name: NumTurns
  summary: 无人机完成环绕轨道的次数 数值标量
  direction: output
```

### 输入

### **Pose** — 当前无人机位姿 `[x y z course]` 向量

当前无人机位姿，指定为 `[x y z course]` 向量。
`[x y z]` 是无人机在 NED 坐标系（北-东-地）中的位置，单位为米。`course` 是地面速度与北向之间的夹角，单位为弧度每秒。

**示例：**
`[1,1,-10,pi/4]`

**数据类型：** `single` | `double`

### **Center** — 环绕中心 `[x y z]` 向量

环绕中心，指定为 `[x y z]` 向量。`[x y z]` 是环绕中心在 NED 坐标系（北-东-地）中的位置，单位为米。

**示例：**
`[5,5,-10]`

**数据类型：** `single` | `double`

### **Radius** — 环绕半径 正标量

环绕半径，指定为正标量，单位为米。

**示例：**
`5`

**数据类型：** `single` | `double`

### **TurnDirection** — 环绕方向 标量

环绕方向，指定为标量。正值表示从上方观察时的顺时针转向。负值表示逆时针转向。值为 `0` 时根据 **Pose** 的输入自动确定该值。

**示例：**
`-1`

**数据类型：** `single` | `double`

### **LookaheadDistance** — 跟踪环绕的前视距离 正标量

跟踪环绕的前视距离，指定为正标量。调整此值有助于调节无人机跟随环绕圆的紧密程度。较小的值可改善跟踪效果，但可能导致路径振荡。

**示例：**
`2`

**数据类型：** `single` | `double`

### **ResetNumTurns** — 圈数计数复位 数值信号

圈数计数复位，指定为数值信号。任何上升信号都会触发 **NumTurns** 输出的复位。

**示例：**
`2`

#### 依赖

要启用此输入，请为 **External reset** 选择 `rising`。

**数据类型：** `single` | `double`
### 输出

### **LookaheadPoint** — 路径上的前视点 `[x y z]` 位置向量

路径上的前视点，返回为 `[x y z]` 位置向量，单位为米。

**数据类型：** `double`

### **DesiredCourse** — 期望航向 数值标量

期望航向，返回为数值标量，单位为弧度，范围为 `[-pi, pi]`。无人机航向是速度矢量方向相对于北向的夹角，以弧度为单位。对于固定翼型无人机，期望航向和期望偏航的值相等。

**数据类型：** `double`

### **DesiredYaw** — 期望偏航 数值标量

期望偏航，返回为数值标量，单位为弧度，范围为 `[-pi, pi]`。无人机偏航是无人机的前进方向（与速度矢量无关）相对于北向的夹角，以弧度为单位。对于固定翼型无人机，期望航向和期望偏航的值相等。

**数据类型：** `double`

### **OrbitRadiusFlag** — 环绕半径标志 `0`（默认）| `1`

环绕半径标志，返回为 `0` 或 `1`。
`0` 表示环绕半径未饱和，`1` 表示环绕半径已饱和至指定的最小环绕半径值。

**数据类型：** `uint8`

### **LookaheadDistFlag** — 前视距离标志 `0`（默认）| `1`

前视距离标志，返回为 `0` 或 `1`。
`0` 表示前视距离未饱和，`1` 表示前视距离已饱和至指定的最小前视距离值。

**数据类型：** `uint8`

### **CrossTrackError** — 从无人机位置到路径的横向跟踪误差 正数值标量

从无人机位置到路径的横向跟踪误差，返回为正数值标量，单位为米。该误差测量从无人机位置到路径上最近点的垂直距离。

#### 依赖

仅当选中 **Show CrossTrackError output port** 时，此端口才可见。

**数据类型：** `double`

### **NumTurns** — 无人机完成环绕轨道的次数 数值标量

无人机完成环绕轨道的次数，以数值标量形式返回。当无人机绕中心点飞行时，该值根据指定的 **Turn Direction** 增加或减少。小数值表示圆的部分完成。如果无人机的横向偏差超过前视距离，环绕次数不会更新。

每当 **Center**、**Radius** 或 **TurnDirection** 发生变化时，**NumTurns** 会被重置。你也可以使用 **ResetNumTurns** 输入。

#### 依赖关系

仅当选中 **Show NumTurns output port** 时，此端口才可见。
## 参数
```yaml
parameters:
- name: UAV type
  summary: 无人机类型 fixed-wing（默认）| multirotor
  group: ''
- name: Minimum orbit radius (m)
  summary: 最小环绕半径 1（默认）| 正数值标量
  group: ''
- name: Minimum lookahead distance (m)
  summary: 最小前视距离 0.1（默认）| 正数值标量
  group: ''
- name: External reset
  summary: 重置触发源 none（默认）| rising
  group: ''
- name: Show CrossTrackError output port
  summary: 输出横向偏差 off（默认）| on
  group: ''
- name: Show NumTurns output port
  summary: 输出无人机航点状态 off（默认）| on
  group: ''
```

### **UAV type** — 无人机类型 `fixed-wing`（默认）| `multirotor`

无人机类型，指定为 `fixed-wing` 或 `multirotor`。

此参数不可调。

### **Minimum orbit radius (m)** — 最小环绕半径 `1`（默认）| 正数值标量

最小环绕半径，指定为以米为单位的正数值标量。

当输入到环绕 **Radius** 端口的值小于最小环绕半径时，**OrbitRadiusFlag** 返回为 `1`，且环绕半径值被指定为最小环绕半径的值。

此参数不可调。

### **Minimum lookahead distance (m)** — 最小前视距离 `0.1`（默认）| 正数值标量

最小前视距离，指定为以米为单位的正数值标量。

当输入到 **LookaheadDistance** 端口的值小于最小前视距离时，**LookaheadDistFlag** 返回为 `1`，且前视距离值被指定为最小前视距离的值。

此参数不可调。

### **External reset** — 重置触发源 `none`（默认）| `rising`

选择 `rising` 以启用 **ResetNumTurns** 模块输入。

此参数不可调。

### **Show CrossTrackError output port** — 输出横向偏差 `off`（默认）| `on`

从 **CrossTrackError** 端口输出横向偏差。

此参数不可调。

### **Show NumTurns output port** — 输出无人机航点状态 `off`（默认）| `on`

从 **Status** 端口输出无人机航点状态。

此参数不可调。
## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

使用无人机环绕关注位置

Orbit Follower 模块根据无人飞行器（UAV）的当前位姿，生成用于围绕关注位置沿圆形轨道飞行的航向和偏航控制。选择固定翼或多旋翼无人机的 **UAV type**。你可以指定任意环绕中心位置、环绕半径和转向方向。前视距离 **LookaheadDistance** 用于调整路径跟踪并生成 **LookaheadPoint** 输出。
