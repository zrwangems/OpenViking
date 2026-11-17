---
type: simulink-block
title: 'Gazebo Read'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboread'
documentation_source_path: 'ref/gazeboread.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Read

## 端口
```yaml
ports:
- name: IsNew
  summary: 上一时间步中消息的状态 0（默认）| 1
  direction: output
  data_types: Boolean
- name: Msg
  summary: Gazebo 消息总线
  direction: output
  data_types: bus
```

### 输出

### **IsNew** — 上一时间步中消息的状态 `0`（默认）| `1`

接收到的消息的状态，以布尔值输出，指示模块输出 `Msg` 是否在上一时间步中接收到。

**数据类型：** `Boolean`

### **Msg** — Gazebo 消息总线

Gazebo 消息，以总线信号输出，其元素与特定的 `Topic` 和 `Message type` 相关。

`Msg` 输出始终输出最近接收到的消息。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Topic source
  summary: 用于指定 topic 的来源 From Gazebo（默认）| Specify your own
  group: ''
- name: Topic
  summary: 消息的 topic 名称 /my_topic（默认）| 字符串
  group: ''
- name: Message type
  summary: Gazebo 消息类型 gazebo_msgs/Pose（默认）| gazebo_msgs/Image | gazebo_msgs/IMU | gazebo_msgs/LaserScan | gazebo_msgs/JointState
    | gazebo_msgs/LinkState
  group: ''
- name: Sample time
  summary: 输入的采样时间 0.001（默认）| 正标量
  group: ''
- name: Number of Joint Axis
  summary: 关节轴数量 2（默认）| 范围 [1, 100] 内的正整数
  group: ''
```

### **Topic source** — 用于指定 topic 的来源 `From Gazebo`（默认）| `Specify your own`

要从现有的 Gazebo 仿真中获取 topic，请选择 `From Gazebo`。点击 **Select** 按钮查看可用 topic 的列表。要连接到 Gazebo 仿真，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

要在没有活动 Gazebo 连接的情况下输入自定义 topic，请选择 `Specify your own`。使用 `Topic` 参数输入消息的名称。

### **Topic** — 消息的 topic 名称 `/my_topic`（默认）| 字符串

消息的 topic 名称，指定为字符串。

要从现有的 Gazebo 仿真中获取 topic，请选择 `From Gazebo`。点击 **Select** 按钮查看可用 topic 的列表。要连接到 Gazebo 仿真，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

要在不连接的情况下指定 topic，请选择 `Specify your own`。

### **Message type** — Gazebo 消息类型 `gazebo_msgs/Pose`（默认）| `gazebo_msgs/Image` | `gazebo_msgs/IMU` | `gazebo_msgs/LaserScan` | `gazebo_msgs/JointState` | `gazebo_msgs/LinkState`

点击 **Select** 获取 Gazebo 中可用的消息类型列表。如果您从已连接的 Gazebo 仿真中选择 `Topic`，此参数将自动设置。

### **Sample time** — 输入的采样时间 `0.001`（默认）| 正标量

采样时间指示模块在仿真期间何时产生输出，并在适当的情况下更新其内部状态。

### **Number of Joint Axis** — 关节轴数量 `2`（默认）| 范围 `[1, 100]` 内的正整数

选择 `Make Joint Axis Related Bus Signal to Fixed Dimensions` 以将关节轴相关的总线信号从可变维度转换为固定维度。然后指定关节轴数量。

#### 依赖关系

要启用此参数，请将 `Message type` 设置为 `gazebo_msgs/JointState`，并选中 `Make Joint Axis Related Bus Signal to Fixed Dimensions` 复选框。
## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从 Gazebo 服务器接收消息

Gazebo Read 模块根据模块指定的 topic 和消息类型从 Gazebo 服务器接收消息。该模块将最近接收到的消息以总线信号 `Msg` 输出，并输出一个布尔值 `IsNew`，指示在上一时间步中是否接收到消息。

要从 Gazebo 服务器接收消息，请连接到 Gazebo 仿真。打开模块封装并点击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

此模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。要查看基本示例，请查看 Perform Co-Simulation Between Simulink and Gazebo
