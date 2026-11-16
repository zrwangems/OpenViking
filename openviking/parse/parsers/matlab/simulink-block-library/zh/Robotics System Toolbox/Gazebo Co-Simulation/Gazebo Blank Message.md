---
type: simulink-block
title: 'Gazebo Blank Message'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboblankmessage'
documentation_source_path: 'ref/gazeboblankmessage.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Blank Message

## 端口

### 输出

### **Msg** — 空白消息总线

空白消息，作为总线信号返回，其中包含与特定 `Message type` 相关的元素。`Msg` 输出始终输出最近接收到的消息。

有七种不同的消息类型，每种都有特定字段：

- `ApplyLinkWrench`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中连杆的名称。
  - `force_type` –– 可变大小 `uint8`
    数组，指定为 `'SET'` 或 `'ADD'`。
    `'SET'` 会覆盖指定 duration 内任何现有的力消息。`'ADD'` 会将值与现有消息相加。
  - `Fx, fy, fz` –– `double` 值，
    指定施加到 Gazebo 模型连杆上的力的大小，使用世界坐标和 Newtons。
  - `torque_type` –– 可变大小 `uint8`
    数组，指定为 `'SET'` 或 `'ADD'`。
    `'SET'` 会覆盖指定 duration 内任何现有的力矩消息。`'ADD'` 会将值与现有消息相加。
  - `Tx, ty, tz` –– `double` 值，
    指定施加到 Gazebo 模型连杆上的力矩大小，使用世界坐标和 Newton-meters。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `ApplyJointTorque`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `joint_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中关节的名称。
  - `index` –– `uint32` 整数，
    标识应将力矩施加到哪个关节轴。
  - `effort` –– `double` 标量值，
    指定要施加到关节的力矩或力的大小。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `SetLinkWorldPose`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中连杆的名称。
  - `world_pose` –– 总线，包含作为 `[x
    y
    z]` 和 `[x
    y
    z
    w]`
    `double` 向量的位置和方向，分别对应。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `SetLinkLinearVelocity`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中连杆的名称。
  - `velocity` –– 总线，包含作为 `[x
    y
    z]`
    `double` 向量的线速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `SetLinkAngularVelocity`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中连杆的名称。
  - `velocity` –– 总线，包含作为 `[x
    y
    z]`
    `double` 向量的角速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `SetJointPosition`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `joint_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中关节的名称。
  - `index` –– `uint32` 整数，
    标识应将力矩施加到哪个关节轴。
  - `position` –– `double` 标量值，
    表示关节位置。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

- `SetJointVelocity`:

  - `model_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型的名称。
  - `joint_name` –– 可变大小 `uint8`
    数组，表示 Gazebo 仿真器中模型中关节的名称。
  - `index` –– `uint32` 整数，
    标识应将力矩施加到哪个关节轴。
  - `velocity` –– `double` 标量值，
    表示关节速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加力矩的时长。

  **注意**

  `SetJointVelocity` 使用 *Set Instantaneous
  Velocity* 方法设置关节速度。有关更多信息，请参阅 Setting Velocity on Links And Joints。

**注意**

- 如果 `duration` 为 `1.005` seconds，则作为 bus 时将是 `1` second and `5000000` nanoseconds。

**数据类型：** `bus`

## 参数

### **Message type** — 消息类型 `ApplyLinkWrench` (默认) | `ApplyJointTorque` | `SetLinkWorldPose` | `SetLinkLinearVelocity` | `SetLinkAngularVelocity` | `SetJointPosition` | `SetJointVelocity`

单击 **Select** 获取 Gazebo 中可用的消息类型列表。

### **Sample time** — 输入的采样时间 `0.001` (默认) | positive

采样时间指示在仿真期间模块何时产生输出，以及（如果适用）何时更新其内部状态。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

创建空白 Gazebo 命令

Gazebo Blank Message 模块基于指定类型创建空白 Gazebo 消息或命令。模块输出是一个总线信号，其中包含该命令类型所需的元素。使用 Bus Assignment 模块修改总线信号中的特定字段。总线信号初始化为零值 (ground)。

要创建空白 Gazebo 命令，请连接到 Gazebo 仿真。打开模块封装，然后单击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

此模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。要查看基本示例，请参阅 Perform Co-Simulation Between Simulink and Gazebo。
