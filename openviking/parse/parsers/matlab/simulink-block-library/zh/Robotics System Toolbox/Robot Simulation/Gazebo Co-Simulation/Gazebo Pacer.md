---
type: simulink-block
title: 'Gazebo Pacer'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / Gazebo Co-Simulation'
documentation_page: 'gazebopacer'
documentation_source_path: 'ref/gazebopacer.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Pacer

## 端口

### 输出

### **Status** — 同步状态 0 | 1

同步状态，输出为 `0` 或 `1`。值 `0` 表示时间同步成功。值 `1` 表示仿真不同步。

**数据类型：** `uint8`

## 参数

### **Reset behavior** — 重置仿真时间或场景 `Reset Gazebo simulation time`（默认）| `Reset Gazebo simulation time and scene`

从 Reset behavior 下拉列表中选择。

- `Reset Gazebo simulation time` — 重置 Gazebo
  仿真器时间。
- `Reset Gazebo simulation time and scene` — 同时重置
  Gazebo 仿真器时间和场景。

### **Sample time** — 输入的采样时间 `0.001`（默认）| 正数

设置 Sample time 参数，以给定速率步进 Gazebo 仿真。此参数必须是 Gazebo 求解器最大步长的倍数。

## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

Gazebo 和 Simulink 之间同步步进的设置

Gazebo Pacer 模块在 Gazebo 和 Simulink® 之间同步仿真时间。同步对于确保您的 Simulink 模型和 Gazebo 仿真行为正确非常重要。该模块输出一个 Boolean，指示同步是否成功。同步步进仅支持一个 Gazebo 仿真。您的整个模型（包括引用模型）只能包含一个 Gazebo Pacer 模块。

为确保成功同步，请连接到 Gazebo 仿真。打开模块封装，然后点击 **配置 Gazebo 网络和仿真设置**。有关详细信息，请参阅配置 Gazebo 仿真。

选择 `Reset behavior` 以在模型重启时重置 Gazebo 仿真，或仅重置仿真时间。

此模块是 MATLAB® 和 Gazebo 之间的协同仿真接口的一部分，用于交换数据和发送命令。要查看基本示例，请参阅在 Simulink 和 Gazebo 之间执行协同仿真。
