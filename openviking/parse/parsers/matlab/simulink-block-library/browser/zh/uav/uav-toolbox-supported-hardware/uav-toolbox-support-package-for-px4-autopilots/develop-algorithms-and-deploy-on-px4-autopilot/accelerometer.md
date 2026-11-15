---
type: simulink-block
title: 'Accelerometer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'accelerometer'
documentation_source_path: 'px4/ref/accelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Accelerometer

## 端口

### 输出

### **Status** — 接收到的 uORB 数据的状态 `0` | `1`

Status 输出指示 sensor\_accel uORB 消息是否在上一个时间步期间接收到。`0` 值表示输出处的 uORB 数据是最新的，`1` 值表示 uORB 数据是在上一个时间步期间接收到的。

此输出可用于触发子系统，以处理在 uORB 网络中接收到的新消息。

**数据类型：** `Boolean`

### **X** — 沿 x 轴的线性加速度标量 (㎨)

PX4 Autopilot 板沿 x 轴的线性加速度，读取自 sensor\_accel uORB 主题。

**数据类型：** `single`

### **Y** — 沿 y 轴的线性加速度标量 (㎨)

PX4 Autopilot 板沿 y 轴的线性加速度，读取自 sensor\_accel uORB 主题。

**数据类型：** `single`

### **Z** — 沿 z 轴的线性加速度标量 (㎨)

PX4 Autopilot 板沿 z 轴的线性加速度，读取自 sensor\_accel uORB 主题。

**数据类型：** `single`

### **Timestamp** — 接收到的 uORB 数据的时间戳，时间单位为 microseconds

表示 sensor\_accel 主题上次更新时的时间（自 PX4 系统启动以来）。

**数据类型：** `double`

要查看 sensor\_accel uorb 主题的更多输出选项，请使用 PX4 uORB Read 模块，订阅该主题，并选择其他输出选项。

## 参数

#### 主选项卡

### **时间戳** — 启用时间戳值作为输出之一 `off` (默认) | `on`

选择此参数以输出时间戳。

### **采样时间** — 模块读取值的时间间隔 `1/250` (默认) | 任何 1/250 的非负倍数 | -1

输入模块从 uORB 网络读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定为该模块的最佳采样时间。

#### 高级选项卡

### **等待直到接收到数据** — 等待直到请求的数据可用 off (默认) | on

- 当您选择此选项时，读取操作以阻塞模式运行。在等待请求的数据可用期间，读取操作会被阻塞。当数据可用时，模块输出所选值，并且 **Status** 端口设置为 `0`。

  板卡在阻塞模式下等待消息，等待时间为 `Timeout in seconds` 中指定的时间。如果在超时之前未接收到数据，则 Status 端口输出 1，并且模块输出最后接收到的值。

  如果目标硬件在下一次读取操作计划开始时仍在等待数据可用，则会发生任务超限。

  要修复超限，请使用 **采样时间** 参数增加时间步。
- 当您清除此选项时，读取操作以非阻塞模式运行。在此模式下，模块不会等待请求的数据可用。

### **超时秒数** — 等待直到接收到数据的时间 `1e-3` (默认) | (0, 2^32/1000]

如果选择了 **等待直到接收到数据** 参数，则指定模块在每个时间步等待数据的时间量。如果发生超时，则中止读取操作。

#### 依赖关系

仅当您选择 **等待直到接收到数据** 参数时，此参数才出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 sensor\_accel uORB 主题并获取三维线性加速度

Accelerometer 模块读取 sensor\_accel uORB 主题，并输出 PX4 Autopilot 板沿 x、y 和 z 轴的线性加速度。该模块还输出时间戳。

在每个仿真步中，模块检查 sensor\_accel 主题上是否有新消息可用。如果有新消息可用，模块会检索该消息并将其输出，同时更新时间戳。如果没有新消息可用，模块输出最后更新的 uORB 消息，并且时间戳不会更新。如果自仿真开始以来尚未接收到消息，则输出为零。

在正常模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
