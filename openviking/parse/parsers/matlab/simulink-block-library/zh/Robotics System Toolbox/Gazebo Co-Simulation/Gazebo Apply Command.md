---
type: simulink-block
title: 'Gazebo Apply Command'
family: 'gazebo-co-simulation'
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

### **Cmd** — Gazebo 命令总线

Gazebo 命令消息，指定为总线。该命令是针对指定模型连杆或关节的指令。使用 Gazebo Select Entity 模块将模型名称指定为总线信号的一部分。

有七种不同的命令类型，每种类型都有特定字段：

- `ApplyLinkWrench`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。可以使用 Gazebo Select Entity 模块指定此字段。
  - `link_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型连杆的名称。可以使用 Gazebo Select Entity 模块指定此字段。
  - `force_type` –– 可变大小 `uint8` 数组，指定为 `'SET'` 或 `'ADD'`。`'SET'` 会在指定持续时间内覆盖任何现有力命令。`'ADD'` 会将该值与现有命令相加。
  - `Fx, fy, fz` –– `double` 值，指定在世界坐标中施加到 Gazebo 模型连杆上的力的大小，单位为 Newtons。
  - `torque_type` –– 可变大小 `uint8` 数组，指定为 `'SET'` 或 `'ADD'`。`'SET'` 会在指定持续时间内覆盖任何现有扭矩命令。`'ADD'` 会将该值与现有命令相加。
  - `Tx, ty, tz` –– `double` 值，指定在世界坐标中施加到 Gazebo 模型连杆上的扭矩的大小，单位为 Newton-meters。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `ApplyJointTorque`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。可以使用 Gazebo Select Entity 模块指定此字段。
  - `joint_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型关节的名称。可以使用 Gazebo Select Entity 模块指定此字段。
  - `index` –– `uint32` 整数，用于标识应将扭矩施加到哪个关节轴。
  - `effort` –– `double` 标量值，指定要施加到关节的扭矩或力的大小。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `SetLinkWorldPose`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型连杆的名称。
  - `world_pose` –– 总线，分别包含作为
    `[x
    y
    z]` 和 `[x
    y
    z
    w]`
    `double` 向量的位置和姿态。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `SetLinkLinearVelocity`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型连杆的名称。
  - `velocity` –– 总线，包含作为
    `[x
    y
    z]`
    `double` 向量的线速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `SetLinkAngularVelocity`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。
  - `link_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型连杆的名称。
  - `velocity` –– 总线，包含作为
    `[x
    y
    z]`
    `double` 向量的角速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `SetJointPosition`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。
  - `joint_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型关节的名称。
  - `index` –– `uint32` 整数，用于标识应将扭矩施加到哪个关节轴。
  - `position` –– `double` 标量值，表示关节位置。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

- `SetJointVelocity`:

  - `model_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型的名称。
  - `joint_name` –– 可变大小 `uint8` 数组，表示 Gazebo 仿真器中模型关节的名称。
  - `index` –– `uint32` 整数，用于标识应将扭矩施加到哪个关节轴。
  - `velocity` –– `double` 标量值，表示关节速度。
  - `duration` –– 总线，包含作为 `double` 整数的 seconds 和 nanoseconds，用于指定在仿真时间中施加扭矩的时长。

  **注意**

  `SetJointVelocity` 使用 *Set Instantaneous
  Velocity* 方法来设置关节速度。有关详细信息，请参阅 Setting Velocity on Links And Joints。

**注意**

- 如果 `duration` 为 `1.005` seconds，则作为总线将是 `1` second 和 `5000000` nanoseconds。

**数据类型：** `bus`

## 参数

### **命令类型** — 命令的类型 `ApplyLinkWrench` (默认) | `ApplyJointTorque` | `SetLinkWorldPose` | `SetLinkLinearVelocity` | `SetLinkAngularVelocity` | `SetJointPosition` | `SetJointVelocity`

点击 **Select** 获取 Gazebo 中可用的命令类型列表。输入 `Cmd` 必须包含与此类型匹配的正确命令消息结构。

### **采样时间** — 输入的采样时间 `0.001` (默认) | 正数

采样时间指示命令发送到 Gazebo 仿真器的间隔。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

## 描述

向 Gazebo 仿真器发送命令

Apply Command 模块向 Gazebo 仿真发送命令。该模块接受作为总线信号输入的命令消息，并将该命令发送到 Gazebo 服务器。

要发送命令消息，请连接到 Gazebo 仿真。打开模块封装，然后点击 **Configure Gazebo network and simulation settings**。有关详细信息，请参阅 Configure Gazebo Simulation。

此模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的联合仿真接口的一部分。要查看基本示例，请查看 Perform Co-Simulation Between Simulink and Gazebo。
