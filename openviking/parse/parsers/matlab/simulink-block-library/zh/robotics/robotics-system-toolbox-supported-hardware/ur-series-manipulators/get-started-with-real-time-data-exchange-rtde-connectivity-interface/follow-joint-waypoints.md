---
type: simulink-block
title: 'Follow Joint Waypoints'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'followjointwaypoints'
documentation_source_path: 'urseries/ref/followjointwaypoints.html'
language: zh-CN
chinese_source: worker-translation
---

# Follow Joint Waypoints

## 端口

### 输入

### **Waypoints** — 用于完成轨迹的关节空间路点 numeric vector

用于完成轨迹的关节空间路点（以 radians 为单位），指定为 `N`-by-6 numeric vector，其中 `N` 是轨迹的维度。

**数据类型：** `double`

### **Valid Waypoints** — 供协作机器人遵循的有效路点数量 numeric scalar

当所需的关节空间路点（使用 **Waypoints** 输入端口）不是直接提供，而是由另一个模块生成时，您希望协作机器人遵循的有效路点数量（N）。

#### 依赖关系

仅当您选择参数 **Enable Valid Number of Waypoints input port** 时，此端口才会出现。

.

**数据类型：** `double`

### **Waypoint Times** — 每个路点段完成运动的绝对时间 numeric vector

每个路点段完成运动的绝对时间（从开始计时），以 seconds 为单位，指定为 1-by-N numeric vector。

#### 依赖关系

仅当您同时选择以下两个选项时，此端口才会出现：**Type of Motion** 的 `Trapezoidal Motion` 和 **Mode of Control** 的 `Time-based control`。

.

**数据类型：** `double`

### **Enable** — 使模块能够接受路点 `1` | `0`

启用模块，并根据关节路点激活协作机器人的运动。将此端口设置为以下值之一：

- `1` – 使模块能够接受 **Waypoints** 输入并执行运动
- `0` – 禁用模块并忽略 **Waypoints** 输入

**数据类型：** `Boolean`

## 参数

### **UR Controller IP address** — UR Controller 的 IP 地址 `192.168.1.10` (默认) | scalar

指定与您要建立连接的 UR Series 协作机器人对应的 UR Controller 的 IP 地址。

### **Cobot model** — UR Series 协作机器人的型号名称 `UR5e` (默认) | `UR3` | `UR3e` | `UR5` | `UR10` | `UR10e` | `UR16e`

您要建立连接的 UR Series 协作机器人的型号名称。

### **Enable Valid Number of Waypoints input port** — 启用额外输入端口以指定有效路点数量 `off` (默认) | on

启用额外输入端口 **Valid Number of Waypoints**，以指定当 **Waypoints** 输入由另一个模块生成时要考虑的有效路点数量（N）。

### **Type of motion** — 完成轨迹时要考虑的运动类型 `Smooth Motion` (默认) | `Trapezoidal Motion`

基于指定的关节空间路点，完成轨迹时要考虑的运动类型：

- 如果选择 `Smooth motion` 选项，则要么使用为 **Blend radius for waypoints to pass through** 参数指定的默认值，要么为该参数指定不同的值。为 smooth motion 指定加速度和速度是可选的，并且可以使用该模块的 **Motion Control** 选项卡下的选项来完成。
- 如果选择 `Trapezoidal motion` 选项，则使用 **Mode of control** 参数，通过该模块的 **Motion Control** 选项卡下的选项，进一步在 acceleration and velocity control 或 time-based control 之间选择。

### **Mode of control** — 协作机器人 trapezoidal motion 的控制模式 `Acceleration and Velocity based Control` (默认) | `Time-Based Control`

基于指定的关节空间路点，协作机器人 trapezoidal motion 的控制模式。

#### 依赖关系

要启用此参数，请为 **Type of Motion** 参数选择 `Trapezoidal Motion` 选项。

### **Blend radius for waypoints to pass through** — 用于完成 smooth motion 的混合半径 `0.05` (默认) | numeric scalar

基于关节路点输入，用于完成协作机器人 smooth motion 的混合半径（以 meters 为单位），指定为 numeric scalar。

#### 依赖关系

要启用此参数，请为 **Type of Motion** 参数选择 `Smooth Motion` 选项。

### **Enable Acceleration input port** — 启用加速度输入端口 `off` (默认) | `on`

启用额外输入端口以提供加速度值，用于协作机器人的 smooth motion 或 trapezoidal motion。选择此参数会禁用使用 **Acceleration to control speed profile** 参数手动输入加速度值的选项。

#### 依赖关系

此参数在以下选项时出现：

- 为 **Type of Motion** 选择 `Smooth Motion`
- 为 **Type of Motion** 选择 `Trapezoidal Motion`，并为 **Mode of Control** 选择 `Acceleration and Velocity based Control`

### **Enable Velocity input port** — 启用速度输入端口 `off` (默认) | `on`

启用额外输入端口以提供速度值，用于协作机器人的 smooth motion 或 trapezoidal motion。选择此参数会禁用使用 **Velocity to control speed profile** 参数手动输入速度值的选项。

#### 依赖关系

此参数在以下选项时出现：

- 为 **Type of Motion** 选择 `Smooth Motion`
- 为 **Type of Motion** 选择 `Trapezoidal Motion`，并为 **Mode of Control** 选择 `Acceleration and Velocity based Control`

### **Acceleration to control speed profile** — 用于控制速度曲线的加速度 `1` (默认) | numeric scalar

用于控制轨迹速度曲线的加速度（以 rad/s² 为单位），指定为 numeric scalar。

#### 依赖关系

仅当未选择 **Enable Acceleration input port** 参数时，此参数才会出现。

### **Velocity to control speed profile** — 用于控制速度曲线的速度 `1` (默认) | numeric scalar

用于控制轨迹速度曲线的速度（以 rad/s 为单位），指定为 numeric scalar。

#### 依赖关系

仅当未选择 **Enable Velocity input port** 参数时，此参数才会出现。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 RTDE 接口命令 UR Series 协作机器人遵循指定的关节位置集合

Follow Joint Waypoints 模块使用 RTDE 接口命令 UR Series 协作机器人遵循一组指定的关节位置以完成轨迹。该模块允许您在 smooth motion 或 trapezoidal motion 之间选择，并为 trapezoidal motion 提供额外控制选项。
