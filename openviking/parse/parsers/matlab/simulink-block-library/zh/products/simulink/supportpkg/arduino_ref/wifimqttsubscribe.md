---
type: simulink-block
title: 'WiFi MQTT Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifimqttsubscribe'
documentation_source_path: 'supportpkg/arduino_ref/wifimqttsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi MQTT Subscribe

## 端口

### 输出

### **isNew** — 新消息指示 `0`（默认）| `1`

如果客户端自上一个采样时间以来收到新消息，则该模块输出 `1`。否则，该模块输出 `0`。

**数据类型：** `Boolean`

### **message** — 从 MQTT broker 接收的消息标量

该模块将从 MQTT broker 接收的消息输出为 ASCII 字符数组。

**数据类型：** `uint8`

### **topic** — 消息的主题 `topic/level/#`

该模块输出与接收消息的主题名称对应的 ASCII 值。例如，如果接收消息的主题是 `model/data`，则该端口输出主题为 `109 111 100 101 108 47 100 97 116 97`。

要将 ASCII 值转换为其字母数字等效形式，请将 ASCII to String 模块连接到 **topic** 端口的输出。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 Topics in MQTT。

#### 依赖项

要启用此端口，请在 **Topic** 参数中包含通配符条目。有关 MQTT 中通配符的更多信息，请参阅 Wildcards in MQTT Topics。

**数据类型：** `uint8`

## 参数

### **Topic** — 用于订阅的主题 `channels/<channelID>/subscribe`（默认）| 任何有效主题名

指定客户端订阅的主题。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 Topics in MQTT。

### **Data length** — 从 MQTT broker 读取的数据长度 `10`（默认）| `positive integer`

指定每个采样时间要接收的数据长度。

### **Print diagnostic messages** — 在串行端口上打印 MQTT broker 响应 `off`（默认）| `on`

选择此选项可在每个发布请求时在 Arduino 串行端口上打印来自 MQTT broker 的响应。

### **Sample time** — 检查来自 MQTT broker 的消息的频率 `1`（默认）| `-1` | 任何正整数

指定客户端检查来自 broker 的新消息的频率。当您将采样时间指定为 `-1` 时，该模块根据模型中模块的上下文继承其采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从消息队列遥测传输 (MQTT) broker 接收消息

使用 WiFi MQTT Subscribe 模块在指定主题上从消息队列遥测传输 (MQTT) broker 接收消息。

**注意**

WiFi MQTT Subscribe 模块仅支持通过 TCP/IP 套接字的 MQTT。

WiFi MQTT Subscribe 模块支持以下硬件板。

- Arduino MKR WiFi 1010
- Arduino MKR 1000
- Arduino Nano 33 IoT
- Arduino® compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
