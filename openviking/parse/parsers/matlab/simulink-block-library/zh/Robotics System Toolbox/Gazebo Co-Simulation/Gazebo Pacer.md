---
type: simulink-block
title: 'Gazebo Pacer'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazebopacer'
documentation_source_path: 'ref/gazebopacer.html'
language: zh-CN
chinese_source: worker-translation
---

# Gazebo Pacer

## 端口
```yaml
ports:
- name: Status
  summary: 同步状态 0 | 1
  direction: output
  data_types: uint8
```

### 输出

### **Status** — 同步状态 0 | 1

同步状态，输出为 `0` 或 `1`。值为 `0` 表示时间同步成功。值为 `1` 表示仿真不同步。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Reset behavior
  summary: 重置仿真时间或场景 Reset Gazebo simulation time（默认）| Reset Gazebo simulation time and scene
  group: ''
- name: Sample time
  summary: 输入的采样时间 0.001（默认）| 正值
  group: ''
```

### **Reset behavior** — 重置仿真时间或场景 `Reset Gazebo simulation time`（默认）| `Reset Gazebo simulation time and scene`

从 Reset behavior 下拉列表中选择。

- `Reset Gazebo simulation time` — 重置 Gazebo 仿真器时间。
- `Reset Gazebo simulation time and scene` — 同时重置 Gazebo 仿真器时间和场景。

### **Sample time** — 输入的采样时间 `0.001`（默认）| 正值

将 Sample time 参数设置为按给定速率步进 Gazebo 仿真。该参数必须是 Gazebo 求解器最大步长的整数倍。
## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

Gazebo 与 Simulink 之间同步步进的设置

Gazebo Pacer 模块同步 Gazebo 与 Simulink® 之间的仿真时间。同步对于确保您的 Simulink 模型和 Gazebo 仿真正确运行非常重要。该模块输出一个布尔值，指示同步是否成功。同步步进仅支持一个 Gazebo 仿真。您的整个模型（包括被引用的模型）只能包含一个 Gazebo Pacer 模块。

为确保同步成功，请连接到 Gazebo 仿真。打开模块封装，然后点击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

选择 `Reset behavior` 以在模型重启时重置 Gazebo 仿真，或仅重置仿真时间。

该模块是 MATLAB® 与 Gazebo 之间协同仿真接口的一部分，用于交换数据和发送命令。如需查看基本示例，请参阅 Perform Co-Simulation Between Simulink and Gazebo。
