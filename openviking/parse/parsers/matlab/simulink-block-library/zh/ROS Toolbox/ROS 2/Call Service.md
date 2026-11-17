---
type: simulink-block
title: 'Call Service'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'callserviceros2'
documentation_source_path: 'ref/callserviceros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Call Service

## 端口

### 输入

### **Req** — 请求消息 非虚拟总线

请求消息，指定为非虚拟总线。请求消息类型对应于您的服务类型。要生成一个空请求消息总线以填充数据，请使用 Blank Message 模块。

**数据类型：** `bus`
### 输出

### **Resp** — 响应消息 非虚拟总线

响应消息，返回为非虚拟总线。响应基于输入 **Req** 消息。响应消息类型对应于您的服务类型。要生成一个空响应消息总线以填充数据，请使用 Blank Message 模块。

**数据类型：** `bus`

### **ErrorCode** — 服务调用的错误条件 整数

服务调用的错误条件，指定为整数。每个整数对应于服务连接的不同错误条件或服务调用的状态。如果发生错误条件，**Resp** 输出最后一条响应消息，如果之前未收到响应，则输出空消息。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 服务响应已成功检索，并可在 `Resp` 输出中获取。 |
| `1` | 在指定的 `Connection timeout` 内未建立连接。 |
| `2` | 未收到来自服务器的响应。 |

#### 依赖关系

当 **Show ErrorCode output port** 复选框为 `on` 时，此输出启用。

**数据类型：** `uint8`

## 参数

#### 主要

### **Source** — 指定服务名称的来源 `Select from ROS network` | `Specify your own`

指定服务名称的来源：

- `Select from ROS network` — 使用 **Select** 选择服务名称。**Name** 和 **Type** 参数会自动设置。您必须连接到 ROS 2 网络。
- `Specify your own` — 在 **Name** 中输入服务名称，并在 **Type** 中指定其服务类型。您必须精确匹配服务名称。

### **Name** — 服务名称 字符向量

服务名称，指定为字符向量。服务名称必须与 ROS 服务服务器上可用的服务名称匹配。要查看 ROS 2 网络中的有效服务列表，请参阅 `ros2`。

### **Type** — 服务类型 字符向量

服务类型，指定为字符向量。每个服务名称都有对应的类型。

### **Connection timeout** — 服务服务器连接超时 `5`（默认）| 正数值标量

服务服务器连接超时，指定为正数值标量，单位为秒。如果在此时间内无法与 ROS 服务服务器建立连接，则 **ErrorCode** 输出 `1`。

### **Show ErrorCode output port** — 启用错误代码输出端口 `on`（默认）| `off`

选中此复选框以输出 **ErrorCode** 输出。如果发生错误条件，**Resp** 输出最后一条响应消息，如果之前未收到响应，则输出空消息。

#### 服务质量 (QoS)

### **History** — 队列中存储请求的模式 `Keep last`（默认）| `Keep all`

确定队列中存储请求的模式。如果队列中填满了等待处理的请求，则旧请求将被丢弃以腾出空间给新请求。如果设置为 `Keep last`，队列存储由 `Depth` 参数设置的请求数量。如果设置为 `Keep all`，队列存储所有请求，直至达到 MATLAB 资源限制。

### **Depth** — 请求队列的大小 `1`（默认）| 正标量

当 `History` 设置为 `Keep last` 时，请求队列中存储的请求数量。

### **Reliability** — 请求的传递保证 `Reliable`（默认）| `Best effort`

影响请求传递的保证。如果为 `Reliable`，则保证传递，但可能重试多次。如果为 `Best effort`，则尝试传递且不重试。对于服务，推荐使用 `Reliable` 设置。

### **Durability** — 请求的持久性 `Volatile`（默认）| `Transient local`

影响请求的持久性，允许延迟启动的服务器接收由 `Depth` 指定的旧请求数量。如果为 `Volatile`，则请求不会持久化。如果为 `Transient local`，则该模块将持久化最近的请求。

### **Deadline** — 发送服务请求与接收响应之间允许的最大时间量 `Inf`（默认）| 正标量

发送服务请求与接收响应之间允许的最大时间量，指定为正标量。从该模块接收请求的服务服务器的 `Deadline` QoS 参数必须小于或等于此参数的值。

默认值为 `Inf`，这意味着服务客户端发送请求后，可以在无限长的时间内等待接收该请求的响应。

**注意**

服务质量设置必须在服务服务器和客户端之间兼容，才能建立连接。

### **Lifespan** — 服务请求被视为有效的时间长度 `Inf`（默认）| 正标量

服务请求被视为有效的时间长度，指定为正标量。此值决定发送的服务请求在队列中存储的时间。

默认值为 `Inf`，这意味着服务客户端发送的服务请求在无限长的时间内被视为有效。

**注意**

服务质量设置必须在服务服务器和客户端之间兼容，才能建立连接。

### **Liveliness** — 该模块提供的以及期望从服务服务器获得的活跃性报告级别 `automatic`（默认）

该模块提供的以及期望从所连接的服务服务器获得的活跃性报告级别，指定为 `automatic`。

Liveliness 设置为 `automatic` 意味着，在该模块从所连接的服务器接收到服务响应后，该模块认为该服务器在另一个 `Lease Duration` 内仍然存活。

**注意**

服务质量设置必须在服务服务器和客户端之间兼容，才能建立连接。

### **Lease Duration** — 所连接的服务服务器必须断言活跃性之前的最长时间量 `Inf`（默认）| 正标量

所连接的服务服务器必须断言活跃性之前的最长时间量，指定为正标量。

默认值为 `Inf`，这意味着连接到客户端的服务服务器可以在无限长的时间内断言活跃性。

**注意**

服务质量设置必须在服务服务器和客户端之间兼容，才能建立连接。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

在 ROS 2 网络中调用服务

使用 Call Service 模块在 Simulink® 中实现 ROS 2 服务客户端。Call Service 模块接收 ROS 2 服务请求消息，将其发送到 ROS 2 服务服务器，并等待响应。在使用此模块之前，应在网络上的某处设置 ROS 2 服务服务器。通过执行 `ros2 service list` 命令检查 ROS 2 网络上的可用服务，该命令使用 `ros2` 函数。使用 `ros2svcserver` 在 MATLAB® 中设置服务服务器。

在模块掩码中指定 ROS 2 服务的名称和服务类型。如果连接到 ROS 2 网络，可以从可用服务列表中选择。可以使用 Blank Message 模块创建空白服务请求或响应消息，以便用数据填充。

始终在模块掩码中指定服务质量（QoS）参数。此模块的 QoS 参数必须与服务服务器兼容，才能发送请求和接收响应。
