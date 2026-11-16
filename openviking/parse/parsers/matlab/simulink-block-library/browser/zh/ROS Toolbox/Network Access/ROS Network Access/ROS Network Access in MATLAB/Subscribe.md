---
type: simulink-block
title: 'Subscribe'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in MATLAB'
documentation_page: 'subscribe'
documentation_source_path: 'ref/subscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# Subscribe

## 端口

### 输出

### **IsNew** — 新消息指示符 `0` | `1`

新消息指示符，返回为 logical。如果输出为 `1`，则自上次采样命中以来已接收到一条新消息。此输出可用于触发子系统，以处理 ROS 网络中接收到的新消息。

### **Msg** — ROS 消息非虚拟总线

ROS 消息，返回为非虚拟总线。ROS 消息的类型由 **Message type** 参数指定。Subscribe 模块在接收到你指定话题名称上的消息之前，输出空白消息。这些空白消息允许你在网络其余部分设置完成之前创建和测试完整模型。

**数据类型：** `bus`

## 参数

### **Topic source** — 用于指定话题名称的来源 `Select from ROS network` | `Specify your own`

用于指定话题名称的来源，指定为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择话题名称。**Topic** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Topic** 中输入话题名称，并在 **Message type** 中指定其消息类型。您必须精确匹配话题名称。

### **Topic** — 要订阅的话题名称 string

要订阅的话题名称，指定为 string。当 **Topic source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择话题。您必须连接到 ROS 网络才能获取话题列表。否则，将 **Topic source** 设置为 `Specify your own`，并指定您想要的话题。

### **Message type** — ROS 消息类型 string

ROS 消息类型，指定为 string。使用 **Select** 从支持的 ROS 消息完整列表中选择。服务消息类型不受支持，并且不包含在列表中。

### **Sample time** — 输出之间的间隔 `–1`（默认）| scalar

输出之间的间隔，指定为 scalar。在仿真中，采样时间遵循仿真时间，而不是实际时钟时间。

此默认值表示该模块采样时间为*继承*。

有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

### **Length of subscribe callback queue** — 消息队列长度 `1`（默认）| integer

代码生成中的消息队列长度，指定为 integer。在仿真中，消息队列始终为 1，且无法调整。为确保捕获每条消息，请使用更小的模型步长，或者仅在 `IsNew` 返回 `1` 时执行模型。

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

从 ROS 网络接收消息

Subscribe 模块创建一个 Simulink® 非虚拟总线，与指定的 ROS 消息类型对应。该模块使用 Simulink 模型的节点为特定话题创建 ROS 订阅者。此节点在模型运行时创建，并在模型终止时删除。如果模型没有节点，该模块会创建一个节点。

在每个仿真步中，该模块检查特定话题上是否有新消息可用。如果有新消息可用，该模块会检索该消息并将其转换为 Simulink 总线信号。**Msg** 端口输出此新消息。如果没有新消息可用，**Msg** 输出最后接收到的 ROS 消息。如果自仿真开始以来尚未接收到消息，**Msg** 输出一条空白消息。
