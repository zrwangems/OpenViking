---
type: simulink-block
title: 'Cancel Action Goal'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'cancelactiongoalros2'
documentation_source_path: 'ref/cancelactiongoalros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Cancel Action Goal

## 端口
```yaml
ports:
- name: UUID
  summary: 专用于任何目标消息的唯一 ID 非虚拟总线
  direction: input
  data_types: bus
- name: Enable
  summary: 用于发送取消活动操作目标请求的布尔值 true 或 1 | false 或 0
  direction: input
  data_types: Boolean
- name: Response
  summary: 取消目标请求的响应消息 非虚拟总线
  direction: output
  data_types: bus
- name: ErrorCode
  summary: 取消操作目标时的错误条件 整数
  direction: output
  data_types: uint8
```

### 输入

### **UUID** — 专用于任何目标消息的唯一 ID 非虚拟总线

专用于任何目标消息的唯一 ID，指定为消息类型为 `unique_identifier_msgs/UUID` 的非虚拟总线。

**数据类型：** `bus`

### **Enable** — 用于发送取消活动操作目标请求的布尔值 `true` 或 `1` | `false` 或 `0`

用于发送取消活动操作目标请求的布尔值，指定为设置为 `true (1)` 或 `false (0)` 的非虚拟总线。如果将 **Enable** 端口设置为 `true`，并且与 **UUID** 输入对应的目标正在运行，则此模块会在同一时间步向操作服务器发送取消目标请求。

**数据类型：** `Boolean`
### 输出

### **Response** — 取消目标请求的响应消息 非虚拟总线

取消目标请求的响应消息，指定为 `action_msgs/CancelGoalResponse` 消息类型的非虚拟总线。如果操作服务器接受取消目标请求，目标将转换为 `canceling` 状态。

**数据类型：** `bus`

### **ErrorCode** — 取消操作目标时的错误条件 整数

取消操作目标时的错误条件，指定为整数。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 操作客户端成功向操作服务器发送了取消目标请求。 |
| `1` | 操作目标无法取消，因为它被拒绝或已处于终止状态。终止状态指以下操作目标状态之一： - 目标处于 `succeeded` 状态。 - 目标处于 `canceled` 状态。 - 目标处于 `aborted` 状态。 |
| `2` | 操作客户端未能发送取消目标请求，但操作服务器可用。 |
| `3` | 操作客户端未能发送取消目标请求，因为操作服务器不可用。 |

#### 依赖关系

当选中 **Show ErrorCode output port** 时，此输出启用。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Show ErrorCode output port
  summary: 启用错误代码输出端口 off（默认）| on
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Show ErrorCode output port** — 启用错误代码输出端口 `off`（默认）| `on`

选中此复选框以启用 **ErrorCode** 输出。如果发生错误条件，**Response** 端口会输出指定为 `action_msgs/CancelGoalResponse` 消息类型的非虚拟总线的空白消息。
## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

Cancel Action Goal 模块遵循基于速率的执行，而非事件驱动的执行。

## 版本历史

**在 R2024a 中引入**

## 描述

取消 ROS 2 网络中的活动操作目标

Cancel Action Goal 模块使您能够取消 ROS 2 网络中的活动操作目标。此模块接受 UUID 输入作为 `unique_identifier_msgs/UUID` 消息类型的 Simulink 非虚拟总线。

**注意**

要使用此模块，您必须至少有一个 Send Action Goal 向此模块提供 UUID 输入。
