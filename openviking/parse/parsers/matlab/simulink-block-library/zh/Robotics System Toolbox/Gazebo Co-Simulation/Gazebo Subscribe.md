---
type: simulink-block
title: 'Gazebo Subscribe'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazebosubscribe'
documentation_source_path: 'ref/gazebosubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Subscribe

## 端口

### 输出

### **IsNew** — 上一时间步自定义消息的状态 `0`（默认）| `1`

接收到的自定义消息的状态，以布尔值形式输出，指示模块输出 `Msg` 是否在上一时间步接收到。

**数据类型：** `Boolean`

### **Msg** — Gazebo 自定义消息总线

Gazebo 自定义消息，以总线信号形式输出，其元素与特定的 `Topic` 和 `Message type` 相关。

`Msg` 输出始终输出最近接收到的消息。

**数据类型：** `bus`

## 参数

### **Topic source** — 指定话题的来源 `From Gazebo`（默认）| `Specify your own`

要从现有的 Gazebo 仿真中获取话题，请选择 `From Gazebo`。点击 **Select** 按钮查看可用话题列表。要连接到 Gazebo 仿真，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

要在没有活动 Gazebo 连接的情况下输入自定义话题，请选择 `Specify your own`。使用 `Topic` 参数输入消息的名称。

### **Topic** — 自定义消息的话题名称 `/my_topic`（默认）| 字符串

自定义消息的话题名称，指定为字符串。

要从现有的 Gazebo 仿真中获取话题，请选择 `From Gazebo`。点击 **Select** 按钮查看可用话题列表。要连接到 Gazebo 仿真，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

要在不连接的情况下指定话题，请选择 `Specify your own`。

### **Message type** — Gazebo 自定义消息类型 `gazebo_msgs/TestPose`（默认）| 字符串

点击 **Select** 获取 Gazebo 中可用的消息类型列表。如果您从已连接的 Gazebo 仿真中选择 `Topic`，此参数将自动设置。

### **Sample time** — 输入的采样时间 `0.001`（默认）| 正数

采样时间表示从 Gazebo 仿真器接收消息的时间间隔。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从 Gazebo 服务器接收自定义消息

Gazebo Subscribe 模块根据模块指定的话题和消息类型，从 Gazebo 服务器接收自定义消息。该模块将最近接收到的消息以总线信号 `Msg` 输出，并输出一个布尔值 `IsNew`，指示上一时间步是否接收到消息。

要接收自定义消息，请连接到 Gazebo 仿真。打开模块封装并点击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

该模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。
