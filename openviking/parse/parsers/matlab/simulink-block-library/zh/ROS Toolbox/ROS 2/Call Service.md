---
type: simulink-block
title: 'Call Service'
family: 'ros-2'
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

### **Req** — 请求消息 nonvirtual bus

请求消息，指定为 nonvirtual bus。请求消息类型对应于您的服务类型。要生成一个可用数据填充的空请求消息总线，请使用 Blank Message 模块。

**数据类型：** `bus`
### 输出

### **Resp** — 响应消息 nonvirtual bus

响应消息，以 nonvirtual bus 形式返回。响应基于输入 **Req** 消息。响应消息类型对应于您的服务类型。要生成一个可用数据填充的空响应消息总线，请使用 Blank Message 模块。

**数据类型：** `bus`

### **ErrorCode** — 服务调用的错误条件 integer

服务调用的错误条件，指定为 integer。每个 integer 对应于服务连接的不同错误条件或服务调用的状态。如果发生错误条件，**Resp** 会输出最后一条响应消息；如果之前未收到响应，则输出空消息。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 服务响应已成功获取，并可在 `Resp` 输出中使用。 |
| `1` | 未在指定的 `Connection timeout` 内建立连接。 |
| `2` | 未收到来自服务器的响应。 |

#### 依赖项

当 **Show ErrorCode output port** 复选框为 `on` 时，启用此输出。

**数据类型：** `uint8`

## 参数

#### 主要

### **Source** — 用于指定服务名称的来源 `Select from ROS network` | `Specify your own`

用于指定服务名称的来源：

- `Select from ROS network` — 使用 **Select** 选择服务名称。**Name** 和 **Type** 参数会自动设置。必须连接到 ROS 2 网络。
- `Specify your own` — 在 **Name** 中输入服务名称，并在 **Type** 中指定其服务类型。必须精确匹配服务名称。

### **Name** — 服务名称 character vector

服务名称，指定为 character vector。服务名称必须与 ROS 服务服务器上可用的服务名称匹配。要查看 ROS 2 网络中的有效服务列表，请参阅 `ros2`。

### **Type** — 服务类型 character vector

服务类型，指定为 character vector。每个服务名称都有对应的类型。

### **Connection timeout** — 服务服务器连接超时 `5`（默认）| positive numeric scalar

服务服务器连接超时，指定为 positive numeric scalar，单位为秒。如果在此时间内无法与 ROS 服务服务器建立连接，则 **ErrorCode** 输出 `1`。

### **Show ErrorCode output port** — 启用错误代码输出端口 `on`（默认）| `off`

选中此复选框以输出 **ErrorCode** 输出。如果发生错误条件，**Resp** 会输出最后一条响应消息；如果之前未收到响应，则输出空消息。

#### 服务质量 (QoS)

### **History** — 在队列中存储请求的模式 `Keep last`（默认）| `Keep all`

确定在队列中存储请求的模式。如果队列中填满了等待处理的请求，则会丢弃旧请求，以便为新请求腾出空间。如果设置为 `Keep last`，队列存储由 `Depth` 参数设置的请求数。如果设置为 `Keep all`，队列会存储所有请求，直到达到 MATLAB 资源限制。

### **Depth** — 请求队列大小 `1`（默认）| positive scalar

当 `History` 设置为 `Keep last` 时，请求队列中存储的请求数。

### **Reliability** — 请求的送达保证 `Reliable`（默认）| `Best effort`

影响请求送达的保证。如果为 `Reliable`，则保证送达，但可能会重试多次。如果为 `Best effort`，则尝试送达且不会重试。对于服务，建议使用 `Reliable` 设置。

### **Durability** — 请求的持久性 `Volatile`（默认）| `Transient local`

影响请求的持久性，这允许晚启动的服务器接收由 `Depth` 指定数量的旧请求。如果为 `Volatile`，则请求不会持久存在。如果为 `Transient local`，则模块会持久保留最近的请求。

### **Deadline** — 发送服务请求与接收响应之间允许的最大时间量 `Inf`（默认）| positive scalar

发送服务请求与接收响应之间允许的最大时间量，指定为 positive scalar。从模块接收请求的服务服务器的 `Deadline` QoS 参数必须小于或等于此参数的值。

默认值为 `Inf`，这意味着服务客户端发送请求后，可以在无限长的时间内等待接收对该请求的响应。

**注意**

服务服务器和客户端之间的服务质量设置必须兼容，才能建立连接。

### **Lifespan** — 服务请求被视为有效的时间长度 `Inf`（默认）| positive scalar

服务请求被视为有效的时间长度，指定为 positive scalar。此值确定已发送的服务请求在队列中存储的时间。

默认值为 `Inf`，这意味着服务客户端发送的服务请求在无限长的时间内被视为有效。

**注意**

服务服务器和客户端之间的服务质量设置必须兼容，才能建立连接。

### **Liveliness** — 模块提供的、以及期望从服务服务器获得的 liveliness 报告级别 `automatic`（默认）

模块提供的、以及期望从已连接服务服务器获得的 liveliness 报告级别，指定为 `automatic`。

将 Liveliness 设置为 `automatic` 意味着，在模块从已连接服务器接收到服务响应后，模块会在另一个 `Lease Duration` 期间内认为该服务器处于活动状态。

**注意**

服务服务器和客户端之间的服务质量设置必须兼容，才能建立连接。

### **Lease Duration** — 已连接服务服务器必须断言 liveliness 的最大时间 `Inf`（默认）| positive scalar

已连接服务服务器必须断言 liveliness 的最大时间，指定为 positive scalar。

默认值为 `Inf`，这意味着连接到客户端的服务服务器可以在无限长的时间内断言 liveliness。

**注意**

服务服务器和客户端之间的服务质量设置必须兼容，才能建立连接。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

在 ROS 2 网络中调用服务

使用 Call Service 模块在 Simulink® 中实现 ROS 2 Service 客户端。Call Service 模块接收 ROS 2 服务请求消息，将其发送到 ROS 2 服务服务器，并等待响应。使用此模块之前，应在网络中的某处设置 ROS 2 服务服务器。通过执行 `ros2 service list` 命令检查 ROS 2 网络上可用的服务，该命令使用 `ros2` 函数。使用 `ros2svcserver` 在 MATLAB® 中设置服务服务器。

在模块掩码中指定 ROS 2 服务的名称和服务类型。如果已连接到 ROS 2 网络，可以从可用服务列表中选择。可以使用 Blank Message 模块创建空的服务请求或响应消息，以便用数据填充。

请始终在模块掩码中指定服务质量 (QoS) 参数。此模块的 QoS 参数必须与服务服务器兼容，才能发送请求和接收响应。
