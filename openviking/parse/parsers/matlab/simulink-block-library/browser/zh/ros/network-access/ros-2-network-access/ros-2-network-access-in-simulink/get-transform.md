---
type: simulink-block
title: 'Get Transform'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'gettransformros2'
documentation_source_path: 'ref/gettransformros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Get Transform

## 端口

### 输出

### **IsAvail** — 变换可用性指示符 `0` | `1`

变换可用性指示符，以 logical 返回。如果输出为 `1`，则在最近一次采样命中时，ROS 2 网络上指定的源坐标系与目标坐标系之间存在一个变换。此输出可用于触发子系统，以处理 ROS 2 网络中收到的新变换。

**数据类型：** `Boolean`

### **Value** — 源坐标系与目标坐标系之间的齐次变换值 `geometry_msgs/TransformStamped` non-virtual bus（默认） | double

源坐标系与目标坐标系之间的齐次变换值，返回为 non-virtual bus 或 *4*×*4* double 矩阵。

## 参数

#### 主要参数

### **Frame source** — 用于指定坐标系的来源 `Select from ROS 2 network` | `Specify your own`

用于指定坐标系的来源，指定为以下之一：

- `Select from ROS 2 network` — 使用 **Select** 选择源坐标系和目标坐标系。**Target** 和 **Message type** 参数会自动设置。必须连接到 ROS 2 网络。
- `Specify your own` — 分别在 **Source** 和 **Target** 参数中手动输入源坐标系和目标坐标系。必须精确匹配坐标系名称。

### **Target** — 目标坐标系 string

目标坐标系，指定为 string。当 **Frame source** 设置为 `Select from ROS 2 network` 时，使用 **Select** 从 ROS 2 网络中选择一个坐标系。必须连接到 ROS 2 网络，才能获取网络变换树中可用坐标系的列表。否则，将 **Frame source** 设置为 `Specify your own`，并指定所需的坐标系。

### **Source** — 源坐标系 string

源坐标系，指定为 string。当 **Frame source** 设置为 `Select from ROS 2 network` 时，使用 **Select** 从 ROS 2 网络中选择一个坐标系。必须连接到 ROS 2 网络，才能获取网络变换树中可用坐标系的列表。否则，将 **Frame source** 设置为 `Specify your own`，并指定所需的坐标系。

### **Output format** — 输出变换值的格式 bus（默认） | double

输出变换值的格式，指定为以下选项之一：

- `bus` — `geometry_msgs/TransformStamped` non-virtual bus
- `double` — *4*×*4* double 矩阵

### **Sample time** — 输出之间的间隔 `–1`（默认） | scalar

输出之间的间隔，指定为 scalar。在仿真中，采样时间遵循仿真时间，而不是实际挂钟时间。

此默认值表示模块采样时间为 *inherited*。有关 inherited 采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

#### 动态监听器和静态监听器的服务质量 (QoS) 参数

### **History** — 在队列中存储变换的模式 `Keep last`（默认） | `Keep all`

确定在队列中存储变换的模式。排队中的变换将发送给后加入的监听器。如果队列中充满等待处理的变换，则旧变换将被丢弃，以便为新变换腾出空间。当设置为 `Keep last` 时，队列存储由 `Depth` 属性设置的变换数量。否则，当设置为 `Keep all` 时，队列存储所有变换，直到达到 MATLAB® 资源限制。

### **Depth** — 变换队列的大小 `1`（默认） | positive scalar

当 `History` 设置为 `Keep last` 时，变换队列中存储的变换数量。

### **Reliability** — 变换的传递保证 `Reliable`（默认） | `Best effort`

影响变换传递的保证。如果为 `Reliable`，则保证传递，但可能重试多次。如果为 `Best effort`，则尝试传递且不重试。

### **Durability** — 变换的持久性 `Volatile`（默认） | `Transient local`

影响 `tf` 或 `tf_static` 话题发布者中变换的持久性，这允许后加入的监听器接收由 `Depth` 指定的旧变换数量。如果为 `Volatile`，则变换不会持久保留。如果为 `Transient local`，则发布者将保留最近的变换。

### **Deadline** — 连续变换之间允许的最大时间量 `Inf`（默认） | positive scalar

连续变换之间允许的最大时间量，指定为 positive scalar。对于动态监听器 QoS 设置，此 deadline 参数指定 `tf` 话题上连续变换之间允许的最大间隔，而对于静态监听器 QoS 设置，它针对 `tf_static` 话题指定相同内容。

### **Lifespan** — 变换被视为有效的时间长度 `Inf`（默认） | positive scalar

变换被视为有效的时间长度，指定为 positive scalar。模块不处理在队列中持续时间超过指定 lifespan 的服务请求。

对于动态监听器 QoS 设置，此 lifespan 参数指定 `tf` 话题上变换被视为有效的时间长度，而对于静态监听器 QoS 设置，它针对 `tf_static` 话题指定相同内容。

### **Liveliness** — 模块提供的活跃性报告级别 `automatic`（默认）

模块作为动态监听器或静态监听器时提供的活跃性报告级别，指定为 `automatic`。

如果为 `automatic`，则在收到新的变换消息后，ROS 2 网络认为该模块在另一个 `Lease Duration` 内保持活跃。

### **Lease Duration** — 模块必须断言活跃性之前的最大时间量 `Inf`（默认） | positive scalar

模块作为静态或动态监听器必须断言活跃性之前的最大时间量，指定为 positive scalar。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从 ROS 2 网络获取源坐标系和目标坐标系之间的变换

Get Transform 模块从 ROS 2 网络读取指定源坐标系和目标坐标系之间的变换值。当不同坐标系之间的变换由 ROS 2 网络上的节点发布时，使用此模块。在每个仿真步中，模块检查指定坐标系之间是否有可用变换。如果有可用变换，模块输出 `geometry_msgs/TransformStamped` non-virtual bus，或输出作为 *4*×*4* double 矩阵的齐次变换矩阵。

可以使用输出变换值，通过 pre-multiply 约定将源坐标系中的点变换到目标坐标系。该模块可以访问并监听 ROS 2 网络上 `tf` 话题下具有动态变换的所有坐标系，以及 `tf_static` 话题下的静态变换。还可以在模块作为静态和动态变换监听器时，为其设置单独的服务质量 (QoS) 参数。
