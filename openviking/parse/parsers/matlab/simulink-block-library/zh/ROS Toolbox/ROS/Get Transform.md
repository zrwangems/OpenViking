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

### **IsAvail** — 变换可用性指示 `0` | `1`

变换可用性指示，以逻辑值形式返回。如果输出为 `1`，则表示在最后一次采样命中时，ROS 网络上指定的源坐标系和目标坐标系之间存在变换。此输出可用于触发子系统，以处理 ROS 网络中接收到的新消息。

**数据类型：** `Boolean`

### **Value** — 源坐标系和目标坐标系之间的齐次变换值 `geometry_msgs/TransformStamped` 非虚拟总线（默认）| double

源坐标系和目标坐标系之间的齐次变换值，以非虚拟总线或 *4*×*4* double 矩阵形式返回。

## 参数

#### 主

### **Frame source** — 用于指定坐标系的来源 `Select from ROS network` | `Specify your own`

用于指定坐标系的来源，指定为以下选项之一：

- `Select from ROS network` — 使用 **Select** 选择源坐标系和目标坐标系。**Target** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own` — 分别在 **Source** 和 **Target** 参数中手动输入源坐标系和目标坐标系。您必须精确匹配坐标系名称。

### **Target** — 目标坐标系 字符串

目标坐标系，指定为字符串。当 **Frame source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择一个坐标系。您必须连接到 ROS 网络，才能获取网络变换树中可用的坐标系列表。否则，将 **Frame source** 设置为 `Specify your own` 并指定您想要的坐标系。

### **Source** — 源坐标系 字符串

源坐标系，指定为字符串。当 **Frame source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择一个坐标系。您必须连接到 ROS 网络，才能获取网络变换树中可用的坐标系列表。否则，将 **Frame source** 设置为 `Specify your own` 并指定您想要的坐标系。

### **Output format** — 输出变换值的格式 bus（默认）| double

输出变换值的格式，指定为以下选项之一：

- `bus` — `geometry_msgs/TransformStamped` 非虚拟总线
- `double` — *4*×*4* double 矩阵

### **Sample time** — 输出之间的间隔 `–1`（默认）| 标量

输出之间的间隔，指定为标量。在仿真中，采样时间遵循仿真时间，而不是实际的挂钟时间。

此默认值表示模块采样时间为*继承*。有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从 ROS 网络获取源坐标系和目标坐标系之间的变换

Get Transform 模块从 ROS 网络读取指定源坐标系和目标坐标系之间的变换值。当 ROS 网络上的节点发布不同坐标系之间的变换时，请使用此模块。在每个仿真步中，该模块检查指定坐标系之间是否存在变换。如果存在，该模块输出 `geometry_msgs/TransformStamped` 非虚拟总线或齐次变换矩阵（以 *4*×*4* double 矩阵形式）。

您可以使用输出变换值，通过预乘约定将源坐标系中的点变换到目标坐标系。该模块可以访问 ROS 网络上 `tf` 话题下具有动态变换的所有坐标系。
