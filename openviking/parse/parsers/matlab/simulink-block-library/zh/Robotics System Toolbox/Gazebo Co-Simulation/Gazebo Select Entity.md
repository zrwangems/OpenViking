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
```yaml
ports:
- name: model
  summary: 实体的模型名称 model1（默认）| 字符串（uint8[]）
  direction: output
  data_types: uint8
- name: Joint/Link
  summary: 实体关联的关节或连杆名称 joint1（默认）| 字符串（uint8[]）
  direction: output
  data_types: uint8
```

### 输出

### **model** — 实体的模型名称 `model1`（默认）| 字符串（`uint8[]`）

实体的模型名称，以字符串标量形式输出。对于 Gazebo，字符串以可变大小的 `uint8` 数组形式输出。

**数据类型：** `uint8`

### **Joint/Link** — 实体关联的关节或连杆名称 joint1（默认）| 字符串（`uint8[]`）

关联的关节或连杆，以字符串标量形式输出。对于 Gazebo，字符串以 `uint8` 数组形式输出。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Model Name
  summary: 选择模型名称 'model1/joint1'（默认）| 字符串标量
  group: ''
- name: Output vector size upper bound
  summary: 输出数组的上限 128（默认）
  group: ''
```

### **Model Name** — 选择模型名称 `'model1/joint1'`（默认）| 字符串标量

通过点击 **Select** 选择模型，这将弹出 Gazebo 服务器上可用名称的列表。该模块假定您已连接到 Gazebo 仿真。如果未连接，请在模块封装中点击 **Configure Gazebo network and simulation settings**。

### **Output vector size upper bound** — 输出数组的上限 `128`（默认）

输出 `uint8` 数组 `Model Name` 和 `Joint/Link` 的大小上限。当名称长度超过默认值 `128` 时，请增大该上限。
## 所属库

Robotics System Toolbox / Gazebo Co-Simulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

选择 Gazebo 实体

Gazebo Select Entity 模块从仿真环境中检索 Gazebo 实体（如连杆或关节）的模型名称。该模块为模型以及关联的关节或连杆名称分别输出一个字符串。在使用 Gazebo Apply Command 模块指定命令时，请同时使用这两个名称。

在选择实体之前，请连接到 Gazebo 仿真。打开模块封装并点击 **Configure Gazebo network and simulation settings**。有关更多信息，请参阅 Configure Gazebo Simulation。

该模块是 MATLAB® 与 Gazebo 之间用于交换数据和发送命令的协同仿真接口的一部分。如需查看基本示例，请参阅 Perform Co-Simulation Between Simulink and Gazebo
