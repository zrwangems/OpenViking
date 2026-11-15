---
type: simulink-block
title: 'PX4 uORB Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbwrite'
documentation_source_path: 'px4/ref/px4uorbwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 uORB Write

## 端口

### 输入

### **Msg** — uORB 消息，指定为非虚拟总线 非虚拟总线

要指定 uORB 消息的类型，请使用参数 `Topic to Publish to`。

**数据类型：** `bus`

## 参数

#### 主选项卡

### **要发布到的主题** — 需要将消息发布到的 uORB 主题的名称 vehicle\_gps\_position（默认）| uORB 主题之一

选择该模块需要发布到的 uORB 主题的名称。单击 **Select** 以浏览已下载的 `px4` 目录的 `Firmware/msg` 文件夹中可用的主题名称。

### **选择实例** — 需要将消息发布到的 uORB 主题的实例 uORB 主题的实例

选择该模块需要需要发布到的 uORB 主题的实例。

#### 依赖关系

仅当您在 **要发布到的主题** 参数中选择支持多个实例的主题时，此参数才会出现。

例如，`actuator_controls` 主题支持多个实例，您可以从下拉列表中选择一个实例。

#### 高级选项卡

### **发布队列长度** — 缓冲元素的最大数量 `1`（默认）| integer

输入发布队列中缓冲元素的最大数量。如果该值为 `1`，则发布数据时不使用排队。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

为指定的 uORB 主题写入 uORB 数据

PX4 uORB Write 模块接受与指定 uORB 主题对应的 Simulink® 非虚拟总线，并将消息发布到 uORB 网络。

在每个采样命中时，该模块将 `Msg` 输入从 Simulink 总线信号转换为 uORB 消息并发布。该模块不区分输入是否为新消息；而只是在每个采样命中时发布它。

在 Connected I/O 仿真期间，此模块将数据写入硬件的外设。
