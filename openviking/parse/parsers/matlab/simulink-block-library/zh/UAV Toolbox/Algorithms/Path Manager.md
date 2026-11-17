---
type: simulink-block
title: 'Path Manager'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Algorithms'
documentation_page: 'pathmanager'
documentation_source_path: 'ref/pathmanager.html'
language: zh-CN
chinese_source: worker-translation
---

# Path Manager

## 端口
```yaml
ports:
- name: Pose
  summary: 当前无人机位姿四元素列向量
  direction: input
  data_types: single | double
- name: MissionData
  summary: 无人机任务数据 UAVPathManagerBus 总线
  direction: input
  data_types: bus
- name: IsModeDone
  summary: 判断任务点是否已执行 0（默认） | 1
  direction: input
  data_types: Boolean
- name: MissionCmd
  summary: 更改任务的命令 uint8(0)（默认）| 0 到 3 之间的 8 位无符号整数
  direction: input
  data_types: uint8
- name: Home
  summary: 无人机 home 位置 三元素列向量
  direction: input
  data_types: single | double
- name: MissionParams
  summary: 无人机任务参数 UAVPathManagerBus 总线
  direction: output
  data_types: bus
```

### 输入

### **Pose** — 当前无人机位姿四元素列向量

当前无人机位姿，指定为 `[x;y;z;courseAngle]` 的四元素列向量。
*x*、*y* 和 *z* 是无人机在当前北东地（NED）坐标系中的位置，单位为米。
*courseAngle* 指定航向角，单位为弧度，范围为 `[-pi, pi]`。

**数据类型：** `single` | `double`

### **MissionData** — 无人机任务数据 `UAVPathManagerBus` 总线

无人机任务数据，指定为 `UAVPathManagerBus` 总线。`UAVPathManagerBus` 总线具有三个总线元素 `mode`、`position` 和 `params`。

您可以使用 Constant (Simulink) 模块将任务数据指定为 *n*×1 的结构体数组，并将输出数据类型设置为 `Bus:UAVPathManagerBus`。*n* 是任务点的数量。每个结构体的字段为：

- `mode` — 任务点的模式，指定为 1 到 6 之间的 8 位无符号整数。
- `position` — 任务点的位置，指定为 `[x;y;z]` 的三元素列向量。
  *x*、*y* 和 *z* 是北东地（NED）坐标系中的位置，单位为米。
- `params` — 任务点的参数，指定为四元素列向量。

依次赋给这些字段的值，会相应地赋给 `UAVPathManagerBus` 总线中对应的总线元素。

下表描述了任务点结构体中 `mode` 的类型以及 `position` 和 `params` 字段的对应值。

| `mode` | `position` | `params` | 模式描述 |
| --- | --- | --- | --- |
| `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Takeoff** — 从地面起飞并飞向指定位置 |
| `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — 偏航角，单位为弧度，范围为 `[-pi, pi]`  *radius* — 过渡半径，单位为米 | **Waypoint** — 导航至航点 |
| `uint8(3)` | `[x;y;z]`  *x*、*y* 和 *z* 是圆形轨道中心的北东地（NED）坐标，单位为米 | `[radius;turnDir;numTurns;p4]`  *radius* — 轨道半径，单位为米  *turnDir* — 转弯方向，指定为以下之一：  - `1` — 顺时针转弯 - `—1` — 逆时针转弯 - `0` — 自动选择转弯方向    *numTurns* — 转弯圈数 | **Orbit** — 沿由参数定义的圆周轨道飞行 |
| `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Land** — 在指定位置着陆 |
| `uint8(5)` | `[x;y;z]`  起飞位置在 `Home` 输入端口指定 | `[p1;p2;p3;p4]` | **RTL** — 返回起飞位置 |
| `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*、*p2*、*p3* 和 *p4* 是对应于自定义任务点的用户指定参数 | **Custom** — 自定义任务点 |

**注意**

*p1*、*p2*、*p3* 和 *p4* 是用户指定的参数。

**示例：** `[struct('mode',uint8(1),'position',[0;0;100],'params',[0;0;0;0])]`

**数据类型：** `bus`

### **IsModeDone** — 判断任务点是否已执行 `0`（默认） | `1`

判断任务点是否已执行，指定为 `0`（`false`）或 `1`（`true`）。

**数据类型：** `Boolean`

### **MissionCmd** — 更改任务的命令 `uint8(0)`（默认）| 0 到 3 之间的 8 位无符号整数

用于在运行时更改任务的命令，指定为 0 到 3 之间的 8 位无符号整数。

下表描述了可能的任务命令。

| 任务命令 | 描述 |
| --- | --- |
| `uint8(0)` | **默认** — 按顺序从第一个任务点执行到最后一个任务点 |
| `uint8(1)` | **保持** — 保持当前任务点  对于固定翼无人机，在当前点盘旋；对于多旋翼无人机，在当前点悬停 |
| `uint8(2)` | **重复** — 到达最后一个任务点后重复执行任务 |
| `uint8(3)` | **返航** — 执行返航（RTL）模式  在 **返航** 后，如果 `MissionCmd` 输入更改为 **默认** 或 **重复**，任务将恢复 |

**数据类型：** `uint8`

### **Home** — 无人机 home 位置 三元素列向量

无人机 home 位置，指定为 `[x;y;z]` 的三元素列向量。
*x*、*y* 和 *z* 是以米为单位、在 north-east-down (NED) 坐标系中指定的位置。

**数据类型：** `single` | `double`
### 输出

### **MissionParams** — 无人机任务参数 `UAVPathManagerBus` 总线

无人机任务参数，以 `UAVPathManagerBus` 类型的 2×1 总线数组形式返回。总线数组的第一个元素是当前任务点，总线数组的第二个元素是上一个任务点。

下表描述了取决于任务模式的输出任务参数。

| 当前任务模式 | 输出任务参数 | | | |
| --- | --- | --- | --- | --- |
| 任务点 | `mode` | `position` | `params` |
| **Takeoff** | 第一个总线元素：当前 | `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |
| **Waypoint** | 第一个总线元素：当前 | `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — 偏航角，单位为弧度，范围为 `[-pi, pi]`  *radius* — 过渡半径，单位为米 |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | - `[yaw;radius;p3;p4]`   如果上一个任务点是   **Takeoff** - `[courseAngle;25;p3;p4]`   否则    *courseAngle* — 上一个位置与当前位置之间线段的夹角，以弧度为单位指定，范围为 `[-pi, pi]` |
| **Orbit** | 第一个总线元素：当前 | `uint8(3)` | `[x;y;z]`  *x*、*y* 和 *z* 是圆形轨道的中心，以 NED 坐标指定，单位为米 | `[radius;turnDir;numTurns;p4]`  *radius* — 轨道半径，单位为米  *turnDir* — 转弯方向，指定为以下之一：  - `1` — 顺时针转弯 - `—1` — 逆时针转弯 - `0` — 自动选择转弯   方向    *numTurns* — 转弯次数 |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |
| **Land** | 第一个总线元素：当前 | `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |
| **RTL** | 第一个总线元素：当前 | `uint8(5)` | `[x;y;z]`  起飞位置在 `Home` 输入端口指定 | `[p1;p2;p3;p4]` |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |
| **Custom** | 第一个总线元素：当前 | `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*、*p2*、*p3* 和 *p4* 是对应于自定义任务点的用户指定参数 |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |

**注意**

*p1*、*p2*、*p3* 和 *p4* 是用户指定的参数。

在仿真开始时，上一个任务点设置为 **Armed** 模式。

| mode | position | params |
| --- | --- | --- |
| `uint8(0)` | `[x;y;z]`  仿真开始时无人机的 `position`。 | `[-1;-1;-1;-1]` |

将结束任务点设置为 **RTL** 或 **Land** 模式，否则结束任务点会自动设置为 **Hold** 模式。

下表描述了当 **MissionCmd** 输入端的输入设置为 **Hold** 模式时的输出任务参数。

| 无人机类型 | 输出任务参数 | | | |
| --- | --- | --- | --- | --- |
| 任务点 | `mode` | `position` | `params` |
| **多旋翼** | 第一个总线元素：当前 | `uint8(7)` | `[x;y;z]` | `[-1;-1;-1;-1]` |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |
| **固定翼** | 第一个总线元素：当前 | `uint8(7)` | `[x;y;z]`  *x*、*y* 和 *z* 是以米为单位指定的 NED 坐标系中圆形轨道的中心 | `[radius;turnDir;-1;-1]`  *radius* — 盘旋半径在 `Loiter radius` 参数中指定  *turnDir* — 转弯方向指定为 `0` 以自动选择转弯方向 |
| 第二个总线元素：上一个 | 上一个任务点的 `mode` | 上一个任务点的 `position` | 上一个任务点的 `params` |

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: UAV type
  summary: 无人机类型 multirotor（默认）| fixed-wing
  group: ''
- name: Loiter radius
  summary: 固定翼无人机的盘旋半径 25（默认）| 正数值标量
  group: ''
- name: Data type
  summary: 输入任务总线的数据类型 double（默认）| single
  group: ''
- name: Mission bus name
  summary: 输入任务总线的名称 'UAVPathManagerBus'（默认）
  group: ''
```

### **UAV type** — 无人机类型 `multirotor`（默认）| `fixed-wing`

无人机类型，指定为 `multirotor` 或 `fixed-wing`。

**可调：** 否

### **Loiter radius** — 固定翼无人机的盘旋半径 25（默认）| 正数值标量

固定翼无人机的盘旋半径，指定为以米为单位的正数值标量。

**依赖关系：** 要启用此参数，请将 **UAV type** 参数设置为 `fixed-wing`。

**可调：** 否

### **Data type** — 输入任务总线的数据类型 `double`（默认）| `single`

输入任务总线的数据类型，指定为 `double` 或 `single`。

**可调：** 否

### **Mission bus name** — 输入任务总线的名称 `'UAVPathManagerBus'`（默认）

输入任务总线的名称，指定为 `'UAVPathManagerBus'`。

**可调：** 否
## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

计算并执行无人机自主任务

Path Manager 模块通过在 **MissionData** 输入端口指定的任务点之间依次切换，计算无人机（UAV）的任务参数。**MissionCmd** 输入端口在运行时更改执行顺序。该模块同时支持多旋翼和固定翼无人机类型。
