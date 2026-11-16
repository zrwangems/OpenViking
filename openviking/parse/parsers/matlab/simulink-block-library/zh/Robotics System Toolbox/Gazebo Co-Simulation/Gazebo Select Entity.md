---
type: simulink-block
title: 'Gazebo Select Entity'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboselectentity'
documentation_source_path: 'ref/gazeboselectentity.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Select Entity

## 端口

### 输出

### **model** — 实体的模型名称 `model1`（默认）| string (`uint8[]`)

实体的模型名称，以 string 标量形式输出。对于 Gazebo，字符串以可变大小 `uint8` 数组形式输出。

**数据类型：** `uint8`

### **Joint/Link** — 实体的关联关节或连杆名称 joint1（默认）| string (`uint8[]`)

关联的关节或连杆，以 string 标量形式输出。对于 Gazebo，字符串以 `uint8` 数组形式输出。

**数据类型：** `uint8`

## 参数

### **Model Name** — 选择模型名称 `'model1/joint1'`（默认）| string scalar

点击 **Select** 选择模型，这会显示 Gazebo 服务器上可用名称的列表。该模块假设您已连接到 Gazebo 仿真。如果未连接，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

### **Output vector size upper bound** — 输出数组的上限 `128`（默认）

输出 `uint8` 数组 `Model Name` 和 `Joint/Link` 的大小上限。当名称长于默认值 `128` 时，增大该上限。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019b 中引入**

## 描述

选择 Gazebo 实体

Gazebo Select Entity 模块从仿真环境中检索 Gazebo 实体（例如连杆或关节）的模型名称。该模块为模型名称以及关联的关节或连杆名称输出字符串。在使用 Gazebo Apply Command 模块指定命令时，请同时使用这两个名称。

在选择实体之前，请连接到 Gazebo 仿真。打开模块封装，然后点击 **Configure Gazebo network and simulation settings**。有关详细信息，请参阅配置 Gazebo 仿真。

该模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的联合仿真接口的一部分。要查看基本示例，请查看在 Simulink 与 Gazebo 之间执行联合仿真。
