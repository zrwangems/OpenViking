---
type: simulink-block
title: 'WiFi MQTT Publish'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifimqttpublish'
documentation_source_path: 'supportpkg/arduino_ref/wifimqttpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi MQTT Publish

## 端口

### 输入

### **message** — 要发布的消息 标量

指定您希望发布者发布到 MQTT broker 的消息，形式为 `uint8` 类型的 ASCII 字符数组。

**数据类型：** `uint8`
### 输出

### **status** — 来自 MQTT broker 的状态代码 `0` | `1`

该模块输出 MQTT broker 针对发布请求发出的状态代码。如果 broker 接受要发布的消息，则该模块在此端口输出 `1`。当 broker 拒绝该消息时，该模块输出 `0`。broker 可能因各种原因拒绝消息，例如用户名或密码不正确，或者消息要求的协议版本是 broker 无法接受的。

**数据类型：** `int8`

## 参数

### **Broker service** — MQTT broker 服务提供商 `ThingSpeak`（默认）| `Other`

选择接收、筛选消息并向客户端发送消息的 MQTT broker 服务提供商。

- `ThingSpeak` — 指定此选项时，对您通道的 MQTT 访问由 ThingSpeak™ MQTT broker 处理。要创建 MQTT 设备，请按照 Create a ThingSpeak MQTT Device (ThingSpeak) 中的步骤操作。
- `Other` — 当对您通道的 MQTT 访问由其他 MQTT 公共 broker（例如 HiveMQ®、Mosquitto™ 等）处理时，指定此选项。

配置与 MQTT 属性中相同的 MQTT broker 属性。

### **Topic** — MQTT broker 的路由信息 `channels/<channelID>/publish`（默认）| 任何有效的主题名称

指定发布者用于筛选消息的主题。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 Topics in MQTT。

### **Retain message** — 将消息发送给新订阅者的选项 `off`（默认）| `on`

控制 MQTT broker 如何处理新订阅。

- `on` — 当对某个主题进行新订阅时，broker 会在其数据库中识别具有匹配主题名称的消息，并立即发送该消息。

  **注意**

  MQTT broker 仅保留与指定主题相关的最后一条已发布消息。
- `off` — 当对某个主题进行新订阅时，订阅者必须等待发布者发送下一条消息。

#### 依赖关系

要启用此参数，请将 **Broker Service** 设置为 `Other`。

### **Update interval (seconds)** — 发布消息的速率 `60`（默认）| 标量

输入将消息发布到 MQTT broker 的时间间隔（以 seconds 为单位）。

### **Print diagnostic messages** — 在串行端口上打印 MQTT broker 响应 `off`（默认）| `on`

选择此选项可针对每个发布请求在 Arduino 串行端口上打印来自 MQTT broker 的响应。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

将消息发布到消息队列遥测传输 (MQTT) broker

使用 WiFi MQTT Publish 模块，将消息从您的发布者（硬件）发布到 MQTT broker 上您在 **Topic** 参数中指定的主题。

**注意**

WiFi MQTT Publish 模块仅支持通过 TCP/IP 套接字的 MQTT。

WiFi MQTT Publish 模块支持以下硬件板。

- Arduino MKR WiFi 1010
- Arduino MKR 1000
- Arduino Nano 33 IoT
- Arduino® compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
