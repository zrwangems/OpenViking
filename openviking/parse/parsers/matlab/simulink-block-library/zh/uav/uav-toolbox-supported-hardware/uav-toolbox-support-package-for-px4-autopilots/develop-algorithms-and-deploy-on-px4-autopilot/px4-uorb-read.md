---
type: simulink-block
title: 'PX4 uORB Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbread'
documentation_source_path: 'px4/ref/px4uorbread.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 uORB Read

## 端口

### 输出

### **Msg** — uORB 消息非虚拟总线

uORB 消息，返回为非虚拟总线。uORB 消息的类型使用参数 `Topic to subscribe to` 指定。

将 Bus Selector 模块连接到 `Msg` 输出以提取信号。

**数据类型：** `bus`

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

Status 输出指示是否在上一时间步接收到 uORB 消息。值 `0` 表示 `Msg` 输出处的 uORB 数据是最新的，值 `1` 表示 uORB 数据是在上一时间步接收到的。

此输出可用于触发子系统，以处理 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

## 参数

#### 主选项卡

### **Topic to subscribe to** — 模块需要订阅的 uORB 主题的名称 sensor\_accel（默认） | uORB 主题之一

选择模块需要订阅以读取 uORB 数据的 uORB 主题的名称。点击 **Select** 浏览您下载的 `px4` 目录的 `Firmware/msg` 文件夹中可用的主题名称。

### **Select instance** — 模块需要订阅的 uORB 主题的实例 uORB 主题的实例

选择模块需要订阅以读取 uORB 数据的 uORB 主题的实例。

#### 依赖关系

仅当您在 **Topic to subscribe to** 参数中选择支持多个实例的主题时，此参数才会出现。

例如，`actuator_controls` 主题支持多个实例，您可以从下拉列表中选择一个实例。

### **Sample time** — 模块读取值的时间间隔 `0.001`（默认） | 任意非负值，且为 0.001 的倍数 | -1

输入模块从 uORB 网络读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认） | on

- 当您选择此选项时，读操作以阻塞模式运行。在等待请求的数据可用期间，读操作被阻塞。等待数据时，**Status** 端口显示上一时间步的相同值。当数据变为可用时，**Data** 端口输出数据字节，并且 **Status** 端口变为 `0`。

  如果当下一次读操作计划开始时，目标硬件仍在等待数据变为可用，则会发生任务超限。

  要修复超限，请使用 **Sample time** 参数增大时间步长。
- 当您清除此选项时，读操作以非阻塞模式运行。在此模式下，模块不等待请求的数据变为可用。

### **Timeout in seconds** — 等待直到接收到数据的时间 `0.1`（默认） | (0, 2^32/1000]

指定如果选中 **Wait until data received** 参数，模块在每个时间步中等待数据的时间量。如果发生超时，读操作将中止。

#### 依赖关系

仅当您选中 **Wait until data received** 参数时，此参数才会出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取指定 uORB 主题的 uORB 数据

PX4 uORB Read 模块创建一个 Simulink® 非虚拟总线，该总线对应于指定的 uORB 主题。

在每个仿真步中，模块检查特定主题上是否有新消息可用。如果有新消息可用，模块将检索该消息并将其转换为 Simulink 总线信号。Msg 端口输出此新消息。如果没有新消息可用，Msg 输出最后接收到的 uORB 消息。如果自仿真开始以来尚未接收到消息，Msg 输出空白消息。

在 Normal 模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件外设读取数据。
