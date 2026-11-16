---
type: simulink-block
title: 'Blank Message'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Connection and Exploration'
documentation_page: 'blankmessage'
documentation_source_path: 'ref/blankmessage.html'
language: zh-CN
chinese_source: worker-translation
---

# Blank Message

## 端口

### 输出

### **Msg** — 空白 ROS 消息非虚拟总线

空白 ROS 消息，返回为非虚拟总线。要指定 ROS 消息的类型，请使用 **Type** 参数。总线的所有元素都初始化为 0。可变长度数组的长度也初始化为 0。

**数据类型：** `bus`

## 参数

### **Class** — ROS 消息的类 `Message`（默认） | `Service Request` | `Service Response`

ROS 消息的类，指定为 `Message`、`Service Request` 或 `Service Response`。对于基本发布和订阅，请使用 `Message` 类。

### **Type** — ROS 消息类型 `'geometry_msgs/Point'`（默认） | 字符向量 | 对话框选择

ROS 消息类型，指定为字符向量或对话框选择。使用 **Select** 从支持的 ROS 消息列表中选择。给出的消息列表取决于所选消息的 **Class**。

### **Sample time** — 输出之间的间隔 `Inf`（默认） | 数值标量

输出之间的间隔，指定为数值标量。默认值表示模块输出从不变化。使用此值可通过消除重新计算模块输出的需要来加速仿真。否则，模块在 **Sample time** 的每个间隔输出一条新的空白消息。

有关详细信息，请参阅指定采样时间 (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用指定的消息类型创建空白消息

Blank Message 模块创建一个与所选 ROS 消息类型对应的 Simulink® 非虚拟总线。该模块创建可与 Publish、Subscribe 或 Call Service 模块配合使用的 ROS 消息总线。在每个采样命中时，该模块会为指定的消息类型输出一个空白或“零”信号。总线的所有元素都初始化为 0。可变长度数组的长度也初始化为 0。
