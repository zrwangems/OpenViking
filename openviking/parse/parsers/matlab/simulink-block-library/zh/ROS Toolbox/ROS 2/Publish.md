---
type: simulink-block
title: 'Publish'
family: 'ros-2'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'publishros2'
documentation_source_path: 'ref/publishros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Publish

## 端口

### 输入

### **Msg** — ROS message non-virtual bus

ROS 消息，指定为非虚拟总线。要指定 ROS 消息的类型，请使用 **Message type** 参数。

**数据类型：** `bus`

## 参数

#### 主要

### **Topic source** — 用于指定主题名称的源 `Select from ROS network` | `Specify your own`

用于指定主题名称的源，指定为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择主题名称。**Topic** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Topic** 中输入主题名称，并在 **Message type** 中指定其消息类型。您必须完全匹配主题名称。

### **Topic** — 要发布到的主题名称 string

要发布到的主题名称，指定为 string。当 **Topic source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择主题。您必须连接到 ROS 2 网络才能获取主题列表。否则，将 **Topic source** 设置为 `Specify your own` 并指定您想要的主题。

### **Message type** — ROS 消息类型 string

ROS 消息类型，指定为 string。使用 **Select** 从支持的 ROS 消息完整列表中选择。不支持服务消息类型，并且它们不包括在列表中。

#### 服务质量 (QoS)

### **History** — 队列中存储消息的模式 `Keep last`（默认） | `Keep all`

确定队列中存储消息的模式。排队的消息将发送给稍后加入的订阅者。如果队列中填满了等待处理的消息，则会丢弃旧消息以便为新消息腾出空间。如果设置为 `'keeplast'`，队列存储由 `Depth` 参数设置的消息数量。如果设置为 `'keepall'`，队列存储所有消息，直到达到 MATLAB 资源限制。

### **Depth** — 消息队列的大小 `1`（默认） | 正标量

当 `History` 设置为 `Keep last` 时，消息队列中存储的消息数量。

### **Reliability** — 消息的传递保证 `Reliable`（默认） | `Best effort`

影响消息传递的保证。如果为 `Reliable`，则保证传递，但可能会重试多次。如果为 `Best effort`，则尝试传递且不重试。

### **Durability** — 消息的持久性 `Volatile`（默认） | `Transient local`

影响发布者中消息的持久性，这允许稍后加入的订阅者接收由 `Depth` 指定的旧消息数量。如果为 `Volatile`，则消息不会持久化。如果为 `Transient local`，则发布者将持久化最近的消息。

### **Deadline** — 发布连续消息之间的预期间隔 `Inf`（默认） | 正标量

定义将连续消息发布到主题的预期间隔，指定为正标量。它设置消息之间允许的持续时间。

默认值为 `Inf`，这意味着消息可以在无限长的时间内发布和接收，而不会被视为过期。如果 `Lifespan` 设置为 5，则表示消息在发布后 5 秒内被视为有效。如果订阅者在该时间范围内未收到消息，则该消息被视为过期。

### **Lifespan** — 发布和接收之间的消息有效窗口 `Inf`（默认） | 正标量

定义从发布到接收消息之间的最大持续时间，而不将消息视为陈旧或过期，指定为正标量。已过期的消息将被静默丢弃。

默认值为 `Inf`，这意味着消息可以在无限长的时间内发布和接收，而不会被视为过期。如果 `Lifespan` 设置为 5，则表示消息在发布后 5 秒内被视为有效。如果订阅者在该时间范围内未收到消息，则该消息被视为过期。

### **Liveliness** — 发布者活跃性断言协议 `"automatic"`（默认）

定义发布者将提供的报告级别，以通知订阅者它们仍然活跃，指定为 string。

`Liveliness` QoS 策略设置为 `"automatic"` 意味着当发布者在该时间范围内发布消息时，会在额外的 `Lease Duration` 内保持活跃状态。

### **Lease Duration** — 活跃性断言之间的最大时间窗口 `Inf`（默认） | 正标量

定义在系统认为发布者已失去活跃性之前，允许发布者证明其活跃性的最大持续时间，指定为正标量。失去活跃性可以作为故障的指示。

默认值为 `Inf`，这意味着发布者可以在无限长的时间内断言其活跃性。如果 `Lease Duration` 设置为 5，则意味着发布者最多有 5 秒的时间来证明其活跃性。如果发布者在该时间范围内未发送任何消息或明确断言其活跃性，则被视为已失去活跃性。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

将消息发送到 ROS 2 网络

Publish 模块将 Simulink® 非虚拟总线作为其输入，该总线对应于指定的 ROS 2 消息类型，并将其发布到 ROS 2 网络。它使用 Simulink 模型的节点为特定主题创建 ROS 2 发布者。该节点在模型运行时创建，并在模型终止时删除。如果模型没有节点，则该模块会创建一个。

在每个采样命中时，该模块将 **Msg** 输入从 Simulink 总线信号转换为 ROS 2 消息并发布。该模块不区分输入是否为新消息，而是在每个采样命中时发布它。对于仿真，此输入是 MATLAB® ROS 2 消息。在代码生成中，它是 C++ ROS 2 消息。

与不同 QoS 策略相关的服务质量 (QoS) 事件会为 Publish 模块触发默认警告。有关不同 QoS 事件及分别触发的警告的详细信息，请参阅 Manage Quality of Service Policies in ROS 2 示例中的 **QoS Events** 部分。
