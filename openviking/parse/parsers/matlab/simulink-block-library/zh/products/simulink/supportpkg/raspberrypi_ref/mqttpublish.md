---
type: simulink-block
title: 'MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'mqttpublish'
documentation_source_path: 'supportpkg/raspberrypi_ref/mqttpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Publish

## 端口

### 输入

### **Message** — 要发布的消息向量

指定您希望发布者向 MQTT 代理发布的消息，表示为 `uint8` 类型的 ASCII 字符数组。

**示例：** `[0,3]`

**数据类型：** `uint8`
### 输出

### **Status** — 来自 MQTT 代理的状态代码标量

MQTT 代理响应发布请求而发出的状态代码。如果代理接受要发布的消息，则该端口输出 `0`。
任何非零输出都表示代理已拒绝该消息。消息可能因各种原因被拒绝，例如用户名或密码不正确，或协议版本不可接受。有关 MQTT 代理状态代码的详细信息，请参阅 MQTT 状态代码。

**数据类型：** `int8`

## 参数

### **Topic** — 消息的主题 `topic/level`（默认）| 任何有效主题名称

指定要发布消息的主题。一个主题最多可以包含 128 个字符。有关主题及其结构的信息，请参阅 MQTT 中的主题。

### **QoS** — QoS 级别 `0`（默认）| `1` | `2`

服务质量 (QoS) 定义了 MQTT 中消息传递过程的可靠性。MQTT 为消息传递提供了三个 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT 代理可能不支持全部三个 QoS 级别。例如，ThingSpeak™ MQTT 仅支持 QoS 0。

从列表中选择一个 QoS 级别：

- `0`：发布者将消息发送到 MQTT 代理一次。代理不发送接收确认。
- `1`：发布者将消息发送到 MQTT 代理至少一次。如果发布者未收到来自代理的确认，则会重新发送消息。
- `2`：发布者将消息发送到 MQTT 代理恰好一次。发布者和代理交换确认，以确保消息仅被接收一次。

有关 QoS 级别的详细信息，请参阅 MQTT 中的 QoS 级别。

### **Retain message** — 向新订阅者发送消息的选项 `off`（默认）| `on`

**Retain message** 参数控制如何处理新订阅：

- `on` –– 当对某个主题进行新订阅时，代理会在其数据库中识别主题名称匹配的消息，并立即发送该消息。

  **注意**

  MQTT 代理仅保留在某个主题上发布的最后一条已知消息。
- `off` –– 当对某个主题进行新订阅时，订阅者必须等待发布者发送下一条消息。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

在指定主题上向 MQTT 代理发布消息

MQTT Publish 模块将来自您的硬件（发布者）的消息发布到指定主题上的消息队列遥测传输 (MQTT) 代理。

该模块具有 **Message** 输入端口和 **Status** 输出端口。**Message** 端口接受要发布到代理的消息。**Status** 端口输出发布请求的状态。模块图标上的字符串 **topic/level** 由 **Topic** 参数指定。

有关 MQTT 的详细信息，请参阅发布 MQTT 消息并订阅消息主题。

**注意**

MQTT Publish 模块仅支持通过 TCP/IP 套接字使用 MQTT。
