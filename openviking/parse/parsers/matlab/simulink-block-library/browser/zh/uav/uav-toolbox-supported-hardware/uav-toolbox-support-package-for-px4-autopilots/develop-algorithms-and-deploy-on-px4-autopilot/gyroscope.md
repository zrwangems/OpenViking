---
type: simulink-block
title: 'Gyroscope'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'gyroscope'
documentation_source_path: 'px4/ref/gyroscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyroscope

## 端口

### 输出

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

Status 输出指示是否在前一时间步接收到了 sensor\_gyro uORB 消息。值 `0` 表示输出端的 uORB 数据是最新的，值 `1` 表示 uORB 数据是在前一时间步接收到的。

此输出可用于触发子系统，以处理 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

### **X** — 沿 x 轴的角速度 标量 | rad/s

PX4 Autopilot 开发板沿 x 轴的角速度，读取自 sensor\_gyro uORB 主题。

**数据类型：** `single`

### **Y** — 沿 y 轴的角速度 标量 | rad/s

PX4 Autopilot 开发板沿 y 轴的角速度，读取自 sensor\_gyro uORB 主题。

**数据类型：** `single`

### **Z** — 沿 z 轴的角速度 标量 | rad/s

PX4 Autopilot 开发板沿 z 轴的角速度，读取自 sensor\_gyro uORB 主题。

**数据类型：** `single`

### **Timestamp** — 接收到的 uORB 数据的时间戳，时间单位为 micoseconds

表示 sensor\_gyro 主题上次更新的时间（自 PX4 系统启动以来）。

**数据类型：** `double`

要查看 sensor\_gyro uorb 主题的更多输出选项，请使用 PX4 uORB Read 模块，订阅该主题，并选择其他输出选项。

## 参数

#### 主选项卡

### **Timestamp** — 启用时间戳值作为输出之一 `off`（默认） | `on`

选择此参数以输出时间戳。

### **Sample time** — 模块读取值的时间间隔 `1/250`（默认） | 任何为 1/250 倍数的非负值 | -1

输入模块从 uORB 网络读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认） | on

- 当您选择此选项时，读取操作以阻塞模式运行。读取操作在等待请求的数据可用时被阻塞。当数据可用时，模块输出所选值，并且 **Status** 端口设置为 `0`。

  开发板以阻塞模式等待消息，等待时间为 `Timeout in seconds` 中提到的时长。如果在超时之前未接收到数据，则 Status 端口输出 1，模块输出最后接收到的值。

  如果目标硬件在下一个读取操作计划开始时仍在等待数据可用，则会发生任务超限。

  要修复超限，请使用 **Sample time** 参数增大时间步长。
- 当您清除此选项时，读取操作以非阻塞模式运行。在此模式下，模块不等待请求的数据可用。

### **Timeout in seconds** — 等待直到接收到数据的时间 `1e-3`（默认） | (0, 2^32/1000]

如果选中了 **Wait until data received** 参数，则指定模块在每个时间步等待数据的时间量。如果发生超时，读取操作将被中止。

#### 依赖项

仅当您选择 **Wait until data received** 参数时，此参数才会出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 sensor_gyro uORB 主题并获取三维旋转速率

Gyroscope 模块读取 sensor\_gyro uORB 主题，并输出 PX4 Autopilot 开发板沿 x、y 和 z 轴的旋转速率。该模块还输出时间戳。

在每个仿真步中，模块检查 sensor\_gyro 主题上是否有新消息可用。如果有新消息可用，模块会检索该消息并输出它，同时更新时间戳。如果没有新消息可用，模块输出最后更新的 uORB 消息，并且时间戳不会更新。如果自仿真开始以来尚未接收到任何消息，则输出为零。

在 Normal 模式仿真期间，该模块输出零。

在 Connected I/O 仿真期间，该模块从硬件的外设读取数据。
