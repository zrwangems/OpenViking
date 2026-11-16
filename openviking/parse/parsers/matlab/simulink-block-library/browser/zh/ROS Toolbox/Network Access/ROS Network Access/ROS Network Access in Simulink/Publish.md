---
type: simulink-block
title: 'Publish'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in MATLAB'
documentation_page: 'publish'
documentation_source_path: 'ref/publish.html'
language: zh-CN
chinese_source: worker-translation
---

# Publish

## 端口

### 输入

### **Msg** — ROS 消息非虚拟总线

ROS 消息，指定为非虚拟总线。要指定 ROS 消息的类型，请使用 **Message type** 参数。

**数据类型：** `bus`

## 参数

### **Topic source** — 用于指定话题名称的来源 `Select from ROS network` | `Specify your own`

用于指定话题名称的来源，指定为下列之一：

- `Select from ROS network`
  — 使用 **Select** 选择话题名称。**Topic** 和 **Message type** 参数会自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Topic** 中输入话题名称，并在 **Message type** 中指定其消息类型。必须精确匹配话题名称。

### **Topic** — 要发布到的话题名称 string

要发布到的话题名称，指定为 string。当 **Topic source** 设置为 `Select from ROS network` 时，使用 **Select** 从 ROS 网络中选择话题。您必须连接到 ROS 网络才能获取话题列表。否则，将 **Topic source** 设置为 `Specify your own`，并指定所需的话题。

### **Message type** — ROS 消息类型 string

ROS 消息类型，指定为 string。使用 **Select** 从支持的 ROS 消息完整列表中选择。不支持服务消息类型，且列表中不包含这些类型。

### **Length of publish queue** — 消息队列长度 `1`（默认） | integer

代码生成中的消息队列长度，指定为 integer。在仿真中，消息队列始终为 1，且无法调整。为确保处理每条消息，请使用更小的模型步长，或仅在发布新消息时执行模型。

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

将消息发送到 ROS 网络

Publish 模块将对应于指定 ROS 消息类型的 Simulink® 非虚拟总线作为输入，并将其发布到 ROS 网络。它使用 Simulink 模型的节点为特定话题创建 ROS 发布者。此节点在模型运行时创建，并在模型终止时删除。如果模型没有节点，该模块会创建一个节点。

在每次采样命中时，该模块将 **Msg** 输入从 Simulink 总线信号转换为 ROS 消息并发布它。该模块不区分输入是否为新消息，而只是在每次采样命中时发布它。对于仿真，此输入是 MATLAB® ROS 消息。在代码生成中，它是 C++ ROS 消息。
