---
type: simulink-block
title: 'PX4 Analog Input'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4analoginput'
documentation_source_path: 'px4/ref/px4analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 Analog Input

## 端口

### 输出

### **Port\_1** — 以 1-by-12 数组表示的电压值 analog

在飞控板上的不同 ADC 通道捕获的电压值。

将此输出连接到 Selector block，并将其 `Input port size` 参数值设置为 `12`。您可以使用 Selector block 指定所需通道编号的索引值，以便从这些通道读取电压值。

**数据类型：** `vector`

## 参数

### **Sample time** — 模块读取模拟电压值的时间间隔 `0.001`（默认值）| 任何为 0.001 的倍数的非负值 | -1

输入该模块从飞控板上的 ADC 通道读取电压值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

测量施加到 ADC 通道的模拟电压

PX4 Analog Input 模块测量 PX4® 飞控硬件上 ADC 通道的模拟电压，并将这些电压输出为 1-by-12 数组。数组中的每个值对应于特定通道编号处的模拟电压。

有关映射通道编号和电压数组的详细信息，请参阅 Index Numbers for Analog Channels on Pixhawk Series Controller Boards。

在 Normal 模式仿真期间，该模块输出零。

在 Connected I/O 仿真期间，该模块从硬件的外设读取数据。
