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

### **Goal** — ROS 2 动作目标消息输入 non-virtual bus

ROS 2 动作目标消息输入，指定为 non-virtual bus。

**数据类型：** `bus`

### **Enable** — 如果当前没有正在运行的目标，则用于发送动作目标的 Boolean 值 `true` | `false`

如果当前没有正在运行的目标，则用于发送动作目标的 Boolean 值，指定为 `1 (true)` 或 `0 (false)`。如果当前没有正在运行的目标且 **Enable** 端口为 `true`，该模块会发送 **Goal** 输入处可用的任何目标消息。要检查是否有目标正在运行，请使用配对 Monitor Action Goal 模块的 **StatusCode** 输出。

**数据类型：** `Boolean`
### 输出

### **UUID** — 专用于任何目标消息的唯一 ID non-virtual bus

专用于任何目标消息的唯一 ID，指定为消息类型为 `unique_identifier_msgs/UUID` 的 non-virtual bus。

**数据类型：** `bus`

### **ErrorCode** — 发送动作目标请求的错误条件 integer

对应于发送动作目标请求的错误条件，指定为 integer。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 动作客户端成功发送目标，并且动作服务器接受了该目标。 |
| `1` | 动作客户端发送了目标，但动作服务器拒绝了该目标。 |
| `2` | 动作客户端未能发送目标，但动作服务器可用。 |
| `3` | 动作客户端未能发送目标，因为动作服务器不可用。 |

#### 依赖项

当选中 **Show ErrorCode output port** 时，启用此输出。

**数据类型：** `uint8`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡中，从 **Prepare** 库中选择 **Property Inspector**。

### 主

### **Source** — 用于指定动作名称的源 `Select from ROS network` | `Specify your own`

用于指定动作名称的源：

- `Select from ROS network` — 使用 **Select...** 从支持的 ROS 2 动作完整列表中选择动作名称和类型。**Name** 和 **Type** 参数会自动设置。您必须连接到 ROS 2 网络。
- `Specify your own` — 在 **Name** 中输入动作名称，并在 **Type** 中指定其类型。您必须完全匹配动作名称。

### **Name** — ROS 2 动作名称 character vector

ROS 2 动作名称，指定为 character vector。动作名称必须与 ROS 2 网络上可用的名称匹配。

### **Type** — ROS 2 动作类型 character vector

ROS 2 动作类型，指定为 character vector。每个动作名称都有对应的动作类型。

### **Paired Monitor Action Goal Block** — 配对 Monitor Action Goal 模块的路径 模块路径

与此 Send Action Goal 模块配对的 Monitor Action Goal 模块的路径。要首次创建配对的 Monitor Action Goal，请点击 **Create paired Monitor Action Goal block**。

创建配对的 Monitor Action Goal 模块后，点击该路径会显示并高亮模型中的 Monitor Action Goal 模块。

#### 提示

为实现正确的动作客户端，请仅使用 **Create paired Monitor Action Goal block** 创建与此 Send Action Goal 模块关联的 Monitor Action Goal。不建议从库中添加 Monitor Action Goal 模块。

### **Show ErrorCode output port** — 启用错误代码输出端口 `off` (默认) | `on`

选中此框以启用 **ErrorCode** 输出。

### QoS

用于与动作服务器建立通信的动作客户端的服务质量 (QoS) 设置，返回为 character vector。您可以使用以下选项设置 **Goal Service QoS**、**Result Service QoS**、**Cancel Service QoS**、**Feedback Topic QoS** 和 **Status QoS**：

### **History** — 在队列中存储目标请求的模式 `Keep last` (默认) | `Keep all`

确定在队列中存储发送目标请求的模式。如果队列中填满了等待处理的请求，则会丢弃旧请求以便为新请求腾出空间。如果设置为 `Keep last`，队列会存储由 `Depth` 参数设置的请求数量。如果设置为 `Keep all`，队列会存储所有请求，直到达到 MATLAB® 资源限制。

### **Depth** — 目标请求队列的大小 `1` (默认) | `non-negative scalar integer`

目标请求队列的大小，指定为 `non-negative scalar integer`。这仅在 `History` 设置为 `Keep last` 时适用。

### **Reliability** — 目标请求的传递保证 `Reliable` (默认) | `Best effort`

对目标请求传递保证的要求，指定为 `Reliable` 或 `Best effort`。如果为 `Reliable`，则保证传递，但可能重试多次。如果为 `Best effort`，则尝试传递且不重试。对于动作，建议使用 `Reliable` 设置。

### **Durability** — 动作目标请求的持久性 `Volatile` (默认) | `Transient local`

对动作目标请求持久性的要求，指定为 `Volatile` 或 `Transient local`。如果为 `Volatile`，则不要求请求持久存在。如果为 `Transient local`，则服务器将要求客户端持久保存由 `Depth` 指定的最近请求。建议使用 `Volatile` 设置，以防止服务器在重启时收到过期请求。

### **Deadline** — 接收目标请求和发送目标结果之间允许的最大时间量 `Inf` (默认) | positive scalar

接收目标请求和发送目标结果之间允许的最大时间量，指定为 positive scalar。发送目标请求的动作客户端的 `Deadline` QoS 参数必须大于或等于动作服务器 `Deadline` QoS 参数的值。默认值为 `Inf`，这意味着后续消息之间的预期间隔为无限大。

### **Lifespan** — 目标请求被视为有效的时长 `Inf` (默认) | positive scalar

目标请求被视为有效的时长，指定为 positive scalar。该模块不会处理在队列中持续存在时间超过指定 lifespan 的目标请求。默认值为 `Inf`，这意味着目标请求在无限长的时间内有效。

### **Liveliness** — 动作客户端对动作服务器的活跃性检查 `automatic` (默认)

动作客户端对动作服务器的活跃性检查，指定为 `automatic`。此参数用于衡量动作服务器是否仍处于活动状态。

`Liveliness` 设置为 `automatic` 意味着，在动作服务器已向动作客户端发送目标响应后，客户端认为服务器在额外的 `Lease Duration` 内仍处于活动状态。

### **Lease Duration** — 动作客户端必须断言活跃性之前的最大时间量 `Inf` (默认) | positive scalar

动作客户端必须断言活跃性之前的最大时间量，指定为 positive scalar。发送目标请求的动作客户端的 `Lease Duration` QoS 参数必须大于或等于动作服务器 `Lease Duration` QoS 参数的值。默认值为 `Inf`，这意味着动作客户端可以在无限长的时间内断言其活跃性。

### QoS 兼容性注意事项

**注意**

要使连接建立，动作服务器和动作客户端之间的服务质量 (QoS) 设置必须兼容。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

由 Send Action Goal 生成的动作客户端遵循基于速率的执行，而不是事件驱动的执行。

## 版本历史

**在 R2024a 中引入**

## 描述

将动作目标消息发送到 ROS 2 网络

Send Action Goal 模块使您能够将动作目标消息发送到 ROS 2 网络中可用的动作服务器。它接受一个 Simulink non-virtual bus 作为其 **Goal** 输入，该输入对应于指定的 ROS 2 动作类型。

要创建 ROS 2 动作客户端，请创建一个 class 设置为 `Action Goal` 的 ROS 2 Blank Message 模块。此模块的输出连接到 Send Action Goal 模块的 **Goal** 输入。动作客户端与 Simulink® 模型的节点相关联。

**注意**

要监视活动的动作目标，您必须首先创建一个配对的 Monitor Action Goal 模块。配对模块将基于 Send Action Goal 模块中指定的动作参数。

### 行为

在每个仿真步中，Send Action Goal 模块会检查当前是否有目标正在进行（活动目标），从而产生以下可能的结果或情况之一：

- 如果为 true，该模块会忽略 **Goal** 输入处可用的任何目标消息，并将活动目标的 UUID 输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink non-virtual bus。
- 如果当前没有正在运行的目标且 **Enable** 端口为 `true`，该模块会发送 **Goal** 输入处可用的任何目标消息，并将新目标的 UUID 输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink non-virtual bus。
- 如果当前没有正在运行的目标且 **Enable** 端口为 `false`，该模块会忽略 **Goal** 输入处可用的任何目标消息，并将默认目标 UUID（空消息）输出为 `unique_identifier_msgs/UUID` 消息类型的 Simulink non-virtual bus。

ROS 2 Action Client 模块行为
