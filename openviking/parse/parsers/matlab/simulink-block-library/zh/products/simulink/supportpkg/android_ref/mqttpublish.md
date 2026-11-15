---
type: simulink-block
title: 'MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'mqttpublish'
documentation_source_path: 'supportpkg/android_ref/mqttpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Publish

## 端口

### 输入

### **message** — 要发布的消息（标量）

将希望发布者发布到 MQTT broker 的消息指定为 `uint8` 类型的 ASCII 字符数组。

**数据类型：** `uint8`

## 参数

### **Broker Service** — MQTT broker 服务提供商 `ThingSpeak`（默认） | `Other`

选择接收、筛选并向客户端发送消息的 MQTT broker 服务提供商。

- `ThingSpeak` — 指定此选项时，对您的通道的 MQTT 访问由 ThingSpeak™ MQTT broker 处理。要创建 MQTT 设备，请按照创建 ThingSpeak MQTT 设备 (ThingSpeak) 中的步骤操作
- `Other` — 当对您的通道的 MQTT 访问由其他 MQTT 公共 broker（例如 HiveMQ®、Mosquitto™ 等）处理时，指定此选项。

配置与 MQTT 属性中相同的 MQTT broker 属性。

### **Topic** — MQTT broker 的路由信息 `channels/<channelID>/publish`（默认） | 任何有效的主题名称

指定发布者用于筛选消息的主题。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 MQTT 中的主题。

### **Quality of Service** — 服务质量级别 `0`（默认） | `1` | `2`

服务质量 (QoS) 定义了 MQTT 中消息传递过程的可靠性。MQTT 为消息传递提供三个 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT broker 可能不支持全部三个 QoS 级别。例如，ThingSpeak MQTT 仅支持 QoS 0。

从下拉菜单中选择 QoS 级别：

- `0` — 发布者向 MQTT broker 发送一次消息。broker 不发送接收确认。
- `1` — 发布者向 MQTT broker 至少发送一次消息。如果发布者未收到来自 broker 的确认，则重新发送消息。
- `2` — 发布者向 MQTT broker 恰好发送一次消息。发布者和 broker 交换确认，以确保消息仅接收一次。

### **Retain Message** — 向新订阅者发送消息的选项 `off`（默认） | `on`

控制 MQTT broker 如何处理新订阅。

- `on` — 当对某个主题进行新订阅时，broker 会在其数据库中识别主题名称匹配的消息，并立即发送该消息。

  **注意**

  MQTT broker 仅保留与指定主题相关的最后一条已发布消息。
- `off` — 当对某个主题进行新订阅时，订阅者必须等待发布者发送下一条消息。

#### 依赖项

要启用此参数，请将 **Broker Service** 设置为 `Other`。

### **Update interval (seconds)** — 发布消息的速率 `60`（默认） | 标量

输入向 MQTT broker 发布消息的时间间隔，单位为 seconds。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

使用指定的 Topic 将消息发布到 MQTT broker

使用 MQTT Publish 模块将消息从您的发布者（硬件）发布到 MQTT broker，主题为您在 **Topic** 参数中指定的主题。
