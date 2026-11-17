---
type: simulink-block
title: 'Receive Service Request'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'receiveservicerequestros2'
documentation_source_path: 'ref/receiveservicerequestros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Receive Service Request

## 端口

### 输出

### **IsNew** — 新服务请求指示符 `0` | `1`

新服务请求指示符，以逻辑值形式返回。如果输出为 `1`，则表示自上次采样命中以来收到了新的服务请求。您可以使用此输出来触发子系统，以处理 ROS 2 网络中收到的新消息。

**数据类型：** `Boolean`

### **Req** — 服务请求消息非虚拟总线

服务请求消息，以对应于服务请求类型的非虚拟总线形式返回。服务请求消息类型取决于 **Service Type** 参数中指定的服务类型。

**数据类型：** `bus`

### **DefaultResp** — 默认响应消息非虚拟总线

默认响应消息，以对应于默认响应消息类型的非虚拟总线形式返回。

#### 依赖关系

- 要启用此输出端口，请选择 **Show Default Response output port** 参数。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

#### 主要

### **Name** — 服务名称 字符向量

服务名称，指定为字符向量。这是服务服务器的名称，客户端随后可以使用该名称进行连接并发送服务请求。

### **Type** — 服务类型 字符向量

服务类型，指定为字符向量。每个服务名称都有对应的类型。点击 **Select** 按钮可从支持的 ROS 2 服务类型的完整列表中进行选择。

如果您使用的是自定义服务类型，请先使用 `ros2genmsg` 函数构建关联的服务定义。然后，您可以使用 **Select** 按钮指定您的自定义服务类型。

### **Paired Send Response Block** — 配对的 Send Service Response 模块的路径 模块路径

与此 Receive Service Request 模块配对的 Send Service Response 模块的路径。要首次创建配对的 Send Service Response，请点击 `Create paired Send Response block`。

创建配对的 Send Service Response 模块后，点击该路径将显示并高亮您模型中的 Send Service Response 模块。

#### 提示

- 为了正确实现服务服务器，请仅使用 `Click to create paired Send Response block` 来创建与此 Receive Service Request 模块关联的 Send Service Response。不要从库中添加 Send Service Response 模块。

### **Sample time** — 输出之间的间隔 `–1`（默认）| 标量

输出之间的间隔，指定为标量。在仿真中，采样时间遵循仿真时间，而不是实际的挂钟时间。

此默认值表示模块采样时间为*继承*。

有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。

### **Show Default Response output port** — 启用默认响应输出端口 `on`（默认）| `off`

选中此框以启用 **DefaultResp** 输出。

#### 服务质量 (QoS)

### **History** — 在队列中存储请求的模式 `Keep last`（默认）| `Keep all`

确定在队列中存储请求的模式。如果队列中填满了等待处理的请求，则旧请求将被丢弃，以便为新请求腾出空间。如果设置为 `Keep last`，队列存储由 `Depth` 参数设置的请求数量。如果设置为 `Keep all`，队列存储所有请求，直至达到 MATLAB® 资源限制。

### **Depth** — 请求队列的大小 `1`（默认）| `non-negative scalar integer`

请求队列的大小，以队列中存储的请求数量表示，指定为 `non-negative scalar integer`。这仅在 `History` 设置为 `Keep last` 时适用。

### **Reliability** — 请求的投递保证 `Reliable`（默认）| `Best effort`

对请求和响应的投递保证的要求，指定为 `Reliable` 或 `Best effort`。如果为 `Reliable`，则保证投递，但可能会重试多次。如果为 `Best effort`，则尝试投递且不重试。对于服务，建议使用 `Reliable` 设置。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

### **Durability** — 请求的持久性 `Volatile`（默认）| `Transient local`

对客户端持久性的要求，指定为 `Volatile` 或 `Transient local`。如果为 `Volatile`，则不要求请求持久化。如果为 `Transient local`，则服务端将要求客户端持久化并接收由 `Depth` 指定的先前请求数量的响应。建议使用 `Volatile` 设置，以防止在服务端重启时服务端接收到过期请求。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

### **Deadline** — 接收服务请求与发送响应之间允许的最大时间量 `Inf`（默认）| 正标量

接收服务请求与发送响应之间允许的最大时间量，指定为正标量。向该模块发送请求的服务客户端的 `Deadline` QoS 参数必须大于或等于此参数的值。

默认值为 `Inf`，这意味着在服务服务端接收到服务请求后，它可以在向该请求发送响应之前等待无限长的时间。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

### **Lifespan** — 服务请求被视为有效的时间长度 `Inf`（默认）| 正标量

服务请求被视为有效的时间长度，指定为正标量。该模块不处理在队列中持续时间超过指定 lifespan 的服务请求。

默认值为 `Inf`，这意味着服务服务端接收到的服务请求被视为在无限长的时间内有效。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

### **Liveliness** — 该模块提供的以及期望从服务客户端获得的活跃性报告级别 `automatic`（默认）

该模块提供的以及期望从所连接的服务客户端获得的活跃性报告级别，指定为 `automatic`。

Liveliness 设置为 `automatic` 意味着，在该模块从所连接的客户端接收到服务请求后，该模块认为该客户端在另一个 `Lease Duration` 内仍然存活。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

### **Lease Duration** — 所连接的服务客户端必须在此之前声明活跃性的最大时间量 `Inf`（默认）| 正标量

所连接的服务客户端必须在此之前声明活跃性的最大时间量，指定为正标量。

默认值为 `Inf`，这意味着连接到服务端的服务客户端可以在无限长的时间内声明活跃性。

**注意**

服务质量设置必须在服务服务端和客户端之间兼容，才能建立连接。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 生成的服务服务端遵循基于速率的执行，而不是事件驱动的执行。

## 版本历史

**在 R2024a 中引入**

## 描述

从 ROS 2 网络接收服务请求

在同一模型中使用 Receive Service Request 和 Send Service Response 模块，在 Simulink® 中实现 ROS 2 服务服务器。Receive Service Request 模块使您能够从服务客户端接收 ROS 2 服务请求消息，在模型中处理它以构造适当的响应，然后使用 Send Service Response 模块将响应发送回客户端。该服务服务器与 Simulink 模型的 ROS 2 节点相关联。

在每个仿真步中，Receive Service Request 模块检查客户端是否发送了新的服务请求。如果有新的服务请求可用，该模块会检索它并输出一个与服务请求消息类型对应的非虚拟总线。如果该模块在某个时间步未收到服务请求，则输出上次收到的服务请求消息。

在模块掩码中指定 ROS 2 服务的名称、服务类型以及服务质量（QoS）参数。此模块的 QoS 参数必须与服务客户端兼容，以便接收请求并发送响应。

**注意**

对于添加到模型中的每个 Receive Service Request，您必须在模块掩码中点击 **Click to create paired Send Response block**，以创建配对的 Send Service Response 模块。不要从库中添加 Send Service Response 模块。
