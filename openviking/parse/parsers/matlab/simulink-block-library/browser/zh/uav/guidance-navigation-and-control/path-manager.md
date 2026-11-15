---
type: simulink-block
title: 'Path Manager'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control'
documentation_page: 'pathmanager'
documentation_source_path: 'ref/pathmanager.html'
language: zh-CN
chinese_source: worker-translation
---

# Path Manager

## 端口

### 输入

### **Pose** — 当前 UAV 位姿四元素列向量

当前 UAV 位姿，指定为 `[x;y;z;courseAngle]` 的四元素列向量。
*x*、*y* 和 *z* 是 UAV 在 north-east-down (NED) 坐标中的当前位置，以 meters 为单位。
*courseAngle* 指定航向角，以 radians 为单位，范围在 `[-pi, pi]` 内。

**数据类型：** `single` | `double`

### **MissionData** — UAV 任务数据 `UAVPathManagerBus` bus

UAV 任务数据，指定为 `UAVPathManagerBus` bus。`UAVPathManagerBus` bus 具有三个 bus 元素 `mode`、`position` 和 `params`。

您可以使用 Constant (Simulink) 模块将任务数据指定为 *n*×1 结构体数组，并将输出数据类型设置为 `Bus:UAVPathManagerBus`。*n* 是任务点的数量。每个结构体的字段为：

- `mode` — 任务点的模式，指定为 1 到 6 之间的 8 位无符号整数。
- `position` — 任务点的位置，指定为 `[x;y;z]` 的三元素列向量。*x*、*y* 和 *z* 是在 north-east-down (NED) 坐标中的位置，以 meters 为单位。
- `params` — 任务点的参数，指定为四元素列向量。

分配给这些字段的值依次分配给 `UAVPathManagerBus` bus 中对应的 bus 元素。

下表描述了 `mode` 的类型以及任务点结构体中 `position` 和 `params` 字段的对应值。

| `mode` | `position` | `params` | 模式描述 |
| --- | --- | --- | --- |
| `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Takeoff** — 从地面起飞并朝指定位置飞行 |
| `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — Yaw angle，以 radians 为单位，范围在 `[-pi, pi]` 内  *radius* — Transition radius，以 meters 为单位 | **Waypoint** — 导航到 waypoint |
| `uint8(3)` | `[x;y;z]`  *x*、*y* 和 *z* 是圆形轨道的中心，位于 NED 坐标中，以 meters 为单位 | `[radius;turnDir;numTurns;p4]`  *radius* — 轨道半径，以 meters 为单位  *turnDir* — 转弯方向，指定为以下之一：  - `1` — 顺时针转弯 - `—1` — 逆时针转弯 - `0` — 自动选择转弯方向    *numTurns* — 转弯次数 | **Orbit** — 沿参数定义的圆周进行轨道飞行 |
| `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` | **Land** — 在指定位置着陆 |
| `uint8(5)` | `[x;y;z]`  launch position 在 `Home` 输入端口指定 | `[p1;p2;p3;p4]` | **RTL** — 返回到 launch position |
| `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*、*p2*、*p3* 和 *p4* 是对应于自定义任务点的用户指定参数 | **Custom** — 自定义任务点 |

**注意**

*p1*、*p2*、*p3* 和 *p4* 是用户指定的参数。

**示例：** `[struct('mode',uint8(1),'position',[0;0;100],'params',[0;0;0;0])]`

**数据类型：** `bus`

### **IsModeDone** — 确定任务点是否已执行 `0` (默认) | `1`

确定任务点是否已执行，指定为 `0` (`false`) 或 `1` (`true`)。

**数据类型：** `Boolean`

### **MissionCmd** — 更改任务的命令 `uint8(0)` (默认) | 0 到 3 之间的 8 位无符号整数

用于在运行时更改任务的命令，指定为 0 到 3 之间的 8 位无符号整数。

下表描述了可能的任务命令。

| 任务命令 | 描述 |
| --- | --- |
| `uint8(0)` | **Default** — 按顺序从第一个任务点执行到最后一个任务点 |
| `uint8(1)` | **Hold** — 保持在当前任务点 对于 fixed-wing，在当前点附近盘旋；对于 multirotor UAV，在当前点悬停 |
| `uint8(2)` | **Repeat** — 到达最后一个任务点后重复任务 |
| `uint8(3)` | **RTL** — 执行 return to launch (RTL) 模式 在 **RTL** 后，如果 `MissionCmd` 输入更改为 **Default** 或 **Repeat**，则任务恢复 |

**数据类型：** `uint8`

### **Home** — UAV home location 三元素列向量

UAV home location，指定为 `[x;y;z]` 的三元素列向量。
*x*、*y* 和 *z* 是在 north-east-down (NED) 坐标中的位置，以 meters 为单位。

**数据类型：** `single` | `double`

### 输出

### **MissionParams** — UAV 任务参数 `UAVPathManagerBus` bus

UAV 任务参数，返回为类型 `UAVPathManagerBus` 的 2×1 bus 数组。bus 数组的第一个元素是当前任务点，bus 数组的第二个元素是前一个任务点。

下表描述了取决于任务模式的输出任务参数。

| 当前任务模式 | 输出任务参数 | | | |
| --- | --- | --- | --- | --- |
| 任务点 | `mode` | `position` | `params` |
| **Takeoff** | 第一个 bus 元素：当前 | `uint8(1)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |
| **Waypoint** | 第一个 bus 元素：当前 | `uint8(2)` | `[x;y;z]` | `[yaw;radius;p3;p4]`  *yaw* — Yaw angle，以 radians 为单位，范围在 `[-pi, pi]` 内  *radius* — Transition radius，以 meters 为单位 |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | - `[yaw;radius;p3;p4]`   如果前一个任务点是 **Takeoff** - `[courseAngle;25;p3;p4]`   否则    *courseAngle* — 前一个位置与当前位置之间线段的角度，以 radians 为单位，范围在 `[-pi, pi]` 内 |
| **Orbit** | 第一个 bus 元素：当前 | `uint8(3)` | `[x;y;z]`  *x*、*y* 和 *z* 是圆形轨道的中心，位于 NED 坐标中，以 meters 为单位 | `[radius;turnDir;numTurns;p4]`  *radius* — 轨道半径，以 meters 为单位  *turnDir* — 转弯方向，指定为以下之一：  - `1` — 顺时针转弯 - `—1` — 逆时针转弯 - `0` — 自动选择转弯方向    *numTurns* — 转弯次数 |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |
| **Land** | 第一个 bus 元素：当前 | `uint8(4)` | `[x;y;z]` | `[p1;p2;p3;p4]` |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |
| **RTL** | 第一个 bus 元素：当前 | `uint8(5)` | `[x;y;z]`  launch position 在 `Home` 输入端口指定 | `[p1;p2;p3;p4]` |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |
| **Custom** | 第一个 bus 元素：当前 | `uint8(6)` | `[x;y;z]` | `[p1;p2;p3;p4]`  *p1*、*p2*、*p3* 和 *p4* 是对应于自定义任务点的用户指定参数 |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |

**注意**

*p1*、*p2*、*p3* 和 *p4* 是用户指定的参数。

在仿真开始时，前一个任务点设置为 **Armed** 模式。

| mode | position | params |
| --- | --- | --- |
| `uint8(0)` | `[x;y;z]`  UAV 在仿真开始时的 `position`。 | `[-1;-1;-1;-1]` |

将结束任务点设置为 **RTL** 或 **Land** 模式，否则结束任务点会自动设置为 **Hold** 模式。

下表描述了当 **MissionCmd** 输入端口输入设置为 **Hold** 模式时的输出任务参数。

| UAV Type | 输出任务参数 | | | |
| --- | --- | --- | --- | --- |
| 任务点 | `mode` | `position` | `params` |
| **Multirotor** | 第一个 bus 元素：当前 | `uint8(7)` | `[x;y;z]` | `[-1;-1;-1;-1]` |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |
| **Fixed-Wing** | 第一个 bus 元素：当前 | `uint8(7)` | `[x;y;z]`  *x*、*y* 和 *z* 是圆形轨道的中心，位于 NED 坐标中，以 meters 为单位 | `[radius;turnDir;-1;-1]`  *radius* — Loiter radius 在 `Loiter radius` 参数中指定  *turnDir* — Turn direction 指定为 `0`，用于自动选择转弯方向 |
| 第二个 bus 元素：前一个 | 前一个任务点的 `mode` | 前一个任务点的 `position` | 前一个任务点的 `params` |

**数据类型：** `bus`

## 参数

### **UAV type** — UAV 类型 `multirotor` (默认) | `fixed-wing`

UAV 类型，指定为 `multirotor` 或 `fixed-wing`。

**可调：** No

### **Loiter radius** — fixed-wing UAV 的 Loiter radius 25 (默认) | 正数值标量

fixed-wing UAV 的 Loiter radius，指定为以 meters 为单位的正数值标量。

**依赖关系：** 要启用此参数，请将 **UAV type** 参数设置为 `fixed-wing`。

**可调：** No

### **Data type** — 输入任务 bus 的数据类型 `double` (默认) | `single`

输入任务 bus 的数据类型，指定为 `double` 或 `single`。

**可调：** No

### **Mission bus name** — 输入任务 bus 的名称 `'UAVPathManagerBus'` (默认)

输入任务 bus 的名称，指定为 `'UAVPathManagerBus'`。

**可调：** No

## 所属库

UAV Toolbox / Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

计算并执行 UAV 自主任务

Path Manager 模块通过在 **MissionData** 输入端口指定的任务点之间依次切换，计算无人驾驶飞行器 (UAV) 的任务参数。**MissionCmd** 输入端口在运行时更改执行顺序。该模块支持 multirotor 和 fixed-wing 两种 UAV 类型。
