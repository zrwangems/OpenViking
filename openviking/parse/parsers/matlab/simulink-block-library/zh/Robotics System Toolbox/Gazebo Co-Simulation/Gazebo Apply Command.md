---
type: simulink-block
title: 'Gazebo Apply Command'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboapplycommand'
documentation_source_path: 'ref/gazeboapplycommand.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Apply Command

## 端口

### 输入

### **Cmd** — Gazebo Command bus

Gazebo 命令消息，指定为总线。该命令是针对指定模型连杆或关节的指令。使用 Gazebo Select Entity 模块将模型名称指定为总线信号的一部分。

有七种不同的命令类型，具有特定字段：

- `ApplyLinkWrench`：

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 模拟器中模型的名称。你可以
    使用 Gazebo
    Select Entity 模块指定此字段。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo
    模拟器中模型的连杆名称。你可以使用 Gazebo
    Select Entity 模块指定此字段。
  - `force_type` –– 可变大小 `uint8`
    数组，指定为 `'SET'` 或 `'ADD'`。
    `'SET'` 会在指定持续时间内覆盖任何现有力命令。`'ADD'` 会将数值与现有
    命令相加。
  - `Fx, fy, fz` –– `double` 值，
    指定施加到 Gazebo 模型连杆上的力的大小，采用世界
    坐标，单位为牛顿。
  - `torque_type` –– 可变大小 `uint8`
    数组，指定为 `'SET'` 或 `'ADD'`。
    `'SET'` 会在指定持续时间内覆盖任何现有力矩命令。`'ADD'` 会将数值与现有
    命令相加。
  - `Tx, ty, tz` –– `double` 值，
    指定施加到 Gazebo 模型连杆上的力矩大小，采用世界
    坐标，单位为牛顿米。
  - `duration` –– 总线，包含以
    `double` 整数表示的秒和纳秒，用于指定在仿真时间中施加
    力矩的时长。

- `ApplyJointTorque`：

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 模拟器中模型的名称。你可以
    使用 Gazebo
    Select Entity 模块指定此字段。
  - `joint_name` –– 可变大小 `uint8`
    数组，表示 Gazebo
    模拟器中模型的关节名称。你可以使用 Gazebo
    Select Entity 模块指定此字段。
  - `index` –– `uint32` 整数，
    用于标识力矩应施加到哪个关节轴。
  - `effort` –– `double` 标量值，
    指定施加到关节上的力矩或力的大小。
  - `duration` –– 总线，包含以
    `double` 整数表示的秒和纳秒，用于指定在仿真时间中施加
    力矩的时长。

- `SetLinkWorldPose`：

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 模拟器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo
    模拟器中模型的连杆名称。
  - `world_pose` –– 总线，分别包含以
    `[x
    y
    z]` 和 `[x
    y
    z
    w]`
    `double` 向量表示的位置和姿态。
  - `duration` –– 总线，包含以
    `double` 整数表示的秒和纳秒，用于指定在仿真时间中施加
    力矩的时长。

- `SetLinkLinearVelocity`：

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 模拟器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo
    模拟器中模型的连杆名称。
  - `velocity` –– 总线，包含以
    `[x
    y
    z]`
    `double` 向量表示的线速度。
  - `duration` –– 总线，包含以
    `double` 整数表示的秒和纳秒，用于指定在仿真时间中施加
    力矩的时长。

- `SetLinkAngularVelocity`：

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 模拟器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo
    模拟器中模型的连杆名称。
  - `velocity` –– 总线，包含以
    `[x
    y
    z]`
    `double` 向量表示的角速度。
  - `duration` –– 总线，包含以
    `double` 整数表示的秒和纳秒，用于指定在仿真时间中施加
    力矩的时长。

- `SetJointPosition`：

- `model_name` —— 可变大小 `uint8` 数组，表示 Gazebo 模拟器中模型的名称。
  - `joint_name` —— 可变大小 `uint8` 数组，表示 Gazebo 模拟器中模型关节的名称。
  - `index` —— `uint32` 整数，用于标识力矩应施加到哪个关节轴。
  - `position` —— `double` 标量值，表示关节位置。
  - `duration` —— 包含秒和纳秒的 Bus，以 `double` 整数表示，用于指定在仿真时间中施加力矩的时长。

- `SetJointVelocity`：

  - `model_name` —— 可变大小 `uint8` 数组，表示 Gazebo 模拟器中模型的名称。
  - `joint_name` —— 可变大小 `uint8` 数组，表示 Gazebo 模拟器中模型关节的名称。
  - `index` —— `uint32` 整数，用于标识力矩应施加到哪个关节轴。
  - `velocity` —— `double` 标量值，表示关节速度。
  - `duration` —— 包含秒和纳秒的 Bus，以 `double` 整数表示，用于指定在仿真时间中施加力矩的时长。

  **注意**

  `SetJointVelocity` 使用 *Set Instantaneous Velocity* 方法设置关节速度。有关更多信息，请参阅 Setting Velocity on Links And Joints。

**注意**

- 如果 `duration` 为 `1.005` 秒，则作为 Bus 将是 `1` 秒和 `5000000` 纳秒。

**数据类型：** `bus`

## 参数

### **Command type** —— 命令类型 `ApplyLinkWrench`（默认）| `ApplyJointTorque` | `SetLinkWorldPose` | `SetLinkLinearVelocity` | `SetLinkAngularVelocity` | `SetJointPosition` | `SetJointVelocity`

点击 **Select** 获取 Gazebo 中可用的命令类型列表。输入 `Cmd` 必须包含与此类型匹配的正确命令消息结构。

### **Sample time** —— 输入的采样时间 `0.001`（默认）| 正值

采样时间表示命令发送到 Gazebo 模拟器的时间间隔。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

向 Gazebo 模拟器发送命令

Apply Command 模块向 Gazebo 仿真发送命令。该模块接受作为 Bus 信号输入的命令消息，并将命令发送到 Gazebo 服务器。

要发送命令消息，请连接到 Gazebo 仿真。打开模块封装并点击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

该模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。要查看基本示例，请查看 Perform Co-Simulation Between Simulink and Gazebo。
