---
type: simulink-block
title: 'Send Joint Configuration'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robotics System Toolbox Supported Hardware / UR Series Manipulators / Get Started with Real-Time Data Exchange (RTDE) Connectivity Interface'
documentation_page: 'sendjointconfiguration'
documentation_source_path: 'urseries/ref/sendjointconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Send Joint Configuration

## 端口

### 输入

### **q** — 用于完成轨迹的关节配置数值向量

用于完成轨迹的关节配置（以 radians 为单位），指定为 1-by-6 vector，其中 N 是轨迹的维度。

**数据类型：** `double`

### **Enable** — 启用模块以接受关节配置 `1` | `0`

启用模块，并基于关节路点激活 cobot 的运动。将端口设置为以下值之一：

- `1` – 启用模块以接受 **q** 输入
  并执行运动
- `0` – 禁用模块并忽略 **q**
  输入

**数据类型：** `Boolean`

## 参数

### **UR Controller IP 地址** — UR Controller 的 IP 地址 `192.168.1.10` (默认) | scalar

指定与要建立连接的 UR Series cobot 对应的 UR Controller 的 IP 地址。

### **等待运动完成** — 基于先前的关节配置等待运动完成 `on` (默认) | `off`

基于发送给 cobot 的先前关节配置，等待 cobot 的运动完成。选中此参数时，发送操作以阻塞模式运行（它会挂起所有其他 MATLAB 任务，直到 cobot 的运动完成）。清除此参数时，发送操作以非阻塞模式运行。

### **控制模式** — cobot 梯形运动的控制模式 `Time-Based Control` (默认) | `Acceleration and Velocity based Control`

基于指定的关节配置，cobot 梯形运动的控制模式。

### **启用 End Time 输入端口** — 启用用于指定结束时间的附加输入端口 `off` (默认) | on

启用附加输入端口 **End Time**，以指定完成运动的时间。选择此参数会禁用使用 **完成运动的结束时间** 参数手动输入结束时间值的选项。

#### 依赖关系

仅当为 **控制模式** 参数选择 `Time-Based Control` 时，此参数才会出现。

### **完成运动的结束时间** — 基于指定的关节配置完成运动的时间 `5` (默认) | numeric scalar

基于指定的关节配置完成 cobot 运动所需的结束时间（以 seconds 为单位），指定为 numeric scalar。

#### 依赖关系

仅当未选择 **启用 End Time 输入端口** 参数时，此参数才会出现。

### **启用 Acceleration 输入端口** — 启用用于加速度的输入端口 `off` (默认) | `on`

启用附加输入端口以提供加速度值。选择此参数会禁用使用 **用于控制速度剖面的加速度** 参数手动输入加速度值的选项。

#### 依赖关系

仅当为 **控制模式** 选择 `Acceleration and Velocity based Control` 时，此参数才会出现。

### **启用 Velocity 输入端口** — 启用用于速度的输入端口 `off` (默认) | `on`

启用附加输入端口以提供速度值。选择此参数会禁用使用 **用于控制速度剖面的速度** 参数手动输入速度值的选项。

#### 依赖关系

仅当为 **控制模式** 选择 `Acceleration and Velocity based Control` 时，此参数才会出现。

### **用于控制速度剖面的加速度** — 用于控制速度剖面的加速度 `1` (默认) | numeric scalar

用于控制轨迹速度剖面的加速度（以 rad/s² 为单位），指定为 numeric scalar。

#### 依赖关系

仅当未选择 **启用 Acceleration 输入端口** 参数时，此参数才会出现。

### **用于控制速度剖面的速度** — 用于控制速度剖面的速度 `1` (默认) | numeric scalar

用于控制轨迹速度剖面的速度（以 rad/s 为单位），指定为 numeric scalar。

#### 依赖关系

仅当未选择 **启用 Velocity 输入端口** 参数时，此参数才会出现。

## 所属库

Robotics System Toolbox Support Package for Universal Robots UR Series Manipulators / UR RTDE Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 RTDE 接口命令 UR cobot 移动到指定的关节配置

Send Joint Configuration 模块使用 RTDE 接口命令 UR cobot 移动到指定的关节配置，以完成轨迹。该模块还允许您指定附加约束（如结束时间、速度或加速度）来完成运动；否则，它会为这些约束使用默认值。

该模块以阻塞模式或非阻塞模式发送命令。在阻塞模式下，模型在等待运动完成时会阻止执行。在非阻塞模式下，模型持续运行。
