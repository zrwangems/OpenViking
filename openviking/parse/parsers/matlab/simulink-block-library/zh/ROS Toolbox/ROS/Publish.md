---
type: simulink-block
title: 'Publish'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'publish'
documentation_source_path: 'ref/publish.html'
language: zh-CN
chinese_source: worker-translation
---

# Publish

## 端口
```yaml
ports:
- name: Msg
  summary: ROS 消息非虚拟总线
  direction: input
  data_types: bus
```

### 输入

### **Msg** — ROS 消息非虚拟总线

ROS 消息，指定为非虚拟总线。要指定 ROS 消息的类型，请使用 **Message type** 参数。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Topic source
  summary: 指定主题名称的来源 Select from ROS network | Specify your own
  group: ''
- name: Topic
  summary: 要发布到的主题名称 string
  group: ''
- name: Message type
  summary: ROS 消息类型 string
  group: ''
- name: Length of publish queue
  summary: 消息队列长度 1（默认） | integer
  group: ''
```

### **Topic source** — 指定主题名称的来源 `Select from ROS network` | `Specify your own`

指定主题名称的来源，可指定为以下选项之一：

- `Select from ROS network`
  — 使用 **Select** 选择主题名称。**Topic** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Topic** 中输入主题名称，并在 **Message type** 中指定其消息类型。主题名称必须完全匹配。

### **Topic** — 要发布到的主题名称 string

要发布到的主题名称，指定为字符串。当 **Topic source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择一个主题。必须连接到 ROS 网络才能获取主题列表。否则，将 **Topic source** 设置为 `Specify your own`，并指定所需的主题。

### **Message type** — ROS 消息类型 string

ROS 消息类型，指定为字符串。使用 **Select** 从受支持的 ROS 消息的完整列表中进行选择。不支持服务消息类型，列表中也不包含这些类型。

### **Length of publish queue** — 消息队列长度 `1`（默认） | integer

代码生成中的消息队列长度，指定为整数。在仿真中，消息队列始终为 1，无法调整。为确保处理每条消息，请使用较小的模型步长，或仅在发布新消息时执行模型。
## 所属库

ROS Toolbox / ROS

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

向 ROS 网络发送消息

Publish 模块接收一个 Simulink® 非虚拟总线作为输入，该总线对应于指定的 ROS 消息类型，并将对应的消息发布到 ROS 网络。它使用 Simulink 模型的节点，为特定主题创建 ROS 发布者。该节点在模型运行时创建，并在模型终止时删除。如果模型没有节点，该模块会创建一个节点。

在每次采样命中时，模块将 **Msg** 输入从 Simulink 总线信号转换为 ROS 消息并发布。该模块不会判断输入是否为新消息，而只是在每次采样命中时将其发布。对于仿真，此输入为 MATLAB® ROS 消息。在代码生成中，此输入为 C++ ROS 消息。
