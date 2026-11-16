---
type: simulink-block
title: 'Blank Message'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Connection and Exploration'
documentation_page: 'blankmessageros2'
documentation_source_path: 'ref/blankmessageros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Blank Message

## 端口

### 输出

### **Msg** — 空白 ROS 2 消息非虚拟总线

空白 ROS 2 消息，以非虚拟总线形式返回。要指定 ROS 消息的类型，请使用 **Type** 参数。总线的所有元素都初始化为 0。可变长度数组的长度也初始化为 `0`。

**数据类型：** `bus`

## 参数

### **Class** — ROS 2 消息的类 `Message`（默认） | `Service Request` | `Service Response` | `Action Goal` | `Action Feedback` | `Action Result`

ROS 2 消息的类，指定为 `Message`、`Service Request`、`Service Response`、`Action Goal`、`Action Feedback` 和 `Action Result`。

对于基本的发布和订阅，请使用 `Message` 类。要为 Call Service 输入创建服务请求消息，请使用 `Service Request` 类。要为 Send Action Goal 的 **Goal** 输入创建动作目标消息，请使用 `Action Goal` 类。您可以分别使用 `Action Feedback` 或 `Action Result` 类来创建特定类型的动作反馈消息或动作结果消息。

### **Message type** — ROS 2 消息类型 `'geometry_msgs/Point'`（默认） | 字符向量 | 对话框选择

ROS 2 消息类型，指定为字符向量或对话框选择。使用 **Select** 从支持的 ROS 消息列表中选择。给出的消息列表取决于您选择的 **Class**。

### **Sample time** — 输出之间的间隔 `Inf`（默认） | 正数值标量

输出之间的间隔，指定为数值标量。默认值表示模块输出永不改变。使用此值可消除重新计算模块输出的需要，从而加快仿真。否则，模块在 **Sample time** 的每个间隔输出一个新的空白消息。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用指定的消息类型创建空白 ROS 2 消息

Blank Message 模块创建一个与选定 ROS 消息类型对应的 Simulink® 非虚拟总线。该模块创建可与 Publish、Subscribe、Call Service 和 Send Action Goal 模块一起使用的 ROS 消息总线。
