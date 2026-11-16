---
type: simulink-block
title: 'PX4 Read Position Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4readpositionsetpoint'
documentation_source_path: 'px4/ref/px4readpositionsetpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Read Position Setpoint

## 端口

### 输出

### **Previous** — 车辆最近经过的设定点的坐标 Vector

此端口输出车辆最近经过的设定点的坐标，采用 WGS84（纬度、经度和高度）坐标系，或采用 NED 和 ENU 坐标系中的局部坐标（`x`、`y` 和 `z`）。

**数据类型：** `double`

### **Current** — 车辆当前目标设定点的坐标 Vector

此端口输出车辆当前目标设定点的坐标，采用 WGS84（纬度、经度和高度）坐标系，或采用 NED 和 ENU 坐标系中的局部坐标（x、y 和 z）。

**数据类型：** `double`

### **Next** — 车辆下一个设定点的坐标 Vector

此端口输出车辆当前目标之后的下一个设定点的坐标，采用 WGS84（纬度、经度和高度）坐标系，或采用 NED 和 ENU 坐标系中的局部坐标（x、y 和 z）。

**数据类型：** `double`

### **Type** — Current 设定点的航点模式 Scalar

**Type** 输出端口提供当前设定点的航点模式或任务命令的信息，该设定点是在从 QGroundControl 创建并上传的任务中设置的。该端口输出以下类型之一。

| 航点类型或任务命令 | Type 输出 |
| --- | --- |
| Takeoff | `3` |
| Land | `4` |
| Waypoint | `0` |
| Loiter | `2` |
| Idle | `5` |

**数据类型：** `uint8`

### **Position Setpoint** — position\_setpoint\_triplet uORB topic 的 Simulink 总线 Bus

此端口输出 `position_setpoint_triplet uORB` topic 的 Simulink 总线。使用此端口可获取由 navigator 模块作为 `position_setpoint_triplet` topic 的一部分发布的其他信息。

#### 依赖关系

要启用此端口，请选择 **Output Simulink bus for position\_setpoint\_triplet** 参数。

**数据类型：** `Bus`

### **Trajectory Waypoint** — vehicle\_trajectory\_waypoint uORB topic 的 Simulink 总线 Bus

此端口输出 `vehicle_trajectory_waypoint uORB` topic 的 Simulink 总线。使用此端口可获取作为 `vehicle_trajectory_waypoint` topic 的一部分发布的其他信息，例如偏航设定点、速度设定点等。

#### 依赖关系

要启用此端口，请选择 **Output Simulink bus for vehicle\_trajectory\_waypoint** 参数。

**数据类型：** `Bus`

### **Onboard Failsafe** — 机载计算机的故障保护标志 Boolean

当在过去 `0.5` 秒内没有从机载计算机接收到新航点时，该端口返回值 `1`。使用此标志可启用控制器中建模的任何特定机载故障保护动作。

#### 依赖关系

要启用此端口，请选择 **Output onboard computer failsafe flag** 参数。

**数据类型：** `Boolean`

### **Onboard Status** — 机载计算机启用状态 Boolean

此端口输出状态标志，以指示机载计算机工作流是否已启用。

当机载计算机启用 PX4 时，该端口返回值 `1`，否则返回 `0`。

#### 依赖关系

要启用此端口，请选择 **Output onboard computer enabled status** 参数。

**数据类型：** `Boolean`

## 参数

#### 主要

### **coordinate Format** — 设定点的坐标系 `Local Coordinates (NED)` (默认) | `WGS84` | `Local Coordinates (ENU)`

使用此参数指定 previous、current 和 next 航点的所需坐标格式。格式可以指定为以下之一：

- `Local Coordinates (NED)`：使用此选项将 previous、current 和 next 设定点输出为 NED 坐标系中的局部坐标（x、y 和 z）。用于将由 PX4 提供的大地坐标转换为局部坐标的变换方法是 *flat*。
- `Local Coordinates (ENU)`：使用此选项将 previous、current 和 next 设定点输出为 ENU 坐标系中的局部坐标（`x`、`y` 和 `z`）。用于将由 PX4 提供的大地坐标转换为局部坐标的变换方法是 *flat*。
- `WGS84`：使用此选项将 previous、current 和 next 设定点输出为 PX4 返回的原始大地坐标（纬度、经度和高度）。

### **Sample time** — 输出之间的间隔 `0.01` (默认) | 任何为 0,001 倍数的非负整数 | `-1`

指定模块从 uORB 网络读取值的时间间隔。将此参数指定为 `-1` 时，Simulink 会根据模块在模型中的上下文确定该模块的最佳采样时间。

#### 高级

### **Output Simulink bus for position\_setpoint\_triplet** — position\_setpoint\_triplet uORB topic 的总线 `off` (默认) | `on`

选择此参数以启用 **Position Setpoint** 端口。此端口包含 `position_setpoint_triplet` uORB topic 的完整 Simulink 总线。使用此端口可获取由 navigator 模块作为 position\_setpoint\_triplet topic 的一部分发布的其他信息。

### **Output Simulink bus for vehicle\_trajectory\_waypoint** — vehicle trajectory waypoint 的总线 `off` (默认) | `on`

选择此参数以启用 **Trajectory Waypoint** 端口。

### **Output onboard computer failsafe flag** — 机载计算机故障保护标志状态 `off` (默认) | `on`

选择此参数以启用 **Onboard Failsafe** 端口。使用此端口对您自己的故障保护条件建模。

### **Output onboard computer enabled status** — 机载计算机启用状态 `off` (默认) | `on`

选择此参数以启用 **Onboard Status** 端口。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

读取由 PX4 Navigator 模块在 uORB topic position_setpoint_triplet 中发布的位置设定点

PX4 Read Position Setpoint 模块输出由 PX4 navigator 模块在 `position_setpoint_triplet` uORB topic 中发布的位置设定点。该模块输出当前目标设定点（Current）的坐标、当前目标之后的下一个设定点（Next）以及最近经过的设定点（Previous）。该模块将 Previous、Current 和 Next 位置设定点输出为坐标，坐标系为 World Geodetic System of 1984 (WGS 84)、局部北-东-下 (NED) 或局部东-北-上 (ENU) 坐标系之一。

您可以在 QGroundControl (QGC) 的规划视图中创建自主任务，并通过 MAVLink 将任务上传到 PX4 Autopilot。有关创建任务的信息，请参阅规划视图。任务由航点组成，例如 TakeOff、Position（也称为 Waypoint）、Land 等。PX4 Autopilot 上的 MAVLink 模块解码任务数据并将其存储在内存中。PX4 中的 navigator 模块从机载内存中检索航点，并将它们发布在 `position_setpoint_triplet` uORB topic 中。当车辆到达这些航点时，navigator 模块会自动更新 Previous、Current 和 Next 设定点。

**注意**

如果机载伴飞计算机启用了 PX4（PX4 参数 COM\_OBS\_AVOID 设置为 1），则将使用从机载计算机接收的航点数据更新当前航点。来自机载计算机的更新航点通过 MAVLink 上的 Path Planning Interface 传送到 PX4。PX4 MAVLink 模块接收该航点，并将其发布在 vehicle\_trajectory\_waypoint uORB topic 中。当启用机载计算机工作流时，此模块从 vehicle\_trajectory\_waypoint uORB topic 读取航点，并将其作为当前航点输出。

该模块还输出当前位置设定点的航点模式，它指示从 QGroundControl (QGC) 上传的任务中已设置的对应航点类型。这有助于在 Simulink® 中区分 Current Waypoint 类型（TakeOff、Waypoint、Land）。

将模块输出的坐标直接作为输入命令提供给在 Simulink 中设计的控制器算法。使用 **Type** 输出区分航点，并在控制器中采取相应的适当操作。

此模块还读取在 QGC 中创建的任务的设定点数据，这些任务的任务类型为 Flight plan。但是，您不能使用此模块读取 geofencing 和 rally 任务的设定点数据。

在 flight plan 任务中，该模块可检索其航点数据的受支持任务命令为 Takeoff、Land 和 Waypoint。不支持 Return to Launch (RTL)。

**注意**

仅当您在 Hardware Setup 过程的 **Select System Startup Script in PX4** 步骤中为 PX4 Autopilot 选择 **Use default startup script (rcS)** 作为启动脚本选项时，才支持 PX4 Read Position Setpoint 模块。有关详细信息，请参阅 Selecting Startup Script for PX4 Autopilot。

**注意**

PX4 Read Position Setpoint 模块要求您将 SD 卡连接到 PX4 Autopilot。确保连接的 SD 卡在 `etc` 文件夹中不包含任何自定义启动脚本 (rc.txt)。

**注意**

PX4 Read Position Setpoint 模块无法确定 QGroundControl 中正在进行的任务是否已暂停。您需要找到单独的逻辑来确定 QGroundControl 中的任务是否已暂停。

在 Normal 模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
