---
type: simulink-block
title: 'Vehicle Attitude'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'vehicleattitude'
documentation_source_path: 'px4/ref/vehicleattitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Attitude

## 端口

### 输出

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

Status 输出指示是否在前一时间步中接收到 vehicle_odometry uORB 消息。值 `0` 表示输出端的 uORB 数据是最新的，值 `1` 表示前一时间步中 uORB 数据未更新。

此输出可用于触发子系统，以处理 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

### **Roll rate** — 关于 x 轴的偏置校正角速度标量 | rad/s

关于 x 轴的偏置校正角速度，从 vehicle_odometry uORB 主题读取。

**数据类型：** `single`

### **Pitch rate** — 关于 y 轴的偏置校正角速度标量 | rad/s

关于 y 轴的偏置校正角速度，从 vehicle_odometry uORB 主题读取。

**数据类型：** `single`

### **Yaw rate** — 关于 z 轴的偏置校正角速度标量 | rad/s

关于 z 轴的偏置校正角速度，从 vehicle_odometry uORB 主题读取。

**数据类型：** `single`

### **Quaternion** — 安装 PX4 飞行控制器的载具姿态，以四元数形式表示的 1×4 数组

安装 PX4 飞行控制器的载具姿态，以四元数形式表示，从 vehicle_odometry uORB 主题读取。

**数据类型：** `single`

### **Timestamp** — 接收到的 uORB 数据的时间戳，以 microseconds 为单位

表示 vehicle_odometry 主题最后一次更新时的时间（自 PX4® 系统启动以来）。

**数据类型：** `double`

## 参数

#### 主选项卡

### **Roll** — 启用 roll 值作为输出之一 `off`（默认）| `on`

### **Pitch** — 启用 pitch 值作为输出之一 `off`（默认）| `on`

### **Yaw** — 启用 yaw 值作为输出之一 `off`（默认）| `on`

### **Quaternion** — 启用 quaternion 值作为输出之一 `on`（默认）| `off`

### **Timestamp** — 启用 timestamp 值作为输出之一 `off`（默认）| `on`

### **Sample time** — 模块读取值的时间间隔 `1/250`（默认）| 任何为 1/250 的倍数的非负值 | -1

输入模块从 uORB 网络读取值的时间间隔。

将此参数设置为 `-1` 时，Simulink® 会根据模块在模型中的上下文确定模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认）| on

- 选择此选项时，读取操作在阻塞模式下运行。等待请求的数据可用时，读取操作会被阻塞。当数据可用时，模块输出所选值，并将 **Status** 端口设置为 `0`。

  板卡会在 `Timeout in seconds` 中所述的时间内以阻塞模式等待消息。如果在超时之前未接收到数据，则 Status 端口输出 1，模块输出最后接收到的值。

  如果目标硬件在下一个读取操作计划开始之时仍在等待数据可用，则会发生任务溢出。

  要修复溢出，请使用 **Sample time** 参数增加时间步长。
- 清除此选项时，读取操作在非阻塞模式下运行。在此模式下，模块不会等待请求的数据可用。

### **Timeout in seconds** — 等待直到接收到数据的时间 `1e-3`（默认）| (0, 2^32/1000]

指定当选中 **Wait until data received** 参数时，模块在每个时间步内等待数据的时间量。如果发生超时，读取操作将中止。

#### 依赖关系

仅当选择 **Wait until data received** 参数时，此参数才会出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 vehicle_odometry uORB 主题并获取姿态测量值

Vehicle Attitude 模块读取 vehicle_odometry uORB 主题，并输出 Pixhawk® 硬件提供的姿态测量值。该模块以 roll、pitch 和 yaw 以及四元数 (NED) 形式输出载具姿态。

在每个仿真步上，模块检查 vehicle_odometry 主题上是否有新消息可用。如果有新消息可用，模块将检索并输出该消息，且时间戳会更新。如果没有新消息可用，模块输出最后更新的 uORB 消息，且时间戳不会更新。如果自仿真开始以来尚未接收到消息，则输出为零。

在 Normal 模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件外设读取数据。
