---
type: simulink-block
title: 'Monitor Action Goal'
family: 'ros-2'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'monitoractiongoalros2'
documentation_source_path: 'ref/monitoractiongoalros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Monitor Action Goal

## 端口

### Input

### **UUID** — 专用于任何目标消息的唯一 ID，非虚拟总线

专用于任何目标消息的唯一 ID，指定为消息类型 `unique_identifier_msgs/UUID` 的非虚拟总线。

**数据类型：** `bus`
### Output

### **StatusCode** — 对应于 `UUID` 输入的动作目标执行状态，标量

对应于 **UUID** 输入的动作目标的执行状态，指定为整数。

| 错误代码 | 条件 |
| --- | --- |
| `-1` | 动作服务器拒绝了该目标。 |
| `0` | 动作服务器接受了该目标，但未能正确设置状态。这表示目标消息的 `unknown` 状态。 |
| `1` | 动作服务器接受了该目标并正在等待执行。这表示目标消息的 `accepted` 状态。 |
| `2` | 动作服务器接受了该目标并且当前正在执行过程中。这表示已接受目标消息的 `executing` 状态。 |
| `3` | 动作服务器已接受动作客户端发起的取消目标请求。这表示已接受目标消息的 `canceling` 状态。 |
| `4` | 动作服务器成功完成了该目标。这表示已接受目标消息的 `succeeded` 状态。 |
| `5` | 动作服务器基于动作客户端发送的外部请求取消了该目标。这表示已接受目标消息的 `canceled` 状态。 |
| `6` | 动作服务器在没有动作客户端发送外部请求的情况下终止了该目标。这表示已接受目标消息的 `aborted` 状态。 |

**数据类型：** `int8`

### **Result** — 与特定动作目标关联的结果消息，非虚拟总线

与特定动作目标关联的结果消息，指定为非虚拟总线。

**数据类型：** `bus`

### **Feedback** — 与特定动作目标关联的反馈消息，非虚拟总线

与特定动作目标关联的反馈消息，指定为非虚拟总线。

- 当在特定时间步有反馈消息可用时，**Feedback** 端口输出最新反馈。
- 当在特定时间步没有反馈消息可用时，**Feedback** 端口输出最后已知反馈。

#### 依赖关系

当选中 **Show Feedback output port** 时，启用此输出。

**数据类型：** `bus`

### **ErrorCode** — 监视动作目标时的错误条件，整数

监视动作目标时的错误条件，指定为整数。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 动作客户端成功发送了目标，并且动作服务器接受了该目标。 |
| `1` | 动作客户端发送了目标，但动作服务器拒绝了该目标。 |
| `2` | UUID 输入无效，但动作服务器可用。 |
| `3` | 由于动作服务器不可用，动作客户端未能发送目标。 |

#### 依赖关系

当选中 **Show ErrorCode output port** 时，启用此输出。

**数据类型：** `uint8`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，从 **Prepare** 库中选择 **Property Inspector**。

### **Name** — 从配对的 `Send Action Goal` 模块继承的动作名称，字符向量

从配对的 `Send Action Goal` 模块继承的动作名称，指定为字符向量。

### **Type** — 从配对的 `Send Action Goal` 模块继承的动作类型，字符向量

从配对的 `Send Action Goal` 模块继承的动作类型，指定为字符向量。

### **Paired Send Action Goal Block** — 配对的 Send Action Goal 模块的路径，模块路径

与此 Monitor Action Goal 模块配对的 Send Action Goal 模块的路径。要首次创建配对的 Send Action Goal，请点击 **Create paired Send Action Goal block**。

创建配对的 Send Action Goal 模块后，点击该路径会显示并高亮模型中的 Send Action Goal 模块。

#### 提示

- 为了实现正确的动作客户端，请仅使用 **Create paired Send Action Goal block** 来创建与此 Monitor Action Goal 模块关联的 Send Action Goal。不建议从库中添加 Send Action Goal 模块。

### **Show Feedback output port** — 启用反馈输出端口 `off`（默认）| `on`

选中此框以启用 **Feedback** 输出。

### **Show ErrorCode output port** — 启用错误代码输出端口 `off`（默认）| `on`

选中此框以启用 **ErrorCode** 输出。如果发生错误条件，**Result** 端口会输出空白消息。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

Monitor Action Goal 模块遵循基于速率的执行，而不是事件驱动执行。

## 版本历史

**在 R2024a 中引入**

## 描述

在 ROS 2 网络中监视动作目标

Monitor Action Goal 模块使您能够在 ROS 2 网络中监视活动动作目标的状态、反馈和结果。此模块接受 UUID 输入，形式为 `unique_identifier_msgs/UUID` 消息类型的 Simulink 非虚拟总线。

要使用此模块，您必须有一个配对的 Send Action Goal 模块，且动作名称和类型匹配。在 Send Action Goal 模块中所做的选择会自动与 Monitor Action Goal 模块同步。

您可以使用此模块监视动作目标被动作服务器接受后的这些状态。

ROS 2 动作客户端监视目标状态
