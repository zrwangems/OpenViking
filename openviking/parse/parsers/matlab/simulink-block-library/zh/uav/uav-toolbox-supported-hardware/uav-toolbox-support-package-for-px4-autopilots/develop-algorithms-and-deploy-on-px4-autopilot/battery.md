---
type: simulink-block
title: 'Battery'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'battery'
documentation_source_path: 'px4/ref/battery.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery

## 端口

### 输出

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

**Status** 输出指示是否在前一个时间步接收到了 `battery_status uORB` 消息。值 `0` 表示输出端的 uORB 数据是最新的，值 `1` 表示 uORB 数据是在前一个时间步接收到的。

此输出可用于触发子系统，以处理 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

### **Voltage** — 电池电压 标量（volts）

电池的输出电压，从 battery\_status uORB 主题读取。

**数据类型：** `single`

### **Current** — 电池正在提供的输出电流 标量（amperes）

输出电流，从 battery\_status uORB 主题读取。

**数据类型：** `single`

### **Percentage** — 剩余电池寿命百分比 标量

剩余电池寿命百分比，从 battery\_status uORB 主题读取。

**数据类型：** `single`

### **Warning** — 电池警告状态 标量

电池警告状态，从 battery\_status uORB 主题读取。

| Status | 描述 |
| --- | --- |
| 0 | 没有激活的电池低电压警告 |
| 1 | 低电压警告 |
| 2 | 临界电压，立即返回 / 中止 |
| 3 | 需要立即着陆 |
| 4 | 电池已完全失效 |

**数据类型：** `uint8`

### **Timestamp** — 接收到的 uORB 数据的时间戳 time

从 uORB 网络读取的 battery\_status uORB 主题的时间戳。

**数据类型：** `double`

## 参数

#### 主选项卡

### **Voltage** — 启用电压值作为输出之一 `on`（默认） | `off`

### **Current** — 启用电流值作为输出之一 `off`（默认） | `on`

### **Battery percentage** — 启用电池电量百分比作为输出之一 `on`（默认） | `off`

### **Battery status warning** — 启用电池状态警告作为输出之一 `off`（默认） | `on`

### **Timestamp** — 启用时间戳值作为输出之一 `off`（默认） | `on`

### **Sample time** — 模块读取值的时间间隔 `1/250`（默认） | 任何为 1/250 倍数的非负值 | -1

输入模块从 uORB 网络读取值的时间间隔。

将此参数设置为 `-1` 时，Simulink® 根据模型中的模块上下文确定模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认） | on

- 选择此选项时，读取操作在阻塞模式下运行。在等待请求的数据可用时，读取操作被阻塞。等待数据时，**Status** 端口显示来自前一个时间步的相同值。当数据变为可用时，模块输出选定的值，并且 **Status** 端口变为 `0`。

  如果目标硬件在下一个读取操作计划开始时仍在等待数据可用，则会发生任务超限。

  要修复超限，请使用 **Sample time** 参数增加时间步长。
- 清除此选项时，读取操作在非阻塞模式下运行。在此模式下，模块不会等待请求的数据可用。

### **Timeout in seconds** — 等待直到接收到数据的时间 `1e-3`（默认） | (0, 2^32/1000]

如果选择了 **Wait until data received** 参数，请指定模块在每个时间步等待数据的时间量。如果发生超时，读取操作将中止。

#### 依赖项

仅当选择 **Wait until data received** 参数时，此参数才会出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 battery_status uORB 主题并获取有关电池状态的详细信息

Battery 模块读取 `battery_status uORB` 主题，并输出有关连接到 PX4 飞行控制器的电池状态的详细信息。该模块还输出时间戳。

在每个仿真步中，模块检查 battery\_status 主题上是否有新消息可用。如果有新消息可用，模块会检索该消息并将其转换为输出值。如果没有新消息可用，输出基于最后接收到的 uORB 消息。如果自仿真开始以来尚未接收到消息，则输出为零。

在正常模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
