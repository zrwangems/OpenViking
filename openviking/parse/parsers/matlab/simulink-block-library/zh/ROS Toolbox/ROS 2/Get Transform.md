---
type: simulink-block
title: 'Get Transform'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'gettransformros'
documentation_source_path: 'ref/gettransformros.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Transform

## 端口

### 输出

### **IsAvail** — 变换可用性指示符 `0` | `1`

变换可用性指示符，以逻辑值形式返回。如果输出为 `1`，则在最近一次采样命中时，ROS 网络上指定的源坐标帧和目标坐标帧之间存在变换。此输出可用于触发子系统，以处理 ROS 网络中接收到的新消息。

**数据类型：** `Boolean`

### **Value** — 源坐标帧和目标坐标帧之间的齐次变换值 `geometry_msgs/TransformStamped` non-virtual bus（默认）| double

源坐标帧和目标坐标帧之间的齐次变换值，以 non-virtual bus 或 *4*×*4* double 矩阵形式返回。

## 参数

#### 主要

### **Frame source** — 用于指定坐标帧的来源 `Select from ROS network` | `Specify your own`

用于指定坐标帧的来源，指定为以下之一：

- `Select from ROS network` — 使用 **Select** 选择源坐标帧和目标坐标帧。**Target** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own` — 分别在 **Source** 和 **Target** 参数中手动输入源坐标帧和目标坐标帧。您必须完全匹配坐标帧的名称。

### **Target** — 目标坐标帧 string

目标坐标帧，指定为 string。当 **Frame source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择一个坐标帧。您必须连接到 ROS 网络，才能获取网络变换树中可用坐标帧的列表。否则，将 **Frame source** 设置为 `Specify your own`，并指定您想要的坐标帧。

### **Source** — 源坐标帧 string

源坐标帧，指定为 string。当 **Frame source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择一个坐标帧。您必须连接到 ROS 网络，才能获取网络变换树中可用坐标帧的列表。否则，将 **Frame source** 设置为 `Specify your own`，并指定您想要的坐标帧。

### **Output format** — 输出变换值的格式 bus（默认）| double

输出变换值的格式，指定为以下选项之一：

- `bus` — `geometry_msgs/TransformStamped` non-virtual bus
- `double` — *4*×*4* double 矩阵

### **Sample time** — 输出之间的间隔 `–1`（默认）| scalar

输出之间的间隔，指定为 scalar。在仿真中，采样时间遵循仿真时间，而不是实际墙上时钟时间。

此默认值表示模块采样时间为*继承*。有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从 ROS 网络获取源坐标帧和目标坐标帧之间的变换

Get Transform 模块从 ROS 网络读取指定的源坐标帧和目标坐标帧之间的变换值。当 ROS 网络上的节点发布不同坐标帧之间的变换时，请使用此模块。在每个仿真步中，模块检查指定坐标帧之间是否有可用变换。如果有可用变换，模块会输出一个 `geometry_msgs/TransformStamped` non-virtual bus 或一个齐次变换矩阵，形式为 *4*×*4* double 矩阵。

您可以使用输出变换值，通过 pre-multiply 约定将源坐标帧中的点变换到目标坐标帧。该模块可以访问 ROS 网络上 `tf` 主题下具有动态变换的所有坐标帧。
