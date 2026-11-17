---
type: simulink-block
title: 'Subscribe'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'subscriberos2'
documentation_source_path: 'ref/subscriberos2.html'
language: zh-CN
chinese_source: worker-translation
---

# Subscribe

## 端口
```yaml
ports:
- name: IsNew
  summary: 新消息指示符 0 | 1
  direction: output
- name: Msg
  summary: ROS 2 消息非虚拟总线
  direction: output
  data_types: bus
```

### 输出

### **IsNew** — 新消息指示符 `0` | `1`

新消息指示符，以逻辑值形式返回。如果输出为 `1`，则表示自上次采样命中以来收到了新消息。此输出可用于触发子系统，以处理在 ROS 2 网络中收到的新消息。

### **Msg** — ROS 2 消息非虚拟总线

ROS 2 消息，以非虚拟总线形式返回。ROS 消息的类型在 **Message type** 参数中指定。Subscribe ROS 2 模块在收到您指定的主题名称上的消息之前，会输出空白消息。这些空白消息允许您在网络的其余部分设置完成之前创建并测试完整模型。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Topic source
  summary: 用于指定主题名称的来源 Select from ROS network | Specify your own
  group: ''
- name: Topic
  summary: 要订阅的主题名称 string
  group: ''
- name: Message type
  summary: ROS 2 消息类型 string
  group: ''
- name: Sample time
  summary: 输出之间的间隔 –1 (默认) | scalar
  group: ''
- name: History
  summary: 在队列中存储消息的模式 Keep last (默认) | Keep all
  group: ''
- name: Depth
  summary: 消息队列的大小 10 (默认) | positive scalar
  group: ''
- name: Reliability
  summary: 消息的传递保证 Reliable (默认) | Best effort
  group: ''
- name: Durability
  summary: 消息的持久性 Volatile (默认) | Transient local
  group: ''
- name: Deadline
  summary: 连续消息接收之间的预期间隔 Inf（默认）| 正标量
  group: ''
- name: Lifespan
  summary: 发布与接收之间的消息有效窗口 Inf（默认）| 正标量
  group: ''
- name: Liveliness
  summary: 发布者存活断言协议 "automatic"（默认）
  group: ''
- name: Lease Duration
  summary: 存活断言之间的最大时间窗口 Inf（默认）| 正标量
  group: ''
```

#### 主

### **Topic source** — 用于指定主题名称的来源 `Select from ROS network` | `Specify your own`

用于指定主题名称的来源，指定为以下之一：

- `Select from ROS network`
  — 使用 **Select** 选择主题名称。**Topic** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Topic** 中输入主题名称，并在 **Message type** 中指定其消息类型。您必须完全匹配主题名称。

### **Topic** — 要订阅的主题名称 string

要订阅的主题名称，指定为字符串。当 **Topic source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择主题。您必须连接到 ROS 2 网络才能获取主题列表。否则，将 **Topic source** 设置为 `Specify your own` 并指定您想要的主题。

### **Message type** — ROS 2 消息类型 string

ROS 2 消息类型，指定为字符串。使用 **Select** 从受支持的 ROS 2 消息完整列表中进行选择。不支持服务消息类型，并且不会包含在列表中。

### **Sample time** — 输出之间的间隔 `–1` (默认) | scalar

输出之间的间隔，指定为标量。在仿真中，采样时间遵循仿真时间，而不是实际挂钟时间。

此默认值表示模块采样时间为*继承*。

有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

#### 服务质量 (QoS)

### **History** — 在队列中存储消息的模式 `Keep last` (默认) | `Keep all`

确定在队列中存储消息的模式。排队的消息将发送给稍后加入的订阅者。如果队列中填满了等待处理的消息，则旧消息将被丢弃，以便为新消息腾出空间。当设置为 `Keep last` 时，队列存储由 `Depth` 属性设置的消息数量。否则，当设置为 `Keep all` 时，队列会存储所有消息，直至达到 MATLAB® 资源限制。

### **Depth** — 消息队列的大小 `10` (默认) | positive scalar

当 `History` 设置为 `Keep last` 时，消息队列中存储的消息数量。

### **Reliability** — 消息的传递保证 `Reliable` (默认) | `Best effort`

影响消息传递的保证。如果为 `Reliable`，则保证传递，但可能会重试多次。如果为 `Best effort`，则尝试传递并且不重试。

### **Durability** — 消息的持久性 `Volatile` (默认) | `Transient local`

影响发布者中消息的持久性，这允许稍后加入的订阅者接收由 `Depth` 指定的旧消息数量。如果为 `Volatile`，则消息不会持久存在。如果为 `Transient local`，则发布者将保留最近的消息。

### **Deadline** — 连续消息接收之间的预期间隔 `Inf`（默认）| 正标量

概述订阅者接收消息之间允许的持续时间，指定为正标量。如果消息未在截止时间内收到，客户端应用程序会收到通知。

默认值为 `Inf`，这意味着后续消息接收之间的预期间隔为无限大。如果将 `Deadline` 设置为 `3`，则确保订阅者在订阅前一条消息后 3 秒内订阅发布到该主题的每一条后续消息。

### **Lifespan** — 发布与接收之间的消息有效窗口 `Inf`（默认）| 正标量

定义消息被视为有效的持续时间，超过该时间后订阅者将不会收到该消息，指定为正标量。已过期的消息会被静默丢弃。

默认值为 `Inf`，这意味着消息被视为有效，并且订阅者可在无限持续时间内接收该消息。如果将 `Lifespan` 设置为 5，则表示消息在发布后 5 秒内被视为有效。如果订阅者未在该时间范围内收到消息，则该消息被视为已过期。

### **Liveliness** — 发布者存活断言协议 `"automatic"`（默认）

确定订阅的发布者所期望的报告标准，指定为字符串。

`Liveliness` 设置为 `"automatic"` 意味着当任一发布者发布了消息时，系统将认为该节点的所有发布者在额外的 `Lease Duration` 内仍然存活。

### **Lease Duration** — 存活断言之间的最大时间窗口 `Inf`（默认）| 正标量

定义订阅者期望发布者证明其存活的最长持续时间，超过该时间后系统将认为其已失去存活状态，指定为正标量。失去存活状态可作为故障的指示。

默认值为 `Inf`，这意味着发布者可以在无限时间段内断言其存活状态。如果将 `Lease Duration` 设置为 5，则表示订阅者可以期望发布者在最多 5 秒内证明其存活状态。如果发布者未在该时间范围内发送任何消息或明确断言其存活状态，则被视为已失去存活状态。
## 所属库

ROS Toolbox / ROS 2

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2025a：`Depth` QoS 设置默认值变更

从 R2025a 开始，ROS 2 Subscribe 模块参数中 `Depth` QoS 设置的默认值为 `10`。您可以增大 `Depth` 值以最小化消息丢弃，或将其设置为 `1` 以在 Simulink 生成的代码中处理最新消息。

## 描述

从 ROS 2 网络接收消息

Subscribe 模块创建一个与指定 ROS 2 消息类型对应的 Simulink® 非虚拟总线。该模块使用 Simulink 模型的节点为特定主题创建 ROS 2 订阅者。该节点在模型运行时创建，在模型终止时删除。如果模型没有节点，该模块将创建一个节点。

在每个仿真步中，该模块检查特定主题上是否有新消息可用。如果有新消息可用，该模块将检索该消息并将其转换为 Simulink 总线信号。**Msg** 端口输出此新消息。如果没有新消息可用，**Msg** 输出最后接收到的 ROS 2 消息。如果自仿真开始以来未接收到任何消息，**Msg** 输出一条空白消息。

与不同 QoS 策略相关的服务质量 (QoS) 事件会触发 Subscribe 模块的默认警告。有关不同 QoS 事件及各自触发的警告的详细信息，请参阅 Manage Quality of Service Policies in ROS 2 示例中的 **QoS Events** 部分。
