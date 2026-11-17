---
type: simulink-block
title: 'Send Action Goal'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'sendactiongoalros2'
documentation_source_path: 'ref/sendactiongoalros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Send Action Goal

## 端口

### 输入

### **Goal** — ROS 2 动作目标消息输入非虚拟总线

ROS 2 动作目标消息输入，指定为非虚拟总线。

**数据类型：** `bus`

### **Enable** — 用于在没有目标运行时发送动作目标的布尔值 `true` | `false`

用于在没有目标运行时发送动作目标的布尔值，指定为 `1 (true)` 或 `0 (false)`。如果没有目标正在运行且 **Enable** 端口为 `true`，该模块会发送 **Goal** 输入处可用的任何目标消息。要检查是否有目标正在运行，请使用配对的 Monitor Action Goal 模块的 **StatusCode** 输出。

**数据类型：** `Boolean`
### 输出

### **UUID** — 专用于任何目标消息的唯一 ID 非虚拟总线

专用于任何目标消息的唯一 ID，指定为消息类型 `unique_identifier_msgs/UUID` 的非虚拟总线。

**数据类型：** `bus`

### **ErrorCode** — 发送动作目标请求的错误条件 整数

对应于发送动作目标请求的错误条件，指定为整数。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 动作客户端成功发送目标，且动作服务器接受了该目标。 |
| `1` | 动作客户端发送了目标，但动作服务器拒绝了该目标。 |
| `2` | 动作客户端未能发送目标，但动作服务器可用。 |
| `3` | 动作客户端未能发送目标，因为动作服务器不可用。 |

#### 依赖关系

当选中 **Show ErrorCode output port** 时，此输出启用。

**数据类型：** `uint8`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Source** — 用于指定动作名称的源 `Select from ROS network` | `Specify your own`

用于指定动作名称的源：

- `Select from ROS network` — 使用 **Select...** 从支持的 ROS 2 动作完整列表中选择动作名称和类型。**Name** 和 **Type** 参数会自动设置。您必须连接到 ROS 2 网络。
- `Specify your own` — 在 **Name** 中输入动作名称，并在 **Type** 中指定其类型。您必须精确匹配动作名称。

### **Name** — ROS 2 动作名称 字符向量

ROS 2 动作名称，指定为字符向量。动作名称必须与 ROS 2 网络上可用的名称匹配。

### **Type** — ROS 2 动作类型 字符向量

ROS 2 动作类型，指定为字符向量。每个动作名称都有对应的动作类型。

### **Paired Monitor Action Goal Block** — 配对 Monitor Action Goal 模块的路径 模块路径

与此 Send Action Goal 模块配对的 Monitor Action Goal 模块的路径。要首次创建配对的 Monitor Action Goal，请点击 **Create paired Monitor Action Goal block**。

创建配对的 Monitor Action Goal 模块后，点击该路径会显示并高亮模型中的 Monitor Action Goal 模块。

#### 提示

为了正确实现动作客户端，请仅使用 **Create paired Monitor Action Goal block** 来创建与此 Send Action Goal 模块关联的 Monitor Action Goal。不建议从库中添加 Monitor Action Goal 模块。

### **Show ErrorCode output port** — 启用错误代码输出端口 `off` (默认) | `on`

选中此框以启用 **ErrorCode** 输出。

### QoS

动作客户端用于与动作服务器建立通信的服务质量 (QoS) 设置，以字符向量形式返回。您可以使用以下选项设置 **Goal Service QoS**、**Result Service QoS**、**Cancel Service QoS**、**Feedback Topic QoS** 和 **Status QoS**：

### **History** — 队列中目标请求的存储模式 `Keep last`（默认）| `Keep all`

确定发送目标请求在队列中的存储模式。如果队列中填满了等待处理的请求，则旧请求将被丢弃，以便为新请求腾出空间。如果设置为 `Keep last`，则队列存储由 `Depth` 参数设置的请求数量。如果设置为 `Keep all`，则队列存储所有请求，直至达到 MATLAB® 资源限制。

### **Depth** — 目标请求队列的大小 `1`（默认）| `non-negative scalar integer`

目标请求队列的大小，指定为 `non-negative scalar integer`。仅当 `History` 设置为 `Keep last` 时适用。

### **Reliability** — 目标请求的投递保证 `Reliable`（默认）| `Best effort`

目标请求的投递保证要求，指定为 `Reliable` 或 `Best effort`。如果为 `Reliable`，则保证投递，但可能重试多次。如果为 `Best effort`，则尝试投递且不重试。对于动作，建议使用 `Reliable` 设置。

### **Durability** — 动作目标请求的持久性 `Volatile`（默认）| `Transient local`

动作目标请求的持久性要求，指定为 `Volatile` 或 `Transient local`。如果为 `Volatile`，则不要求请求持久化。如果为 `Transient local`，则服务器将要求客户端持久化由 `Depth` 指定的最新请求。建议使用 `Volatile` 设置，以防止服务器在重启时接收到过期的请求。

### **Deadline** — 接收目标请求与发送目标结果之间允许的最大时间量 `Inf`（默认）| 正标量

接收目标请求与发送目标结果之间允许的最大时间量，指定为正标量。发送目标请求的动作客户端的 `Deadline` QoS 参数必须大于或等于动作服务器 `Deadline` QoS 参数的值。默认值为 `Inf`，表示后续消息之间的预期间隔为无限大。

### **Lifespan** — 目标请求被视为有效的时间长度 `Inf`（默认）| 正标量

目标请求被视为有效的时间长度，指定为正标量。该模块不处理在队列中持续时间超过指定生命周期的目标请求。默认值为 `Inf`，表示目标请求在无限长的时间内有效。

### **Liveliness** — 动作客户端对动作服务器的活跃性检查 `automatic`（默认）

动作客户端对动作服务器的活跃性检查，指定为 `automatic`。此参数用于衡量动作服务器是否仍然存活。

Liveliness 设置为 `automatic` 表示在动作服务器向动作客户端发送目标响应后，客户端认为服务器在额外的 `Lease Duration` 内仍然存活。

### **Lease Duration** — 动作客户端必须声明活跃性之前的最大时间量 `Inf`（默认）| 正标量

动作客户端必须声明活跃性之前的最大时间量，指定为正标量。发送目标请求的动作客户端的 `Lease Duration` QoS 参数必须大于或等于动作服务器 `Lease Duration` QoS 参数的值。默认值为 `Inf`，表示动作客户端可以在无限长的时间内声明其活跃性。

### QoS 兼容性注意事项

**注意**

服务质量 (QoS) 设置必须在动作服务器和动作客户端之间兼容，才能建立连接。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

从 Send Action Goal 生成的动作客户端遵循基于速率的执行，而非事件驱动的执行。

## 版本历史

**在 R2024a 中引入**

## 描述

向 ROS 2 网络发送动作目标消息

Send Action Goal 模块使您能够向 ROS 2 网络中可用的动作服务器发送动作目标消息。它接收一个 Simulink 非虚拟总线作为其 **Goal** 输入，该输入对应于指定的 ROS 2 动作类型。

要创建 ROS 2 动作客户端，请创建一个 ROS 2 Blank Message 模块，并将 class 设置为 `Action Goal`。该模块的输出连接到 Send Action Goal 模块的 **Goal** 输入。动作客户端与 Simulink® 模型的节点相关联。

**注意**

要监控一个活动的动作目标，您必须首先创建一个配对的 Monitor Action Goal 模块。该配对模块将基于 Send Action Goal 模块中指定的动作参数。

### 行为

在每个仿真步中，Send Action Goal 模块检查当前是否有目标正在进行（活动目标），从而导致以下可能的结果或情况之一：

- 如果为真，该模块忽略 **Goal** 输入处可用的任何目标消息，并将活动目标 UUID 输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink 非虚拟总线。
- 如果没有目标正在运行且 **Enable** 端口为 `true`，该模块发送 **Goal** 输入处可用的任何目标消息，并将新目标 UUID 输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink 非虚拟总线。
- 如果没有目标正在运行且 **Enable** 端口为 `false`，该模块忽略 **Goal** 输入处可用的任何目标消息，并将默认目标 UUID（空消息）输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink 非虚拟总线。

ROS 2 Action Client 模块行为
