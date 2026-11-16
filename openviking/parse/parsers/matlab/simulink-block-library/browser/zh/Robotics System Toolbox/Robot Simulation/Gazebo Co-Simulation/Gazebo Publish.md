---
type: simulink-block
title: 'Gazebo Publish'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / Gazebo Co-Simulation'
documentation_page: 'gazebopublish'
documentation_source_path: 'ref/gazebopublish.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Publish

## 端口

### 输入

### **Msg** — Gazebo 自定义消息总线

Gazebo 自定义消息，指定为总线信号，其元素与特定的 `Topic` 和 `Message type` 相关。

**数据类型：** `bus`

## 参数

### **Topic source** — 用于指定主题的源 `From Gazebo`（默认）| `Specify your own`

要从现有 Gazebo 仿真获取主题，请选择 `From Gazebo`。点击 **Select** 按钮查看可用主题列表。要连接到 Gazebo 仿真，请在模块掩码中点击 **Configure Gazebo network and simulation settings**。

要在没有活动 Gazebo 连接的情况下输入自定义主题，请选择 `Specify your own`。使用 `Topic` 参数键入消息的名称。

### **Topic** — 自定义消息的主题名称 `/my_topic`（默认）| string

自定义消息的主题名称，指定为字符串。

要从现有 Gazebo 仿真获取主题，请选择 `From Gazebo`。点击 **Select** 按钮查看可用主题列表。要连接到 Gazebo 仿真，请在模块掩码中点击 **Configure Gazebo network and simulation settings**。

要在不连接的情况下指定主题，请选择 `Specify your own`。

### **Message type** — Gazebo 自定义消息类型 `gazebo_msgs/TestPose`（默认）| string

点击 **Select** 获取 Gazebo 中可用的消息类型列表。如果您从已连接的 Gazebo 仿真中选择 `Topic`，此参数将自动设置。

### **Sample time** — 输入的采样时间 `0.001`（默认）| positive

采样时间指示将消息发送到 Gazebo 模拟器的间隔。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

将自定义消息发送到 Gazebo 服务器

Gazebo Publish 模块根据该模块指定的主题和消息类型，将自定义消息发送到 Gazebo 服务器。

要发送自定义消息，请连接到 Gazebo 仿真。打开模块掩码，然后点击 **Configure Gazebo network and simulation settings**。有关详细信息，请参阅 Configure Gazebo Simulation。

此模块是 MATLAB® 和 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。
